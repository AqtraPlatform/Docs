# Aqtra Docs

[English](./README.md) · [Русский](./README.ru.md) · [Deutsch 🇩🇪](https://docs.aqtra.io/de/)

[![Build Status](https://img.shields.io/github/actions/workflow/status/Fershtater/AqtraDocs/docs-quality.yml?branch=main)](https://github.com/Fershtater/AqtraDocs/actions)
[![License](https://img.shields.io/github/license/Fershtater/AqtraDocs)](LICENSE)
[![Languages](https://img.shields.io/badge/languages-EN%20%7C%20DE-blue)](https://docs.aqtra.io)

Official documentation for the Aqtra platform, built with MkDocs Material.

> **What's new**: ✨ German (DE) localization now available! Full German translation with localized navigation, search, and UX enhancements.

> **Note:** QA reports and refactoring documentation are preserved in tag `docs-cleanup-pre` for historical reference.

## 📖 Live Documentation

- **English**: [https://docs.aqtra.io](https://docs.aqtra.io)
- **Deutsch**: [https://docs.aqtra.io/de/](https://docs.aqtra.io/de/) 🇩🇪

**Language switcher** available in the site header for easy switching between EN ↔ DE.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Poetry (recommended) or pip

### Local Development

1. **Install dependencies:**

   Using Poetry (recommended):

   ```bash
   poetry install --no-root
   ```

   Or using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Start development server:**

   ```bash
   poetry run mkdocs serve
   # Or: mkdocs serve
   ```

   Open http://localhost:8000 in your browser.

3. **Build documentation:**

   ```bash
   poetry run mkdocs build --strict
   ```

   The `--strict` flag ensures zero warnings/errors.

## 📁 Project Structure

```
AqtraDocs/
├── docs/                    # Documentation source files
│   ├── assets/             # Images, CSS, JavaScript
│   ├── app-development/    # Application development guides
│   ├── user-interface/     # UI documentation
│   ├── tutorials/          # Step-by-step tutorials
│   └── index.md           # Homepage
├── tools/                  # Diagnostic and fix tools
├── scripts/                # Utility scripts
├── mkdocs.yml             # MkDocs configuration
└── pyproject.toml         # Poetry dependencies
```

## 🛠️ Diagnostic Tools

### Check documentation health:

```bash
poetry run python tools/docs_doctor.py
```

### Fix image paths:

```bash
poetry run python tools/fix_image_paths.py --apply
```

### Fix navigation:

```bash
poetry run python tools/fix_nav.py
```

### Check anchor links:

```bash
poetry run python tools/anchors_doctor.py --apply
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b docs/your-feature
   ```
3. **Make your changes** following our [Style Guide](STYLEGUIDE_DOCS.md)
4. **Test locally:**
   ```bash
   poetry run mkdocs build --strict
   ```
5. **Submit a pull request**

### Documentation Guidelines

- Use relative paths for images: `assets/images/...` (no leading `/`)
- Add stable anchors for external references: `{#stable-id}`
- Run diagnostic tools before committing
- Ensure `mkdocs build --strict` passes with 0 warnings

### Contributing Translations

We use `mkdocs-static-i18n` with folder structure for multi-language support.

**To add or improve German (DE) translations:**

1. Edit files in `docs/de/` directory (mirrors `docs/` structure)
2. **Translate**: headings, text, tables, admonitions, image alt-texts
3. **Preserve**: code blocks, file paths, API endpoints, YAML configs, class names
4. Keep stable anchor IDs: `{: #same-id }` to avoid breaking links
5. Update `nav_translations.de` in `mkdocs.yml` if adding new menu items
6. Test both languages: `mkdocs serve` → check http://localhost:8000/de/

**Adding a new language:**

1. Create `docs/<locale>/` directory
2. Add locale to `plugins.i18n.languages` in `mkdocs.yml`
3. Add `nav_translations.<locale>` for menu items
4. Create `docs/<locale>/assets` symlink: `ln -s ../assets assets`
5. Test: `mkdocs build --strict`

**Translation tools**: See reports in `DE_I18N_REPORT.md` and `DE_I18N_FIX_REPORT.md` for examples.

## 📊 Build & Deploy

### CI/CD

The project uses GitHub Actions for:

- **Build verification** on pull requests
- **Automatic deployment** to GitHub Pages on push to `main`

### Manual Build

```bash
# Clean strict build
poetry run mkdocs build --strict

# Deploy to GitHub Pages (maintainers only)
poetry run mkdocs gh-deploy --force
```

## 📝 Versioning

Documentation releases follow semantic versioning with `docs-v*` tags:

- `docs-v1.0.0` - Initial production release
- `docs-v1.1.0` - Current release (navigation improvements, cleanup)

View all releases: [GitHub Releases](https://github.com/Fershtater/AqtraDocs/releases)

## 🔧 Troubleshooting

### Clean repository artifacts:

```bash
./scripts/clean_repo.sh
```

### Fix broken image links:

```bash
poetry run python tools/fix_image_paths.py --apply
```

### Fix navigation issues:

```bash
poetry run python tools/fix_nav.py
```

### Poetry environment issues:

```bash
# Remove and recreate virtual environment
poetry env remove python
poetry install --no-root
```

## 📄 License

See [LICENSE](LICENSE) file for details.

## 🏷️ Tags

- `docs-v1.1.0` - Current release (navigation improvements, QA cleanup)
- `docs-v1.0` - Production baseline
- `docs-cleanup-pre` - Pre-cleanup snapshot with QA reports

---

**Maintainers:** For release procedures and advanced workflows, see internal documentation in previous releases.
