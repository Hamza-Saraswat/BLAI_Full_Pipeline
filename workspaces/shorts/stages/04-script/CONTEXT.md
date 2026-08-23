# Stage 04: Script

Turn the brief into two competing drafts, judge them, and hand the winner to the build agent as a script and a storyboard. Facts bind you; shape does not.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../03-research/output/[slug]-brief.md` | Full file | Every fact, number, analogy, viewer situation and objection comes from here |
| Hub note | `../../videos/[slug].md` | Frontmatter: pillar, format, value_types, feedback | What was locked at ideation; any re-script feedback |
| Brand vault | `../../../../brand-vault/voice-rules.md` | "Hard Constraints" through "What the Voice Is NOT" | Voice, navigation, wit, person, the ending rule |
| Brand vault | `../../../../brand-vault/signature-analogies.md` | The analogy this topic needs, or "Rules" | Re-teach a known picture in fresh words |
| Brand vault | `../../../../brand-vault/identity.md` | "Audience" | Who is listening |
| Reference | `references/script-structures.md` | Full file | The menu, the rotation rule, how to pick two |
| Reference | `references/hook-library.md` | Full file | Hook patterns and scoring |
| Reference | `references/judge-rubric.md` | Full file | How the winner is chosen |
| Reference | `references/script-format.md` | Full file | Layout of the script note, the drafts note and the storyboard mapping |
| Skill | `../../../../skills/script-gates/SKILL.md` | Full file | Validator, eval gates, variety check, normalizer |
| Skill rule | `../../../../skills/script-gates/rules/format-bands.md` | Row for the hub's `format` | Duration, words, scene count, numbers policy, person |
| Skill rule | `../../../../skills/render-shorts/rules/style-packs.md` | "Selection rules" | Choosing the style pack |
| Shared | `../../../../shared/platform-specs.md` | "Shorts" table | Safe area, caption band, hook physics |
| Ledger | `output/script-ledger.json` | Last 5 entries | Structure, hook, closing and duration rotation |

## Process

1. Read the brief and the hub note. Rank the structures by fit and take the **top two**, both clearing the rotation rule. Confirm the two locked value types and write the promise in one sentence. **[Checkpoint]** -- present the two structures, the value types and the promise.
2. Write 10 hook candidates per hook-library.md and score them. Keep the best two, one for each draft. **[Checkpoint]** -- present the 10 with the two picks marked.
3. Write **draft A and draft B in parallel**, one worker each. A worker receives only: the brief, the voice-rule sections, signature-analogies.md, its own structure row, the hook library, its band row and the Shorts platform row. Neither worker sees the other's draft.
4. Pick the style pack (`style_rotation.py --pick --slug [slug]`) and build a storyboard JSON for each draft per script-format.md.
5. Run `normalize_narration.py`, `validate_storyboard.py` and `eval_short.py --ledger output/script-ledger.json` on both. Fix blockers inside the draft that has them; a draft still failing after two rounds is withdrawn and the other wins by default.
6. Judge the survivors per judge-rubric.md. Apply any graft the rubric allows. Write `output/[slug]-drafts.md`.
7. Run the audit checks below. If any fail, revise before saving.
8. Save the winner as `output/[slug]-script.md` and `output/[slug]-storyboard.json`; run `variety_check.py record --storyboard output/[slug]-storyboard.json --ledger output/script-ledger.json`; record the style pack (`style_rotation.py --record`); update the hub note (`status: scripted`, `structure`, `style_pack`, `value_types`, Artifacts link, Decisions).
9. Unattended: `../../../../tools/git-sync.sh "shorts: [slug] script"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | The two structures, the value types, the promise | Approve or redirect before drafting |
| 2 | 10 hooks with the two picks marked | Pick others or approve |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Validator | `validate_storyboard.py` reports zero blockers on the winner |
| Eval gates | `eval_short.py` passes `number_spend`, `hook_concrete`, `scene_specificity`, `skeleton`, `positional_labels`, `sameness` and `validator`; the entity gates may warn |
| Navigation | no positional label survives unless the structure permits it and each names an action |
| Payoff timing | the first concrete fact is spoken by second 4 of the estimate |
| Ending | the last spoken sentence is the payoff; no ask, no tease, no extra recap |
| Voice | zero Hard Constraint violations; second person inside the first three sentences; at most one wry beat per 20 seconds |
| Value delivery | the script delivers both locked value types, and the note names the line for each |
| Two real drafts | `output/[slug]-drafts.md` holds both drafts, both score tables and the winner's reason |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Script | `output/[slug]-script.md` | per script-format.md |
| Storyboard | `output/[slug]-storyboard.json` | `shared/schemas/storyboard.schema.json` |
| Drafts and scores | `output/[slug]-drafts.md` | per judge-rubric.md |
| Ledger | `output/script-ledger.json` | appended by `variety_check.py` |

The script and the storyboard in `output/` are the human edit surface. Rewrite a line, swap the hook, change a scene. The package stage and the build agent read whatever is there.
