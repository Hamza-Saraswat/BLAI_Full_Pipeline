---
slug: 2026-10-31-fake-qwen2-checkpoints-the-tru
duration_s: 49.00
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.805113
---

# Render: 2026-10-31-fake-qwen2-checkpoints-the-tru

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-31T12:33:11Z.

## Gates
- lint_video --final: pass (duration 49.00 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.805113)
- Length: 49.00 s; narration 47.96 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 126 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.56 | 5.57 | 1 | glm-5.3-flash |  |
| s02 | 10.71 | 10.73 | 3 | glm-5.3 |  |
| s03 | 6.00 | 6.00 | 1 | glm-5.3-flash |  |
| s04 | 6.90 | 6.90 | 5 | glm-5.3 |  |
| s05 | 12.83 | 12.83 | 2 | glm-5.3-flash |  |
| s06 | 6.96 | 6.97 | 2 | glm-5.3-flash |  |

## Assembly
- video total 49.00s vs narration 47.96s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-31-fake-qwen2-checkpoints-the-tru/render/2026-10-31-fake-qwen2-checkpoints-the-tru-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 299
