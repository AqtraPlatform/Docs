#!/usr/bin/env python3
"""
Auto-fix common broken anchor issues from anchors_report.csv
Fixes:
- Directory links → /index.md
- Case-insensitive file matching
- Fuzzy anchor slug matching
"""
import os, re, sys, unicodedata, difflib, argparse, pathlib

def slugify(h):
    """Convert heading text to URL-friendly slug"""
    s = unicodedata.normalize("NFKD", h).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    s = re.sub(r"[\s_-]+", "-", s)
    return s

def headings_slugs(path):
    """Extract all heading slugs from markdown file"""
    slugs = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r'^\s{0,3}#{1,6}\s+(.*)\s*$', line)
                if m:
                    slugs.append(slugify(m.group(1)))
    except Exception:
        pass
    return slugs

def find_case_insensitive(root, target):
    """Find file with case-insensitive matching"""
    target = target.replace("\\", "/")
    parts = [p for p in target.split("/") if p]
    cur = pathlib.Path(root)
    for p in parts:
        cand = None
        try:
            names = {x.name.lower(): x.name for x in cur.iterdir() if x.exists()}
            if p.lower() in names:
                cand = names[p.lower()]
            else:
                if names:
                    key = difflib.get_close_matches(p.lower(), names.keys(), n=1, cutoff=0.8)
                    if key:
                        cand = names[key[0]]
        except (OSError, PermissionError):
            return None
        if not cand:
            return None
        cur = cur / cand
    return str(cur)

def main():
    ap = argparse.ArgumentParser(description='Auto-fix broken anchors from CSV report')
    ap.add_argument("--docs", default="docs", help="Documentation root directory")
    ap.add_argument("--report", default="build/anchors_report.csv", help="Path to anchors report CSV")
    args = ap.parse_args()

    if not os.path.isfile(args.report):
        print("ℹ️  No anchors report found, nothing to fix")
        return 0

    fixes = 0
    with open(args.report, encoding="utf-8") as f:
        lines = f.read().splitlines()
        if len(lines) <= 1:
            print("ℹ️  Empty anchors report")
            return 0
        # Parse CSV (simple split, assumes no commas in values)
        rows = [r.split(",", 2) for r in lines[1:] if r.strip()]

    print(f"🔧 Processing {len(rows)} broken links from report...")

    for file_path, url, error_msg in rows:
        if not url or url.startswith("http"):
            continue
        
        # Split URL into path and anchor
        if "#" in url:
            tpath, anchor = url.split("#", 1)
        else:
            tpath, anchor = url, ""

        # Fix 1: Directory → index.md
        source_dir = os.path.dirname(file_path) if file_path else args.docs
        abs_candidate = os.path.normpath(os.path.join(source_dir, tpath))
        if os.path.isdir(abs_candidate):
            tpath = (tpath.rstrip("/") + "/index.md").lstrip("./")

        # Fix 2: Case-insensitive file matching
        abs2 = os.path.normpath(os.path.join(source_dir, tpath))
        if not os.path.exists(abs2):
            ci = find_case_insensitive(source_dir, tpath)
            if ci:
                tpath = os.path.relpath(ci, source_dir).replace("\\", "/")

        # Fix 3: Fuzzy anchor matching
        if anchor:
            abs3 = os.path.normpath(os.path.join(source_dir, tpath))
            if os.path.exists(abs3) and abs3.endswith('.md'):
                slugs = headings_slugs(abs3)
                want = anchor.strip().lower()
                if want not in slugs and slugs:
                    near = difflib.get_close_matches(want, slugs, n=1, cutoff=0.6)
                    if near:
                        anchor = near[0]

        # Apply fix if URL changed
        old = url
        new = tpath + (("#" + anchor) if anchor else "")
        
        if new != old:
            src = os.path.join(args.docs, file_path) if not file_path.startswith(args.docs) else file_path
            try:
                with open(src, "r", encoding="utf-8") as fh:
                    content = fh.read()
                
                # Replace old URL with new URL
                content_new = content.replace(f"]({old})", f"]({new})")
                
                if content_new != content:
                    with open(src, "w", encoding="utf-8") as fh:
                        fh.write(content_new)
                    fixes += 1
                    print(f"  ✅ {file_path}: {old} → {new}")
            except Exception as e:
                print(f"  ⚠️  Cannot edit {src}: {e}")

    print(f"\n🎉 Auto-fixes applied: {fixes}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

