---
slug: 2026-10-01-llmxray-local-llm-observabilit
workspace: shorts
title: "Local LLM observability: llmxray reads Ollama's gauges"
status: building
pillar: how-to
structure: worked-example
format: smooth-explainer
style_pack: signal
value_types: "EQUIPS,TEACHES"
created: 2026-10-01
updated: "2026-10-01T15:43:46Z"
publish_slot: ""
seo_score: 95
feedback: ""
blocked_reason: ""
assemble: "$ npx remotion still Assembly /home/buildlocalai/blai/builds/2026-10-01-llmxray-local-llm-observabilit/render/qa/safe-z\\\\\""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# llmxray: local LLM observability you can install tonight

## Artifacts
- Radar: [[stages/01-radar/output/2026-10-01-radar]]
- Ideas: [[stages/02-ideas/output/2026-10-01-ideas]]
- Research: [[stages/03-research/output/2026-10-01-llmxray-local-llm-observabilit-brief|Brief]]
- Script: [[stages/04-script/output/2026-10-01-llmxray-local-llm-observabilit-script|Script]]
- Package: [[stages/05-package/output/2026-10-01-llmxray-local-llm-observabilit-package|Package]]
- Voice: [[stages/06-voice/output/2026-10-01-llmxray-local-llm-observabilit-voice]]
- Render: (filled by stage 07)
- Publish: (filled by stage 08)

## Decisions
- Research checkpoint (unattended): angle confirmed as "llmxray makes what a local Ollama model is doing visible token by token on your own box"; one carry scenario for the explainer is the cache-killing timestamp.
- Research depth: 12 sources (web_search + web_extract; FireCrawl absent), 10 claims, 8 key numbers, validator exit 0.
- Picked as rank 1 (smooth-explainer, how-to, opportunity 68.4): strongest fresh-lane candidate; token-level observability for local models is unclaimed search ground (depth 15).
- Format smooth-explainer despite a two-day run: only two bands exist, fit wins per selection-rules.md; documented in the ideas note.

## Build journal

- 2026-10-01 stage 05: searchable title chosen (search-surface lane, keyword at char 0); description leads keyword+promise, names vLLM 0.29 KV-cache Short as closest watch; rubric 95/100 (only loss: 55-char title vs the 40 ideal, kept to carry both keyword and product in a fresh lane). contains_synthetic_media false (typographic scenes, creator's cloned voice). Ready for the Spark build.

- 2026-10-01 stage 04: draft A (worked-example) beat draft B (myth-bust) 18-17; no grafts. Gates: eval gate1_ready true (number_spend 3/3, hook waived-by-format, scene_specificity ok, skeleton ok, positional_labels ok, sameness ok, validator 0 blockers); 4 advisories kept with reasons in the script note. Ledger recorded; style pack signal.
- 2026-10-01T12:52:46Z build start on gn100-83c4
- 2026-10-01T12:55:18Z 06-voice ok 150s
- 2026-10-01T13:20:28Z 07-render fail 1508s (07-render: scene s9 did not pass safe_zone_check after 5 rounds)
- 2026-10-01T13:26:27Z 07-render fail 359s (07-render: assemble.py exited 1: xray-local-llm-observabilit/render/qa
assemble: $ node /home/buildlocalai/blai/repo/skills/render-shorts/remotion/scripts/loop_)
- 2026-10-01T13:26:27Z blocked at 07-render
- 2026-10-01T15:40:59Z telegram retry
- 2026-10-01T15:43:46Z build start on gn100-83c4
