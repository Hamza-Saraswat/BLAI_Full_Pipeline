# BLAI Analytics

Weekly retro: what shipped, what worked, and which playbook lines to change. Run by the `blai-weekly-retro` routine on Sundays or by typing `retro` here.

## Triggers

| Keyword | Action |
|---------|--------|
| `retro [--week YYYY-WW] [--unattended]` | Pull stats, write the week's retro note, propose playbook edits |

## Process for `retro`

1. `python3 ../skills/youtube-analytics/scripts/yt_stats.py --out stats/` (needs `YT_API_KEY`; skip with a note if absent).
2. `python3 ../skills/youtube-analytics/scripts/weekly_retro.py --week [week] --out .` writes `[week].md`.
3. Read the retro note's "Proposed playbook edits". For each edit that a number supports (views per day, retention where available), change the one sentence it names in `../shared/playbook/*.md`, `../brand-vault/content-pillars.md`, or a stage reference file, and cite the retro note in the commit message.
4. Unattended: create a branch `claude/retro-[week]`, commit, push, and open a pull request titled "retro [week]: playbook edits" so the edits are reviewed before they reach `main`. Interactive: show the diff and ask.
5. Add the week's view counts to the `views_7d` field of each `workspaces/*/published/*.md` note touched.

## What to Load

| Task | Load These | Do NOT Load |
|------|-----------|-------------|
| `retro` | `../skills/youtube-analytics/SKILL.md`, the two newest `stats/*.json`, the newest `*.md` here, `../shared/playbook/publish-timing.md` | workspace stage contracts, research docs |

Retro notes follow `../skills/youtube-analytics/rules/retro-format.md`. They are committed; stats JSON snapshots are committed too (small) so the retro can diff weeks.
