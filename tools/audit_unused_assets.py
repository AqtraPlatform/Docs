#!/usr/bin/env python3
"""
Documentation Asset Audit Tool
Finds unused images, broken links, and orphaned pages in MkDocs documentation.
"""

import os
import re
from pathlib import Path
from typing import Set, List, Dict
import yaml

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
ASSETS_DIR = DOCS_DIR / "assets" / "images"
MKDOCS_CONFIG = PROJECT_ROOT / "mkdocs.yml"

def load_nav_files(mkdocs_yml: Path) -> Set[str]:
    """Extract all files referenced in mkdocs.yml nav."""
    with open(mkdocs_yml, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    nav_files = set()
    
    def extract_files(nav_item):
        if isinstance(nav_item, dict):
            for value in nav_item.values():
                if isinstance(value, str) and value.endswith('.md'):
                    nav_files.add(value)
                elif isinstance(value, list):
                    for item in value:
                        extract_files(item)
        elif isinstance(nav_item, list):
            for item in nav_item:
                extract_files(item)
        elif isinstance(nav_item, str) and nav_item.endswith('.md'):
            nav_files.add(nav_item)
    
    if 'nav' in config:
        extract_files(config['nav'])
    
    return nav_files

def find_all_md_files(docs_dir: Path) -> Set[Path]:
    """Find all Markdown files in docs directory."""
    return set(docs_dir.rglob("*.md"))

def find_all_images(assets_dir: Path) -> Set[Path]:
    """Find all image files in assets directory."""
    images = set()
    if assets_dir.exists():
        for ext in ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg', '*.webp']:
            images.update(assets_dir.rglob(ext))
    return images

def find_image_references(docs_dir: Path) -> Dict[str, List[str]]:
    """Find all image references in Markdown files."""
    image_refs = {}
    
    # Patterns for image references
    patterns = [
        r'!\[.*?\]\((.*?)\)',  # ![alt](path)
        r'<img[^>]+src="([^"]+)"',  # <img src="path">
        r'<img[^>]+src=\'([^\']+)\'',  # <img src='path'>
    ]
    
    for md_file in docs_dir.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for pattern in patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    # Normalize path
                    img_path = match.strip()
                    if img_path not in image_refs:
                        image_refs[img_path] = []
                    image_refs[img_path].append(str(md_file))
        except Exception as e:
            print(f"Warning: Could not read {md_file}: {e}")
    
    return image_refs

def main():
    print("=" * 80)
    print("DOCUMENTATION ASSET AUDIT")
    print("=" * 80)
    print()
    
    # 1. Find orphaned pages (not in nav)
    print("1. ORPHANED PAGES (Not in mkdocs.yml nav)")
    print("-" * 80)
    
    nav_files = load_nav_files(MKDOCS_CONFIG)
    all_md_files = find_all_md_files(DOCS_DIR)
    
    orphaned_pages = []
    for md_file in all_md_files:
        rel_path = md_file.relative_to(PROJECT_ROOT)
        # Check if file is in nav (relative to docs/)
        try:
            doc_relative = md_file.relative_to(DOCS_DIR)
            if str(doc_relative) not in nav_files:
                orphaned_pages.append(str(rel_path))
        except ValueError:
            pass
    
    if orphaned_pages:
        print(f"Found {len(orphaned_pages)} orphaned pages:")
        for page in sorted(orphaned_pages):
            print(f"  - {page}")
    else:
        print("✓ No orphaned pages found")
    print()
    
    # 2. Find unused images
    print("2. UNUSED IMAGES")
    print("-" * 80)
    
    all_images = find_all_images(ASSETS_DIR)
    image_refs = find_image_references(DOCS_DIR)
    
    # Get all referenced image paths (resolve relative paths)
    referenced_images = set()
    for img_ref in image_refs.keys():
        # Try to resolve the path
        possible_paths = [
            DOCS_DIR / img_ref.lstrip('/'),
            ASSETS_DIR / img_ref.lstrip('/'),
            Path(img_ref),
        ]
        for p in possible_paths:
            if p.exists() and p in all_images:
                referenced_images.add(p)
    
    unused_images = all_images - referenced_images
    
    if unused_images:
        print(f"Found {len(unused_images)} potentially unused images:")
        for img in sorted(unused_images):
            rel_path = img.relative_to(PROJECT_ROOT)
            size_kb = img.stat().st_size / 1024
            print(f"  - {rel_path} ({size_kb:.1f} KB)")
    else:
        print("✓ All images appear to be referenced")
    print()
    
    # 3. Find broken image links
    print("3. BROKEN IMAGE LINKS")
    print("-" * 80)
    
    broken_links = []
    for img_ref, sources in image_refs.items():
        # Try to resolve the image
        found = False
        possible_paths = [
            DOCS_DIR / img_ref.lstrip('/'),
            ASSETS_DIR / img_ref.lstrip('/'),
            Path(img_ref),
        ]
        
        for p in possible_paths:
            if p.exists():
                found = True
                break
        
        if not found and not img_ref.startswith('http'):
            broken_links.append((img_ref, sources))
    
    if broken_links:
        print(f"Found {len(broken_links)} broken image links:")
        for img_ref, sources in broken_links:
            print(f"  - {img_ref}")
            for source in sources[:3]:  # Show first 3 sources
                print(f"    Referenced in: {source}")
    else:
        print("✓ No broken image links found")
    print()
    
    # 4. Summary
    print("4. SUMMARY")
    print("-" * 80)
    print(f"Total MD files:        {len(all_md_files)}")
    print(f"Files in nav:          {len(nav_files)}")
    print(f"Orphaned pages:        {len(orphaned_pages)}")
    print(f"Total images:          {len(all_images)}")
    print(f"Referenced images:     {len(referenced_images)}")
    print(f"Unused images:         {len(unused_images)}")
    print(f"Broken image links:    {len(broken_links)}")
    print()
    
    # Calculate potential space savings
    if unused_images:
        total_size = sum(img.stat().st_size for img in unused_images) / (1024 * 1024)
        print(f"Potential space savings: {total_size:.2f} MB")
    
    print("=" * 80)

if __name__ == "__main__":
    main()

