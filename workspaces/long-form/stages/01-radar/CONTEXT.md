# Stage 01: Radar

Sweep the local-AI world and the creator's own input notes; write a scored digest shaped for episodes.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Skill | `../../../../skills/trend-radar/SKILL.md` | Full file | How to run the sweep |
| Skill rule | `../../../../skills/trend-radar/rules/scoring.md` | "Why-now rubric" | Judging items |
| User notes | `../../input/` | Every `.md` except README | The priority lane: the creator's own projects |
| Brand vault | `../../../../brand-vault/content-pillars.md` | "Long-form Series" | Grouping by series |
| Archive | `../../published/` | Frontmatter titles | Dedupe |
| Previous runs | `output/` | The last 7 radar JSON files | Dedupe |
| Reference | `references/episode-signals.md` | Full file | What makes an item episode-worthy rather than Short-worthy |

## Process

1. Confirm the run date; note absent keys (skipped sources are named, never faked).
2. Run `python3 ../../../../skills/trend-radar/scripts/radar.py --workspace long-form --date [date] --hours 168 --out output --dedupe-dir ../..`.
3. Add every note in `../../input/` as an item at the top (`source: input`, score 1.0, series guessed from content-pillars.md).
4. For the top 12 items write an episode-signal line per episode-signals.md: does this carry 10 minutes, and what would we measure.
5. Run the audit checks below. If any fail, revise before saving.
6. Save `output/[date]-radar.md`.
7. Unattended: `../../../../tools/git-sync.sh "long-form: [date] radar"`.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Volume | at least 12 items after dedupe, or the digest names the failed sources |
| Input lane | every note in `input/` appears as an item |
| Sourced | every non-input item has a URL fetched this run |
| Series | every top-12 item carries a series from content-pillars.md |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Radar digest | `output/[date]-radar.md` | markdown grouped by series with episode-signal lines |
| Radar data | `output/[date]-radar.json` | JSON list of items |

The digest in `output/` is the human edit surface. The ideas stage reads whatever is there.
