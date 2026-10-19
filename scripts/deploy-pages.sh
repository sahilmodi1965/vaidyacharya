#!/bin/sh
# Build the GitHub Pages preview and publish it to the gh-pages branch.
# Live at https://<owner>.github.io/vaidyacharya/, where <owner> owns origin.
# Usage: sh scripts/deploy-pages.sh
set -eu

cd "$(dirname "$0")/.."
remote=$(git remote get-url origin)
owner=$(echo "$remote" | sed -E 's#^.*github\.com[:/]([^/]+)/.*$#\1#')
SITE_URL=https://$owner.github.io BASE_PATH=/vaidyacharya npx astro build

# _astro/ starts with an underscore, so Jekyll must be switched off
touch dist/.nojekyll

rev=$(git rev-parse --short HEAD)
tmp=$(mktemp -d)
cp -R dist/. "$tmp"
cd "$tmp"
git init -q -b gh-pages
git add -A
git commit -q -m "Deploy preview from $rev"
git push -q --force "$remote" gh-pages
cd - >/dev/null
rm -rf "$tmp"
echo "Deployed $rev to gh-pages"
