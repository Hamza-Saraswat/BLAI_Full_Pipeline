---
slug: 2026-09-15-4x-dgx-sparks-the-rack-power-a
workspace: shorts
title: "DGX Spark cluster: the multi-node math"
status: published
pillar: explainer
structure: worked-example
format: smooth-explainer
style_pack: silicon
value_types: "TEACHES,REFRAMES"
created: 2026-09-15
updated: "2026-09-15T23:05:46Z"
publish_slot: "2026-09-15T18:00:00-05:00"
seo_score: 100
feedback: ""
blocked_reason: ""
build_host: gn100-83c4
preview_url: ""
youtube_url: "https://www.youtube.com/watch?v=q4T-g-opwUg"
blotato_post_id: c7842333-59bd-4fa1-9296-8451e2d872cd
---
# 4x DGX Sparks: the rack, power and multi-node math

## Artifacts
- Radar: [[stages/01-radar/output/2026-09-15-radar]]
- Ideas: [[stages/02-ideas/output/2026-09-15-ideas]]
- Research: [[stages/03-research/output/2026-09-15-4x-dgx-sparks-the-rack-power-a-brief]]
- Script: [[stages/04-script/output/2026-09-15-4x-dgx-sparks-the-rack-power-a-script]]
- Package: [[stages/05-package/output/2026-09-15-4x-dgx-sparks-the-rack-power-a-package]]
- Voice: [[stages/06-voice/output/2026-09-15-4x-dgx-sparks-the-rack-power-a-narration]] (normalized narration; voice render itself is stage 06 on the Spark)
- Render: [[stages/07-render/output/2026-09-15-4x-dgx-sparks-the-rack-power-a-render]]
- Publish: [[stages/08-publish/output/2026-09-15-4x-dgx-sparks-the-rack-power-a-publish]]

## Decisions

- Picked (unattended 2026-09-15): rank 1 at opportunity 100.0, deepest keyword in the pool (dgx spark, depth 224); explainer lane free of yesterday's picks.
- Format smooth-explainer: the rack/power/payoff math needs a worked example carried the whole way.
- Research (unattended 2026-09-15): 12 sources, 10 claims, 8 key numbers; validator exit 0. Thesis: four Sparks buy memory (512 GB, GLM-5.2 753B fits), not speed (26.5 tok/s ring decode vs 233-339 tok/s on four H200s); ring topology saves the 1500 GBP switch; colo cost and own-hardware tok/s parked under Unverified.
- Script (unattended 2026-09-15): checkpoint 1 -- structures worked-example + number-first (both rotation-legal vs how-to-three-moves and number-first in the ledger's last two); value types TEACHES, REFRAMES locked; promise: decide whether a Spark rack buys your model class, knowing it buys memory not speed. Checkpoint 2 -- 10 hooks scored, picks: A situation ("Your DGX Spark just hit its ceiling."), B price. B v1 failed sameness (number-first = 09-12 structure; price hook classified number-shock = 09-12 pattern); B rewritten as myth-bust, wrong-diagnosis hook with no number words. entity_spend advisory kept: 0.21 vs 0.5 target, the brief's entity pool is number-heavy (GB, tok/s, GBP) and the 3-number cap crowds out names; GLM + Ellis present in top2.
- Package (unattended 2026-09-15): checkpoint 3 -- searchable title "DGX Spark cluster: the multi-node math" picked over two intriguing variants (search-heavy product topic per the ideas keyword notes: "dgx spark" depth 224, competing titles are unboxings); rubric 100/100; description leads with 512 GB + 753B and links the closest published video (2026-09-02 DGX Spark 180B); contains_synthetic_media false (typographic scenes, creator's own cloned voice); tags 14 phrases, 198 chars.

## Build journal
- 2026-09-15T17:52:48Z 03-research ok: 12 sources, validator exit 0, status researched
- 2026-09-15T18:29:21Z 04-script ok: writerA kimi-k3 17.1k tok, writerB kimi-k3 18.9k tok (2 rounds), judge kimi-k3 5.3k tok; A (worked-example) beat B (myth-bust) 19-16, 1 graft; validator 0 blockers 0 advisories; eval gate1_ready true; variety check ok; normalizer 4 scenes changed
- 2026-09-15T18:31:08Z 05-package ok: searchable title (38 chars, keyword at 0), seo 100/100, check_outputs 0 failures, status ready-to-build
- 2026-09-15T18:35:46Z build start on gn100-83c4
- 2026-09-15T18:38:08Z 06-voice ok 140s
- 2026-09-15T19:06:16Z 07-render ok 102.17s: 11 scenes via scene_worker.py, lint True, safe-zone True, loop True, card message_id 66
- 2026-09-15T19:06:16Z 07-render ok 1685s
- 2026-09-15T19:06:18Z build done, status review
- 2026-09-15T19:16:18Z telegram approve (approved_at 2026-09-15T19:16:18Z)
- 2026-09-15T19:17:51Z 08-publish ok 4s
- 2026-09-15T23:05:46Z published https://www.youtube.com/watch?v=q4T-g-opwUg
