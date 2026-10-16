---
slug: 2026-10-16-mlx-distributed-inference-two
duration_s: 88.80
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.898828
---

# Render: 2026-10-16-mlx-distributed-inference-two

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-16T13:18:43Z.

## Gates
- lint_video --final: pass (duration 88.80 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.898828)
- Length: 88.80 s; narration 87.72 s
- Scenes: 8/8 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08)
- Captions: 263 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 9.44 | 9.47 | 2 | glm-5.3-flash |  |
| s02 | 11.22 | 11.23 | 4 | glm-5.3 |  |
| s03 | 14.46 | 14.47 | 3 | glm-5.3 |  |
| s04 | 13.40 | 13.40 | 2 | glm-5.3-flash |  |
| s05 | 18.31 | 18.33 | 4 | glm-5.3 |  |
| s06 | 8.33 | 8.33 | 4 | glm-5.3 |  |
| s07 | 9.18 | 9.17 | 3 | glm-5.3 |  |
| s08 | 4.38 | 4.40 | 2 | glm-5.3-flash |  |

## Assembly
- video total 88.80s vs narration 87.72s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-16-mlx-distributed-inference-two/render/2026-10-16-mlx-distributed-inference-two-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 231
