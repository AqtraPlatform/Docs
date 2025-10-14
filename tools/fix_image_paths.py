#!/usr/bin/env python3
"""
Image Path Fixer for MkDocs Documentation

Automatically fixes broken image references in Markdown files by:
1. Finding all image references
2. Locating the actual image file in docs/assets/images/
3. Calculating correct relative path from MD file to image
4. Updating the reference with proper path

Usage:
    python tools/fix_image_paths.py --dry-run    # Preview changes
    python tools/fix_image_paths.py --apply      # Apply changes
    python tools/fix_image_paths.py --src docs --assets-dir assets --dry-run
"""

import os
import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_DOCS_DIR = PROJECT_ROOT / "docs"
DEFAULT_ASSETS_DIR = "assets"  # Relative to docs/


class ImagePathFixer:
    def __init__(self, docs_dir: Path, assets_dir: str):
        self.docs_dir = docs_dir
        self.assets_dir = assets_dir
        self.images_dir = self.docs_dir / assets_dir / "images"
        
        # Build image index
        self.image_index = self._build_image_index()
        
        # Statistics
        self.files_scanned = 0
        self.images_found = 0
        self.images_fixed = 0
        self.errors = 0
    
    def _build_image_index(self) -> Dict[str, Path]:
        """Create index of all images: filename -> full path"""
        index = {}
        
        if not self.images_dir.exists():
            print(f"WARNING: Images directory not found: {self.images_dir}")
            return index
        
        for img_file in self.images_dir.rglob("*"):
            if img_file.is_file() and img_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']:
                filename = img_file.name
                # Store all instances (there might be duplicates in different categories)
                if filename not in index:
                    index[filename] = []
                index[filename].append(img_file)
        
        return index
    
    def _calculate_relative_path(self, md_file: Path, image_file: Path) -> str:
        """Calculate relative path from markdown file to image file"""
        try:
            # Both paths should be absolute
            md_dir = md_file.parent
            rel_path = os.path.relpath(image_file, md_dir)
            return rel_path
        except Exception as e:
            print(f"ERROR calculating path from {md_file} to {image_file}: {e}")
            return None
    
    def _find_image_file(self, image_ref: str, md_file: Path) -> Optional[Path]:
        """Find the actual image file based on reference"""
        # Extract filename from reference
        filename = Path(image_ref).name
        
        if filename not in self.image_index:
            return None
        
        candidates = self.image_index[filename]
        
        if len(candidates) == 1:
            return candidates[0]
        
        # Multiple candidates - try to guess correct one based on MD file location
        md_relative = md_file.relative_to(self.docs_dir)
        md_category = md_relative.parts[0] if len(md_relative.parts) > 1 else "general"
        
        # Prefer image in matching category
        for img_path in candidates:
            img_relative = img_path.relative_to(self.images_dir)
            img_category = img_relative.parts[0] if len(img_relative.parts) > 1 else "general"
            if img_category == md_category:
                return img_path
        
        # Return first candidate if no category match
        return candidates[0]
    
    def _fix_image_references(self, md_file: Path, content: str, dry_run: bool = True) -> Tuple[str, List[Dict]]:
        """Fix all image references in a markdown file"""
        changes = []
        new_content = content
        
        # Pattern for markdown image syntax: ![alt](path)
        pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        
        matches = list(re.finditer(pattern, content))
        
        for match in matches:
            alt_text = match.group(1)
            old_path = match.group(2)
            
            # Skip external URLs
            if old_path.startswith('http://') or old_path.startswith('https://'):
                continue
            
            # Skip if already a proper relative path to assets
            if '../assets/' in old_path or './assets/' in old_path:
                continue
            
            # Check if current path is broken (just filename or wrong path)
            current_ref_path = (md_file.parent / old_path).resolve()
            if current_ref_path.exists():
                # Path is correct, skip
                continue
            
            # Find the actual image file
            image_file = self._find_image_file(old_path, md_file)
            
            if not image_file:
                changes.append({
                    'type': 'not_found',
                    'old': old_path,
                    'new': None,
                    'alt': alt_text
                })
                continue
            
            # Calculate correct relative path
            new_path = self._calculate_relative_path(md_file, image_file)
            
            if not new_path:
                changes.append({
                    'type': 'error',
                    'old': old_path,
                    'new': None,
                    'alt': alt_text
                })
                continue
            
            # Normalize path separators
            new_path = new_path.replace('\\', '/')
            
            if new_path != old_path:
                changes.append({
                    'type': 'fixed',
                    'old': old_path,
                    'new': new_path,
                    'alt': alt_text,
                    'image': str(image_file.relative_to(self.docs_dir))
                })
                
                # Replace in content
                old_ref = f'![{alt_text}]({old_path})'
                new_ref = f'![{alt_text}]({new_path})'
                new_content = new_content.replace(old_ref, new_ref)
        
        return new_content, changes
    
    def process_file(self, md_file: Path, dry_run: bool = True) -> bool:
        """Process a single markdown file"""
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content, changes = self._fix_image_references(md_file, content, dry_run)
            
            if changes:
                rel_path = md_file.relative_to(PROJECT_ROOT)
                print(f"\n📄 {rel_path}")
                
                for change in changes:
                    if change['type'] == 'fixed':
                        self.images_fixed += 1
                        print(f"  ✓ FIXED: {change['old']}")
                        print(f"          → {change['new']}")
                        print(f"          (resolves to: {change['image']})")
                    elif change['type'] == 'not_found':
                        self.errors += 1
                        print(f"  ✗ NOT FOUND: {change['old']}")
                    elif change['type'] == 'error':
                        self.errors += 1
                        print(f"  ✗ ERROR: {change['old']}")
                
                if not dry_run and new_content != content:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"  💾 File updated")
            
            self.files_scanned += 1
            self.images_found += len(changes)
            
            return len(changes) > 0
            
        except Exception as e:
            print(f"ERROR processing {md_file}: {e}")
            self.errors += 1
            return False
    
    def process_all(self, dry_run: bool = True):
        """Process all markdown files in docs directory"""
        print("=" * 80)
        print("IMAGE PATH FIXER")
        print("=" * 80)
        print(f"Docs directory: {self.docs_dir}")
        print(f"Images directory: {self.images_dir}")
        print(f"Mode: {'DRY RUN (no changes)' if dry_run else 'APPLY (will modify files)'}")
        print(f"Total images indexed: {sum(len(v) for v in self.image_index.values())}")
        print("=" * 80)
        
        # Find all markdown files
        md_files = list(self.docs_dir.rglob("*.md"))
        print(f"\nFound {len(md_files)} markdown files to scan...")
        print()
        
        # Process each file
        files_with_changes = 0
        for md_file in sorted(md_files):
            if self.process_file(md_file, dry_run):
                files_with_changes += 1
        
        # Summary
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Files scanned:        {self.files_scanned}")
        print(f"Files with changes:   {files_with_changes}")
        print(f"Images fixed:         {self.images_fixed}")
        print(f"Errors/Not found:     {self.errors}")
        print("=" * 80)
        
        if dry_run:
            print("\n⚠️  DRY RUN MODE - No files were modified")
            print("Run with --apply to make changes")
        else:
            print(f"\n✅ {self.images_fixed} image references updated!")
            if self.errors > 0:
                print(f"⚠️  {self.errors} images could not be found")


def main():
    parser = argparse.ArgumentParser(
        description="Fix broken image references in MkDocs documentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python tools/fix_image_paths.py --dry-run              # Preview changes
  python tools/fix_image_paths.py --apply                # Apply changes
  python tools/fix_image_paths.py --src docs --dry-run  # Custom docs dir
        """
    )
    
    parser.add_argument(
        '--src',
        type=str,
        default='docs',
        help='Source documentation directory (default: docs)'
    )
    
    parser.add_argument(
        '--assets-dir',
        type=str,
        default='assets',
        help='Assets directory name relative to docs (default: assets)'
    )
    
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Apply changes (default is dry-run mode)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without modifying files (default)'
    )
    
    args = parser.parse_args()
    
    # Determine mode
    dry_run = not args.apply
    
    # Resolve paths
    docs_dir = PROJECT_ROOT / args.src
    
    if not docs_dir.exists():
        print(f"ERROR: Documentation directory not found: {docs_dir}")
        return 1
    
    # Create fixer and run
    fixer = ImagePathFixer(docs_dir, args.assets_dir)
    fixer.process_all(dry_run=dry_run)
    
    return 0 if fixer.errors == 0 else 1


if __name__ == "__main__":
    exit(main())
