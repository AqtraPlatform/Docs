#!/usr/bin/env bash
# Quick deployment script for docs-v1.2.0
set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  🚀 Aqtra Docs v1.2.0 - Deployment Script                 ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Step 1: Pre-flight checks
echo "📋 Step 1/5: Pre-flight checks..."
if [ "$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then
    echo "❌ Not on main branch!"
    exit 1
fi
echo "✅ On main branch"

# Step 2: Pull latest
echo ""
echo "📥 Step 2/5: Pull latest changes..."
git pull --ff-only
echo "✅ Up to date"

# Step 3: Clean build
echo ""
echo "🔨 Step 3/5: Building docs (strict mode)..."
rm -rf site/
mkdocs build --strict
echo "✅ Build successful"

# Step 4: Verify
echo ""
echo "🔍 Step 4/5: Verification..."
test -d site/de || (echo "❌ site/de/ not found!" && exit 1)
grep -q "Willkommen" site/de/index.html || (echo "❌ DE content missing!" && exit 1)
grep -q "back-to-top.js" site/index.html || (echo "❌ Back-to-Top missing!" && exit 1)
echo "✅ DE content verified"
echo "✅ Back-to-Top verified"

# Step 5: Tag
echo ""
echo "🏷️  Step 5/5: Creating release tag..."
VER=${1:-docs-v1.2.0}

if git rev-parse "$VER" >/dev/null 2>&1; then
    echo "⚠️  Tag $VER already exists. Skipping tag creation."
else
    git tag -a "$VER" -F RELEASE_NOTES_v1.2.0.md
    echo "✅ Tag created: $VER"
    
    read -p "Push tag to remote? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git push origin "$VER"
        echo "✅ Tag pushed"
    fi
fi

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  ✅ Deployment prepared successfully!                      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "📝 Next steps:"
echo ""
echo "  1. Create GitHub release:"
echo "     gh release create $VER --notes-file RELEASE_NOTES_v1.2.0.md --latest"
echo ""
echo "  2. Deploy to production:"
echo "     mkdocs gh-deploy --force"
echo ""
echo "  3. Verify:"
echo "     https://docs.aqtra.io      (EN)"
echo "     https://docs.aqtra.io/de/  (DE)"
echo ""

