---
slug: 2026-11-23-local-llms-reproduce-claude-wh
workspace: shorts
title: Local LLMs reproduce Claude? Receipts
status: expired
pillar: myth-bust
structure: worked-example
format: smooth-explainer
style_pack: halftone
value_types: "REFRAMES,TEACHES"
created: 2026-11-23
updated: "2026-11-24T14:35:39Z"
publish_slot: ""
seo_score: 100
feedback: ""
blocked_reason: ""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# Local LLMs reproduce Claude: what the experiments show

## Artifacts
- Radar: [[stages/01-radar/output/2026-11-23-radar]]
- Ideas: [[stages/02-ideas/output/2026-11-23-ideas]]
- Research: [[stages/03-research/output/2026-11-23-local-llms-reproduce-claude-wh-brief|Brief]]
- Script: [[stages/04-script/output/2026-11-23-local-llms-reproduce-claude-wh-script|Script]] ([[stages/04-script/output/2026-11-23-local-llms-reproduce-claude-wh-drafts|drafts]], [[stages/04-script/output/2026-11-23-local-llms-reproduce-claude-wh-storyboard|board]])
- Package: [[stages/05-package/output/2026-11-23-local-llms-reproduce-claude-wh-package|Package]]
- Voice: [[stages/06-voice/output/2026-11-23-local-llms-reproduce-claude-wh-narration|Narration]] (normalized pre-voice; stage 06 fills the rest)
- Render: [[stages/07-render/output/2026-11-23-local-llms-reproduce-claude-wh-render]]
- Publish: (filled by stage 08)

## Decisions
- 2026-11-23T12:50:03Z 03-research checkpoint (angle/slug): slug confirmed; angle unchanged from pick 2, receipts-first read of the reproduce-Claude claim. Unattended call: proceed.
03-research: standard depth, 10 sources fetched this run, validator exit 0; 10 claims, 8 key numbers. Thesis: reproduced is last year's Claude, half speed, rehearsed workloads -- not today's, not drop-in.
- 2026-11-23T13:15:50Z - 04-script checkpoint (structures/promise): A worked-example vs B contrarian-take, both clear the last-two rotation (news-react-so-what, myth-bust). Promise: viewer can decide whether Claude-at-home replaces the subscription and name the trade. Unattended call: proceed.
- 04-script checkpoint (hooks): 10 written and scored per hook-library; picks were situation (A) and wrong-diagnosis (B), different patterns by construction. Unattended call: proceed.
- 04-script: blind kimi-k3 writers A/B (worked-example, situation hook) and judge all via llm_call.py; A won 22-20. One graft from B (independent-engineer sentence, s08). Gates on winner: validator 0 blockers (3 advisories: tags list is stage-05 work; s08 est 18.3s over the 16s advisory split line -- the verdict beat carries judge-approved graft, kept whole rather than split mid-argument); eval 0 failures (number_spend 2/8 under cap-only policy, entity/top2 pass); sameness clean; normalizer 0 scenes changed. Ledger + halftone recorded.
- 2026-11-23T13:17:32Z - 05-package checkpoint (titles/desc/score): searchable pick "Local LLMs reproduce Claude? Receipts" (37 chars, keyword at 0) over two intriguing variants; description opens keyword+promise in first 91 chars; rubric 100/100. Unattended call: proceed.
- 05-package: contains_synthetic_media false (typographic scenes + creator voice clone, exempt); original_insight names the no-blind-test gap and the trade; no duplicate title vs published/. check_outputs clean after Artifacts links filled.

## Build journal
- 2026-11-23T13:18:10Z build start on gn100-83c4
- 2026-11-23T13:21:37Z 06-voice ok 204s
- 2026-11-23T13:41:09Z 07-render fail 1169s (07-render: scene s06 did not pass HyperFrames inspect after 5 rounds: t=3.03-8.37s (64 samples) content_overlap span.gpu-label inside span.body-text.mono "YOUR )
- 2026-11-23T14:01:36Z 07-render ok 91.20s: 10 scenes via scene_worker.py, lint True, safe-zone True, loop True, card message_id 383
- 2026-11-23T14:01:36Z 07-render ok 1226s
- 2026-11-23T14:01:38Z build done, status review
- 2026-11-24T14:35:39Z 2026-11-24T14:35:39Z expired: not from today's picks (2026-11-24); the factory carries no backlog
