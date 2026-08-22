# Stage 01: Radar

Sweep the local-AI world for the last 48 hours and write a scored, deduplicated digest.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Skill | `../../../../skills/trend-radar/SKILL.md` | Full file | How to run the sweep and what the digest contains |
| Skill rule | `../../../../skills/trend-radar/rules/scoring.md` | "Why-now rubric" | Judging why an item matters this week |
| Brand vault | `../../../../brand-vault/content-pillars.md` | "Shorts Lanes" | Grouping the digest by lane |
| User notes | `../../input/` | Every `.md` except README | Items the creator wants considered |
| Archive | `../../published/` | Frontmatter titles | Dedupe |
| Previous runs | `output/` | The last 7 radar JSON files | Dedupe |
| Reference | `references/so-what-rules.md` | Full file | Writing the so-what line |

## Process

1. Confirm the run date (`--date`, default today UTC). Note which of `YT_API_KEY`, `FIRECRAWL_API_KEY`, `REDDIT_CLIENT_ID` are absent; those sources are skipped, never faked.
2. Run `python3 ../../../../skills/trend-radar/scripts/radar.py --workspace shorts --date [date] --hours 48 --out output --dedupe-dir ../..`.
3. Add every note in `../../input/` as an item at the top of the digest (`source: input`, the note's URL if it has one, score 1.0).
4. For the top 15 items write a one-line so-what per `references/so-what-rules.md`; flag any item that contradicts a claim in a published Short's title.
5. Run the audit checks below. If any fail, revise before saving.
6. Save `output/[date]-radar.md` (the script's digest plus your lines).
7. Unattended: `../../../../tools/git-sync.sh "shorts: [date] radar"`.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Volume | at least 15 items after dedupe, or the digest names the sources that failed |
| Sourced | every item has a URL fetched this run (input notes may cite none) |
| Fresh | no item matches a title in `../../published/` or a hub note |
| Lanes | every top-15 item carries a lane from content-pillars.md |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Radar digest | `output/[date]-radar.md` | markdown grouped by lane: score, title, source, url, products, why-now, so-what |
| Radar data | `output/[date]-radar.json` | JSON list of items |

The digest in `output/` is the human edit surface. Delete an item, add one you saw elsewhere with its URL, change a so-what. The ideas stage reads whatever is there.
