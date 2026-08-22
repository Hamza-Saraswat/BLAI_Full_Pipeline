# Stage 10: Render

Compile the spec, narration, captions and captures into the episode, render the thumbnails, pass the linters, and send the Telegram gate card. Creative: the build agent runs this stage through Claude Code.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../06-spec/output/[slug]-spec.json` | Full file | The scene list |
| Previous stage | `../09-voice/output/[slug]-voice.md` | "Chapters (measured)" | Chapter times |
| Previous stage | `../08-capture/output/[slug]-capture.md` | "Results" | Which captures exist |
| Build dir | `[build-dir]/[slug]/voice/` and `[build-dir]/[slug]/capture/` | narration.wav, captions.json, capture.json, casts | Audio, timings, recordings |
| Hub note | `../../videos/[slug].md` | `feedback`, `thumbnail_pick` | Re-render notes, chosen thumbnail |
| Skill | `../../../../skills/render-longform/SKILL.md` | Full file | Render command, lint, thumbnails |
| Skill rule | `../../../../skills/render-longform/rules/spec-to-composition.md` | Full file | Timing and compilation rules |
| Skill | `../../../../skills/blotato-publish/SKILL.md` | "r2.py" | Preview upload |
| Skill | `../../../../skills/telegram-gate/SKILL.md` | "gate" card | Sending the card |
| Reference | `references/render-workflow.md` | Full file | Draft then final, preview, chapters file |

## Process

1. Apply any `feedback` from a Re-render tap to the spec scenes it names (edit the spec in place and say so in the render note).
2. Run `render_longform.py --spec [spec] --audio [narration.wav] --captions [captions.json] --captures [capture dir] --out [build-dir]/[slug]/render --draft`; check the draft for a missing asset, a scene that reads wrong, or a sync point that misses; fix the spec or the data and re-run until the draft is clean.
3. Run the same command without `--draft`; run `lint_longform.py final.mp4 --target-s [target]`.
4. Write `[build-dir]/[slug]/render/chapters.json` from the measured chapter times (`[{"time": "MM:SS", "label": ...}]`).
5. Upload the preview: `r2.py upload [final.mp4] --key previews/[slug]/final.mp4`; set `preview_url` in the hub note.
6. Run the audit and verify checks below. If any fail, fix before sending the card; otherwise set the hub note to `blocked`.
7. Write `output/[slug]-render.md`; set `status: review`; send `send_card.py --kind gate --hub [hub] --preview-url [url]`.
8. `../../../../tools/git-sync.sh "long-form: [slug] render"`.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Linter | `lint_longform.py` exits 0 (1920x1080, 30 fps, loudness, duration within 10 %) |
| Thumbnails | three stills exist, each 1280x720 or larger and 2 MB or smaller |
| Chapters | `chapters.json` has one entry per spec chapter, ascending, 10 s or more apart |
| Captures | every terminal-replay scene found its capture; none rendered as a placeholder |

## Verify

| Compare | Against | Criteria |
|---------|---------|----------|
| Narration heard in the cut | `../05-script/output/[slug]-narration.txt` | identical text; no beat dropped |
| Scene order and count | `../06-spec/output/[slug]-spec.json` | identical; chapter cards at the chapter starts |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Render note | `output/[slug]-render.md` | lint report, chapter times, thumbnail list, card message id, attempts |
| Episode, thumbnails, chapters | `[build-dir]/[slug]/render/` | final.mp4, thumbnails/1-3.png, chapters.json, captions.srt (never committed) |

The Telegram card is the human gate. Approve publishes; Reject with a note, Re-render, or Re-script loop back through the hub note's `feedback`.
