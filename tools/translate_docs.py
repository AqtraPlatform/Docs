#!/usr/bin/env python3
"""
Script to translate documentation from Russian to English using .po files
"""
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

def parse_po_file(po_path: str) -> List[Tuple[str, str]]:
    """
    Parse a .po file and extract msgid/msgstr pairs.
    Returns a list of (msgid, msgstr) tuples.
    """
    translations = []
    current_msgid = []
    current_msgstr = []
    in_msgid = False
    in_msgstr = False
    
    def save_translation():
        """Helper to save current translation pair."""
        if current_msgid or current_msgstr:
            msgid = ''.join(current_msgid)
            msgstr = ''.join(current_msgstr)
            # Only add if both exist and are not identical
            if msgid and msgstr and msgid != msgstr:
                translations.append((msgid, msgstr))
    
    with open(po_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            
            # Skip comments
            if line.startswith('#'):
                continue
            
            # Empty line ends current entry
            if not line.strip():
                save_translation()
                current_msgid = []
                current_msgstr = []
                in_msgid = False
                in_msgstr = False
                continue
            
            # Start of msgid
            if line.startswith('msgid '):
                # Save previous entry if it exists
                save_translation()
                current_msgid = []
                current_msgstr = []
                
                # Extract the string content
                match = re.match(r'msgid\s+"(.*)"', line)
                if match:
                    content = match.group(1)
                    # Only add if not empty (msgid "" is used for multi-line starts)
                    if content:
                        current_msgid.append(content)
                in_msgid = True
                in_msgstr = False
                
            # Start of msgstr
            elif line.startswith('msgstr '):
                match = re.match(r'msgstr\s+"(.*)"', line)
                if match:
                    content = match.group(1)
                    # Only add if not empty
                    if content:
                        current_msgstr.append(content)
                in_msgid = False
                in_msgstr = True
                
            # Continuation line
            elif line.startswith('"') and line.endswith('"'):
                content = line[1:-1]  # Remove quotes
                if in_msgid:
                    current_msgid.append(content)
                elif in_msgstr:
                    current_msgstr.append(content)
        
        # Don't forget the last pair
        save_translation()
    
    return translations


def find_po_file(docs_file: Path, locale_dir: Path, docs_dir: Path) -> Path:
    """
    Find the corresponding .po file for a documentation file.
    """
    # Get relative path from docs directory
    rel_path = docs_file.relative_to(docs_dir)
    
    # Construct .po file path
    # Remove .md extension and add .po
    po_rel_path = str(rel_path).replace('.md', '.po')
    
    # Handle special directory and file mappings
    # app-development -> app-develop
    po_rel_path = po_rel_path.replace('app-development/', 'app-develop/')
    
    # tutorials mappings
    po_rel_path = po_rel_path.replace('tutorials/01-basic-setup.po', 'tutorials/tutorial1.po')
    po_rel_path = po_rel_path.replace('tutorials/02-data-flow.po', 'tutorials/tutorial2.po')
    po_rel_path = po_rel_path.replace('tutorials/03-workflow.po', 'tutorials/tutorial3.po')
    
    # installation mappings
    po_rel_path = po_rel_path.replace('installation/configuration.po', 'install1/basic-settings.po')
    
    # overview mappings
    po_rel_path = po_rel_path.replace('overview/getting-started.po', 'overview1/first-entry.po')
    po_rel_path = po_rel_path.replace('overview/index.po', 'overview1/index.po')
    po_rel_path = po_rel_path.replace('overview/terms-of-use.po', 'overview1/terms-of-use.po')
    
    po_path = locale_dir / po_rel_path
    
    return po_path


def apply_translations(md_content: str, translations: List[Tuple[str, str]]) -> str:
    """
    Apply translations to markdown content.
    Sort translations by length (longest first) to avoid partial replacements.
    """
    # Sort by length of msgid (descending) to replace longer strings first
    sorted_translations = sorted(translations, key=lambda x: len(x[0]), reverse=True)
    
    result = md_content
    
    for msgid, msgstr in sorted_translations:
        # Unescape the msgid and msgstr (remove backslash escaping)
        # This is needed because .po files escape quotes
        msgid_unescaped = msgid.replace('\\"', '"').replace("\\'", "'")
        msgstr_unescaped = msgstr.replace('\\"', '"').replace("\\'", "'")
        
        # Try to replace with unescaped version
        if msgid_unescaped in result:
            result = result.replace(msgid_unescaped, msgstr_unescaped)
        # Also try with escaped version in case it's used
        elif msgid in result:
            result = result.replace(msgid, msgstr_unescaped)
        else:
            # Try variations for common differences between .po and .md files:
            # 1. .po files sometimes have " <br>" at the end, but .md files might not
            # 2. .po files don't have markdown list markers "- " at the start
            
            # Remove trailing <br> and whitespace from msgid
            msgid_no_br = msgid_unescaped.rstrip()
            if msgid_no_br.endswith('<br>'):
                msgid_no_br = msgid_no_br[:-4].rstrip()
                msgstr_no_br = msgstr_unescaped.rstrip()
                if msgstr_no_br.endswith('<br>'):
                    msgstr_no_br = msgstr_no_br[:-4].rstrip()
                
                # Try to find and replace without <br>
                if msgid_no_br in result:
                    result = result.replace(msgid_no_br, msgstr_no_br)
    
    return result


def translate_file(md_path: Path, locale_dir: Path, docs_dir: Path, dry_run: bool = False) -> bool:
    """
    Translate a single markdown file using its corresponding .po file.
    Returns True if translation was applied, False otherwise.
    """
    po_path = find_po_file(md_path, locale_dir, docs_dir)
    
    if not po_path.exists():
        print(f"⚠️  No .po file found for {md_path.name} (expected: {po_path})")
        return False
    
    # Parse .po file
    translations = parse_po_file(str(po_path))
    
    if not translations:
        print(f"⚠️  No translations found in {po_path.name}")
        return False
    
    # Read markdown file
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Apply translations
    translated_content = apply_translations(md_content, translations)
    
    # Check if anything changed
    if translated_content == md_content:
        print(f"ℹ️  No changes for {md_path.name}")
        return False
    
    if dry_run:
        print(f"✓ Would translate {md_path.name} ({len(translations)} translation pairs)")
        return True
    
    # Write back
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(translated_content)
    
    print(f"✓ Translated {md_path.name} ({len(translations)} translation pairs)")
    return True


def main():
    """Main function to translate all documentation files."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Translate documentation using .po files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    parser.add_argument('--file', type=str, help='Translate only a specific file')
    args = parser.parse_args()
    
    # Setup paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    docs_dir = project_dir / 'docs'
    locale_dir = project_dir / 'locale' / 'en' / 'LC_MESSAGES'
    
    if not locale_dir.exists():
        print(f"❌ Locale directory not found: {locale_dir}")
        return
    
    if args.file:
        # Translate single file
        md_path = Path(args.file)
        if not md_path.exists():
            md_path = docs_dir / args.file
        
        if not md_path.exists():
            print(f"❌ File not found: {args.file}")
            return
        
        translate_file(md_path, locale_dir, docs_dir, args.dry_run)
        return
    
    # Find all markdown files
    md_files = list(docs_dir.glob('**/*.md'))
    
    print(f"Found {len(md_files)} markdown files")
    print(f"Locale directory: {locale_dir}")
    
    if args.dry_run:
        print("\n🔍 DRY RUN MODE - No files will be modified\n")
    
    translated_count = 0
    skipped_count = 0
    
    for md_path in sorted(md_files):
        # Skip certain files
        if md_path.name in ['terms-of-use.rst', 'robots.txt']:
            continue
        
        # Skip i18n directory itself
        if 'i18n/' in str(md_path):
            continue
        
        if translate_file(md_path, locale_dir, docs_dir, args.dry_run):
            translated_count += 1
        else:
            skipped_count += 1
    
    print(f"\n{'Would translate' if args.dry_run else 'Translated'} {translated_count} files")
    print(f"Skipped {skipped_count} files")


if __name__ == '__main__':
    main()

