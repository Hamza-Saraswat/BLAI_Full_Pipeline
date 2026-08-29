---
name: trend-radar
description: Collect the last 48 hours of local-AI signals from Reddit, Hacker News, Hugging Face, GitHub releases, YouTube and FireCrawl, score and dedupe them, and write the daily radar JSON and digest that the ideas stage reads.
metadata:
  tags: "trend-radar, local-ai, reddit, hacker-news, hugging-face, github-releases, youtube-data-api, firecrawl, shorts"
---

# Trend Radar

## When to Use

- Stage 01 of the shorts workspace, at the start of every ideas routine (daily).
- Any time you need "what shipped, changed, measured or broke in local AI in the last two days" as ranked, deduped data rather than a browsing session.
- Not for research on one topic (that is `skills/blai-research`) and not for keyword demand (that is `skills/youtube-keyword-research`).

## What You Need Before Calling

- The workspace (`shorts`) and today's date.
- Environment: nothing is required. `YT_API_KEY` adds the YouTube source, `FIRECRAWL_API_KEY` adds web news, `REDDIT_CLIENT_ID` + `REDDIT_CLIENT_SECRET` switch Reddit to OAuth (needed in practice: the public endpoint answered 403 during the build), `GITHUB_TOKEN` lifts the GitHub rate limit. Missing keys skip their source with a stderr note. See `shared/env-template.md`.
- Network access to the domains in `shared/cloud-environment.md`. Offline, use `--dry-run` (fixtures, pinned clock 2026-08-25T12:00Z).
- Python 3.9 or newer, standard library only.

## How It Works

1. Run the orchestrator from anywhere in the repo:
   `python3 skills/trend-radar/scripts/radar.py --workspace shorts --date 2026-08-25 [--hours 48] [--out DIR] [--dedupe-dir DIR] [--dry-run]`
2. It calls the six source modules in turn (`reddit.py`, `hn.py`, `hf_trending.py`, `github_releases.py`, `youtube_recent.py`, `firecrawl_search.py`; each also runs standalone with `--hours N --limit N [--dry-run]` and prints its JSON list). Query and repo lists live in `rules/sources.md`.
3. Each raw item is normalized: engagement to a 0-1 signal, recency decay with a 48 h half-life, product names extracted, a why-now kind assigned, score 0-100 (`rules/scoring.md`).
4. Duplicates across sources merge (same URL or title); items already in hub notes, `published/`, or the previous seven radars are dropped (`rules/dedupe.md`).
5. Items get a Shorts lane from `brand-vault/content-pillars.md` (stored in `signals.group`) and are sorted by score.
6. It writes `DIR/<date>-radar.json` (items: `id, title, url, source, published_at, signals, products, summary, why_now, score`) and `DIR/<date>-radar.md` (Top 10, then one bullet per item grouped by lane, at least the top 30, at most 60). Default `DIR` is `workspaces/<ws>/stages/01-radar/output`.
7. stdout gets a one-line JSON summary (paths, kept, merged, dropped, per-source status). Exit 1 only when no source produced an item or a file could not be written.

## Rules

- `rules/sources.md`: what each source answers, the subreddit, query and repo lists the scripts read at run time, rate limits, what happens when a source fails, and what the fixtures contain.
- `rules/scoring.md`: signal normalization per source, the decay curve, the product and vendor regex list with the +15 bonus, the why-now rubric, and the lane assignment rules.
- `rules/dedupe.md`: the three dedupe passes (cross-source merge, hub-note titles, previous seven radars), URL and title normalization, what the run reports, known limits.

## After the Call

- Read the digest, not the JSON, when picking ideas; use the JSON when you need `why_now`, `products` or `signals` for a brief.
- Check the Sources line first: a skipped YouTube or FireCrawl source means the radar is thinner than usual, and the ideas note must say so.
- Never edit the radar files by hand; re-run with different flags instead. Same-day re-runs overwrite and do not dedupe against themselves.
- Link the digest from the hub note's Artifacts section as `[[stages/01-radar/output/<date>-radar]]`.
- When the same drop or mis-scored item repeats three runs in a row, fix `rules/scoring.md` and `scripts/scoring.py` together, or the list in `rules/sources.md`, rather than the output (ICM 8.6).
