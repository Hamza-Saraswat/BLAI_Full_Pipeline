# Stage 04: Outline

Set the direction of the episode: the angle, the two value types, the hook, the payoff, the chapters, and what a muted viewer should understand.

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

## Process

1. Propose 3 angles, one sentence each, tagged with value types. **[Checkpoint]** -- pick one (unattended: decide, record).
2. Write the value brief: concept, two locked value types with specifics, the hook in one sentence, the payoff in one sentence, the one surprising number spoken by 0:20.
3. Write the chapter outline per outline-format.md: 3-6 chapters, each with a target length, the one idea it carries, the measurement it shows (if any), and the visual philosophy line (what a muted viewer understands).
4. Run the audit checks below. If any fail, revise before saving.
5. Save `output/[slug]-outline.md`; update the hub (`value_types`, Decisions).
6. Unattended: `../../../../tools/git-sync.sh "long-form: [slug] outline"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | Three angles with value tags | Which angle |
| 2 | The value brief | Confirm before chapters are written |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Chapters | 3-6 chapters, each 60 s or longer by target, summing to the length band |
| Payoff | the payoff sentence is something a viewer could repeat to a friend |
| Mission | the outline names the one thing the viewer can do or decide afterwards |
| Measurements | every planned experiment command is placed in a chapter, or the outline says why it is dropped |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Outline | `output/[slug]-outline.md` | per outline-format.md |

The outline in `output/` is the human edit surface and the cheapest place to change direction. The script stage reads whatever is there.
