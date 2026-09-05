---
slug: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n
workspace: shorts
title: DGX Spark runs a 180B model at 43 tok/s
status: blocked
pillar: news-react
structure: news-react-so-what
format: classic
style_pack: silicon
value_types: "TEACHES,REFRAMES"
created: 2026-09-02
updated: "2026-09-05T22:04:21Z"
publish_slot: ""
seo_score: 100
feedback: ""
blocked_reason: "06-voice: voice QA failed: WER 0.035, 4 mismatch(es): expected 'per' heard 'a'; expected 'point' heard ''; expected '' heard 'gigabytes'"
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# DGX Spark runs Qwen3.8-Flash-Next at 43 tok/s in coding

## Artifacts
- Radar: [[stages/01-radar/output/2026-09-02-radar]]
- Ideas: [[stages/02-ideas/output/2026-09-02-ideas]]
- Research: [[stages/03-research/output/2026-09-02-dgx-spark-runs-qwen3-8-flash-n-brief]]
- Script: [[stages/04-script/output/2026-09-02-dgx-spark-runs-qwen3-8-flash-n-script]]
- Package: [[stages/05-package/output/2026-09-02-dgx-spark-runs-qwen3-8-flash-n-package]]
- Voice: [[stages/06-voice/output/2026-09-02-dgx-spark-runs-qwen3-8-flash-n-narration|narration.txt (normalized, stage 04)]]
- Render: [[stages/07-render/output/2026-09-02-dgx-spark-runs-qwen3-8-flash-n-render|render note]]
- Publish: (filled by stage 08)

## Decisions

## Build journal
- 2026-09-03T02:00:39Z 03-research ok: 8 sources, 8 claims, validator exit 0; unattended decision: 2.6x cited over 1.9x (names model+framework)
- 2026-09-03T02:43:36Z 04-script ok: drafts A(news-react-so-what) vs B(comparison-ladder), judge 22-21 A, graft of B bandwidth figures applied; validator 0 blockers, eval gates all pass (entity_spend 0.25 advisory: brief entity set carries vLLM/Qwen3.6/Qwen4 artifacts the script rightly omits, top2 present); sameness pass via explicit hook_pattern named-contradiction (classifier saw the digit); normalizer scenes_changed=2; ledger + silicon pack recorded
- 2026-09-03T02:44:44Z 05-package ok: seo rubric 100/100, check_outputs exit 0, title searchable (dgx spark keyword first), 3 hashtags, 12 tags, slot hint left empty for the publisher's own 11:00/18:00 CT rule
- 2026-09-03T07:18:49Z 06-voice ok 33.96s
- 2026-09-03T07:19:02Z 06-voice ok 33.96s
- 2026-09-03T09:33:00Z 07-render ok 35.07s: 6/6 scenes (attempts 1,2,1,1,1,1), lint/safe-zone/loop all pass (ssim 0.837), gate card message_id 5, status review
- 2026-09-05T21:56:27Z 2026-09-05 re-queued for the scripted render (scene_worker.py) with the creator voice clone; the 2026-09-03 stock-voice cut is superseded
- 2026-09-05T21:56:30Z build start on gn100-83c4
- 2026-09-05T21:57:44Z 06-voice fail 71s (voice QA failed: WER 0.068, 5 mismatch(es): expected 'qwen three point' heard 'q one three'; expected 'gigabytes' heard 'gb'; expected '' heard 'gb')
- 2026-09-05T21:57:49Z 06-voice fail 5s (voice QA failed: WER 0.068, 5 mismatch(es): expected 'qwen three point' heard 'q one three'; expected 'gigabytes' heard 'gb'; expected '' heard 'gb')
- 2026-09-05T21:57:49Z blocked at 06-voice
- 2026-09-05T22:04:07Z build start on gn100-83c4
- 2026-09-05T22:04:15Z 06-voice fail 5s (voice QA failed: WER 0.035, 4 mismatch(es): expected 'per' heard 'a'; expected 'point' heard ''; expected '' heard 'gigabytes')
- 2026-09-05T22:04:21Z 06-voice fail 6s (voice QA failed: WER 0.035, 4 mismatch(es): expected 'per' heard 'a'; expected 'point' heard ''; expected '' heard 'gigabytes')
- 2026-09-05T22:04:21Z blocked at 06-voice
