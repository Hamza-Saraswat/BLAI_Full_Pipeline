---
slug: 2026-10-28-qwen3-coder-wrote-19-more-hack
duration_s: 97.83
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.775255
---

# Render: 2026-10-28-qwen3-coder-wrote-19-more-hack

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-28T13:20:24Z.

## Gates
- lint_video --final: pass (duration 97.83 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.775255)
- Length: 97.83 s; narration 96.72 s
- Scenes: 9/9 storyboard scenes rendered (s1, s2, s3, s4, s5, s6, s7, s8, s9)
- Captions: 303 words; sfx cues tick, ding, ding, pop, ding, type; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 6.64 | 6.67 | 1 | glm-5.3-flash |  |
| s2 | 10.80 | 10.80 | 3 | glm-5.3 |  |
| s3 | 10.89 | 10.90 | 3 | glm-5.3 |  |
| s4 | 12.03 | 12.03 | 1 | glm-5.3-flash |  |
| s5 | 11.33 | 11.33 | 2 | glm-5.3-flash |  |
| s6 | 6.67 | 6.70 | 3 | glm-5.3 |  |
| s7 | 14.21 | 14.20 | 5 | glm-5.3 |  |
| s8 | 12.97 | 13.00 | 4 | glm-5.3 |  |
| s9 | 12.18 | 12.20 | 3 | glm-5.3 |  |

## Assembly
- video total 97.83s vs narration 96.72s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-28-qwen3-coder-wrote-19-more-hack/render/2026-10-28-qwen3-coder-wrote-19-more-hack-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 286
