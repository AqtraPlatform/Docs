# Contributing to Aqtra Docs

Thank you for your interest in improving Aqtra documentation! This guide will help you get started.

## Quick Start for Contributors

### Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/) 1.8+ (recommended) or pip

### Local Development Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AqtraPlatform/Docs.git
   cd Docs
   ```

2. **Install dependencies:**

   Using Poetry (recommended):

   ```bash
   poetry install --no-root
   ```

   Or using pip:

   ```bash
   pip install mkdocs mkdocs-material mkdocs-glightbox mkdocs-mermaid2-plugin \
     mkdocs-git-revision-date-localized-plugin mkdocs-static-i18n mkdocs-minify-plugin
   ```

3. **Start the development server:**

   ```bash
   poetry run mkdocs serve
   # Or: mkdocs serve
   ```

   Open http://localhost:8000 in your browser.

4. **Make your changes** in the `docs/` directory

5. **Test your changes:**

   ```bash
   # Build in strict mode (catches errors)
   poetry run mkdocs build --strict

   # Run linters
   poetry run yamllint .

   # Check for broken links and images
   poetry run python tools/docs_doctor.py
   poetry run python tools/anchors_doctor.py --dry-run
   ```

## Project Structure

```text
Docs/
├── docs/                       # Documentation source files
│   ├── assets/                # Images, CSS, JavaScript
│   │   ├── brand/             # Logos and branding
│   │   ├── images/            # Screenshots and diagrams
│   │   ├── js/                # Custom JavaScript
│   │   └── styles/            # Custom CSS
│   ├── app-development/       # App development guides
│   │   ├── ui-components/     # UI component reference
│   │   ├── data-flow-components/ # Data flow reference
│   │   └── workflow-components/  # Workflow reference
│   ├── user-interface/        # UI documentation
│   ├── tutorials/             # Step-by-step tutorials
│   ├── de/                    # German translations
│   └── index.md              # Homepage
├── .github/workflows/         # CI/CD workflows
├── tools/                     # Diagnostic and fix tools
├── scripts/                   # Utility scripts
├── mkdocs.yml                # MkDocs configuration
└── pyproject.toml            # Poetry dependencies
```

## Documentation Guidelines

### Writing Style

- Use clear, concise language
- Write in second person ("you") when addressing readers
- Use active voice
- Break up long paragraphs
- Use headings to organize content
- Include examples where helpful

### Formatting

- **Headings**: Use ATX style (`#`, `##`, `###`)
- **Images**: Use relative paths `assets/images/...` (no leading `/`)
- **Links**: Use descriptive text, not "click here"
- **Code blocks**: Include language identifier for syntax highlighting
- **Stable anchors**: Add custom IDs for important sections: `## Heading {: #stable-id }`

### Images

- Place images in `docs/assets/images/<section>/`
- Use descriptive filenames (kebab-case)
- Include alt text for accessibility
- Optimize images before committing (use `scripts/optimize_images.sh`)

## Contributing Translations

We use `mkdocs-static-i18n` with folder structure for multi-language support.

### Improving German (DE) Translations

1. Edit files in `docs/de/` directory (mirrors `docs/` structure)
2. **Translate**: headings, text, tables, admonitions, image alt-texts
3. **Preserve**: code blocks, file paths, API endpoints, YAML configs, class names
4. Keep stable anchor IDs: `{: #same-id }` to avoid breaking links
5. Update `nav_translations.de` in `mkdocs.yml` if adding new menu items
6. Test both languages: `mkdocs serve` → check http://localhost:8000/de/

### Adding a New Language

1. Create `docs/<locale>/` directory
2. Add locale to `plugins.i18n.languages` in `mkdocs.yml`
3. Add `nav_translations.<locale>` for menu items
4. Create `docs/<locale>/assets` symlink: `ln -s ../assets assets`
5. Test: `mkdocs build --strict`

## Diagnostic Tools

The `tools/` directory contains helpful utilities:

### Check Documentation Health

```bash
poetry run python tools/docs_doctor.py
```

### Fix Image Paths

```bash
# Dry run (shows what would change)
poetry run python tools/fix_image_paths.py --dry-run

# Apply fixes
poetry run python tools/fix_image_paths.py --apply
```

### Fix Anchor Links

```bash
# Dry run
poetry run python tools/anchors_doctor.py --dry-run

# Apply fixes
poetry run python tools/anchors_doctor.py --apply
```

### Clean Build Artifacts

```bash
./scripts/clean_repo.sh
```

## Pull Request Process

1. **Fork** the repository
2. **Create a branch** from `main`:

   ```bash
   git checkout -b docs/your-feature-name
   ```

3. **Make your changes** following the guidelines above

4. **Test locally**:

   ```bash
   poetry run mkdocs build --strict
   poetry run yamllint .
   ```

5. **Commit** with clear, descriptive messages
6. **Push** to your fork
7. **Open a Pull Request** with:
   - Clear description of changes
   - Screenshots for visual changes
   - Reference to related issues (if any)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy toward other contributors

## Getting Help

- **Questions?** Open a [Discussion](https://github.com/AqtraPlatform/Docs/discussions)
- **Found a bug?** Open an [Issue](https://github.com/AqtraPlatform/Docs/issues)
- **Need guidance?** Tag maintainers in your PR or issue

## License

By contributing to Aqtra Docs, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make Aqtra documentation better! 🎉
