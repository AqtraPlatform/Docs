#!/usr/bin/env python3
"""
MkDocs Doctor - диагностика и исправление типовых поломок MkDocs проекта
"""

import os
import sys
import yaml
import json
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
import subprocess
import re

class MkDocsDoctor:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.docs_dir = self.project_root / "docs"
        self.config_file = None
        self.config = None
        self.issues = []
        self.warnings = []
        self.fixes = []
        
        # Найти конфиг файл
        for config_name in ["mkdocs.yml", "mkdocs.yaml"]:
            config_path = self.project_root / config_name
            if config_path.exists():
                self.config_file = config_path
                break
    
    def run_diagnosis(self) -> Dict[str, Any]:
        """Запуск полной диагностики"""
        print("🔍 Запуск диагностики MkDocs проекта...")
        
        # 1. Проверка базовой структуры
        self._check_basic_structure()
        
        # 2. Валидация YAML
        self._validate_yaml()
        
        if self.config:
            # 3. Проверка навигации
            self._check_navigation()
            
            # 4. Проверка ассетов
            self._check_assets()
            
            # 5. Проверка плагинов
            self._check_plugins()
            
            # 6. Проверка зависимостей
            self._check_dependencies()
        
        # Генерация отчета
        report = self._generate_report()
        self._save_report(report)
        
        return report
    
    def _check_basic_structure(self):
        """Проверка базовой структуры проекта"""
        print("  📁 Проверка структуры проекта...")
        
        if not self.config_file:
            self.issues.append({
                "type": "critical",
                "message": "Конфигурационный файл mkdocs.yml не найден",
                "fix": "Создать минимальный mkdocs.yml"
            })
            return
        
        if not self.docs_dir.exists():
            self.issues.append({
                "type": "critical", 
                "message": "Папка docs/ не найдена",
                "fix": "Создать папку docs/ с файлом index.md"
            })
        else:
            print(f"    ✅ Папка docs/ найдена")
    
    def _validate_yaml(self):
        """Валидация YAML конфигурации"""
        print("  📝 Проверка YAML конфигурации...")
        
        if not self.config_file:
            return
            
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f)
            print("    ✅ YAML синтаксис корректен")
        except yaml.YAMLError as e:
            self.issues.append({
                "type": "critical",
                "message": f"Ошибка парсинга YAML: {e}",
                "fix": "Исправить синтаксис YAML"
            })
        except Exception as e:
            self.issues.append({
                "type": "critical",
                "message": f"Ошибка чтения конфига: {e}",
                "fix": "Проверить права доступа к файлу"
            })
    
    def _check_navigation(self):
        """Проверка навигации"""
        print("  🧭 Проверка навигации...")
        
        if not self.config or 'nav' not in self.config:
            self.issues.append({
                "type": "warning",
                "message": "Секция nav не найдена в конфиге",
                "fix": "Добавить секцию nav с базовой навигацией"
            })
            return
        
        missing_files = []
        self._check_nav_recursive(self.config['nav'], missing_files)
        
        if missing_files:
            self.issues.append({
                "type": "error",
                "message": f"Найдено {len(missing_files)} несуществующих файлов в навигации",
                "files": missing_files[:50],  # Показываем только первые 50
                "fix": "Запустить tools/fix_nav.py для автовосстановления"
            })
        else:
            print("    ✅ Все файлы навигации существуют")
    
    def _check_nav_recursive(self, nav_items: List, missing_files: List):
        """Рекурсивная проверка элементов навигации"""
        for item in nav_items:
            if isinstance(item, dict):
                for title, path in item.items():
                    if isinstance(path, str) and path.endswith(('.md', '.rst')):
                        file_path = self.docs_dir / path
                        if not file_path.exists():
                            missing_files.append({
                                "title": title,
                                "path": path,
                                "full_path": str(file_path)
                            })
                    elif isinstance(path, list):
                        self._check_nav_recursive(path, missing_files)
            elif isinstance(item, str) and item.endswith(('.md', '.rst')):
                file_path = self.docs_dir / item
                if not file_path.exists():
                    missing_files.append({
                        "title": "Без названия",
                        "path": item,
                        "full_path": str(file_path)
                    })
    
    def _check_assets(self):
        """Проверка ассетов"""
        print("  🎨 Проверка ассетов...")
        
        if not self.config:
            return
        
        # Проверка логотипов и иконок
        theme_config = self.config.get('theme', {})
        asset_paths = []
        
        for key in ['logo', 'logo_dark', 'favicon']:
            if key in theme_config:
                asset_paths.append((key, theme_config[key]))
        
        # Проверка extra_css и extra_javascript
        for key in ['extra_css', 'extra_javascript']:
            if key in self.config:
                for path in self.config[key]:
                    asset_paths.append((key, path))
        
        for asset_type, path in asset_paths:
            if path.startswith('http'):
                print(f"    ⚠️  {asset_type}: внешняя ссылка {path}")
                continue
                
            # Проверяем в docs/ и в корне проекта
            possible_paths = [
                self.docs_dir / path,
                self.project_root / path,
                self.docs_dir / "assets" / path.split('/')[-1] if '/' in path else path
            ]
            
            found = False
            for check_path in possible_paths:
                if check_path.exists():
                    found = True
                    break
            
            if not found:
                self.issues.append({
                    "type": "error",
                    "message": f"Ассет не найден: {asset_type} = {path}",
                    "fix": f"Проверить путь или переместить файл в docs/{path}"
                })
            else:
                print(f"    ✅ {asset_type}: {path}")
    
    def _check_plugins(self):
        """Проверка плагинов"""
        print("  🔌 Проверка плагинов...")
        
        if not self.config or 'plugins' not in self.config:
            print("    ⚠️  Секция plugins не найдена")
            return
        
        plugins = self.config['plugins']
        for plugin in plugins:
            if isinstance(plugin, dict):
                plugin_name = list(plugin.keys())[0]
            else:
                plugin_name = plugin
            
            # Проверяем, что плагин установлен
            if not self._is_plugin_installed(plugin_name):
                self.issues.append({
                    "type": "error",
                    "message": f"Плагин {plugin_name} не установлен",
                    "fix": f"Установить: pip install {self._get_plugin_package(plugin_name)}"
                })
            else:
                print(f"    ✅ Плагин {plugin_name} установлен")
    
    def _is_plugin_installed(self, plugin_name: str) -> bool:
        """Проверка установки плагина"""
        try:
            result = subprocess.run([
                sys.executable, '-c', 
                f'import {plugin_name.replace("-", "_")}; print("installed")'
            ], capture_output=True, text=True, timeout=10)
            return result.returncode == 0
        except:
            return False
    
    def _get_plugin_package(self, plugin_name: str) -> str:
        """Получение имени пакета для плагина"""
        plugin_packages = {
            'search': 'mkdocs',
            'glightbox': 'mkdocs-glightbox',
            'mermaid2': 'mkdocs-mermaid2-plugin',
            'i18n': 'mkdocs-static-i18n',
            'git-revision-date-localized': 'mkdocs-git-revision-date-localized-plugin',
            'mkdocstrings': 'mkdocstrings[python]',
            'redirects': 'mkdocs-redirects'
        }
        return plugin_packages.get(plugin_name, f'mkdocs-{plugin_name}')
    
    def _check_dependencies(self):
        """Проверка зависимостей"""
        print("  📦 Проверка зависимостей...")
        
        # Проверяем requirements.txt
        req_file = self.project_root / "requirements.txt"
        if req_file.exists():
            print("    ✅ requirements.txt найден")
        else:
            self.warnings.append({
                "type": "warning",
                "message": "requirements.txt не найден",
                "fix": "Создать requirements.txt с зависимостями"
            })
        
        # Проверяем pyproject.toml
        pyproject_file = self.project_root / "pyproject.toml"
        if pyproject_file.exists():
            print("    ✅ pyproject.toml найден")
    
    def _generate_report(self) -> Dict[str, Any]:
        """Генерация отчета"""
        report = {
            "timestamp": str(Path.cwd()),
            "project_root": str(self.project_root),
            "config_file": str(self.config_file) if self.config_file else None,
            "summary": {
                "total_issues": len(self.issues),
                "critical_issues": len([i for i in self.issues if i['type'] == 'critical']),
                "errors": len([i for i in self.issues if i['type'] == 'error']),
                "warnings": len(self.warnings)
            },
            "issues": self.issues,
            "warnings": self.warnings,
            "recommendations": self._generate_recommendations()
        }
        
        return report
    
    def _generate_recommendations(self) -> List[str]:
        """Генерация рекомендаций"""
        recommendations = []
        
        if any(i['type'] == 'critical' for i in self.issues):
            recommendations.append("🚨 Критические ошибки требуют немедленного исправления")
        
        if any(i['type'] == 'error' for i in self.issues):
            recommendations.append("🔧 Запустите tools/fix_nav.py для автовосстановления навигации")
        
        if not self.config:
            recommendations.append("📝 Создайте минимальный mkdocs.yml для базовой сборки")
        
        recommendations.extend([
            "📚 Убедитесь, что все зависимости установлены: pip install -r requirements.txt",
            "🔨 Протестируйте сборку: mkdocs build --strict",
            "🌐 Проверьте CI/CD pipeline для автоматической сборки"
        ])
        
        return recommendations
    
    def _save_report(self, report: Dict[str, Any]):
        """Сохранение отчета"""
        # Создаем папку build если не существует
        build_dir = self.project_root / "build"
        build_dir.mkdir(exist_ok=True)
        
        # Сохраняем JSON отчет
        report_file = build_dir / "doctor_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Сохраняем Markdown отчет
        md_report_file = build_dir / "doctor_report.md"
        with open(md_report_file, 'w', encoding='utf-8') as f:
            f.write(self._format_markdown_report(report))
        
        print(f"  📊 Отчет сохранен: {md_report_file}")
    
    def _format_markdown_report(self, report: Dict[str, Any]) -> str:
        """Форматирование отчета в Markdown"""
        md = f"""# MkDocs Doctor Report

**Время:** {report['timestamp']}  
**Проект:** {report['project_root']}  
**Конфиг:** {report['config_file'] or 'Не найден'}

## 📊 Сводка

- **Всего проблем:** {report['summary']['total_issues']}
- **Критические:** {report['summary']['critical_issues']}
- **Ошибки:** {report['summary']['errors']}
- **Предупреждения:** {report['summary']['warnings']}

## 🚨 Проблемы

"""
        
        if report['issues']:
            for i, issue in enumerate(report['issues'], 1):
                md += f"### {i}. {issue['type'].upper()}: {issue['message']}\n\n"
                if 'files' in issue:
                    md += "**Файлы:**\n"
                    for file_info in issue['files'][:10]:  # Показываем первые 10
                        md += f"- {file_info['title']}: `{file_info['path']}`\n"
                    if len(issue['files']) > 10:
                        md += f"- ... и еще {len(issue['files']) - 10} файлов\n"
                    md += "\n"
                md += f"**Исправление:** {issue['fix']}\n\n"
        else:
            md += "✅ Проблем не найдено!\n\n"
        
        if report['warnings']:
            md += "## ⚠️ Предупреждения\n\n"
            for warning in report['warnings']:
                md += f"- {warning['message']} → {warning['fix']}\n"
            md += "\n"
        
        md += "## 💡 Рекомендации\n\n"
        for rec in report['recommendations']:
            md += f"- {rec}\n"
        
        return md
    
    def print_summary(self, report: Dict[str, Any]):
        """Вывод краткой сводки в консоль"""
        print("\n" + "="*60)
        print("📋 СВОДКА ДИАГНОСТИКИ")
        print("="*60)
        
        summary = report['summary']
        print(f"Всего проблем: {summary['total_issues']}")
        print(f"Критические: {summary['critical_issues']}")
        print(f"Ошибки: {summary['errors']}")
        print(f"Предупреждения: {summary['warnings']}")
        
        if summary['total_issues'] == 0:
            print("\n🎉 Отлично! Проблем не найдено.")
        else:
            print(f"\n📊 Подробный отчет: build/doctor_report.md")
            print(f"🔧 Для автовосстановления: python tools/fix_nav.py")
        
        print("="*60)

def main():
    """Главная функция"""
    project_root = sys.argv[1] if len(sys.argv) > 1 else "."
    
    doctor = MkDocsDoctor(project_root)
    report = doctor.run_diagnosis()
    doctor.print_summary(report)
    
    # Возвращаем код выхода в зависимости от критических ошибок
    if report['summary']['critical_issues'] > 0:
        sys.exit(1)
    elif report['summary']['errors'] > 0:
        sys.exit(2)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
