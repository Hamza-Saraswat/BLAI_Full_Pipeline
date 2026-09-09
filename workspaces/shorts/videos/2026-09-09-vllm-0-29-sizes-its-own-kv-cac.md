---
slug: 2026-09-09-vllm-0-29-sizes-its-own-kv-cac
workspace: shorts
title: vLLM 0.29 sizes its own KV cache
status: researched
pillar: how-to
structure: ""
format: classic
style_pack: ""
value_types: "TEACHES,EQUIPS"
created: 2026-09-09
updated: "2026-09-09T11:56:19Z"
publish_slot: ""
seo_score: 0
feedback: ""
blocked_reason: ""
build_host: ""
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# vLLM 0.29 sizes its own KV cache

## Artifacts
- Radar: [[stages/01-radar/output/2026-09-09-radar]]
- Ideas: [[stages/02-ideas/output/2026-09-09-ideas]]
- Research: [[stages/03-research/output/2026-09-09-vllm-0-29-sizes-its-own-kv-cac-brief]]
- Script: (filled by stage 04)
- Package: (filled by stage 05)
- Voice: (filled by stage 06)
- Render: (filled by stage 07)
- Publish: (filled by stage 08)

## Decisions
- 2026-09-09 research: angle confirmed (unattended). MRV2 default + CUDA-graph memory profiling auto-sizes the KV cache at startup; 9 claims, 4 key numbers, 10 fetched sources; validator exit 0.
- 2026-09-09 ideas: picked (unattended). vLLM: top score 100.0 (autocomplete depth 223), release + one consequence, classic. MiniCPM5-2B: best candidate outside pick 1 lane and outside yesterday news-react/myth-bust lanes, smooth-explainer.
- Skipped TensorRT-LLM LoRA issue (rank 3): myth-bust repeats yesterday lane; skipped LTX 2.5 (rank 2): shares pick 1 how-to lane.

## Build journal
