#!/usr/bin/env bash
# Re-clone all repos from the library registry
# Reads lode/registry.md and clones each repo into repos/
# Skips repos that already exist in repos/

set -euo pipefail

LIBRARY_DIR="$(cd "$(dirname "$0")" && pwd)"
REGISTRY="$LIBRARY_DIR/lode/registry.md"
REPOS_DIR="$LIBRARY_DIR/repos"

mkdir -p "$REPOS_DIR"

if [ ! -f "$REGISTRY" ]; then
  echo "Registry not found at $REGISTRY"
  exit 1
fi

while IFS='|' read -r name url notes; do
  # Skip header, separator lines, empty lines, and lines without a URL
  name=$(echo "$name" | xargs)
  url=$(echo "$url" | xargs)
  [ -z "$name" ] && continue
  [ -z "$url" ] && continue
  [[ "$name" == Repo* ]] && continue
  [[ "$name" == "<!"* ]] && continue

  target="$REPOS_DIR/$name"
  if [ -d "$target" ]; then
    echo "SKIP  $name (already exists)"
  else
    echo "CLONE $name from $url"
    git clone "$url" "$target"
  fi
done < "$REGISTRY"

echo ""
echo "Done. Remember to update version markers in lode/version-markers.md"