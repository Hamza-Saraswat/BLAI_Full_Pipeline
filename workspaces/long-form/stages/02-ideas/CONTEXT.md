# Stage 02: Ideas

Turn the digest into scored episode candidates and pick the one to produce.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../01-radar/output/[date]-radar.md` | Full file | The candidate pool |
| Skill | `../../../../skills/youtube-keyword-research/SKILL.md` | Full file | Autocomplete, competition, vidIQ, opportunity score |
| Skill rule | `../../../../skills/youtube-keyword-research/rules/vidiq-mcp.md` | Full file | Connector usage and budget |
| Brand vault | `../../../../brand-vault/content-pillars.md` | "Long-form Series" | Series fit and rotation |
| Brand vault | `../../../../brand-vault/value-framework.md` | Full file | Value tags |
| Reference | `references/selection-rules.md` | Full file | Cadence, rotation, how the pick is chosen |
| Reference | `references/ideas-format.md` | Full file | Layout of the ideas note |
| Ledger | `output/series-ledger.json` | Last 6 entries | Series rotation |
| Skill | `../../../../skills/telegram-gate/SKILL.md` | "fyi-ideas" card | The morning FYI |

## Process

1. Draft 5-8 episode candidates: title naming a product or a project, the road the episode walks in one sentence, series, what we would measure, two value tags, the radar items it draws on.
2. Keyword research per candidate (evergreen phrasing: "how to", "vs", "explained"): `autocomplete.py`, `competition.py` (skip without `YT_API_KEY`), the vidIQ keyword tool (skip without the connector); save `output/[date]-candidates.json`.
3. Run `opportunity_score.py --candidates output/[date]-candidates.json --out output/[date]-scored.json`.
4. Choose the pick per selection-rules.md. **[Checkpoint]** -- present the ranked top 5 with the pick (unattended: decide, record under Decisions).
5. Create the hub note: `python3 ../../../../tools/new-run.py --workspace long-form --title "..." --series [series] --value-types "A,B" --date [date]`.
6. Write `output/[date]-ideas.md` per ideas-format.md; append `{slug, series, date}` to `output/series-ledger.json`. Run the audit checks below; if any fail, revise before saving.
7. Send the FYI: `send_card.py --kind fyi-ideas --ideas output/[date]-ideas.md --hub ../../videos/[slug].md` (skip with a note without `TELEGRAM_BOT_TOKEN`).
8. Unattended: `../../../../tools/git-sync.sh "long-form: [date] ideas"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 4 | Ranked top 5 with the pick | Keep, swap, or redirect |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Carries an episode | the pick names at least three visible steps, three comparison axes, or an example with two edge cases |
| Rotation | the pick's series differs from the previous ledger entry |
| Scores | every candidate has an autocomplete depth and an opportunity score; nulls carry a reason |
| Value tags | exactly two; PROVES only when something will be measured or cited |
| Hub note | `python3 ../../../../tools/check_outputs.py` exits 0 |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Ideas note | `output/[date]-ideas.md` | ranked table, pick, keyword notes, decisions |
| Candidates and scores | `output/[date]-candidates.json`, `output/[date]-scored.json` | JSON |
| Hub note | `../../videos/[slug].md` | hub note with status `idea` |
| Ledger | `output/series-ledger.json` | JSON list |

The ideas note and the hub note are the human edit surface. Swap the pick by tapping the card or by writing `output/[date]-picks.md` (`swap 1 -> 3`). The research stage reads whatever is there.
