#!/usr/bin/env bash
# OzODent – push na GitHub (onluxall) + deploy na Vercel
set -euo pipefail
cd "$(dirname "$0")"
OWNER="onluxall"; REPO="ozodent"
V="npx -y vercel@latest"

command -v gh >/dev/null || { echo "Instaluję GitHub CLI..."; brew install gh; }
gh auth status >/dev/null 2>&1 || gh auth login -h github.com -w -p https

git add -A && git commit -qm "Update deploy target to onluxall" || true

if git remote get-url origin >/dev/null 2>&1; then
  git push -u origin main
else
  gh repo create "$OWNER/$REPO" --public --source . --remote origin --push \
    --description "Strona OzODent Centrum Stomatologii, Ozorków"
fi
echo "✅ GitHub: https://github.com/$OWNER/$REPO"

$V whoami >/dev/null 2>&1 || $V login
$V link --yes --project "$REPO"
$V git connect "https://github.com/$OWNER/$REPO" --yes \
  || echo "ℹ️  Auto-deploy z GitHuba: Vercel → projekt ozodent → Settings → Git → Connect"
URL=$($V deploy --prod --yes | tail -1)
echo "✅ Vercel: $URL"
open "$URL" 2>/dev/null || true
