---
slug: 2026-11-11-minimax-h3-image-in-comfyui-lo
workspace: shorts
title: Install MiniMax H3-Image in ComfyUI
status: review
pillar: how-to
structure: how-to-three-moves
format: smooth-explainer
style_pack: terminal
value_types: "TEACHES,EQUIPS"
created: 2026-11-11
updated: "2026-11-11T14:08:29Z"
publish_slot: ""
seo_score: 100
feedback: ""
blocked_reason: ""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# MiniMax H3-Image in ComfyUI: local image gen today

## Artifacts
- Radar: [[stages/01-radar/output/2026-11-11-radar]]
- Ideas: [[stages/02-ideas/output/2026-11-11-ideas]]
- Research: [[stages/03-research/output/2026-11-11-minimax-h3-image-in-comfyui-lo-brief]]
- Script: [[stages/04-script/output/2026-11-11-minimax-h3-image-in-comfyui-lo-script]]
- Package: [[stages/05-package/output/2026-11-11-minimax-h3-image-in-comfyui-lo-package]]
- Voice: [[stages/06-voice/output/2026-11-11-minimax-h3-image-in-comfyui-lo-voice]]
- Render: [[stages/07-render/output/2026-11-11-minimax-h3-image-in-comfyui-lo-render]]
- Publish: (filled by stage 08)

## Decisions
- 03-research checkpoint: angle kept as picked ("open weights 3 d ago; load the Comfy-Org node, generate on your own GPU tonight"), slug unchanged.
- Why: pick is the day's top opportunity (97.4) and the primary pages fetched this run support the full walkthrough; no redirect needed.
- 04-script checkpoint: structures A how-to-three-moves vs B contrarian-take (rotation banned the last two shipped), value types TEACHES+EQUIPS confirmed, promise "generate inside ComfyUI tonight, knowing the disk cost and the unpublished VRAM floor".
- 04-script hooks: 10 written, picks A=tonight ("MiniMax H3 runs tonight") and B=wrong-diagnosis, different patterns because number-shock and situation were the last two shipped.
- 04-script judge: A 19, B 17; one graft applied (RTX 3060 correction sentence from B into A s09), gates re-run clean after it. Kept because the judge is contract law here and the graft passed every gate.
- 05-package checkpoint: title pick "Install MiniMax H3-Image in ComfyUI" (searchable; the topic is search-heavy, autocomplete depth 88), rubric 100/100, description and manifest written, check_outputs clean.

## Build journal
- 2026-11-11T12:41:06Z 03-research ok: brief 12 sources, 10 claims (8 primary / 2 docs), validator exit 0; unattended checkpoint: angle confirmed as picked, no redirect
- 2026-11-11T13:13:03Z 04-script ok: draft A how-to-three-moves beat draft B contrarian-take 19-17; validator 0/0, eval 9/9, normalizer 2 scenes changed; 1 graft (RTX 3060 correction from B); ledger entry 67 recorded; style pack terminal
- 2026-11-11T13:14:56Z 05-package ok: seo 100/100, title searchable 35 chars, check_outputs 0 failures, manifest schema PASS; status ready-to-build; produce half ends here, build.py --once takes it from here
- 2026-11-11T13:20:10Z build start on gn100-83c4
- 2026-11-11T13:22:34Z 06-voice ok 142s
- 2026-11-11T13:33:29Z 07-render fail 652s (07-render: scene s04 did not pass HyperFrames inspect after 5 rounds: t=7.4s container_overflow #timeline-panel inside div.panel-slot overflowed bottom 2.56px —)
- 2026-11-11T14:08:53Z 07-render ok 110.50s: 11 scenes via scene_worker.py, lint True, safe-zone True, loop True, card message_id 345
- 2026-11-11T14:08:53Z 07-render ok 2124s
- 2026-11-11T14:09:01Z build done, status review
