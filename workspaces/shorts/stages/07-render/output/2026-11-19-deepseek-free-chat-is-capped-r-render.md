---
slug: 2026-11-19-deepseek-free-chat-is-capped-r
duration_s: 42.43
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.767918
---

# Render: 2026-11-19-deepseek-free-chat-is-capped-r

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-19T13:49:12Z.

## Gates
- lint_video --final: pass (duration 42.43 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.767918)
- Length: 42.43 s; narration 41.40 s
- Scenes: 5/5 storyboard scenes rendered (s01, s02, s03, s04, s05)
- Captions: 109 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 9.12 | 9.13 | 2 | glm-5.3-flash |  |
| s02 | 3.95 | 3.97 | 2 | glm-5.3-flash |  |
| s03 | 14.87 | 14.90 | 2 | glm-5.3-flash |  |
| s04 | 9.26 | 9.27 | 2 | glm-5.3-flash |  |
| s05 | 5.16 | 5.17 | 4 | glm-5.3 |  |

## Assembly
- video total 42.43s vs narration 41.40s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-19-deepseek-free-chat-is-capped-r/render/2026-11-19-deepseek-free-chat-is-capped-r-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 371
