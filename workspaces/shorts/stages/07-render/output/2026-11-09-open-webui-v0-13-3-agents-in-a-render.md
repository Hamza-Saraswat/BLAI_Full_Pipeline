---
slug: 2026-11-09-open-webui-v0-13-3-agents-in-a
duration_s: 115.97
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.765803
---

# Render: 2026-11-09-open-webui-v0-13-3-agents-in-a

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-09T13:54:56Z.

## Gates
- lint_video --final: pass (duration 115.97 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.765803)
- Length: 115.97 s; narration 115.72 s
- Scenes: 8/8 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08)
- Captions: 387 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 12.80 | 12.80 | 2 | glm-5.3-flash |  |
| s02 | 12.46 | 12.47 | 2 | glm-5.3-flash |  |
| s03 | 11.74 | 11.77 | 3 | glm-5.3 |  |
| s04 | 13.24 | 13.13 | 4 | glm-5.3 |  |
| s05 | 19.76 | 19.77 | 3 | glm-5.3 |  |
| s06 | 19.27 | 19.30 | 2 | glm-5.3-flash |  |
| s07 | 18.73 | 18.73 | 3 | glm-5.3 |  |
| s08 | 8.00 | 8.00 | 2 | glm-5.3-flash |  |

## Assembly
- no assembler warnings
- props: /home/buildlocalai/blai/builds/2026-11-09-open-webui-v0-13-3-agents-in-a/render/2026-11-09-open-webui-v0-13-3-agents-in-a-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 334
