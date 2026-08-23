# Stage 04: Outline

Set the direction of the episode twice, under two different shapes, and judge which one gets built: the angle, the two value types, the hook, the payoff, the chapters, and what a muted viewer should understand.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../03-research/output/[slug]-brief.md` | Full file | Facts and the suggested outline |
| Previous stage | `../03-research/output/[slug]-experiment.md` | Full file when present | What will be measured |
| Hub note | `../../videos/[slug].md` | Frontmatter | Series, value types, feedback |
| Brand vault | `../../../../brand-vault/content-pillars.md` | The row for this series | Angle and episode shapes |
| Brand vault | `../../../../brand-vault/value-framework.md` | Full file | Locking two value types |
| Brand vault | `../../../../brand-vault/identity.md` | "Audience", "Content Mission" | Who it is for and what it must leave them able to do |
| Reference | `references/outline-format.md` | Full file | Layout, length, chapter rules |
| Reference | `references/judge-rubric.md` | Full file | The seven dimensions and the tiebreak |
| Reference | `references/episode-structures.md` | The shapes table and "Choosing" | The two shapes to write against |
| Ledger | `../02-ideas/output/episode-ledger.json` | Last 5 entries | Shape rotation and the difference score |

`../*-script/references/` is the script stage's reference folder: the shape library lives with the writer that uses it every run.

## Process

1. Read the brief and the hub note. Rank the shapes in `episode-structures.md` by fit and take the top two. Both must differ from the last two ledger entries; a missing or empty ledger is no constraint. **[Checkpoint]** -- present the two shapes with a one-sentence angle each.
2. Write outline A and outline B per outline-format.md, one under each shape. Each carries: the angle, two locked value types, the hook, the payoff, the surprising number spoken by 0:20, the chapter table, and the visual philosophy.
3. Score both against judge-rubric.md: seven dimensions, 0 to 3 each. The higher total wins; a tie goes to the more different outline. **[Checkpoint]** -- present both totals and the winner.
4. Run the audit checks below against the winner. If any fail, revise before saving.
5. Save the winner as `output/[slug]-outline.md`, and both outlines with every score and the reasoning as `output/[slug]-outlines.md`.
6. Write `structure` into this slug's entry in `../02-ideas/output/episode-ledger.json`, appending `{slug, series, structure, date}` when the ideas stage left no entry; update the hub (`value_types`, `structure`, Decisions).
7. Unattended: `../../../../tools/git-sync.sh "long-form: [slug] outline"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | The two shapes with an angle each | Which two shapes, or a different angle |
| 3 | Both outlines, the fourteen scores, the winner | Keep the winner or take the other one |

Unattended: the agent resolves both checkpoints itself and records the choice and the reason under `## Decisions` in the outline note and in the hub note, as the rest of the repo does.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Two outlines | both written, under different shapes, and neither shape appears in the last two ledger entries |
| Judged | seven dimensions scored for both outlines; totals and the tiebreak recorded |
| Chapters | 3-6 chapters, each 60 s or longer by target, summing to the length band |
| Payoff | the payoff sentence is something a viewer could repeat to a friend, and it sits where the shape says |
| Mission | the outline names the one thing the viewer can do or decide afterwards |
| Measurements | every planned experiment command is placed in a chapter, or the outline says why it is dropped |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Outline | `output/[slug]-outline.md` | per outline-format.md; frontmatter carries `structure` |
| Both outlines | `output/[slug]-outlines.md` | outline A, outline B, the score table, the judge's reasoning |
| Ledger | `../02-ideas/output/episode-ledger.json` | JSON list of `{slug, series, structure, date}` |

The winning outline in `output/` is the human edit surface and the cheapest place to change direction. Swap in the other outline by copying it over. The script stage reads whatever is there.
