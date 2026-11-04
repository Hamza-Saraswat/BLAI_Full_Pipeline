---
slug: 2026-11-04-qwen-3-8-27b-reads-its-own-wei
workspace: shorts
title: Qwen 3.8 27B reads weights. Not its own.
status: blocked
pillar: how-to
structure: myth-bust
format: classic
style_pack: signal
value_types: "TEACHES,EQUIPS"
created: 2026-11-04
updated: "2026-11-04T13:20:38Z"
publish_slot: ""
seo_score: 90
feedback: ""
blocked_reason: "06-voice: voice QA failed: WER 0.045, 4 mismatch(es): expected 'thousand' heard 'zero'; expected 'thousand' heard ''; expected \\"rikiyat's\\" heard \\"ricky ateez's\\""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# Qwen 3.8 27B reads its own weights on a laptop

## Artifacts
- Radar: [[stages/01-radar/output/2026-11-04-radar]]
- Ideas: [[stages/02-ideas/output/2026-11-04-ideas]]
- Research: [[stages/03-research/output/2026-11-04-qwen-3-8-27b-reads-its-own-wei-brief]]
- Script: [[stages/04-script/output/2026-11-04-qwen-3-8-27b-reads-its-own-wei-script]]
- Package: [[stages/05-package/output/2026-11-04-qwen-3-8-27b-reads-its-own-wei-package]]
- Voice: [[stages/06-voice/output/2026-11-04-qwen-3-8-27b-reads-its-own-wei-narration|narration (normalized by stage 04; stage 6 adds audio)]]
- Render: (filled by stage 07)
- Publish: (filled by stage 08)

## Decisions
- 2026-11-04 ideas: picked -- how-to/classic, opportunity 79.4, keyword "qwen 3.8" depth 253; highest scorer after ollama rc0 was deduped (published 2026-10-25, same product+angle).
- Lane and band differ from yesterday's picks (explainer/smooth-explainer, comparison/classic); value types TEACHES,EQUIPS.
- 2026-11-04 research: checkpoint confirmed angle + slug, no redirect; brief corrects the "its own weights" framing via misconception 1 (it read a 17,253-parameter toy network). Standard depth, 14 sources, validator exit 0.
- 2026-11-04 script: checkpoint 1 confirmed structures worked-example + myth-bust (rotation clear vs comparison-ladder/story-first), value types TEACHES+EQUIPS. Checkpoint 2: 10 hooks scored, picks re-hooked after the sameness gate flagged number-shock repeating 2026-11-03. Both drafts passed all hard gates (validator 0 blockers, eval exit 0 each); soft entity_spend advisory kept with reason in the drafts note. Judge (kimi-k3, blind): B wins 21-20, no grafts. Winner fixed post-judge so the payoff line is the last spoken sentence. Style pack signal (rotation ok); ledger entry 60 recorded.
- 2026-11-04 package: checkpoint picked the intriguing title "Qwen 3.8 27B reads weights. Not its own." (searchable variant kept for search surface); rubric 90/100, every row full. check_outputs 0 failures after linking the package artifact (and the stage-04 normalized narration that already sits in 06-voice/output/). Hub to ready-to-build; stages 06-08 are the Spark build job's.

## Build journal
- 2026-11-04T13:15:53Z build start on gn100-83c4
- 2026-11-04T13:18:42Z 06-voice fail 166s (voice QA failed: WER 0.054, 4 mismatch(es): expected 'thousand' heard 'zero'; expected 'thousand' heard ''; expected 'waiting' heard 'weighting')
- 2026-11-04T13:20:38Z 06-voice fail 116s (voice QA failed: WER 0.045, 4 mismatch(es): expected 'thousand' heard 'zero'; expected 'thousand' heard ''; expected "rikiyat's" heard "ricky ateez's")
- 2026-11-04T13:20:38Z blocked at 06-voice
