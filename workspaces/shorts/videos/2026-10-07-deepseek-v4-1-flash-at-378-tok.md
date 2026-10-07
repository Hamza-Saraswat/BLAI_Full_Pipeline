---
slug: 2026-10-07-deepseek-v4-1-flash-at-378-tok
workspace: shorts
title: "DeepSeek v4.1 Flash at 378 tok/s: the cache-hit catch"
status: blocked
pillar: myth-bust
structure: contrarian-take
format: smooth-explainer
style_pack: blueprint
value_types: "REFRAMES,PROVES"
created: 2026-10-07
updated: "2026-10-07T12:54:06Z"
publish_slot: ""
seo_score: 90
feedback: ""
blocked_reason: "\"07-render: 07-render: assemble.py exited 1: pseek-v4-1-flash-at-378-tok/render/qa"
assemble: "$ npx remotion still Assembly /home/buildlocalai/blai/builds/2026-10-07-deepseek-v4-1-flash-at-378-tok/render/qa/safe-z\""
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# DeepSeek v4.1 Flash at 378 tok/s: the cache-hit catch

## Artifacts
- Radar: [[stages/01-radar/output/2026-10-07-radar]]
- Ideas: [[stages/02-ideas/output/2026-10-07-ideas]]
- Research: [[stages/03-research/output/2026-10-07-deepseek-v4-1-flash-at-378-tok-brief|Brief]]
- Script: [[stages/04-script/output/2026-10-07-deepseek-v4-1-flash-at-378-tok-script|Script]]
- Package: [[stages/05-package/output/2026-10-07-deepseek-v4-1-flash-at-378-tok-package|Package]]
- Voice: [[stages/06-voice/output/2026-10-07-deepseek-v4-1-flash-at-378-tok-narration|Narration (normalized)]]
- Render: (filled by stage 07)
- Publish: (filled by stage 08)

## Decisions
- 03-research (unattended checkpoint): angle confirmed unchanged, 378 tok/s as a 99.7% cache-hit demo whose cold-path cost the video exposes; 12 sources fetched (5 primary/docs, 4 benchmark, 3 community), validator exit 0.
- Picked as rank 1 (opportunity 90.7, myth-bust): the 378 tok/s runinfra number is a 99.7% cache-hit demo; the video dismantles the headline and shows what cold-prompt tok/s looks like.
- Lane myth-bust + band smooth-explainer: a belief to dismantle with state changes; differs from yesterday's lanes.

## Build journal
- 2026-10-07T11:52:04Z 03-research complete: brief md+json written, validate_research.py exit 0
- 2026-10-07T12:30:10Z build start on gn100-83c4
- 2026-10-07T12:31:51Z 06-voice ok 99s
- 2026-10-07T12:44:59Z 07-render fail 785s (07-render: scene s05 did not pass safe_zone_check after 5 rounds)
- 2026-10-07T12:54:06Z 07-render fail 546s (07-render: assemble.py exited 1: pseek-v4-1-flash-at-378-tok/render/qa
assemble: $ node /home/buildlocalai/blai/repo/skills/render-shorts/remotion/scripts/loop_)
- 2026-10-07T12:54:06Z blocked at 07-render

## ## Decisions
- 2026-10-07T12:21:59Z - 04-script (unattended): contrarian-take beat worked-example 21-18 (kimi-k3 judge, no grafts); hooks from two patterns (named-contradiction vs situation); gates on winner: validator 0 blockers, eval exit 0, variety ok (entry 32); pack blueprint; 99.7 kept off the tongue, three numbers spent.
- 2026-10-07T12:24:44Z - 05-package (unattended checkpoint): searchable title kept (52 chars, keyword in first 20; half credit on the length row accepted because product search traffic dominates and truncation keeps the keyword); seo_score 90; description leads with the 378 catch and names the 2026-09-17 DeepSeek receipt video; contains_synthetic_media false (typographic scenes plus creator voice clone); check_outputs exit 0 after linking Package and the normalized narration artifact.

## ## Build journal
- 2026-10-07T12:21:59Z - 2026-10-07 04-script complete: draft A contrarian-take wins; storyboard + script + drafts saved; narration normalized for voice.
- 2026-10-07T12:24:44Z - 2026-10-07 05-package complete: package note + manifest written, seo 90, hub ready-to-build. Stages 06-08 belong to build/build.py.
