---
slug: 2026-11-26-claude-code-with-a-free-local
workspace: shorts
title: Run Claude Code on Ollama for free
status: blocked
pillar: how-to
structure: news-react-so-what
format: classic
style_pack: terminal
value_types: "TEACHES,EQUIPS"
created: 2026-11-26
updated: "2026-11-26T13:57:01Z"
publish_slot: ""
seo_score: 96
feedback: ""
blocked_reason: "06-voice: voice QA failed: WER 0.110, 12 mismatch(es): expected 'clawed' heard 'claude'; expected 'ohlah' heard 'olah'; expected 'clawed' heard 'claude'"
build_host: gn100-83c4
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---
# Claude Code with a free local LLM: the Ollama setup

## Artifacts
- Radar: [[stages/01-radar/output/2026-11-26-radar]]
- Ideas: [[stages/02-ideas/output/2026-11-26-ideas]]
- Research: [[stages/03-research/output/2026-11-26-claude-code-with-a-free-local-brief]]
- Script: [[stages/04-script/output/2026-11-26-claude-code-with-a-free-local-script]]
- Package: [[stages/05-package/output/2026-11-26-claude-code-with-a-free-local-package]]
- Voice: [[stages/06-voice/output/2026-11-26-claude-code-with-a-free-local-voice]]
- Render: (filled by stage 07)
- Publish: (filled by stage 08)

## Decisions

- 2026-11-26 stage 04 checkpoint 1 (unattended): draft A structure worked-example, draft B news-react-so-what; both clear the rotation rule (last two ledger entries: contrarian-take, how-to-three-moves). how-to-three-moves is the brief's natural fit but is barred by yesterday's entry, so worked-example carries the process instead. Locked value types TEACHES (the BASE_URL redirect mechanism and the context trap) and EQUIPS (three lines plus a model pick the viewer runs tonight). Promise: after thirty-five seconds you can point Claude Code at a free local Ollama model and run your first prompt tonight.
- 2026-11-26 stage 04 checkpoint 2 (unattended): 10 hooks scored, picks are "Twenty dollars a month, or three lines tonight." (Price, draft A) and "Claude Code runs without Anthropic's cloud." (named contradiction, draft B); different patterns, both carry a product or number, both true per brief claims 1, 3 and 7.
- 2026-11-26 stage 03 checkpoint (unattended): angle confirmed as the ideas note states it -- "Point Claude Code at a local Ollama model tonight and stop paying per prompt"; slug 2026-11-26-claude-code-with-a-free-local, lane how-to, format classic. No redirect; no swap requested (no picks.md).
- FireCrawl is out of credits this run (402), so research runs on web_search + web_extract, the documented fallback; source count stays at standard depth (8-12).
- 2026-11-26 stage 04 close (unattended): writers ran as two llm_call.py kimi-k3 calls in private scratch dirs (writer A's first two calls died at the 32k completion cap; a third call with an explicit output-cap line in the system file landed). Validator 0 blockers 0 advisories on both drafts; eval gates pass on both (entity_spend soft advisory only); normalize A scenes_changed 2, B 4; sameness clean (5 comparisons, 0 violations). Draft B (news-react-so-what) won 22-17 over draft A (worked-example); one graft from A (the Ollama's-engineering catch line). style_rotation picked terminal (3 keyword hits, previous signal); ledger entry 82 recorded. Hook: "Claude Code runs without Anthropic's cloud." (named contradiction, candidate 2 of 10).
- 2026-11-26 stage 05 checkpoint (unattended): title "Run Claude Code on Ollama for free" picked (searchable, "Claude Code" and "Ollama" in the first 34 characters, search-heavy topic per the ideas keyword notes); alternatives were the intriguing 3-line and 19GB variants. Description leads with the keyword-plus-promise line, names the closest related video (Claude Code MCP, 2026-10-21), carries the context-trap promise; rubric scored 100 then rescored to 96 (title row half credit: the promise is conditional on hardware the viewer already owns). check_outputs 0 failures; no duplicate title against the 38 published notes; hub set to ready-to-build.
## Build journal
- 2026-11-26T12:51:44Z 03-research ok: 16 sources, 10 claims, validator exit 0
- 2026-11-26T13:45:53Z 04-script ok: draft B wins 22-17, validator 0 blockers, eval gates pass, sameness clean
- 2026-11-26T13:48:27Z 05-package ok: title searchable, seo 96, manifest written
- 2026-11-26T13:51:11Z build start on gn100-83c4
- 2026-11-26T13:54:39Z 06-voice fail 205s (voice QA failed: WER 0.136, 14 mismatch(es): expected "anthropic's" heard 'anthropics'; expected 'ollama' heard 'olahma'; expected 'api' heard 'of pi')
- 2026-11-26T13:57:01Z 06-voice fail 142s (voice QA failed: WER 0.110, 12 mismatch(es): expected 'clawed' heard 'claude'; expected 'ohlah' heard 'olah'; expected 'clawed' heard 'claude')
- 2026-11-26T13:57:01Z blocked at 06-voice
