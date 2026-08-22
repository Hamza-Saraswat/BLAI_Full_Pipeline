---
name: youtube-analytics
description: Weekly channel numbers from the YouTube Data API and the retro note that turns them into playbook edits.
metadata:
  tags: "analytics, youtube, retro, stats, playbook"
---

# YouTube Analytics

Pulls public stats for every video on the channel into a dated snapshot and writes the weekly retro that ranks the week's videos, names what worked, and proposes playbook edits as a checklist.

## When to Use

- Sunday retro (the `blai-weekly-retro` routine): snapshot, then retro note, then a pull request with the playbook edits.
- Any time a stage wants last week's numbers (the ideas stages may read the latest `analytics/<year>-w<ww>.md` for "what worked" only; never the raw snapshots).
- After OAuth is added (see `rules/analytics-api.md`): retention and search terms join the same note.

## What You Need Before Calling

- `YT_API_KEY` in the environment (cloud) or in `build/.env` (Spark). No OAuth for the stats pull.
- At least one `published/<slug>.md` note per workspace with a `youtube_url` (the publish stage writes it, the build loop fills the URL), so video ids map to slugs, pillars, structures and style packs through `videos/<slug>.md`.
- For deltas: a previous snapshot in `analytics/stats/` at least six days old. Snapshots are committed on purpose.
- Python 3.9+ with the standard library only. `python-dotenv` is optional.

## How It Works

1. `python3 skills/youtube-analytics/scripts/yt_stats.py [--handle @BuildLocalAI | --channel-id UC... | --ids a,b,c] [--max 500] [--out analytics/stats] [--dry-run]` resolves the channel (`channels.list`), walks its uploads playlist (`playlistItems.list`), fetches statistics, duration and publish time (`videos.list`, 50 per call), maps ids to slugs through the `youtube_url` fields, and writes `analytics/stats/<date>.json` (`{fetched_at, channel{}, rows[{videoId, slug, workspace, format, title, publishedAt, durationS, views, likes, comments}]}`). About 1 + 2 * ceil(videos / 50) quota units. `--dry-run` prints a fixture snapshot and writes nothing.
2. `python3 skills/youtube-analytics/scripts/weekly_retro.py --week 2026-W34 --out analytics/ [--stats analytics/stats] [--stdout] [--dry-run]` takes the latest snapshot and the latest one at least six days older, reads `published/*.md` plus the hub notes of both workspaces, computes delta and views/day per video, ranks the videos published in the ISO week (Monday to Sunday, America/Chicago), lists blocked and rejected notes of the week, derives hypotheses and a playbook-edit checklist from groups with at least two videos, and writes `analytics/<year>-w<ww>.md` in the layout of `rules/retro-format.md`. `--dry-run` renders a fixture week to stdout.
3. The retro routine (`build/routines/weekly-retro.md`) commits the snapshot and the note to `main`, applies the convincing checklist items on a branch `retro/<week>`, and opens the pull request.
4. Both scripts exit 0 on success and 1 on failure (no key, API error, no snapshot, no published notes) and log to stderr; the data goes to the file named in the last line of stdout.

## Rules

- `rules/retro-format.md`: the sections of the weekly note, how ranking and thresholds work, the checklist item format, the `## Blocked` convention.
- `rules/analytics-api.md`: what the API key gives, what needs the Analytics API with OAuth (retention, search terms), what is Studio only (impressions CTR, swipe-away), and the steps to add OAuth later.

## After the Call

- Read the note in Obsidian (`analytics/`); tick or untick the proposed edits before the PR merges.
- Impressions CTR and retention are not in the note until OAuth exists; read them in Studio for the top and bottom video and add a line by hand when they change the conclusion.
- If the same hypothesis appears three weeks in a row, the fix belongs in the reference file that produced it (the script structures, the pillar table, the timing playbook), not in another retro.
