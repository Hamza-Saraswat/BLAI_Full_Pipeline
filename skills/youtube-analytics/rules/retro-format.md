# Retro Note Format

`weekly_retro.py --week YYYY-WW --out analytics/` writes `analytics/<year>-w<ww>.md` (lowercase so the name passes the repo's naming rule). The retro routine reads it, applies the convincing playbook edits on a branch and opens a pull request. Keep the sections in this order and with these headings; the routine and future tooling look for them by name.

## Header

`# Retro YYYY-WW`, then one line naming the week (Monday to Sunday, America/Chicago) and the two snapshots the numbers come from. Definitions used everywhere below:

- Delta: views gained between the previous snapshot and the current one (`n/a` when the video is younger than the previous snapshot).
- Views/day: views at the current snapshot divided by the video's age in days, floored at 1 day. It is the ranking key for the week; it is noisy for videos under two days old, so the note says how old each video is through its slot.
- The week's videos: published between Monday 00:00 and Sunday 23:59 CT (the YouTube `publishedAt`, else the hub note's `published_slot`).

## What shipped

A table, one row per video published in the week, oldest first: slug, workspace, pillar (or long-form series), structure, style pack, slot (weekday and CT time), views, views/day, delta. Below it: how many shipped, how many have stats, and up to three catalog movers (older videos with the largest delta this week).

## What worked

The top three of the week by views/day, numbered, each with its pillar, structure and style pack, the views/day value, the multiple of the week's median, and the title. Three is the cap: the point is to name what to repeat, not to list everything.

## What did not

- Videos below half the week's median views/day (only when at least four videos have stats; with fewer, say so).
- Videos that did not ship: hub notes created in the week with `status: blocked` or `rejected`, with the `blocked_reason` or the `feedback`. Production failures count as outcomes.

## Hypotheses for next week

One bullet per hypothesis. Each carries its numbers and ends with "Next week:" and one action. The script only states a pattern when a group (pillar, structure, style pack, slot) has at least two videos and differs from the week's average by 1.5x (1.3x for the two Shorts slots, and for the seo_score split). With fewer than two videos it says so instead of guessing. The routine may add hypotheses of its own below the generated ones, marked `(routine)`.

## Proposed playbook edits

A checklist the routine turns into a pull request. One item per edit, in this form:

`- [ ] <file>: <the edit in one sentence> (evidence: <the numbers>)`

Targets are `shared/playbook/publish-timing.md` (slots), `shared/playbook/seo-rubric.md` (minimum score) and `brand-vault/content-pillars.md` (rotation notes, default structures). When nothing qualifies the single item says `no playbook edit this week` with the reason, so the routine knows there is nothing to open. The routine ticks the items it applied on the branch and leaves one line under each item it did not apply.

## Data

Where the numbers came from and the command that regenerates the note. Public Data API numbers only; retention, impressions CTR and search terms are not in the snapshots (`analytics-api.md`).

## Blocked

Not written by the script. When the routine cannot produce the retro (no `YT_API_KEY`, API error, a single snapshot), it appends `## Blocked` with the step and the exact error to an otherwise empty note, so the failure is visible in Obsidian and in git.

## Style

No em dashes; write `--` or a comma. Slugs in backticks. Numbers with thousands separators. Never paste a key or a token. Under 120 lines for a normal week.
