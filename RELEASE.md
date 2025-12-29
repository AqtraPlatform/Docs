# Release Process

This guide describes the process for releasing documentation updates to the main branch.

## Prerequisites

- All translations are complete (if applicable)
- All quality checks pass
- You have write access to the repository

## Release Steps

### 1. Run Quality Checks

Before releasing, ensure everything builds correctly:

```bash
poetry run mkdocs build -s
```

If you've run translations, check for leftover placeholders:

```bash
rg -n "@@URL_|@@IMG_|@@CODE_BLOCK_|@@HTML_" docs/de docs/fr docs/es docs/pt
```

Expected: 0 matches.

### 2. Update Translations (if needed)

If documentation has changed, update translations as needed:

```bash
./scripts/translate_docs.sh --langs fr es pt
```

Or translate specific files:

```bash
poetry run python tools/llm_translate_mkdocs.py --langs fr es pt --paths \
  path/to/file.md
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed translation instructions.

### 3. Review Changes

Review what will be committed:

```bash
git status
git diff
```

Verify that:

- Only intended changes are included
- No temporary files or build artifacts are staged
- Translations are complete (if applicable)

### 4. Stage Changes

Stage all changes:

```bash
git add -A
```

Or stage specific files:

```bash
git add docs/ scripts/ tools/ mkdocs.yml pyproject.toml
```

### 5. Create Release Commit

Create a release commit with a descriptive message:

```bash
git commit -m "release: multilingual docs (de/fr/es/pt) + translation pipeline"
```

Or for a more specific release:

```bash
git commit -m "release: update documentation and translations"
```

### 6. Update and Push

Before pushing, update your local branch with remote changes:

```bash
git pull --rebase origin main
```

If there are conflicts, resolve them and continue:

```bash
# After resolving conflicts
git rebase --continue
```

Then push to main:

```bash
git push origin main
```

## PR-Based Workflow (Alternative)

If your project uses pull requests for releases:

### 1. Create Release Branch

```bash
git checkout -b release/i18n-docs
```

### 2. Make Changes and Commit

Follow steps 1-5 above on your release branch.

### 3. Push Branch and Open PR

```bash
git push origin release/i18n-docs
```

Then open a Pull Request to `main` on GitHub with:

- Clear description of changes
- Reference to related issues (if any)
- Confirmation that quality checks passed

### 4. Review and Merge

After PR review and approval, merge the PR to `main`.

## Post-Release

After pushing to main:

1. **Verify the site builds** (if CI/CD is configured, check the build status)
2. **Check the live site** at https://docs.aqtra.io to ensure changes are deployed correctly
3. **Monitor for issues** in the first few hours after deployment

## Troubleshooting

### Build Failures

If `mkdocs build -s` fails:

1. Check error messages for specific file issues
2. Verify all Markdown files are valid
3. Check for broken links using `poetry run python tools/docs_doctor.py`
4. Ensure redirect maps are normalized (see [CONTRIBUTING.md](CONTRIBUTING.md))

### Translation Issues

If translations fail:

1. Check `OPENAI_API_KEY` is set correctly
2. Review translation logs for specific errors
3. Check for placeholder validation failures
4. Use `--no-fallback` flag to identify problematic files

### Merge Conflicts

If `git pull --rebase origin main` has conflicts:

1. Resolve conflicts manually
2. Test the build after resolution: `poetry run mkdocs build -s`
3. Continue rebase: `git rebase --continue`

---

For contribution guidelines and translation workflow, see [CONTRIBUTING.md](CONTRIBUTING.md).
