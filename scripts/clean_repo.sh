#!/bin/bash
# Clean repository script - removes build artifacts, caches, and backup files
# Idempotent: safe to run multiple times

set -e

echo "🧹 Cleaning repository..."

# Function to safely remove files/directories
safe_remove() {
    local pattern="$1"
    local description="$2"
    
    if ls $pattern 1> /dev/null 2>&1; then
        echo "  Removing $description..."
        rm -rf $pattern
    else
        echo "  No $description found (already clean)"
    fi
}

# Python artifacts
safe_remove "__pycache__/" "Python cache directories"
safe_remove "*.pyc" "Python compiled files"
safe_remove "*.pyo" "Python optimized files"
safe_remove "*.pyd" "Python extension modules"
safe_remove "*.so" "Python shared objects"

# Virtual environments
safe_remove ".venv/" "Python virtual environment (.venv)"
safe_remove "venv/" "Python virtual environment (venv)"
safe_remove "ENV/" "Python virtual environment (ENV)"
safe_remove "env/" "Python virtual environment (env)"
safe_remove ".env" "Environment file"

# Build artifacts
safe_remove "site/" "MkDocs site directory"
safe_remove "build/" "Build directory"
safe_remove "dist/" "Distribution directory"
safe_remove "*.egg-info/" "Python egg info directories"

# Caches
safe_remove ".cache/" "Cache directory"
safe_remove ".mypy_cache/" "MyPy cache"
safe_remove ".pytest_cache/" "Pytest cache"
safe_remove ".ruff_cache/" "Ruff cache"
safe_remove ".coverage" "Coverage file"

# Node.js artifacts (if present)
safe_remove "node_modules/" "Node.js modules"
safe_remove "package-lock.json" "NPM lock file"
safe_remove "yarn.lock" "Yarn lock file"

# Old package managers
safe_remove "requirements*.txt" "Requirements files"
safe_remove "Pipfile" "Pipfile"
safe_remove "Pipfile.lock" "Pipfile lock"
safe_remove "setup.py" "Setup.py"
safe_remove "setup.cfg" "Setup.cfg"

# Editor and system files
safe_remove ".DS_Store" "macOS system files"
safe_remove "Thumbs.db" "Windows thumbnail cache"
safe_remove ".idea/" "IntelliJ IDEA files"
safe_remove ".vscode/" "VS Code files"
safe_remove "*.iml" "IntelliJ module files"

# Backup files
safe_remove "*.bak" "Backup files"
safe_remove "*.old" "Old files"
safe_remove "*.orig" "Original files"
safe_remove "*.tmp" "Temporary files"
safe_remove "*~" "Temporary files"
safe_remove "*.swp" "Vim swap files"
safe_remove "*.swo" "Vim swap files"
safe_remove "*.backup" "Backup files"
safe_remove "*.yml.bak" "YAML backup files"
safe_remove "*.md.bak" "Markdown backup files"
safe_remove "mkdocs.yml.bak" "MkDocs config backup"

# Archives and binaries
safe_remove "*.zip" "ZIP archives"
safe_remove "*.tar" "TAR archives"
safe_remove "*.tar.gz" "GZIP TAR archives"
safe_remove "*.7z" "7-Zip archives"
safe_remove "*.exe" "Windows executables"
safe_remove "*.dll" "Windows DLLs"

# Log files
safe_remove "*.log" "Log files"
safe_remove "logs/" "Log directories"

# Temporary directories
safe_remove ".tmp/" "Temporary directory"
safe_remove "temp/" "Temporary directory"

echo "✅ Repository cleaned successfully!"
echo "💡 Run 'git status' to see what was removed"
