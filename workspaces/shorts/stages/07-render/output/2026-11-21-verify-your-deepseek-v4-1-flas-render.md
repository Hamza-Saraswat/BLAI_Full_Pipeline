---
slug: 2026-11-21-verify-your-deepseek-v4-1-flas
duration_s: 40.90
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.757612
---

# Render: 2026-11-21-verify-your-deepseek-v4-1-flas

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-21T13:34:08Z.

## Gates
- lint_video --final: pass (duration 40.90 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.757612)
- Length: 40.90 s; narration 39.76 s
- Scenes: 5/5 storyboard scenes rendered (s01, s02, s03, s04, s05)
- Captions: 108 words; sfx cues type, tick, pop, type, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 6.12 | 6.13 | 3 | glm-5.3 |  |
| s02 | 8.92 | 8.93 | 2 | glm-5.3-flash |  |
| s03 | 11.76 | 11.77 | 4 | glm-5.3 |  |
| s04 | 7.14 | 7.17 | 3 | glm-5.3 |  |
| s05 | 6.74 | 6.77 | 1 | glm-5.3-flash |  |

## Assembly
- video total 40.77s vs narration 39.76s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-21-verify-your-deepseek-v4-1-flas/render/2026-11-21-verify-your-deepseek-v4-1-flas-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 377
