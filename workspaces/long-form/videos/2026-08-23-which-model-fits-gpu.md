---
slug: 2026-08-23-which-model-fits-gpu
workspace: long-form
title: "LLM GPU Requirements: Which Qwen Build Fits Your Card"
status: review
pillar: ""
series: benchmarks
structure: buyers-guide
format: ""
style_pack: ""
value_types: "EQUIPS,TEACHES"
created: 2026-08-23
updated: "2026-08-23T14:40:29Z"
publish_slot: ""
seo_score: 100
feedback: ""
blocked_reason: ""
build_host: "local-mac"
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# Which local model actually fits your GPU

## Artifacts
- Radar: [[stages/01-radar/output/2026-08-23-radar]]
- Ideas: [[stages/02-ideas/output/2026-08-23-ideas]]
- Research: [[stages/03-research/output/2026-08-23-which-model-fits-gpu-brief]]
- Outline: [[stages/04-outline/output/2026-08-23-which-model-fits-gpu-outline]]
- Script: [[stages/05-script/output/2026-08-23-which-model-fits-gpu-script]]
- Spec: [[stages/06-spec/output/2026-08-23-which-model-fits-gpu-spec]]
- Package: [[stages/07-package/output/2026-08-23-which-model-fits-gpu-package]]
- Capture: [[stages/08-capture/output/2026-08-23-which-model-fits-gpu-capture]]
- Voice: (local test run; voice.json in .local-builds, not committed)
- Render: [[stages/10-render/output/2026-08-23-which-model-fits-gpu-render]]
- Publish: (filled by stage 11)

## Decisions
- Rendered locally on this Mac in local test mode, voiced by Kokoro rather than the ElevenLabs clone. Not publishable: `privacy_status` is `private` and `publish_slot_hint` is empty.
- `lint_longform.py` failed on duration only (493.4 s against a 648-792 s window). Left as a failure rather than waived: it is a real inconsistency between the script stage's word band and the render stage's duration target, logged as finding 48.
- Chapter times in the package replaced with the measured ones. The estimates were wrong by up to three minutes.


## Build journal
- 09:51 voice: kokoro, 3 chunks, 489.1 s, whisper alignment, 3.691 wps
- 09:55 render draft: 30 s at 640x360 in 19.5 s, 0 warnings
- 09:57 render full: 493.4 s at 1920x1080 in 386.9 s, 0 warnings, lint FAIL (duration)

