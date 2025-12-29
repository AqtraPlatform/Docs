#!/usr/bin/env python3
"""
MkDocs Anchors Doctor - проверка и исправление якорных ссылок
Enhanced version with proper slugify and safe fixes
"""

import os
import re
import csv
import sys
from pathlib import Path
from typing import List, Dict, Set, Optional, Tuple
import argparse

try:
    from pymdownx.slugs import slugify
except ImportError:
    # Fallback slugify function
    def slugify(text, max_length=0, word_boundary=False, separator="-", stopwords=None):
        """Simple slugify function"""
        import unicodedata
        import re
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove accents
        text = unicodedata.normalize('NFD', text)
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
        
        # Replace spaces and special characters with separator
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', separator, text)
        
        # Remove leading/trailing separators
        text = text.strip(separator)
        
        return text

# Fallback slugify function
def fallback_slugify(text, separator="-"):
    """Simple slugify function"""
    import unicodedata
    import re
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove accents
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    
    # Replace spaces and special characters with separator
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', separator, text)
    
    # Remove leading/trailing separators
    text = text.strip(separator)
    
    return text

# Ensure slugify is callable with the right signature
def safe_slugify(text, separator="-"):
    """Safe slugify function that works with pymdownx.slugs.slugify"""
    try:
        # Try the correct signature for pymdownx.slugs.slugify
        return slugify(text, max_length=0, word_boundary=False, separator=separator, stopwords=None)
    except TypeError:
        try:
            # Try with just text and separator
            return slugify(text, separator=separator)
        except TypeError:
            try:
                # Try with just text
                return slugify(text)
            except TypeError:
                # Use fallback function
                return fallback_slugify(text, separator)

class AnchorsDoctor:
    # Improved regex patterns - non-greedy, no multiline
    MD_LINK_RE = re.compile(r'(?<!\!)\[[^\]]+\]\(([^)\n]+?)\)')  # [text](url)
    MD_IMG_RE = re.compile(r'!\[[^\]]*\]\(([^)\n]+?)\)')        # ![alt](url)
    
    def __init__(self, src_dir: str = "docs", exclude: List[str] = None, skip_images: bool = False):
        self.src_dir = Path(src_dir).resolve()
        self.anchors_found = {}  # page -> set of anchors
        self.broken_links = []   # list of broken links
        self.fixes_applied = []  # list of applied fixes
        self.safe_fixes = []     # list of safe fixes that can be applied
        self.exclude_patterns = exclude or []  # list of files to exclude
        self.skip_images = skip_images  # skip image validation
        self.image_warnings = []  # warnings for missing images
    
    @staticmethod
    def clean_url(url: str) -> str:
        """Clean URL from trailing punctuation and whitespace"""
        url = url.strip()
        # Remove common trailing punctuation from prose
        url = url.rstrip(').,;:!?»"\'')
        return url
    
    @staticmethod
    def is_external_url(url: str) -> bool:
        """Check if URL is external (has protocol)"""
        return bool(re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://', url))
    
    def is_excluded(self, file_path: str) -> bool:
        """Check if file should be excluded from checking"""
        for pattern in self.exclude_patterns:
            if pattern in file_path or Path(file_path).match(pattern):
                return True
        return False
    
    @staticmethod
    def remove_code_blocks(content: str) -> str:
        """Remove code blocks from markdown to avoid false positives"""
        # Remove fenced code blocks
        content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        # Remove inline code
        content = re.sub(r'`[^`\n]+`', '', content)
        return content
        
    def check_anchors(self, dry_run: bool = False) -> bool:
        """Проверка и исправление якорных ссылок"""
        print("🔗 Запуск проверки якорных ссылок...")
        print(f"  📁 Исходники: {self.src_dir}")
        
        if not self.src_dir.exists():
            print("❌ Папка с исходниками не найдена")
            return False
        
        # Собираем все якоря из заголовков
        self._collect_anchors()
        print(f"  📋 Найдено якорей: {sum(len(anchors) for anchors in self.anchors_found.values())}")
        
        # Проверяем ссылки
        self._check_links(dry_run)
        
        # Сохраняем отчеты
        self._save_reports()
        
        # Выводим отчет
        self._print_report()
        
        return len(self.broken_links) == 0
    
    def _collect_anchors(self):
        """Сбор якорей из заголовков всех страниц и явных id"""
        md_files = list(self.src_dir.rglob('*.md'))
        
        for md_file in md_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                relative_path = str(md_file.relative_to(self.src_dir))
                
                # Remove code blocks to avoid false positives
                content_no_code = self.remove_code_blocks(content)
                
                anchors = set()
                
                # Extract explicit HTML id attributes: <a id="..."></a> or <div id="..."> or <span id="...">
                html_id_pattern = r'<(?:a|div|span|h[1-6])\s+[^>]*id=["\']([^"\']+)["\']'
                for match in re.finditer(html_id_pattern, content_no_code):
                    anchor_id = match.group(1).strip()
                    if anchor_id:
                        anchors.add(anchor_id)
                
                # Extract explicit id attributes: {: #my-id }
                explicit_id_pattern = r'\{:\s*#([A-Za-z0-9_.\-]+)\s*\}'
                for match in re.finditer(explicit_id_pattern, content_no_code):
                    anchor_id = match.group(1).strip()
                    if anchor_id:
                        anchors.add(anchor_id)
                
                # Ищем заголовки (##, ###, ####, etc.)
                header_pattern = r'^(#{1,6})\s+(.+)$'
                slug_list = []  # List to track slug order for duplicate handling
                
                for line in content_no_code.split('\n'):
                    match = re.match(header_pattern, line.strip())
                    if match:
                        level = len(match.group(1))
                        title = match.group(2).strip()
                        
                        # Check for explicit id in header: ## Title {#my-id}
                        explicit_id_match = re.search(r'\{#([A-Za-z0-9_.\-]+)\}\s*$', title)
                        if explicit_id_match:
                            explicit_id = explicit_id_match.group(1).strip()
                            anchors.add(explicit_id)
                            # Remove {#id} from title for slugify
                            title = re.sub(r'\s*\{#[^}]+\}\s*$', '', title).strip()
                        
                        # Generate slug from clean title (if title is not empty)
                        if title:
                            slug = safe_slugify(title, separator="-")
                            if slug:
                                slug_list.append(slug)
                
                # Process slugs to handle duplicates like MkDocs: slug, slug-1, slug-2, ...
                # First pass: count occurrences
                slug_counts = {}
                for slug in slug_list:
                    slug_counts[slug] = slug_counts.get(slug, 0) + 1
                
                # Second pass: add anchors
                slug_seen = {}
                for slug in slug_list:
                    if slug not in slug_seen:
                        slug_seen[slug] = 0
                    
                    slug_seen[slug] += 1
                    occurrence = slug_seen[slug]
                    
                    if occurrence == 1:
                        # First occurrence: add base slug
                        anchors.add(slug)
                    else:
                        # Duplicate: add slug-1, slug-2, etc. (second occurrence = slug-1)
                        anchors.add(f"{slug}-{occurrence - 1}")
                
                if anchors:
                    self.anchors_found[relative_path] = anchors
                    
            except Exception as e:
                print(f"  ⚠️  Ошибка обработки {md_file}: {e}")
    
    def _check_links(self, dry_run: bool = False):
        """Проверка ссылок в Markdown файлах с улучшенным парсингом"""
        md_files = list(self.src_dir.rglob('*.md'))
        
        for md_file in md_files:
            try:
                relative_path = str(md_file.relative_to(self.src_dir))
                
                # Skip excluded files
                if self.is_excluded(relative_path):
                    print(f"  ⏭️  Пропущен (excluded): {relative_path}")
                    continue
                
                content = md_file.read_text(encoding='utf-8')
                
                # Remove code blocks to avoid false positives
                content_no_code = self.remove_code_blocks(content)
                
                # Extract all markdown links (not images)
                for match in self.MD_LINK_RE.finditer(content_no_code):
                    url = self.clean_url(match.group(1))
                    
                    # Skip external URLs
                    if self.is_external_url(url):
                        continue
                    
                    # Parse URL components
                    if '#' in url:
                        # Link with anchor
                        parts = url.split('#', 1)
                        file_part = parts[0].strip()
                        anchor = parts[1].strip()
                        
                        if file_part:
                            # Link to anchor in another file: [text](file.md#anchor)
                            self._check_anchor_link(relative_path, file_part, anchor, match.group(0), dry_run)
                        else:
                            # Link to anchor in current file: [text](#anchor)
                            self._check_anchor_link(relative_path, relative_path, anchor, match.group(0), dry_run)
                    else:
                        # Link without anchor - check file existence
                        if url:  # Skip empty links
                            self._check_file_link(relative_path, url, match.group(0), dry_run, is_image=False)
                
                # Also check image links for completeness
                for match in self.MD_IMG_RE.finditer(content_no_code):
                    url = self.clean_url(match.group(1))
                    
                    # Skip external URLs
                    if self.is_external_url(url):
                        continue
                    
                    # Check only file part (images usually don't have anchors)
                    file_part = url.split('#')[0].strip()
                    if file_part:
                        self._check_file_link(relative_path, file_part, match.group(0), dry_run, is_image=True)
                            
            except Exception as e:
                print(f"  ⚠️  Ошибка обработки {md_file}: {e}")
    
    def _check_anchor_link(self, source_page: str, target_file: str, anchor: str, full_link: str, dry_run: bool):
        """Проверка ссылки с якорем"""
        # Определяем целевой файл
        if target_file == source_page:
            # Ссылка на якорь в текущем файле
            target_page = source_page
        else:
            # Ссылка на якорь в другом файле
            target_page = self._resolve_file_path(source_page, target_file)
            if not target_page:
                self.broken_links.append({
                    'page': source_page,
                    'original_link': full_link,
                    'target_file': target_file,
                    'broken_anchor': f"#{anchor}",
                    'status': 'Target file not found',
                    'suggestion': ''
                })
                return
        
        # Проверяем существование якоря
        if target_page in self.anchors_found:
            # Нормализуем якорь
            normalized_anchor = safe_slugify(anchor, separator="-")
            
            if normalized_anchor in self.anchors_found[target_page]:
                # Якорь найден
                return
            else:
                # Ищем похожие якоря
                similar_anchor = self._find_similar_anchor(normalized_anchor, target_page)
                if similar_anchor:
                    # Нашли похожий якорь - это безопасное исправление
                    self.safe_fixes.append({
                        'page': source_page,
                        'original_link': full_link,
                        'target_file': target_file,
                        'broken_anchor': f"#{anchor}",
                        'status': 'Similar anchor found',
                        'suggestion': full_link.replace(f"#{anchor}", f"#{similar_anchor}")
                    })
                    if not dry_run:
                        self._apply_fix(source_page, full_link, full_link.replace(f"#{anchor}", f"#{similar_anchor}"))
                else:
                    # Якорь не найден
                    self.broken_links.append({
                        'page': source_page,
                        'original_link': full_link,
                        'target_file': target_file,
                        'broken_anchor': f"#{anchor}",
                        'status': 'Anchor not found',
                        'suggestion': ''
                    })
        else:
            # Целевой файл не найден в сканированных
            self.broken_links.append({
                'page': source_page,
                'original_link': full_link,
                'target_file': target_file,
                'broken_anchor': f"#{anchor}",
                'status': 'Target file not scanned',
                'suggestion': ''
            })
    
    def _check_file_link(self, source_page: str, target_file: str, full_link: str, dry_run: bool, is_image: bool = False):
        """Проверка ссылки на файл без якоря"""
        target_page = self._resolve_file_path(source_page, target_file)
        if not target_page:
            # Check if this is an image and skip_images is enabled
            if is_image and self.skip_images:
                self.image_warnings.append({
                    'page': source_page,
                    'original_link': full_link,
                    'target_file': target_file,
                    'status': 'Image not found (skipped)'
                })
                return
            
            self.broken_links.append({
                'page': source_page,
                'original_link': full_link,
                'target_file': target_file,
                'broken_anchor': '',
                'status': 'File not found',
                'suggestion': ''
            })
    
    def _resolve_file_path(self, source_page: str, target_file: str) -> Optional[str]:
        """Разрешение пути к файлу с поддержкой относительных путей"""
        # Если это уже полный путь относительно docs/
        if target_file in self.anchors_found:
            return target_file
        
        # Нормализуем путь для корректной обработки ../
        source_path = Path(source_page).parent
        normalized_target = os.path.normpath(os.path.join(str(source_path), target_file))
        normalized_target = normalized_target.replace('\\', '/')  # Windows compatibility
        
        # Проверяем нормализованный путь
        if normalized_target in self.anchors_found:
            return normalized_target
        
        # Пытаемся найти файл относительно исходной страницы
        possible_paths = [
            self.src_dir / normalized_target,
            self.src_dir / f"{normalized_target}.md",
            self.src_dir / target_file,
            self.src_dir / f"{target_file}.md",
        ]
        
        for path in possible_paths:
            try:
                if path.exists() and path.is_file():
                    # Проверяем, что это markdown файл
                    if path.suffix == '.md':
                        relative_path = str(path.relative_to(self.src_dir))
                        if relative_path in self.anchors_found:
                            return relative_path
            except (ValueError, OSError):
                continue
        
        return None
    
    def _find_similar_anchor(self, anchor: str, target_page: str) -> Optional[str]:
        """Поиск похожего якоря"""
        if target_page not in self.anchors_found:
            return None
        
        available_anchors = self.anchors_found[target_page]
        
        # Точное совпадение (уже проверено выше)
        if anchor in available_anchors:
            return anchor
        
        # Поиск по частичному совпадению
        for available_anchor in available_anchors:
            if anchor in available_anchor or available_anchor in anchor:
                return available_anchor
        
        # Поиск по расстоянию Левенштейна (упрощенный)
        for available_anchor in available_anchors:
            if self._similarity(anchor, available_anchor) > 0.8:
                return available_anchor
        
        return None
    
    def _similarity(self, a: str, b: str) -> float:
        """Упрощенная мера схожести строк"""
        if not a or not b:
            return 0.0
        
        # Нормализуем строки
        a = a.lower().replace('-', '').replace('_', '')
        b = b.lower().replace('-', '').replace('_', '')
        
        if a == b:
            return 1.0
        
        # Простая проверка на вхождение
        if a in b or b in a:
            return 0.9
        
        # Проверка на общие слова
        a_words = set(a.split())
        b_words = set(b.split())
        if a_words and b_words:
            common_words = len(a_words & b_words)
            total_words = len(a_words | b_words)
            return common_words / total_words
        
        return 0.0
    
    def _apply_fix(self, page: str, original: str, fixed: str):
        """Применение исправления к файлу"""
        page_path = self.src_dir / page
        try:
            content = page_path.read_text(encoding='utf-8')
            new_content = content.replace(original, fixed)
            if new_content != content:
                page_path.write_text(new_content, encoding='utf-8')
                self.fixes_applied.append({
                    'page': page,
                    'original': original,
                    'suggestion': fixed,
                    'status': 'Applied'
                })
        except Exception as e:
            print(f"  ⚠️  Ошибка применения исправления в {page}: {e}")
    
    def _save_reports(self):
        """Сохранение отчетов в CSV"""
        build_dir = Path("build")
        build_dir.mkdir(exist_ok=True)
        
        # Объединяем все записи для отчета
        all_records = []
        
        # Добавляем исправления
        for fix in self.fixes_applied:
            all_records.append({
                'page': fix['page'],
                'original_link': fix['original'],
                'target_file': '',
                'broken_anchor': '',
                'status': fix['status'],
                'suggestion': fix['suggestion']
            })
        
        # Добавляем безопасные исправления
        for fix in self.safe_fixes:
            all_records.append({
                'page': fix['page'],
                'original_link': fix['original_link'],
                'target_file': fix['target_file'],
                'broken_anchor': fix['broken_anchor'],
                'status': fix['status'],
                'suggestion': fix['suggestion']
            })
        
        # Добавляем битые ссылки
        for broken in self.broken_links:
            all_records.append({
                'page': broken['page'],
                'original_link': broken['original_link'],
                'target_file': broken['target_file'],
                'broken_anchor': broken['broken_anchor'],
                'status': broken['status'],
                'suggestion': broken['suggestion']
            })
        
        # Сохраняем в CSV
        with open(build_dir / "anchors_report.csv", "w", newline="", encoding="utf-8") as f:
            fieldnames = ['page', 'original_link', 'target_file', 'broken_anchor', 'status', 'suggestion']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for record in all_records:
                writer.writerow(record)
    
    def _print_report(self):
        """Вывод отчета"""
        print("\n" + "="*60)
        print("📋 ОТЧЕТ О ПРОВЕРКЕ ЯКОРНЫХ ССЫЛОК")
        print("="*60)
        
        if self.fixes_applied:
            print(f"✅ Применено исправлений: {len(self.fixes_applied)}")
            for fix in self.fixes_applied[:5]:
                print(f"  {fix['page']}: {fix['original']} → {fix['suggestion']}")
            if len(self.fixes_applied) > 5:
                print(f"  ... и еще {len(self.fixes_applied) - 5} исправлений")
        
        if self.safe_fixes:
            print(f"🔧 Безопасных исправлений: {len(self.safe_fixes)}")
            for fix in self.safe_fixes[:5]:
                print(f"  {fix['page']}: {fix['original_link']} → {fix['suggestion']}")
            if len(self.safe_fixes) > 5:
                print(f"  ... и еще {len(self.safe_fixes) - 5} исправлений")
        
        if self.image_warnings:
            print(f"⚠️  Пропущенных изображений: {len(self.image_warnings)}")
            for warning in self.image_warnings[:10]:
                print(f"  {warning['page']}: {warning['original_link']} ({warning['status']})")
            if len(self.image_warnings) > 10:
                print(f"  ... и еще {len(self.image_warnings) - 10} пропущенных изображений")
        
        if self.broken_links:
            print(f"❌ Битых ссылок: {len(self.broken_links)}")
            for broken in self.broken_links[:10]:
                print(f"  {broken['page']}: {broken['original_link']} ({broken['status']})")
            if len(self.broken_links) > 10:
                print(f"  ... и еще {len(self.broken_links) - 10} битых ссылок")
        else:
            print("✅ Все якорные ссылки валидны")
        
        print(f"\n📊 Отчет сохранен: build/anchors_report.csv")
        print("="*60)

def main():
    """Главная функция"""
    parser = argparse.ArgumentParser(description='Check and fix anchor links in MkDocs documentation')
    parser.add_argument('--src', default='docs', help='Source directory (default: docs)')
    parser.add_argument('--dry-run', action='store_true', help='Only generate report, do not apply fixes')
    parser.add_argument('--apply', action='store_true', help='Apply safe fixes')
    parser.add_argument('--exclude', action='append', help='Exclude files matching pattern (can be used multiple times)')
    parser.add_argument('--skip-images', action='store_true', help='Do not fail on missing image files, only warn')
    
    args = parser.parse_args()
    
    if args.apply and args.dry_run:
        print("❌ Нельзя использовать --apply и --dry-run одновременно")
        sys.exit(1)
    
    if not args.apply and not args.dry_run:
        print("ℹ️  Режим не указан. Запуск в режиме --dry-run")
        args.dry_run = True
    
    if args.exclude:
        print(f"📋 Исключения: {', '.join(args.exclude)}")
    
    if args.skip_images:
        print("🖼️  Режим: пропускать отсутствующие изображения (только предупреждения)")
    
    doctor = AnchorsDoctor(args.src, exclude=args.exclude or [], skip_images=args.skip_images)
    success = doctor.check_anchors(args.dry_run)
    
    if not success:
        print(f"\n❌ Найдено {len(doctor.broken_links)} битых ссылок")
        print("📊 Подробный отчет сохранен в build/anchors_report.csv")
        sys.exit(1)

if __name__ == "__main__":
    main()