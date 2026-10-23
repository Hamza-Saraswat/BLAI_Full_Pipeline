---
slug: 2026-10-21-same-mcp-server-different-answ
workspace: shorts
title: "Claude Code MCP: two agents, two answers"
status: published
pillar: explainer
structure: contrarian-take
format: smooth-explainer
style_pack: signal
value_types: "TEACHES,REFRAMES"
created: 2026-10-21
updated: "2026-10-23T16:05:10Z"
publish_slot: "2026-10-23T11:00:00-05:00"
seo_score: 100
feedback: ""
blocked_reason: ""
build_host: gn100-83c4
preview_url: ""
youtube_url: "https://www.youtube.com/watch?v=d9MWlSqkudw"
blotato_post_id: 031e9bc4-13da-48ad-b0b0-539caecad7b8
---
# Same MCP server, different answers: what the Harness measured

## Decisions

- Picked (ideas 2026-10-21): rank 1 of 10, opportunity 100.0, autocomplete depth 115 on "claude code mcp"; explainer lane keeps rotation vs yesterday's how-to + comparison.
- Format smooth-explainer: the viewer follows a state changing three or more times (same tool call, different harness behaviors), per selection-rules.md fit table.

## Artifacts
- Radar: [[stages/01-radar/output/2026-10-21-radar]]
- Ideas: [[stages/02-ideas/output/2026-10-21-ideas]]
- Research: [[stages/03-research/output/2026-10-21-same-mcp-server-different-answ-brief]]
- Script: [[stages/04-script/output/2026-10-21-same-mcp-server-different-answ-script]]
- Package: [[stages/05-package/output/2026-10-21-same-mcp-server-different-answ-package]]
- Voice: [[stages/06-voice/output/2026-10-21-same-mcp-server-different-answ-narration]]
- Render: [[stages/07-render/output/2026-10-21-same-mcp-server-different-answ-render]]
- Publish: [[stages/08-publish/output/2026-10-21-same-mcp-server-different-answ-publish]]

## Decisions

- Checkpoint (angle, unattended): confirmed slug 2026-10-21-same-mcp-server-different-answ on the ideas row (rank 1 of 10, opportunity 100.0); angle held: measured per-harness differences, not the docs, are the spec. No picks.md swap exists for today.
- Research (unattended): 8 sources, all fetched this run; 10 claims, 6 key numbers; FireCrawl 402 so direct fetches; validate_research.py exit 0. Thesis: one MCP server, different harnesses, different answers, so the measured compatibility table is the working spec.
- Checkpoint (structures, unattended): contrarian-take (A) vs worked-example (B); both clear the rotation rule (last two were myth-bust, news-react-so-what); value types TEACHES+REFRAMES confirmed; promise: after this you check what your own harness shows the model before you blame the server.
- Checkpoint (hooks, unattended): 10 written and scored; kept situation (A) and case (B), two different patterns per finding 12; frame-1 texts "ONE SERVER. TWO AGENTS. TWO ANSWERS." and "EVERY AGENT. ONE MCP PROBE."
- Writers: two blind kimi-k3 calls (llm_call.py, temp 1 recipe, 32000 max tokens, 900 timeout); A 724 s, B 785 s; both boards validated clean (validator 0/0) and eval gates all pass; explicit hook_pattern set per variety.md because the classifier misread both hooks as number-shock.
- Judge: kimi-k3 blind verdict B wins 20/24 vs 16/24; graft from A (marker mechanism sentence) applied; draft B re-gated clean after the graft. MCP added to tts_lexicon keep list, self-test 168/168. Ledger recorded (entry 46); style pack signal recorded.
- Checkpoint (package, unattended): searchable title "Claude Code MCP: two agents, two answers" picked over two intriguing variants; keyword "claude code mcp" is the day's deepest autocomplete (115), so the search-heavy surface gets the searchable type. Rubric 100/100; check_outputs 0 failures; contains_synthetic_media false (typographic scenes plus the creator's cloned voice, both exempt); slot hint empty (default 11:00/18:00 CT rotation).

## Build journal
- 2026-10-21T12:38:12Z build start on gn100-83c4
- 2026-10-21T12:40:35Z 06-voice ok 140s
- 2026-10-21T13:04:04Z 07-render ok 106.63s: 11 scenes via scene_worker.py, lint True, safe-zone True, loop True, card message_id 255
- 2026-10-21T13:04:04Z 07-render ok 1406s
- 2026-10-21T13:04:06Z build done, status review
- 2026-10-22T13:35:55Z 2026-10-22T13:35:55Z expired: not from today's picks (2026-10-22); the factory carries no backlog
- 2026-10-23T10:56:48Z telegram approve (approved_at 2026-10-23T10:56:48Z)
- 2026-10-23T10:57:12Z 08-publish ok 2s
- 2026-10-23T16:05:10Z published https://www.youtube.com/watch?v=d9MWlSqkudw
