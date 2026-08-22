---
name: youtube-keyword-research
description: Measure demand and competition for candidate YouTube keywords with free autocomplete fan-out, the Data API competition snapshot and the vidIQ MCP, then rank candidates with the opportunity score so the ideas stage picks searchable, winnable titles.
metadata:
  tags: "youtube, keyword-research, autocomplete, youtube-data-api, vidiq, opportunity-score, seo, shorts, long-form"
---

# YouTube Keyword Research

## When to Use

- Stage 02 (ideas) of either workspace, after the trend radar, to turn radar items into keyword candidates and pick the ones worth a video.
- The package stage, when a title needs a primary keyword with evidence rather than a guess.
- Not for checking a finished title against the rubric (that is `shared/playbook/seo-rubric.md`) and not for news discovery (that is `skills/trend-radar`).

## What You Need Before Calling

- A list of seed keywords (product names first: "dgx spark", "deepseek v4 flash ollama").
- `YT_API_KEY` for `competition.py` (100 quota units per query; the daily 10,000 are shared with the radar's YouTube source, so budget about 10 queries per run). `autocomplete.py` needs no key.
- The vidIQ MCP connector attached to the routine when you want search volume (`rules/vidiq-mcp.md`); without it the score still works.
- Python 3.9 or newer, standard library only. Offline: every script has `--dry-run` with fixtures under `fixtures/` and the clock pinned to 2026-08-25T12:00Z.

## How It Works

1. Expand each seed: `python3 skills/youtube-keyword-research/scripts/autocomplete.py "dgx spark" [--hl en --gl US]` prints `{seed, suggestions, expansions, depth_score}`; `depth_score` (unique suggestions across 32 expansions) is the free demand proxy, and the suggestions themselves are the long-tail candidates.
2. Snapshot the competition for each shortlisted keyword: `python3 .../competition.py "dgx spark" [--max 20]` prints the top videos with `median_views`, `median_subs`, `share_recent_180d`, `exact_title_rate` and `small_channel_velocity` (mean views per day on channels under 10,000 subscribers).
3. Ask vidIQ (when attached) for volume and competition per shortlisted keyword, about 10 calls per run, and record the answer in the candidate's `vidiq` object (`rules/vidiq-mcp.md`).
4. Build `candidates.json`: one object per keyword with `title, keyword, autocomplete, competition, vidiq|null, trend_slope|null, named_product`.
5. Rank: `python3 .../opportunity_score.py --candidates candidates.json --out ranked.json` adds `demand`, `competition_score`, `opportunity` (0-100) and `rank` per `rules/opportunity-score.md`.
6. Carry the top candidates, their opportunity and the evidence (depth, median views, small-channel velocity, vidIQ volume or "not available") into the ideas note and the hub note.

## Rules

- `rules/opportunity-score.md`: the formula (z-blended demand minus z-blended competition, centred on 50, spread 15, +10 for a named product, +5 for above-median small-channel velocity) written out with a worked example from the fixture.
- `rules/vidiq-mcp.md`: how to find the vidIQ tools at run time, what to record, the 10-call budget, and what to do when the connector is absent.

## After the Call

- Prefer a lower-ranked keyword that names a product over a higher-ranked generic one when the gap is under 10 points; product names are what the channel's search traffic is made of (`shared/playbook/titles-descriptions.md`).
- Write the opportunity score and its inputs next to each idea; a score without its evidence cannot be audited at the weekly retro.
- Treat `exact_title_rate` above 0.7 with `median_subs` above 100,000 as a saturated keyword: take the long-tail suggestion instead of the head term.
- When `competition.py` reports `quotaExceeded`, stop calling it for the day and score the rest of the candidates without competition data (the z-blend ignores missing columns), saying so in the ideas note.
- Re-run `autocomplete.py` for the winning keyword before the package stage; suggestions shift week to week and the description should carry the current ones.
