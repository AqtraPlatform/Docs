#!/usr/bin/env python3
"""
MkDocs Nav Fixer - автовосстановление навигации MkDocs проекта
"""

import os
import sys
import yaml
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
import difflib

class MkDocsNavFixer:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.docs_dir = self.project_root / "docs"
        self.config_file = None
        self.config = None
        self.fixes_applied = []
        self.broken_items = []
        
        # Найти конфиг файл
        for config_name in ["mkdocs.yml", "mkdocs.yaml"]:
            config_path = self.project_root / config_name
            if config_path.exists():
                self.config_file = config_path
                break
    
    def fix_navigation(self) -> bool:
        """Автовосстановление навигации"""
        print("🔧 Запуск автовосстановления навигации...")
        
        if not self.config_file:
            print("❌ Конфигурационный файл mkdocs.yml не найден")
            return False
        
        if not self.docs_dir.exists():
            print("❌ Папка docs/ не найдена")
            return False
        
        # Загружаем конфиг
        if not self._load_config():
            return False
        
        # Создаем резервную копию
        self._create_backup()
        
        # Сканируем все доступные файлы
        available_files = self._scan_available_files()
        print(f"  📁 Найдено {len(available_files)} файлов в docs/")
        
        # Исправляем навигацию
        if 'nav' in self.config:
            self._fix_nav_recursive(self.config['nav'], available_files)
        
        # Сохраняем исправленный конфиг
        self._save_config()
        
        # Выводим отчет
        self._print_report()
        
        return True
    
    def _load_config(self) -> bool:
        """Загрузка конфигурации"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f)
            print("  ✅ Конфигурация загружена")
            return True
        except Exception as e:
            print(f"  ❌ Ошибка загрузки конфига: {e}")
            return False
    
    def _create_backup(self):
        """Создание резервной копии"""
        backup_file = self.config_file.with_suffix('.yml.bak')
        shutil.copy2(self.config_file, backup_file)
        print(f"  💾 Создана резервная копия: {backup_file}")
    
    def _scan_available_files(self) -> Dict[str, Path]:
        """Сканирование доступных файлов"""
        available_files = {}
        
        for file_path in self.docs_dir.rglob('*.md'):
            relative_path = file_path.relative_to(self.docs_dir)
            # Добавляем разные варианты ключей для поиска
            keys = [
                str(relative_path),
                str(relative_path).replace('\\', '/'),
                relative_path.stem,  # имя файла без расширения
                relative_path.name,  # имя файла с расширением
            ]
            
            for key in keys:
                available_files[key.lower()] = file_path
        
        # Также сканируем .rst файлы
        for file_path in self.docs_dir.rglob('*.rst'):
            relative_path = file_path.relative_to(self.docs_dir)
            keys = [
                str(relative_path),
                str(relative_path).replace('\\', '/'),
                relative_path.stem,
                relative_path.name,
            ]
            
            for key in keys:
                available_files[key.lower()] = file_path
        
        return available_files
    
    def _fix_nav_recursive(self, nav_items: List, available_files: Dict[str, Path]):
        """Рекурсивное исправление навигации"""
        for i, item in enumerate(nav_items):
            if isinstance(item, dict):
                for title, path in item.items():
                    if isinstance(path, str) and (path.endswith('.md') or path.endswith('.rst')):
                        fixed_path = self._find_best_match(path, available_files)
                        if fixed_path:
                            if fixed_path != path:
                                nav_items[i][title] = fixed_path
                                self.fixes_applied.append({
                                    "title": title,
                                    "old_path": path,
                                    "new_path": fixed_path,
                                    "type": "fixed"
                                })
                                print(f"    ✅ Исправлено: {title} → {fixed_path}")
                        else:
                            # Перемещаем в секцию битых ссылок
                            self.broken_items.append({
                                "title": title,
                                "path": path,
                                "type": "broken"
                            })
                            print(f"    ❌ Не найден: {title} ({path})")
                    elif isinstance(path, list):
                        self._fix_nav_recursive(path, available_files)
            elif isinstance(item, str) and (item.endswith('.md') or item.endswith('.rst')):
                fixed_path = self._find_best_match(item, available_files)
                if fixed_path:
                    if fixed_path != item:
                        nav_items[i] = fixed_path
                        self.fixes_applied.append({
                            "title": "Без названия",
                            "old_path": item,
                            "new_path": fixed_path,
                            "type": "fixed"
                        })
                        print(f"    ✅ Исправлено: {item} → {fixed_path}")
                else:
                    self.broken_items.append({
                        "title": "Без названия",
                        "path": item,
                        "type": "broken"
                    })
                    print(f"    ❌ Не найден: {item}")
    
    def _find_best_match(self, original_path: str, available_files: Dict[str, Path]) -> Optional[str]:
        """Поиск лучшего соответствия для файла"""
        # Прямое совпадение
        if original_path.lower() in available_files:
            return original_path
        
        # Нормализация пути
        normalized_path = original_path.replace('\\', '/').lower()
        if normalized_path in available_files:
            return original_path
        
        # Поиск по имени файла
        filename = Path(original_path).name.lower()
        if filename in available_files:
            found_path = available_files[filename]
            return str(found_path.relative_to(self.docs_dir)).replace('\\', '/')
        
        # Поиск по имени без расширения
        stem = Path(original_path).stem.lower()
        for key, file_path in available_files.items():
            if Path(key).stem.lower() == stem:
                return str(file_path.relative_to(self.docs_dir)).replace('\\', '/')
        
        # Нечеткий поиск
        candidates = []
        for key, file_path in available_files.items():
            similarity = difflib.SequenceMatcher(None, original_path.lower(), key).ratio()
            if similarity > 0.6:  # Порог схожести
                candidates.append((similarity, str(file_path.relative_to(self.docs_dir)).replace('\\', '/')))
        
        if candidates:
            # Сортируем по схожести и возвращаем лучший
            candidates.sort(key=lambda x: x[0], reverse=True)
            return candidates[0][1]
        
        return None
    
    def _save_config(self):
        """Сохранение исправленной конфигурации"""
        # Добавляем секцию битых ссылок в конец навигации
        if self.broken_items:
            broken_section = {
                "⚠️ Broken (temp)": []
            }
            
            for item in self.broken_items:
                broken_section["⚠️ Broken (temp)"].append({
                    item["title"]: item["path"]
                })
            
            if 'nav' not in self.config:
                self.config['nav'] = []
            
            self.config['nav'].append(broken_section)
        
        # Сохраняем конфиг
        with open(self.config_file, 'w', encoding='utf-8') as f:
            yaml.dump(self.config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        print("  💾 Конфигурация сохранена")
    
    def _print_report(self):
        """Вывод отчета"""
        print("\n" + "="*60)
        print("📋 ОТЧЕТ О ВОССТАНОВЛЕНИИ НАВИГАЦИИ")
        print("="*60)
        
        print(f"Исправлено файлов: {len(self.fixes_applied)}")
        print(f"Битых ссылок: {len(self.broken_items)}")
        
        if self.fixes_applied:
            print("\n✅ ИСПРАВЛЕННЫЕ ФАЙЛЫ:")
            for fix in self.fixes_applied:
                print(f"  {fix['title']}: {fix['old_path']} → {fix['new_path']}")
        
        if self.broken_items:
            print("\n❌ БИТЫЕ ССЫЛКИ (перемещены в секцию 'Broken'):")
            for item in self.broken_items:
                print(f"  {item['title']}: {item['path']}")
        
        print(f"\n💾 Резервная копия: {self.config_file}.bak")
        print("🔨 Рекомендуется запустить: mkdocs build --strict")
        print("="*60)

def main():
    """Главная функция"""
    project_root = sys.argv[1] if len(sys.argv) > 1 else "."
    
    fixer = MkDocsNavFixer(project_root)
    success = fixer.fix_navigation()
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
