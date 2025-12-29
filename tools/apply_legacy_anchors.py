#!/usr/bin/env python3
"""
Apply legacy anchors to Markdown files based on anchors_report.csv
"""

import csv
import sys
import re
from pathlib import Path
from collections import defaultdict
import difflib

BEGIN = "<!-- LEGACY-ANCHORS:BEGIN"
END = "<!-- LEGACY-ANCHORS:END -->"

def read_report(path):
    """Read anchors report CSV file"""
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            rows.append(row)
    return rows

def extract_existing_ids(text: str):
    """Extract existing anchor IDs from text"""
    ids = set()
    # Extract from <a id="..."> tags
    ids.update(re.findall(r'id="([^"]+)"', text))
    # Extract from {#custom-id} syntax
    ids.update(re.findall(r'\{#([A-Za-z0-9_.\-]+)\}', text))
    return ids

def generate_stable_ids_for_release_notes(anchors, text):
    """Generate stable IDs for release notes based on version patterns"""
    stable_ids = {}
    
    # Find version headers in the text
    version_headers = re.findall(r'^#+\s+(.+?)\s*$', text, re.MULTILINE)
    
    for anchor in anchors:
        if not anchor:
            continue
            
        # Try to match with version headers
        for header in version_headers:
            if difflib.get_close_matches(anchor, [header], cutoff=0.9):
                # Generate stable ID based on header
                clean_header = re.sub(r'[^\w\s-]', '', header.lower())
                clean_header = re.sub(r'\s+', '-', clean_header)
                
                # Try different patterns
                clean_anchor = re.sub(r'[^\w-]', '', anchor)
                patterns = [
                    f"rel-{clean_header}",
                    f"rel-{clean_header[:20]}",  # Truncate if too long
                    f"rel-{clean_anchor}"
                ]
                
                for pattern in patterns:
                    if pattern not in stable_ids.values():
                        stable_ids[anchor] = pattern
                        break
                break
    
    return stable_ids

def inject_block(text: str, ids, is_release_notes=False):
    """Inject legacy anchors block into text"""
    if not ids:
        return text
    
    # Generate stable IDs for release notes
    if is_release_notes:
        stable_ids = generate_stable_ids_for_release_notes(ids, text)
        # Use stable IDs where available, fallback to original
        final_ids = [stable_ids.get(id, id) for id in ids]
    else:
        final_ids = list(ids)
    
    # Remove duplicates while preserving order
    seen = set()
    final_ids = [id for id in final_ids if id not in seen and not seen.add(id)]
    
    if BEGIN in text and END in text:
        # Replace existing block
        return re.sub(
            rf"{re.escape(BEGIN)}[\s\S]*?{re.escape(END)}",
            build_block(final_ids), text, flags=re.MULTILINE
        )
    
    # Insert after first H1 if present
    m = re.search(r"^# .*$", text, flags=re.MULTILINE)
    if m:
        insert_at = m.end()
        return text[:insert_at] + "\n\n" + build_block(final_ids) + "\n" + text[insert_at:]
    
    # Else prepend
    return build_block(final_ids) + "\n\n" + text

def build_block(ids):
    """Build the legacy anchors HTML block"""
    if not ids:
        return ""
    
    anchors = "\n".join(f'<a id="{i}"></a>' for i in sorted(ids))
    return f"{BEGIN} (auto-generated; do not edit) -->\n<div hidden>\n{anchors}\n</div>\n{END}"

def is_safe_anchor(anchor):
    """Check if anchor contains only safe characters"""
    return bool(re.fullmatch(r"[A-Za-z0-9_.\-]+", anchor))

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Apply legacy anchors to Markdown files")
    ap.add_argument("--src", required=True, help="Source directory")
    ap.add_argument("--report", required=True, help="Anchors report CSV file")
    ap.add_argument("--apply", action="store_true", help="Apply changes")
    args = ap.parse_args()

    src = Path(args.src)
    if not src.exists():
        print(f"Error: Source directory {src} does not exist")
        sys.exit(1)
    
    if not Path(args.report).exists():
        print(f"Error: Report file {args.report} does not exist")
        sys.exit(1)

    rep = read_report(args.report)
    per_file = defaultdict(set)
    skipped_anchors = []

    # Group anchors by target file (determine correct file for injection)
    for r in rep:
        source_page_str = r["page"]
        source_page = src / source_page_str
        if not str(source_page).endswith(".md"): 
            continue
        
        anchor = r.get("broken_anchor", "").strip()
        if not anchor:
            continue
            
        # Remove # prefix if present
        if anchor.startswith("#"):
            anchor = anchor[1:]
        
        # Check if anchor is safe
        if not is_safe_anchor(anchor):
            skipped_anchors.append({
                "page": source_page_str,
                "anchor": anchor,
                "reason": "unsafe_characters"
            })
            continue
        
        # Determine target file for anchor injection
        target_file_str = r.get("target_file", "").strip()
        
        if not target_file_str:
            # No target_file specified -> inject in source page
            target_page = source_page
        elif target_file_str == source_page_str:
            # Link to current file -> inject in source page
            target_page = source_page
        else:
            # Inter-page link -> resolve target file path
            target_page = source_page  # Default fallback
            
            try:
                # First try: target_file_str might already be relative to src/
                target_path = src / target_file_str
                if target_path.exists() and target_path.is_file() and str(target_path).endswith(".md"):
                    target_page = target_path
                else:
                    # Second try: resolve path relative to source page directory
                    source_dir = source_page.parent
                    # Normalize path (handle ../)
                    try:
                        target_path = (source_dir / target_file_str).resolve()
                        
                        # Check if target_path exists and is within src directory
                        try:
                            target_path.relative_to(src)
                            if target_path.exists() and target_path.is_file() and str(target_path).endswith(".md"):
                                target_page = target_path
                        except ValueError:
                            # Path is outside src -> keep fallback (source_page)
                            pass
                    except Exception:
                        # Error resolving relative path -> keep fallback (source_page)
                        pass
            except Exception:
                # Any error -> keep fallback (source_page)
                pass
            
        per_file[target_page].add(anchor)

    modified = 0
    applied_anchors = []

    for target_page, ids in per_file.items():
        if not target_page.exists():
            print(f"Warning: File {target_page} does not exist")
            continue
            
        try:
            text = target_page.read_text(encoding="utf-8")
            existing = extract_existing_ids(text)
            new_ids = [i for i in ids if i not in existing]
            
            if not new_ids:
                continue
                
            is_release_notes = target_page.name == "release-notes.md"
            new_text = inject_block(text, set(existing) | set(new_ids), is_release_notes)
            
            if new_text != text:
                if args.apply:
                    target_page.write_text(new_text, encoding="utf-8")
                    modified += 1
                    print(f"Modified: {target_page.relative_to(src)}")
                
                for anchor in new_ids:
                    applied_anchors.append({
                        "page": str(target_page.relative_to(src)),
                        "anchor": anchor,
                        "status": "applied"
                    })
        except Exception as e:
            print(f"Error processing {target_page}: {e}")

    # Write applied anchors report
    if applied_anchors or skipped_anchors:
        report_path = src.parent / "build" / "anchors_applied.csv"
        report_path.parent.mkdir(exist_ok=True)
        
        with open(report_path, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["page", "anchor", "status", "reason"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for anchor in applied_anchors:
                writer.writerow(anchor)
            
            for anchor in skipped_anchors:
                writer.writerow(anchor)

    print(f"Modified files: {modified}")
    print(f"Applied anchors: {len(applied_anchors)}")
    print(f"Skipped anchors: {len(skipped_anchors)}")

if __name__ == "__main__":
    main()
