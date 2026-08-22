# Stage 04: Script

Turn the brief into a Short's script and a storyboard the build agent can render. Facts bind you; shape does not.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../03-research/output/[slug]-brief.md` | Full file | Every fact, number and analogy comes from here |
| Hub note | `../../videos/[slug].md` | Frontmatter: pillar, format, value_types, feedback | What was locked at ideation; any re-script feedback |
| Brand vault | `../../../../brand-vault/voice-rules.md` | "Hard Constraints" through "What the Voice Is NOT" | Voice discipline |
| Brand vault | `../../../../brand-vault/identity.md` | "Audience" | Who is listening |
| Reference | `references/script-structures.md` | Full file | The structure menu and rotation rule |
| Reference | `references/hook-library.md` | Full file | Hook patterns; write 10, keep 1 |
| Reference | `references/script-format.md` | Full file | Layout of the script note and the storyboard mapping |
| Skill | `../../../../skills/script-gates/SKILL.md` | Full file | Validator, eval gates, normalizer commands |
| Skill rule | `../../../../skills/script-gates/rules/format-bands.md` | Row for the hub's `format` | Duration, words, scene count, numbers policy |
| Skill rule | `../../../../skills/render-shorts/rules/style-packs.md` | "Selection rules" | Choosing the style pack |
| Shared | `../../../../shared/platform-specs.md` | "Shorts" table | Safe area, caption band, hook physics |
| Ledger | `output/structure-ledger.json` | Last 7 entries | Structure rotation |

## Process

1. Read the brief and the hub note. Choose the structure (must differ from the other pick today and from the last two ledger entries) and confirm the two value types. **[Checkpoint]** -- present structure, value types and the one-sentence promise.
2. Write 10 hook candidates per hook-library.md; pick the strongest. **[Checkpoint]** -- present the 10 with the pick marked.
3. Write the full script in one pass per script-format.md: narration in spoken form, on-screen text with digits, a scene plan with tool and layout per scene, estimates inside the format band.
4. Pick the style pack: `python3 ../../../../skills/render-shorts/scripts/style_rotation.py --pick --slug [slug]`, then `--record [pack] --slug [slug]`.
5. Produce `output/[slug]-storyboard.json` (mapping in script-format.md). Run `normalize_narration.py`, `validate_storyboard.py` and `eval_short.py` from the script-gates skill; fix until zero blockers and the hard gates pass.
6. Run the audit checks below. If any fail, revise before saving.
7. Save `output/[slug]-script.md`; append `{slug, structure, date}` to `output/structure-ledger.json`; update the hub note (`status: scripted`, `structure`, `style_pack`, `value_types`, Artifacts link, Decisions).
8. Unattended: `../../../../tools/git-sync.sh "shorts: [slug] script"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | Structure, value types, promise | Approve or redirect before writing |
| 2 | 10 hooks with the pick marked | Pick another or approve |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Validator | `validate_storyboard.py` reports zero blockers |
| Eval gates | `eval_short.py` passes number_spend, hook_concrete, scene_specificity, skeleton and validator; entity gates may warn |
| Payoff timing | the first concrete fact is spoken by second 4 of the estimate |
| Voice | zero Hard Constraint violations; FK grade 5 or lower; sentences 20 words or fewer, average 15 or fewer |
| Value delivery | the script delivers both locked value types (the note names the line for each) |
| Rotation | the ledger shows the structure was not used in the previous two runs |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Script | `output/[slug]-script.md` | per script-format.md |
| Storyboard | `output/[slug]-storyboard.json` | `shared/schemas/storyboard.schema.json` |
| Ledger | `output/structure-ledger.json` | JSON list of `{slug, structure, date}` |

The script and the storyboard in `output/` are the human edit surface. Rewrite a line, swap the hook, change a scene. The package stage and the build agent read whatever is there.
