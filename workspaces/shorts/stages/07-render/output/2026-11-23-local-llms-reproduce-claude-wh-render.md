---
slug: 2026-11-23-local-llms-reproduce-claude-wh
duration_s: 91.20
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.733451
---

# Render: 2026-11-23-local-llms-reproduce-claude-wh

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-23T14:01:36Z.

## Gates
- lint_video --final: pass (duration 91.20 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.733451)
- Length: 91.20 s; narration 90.20 s
- Scenes: 10/10 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10)
- Captions: 302 words; sfx cues pop, ding, whoosh, tick, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.28 | 5.30 | 3 | glm-5.3 |  |
| s02 | 9.53 | 9.53 | 3 | glm-5.3 |  |
| s03 | 8.69 | 8.70 | 2 | glm-5.3-flash |  |
| s04 | 7.39 | 7.40 | 2 | glm-5.3-flash |  |
| s05 | 6.13 | 6.13 | 2 | glm-5.3-flash | motion inside the first 0.5s (rule 10 stillness) |
| s06 | 8.37 | 8.40 | 3 | glm-5.3 |  |
| s07 | 8.14 | 8.17 | 5 | glm-5.3 |  |
| s08 | 19.27 | 19.30 | 3 | glm-5.3 |  |
| s09 | 10.64 | 10.67 | 3 | glm-5.3 |  |
| s10 | 7.46 | 7.47 | 3 | glm-5.3 |  |

## Assembly
- video total 91.07s vs narration 90.20s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-23-local-llms-reproduce-claude-wh/render/2026-11-23-local-llms-reproduce-claude-wh-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 383
