# Stage 02: Ideas

Turn the radar digest into scored candidates and pick today's two Shorts.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../01-radar/output/[date]-radar.md` | Full file | The candidate pool |
| Skill | `../../../../skills/youtube-keyword-research/SKILL.md` | Full file | Autocomplete, competition scan, vidIQ, opportunity score |
| Skill rule | `../../../../skills/youtube-keyword-research/rules/vidiq-mcp.md` | Full file | Using the vidIQ connector within its credit budget |
| Brand vault | `../../../../brand-vault/content-pillars.md` | "Shorts Lanes" | Lane tagging and rotation |
| Brand vault | `../../../../brand-vault/value-framework.md` | Full file | Value tags per candidate |
| Reference | `references/selection-rules.md` | Full file | How two picks are chosen |
| Reference | `references/ideas-format.md` | Full file | Layout of the ideas note |
| Archive | `../../videos/` | Frontmatter of the previous day's hub notes | Lane and format rotation |
| Skill | `../../../../skills/telegram-gate/SKILL.md` | "fyi-ideas" card | The morning FYI |

## Process

1. Read the digest. Draft 8-12 candidates: a title that names a product, an angle in one sentence a viewer could repeat, lane, why-now, the radar items it draws on, two value tags.
2. For each candidate choose one search keyword; run `autocomplete.py`, `competition.py` (skip without `YT_API_KEY`) and the vidIQ keyword tool (skip without the connector); save `output/[date]-candidates.json`.
3. Run `opportunity_score.py --candidates output/[date]-candidates.json --out output/[date]-scored.json`.
4. Choose two picks per selection-rules.md. **[Checkpoint]** -- present the ranked top 5 with the two picks (unattended: decide and record under Decisions).
5. Create one hub note per pick: `python3 ../../../../tools/new-run.py --workspace shorts --title "..." --pillar [lane] --format [band] --value-types "A,B" --date [date]`.
6. Write `output/[date]-ideas.md` per ideas-format.md. Run the audit checks below. If any fail, revise before saving.
7. Send the FYI: `python3 ../../../../skills/telegram-gate/scripts/send_card.py --kind fyi-ideas --ideas output/[date]-ideas.md --hub ../../videos/[first-pick-slug].md` (skip with a note when `TELEGRAM_BOT_TOKEN` is absent).
8. Unattended: `../../../../tools/git-sync.sh "shorts: [date] ideas" workspaces/shorts skills/render-shorts/styles/history.json`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 4 | Ranked top 5 with the two picks and their scores | Keep, swap, or redirect |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Named products | both picks name a product, model or tool in the title |
| Rotation | the two picks differ in lane from each other and from yesterday's picks; at most one `news-react` |
| Scores | every candidate has an autocomplete depth and an opportunity score; null vidIQ or competition values carry a reason |
| Value tags | each pick has exactly two value types |
| Hub notes | `python3 ../../../../tools/check_outputs.py` exits 0 |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Ideas note | `output/[date]-ideas.md` | ranked table, picks, keyword tables, decisions |
| Candidates and scores | `output/[date]-candidates.json`, `output/[date]-scored.json` | JSON |
| Hub notes | `../../videos/[slug].md` (two) | hub note with status `idea` |

The ideas note and the hub notes are the human edit surface. Swap a pick by tapping the Telegram card, or write `output/[date]-picks.md` with one line such as `swap 2 -> 4`. The research stage reads whatever is there.
