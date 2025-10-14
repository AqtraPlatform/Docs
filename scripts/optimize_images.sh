#!/usr/bin/env bash
set -euo pipefail
shopt -s globstar nullglob

# Ужать PNG/JPG без потери видимости диффов
for f in docs/assets/**/*.{png,PNG}; do
  [ -f "$f" ] || continue
  command -v oxipng >/dev/null && oxipng -o4 -q "$f" || true
done
for f in docs/assets/**/*.{jpg,JPG,jpeg,JPEG}; do
  [ -f "$f" ] || continue
  command -v jpegoptim >/dev/null && jpegoptim --strip-all --max=85 "$f" || true
done

echo "✓ images optimized (best-effort)"
