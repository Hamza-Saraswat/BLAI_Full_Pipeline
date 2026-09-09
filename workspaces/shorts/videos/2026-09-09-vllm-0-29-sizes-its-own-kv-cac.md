---
slug: 2026-09-09-vllm-0-29-sizes-its-own-kv-cac
workspace: shorts
title: vLLM 0.29 sizes its own KV cache now
status: approved
pillar: how-to
structure: worked-example
format: classic
style_pack: blueprint
value_types: "TEACHES,EQUIPS"
created: 2026-09-09
updated: "2026-09-09T14:13:55Z"
publish_slot: ""
seo_score: 100
feedback: ""
blocked_reason: ""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# vLLM 0.29 sizes its own KV cache

## Artifacts
- Radar: [[stages/01-radar/output/2026-09-09-radar]]
- Ideas: [[stages/02-ideas/output/2026-09-09-ideas]]
- Research: [[stages/03-research/output/2026-09-09-vllm-0-29-sizes-its-own-kv-cac-brief]]
- Script: [[stages/04-script/output/2026-09-09-vllm-0-29-sizes-its-own-kv-cac-script]] (+ [[stages/04-script/output/2026-09-09-vllm-0-29-sizes-its-own-kv-cac-drafts|drafts]] and [[stages/04-script/output/2026-09-09-vllm-0-29-sizes-its-own-kv-cac-storyboard|storyboard]])
- Package: [[stages/05-package/output/2026-09-09-vllm-0-29-sizes-its-own-kv-cac-package]]
- Voice: [[stages/06-voice/output/2026-09-09-vllm-0-29-sizes-its-own-kv-cac-voice]]
- Render: [[stages/07-render/output/2026-09-09-vllm-0-29-sizes-its-own-kv-cac-render]]
- Publish: (filled by stage 08)

## Decisions
- 2026-09-09 research: angle confirmed (unattended).
- 2026-09-09 package (unattended): searchable title chosen (keyword depth 223 makes this a search-surface Short); rubric 100/100; contains_synthetic_media false (typographic scenes, creator voice); original_insight ties the boot-crash advice to the MRV2 graph-probe bug. Hub set ready-to-build for the Spark build job.
- 2026-09-09 script (unattended): structures worked-example (A) vs number-first (B), rotation clear; A won 21-20, no grafts. Gates on winner: validator 0/0, eval gate1_ready true, variety check ok; hooks named-contradiction (A) and number-shock (B) from 10 scored. Style pack blueprint (topic fit; prev halftone). Two in-draft gate fixes named in the drafts note (number_spend second number, B hook-scene trim). MRV2 default + CUDA-graph memory profiling auto-sizes the KV cache at startup; 9 claims, 4 key numbers, 10 fetched sources; validator exit 0.
- 2026-09-09 ideas: picked (unattended). vLLM: top score 100.0 (autocomplete depth 223), release + one consequence, classic. MiniCPM5-2B: best candidate outside pick 1 lane and outside yesterday news-react/myth-bust lanes, smooth-explainer.
- Skipped TensorRT-LLM LoRA issue (rank 3): myth-bust repeats yesterday lane; skipped LTX 2.5 (rank 2): shares pick 1 how-to lane.

## Build journal
- 2026-09-09T13:35:20Z build start on gn100-83c4
- 2026-09-09T13:36:23Z 06-voice ok 61s
- 2026-09-09T13:49:41Z 07-render ok 40.33s: 6 scenes via scene_worker.py, lint True, safe-zone True, loop True, card message_id 43
- 2026-09-09T13:49:41Z 07-render ok 795s
- 2026-09-09T13:49:44Z build done, status review
- 2026-09-09T14:13:55Z telegram approve (approved_at 2026-09-09T14:13:55Z)
