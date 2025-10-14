#!/usr/bin/env python3
"""
Конвертер .po файлов в локализованные .md файлы для MkDocs
"""
import argparse
import re
import sys
import shutil
import logging
from pathlib import Path
from typing import Dict, Tuple, List, Optional
import polib
import yaml

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Регулярные выражения для защиты кода
CODE_FENCE = re.compile(r"(^```[\s\S]*?^```)|(^~~~[\s\S]*?^~~~)", re.MULTILINE)
INLINE_CODE = re.compile(r"`[^`]+`")
HTML_TAGS = re.compile(r"<[^>]+>")
LINKS = re.compile(r"\[([^\]]+)\]\([^)]+\)")
IMAGES = re.compile(r"!\[([^\]]*)\]\([^)]+\)")


def load_glossary(path: Path) -> Dict[str, str]:
    """Загружает глоссарий терминов из YAML файла"""
    if not path or not path.exists():
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        return data or {}
    except Exception as e:
        logger.warning(f"Не удалось загрузить глоссарий {path}: {e}")
        return {}


def split_protected(text: str) -> List[Tuple[bool, str]]:
    """Разделяет текст на защищенные (код) и обычные части"""
    parts = []
    last = 0
    
    for m in CODE_FENCE.finditer(text):
        if m.start() > last:
            parts.append((False, text[last:m.start()]))
        parts.append((True, m.group(0)))
        last = m.end()
    
    if last < len(text):
        parts.append((False, text[last:]))
    
    return parts


def normalize(s: str) -> str:
    """Нормализует строку для сравнения"""
    return re.sub(r"\s+", " ", s.strip())


def protect_inline_elements(text: str) -> Tuple[str, List[str]]:
    """Защищает инлайн элементы (код, ссылки, изображения) от перевода"""
    placeholders = []
    
    def protect_inline_code(match):
        placeholders.append(match.group(0))
        return f"§INLINE_CODE_{len(placeholders)-1}§"
    
    def protect_links(match):
        placeholders.append(match.group(0))
        return f"§LINK_{len(placeholders)-1}§"
    
    def protect_images(match):
        placeholders.append(match.group(0))
        return f"§IMAGE_{len(placeholders)-1}§"
    
    def protect_html(match):
        placeholders.append(match.group(0))
        return f"§HTML_{len(placeholders)-1}§"
    
    # Защищаем в порядке от более специфичных к менее специфичным
    text = INLINE_CODE.sub(protect_inline_code, text)
    text = IMAGES.sub(protect_images, text)
    text = LINKS.sub(protect_links, text)
    text = HTML_TAGS.sub(protect_html, text)
    
    return text, placeholders


def restore_inline_elements(text: str, placeholders: List[str]) -> str:
    """Восстанавливает защищенные инлайн элементы"""
    def restore(match):
        element_type = match.group(1)
        idx = int(match.group(2))
        if 0 <= idx < len(placeholders):
            return placeholders[idx]
        return match.group(0)
    
    text = re.sub(r"§(INLINE_CODE|LINK|IMAGE|HTML)_(\d+)§", restore, text)
    return text


def apply_po_to_text(text: str, po_map: Dict[str, Tuple[str, Dict]], allow_fuzzy: bool = False) -> str:
    """Применяет переводы из .po файла к тексту"""
    chunks = split_protected(text)
    out = []
    
    for is_code, chunk in chunks:
        if is_code:
            out.append(chunk)
            continue
        
        # Защищаем инлайн элементы
        protected_text, placeholders = protect_inline_elements(chunk)
        
        # Применяем переводы
        for src, (dst, flags) in po_map.items():
            if not dst or not src:
                continue
            if flags.get("fuzzy") and not allow_fuzzy:
                continue
            
            # Точное совпадение
            if src in protected_text:
                protected_text = protected_text.replace(src, dst)
                continue
            
            # Нормализованное совпадение
            norm_src = normalize(src)
            norm_dst = normalize(dst)
            if norm_src in normalize(protected_text):
                # Заменяем по нормализованному тексту
                lines = protected_text.split('\n')
                for i, line in enumerate(lines):
                    if normalize(src) in normalize(line):
                        lines[i] = line.replace(normalize(src), normalize(dst))
                protected_text = '\n'.join(lines)
        
        # Восстанавливаем инлайн элементы
        final_text = restore_inline_elements(protected_text, placeholders)
        out.append(final_text)
    
    return "".join(out)


def build_po_map(po_path: Path) -> Dict[str, Tuple[str, Dict]]:
    """Строит карту переводов из .po файла"""
    try:
        po = polib.pofile(str(po_path))
        m = {}
        for entry in po:
            src = entry.msgid
            dst = entry.msgstr or ""
            flags = {"fuzzy": "fuzzy" in entry.flags}
            if src and src not in m:
                m[src] = (dst, flags)
        return m
    except Exception as e:
        logger.error(f"Ошибка при чтении {po_path}: {e}")
        return {}


def find_matching_po_files(md_path: Path, po_dir: Path) -> List[Path]:
    """Находит соответствующие .po файлы для .md файла"""
    # Получаем относительный путь от docs/
    try:
        rel_path = md_path.relative_to(Path("docs"))
    except ValueError:
        return []
    
    # Ищем .po файлы с похожими именами
    po_files = []
    
    # Прямое соответствие по имени файла
    po_name = rel_path.with_suffix('.po')
    po_path = po_dir / po_name
    if po_path.exists():
        po_files.append(po_path)
    
    # Поиск в подпапках
    for po_file in po_dir.rglob(f"{rel_path.stem}.po"):
        po_files.append(po_file)
    
    # Поиск по частичному совпадению
    for po_file in po_dir.rglob("*.po"):
        if rel_path.stem in po_file.stem or po_file.stem in rel_path.stem:
            po_files.append(po_file)
    
    return po_files


def process_md_file(md_path: Path, po_map: Dict[str, Tuple[str, Dict]], 
                   allow_fuzzy: bool = False, glossary: Dict[str, str] = None) -> Tuple[bool, int]:
    """Обрабатывает один .md файл"""
    try:
        text = md_path.read_text(encoding="utf-8")
        original_text = text
        
        # Применяем переводы
        text = apply_po_to_text(text, po_map, allow_fuzzy)
        
        # Применяем глоссарий
        if glossary:
            for term, replacement in glossary.items():
                # Заменяем только целые слова
                pattern = r'\b' + re.escape(term) + r'\b'
                text = re.sub(pattern, replacement, text)
        
        # Проверяем, изменился ли файл
        if text != original_text:
            md_path.write_text(text, encoding="utf-8")
            return True, 1
        return False, 0
        
    except Exception as e:
        logger.error(f"Ошибка при обработке {md_path}: {e}")
        return False, 0


def main():
    parser = argparse.ArgumentParser(description="Конвертер .po файлов в локализованные .md файлы")
    parser.add_argument("--lang", required=True, help="Язык для конверсии (en, ru)")
    parser.add_argument("--po-root", default="locale", help="Корневая папка с .po файлами")
    parser.add_argument("--src", default="docs", help="Исходная папка с .md файлами")
    parser.add_argument("--dst", help="Папка назначения (по умолчанию docs.{lang})")
    parser.add_argument("--glossary", default="tools/glossary.yaml", help="Файл глоссария")
    parser.add_argument("--allow-fuzzy", action="store_true", help="Разрешить fuzzy переводы")
    parser.add_argument("--dry-run", action="store_true", help="Только показать что будет сделано")
    parser.add_argument("--verbose", "-v", action="store_true", help="Подробный вывод")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Определяем пути
    src_root = Path(args.src)
    dst_root = Path(args.dst or f"{args.src}.{args.lang}")
    po_dir = Path(args.po_root) / args.lang / "LC_MESSAGES"
    
    # Проверяем существование папок
    if not src_root.exists():
        logger.error(f"Исходная папка не найдена: {src_root}")
        sys.exit(1)
    
    if not po_dir.exists():
        logger.error(f"Папка с .po файлами не найдена: {po_dir}")
        sys.exit(1)
    
    # Загружаем глоссарий
    glossary = load_glossary(Path(args.glossary))
    if glossary:
        logger.info(f"Загружен глоссарий: {len(glossary)} терминов")
    
    # Создаем папку назначения
    if not args.dry_run:
        if dst_root.exists():
            logger.info(f"Удаляем существующую папку: {dst_root}")
            shutil.rmtree(dst_root)
        logger.info(f"Копируем файлы из {src_root} в {dst_root}")
        shutil.copytree(src_root, dst_root)
    
    # Собираем все .po файлы
    logger.info(f"Сканируем .po файлы в {po_dir}")
    po_map = {}
    po_files = list(po_dir.rglob("*.po"))
    logger.info(f"Найдено {len(po_files)} .po файлов")
    
    for po_file in po_files:
        file_map = build_po_map(po_file)
        po_map.update(file_map)
        logger.debug(f"Загружен {po_file}: {len(file_map)} записей")
    
    logger.info(f"Всего загружено {len(po_map)} переводов")
    
    # Обрабатываем .md файлы
    total_files = 0
    modified_files = 0
    total_entries = 0
    
    for md_file in dst_root.rglob("*.md"):
        total_files += 1
        logger.debug(f"Обрабатываем {md_file}")
        
        if not args.dry_run:
            modified, entries = process_md_file(md_file, po_map, args.allow_fuzzy, glossary)
            if modified:
                modified_files += 1
            total_entries += entries
        else:
            # В dry-run режиме просто считаем
            modified_files += 1
            total_entries += 1
    
    # Выводим статистику
    print(f"\n=== Статистика для языка {args.lang} ===")
    print(f"Обработано файлов: {total_files}")
    print(f"Изменено файлов: {modified_files}")
    print(f"Всего переводов: {len(po_map)}")
    print(f"Применено переводов: {total_entries}")
    print(f"Выходная папка: {dst_root}")
    
    if args.dry_run:
        print("(DRY RUN - файлы не изменены)")
    
    logger.info("Конверсия завершена")


if __name__ == "__main__":
    main()
