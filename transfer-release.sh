#!/usr/bin/env bash
#
# transfer-release.sh - Copy a GitHub release from one repo to another
#
# Usage:
#   ./transfer-release.sh \
#     --src Fershtater/AqtraDocs \
#     --dst AqtraPlatform/Docs \
#     --tag docs-v1.1.0 \
#     [--create-branch] [--draft] [--prerelease] [--dry-run] [--verbose]
#

set -euo pipefail

# ============================================================================
# Configuration & Defaults
# ============================================================================

SRC_REPO=""
DST_REPO=""
TAG=""
CREATE_BRANCH=0
DRAFT=0
PRERELEASE=0
DRY_RUN=0
VERBOSE=0

TEMP_DIR=""

# ============================================================================
# Helper Functions
# ============================================================================

log() {
  echo "[INFO] $*"
}

log_verbose() {
  [[ $VERBOSE -eq 1 ]] && echo "[DEBUG] $*" || true
}

error() {
  echo "[ERROR] $*" >&2
  exit 1
}

cleanup() {
  if [[ -n "$TEMP_DIR" && -d "$TEMP_DIR" ]]; then
    log_verbose "Cleaning up temp directory: $TEMP_DIR"
    rm -rf "$TEMP_DIR"
  fi
}

trap cleanup EXIT

usage() {
  cat <<EOF
Usage: $0 [OPTIONS]

Copy a GitHub release (tag, notes, assets) from one repo to another.

Required options:
  --src OWNER/REPO    Source repository (e.g., Fershtater/AqtraDocs)
  --dst OWNER/REPO    Destination repository (e.g., AqtraPlatform/Docs)
  --tag TAG_NAME      Tag to transfer (e.g., docs-v1.1.0)

Optional flags:
  --create-branch     Create and push release-<TAG> branch from tag
  --draft             Create release as draft
  --prerelease        Mark release as prerelease
  --dry-run           Check without making changes
  --verbose           Enable verbose logging
  -h, --help          Show this help

Examples:
  # Basic transfer
  $0 --src Fershtater/AqtraDocs --dst AqtraPlatform/Docs --tag docs-v1.1.0

  # Dry run with verbose logging
  $0 --src Fershtater/AqtraDocs --dst AqtraPlatform/Docs --tag docs-v1.1.0 --dry-run --verbose

  # Create as draft with branch
  $0 --src Fershtater/AqtraDocs --dst AqtraPlatform/Docs --tag docs-v1.1.0 --draft --create-branch

EOF
  exit 0
}

# ============================================================================
# Argument Parsing
# ============================================================================

while [[ $# -gt 0 ]]; do
  case $1 in
    --src)
      SRC_REPO="$2"
      shift 2
      ;;
    --dst)
      DST_REPO="$2"
      shift 2
      ;;
    --tag)
      TAG="$2"
      shift 2
      ;;
    --create-branch)
      CREATE_BRANCH=1
      shift
      ;;
    --draft)
      DRAFT=1
      shift
      ;;
    --prerelease)
      PRERELEASE=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --verbose)
      VERBOSE=1
      shift
      ;;
    -h|--help)
      usage
      ;;
    *)
      error "Unknown option: $1. Use --help for usage."
      ;;
  esac
done

# ============================================================================
# Validation
# ============================================================================

[[ -z "$SRC_REPO" ]] && error "Missing --src OWNER/REPO"
[[ -z "$DST_REPO" ]] && error "Missing --dst OWNER/REPO"
[[ -z "$TAG" ]] && error "Missing --tag TAG_NAME"

log "Transfer configuration:"
log "  Source:      $SRC_REPO"
log "  Destination: $DST_REPO"
log "  Tag:         $TAG"
[[ $DRY_RUN -eq 1 ]] && log "  Mode:        DRY RUN (no changes will be made)"

# ============================================================================
# Pre-flight Checks
# ============================================================================

log "Step 1/7: Pre-flight checks..."

# Check git
if ! command -v git &>/dev/null; then
  error "git is not installed. Please install git first."
fi
log_verbose "✓ git found: $(git --version | head -1)"

# Check gh CLI
if ! command -v gh &>/dev/null; then
  error "GitHub CLI (gh) is not installed. Install from: https://cli.github.com"
fi
log_verbose "✓ gh found: $(gh --version | head -1)"

# Check gh auth
if ! gh auth status &>/dev/null; then
  error "Not authenticated with GitHub. Run: gh auth login"
fi
log_verbose "✓ gh authenticated"

log "✓ Pre-flight checks passed"

# ============================================================================
# Verify Source Tag & Release
# ============================================================================

log "Step 2/7: Verifying source tag and release..."

# Check if tag exists in source
if ! gh release view "$TAG" -R "$SRC_REPO" &>/dev/null; then
  error "Tag/release '$TAG' not found in $SRC_REPO"
fi

# Get release metadata
RELEASE_TITLE=$(gh release view "$TAG" -R "$SRC_REPO" --json name -q .name)
RELEASE_IS_DRAFT=$(gh release view "$TAG" -R "$SRC_REPO" --json isDraft -q .isDraft)
RELEASE_IS_PRERELEASE=$(gh release view "$TAG" -R "$SRC_REPO" --json isPrerelease -q .isPrerelease)

log "✓ Found release in $SRC_REPO:"
log "  Title: $RELEASE_TITLE"
log "  Draft: $RELEASE_IS_DRAFT"
log "  Prerelease: $RELEASE_IS_PRERELEASE"

# ============================================================================
# Check Destination
# ============================================================================

log "Step 3/7: Checking destination repository..."

# Check if tag already exists in destination
if git ls-remote --tags "https://github.com/$DST_REPO.git" | grep -q "refs/tags/$TAG\$"; then
  if [[ $DRY_RUN -eq 1 ]]; then
    log "! Tag '$TAG' already exists in $DST_REPO (continuing in dry-run mode)"
  else
    error "Tag '$TAG' already exists in $DST_REPO. Aborting to prevent overwrite."
  fi
fi

# Check if release already exists
if gh release view "$TAG" -R "$DST_REPO" &>/dev/null; then
  if [[ $DRY_RUN -eq 1 ]]; then
    log "! Release '$TAG' already exists in $DST_REPO (continuing in dry-run mode)"
  else
    error "Release '$TAG' already exists in $DST_REPO. Delete it first or use a different tag."
  fi
fi

log "✓ Destination is clear for tag '$TAG'"

# ============================================================================
# Prepare Temp Directory
# ============================================================================

log "Step 4/7: Preparing temporary workspace..."

# Create temp directory for operations
TEMP_DIR=$(mktemp -d)
log_verbose "Created temp directory: $TEMP_DIR"

log "✓ Workspace ready"

# Note: Git tag will be created automatically by gh release create
# if it doesn't exist. If you need to preserve commit history,
# the destination repo must first have the commit that the tag references.

# ============================================================================
# Download Release Assets
# ============================================================================

log "Step 5/7: Downloading release assets from source..."

ASSETS_DIR="$TEMP_DIR/assets"
mkdir -p "$ASSETS_DIR"
cd "$ASSETS_DIR"

# Download all assets
ASSET_COUNT=$(gh release view "$TAG" -R "$SRC_REPO" --json assets -q '.assets | length')
log_verbose "Release has $ASSET_COUNT asset(s)"

if [[ $ASSET_COUNT -gt 0 ]]; then
  gh release download "$TAG" -R "$SRC_REPO" -D "$ASSETS_DIR" 2>/dev/null || true
  DOWNLOADED=$(find "$ASSETS_DIR" -type f | wc -l | tr -d ' ')
  log "✓ Downloaded $DOWNLOADED asset(s)"
else
  log "✓ No assets to download"
fi

cd - >/dev/null

# ============================================================================
# Get Release Notes
# ============================================================================

log "Step 6/7: Fetching release notes..."

NOTES_FILE="$TEMP_DIR/release_notes.md"
gh release view "$TAG" -R "$SRC_REPO" --json body -q .body > "$NOTES_FILE"

NOTES_SIZE=$(wc -c < "$NOTES_FILE" | tr -d ' ')
log_verbose "Release notes: $NOTES_SIZE bytes"
log "✓ Release notes saved"

# ============================================================================
# Create Destination Release
# ============================================================================

log "Step 7/7: Creating release in destination..."

# Build gh release create command
RELEASE_CMD=(gh release create "$TAG" -R "$DST_REPO")
RELEASE_CMD+=(--title "$RELEASE_TITLE")
RELEASE_CMD+=(--notes-file "$NOTES_FILE")

[[ $DRAFT -eq 1 ]] && RELEASE_CMD+=(--draft)
[[ $PRERELEASE -eq 1 ]] && RELEASE_CMD+=(--prerelease)

# Add assets if any
if [[ $ASSET_COUNT -gt 0 ]]; then
  while IFS= read -r -d '' asset; do
    RELEASE_CMD+=("$asset")
  done < <(find "$ASSETS_DIR" -type f -print0)
fi

# Execute or show
if [[ $DRY_RUN -eq 0 ]]; then
  "${RELEASE_CMD[@]}"
  log "✓ Release created in $DST_REPO"
else
  log "[DRY RUN] Would execute:"
  log_verbose "  ${RELEASE_CMD[*]}"
  log "✓ [DRY RUN] Release would be created in $DST_REPO"
fi

# ============================================================================
# Success
# ============================================================================

echo ""
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║                       ✅ Transfer Complete                           ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""
echo "Done: $SRC_REPO@$TAG → $DST_REPO@$TAG"
echo ""

if [[ $DRY_RUN -eq 0 ]]; then
  echo "Verification:"
  echo "  gh release view $TAG -R $DST_REPO"
  echo "  git ls-remote --tags https://github.com/$DST_REPO.git | grep $TAG"
  echo ""
  echo "View release:"
  echo "  https://github.com/$DST_REPO/releases/tag/$TAG"
else
  echo "This was a DRY RUN - no changes were made."
  echo "Run without --dry-run to actually transfer the release."
fi

echo ""

