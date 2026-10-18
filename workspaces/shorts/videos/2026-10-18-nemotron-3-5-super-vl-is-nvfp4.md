---
slug: 2026-10-18-nemotron-3-5-super-vl-is-nvfp4
workspace: shorts
title: "Nemotron NVFP4: which GPUs can run it"
status: approved
pillar: explainer
structure: worked-example
format: classic
style_pack: silicon
value_types: "TEACHES,REFRAMES"
created: 2026-10-18
updated: "2026-10-18T14:20:04Z"
publish_slot: ""
seo_score: 93
feedback: ""
blocked_reason: ""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# Nemotron 3.5 Super VL is NVFP4 only: what that means for local

## Artifacts
- Radar: [[stages/01-radar/output/2026-10-18-radar]]
- Ideas: [[stages/02-ideas/output/2026-10-18-ideas]]
- Research: [[stages/03-research/output/2026-10-18-nemotron-3-5-super-vl-is-nvfp4-brief]]
- Script: [[stages/04-script/output/2026-10-18-nemotron-3-5-super-vl-is-nvfp4-script]]
- Package: [[stages/05-package/output/2026-10-18-nemotron-3-5-super-vl-is-nvfp4-package]]
- Voice: [[stages/06-voice/output/2026-10-18-nemotron-3-5-super-vl-is-nvfp4-voice]]
- Render: [[stages/07-render/output/2026-10-18-nemotron-3-5-super-vl-is-nvfp4-render]]
- Publish: (filled by stage 08)

## Decisions

- 03 checkpoint: angle confirmed unchanged (NVFP4 ties the model to NVIDIA GPUs; everyone else re-routes through a GGUF re-quant); slug unchanged.
- 03 research: 9 sources (5 primary), validator exit 0; unverified keeps local tok/s and any NVFP4-vs-Q4_K_M quality claim out of the script.

- Pick 2 of 2, 2026-10-18: explainer lane, classic; opportunity 52.5 (autocomplete depth 10), names Nemotron 3.5 Super VL.
- Lane rotation: news-react and how-to (yesterday's picks) excluded; nvfp4 quantization is one fact with one consequence, so classic.

- 04 structures: worked-example vs myth-bust (rotation clean; last two were how-to-three-moves and news-react-so-what); A won 21-18; grafts: power-adapter line, hardware-commitment close.
- 04 hooks: 10 candidates scored; picks "You downloaded the wrong Nemotron." (wrong-diagnosis, A) and "Everyone says just quantize it." (named-contradiction, B), both off the last-two patterns (tonight, number-shock).
- 04 gates: winner validator 0 blockers 0 advisories; eval all hard gates pass; sameness clean vs last 5; normalizer 6 scenes / 2 changed; ledger entry 43 recorded; style silicon recorded (prev terminal).
- 04 soft gates kept with reason: entity_spend 0.065, top2 NVIDIA/Blackwell absent as literal tokens (extractor misses possessives; script carries "NVIDIA's" and "Blackwell tensor cores" once each).
- 04 value lines: TEACHES = s2 "weights are quantized, stored in fewer bits, four each. Sixteen weights share a scale"; REFRAMES = s3 "The blocker is generation, not size."
- 05 checkpoint: searchable title picked over two intriguing variants (thin "nvfp4" keyword field is product-query surface); score 93, rubric rows all pass.
- 05 compliance: contains_synthetic_media false (typographic scenes + creator voice clone, both exempt); original_insight names the silicon-gate reframe; narration normalized files live beside the storyboard (2026-10-17 precedent), 06-voice/output left for the Spark.
## Build journal
- 2026-10-18T11:50:53Z 03-research ok: 9 sources, validator 0
- 2026-10-18T12:21:43Z 04-script ok: A won 21-18, gates clean, ledger+style recorded
- 2026-10-18T12:23:53Z 05-package ok: seo 93, ready-to-build
- 2026-10-18T12:27:10Z build start on gn100-83c4
- 2026-10-18T12:28:13Z 06-voice ok 61s
- 2026-10-18T12:45:31Z 07-render ok 44.80s: 6 scenes via scene_worker.py, lint True, safe-zone True, loop True, card message_id 240
- 2026-10-18T12:45:31Z 07-render ok 1035s
- 2026-10-18T12:45:33Z build done, status review
- 2026-10-18T14:20:04Z telegram approve (approved_at 2026-10-18T14:20:04Z)
