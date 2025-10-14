#!/usr/bin/env python3
"""
Remove standalone <br> tags and collapse extra blank lines in App Development docs.

Usage:
    python tools/strip_br_app_dev.py --dry-run  # Preview changes
    python tools/strip_br_app_dev.py --apply    # Apply changes
"""

import argparse
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Tuple, List


def is_fence_delimiter(line: str) -> bool:
    """Check if line is a code fence delimiter (``` or ~~~)."""
    stripped = line.strip()
    return stripped.startswith('```') or stripped.startswith('~~~')


def process_file(file_path: Path, apply: bool = False) -> Tuple[int, int]:
    """
    Process a single markdown file.
    
    Returns:
        (removed_br_count, collapsed_blank_count)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    processed_lines: List[str] = []
    removed_br = 0
    collapsed_blank = 0
    in_code_block = False
    prev_was_blank = False
    
    br_pattern = re.compile(r'^\s*<br\s*/?>\s*$')
    
    for line in lines:
        # Check for code fence
        if is_fence_delimiter(line):
            in_code_block = not in_code_block
            processed_lines.append(line)
            prev_was_blank = False
            continue
        
        # If inside code block, preserve everything
        if in_code_block:
            processed_lines.append(line)
            prev_was_blank = False
            continue
        
        # Check if line is standalone <br>
        if br_pattern.match(line):
            removed_br += 1
            continue
        
        # Check if line is blank
        is_blank = line.strip() == ''
        
        if is_blank:
            if prev_was_blank:
                # This is 2+ consecutive blank line, collapse it
                collapsed_blank += 1
                continue
            else:
                # First blank line, keep it
                processed_lines.append(line)
                prev_was_blank = True
        else:
            # Non-blank line
            processed_lines.append(line)
            prev_was_blank = False
    
    # Apply changes if requested
    if apply and (removed_br > 0 or collapsed_blank > 0):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(processed_lines)
    
    return removed_br, collapsed_blank


def find_app_dev_files(docs_dir: Path) -> List[Path]:
    """Find all markdown files in docs/app-development/."""
    app_dev_dir = docs_dir / 'app-development'
    if not app_dev_dir.exists():
        return []
    
    return sorted(app_dev_dir.rglob('*.md'))


def create_report(results: Dict[Path, Tuple[int, int]], docs_dir: Path, apply: bool):
    """Create cleanup report."""
    report_path = Path('APP_DEV_SPACING_CLEANUP.md')
    
    total_files = len([r for r in results.values() if r[0] > 0 or r[1] > 0])
    total_br = sum(r[0] for r in results.values())
    total_blank = sum(r[1] for r in results.values())
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mode = "APPLIED" if apply else "DRY RUN"
    
    report = f"""# App Development Spacing Cleanup Report

**Date:** {timestamp}  
**Mode:** {mode}  
**Target:** `docs/app-development/**/*.md`

## Summary

- **Files processed:** {len(results)}
- **Files modified:** {total_files}
- **Standalone `<br>` removed:** {total_br}
- **Extra blank lines collapsed:** {total_blank}

## Changes by File

| File | Removed `<br>` | Collapsed Blanks |
|------|----------------|------------------|
"""
    
    for file_path, (removed_br, collapsed_blank) in sorted(results.items()):
        if removed_br > 0 or collapsed_blank > 0:
            rel_path = file_path.relative_to(docs_dir.parent)
            report += f"| `{rel_path}` | {removed_br} | {collapsed_blank} |\n"
    
    if total_files == 0:
        report += "| _(no changes needed)_ | 0 | 0 |\n"
    
    report += f"""
## Details

### Removed Elements

- Standalone lines matching: `^\\s*<br\\s*/?>\\s*$`
- Only outside of code blocks (` ``` ` or `~~~` fences)

### Collapsed Blank Lines

- Sequences of 2+ consecutive blank lines reduced to 1
- Only outside of code blocks

### Verification

```bash
# Check for remaining standalone <br>
rg -n '^\\s*<br\\s*/?>\\s*$' docs/app-development

# Verify build
mkdocs build --strict
```

---

**Status:** {'✅ APPLIED' if apply else '📋 DRY RUN - No files modified'}
"""
    
    if apply:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n✅ Report saved to: {report_path}")
    
    return report


def main():
    parser = argparse.ArgumentParser(
        description='Remove standalone <br> tags and collapse blank lines in App Development docs'
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Apply changes (default is dry-run)'
    )
    parser.add_argument(
        '--docs-dir',
        type=Path,
        default=Path('docs'),
        help='Path to docs directory (default: docs)'
    )
    
    args = parser.parse_args()
    
    docs_dir = args.docs_dir
    if not docs_dir.exists():
        print(f"❌ Error: docs directory not found: {docs_dir}")
        return 1
    
    # Find all markdown files in app-development
    files = find_app_dev_files(docs_dir)
    
    if not files:
        print("❌ No markdown files found in docs/app-development/")
        return 1
    
    print(f"🔍 Found {len(files)} markdown files in docs/app-development/")
    print(f"📋 Mode: {'APPLY' if args.apply else 'DRY RUN'}")
    print()
    
    # Process files
    results: Dict[Path, Tuple[int, int]] = {}
    
    for file_path in files:
        removed_br, collapsed_blank = process_file(file_path, apply=args.apply)
        results[file_path] = (removed_br, collapsed_blank)
        
        if removed_br > 0 or collapsed_blank > 0:
            rel_path = file_path.relative_to(docs_dir.parent)
            print(f"  {rel_path}")
            print(f"    - Removed <br>: {removed_br}")
            print(f"    - Collapsed blanks: {collapsed_blank}")
    
    # Summary
    total_files = len([r for r in results.values() if r[0] > 0 or r[1] > 0])
    total_br = sum(r[0] for r in results.values())
    total_blank = sum(r[1] for r in results.values())
    
    print()
    print("=" * 60)
    print(f"📊 SUMMARY")
    print("=" * 60)
    print(f"Files processed:      {len(results)}")
    print(f"Files modified:       {total_files}")
    print(f"Standalone <br>:      {total_br} removed")
    print(f"Extra blank lines:    {total_blank} collapsed")
    print()
    
    # Create report
    report = create_report(results, docs_dir, args.apply)
    
    if not args.apply:
        print("📋 DRY RUN completed. No files were modified.")
        print("   Run with --apply to make changes.")
    else:
        print("✅ Changes applied successfully!")
        print()
        print("Next steps:")
        print("  1. Review changes: git diff docs/app-development/")
        print("  2. Verify build: mkdocs build --strict")
        print("  3. Commit: git commit -m 'chore(docs): remove stray <br> in App Development'")
    
    return 0


if __name__ == '__main__':
    exit(main())

