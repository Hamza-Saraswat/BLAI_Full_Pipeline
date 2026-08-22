#!/usr/bin/env bash
# Commit everything and push to main, rebasing and retrying so that two cloud routines
# and the Spark build agent can all push the same morning without manual conflict work.
#   tools/git-sync.sh "shorts: 2026-08-25 ideas"
set -euo pipefail
MSG="${1:-pipeline update}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
BRANCH="$(git rev-parse --abbrev-ref HEAD)"
git add -A
if git diff --cached --quiet; then
  echo "git-sync: nothing to commit"
else
  git commit -q -m "$MSG" -m "Automated by BLAI pipeline on $(hostname) at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
fi
for attempt in 1 2 3 4 5; do
  if git pull --rebase -q origin "$BRANCH" && git push -q origin "$BRANCH"; then
    echo "git-sync: pushed $BRANCH (attempt $attempt)"
    exit 0
  fi
  git rebase --abort 2>/dev/null || true
  sleep $((attempt * 7))
done
echo "git-sync: push failed after 5 attempts" >&2
exit 1
