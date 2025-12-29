#!/usr/bin/env python3
"""
Inject legacy anchors into markdown files based on anchors_report.csv

This script reads broken anchors from anchors_doctor.py report and injects them
either into headers (if matching numbered header found) or as HTML anchors at the top.
"""

import csv
import sys
import re
from pathlib import Path
from collections import defaultdict
import argparse


def read_report(path):
    """Read anchors report CSV file"""
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            rows.append(row)
    return rows


def has_explicit_id(content: str, anchor_id: str) -> bool:
    """Check if anchor_id already exists in content"""
    # Check for {#anchor_id}
    if re.search(r'\{#\s*' + re.escape(anchor_id) + r'\s*\}', content):
        return True
    
    # Check for {: #anchor_id }
    if re.search(r'\{:\s*#' + re.escape(anchor_id) + r'\s*\}', content):
        return True
    
    # Check for HTML id="anchor_id"
    if re.search(r'id=["\']' + re.escape(anchor_id) + r'["\']', content):
        return True
    
    return False


def inject_anchor_to_header(content: str, anchor_id: str, header_number: int) -> tuple:
    """
    Try to inject anchor to numbered header.
    Returns (new_content, success)
    """
    lines = content.split('\n')
    pattern1 = rf'^(#{{1,6}})\s+{re.escape(str(header_number))}\)\s+(.+)$'  # N) Title
    pattern2 = rf'^(#{{1,6}})\s+{re.escape(str(header_number))}\.\s+(.+)$'  # N. Title
    
    for i, line in enumerate(lines):
        for pattern in [pattern1, pattern2]:
            match = re.match(pattern, line.strip())
            if match:
                # Check if header already has explicit id
                header_text = match.group(2).strip()
                if not re.search(r'\{#', header_text):
                    # Add {#anchor_id} to header
                    new_line = line.rstrip() + f" {{#{anchor_id}}}"
                    lines[i] = new_line
                    return '\n'.join(lines), True
    
    return content, False


def inject_anchor_at_top(content: str, anchor_id: str) -> str:
    """Inject HTML anchor at the top of file (before first header)"""
    anchor_html = f'<a id="{anchor_id}"></a>'
    
    # Check if already exists
    if has_explicit_id(content, anchor_id):
        return content
    
    # Find first header
    header_pattern = r'^(#{1,6})\s+(.+)$'
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if re.match(header_pattern, line.strip()):
            # Insert anchor before first header
            lines.insert(i, anchor_html)
            return '\n'.join(lines)
    
    # No header found, prepend to file
    return anchor_html + '\n\n' + content


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Inject legacy anchors into markdown files")
    ap.add_argument("--docs", required=True, help="Source directory (docs)")
    ap.add_argument("--report", required=True, help="Anchors report CSV file")
    ap.add_argument("--apply", action="store_true", help="Apply changes")
    args = ap.parse_args()

    docs_dir = Path(args.docs).resolve()
    if not docs_dir.exists():
        print(f"Error: Source directory {docs_dir} does not exist", file=sys.stderr)
        sys.exit(1)
    
    report_file = Path(args.report)
    if not report_file.exists():
        print(f"Error: Report file {args.report} does not exist", file=sys.stderr)
        sys.exit(1)
    
    # Determine build directory: same directory where report file is located
    build_dir = report_file.parent

    rep = read_report(args.report)
    
    # Filter only "Anchor not found" entries with broken_anchor starting with #
    entries = []
    for r in rep:
        status = r.get("status", "").strip()
        broken_anchor = r.get("broken_anchor", "").strip()
        
        if status == "Anchor not found" and broken_anchor.startswith("#"):
            entries.append(r)
    
    if not entries:
        print("No broken anchors to inject")
        return
    
    applied_records = []
    skipped_records = []
    
    for entry in entries:
        source_page_str = entry["page"]
        target_file_str = entry.get("target_file", "").strip()
        broken_anchor = entry.get("broken_anchor", "").strip()
        
        # Extract anchor_id (remove #)
        anchor_id = broken_anchor[1:] if broken_anchor.startswith("#") else broken_anchor
        
        # Determine target file
        source_page = docs_dir / source_page_str
        if not source_page.exists():
            skipped_records.append({
                "target_file": source_page_str,
                "anchor_id": anchor_id,
                "method": "none",
                "result": "skipped",
                "reason": "source_file_not_found"
            })
            continue
        
        if not target_file_str or target_file_str == source_page_str:
            # Inject in source page
            target_page = source_page
        else:
            # Try to resolve target file
            target_page = source_page  # Default fallback
            
            # First try: relative to docs_dir
            target_path = docs_dir / target_file_str
            if target_path.exists() and target_path.is_file() and str(target_path).endswith(".md"):
                target_page = target_path
            else:
                # Second try: relative to source page directory
                try:
                    source_dir = source_page.parent
                    target_path = (source_dir / target_file_str).resolve()
                    
                    try:
                        target_path.relative_to(docs_dir)
                        if target_path.exists() and target_path.is_file() and str(target_path).endswith(".md"):
                            target_page = target_path
                    except ValueError:
                        pass
                except Exception:
                    pass
        
        # Read target file
        try:
            content = target_page.read_text(encoding="utf-8")
        except Exception as e:
            skipped_records.append({
                "target_file": str(target_page.relative_to(docs_dir)),
                "anchor_id": anchor_id,
                "method": "none",
                "result": "skipped",
                "reason": f"read_error: {e}"
            })
            continue
        
        # Check if anchor already exists
        if has_explicit_id(content, anchor_id):
            skipped_records.append({
                "target_file": str(target_page.relative_to(docs_dir)),
                "anchor_id": anchor_id,
                "method": "none",
                "result": "skipped",
                "reason": "already_exists"
            })
            continue
        
        # Try to inject to numbered header
        # Extract number from anchor_id if it starts with digit-number-
        numbered_match = re.match(r'^(\d+)-', anchor_id)
        if numbered_match:
            header_number = int(numbered_match.group(1))
            new_content, success = inject_anchor_to_header(content, anchor_id, header_number)
            if success:
                if args.apply:
                    target_page.write_text(new_content, encoding="utf-8")
                    print(f"Applied to header: {target_page.relative_to(docs_dir)} ({anchor_id})")
                applied_records.append({
                    "target_file": str(target_page.relative_to(docs_dir)),
                    "anchor_id": anchor_id,
                    "method": "heading",
                    "result": "applied"
                })
                continue
        
        # Fallback: inject at top
        new_content = inject_anchor_at_top(content, anchor_id)
        if new_content != content:
            if args.apply:
                target_page.write_text(new_content, encoding="utf-8")
                print(f"Applied at top: {target_page.relative_to(docs_dir)} ({anchor_id})")
            applied_records.append({
                "target_file": str(target_page.relative_to(docs_dir)),
                "anchor_id": anchor_id,
                "method": "top",
                "result": "applied"
            })
        else:
            skipped_records.append({
                "target_file": str(target_page.relative_to(docs_dir)),
                "anchor_id": anchor_id,
                "method": "top",
                "result": "skipped",
                "reason": "no_change"
            })
    
    # Write report to same directory as input report
    report_path = build_dir / "anchors_legacy_applied.csv"
    build_dir.mkdir(exist_ok=True, parents=True)
    
    with open(report_path, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["target_file", "anchor_id", "method", "result", "reason"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for record in applied_records:
            writer.writerow(record)
        
        for record in skipped_records:
            writer.writerow(record)
    
    print(f"\nApplied: {len(applied_records)}")
    print(f"Skipped: {len(skipped_records)}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()

