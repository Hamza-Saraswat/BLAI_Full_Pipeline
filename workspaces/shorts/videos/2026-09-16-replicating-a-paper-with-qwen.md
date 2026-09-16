---
slug: 2026-09-16-replicating-a-paper-with-qwen
workspace: shorts
title: "Qwen-2.5 replicates Jev's trick at home"
status: scheduled
pillar: how-to
structure: myth-bust
format: smooth-explainer
style_pack: terminal
value_types: "TEACHES,EQUIPS"
created: 2026-09-16
updated: "2026-09-16T17:26:50Z"
publish_slot: "2026-09-16T18:00:00-05:00"
seo_score: 100
feedback: ""
blocked_reason: ""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: d6cb3bd9-c15d-4646-afea-bc5caa82a39a
---
# Replicating a paper with Qwen-2.5 at home

## Artifacts
- Radar: [[stages/01-radar/output/2026-09-16-radar]]
- Ideas: [[stages/02-ideas/output/2026-09-16-ideas]]
- Research: [[stages/03-research/output/2026-09-16-replicating-a-paper-with-qwen-brief|Brief]]
- Script: [[stages/04-script/output/2026-09-16-replicating-a-paper-with-qwen-script|Script]] ([[stages/04-script/output/2026-09-16-replicating-a-paper-with-qwen-storyboard|storyboard]], [[stages/04-script/output/2026-09-16-replicating-a-paper-with-qwen-drafts|drafts]])
- Package: [[stages/05-package/output/2026-09-16-replicating-a-paper-with-qwen-package|Package]]
- Voice: [[stages/06-voice/output/2026-09-16-replicating-a-paper-with-qwen-voice]]
- Render: [[stages/07-render/output/2026-09-16-replicating-a-paper-with-qwen-render]]
- Publish: [[stages/08-publish/output/2026-09-16-replicating-a-paper-with-qwen-publish]]

## Decisions

- 2026-09-16: Picked as rank 1 (opportunity 99.5, autocomplete depth 72 on "qwen 2.5"); strongest demand of the day, lane rotates off yesterday's explainer + news-react. Chosen unattended per the stage 02 checkpoint; see stages/02-ideas/output/2026-09-16-ideas.md.
- 2026-09-16 stage 03 checkpoint (angle confirm, unattended): angle kept as picked -- a published result replicated on open weights a home rig can serve; the workflow is the video. No redirect. Source lead hn-4dfe90f8a8 resolved to the harshatheg HF replication of TypeSafe Jev with stock Qwen-2.5-1.5B.
- 2026-09-16 stage 04 checkpoints (unattended): structures how-to-three-moves vs myth-bust (rotation barred number-first and worked-example); hooks tonight vs named-contradiction (rotation barred number-shock and situation); value types TEACHES+EQUIPS locked. Judge: myth-bust 24, how-to 12, no grafts. Gate fixes: 1,900 ms kept spoken but off screen (number cap; the "two hundred seventy milliseconds" ghost also matches Jev's 70-to-500 ms row), s02/s06 trimmed, s11 tail cut to two sentences, lexicon say-entries added (JSON "jason", LM, LM Studio), writer's storyboard slug corrected to the hub slug before ledger record. Validator 0 blockers 0 advisories; eval 9/9; variety ok; style pack terminal (silicon barred).
- 2026-09-16 stage 05 checkpoint (unattended): searchable title chosen over two intriguing variants -- the pick was scored on search demand (autocomplete depth 72 on "qwen 2.5"), so the target surface is search per titles-descriptions.md. Rubric 100/100 (title row and description row full marks; channel line used as the related line, no published video is close to this topic). check_outputs 0 failures. contains_synthetic_media false: typographic terminal scenes plus the creator's own cloned voice, both exempt under compliance.md.

## Build journal
- 2026-09-16T11:59:57Z 03-research ok: 11 sources, 10 claims, validator exit 0
- 2026-09-16T12:53:00Z 04-script ok: myth-bust won 24-12 over how-to-three-moves; validator 0/0, eval 9/9, variety ok
- 2026-09-16T12:57:38Z 05-package ok: searchable title picked (search surface, autocomplete 72), rubric 100, check_outputs 0 failures
- 2026-09-16T12:59:32Z build start on gn100-83c4
- 2026-09-16T13:04:31Z 06-voice ok 296s
- 2026-09-16T13:36:45Z 07-render fail 1931s (07-render: scene s9 did not pass HyperFrames inspect after 5 rounds: t=2.76-10.39s (56 samples) text_occluded span.green inside #strike ">" — Text is hidden ben)
- 2026-09-16T13:45:20Z 07-render ok 126.77s: 11 scenes via scene_worker.py, lint True, safe-zone True, loop True, card message_id 71
- 2026-09-16T13:45:20Z 07-render ok 515s
- 2026-09-16T13:45:24Z build done, status review
- 2026-09-16T17:08:43Z telegram approve (approved_at 2026-09-16T17:08:43Z)
- 2026-09-16T17:08:46Z 08-publish fail 0s (publish exited 1: [publish] not an ISO-8601 timestamp: 11:00 CT)
- 2026-09-16T17:08:46Z 08-publish fail 0s (publish exited 1: [publish] not an ISO-8601 timestamp: 11:00 CT)
- 2026-09-16T17:08:46Z blocked at 08-publish
- 2026-09-16T17:08:56Z telegram retry
- 2026-09-16T17:14:46Z build start on gn100-83c4
- 2026-09-16T17:15:05Z 06-voice ok 16s
- 2026-09-16T17:16:51Z 07-render ok 126.77s: 11 scenes via scene_worker.py, lint True, safe-zone True, loop True, card message_id 75
- 2026-09-16T17:16:51Z 07-render ok 103s
- 2026-09-16T17:16:53Z build done, status review
- 2026-09-16T17:16:57Z telegram approve (approved_at 2026-09-16T17:16:57Z)
- 2026-09-16T17:20:46Z 08-publish fail 0s (publish exited 1: [publish] not an ISO-8601 timestamp: 11:00 CT)
- 2026-09-16T17:20:46Z 08-publish fail 0s (publish exited 1: [publish] not an ISO-8601 timestamp: 11:00 CT)
- 2026-09-16T17:20:46Z blocked at 08-publish
- 2026-09-16T17:23:06Z operator unblocked after the slot-hint fix (publish.py tolerant, hint blanked); the 2026-09-16T17:16:57Z approval stands, status approved
- 2026-09-16T17:26:51Z 08-publish ok 4s
