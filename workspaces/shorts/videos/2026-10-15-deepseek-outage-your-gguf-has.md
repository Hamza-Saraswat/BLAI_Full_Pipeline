---
slug: 2026-10-15-deepseek-outage-your-gguf-has
workspace: shorts
title: DeepSeek down? Your GGUF never noticed
status: building
pillar: myth-bust
structure: myth-bust
format: smooth-explainer
style_pack: halftone
value_types: "TEACHES,REFRAMES"
created: 2026-10-15
updated: "2026-10-15T12:25:43Z"
publish_slot: ""
seo_score: 95
feedback: ""
blocked_reason: ""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# DeepSeek outage: your GGUF has no status page

## Artifacts
- Radar: [[stages/01-radar/output/2026-10-15-radar]]
- Ideas: [[stages/02-ideas/output/2026-10-15-ideas]]
- Research: [[stages/03-research/output/2026-10-15-deepseek-outage-your-gguf-has-brief]]
- Script: [[stages/04-script/output/2026-10-15-deepseek-outage-your-gguf-has-script]]
- Package: [[stages/05-package/output/2026-10-15-deepseek-outage-your-gguf-has-package]]
- Voice: [[stages/06-voice/output/2026-10-15-deepseek-outage-your-gguf-has-narration]]
- Render: (filled by stage 07)
- Publish: (filled by stage 08)

## Decisions
- Picked over #2 Open WebUI (81.7): a second news-react would break the one-per-day rule; the outage angle reframes as myth-bust with a durable evergreen pull.
- Format: smooth-explainer per selection-rules.md (a belief to dismantle: "the cloud API is the model"; needs a worked example carried through).
- 03 checkpoint (unattended): angle confirmed as "when the hosted API blinks out, a local GGUF keeps generating; dependency is a choice"; slug unchanged.
- 03 research: 12 sources fetched (status page, incident, history, pricing, R1 card, three GGUF cards, two HF API records, Reuters, HN); validator exit 0; has_process false (argument video, no viewer steps); thesis: the API is a service wrapped around open-weight models.

- 04 checkpoint (unattended): structures myth-bust (A) and comparison-ladder (B), both clearing rotation; value types TEACHES+REFRAMES confirmed; promise: after this you can say what failed, why a GGUF kept working, and which copy fits your GPU.
- 04 hooks: 10 candidates scored; A kept the situation hook "DeepSeek went down last night. Yours didn't have to."; B drew a decision hook to force divergence.
- 04 gates: validator 0 blockers 0 advisories on the winner; eval gate1_ready (soft advisories entity_spend, top2 kept with reason); number budget capped at three (4h 52m, 404.43 GB, 24 GB); judge A 21-16, no grafts; variety_check clean; style pack halftone; ledger entry 40; normalizer 10 scenes, 8 changed.

- 05 checkpoint (unattended): titles "DeepSeek API outage: run the model locally instead" (searchable) / "DeepSeek down? Your GGUF never noticed" (intriguing, chosen) / "The DeepSeek outage your local model slept through"; rubric 95/100 (5-point dock: title and hook share one angle); feed-first surface picked the intriguing one.
- 05 package: description keyword-first with the Ecosia open-weights video as closest related; 3 hashtags; 15 tags (218 chars); contains_synthetic_media false (typographic scenes + creator voice clone); original_insight: October's five incidents vs 99.47% Flash uptime reframes the outage as an opted-in dependency; check_outputs exit 0.

## Build journal
- 2026-10-15T12:25:43Z build start on gn100-83c4
- 2026-10-15T12:27:44Z 06-voice ok 118s
