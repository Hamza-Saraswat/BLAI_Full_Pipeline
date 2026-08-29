# Stage 07: Render

Turn the storyboard, the narration and the captions into `final.mp4`, pass the machine gates, and send the Telegram gate card. Creative: the build agent runs this stage through Claude Code.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../04-script/output/[slug]-storyboard.json` | Full file | Scenes, tools, on-screen text, style pack |
| Previous stage | `../06-voice/output/[slug]-voice.md` | "Timing" | Actual duration per scene |
| Build dir | `[build-dir]/[slug]/voice/` | narration.wav, captions.json | Audio and word timings |
| Hub note | `../../videos/[slug].md` | `style_pack`, `feedback` | The pack and any re-render note |
| Skill | `../../../../skills/render-shorts/SKILL.md` | Full file | Renderers, assembly, linters |
| Skill rule | `../../../../skills/render-shorts/rules/scene-agent.md` | Full file | Scene worker rules, hard tokens, brand tokens |
| Skill rule | `../../../../skills/render-shorts/rules/hyperframes-1.md` | When a scene names hyperframes; `hyperframes-2.md` for the advanced sections it points to | Per-tool conventions |
| Skill rule | `../../../../skills/render-shorts/rules/manim-1.md` | When a scene names manim; `manim-2.md` for the advanced sections it points to | Per-tool conventions |
| Style pack | `../../../../skills/render-shorts/styles/` | The file named by `style_pack` | The look of this video |
| Skill | `../../../../skills/telegram-gate/SKILL.md` | "gate" card | Sending the card |
| Reference | `references/scene-workflow.md` | Full file | Parallelism, retries, draft then final, where files go, preview delivery |

## Process

1. Read the storyboard and the Timing table; set each scene's target duration from the captions (within 0.15 s).
2. Render scenes per scene-workflow.md: one worker per scene, three in parallel, draft first, verify, then final; at most 5 attempts per scene with the exact error fed back; a scene that fails 5 times blocks the run.
3. Run `assemble.py --slug [slug] --storyboard [storyboard] --audio [narration.wav] --captions [captions.json] --scenes-dir [build-dir]/[slug]/scenes --out [build-dir]/[slug]/render`.
4. Run `lint_video.py` and `safe_zone_check.py` on `final.mp4`; fix and re-assemble on failure.
5. Run the audit checks below. If any fail, fix before sending the card; if they cannot be fixed, set the hub note to `blocked`.
6. Write `output/[slug]-render.md`; update the hub (`status: review`, `preview_url` when a link is used); send `send_card.py --kind gate --hub [hub] --video [build-dir]/[slug]/render/final.mp4`.
7. `../../../../tools/git-sync.sh "shorts: [slug] render" workspaces/shorts skills/render-shorts/styles/history.json`.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Linters | `lint_video.py` and `safe_zone_check.py` exit 0 |
| Length | final duration within `final_warn_s` of the format band |
| Scenes | every storyboard scene has a rendered file and appears in the cut |
| Frame 1 | hook text legible at frame 1 with a motion onset within 0.5 s |
| Numbers | every number on screen is spoken in the same beat |

## Verify

| Compare | Against | Criteria |
|---------|---------|----------|
| Scene narration heard in the cut | `../04-script/output/[slug]-storyboard.json` | identical text; no scene added or dropped |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Render note | `output/[slug]-render.md` | gate results, scene timings, attempts, card message id |
| Video | `[build-dir]/[slug]/render/final.mp4` | never committed |

The Telegram card is the human gate. Approve publishes; Reject with a note, Re-render, or Re-script loop back through the hub note's `feedback`.
