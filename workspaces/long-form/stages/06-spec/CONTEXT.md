# Stage 06: Spec

Turn the script into a scene list the render stage compiles. The spec says what and when, never how.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../05-script/output/[slug]-script.md` | Every chapter's beat table | Beats become scenes |
| Previous stage | `../05-script/output/[slug]-narration.txt` | Full file | The narration the scenes must cover exactly |
| Previous stage | `../04-outline/output/[slug]-outline.md` | "Chapters", "Visual philosophy" | Chapter starts and the visual stance |
| Previous stage | `../03-research/output/[slug]-experiment.md` | Command ids, when present | `capture_ref` values |
| Skill rule | `../../../../skills/render-longform/rules/scene-library.md` | Full file | Scene types and what each needs in `data` |
| Skill rule | `../../../../skills/render-longform/rules/thumbnails.md` | Full file | Thumbnail concepts |
| Reference | `references/spec-format.md` | Full file | Enabled scene types, the spec note layout, the verify rule |
| Schema | `../../../../shared/schemas/longform-spec.schema.json` | Full file | Field names and limits |
| Playbook | `../../../../shared/playbook/thumbnails.md` | "Long-form" | Thumbnail rules |

## Process

1. Map each beat to one scene: pick the type from the enabled list in spec-format.md, write `visual_intent`, `on_screen_text`, `data` per the scene library, `est_duration_s` from the beat's word count (about 2.5 words per second), `capture_ref` for measured beats, and sync points for numbers that must land on a word.
2. Set `chapters` (label and `starts_at_scene`), `target_duration_s`, `music_mood`, and three thumbnail concepts (words and focus). **[Checkpoint]** -- present the scene-type sequence and the three concepts.
3. Write `output/[slug]-spec.json` and `output/[slug]-spec.md` (the human-readable table).
4. Run `python3 ../../../../tools/check_outputs.py` (validates the spec against the schema).
5. Run the audit and verify checks below. If any fail, revise before saving.
6. Update the hub (Artifacts link, Decisions).
7. Unattended: `../../../../tools/git-sync.sh "long-form: [slug] spec"`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | The scene-type sequence by chapter and the three thumbnail concepts | Approve or change the visual mix |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Schema | `check_outputs.py` exits 0 |
| Variety | no scene type three times in a row; at least four distinct types per episode |
| Enabled only | every scene type is in the enabled list |
| Durations | scene durations sum to the target within 10 %; no scene over 45 s except terminal-replay and code-typing |
| Thumbnails | three concepts, each 4 words or fewer with one focus |

## Verify

| Compare | Against | Criteria |
|---------|---------|----------|
| Scene narrations in order | `../05-script/output/[slug]-narration.txt` | concatenation equals the narration file (whitespace aside); no beat dropped or merged |
| `chapters[].starts_at_scene` | `../04-outline/output/[slug]-outline.md` | one chapter card per outline chapter, in order |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Spec | `output/[slug]-spec.json` | `shared/schemas/longform-spec.schema.json` |
| Spec note | `output/[slug]-spec.md` | per spec-format.md |

The spec is the human edit surface for visuals. Change a scene type, move a chapter card. The package stage and the render stage read whatever is there.
