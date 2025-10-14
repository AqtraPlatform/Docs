#!/usr/bin/env python3
"""
Normalize very long URLs in Markdown files to reference-style links
"""

import re
import csv
from pathlib import Path
from typing import List, Dict, Set, Optional, Tuple
import argparse

class LinkNormalizer:
    def __init__(self, src_dir: str = "docs", threshold: int = 120):
        self.src_dir = Path(src_dir).resolve()
        self.threshold = threshold
        self.normalized_links = []
        self.skipped_links = []
        
    def normalize_links(self, dry_run: bool = False) -> bool:
        """Нормализация длинных ссылок"""
        print("🔗 Запуск нормализации длинных ссылок...")
        print(f"  📁 Исходники: {self.src_dir}")
        print(f"  📏 Порог длины: {self.threshold} символов")
        
        if not self.src_dir.exists():
            print("❌ Папка с исходниками не найдена")
            return False
        
        # Обрабатываем все .md файлы
        md_files = list(self.src_dir.rglob('*.md'))
        print(f"  📁 Найдено {len(md_files)} Markdown файлов")
        
        for md_file in md_files:
            self._normalize_file_links(md_file, dry_run)
        
        # Сохраняем отчеты
        self._save_reports()
        
        # Выводим отчет
        self._print_report()
        
        return True
    
    def _normalize_file_links(self, md_file: Path, dry_run: bool):
        """Нормализация ссылок в одном файле"""
        try:
            content = md_file.read_text(encoding='utf-8')
            original_content = content
            
            # Паттерны для поиска ссылок
            link_patterns = [
                # [text](url) - стандартный markdown
                r'\[([^\]]+)\]\(([^)]+)\)',
                # [text](url "title") - с заголовком
                r'\[([^\]]+)\]\(([^)]+)\s+"([^"]+)"\)',
            ]
            
            # Собираем все ссылки для нормализации
            links_to_normalize = []
            reference_definitions = {}
            
            for pattern in link_patterns:
                for match in re.finditer(pattern, content):
                    text = match.group(1)
                    url = match.group(2)
                    title = match.group(3) if len(match.groups()) > 2 else None
                    
                    # Проверяем длину URL
                    if len(url) > self.threshold and not url.startswith(('http://', 'https://')):
                        # Пропускаем внешние ссылки
                        continue
                    
                    if len(url) > self.threshold:
                        # Генерируем ссылку-ссылку
                        ref_key = self._generate_reference_key(text, url)
                        if ref_key not in reference_definitions:
                            reference_definitions[ref_key] = {
                                'url': url,
                                'title': title,
                                'original_match': match.group(0)
                            }
                            links_to_normalize.append({
                                'text': text,
                                'url': url,
                                'title': title,
                                'ref_key': ref_key,
                                'original_match': match.group(0)
                            })
            
            if not links_to_normalize:
                return
            
            # Заменяем ссылки на ссылки-ссылки
            new_content = content
            for link in links_to_normalize:
                if link['title']:
                    new_ref = f"[{link['text']}][{link['ref_key']}]"
                else:
                    new_ref = f"[{link['text']}][{link['ref_key']}]"
                
                new_content = new_content.replace(link['original_match'], new_ref)
            
            # Добавляем определения ссылок в конец файла
            if reference_definitions:
                ref_section = self._build_reference_section(reference_definitions)
                new_content = new_content.rstrip() + "\n\n" + ref_section + "\n"
            
            # Сохраняем изменения
            if not dry_run and new_content != original_content:
                md_file.write_text(new_content, encoding='utf-8')
                print(f"  ✅ Нормализован: {md_file.relative_to(self.src_dir)}")
            
            # Записываем в отчет
            for link in links_to_normalize:
                self.normalized_links.append({
                    'page': str(md_file.relative_to(self.src_dir)),
                    'original': link['original_match'],
                    'replacement': f"[{link['text']}][{link['ref_key']}]",
                    'ref_key': link['ref_key'],
                    'url': link['url'],
                    'status': 'normalized'
                })
                
        except Exception as e:
            print(f"  ⚠️  Ошибка обработки {md_file}: {e}")
            self.skipped_links.append({
                'page': str(md_file.relative_to(self.src_dir)),
                'original': '',
                'replacement': '',
                'ref_key': '',
                'url': '',
                'status': 'skipped'
            })
    
    def _generate_reference_key(self, text: str, url: str) -> str:
        """Генерирует ключ для ссылки-ссылки"""
        # Создаем ключ на основе текста ссылки
        key = re.sub(r'[^\w\s-]', '', text.lower())
        key = re.sub(r'\s+', '-', key)
        key = key[:20]  # Ограничиваем длину
        
        # Добавляем суффикс если нужно
        counter = 1
        original_key = key
        while f"[{key}]" in self._get_existing_references():
            key = f"{original_key}-{counter}"
            counter += 1
        
        return key
    
    def _get_existing_references(self) -> Set[str]:
        """Получает существующие ссылки-ссылки в проекте"""
        existing = set()
        for md_file in self.src_dir.rglob('*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')
                # Ищем существующие ссылки-ссылки
                refs = re.findall(r'\[([^\]]+)\]', content)
                existing.update(refs)
            except Exception:
                continue
        return existing
    
    def _build_reference_section(self, reference_definitions: Dict) -> str:
        """Строит секцию с определениями ссылок"""
        section = "<!-- Reference links -->\n"
        for ref_key, ref_data in reference_definitions.items():
            if ref_data['title']:
                section += f"[{ref_key}]: {ref_data['url']} \"{ref_data['title']}\"\n"
            else:
                section += f"[{ref_key}]: {ref_data['url']}\n"
        return section
    
    def _save_reports(self):
        """Сохранение отчетов в CSV"""
        build_dir = Path("build")
        build_dir.mkdir(exist_ok=True)
        
        # Объединяем все записи для отчета
        all_records = []
        
        # Добавляем нормализованные ссылки
        for link in self.normalized_links:
            all_records.append({
                'page': link['page'],
                'original': link['original'],
                'replacement': link['replacement'],
                'ref_key': link['ref_key'],
                'url': link['url'],
                'status': link['status']
            })
        
        # Добавляем пропущенные ссылки
        for link in self.skipped_links:
            all_records.append({
                'page': link['page'],
                'original': link['original'],
                'replacement': link['replacement'],
                'ref_key': link['ref_key'],
                'url': link['url'],
                'status': link['status']
            })
        
        # Сохраняем в CSV
        with open(build_dir / "links_normalized.csv", "w", newline="", encoding="utf-8") as f:
            fieldnames = ['page', 'original', 'replacement', 'ref_key', 'url', 'status']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for record in all_records:
                writer.writerow(record)
    
    def _print_report(self):
        """Вывод отчета"""
        print("\n" + "="*60)
        print("📋 ОТЧЕТ О НОРМАЛИЗАЦИИ ССЫЛОК")
        print("="*60)
        
        if self.normalized_links:
            print(f"✅ Нормализовано ссылок: {len(self.normalized_links)}")
            for link in self.normalized_links[:10]:  # Показываем первые 10
                print(f"  {link['page']}: {link['ref_key']} → {link['url'][:50]}...")
            if len(self.normalized_links) > 10:
                print(f"  ... и еще {len(self.normalized_links) - 10} ссылок")
        else:
            print("ℹ️  Нормализация не требуется")
        
        if self.skipped_links:
            print(f"⚠️  Пропущенных файлов: {len(self.skipped_links)}")
        
        print(f"\n📊 Отчет сохранен: build/links_normalized.csv")
        print("="*60)

def main():
    """Главная функция"""
    parser = argparse.ArgumentParser(description='Normalize very long URLs in Markdown files')
    parser.add_argument('--src', default='docs', help='Source directory (default: docs)')
    parser.add_argument('--threshold', type=int, default=120, help='URL length threshold (default: 120)')
    parser.add_argument('--dry-run', action='store_true', help='Only generate report, do not apply fixes')
    parser.add_argument('--apply', action='store_true', help='Apply fixes')
    
    args = parser.parse_args()
    
    if args.apply and args.dry_run:
        print("❌ Нельзя использовать --apply и --dry-run одновременно")
        sys.exit(1)
    
    if not args.apply and not args.dry_run:
        print("ℹ️  Режим не указан. Запуск в режиме --dry-run")
        args.dry_run = True
    
    normalizer = LinkNormalizer(args.src, args.threshold)
    success = normalizer.normalize_links(args.dry_run)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
