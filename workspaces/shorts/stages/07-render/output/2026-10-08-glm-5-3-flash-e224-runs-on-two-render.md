---
slug: 2026-10-08-glm-5-3-flash-e224-runs-on-two
duration_s: 38.90
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.938173
---

# Render: 2026-10-08-glm-5-3-flash-e224-runs-on-two

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-08T12:40:40Z.

## Gates
- lint_video --final: pass (duration 38.90 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.938173)
- Length: 38.90 s; narration 37.80 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 111 words; sfx cues pop, tick, tick, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 6.56 | 6.57 | 3 | glm-5.3 |  |
| s02 | 7.92 | 7.93 | 1 | glm-5.3-flash |  |
| s03 | 5.87 | 5.90 | 2 | glm-5.3-flash |  |
| s04 | 8.77 | 8.80 | 3 | glm-5.3 |  |
| s05 | 4.79 | 4.80 | 4 | glm-5.3 |  |
| s06 | 4.89 | 4.90 | 2 | glm-5.3-flash |  |

## Assembly
- video total 38.90s vs narration 37.80s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-08-glm-5-3-flash-e224-runs-on-two/render/2026-10-08-glm-5-3-flash-e224-runs-on-two-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 188
