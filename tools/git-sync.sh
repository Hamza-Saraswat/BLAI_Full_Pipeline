#!/usr/bin/env bash
# Commit and push to main, rebasing and retrying so that two cloud routines and the
# Spark build agent can all push the same morning without manual conflict work.
#   tools/git-sync.sh "shorts: 2026-08-25 ideas" [path ...]
#
# Pass the paths the caller actually changed. With paths, only those are staged.
# Without paths it falls back to `git add -A` for a clean automation checkout
# (cloud routines, the Spark) -- but the repo root on the Mac is a LIVE OBSIDIAN
# VAULT the user hand-edits, and an unscoped add there commits half-written notes
# under the pipeline's name (finding 41, 2026-08-23 dry run). Every in-repo caller
# passes paths; keep it that way.
set -euo pipefail
MSG="${1:-pipeline update}"
shift || true
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
BRANCH="$(git rev-parse --abbrev-ref HEAD)"
if [ "$#" -gt 0 ]; then
  git add -- "$@"
else
  git add -A
fi
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
