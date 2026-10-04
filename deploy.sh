#!/usr/bin/env bash
# OzODent – push na GitHub (onluxall) + deploy na Vercel
set -euo pipefail
cd "$(dirname "$0")"
OWNER="onluxall"; REPO="ozodent"
V="npx -y vercel@latest"

command -v gh >/dev/null || { echo "Instaluję GitHub CLI..."; brew install gh; }
gh auth status >/dev/null 2>&1 || gh auth login -h github.com -w -p https

rm -f public/regulamin.html   # strona usunięta w wersji v4
python3 build.py >/dev/null 2>&1 || true
git add -A && git commit -qm "Aktualizacja strony OzODent" || true

URL_GH="https://github.com/$OWNER/$REPO.git"
if gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  echo "ℹ️  Repo $OWNER/$REPO już istnieje – podłączam i wysyłam."
  git remote get-url origin >/dev/null 2>&1 && git remote set-url origin "$URL_GH" || git remote add origin "$URL_GH"
  gh auth setup-git
  if ! git push -u origin main 2>/dev/null; then
    echo "ℹ️  Repo ma już inne commity – łączę historię (nasze pliki mają pierwszeństwo, nic nie jest kasowane)."
    git fetch origin
    BR=$(gh repo view "$OWNER/$REPO" --json defaultBranchRef -q .defaultBranchRef.name)
    BR=${BR:-main}
    git merge "origin/$BR" --allow-unrelated-histories -X ours --no-edit -m "Merge existing $OWNER/$REPO ($BR)"
    git push -u origin "main:$BR"
  fi
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
