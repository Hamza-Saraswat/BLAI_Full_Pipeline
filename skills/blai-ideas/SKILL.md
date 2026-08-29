---
name: blai-ideas
description: Run the Shorts thinking-half opener for a date: radar sweep then scored ideas and two picks (stages 01-02). Use when asked to find or pick today's Shorts topics.
metadata: {tags: "blai, trigger, shorts, radar, ideas"}
---

# blai-ideas

A routing shim. The contract is the workspace's, not this file's.

1. `cd workspaces/shorts` and read `CLAUDE.md`; run its trigger `ideas [--date YYYY-MM-DD] [--unattended]` exactly as described there (stages `01-radar` then `02-ideas`, each per its own `stages/NN-*/CONTEXT.md`).
2. Radar entry point: `python3 skills/trend-radar/scripts/radar.py --workspace shorts --date <date> --hours 48 --out workspaces/shorts/stages/01-radar/output --dedupe-dir workspaces/shorts` (repo root). FireCrawl source activates when `FIRECRAWL_API_KEY` is set.
3. Long steps run in the background (`background=true`), never as foreground turns.
4. Unattended: decisions land in the ideas note's `## Decisions`; commit with the scoped git-sync line the stage names.
