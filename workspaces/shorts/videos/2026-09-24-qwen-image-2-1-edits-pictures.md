---
slug: 2026-09-24-qwen-image-2-1-edits-pictures
workspace: shorts
title: Qwen-Image-2.1 edits your photos locally
status: blocked
pillar: how-to
structure: how-to-three-moves
format: smooth-explainer
style_pack: signal
value_types: "EQUIPS,TEACHES"
created: 2026-09-24
updated: "2026-09-24T12:37:07Z"
publish_slot: ""
seo_score: 100
feedback: ""
blocked_reason: "\"07-render: 07-render: assemble.py exited 1: 4-qwen-image-2-1-edits-pictures/render/qa"
assemble: "$ npx remotion still Assembly /home/buildlocalai/blai/builds/2026-09-24-qwen-image-2-1-edits-pictures/render/qa/safe\""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# Qwen-Image-2.1 does image editing too -- Unsloth ships it in FP8

## Artifacts
- Radar: [[stages/01-radar/output/2026-09-24-radar]]
- Ideas: [[stages/02-ideas/output/2026-09-24-ideas]]
- Research: [[stages/03-research/output/2026-09-24-qwen-image-2-1-edits-pictures-brief]]
- Script: [[stages/04-script/output/2026-09-24-qwen-image-2-1-edits-pictures-script]]
- Package: [[stages/05-package/output/2026-09-24-qwen-image-2-1-edits-pictures-package]]
- Voice: [[stages/06-voice/output/2026-09-24-qwen-image-2-1-edits-pictures-voice]]
- Render: (filled by stage 07)
- Publish: (filled by stage 08)

## Decisions
- Picked: opportunity 100.0, deepest autocomplete depth in the pool (155 vs next 44); covers the editing mode the 09-22 GGUF Short did not.
- Skipped for pick 2's slot context: none needed here; lane how-to differs from yesterday's comparison/explainer picks.
- 03 checkpoint: angle confirmed (editing mode + Unsloth FP8, not the GGUF pull); slug unchanged, no redirect.
- 04 checkpoint 1: structures A how-to-three-moves (has_process true, EQUIPS) vs B news-react-so-what (the shipping story, different shape); value types EQUIPS,TEACHES locked; promise: edit a photo with Qwen Image two point one on the card you already own, tonight.
- 04 checkpoint 2: 10 hooks scored; A took 1 (tonight), B took 2 (named-contradiction); last two ledger hooks were decision and number-shock, both picks clear rotation.
- 04 result: A won 21-19, no grafts. Gates: validator 0 blockers / 5 advisories (long s02/s04/s05 kept: mechanism and moves beats, split would break the analogy unit); eval 9/9; numbers 3 heard (14.23 GB, 7.26 GB spoken-only, 6 GB VRAM); hook_text pinned to "Photo edits tonight: three moves" so the ledger classifier reads the true pattern (tonight, not number-shock); style pack signal recorded.
- 05 checkpoint: searchable title picked over two intriguing (surface is search: autocomplete depth 155); rubric 100/100 all rows; manifest validated against publish-manifest.schema.json; contains_synthetic_media false (typographic scenes, creator voice clone); slot hint empty (default 11:00/18:00 CT rotation).

## Build journal
- 2026-09-24T11:40:23Z 03-research ok: 8 sources (6 primary), validator exit 0; Unverified: Nano Banana 2.0 comparison (Tom's Hardware paywalled)
- 2026-09-24T12:06:22Z 04-script ok: A how-to-three-moves beat B news-react 21-19 (kimi-k3 blind judge); 0 blockers, eval 9/9; ledger + style recorded.
- 2026-09-24T12:07:58Z 05-package ok: title "Qwen-Image-2.1 edits your photos locally", seo 100, check_outputs pass; ready-to-build.
- 2026-09-24T12:12:46Z build start on gn100-83c4
- 2026-09-24T12:18:32Z 06-voice ok 344s
- 2026-09-24T12:35:49Z 07-render fail 1034s (07-render: assemble.py exited 1: 4-qwen-image-2-1-edits-pictures/render/qa
assemble: $ node /home/buildlocalai/blai/repo/skills/render-shorts/remotion/scripts/l)
- 2026-09-24T12:37:07Z 07-render fail 78s (07-render: assemble.py exited 1: 4-qwen-image-2-1-edits-pictures/render/qa
assemble: $ node /home/buildlocalai/blai/repo/skills/render-shorts/remotion/scripts/l)
- 2026-09-24T12:37:07Z blocked at 07-render
