# Contributing to Aqtra Docs

Thank you for your interest in improving Aqtra documentation! This guide will help you get started.

## Prerequisites and Setup

### Requirements

- Python 3.11+
- [Poetry](https://python-poetry.org/) 1.8+ (recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AqtraPlatform/Docs.git
   cd Docs
   ```

2. **Install dependencies:**

   ```bash
   poetry install
   ```

   This installs all required packages including:

   - `mkdocs` and `mkdocs-material`
   - `mkdocs-static-i18n` (for multilingual support)
   - `mkdocs-redirects` (for URL redirects)
   - `ruamel.yaml` (for YAML processing with special tags like `!ENV`)
   - Translation tools and utilities

3. **Set up OpenAI API key (for translation):**

   ```bash
   export OPENAI_API_KEY='your_api_key_here'
   ```

   Or add it to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.).

### Local Development

1. **Start the development server:**

   ```bash
   poetry run mkdocs serve
   ```

   Open http://localhost:8000 in your browser.

2. **Build documentation:**

   ```bash
   poetry run mkdocs build -s
   ```

   The `-s` flag enables strict mode, which catches errors during build.

3. **Make your changes** in the `docs/` directory

4. **Test your changes** (see Quality Checks section below)

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

## Translation Workflow (LLM)

Documentation translations are managed using an LLM-powered translation script that preserves Markdown structure, code blocks, links, and cross-references.

### Main Translation Script

The primary tool is `tools/llm_translate_mkdocs.py`. For convenience, use the wrapper script:

```bash
./scripts/translate_docs.sh --langs fr es pt
```

This script:

- Checks for Poetry and `OPENAI_API_KEY`
- Installs dependencies if needed
- Normalizes `redirect_maps` in `mkdocs.yml` (see Redirect Maps section)
- Runs the translation script

### Translation Commands

**Translate all new languages (fr, es, pt):**

```bash
poetry run python tools/llm_translate_mkdocs.py --langs fr es pt
```

**Translate German from scratch:**

```bash
rm -rf docs/de
mkdir -p docs/de
poetry run python tools/llm_translate_mkdocs.py --langs de --force
```

**Translate specific files only (e.g., tutorials):**

```bash
poetry run python tools/llm_translate_mkdocs.py --langs fr es pt --force --paths \
  tutorials/01-basic-setup.md tutorials/02-data-flow.md tutorials/03-workflow.md
```

**Translate specific files for one language:**

```bash
poetry run python tools/llm_translate_mkdocs.py --langs fr --force --paths \
  app-development/using-python.md overview/getting-started.md
```

### Translation Flags

- `--langs` — Target languages (e.g., `de fr es pt`)
- `--paths` — Translate only specific files (relative to `docs/`)
- `--force` — Overwrite existing translations (without this flag, already translated files are skipped)
- `--only-changed` — Translate only changed files (uses cache, default behavior)
- `--dry-run` — Show what would be done without making changes
- `--no-fallback` — Strict mode (fail if placeholders are lost, default: fallback to original)

**Important:** By default, the script skips existing translated files to preserve manual edits. Use `--force` only when you need to regenerate translations.

### Translation Features

The translation system:

- Preserves Markdown markup and structure
- Does not translate code blocks, inline code, URLs, or technical terms
- Maintains cross-references and internal links
- Automatically adds language prefix (`/{lang}/`) to internal `docs.aqtra.io` links
- Uses chunk-based translation for large files
- Includes placeholder validation and retry mechanism
- Falls back to original content if translation fails (unless `--no-fallback` is used)

## Redirect Maps Normalization

The project uses `mkdocs-redirects` plugin to handle legacy external URLs. Redirect map keys in `mkdocs.yml` need to be normalized to valid markdown paths to ensure strict builds pass without warnings.

### Normalization Tool

Use `tools/normalize_redirect_maps.py` to normalize redirect map keys:

```bash
poetry run python tools/normalize_redirect_maps.py
```

**Normalization rules:**

- Keys ending with `.md` remain unchanged
- Keys ending with `/index` are replaced with `/index.md`
- Other keys have `/index.md` appended

The script creates a backup (`mkdocs.yml.bak`) on first run and is idempotent—running it multiple times won't change already normalized keys.

### Automatic Normalization

The normalization script runs automatically in `scripts/translate_docs.sh`, so you typically don't need to run it manually.

## Quality Checks

After making changes or running translations, verify quality:

### 1. Strict Build

```bash
poetry run mkdocs build -s
```

This catches errors and ensures all files are valid.

### 2. Check for Leftover Placeholders

After translation, verify that no placeholder tokens remain in translated files:

```bash
rg -n "@@URL_|@@IMG_|@@CODE_BLOCK_|@@HTML_" docs/de docs/fr docs/es docs/pt
```

**Expected:** 0 matches. If placeholders are found, the translation may have failed for those sections.

### 3. Additional Checks

```bash
# Run linters
poetry run yamllint .

# Check for broken links and images
poetry run python tools/docs_doctor.py
poetry run python tools/anchors_doctor.py --dry-run
```

### 4. Preview Locally

```bash
poetry run mkdocs serve -a 127.0.0.1:8000
```

## Contributing Translations (Manual)

For manual translation improvements or adding new languages:

### Improving Existing Translations

1. Edit files in `docs/{lang}/` directory (mirrors `docs/` structure)
2. **Translate**: headings, text, tables, admonitions, image alt-texts
3. **Preserve**: code blocks, file paths, API endpoints, YAML configs, class names
4. Keep stable anchor IDs: `{: #same-id }` to avoid breaking links
5. Update `nav_translations.{lang}` in `mkdocs.yml` if adding new menu items
6. Test: `poetry run mkdocs serve` → check http://localhost:8000/{lang}/

### Adding a New Language

1. Create `docs/<locale>/` directory
2. Add locale to `plugins.i18n.languages` in `mkdocs.yml`
3. Add `nav_translations.<locale>` for menu items
4. Create `docs/<locale>/assets` symlink: `ln -s ../assets assets`
5. Test: `poetry run mkdocs build -s`

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

4. **Test locally** (see Quality Checks section):

   ```bash
   poetry run mkdocs build -s
   poetry run yamllint .
   ```

5. **Commit** with clear, descriptive messages
6. **Push** to your fork
7. **Open a Pull Request** with:
   - Clear description of changes
   - Screenshots for visual changes
   - Reference to related issues (if any)

For release process, see [RELEASE.md](RELEASE.md).

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
