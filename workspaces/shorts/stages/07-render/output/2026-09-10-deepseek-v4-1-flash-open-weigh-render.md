---
slug: 2026-09-10-deepseek-v4-1-flash-open-weigh
duration_s: 37.00
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.877134
---

# Render: 2026-09-10-deepseek-v4-1-flash-open-weigh

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-10T13:49:30Z.

## Gates
- lint_video --final: pass (duration 37.00 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.877134)
- Length: 37.00 s; narration 36.20 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 109 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 4.72 | 4.73 | 2 | glm-5.3-flash |  |
| s02 | 4.97 | 5.00 | 2 | glm-5.3-flash |  |
| s03 | 7.34 | 7.33 | 2 | glm-5.3-flash |  |
| s04 | 8.74 | 8.77 | 4 | glm-5.3 |  |
| s05 | 5.99 | 6.00 | 2 | glm-5.3-flash |  |
| s06 | 5.16 | 5.17 | 1 | glm-5.3-flash |  |

## Assembly
- video total 37.00s vs narration 36.20s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-10-deepseek-v4-1-flash-open-weigh/render/2026-09-10-deepseek-v4-1-flash-open-weigh-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 48
