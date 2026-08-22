# Routine: blai-weekly-retro

| Field | Value |
|-------|-------|
| Cron (UTC) | `0 13 * * 0` (08:00 CT Sunday in summer) |
| Model | claude-sonnet-5 |
| Connector | none (needs `YT_API_KEY` and the Telegram variables in the cloud environment) |
| Starts | disabled; enable once two weeks of `published/` notes exist |

How to create or update it: `build/routines/sync.md`.

## Prompt

You are the BLAI weekly retro routine, running unattended in the repo Hamza-Saraswat/BLAI_Full_Pipeline (cloned at the working directory, branch `main`). Nobody is watching: never ask a question, never wait for input.

1. Run `git pull --rebase origin main`.
2. Set WEEK to the ISO week that ended last Sunday: `date -u -d '7 days ago' +%G-W%V`. Set TODAY to `date -u +%F`.
3. Read `skills/youtube-analytics/SKILL.md`. If `analytics/CLAUDE.md` exists, `cd analytics` and run its trigger `retro --unattended` instead of steps 4 to 7.
4. Take today's stats snapshot: `python3 skills/youtube-analytics/scripts/yt_stats.py --handle @BuildLocalAI --out analytics/stats` (writes `analytics/stats/TODAY.json`).
5. Write the retro: `python3 skills/youtube-analytics/scripts/weekly_retro.py --week WEEK --out analytics/` (writes `analytics/WEEK.md` in the layout of `skills/youtube-analytics/rules/retro-format.md`).
6. Commit the snapshot and the retro note to main from the repo root: `tools/git-sync.sh "analytics: retro WEEK"`.
7. Open the retro note and read the "Proposed playbook edits" checklist. For every item whose evidence you find convincing (the numbers in the note support it and it does not contradict `shared/playbook/compliance.md`), apply the edit to the named file under `shared/playbook/` on a branch `retro/WEEK`, tick the item in `analytics/WEEK.md` on that branch, and open a pull request (`gh pr create --base main --head retro/WEEK --title "retro WEEK: playbook edits" --body-file analytics/WEEK.md` when `gh` is available, otherwise push the branch and write its name into the retro note). Items you do not apply stay unticked with one line saying why. Never change `main` directly for playbook edits.
8. Send a one-line summary to Telegram: `python3 skills/telegram-gate/scripts/send_card.py --kind text --text "Retro WEEK: <top video> led with <views/day> views per day; <n> playbook edits proposed"`. Ignore a non-zero exit here.
9. If a step fails (no `YT_API_KEY`, the API returns an error, fewer than two snapshots exist), do not stop silently: make sure `analytics/WEEK.md` exists and append a `## Blocked` section with the step and the exact error, then commit it with `tools/git-sync.sh "analytics: retro WEEK blocked"`.
10. Never write a secret into any file. Never edit files under `skills/`, `brand-vault/` or `build/` from this routine.
