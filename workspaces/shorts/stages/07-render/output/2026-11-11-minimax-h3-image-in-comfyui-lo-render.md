---
slug: 2026-11-11-minimax-h3-image-in-comfyui-lo
duration_s: 110.50
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.848994
---

# Render: 2026-11-11-minimax-h3-image-in-comfyui-lo

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-11T14:08:53Z.

## Gates
- lint_video --final: pass (duration 110.50 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.848994)
- Length: 110.50 s; narration 109.64 s
- Scenes: 11/11 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11)
- Captions: 324 words; sfx cues pop, whoosh, whoosh, tick, tick, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 8.67 | 8.70 | 1 | glm-5.3-flash |  |
| s02 | 8.55 | 8.57 | 1 | glm-5.3-flash |  |
| s03 | 8.17 | 8.20 | 1 | glm-5.3-flash |  |
| s04 | 12.69 | 12.70 | 5 | glm-5.3 |  |
| s05 | 10.67 | 10.70 | 3 | glm-5.3 |  |
| s06 | 8.38 | 8.40 | 2 | glm-5.3-flash |  |
| s07 | 13.46 | 13.47 | 2 | glm-5.3-flash |  |
| s08 | 11.57 | 11.60 | 3 | glm-5.3 |  |
| s09 | 13.37 | 13.40 | 5 | glm-5.3 |  |
| s10 | 4.90 | 4.90 | 2 | glm-5.3-flash |  |
| s11 | 9.85 | 9.87 | 3 | glm-5.3 |  |

## Assembly
- video total 110.50s vs narration 109.64s (segments win; check scene durations)
- scene s11: no spoken number found, number-reveal cue at scene midpoint
- props: /home/buildlocalai/blai/builds/2026-11-11-minimax-h3-image-in-comfyui-lo/render/2026-11-11-minimax-h3-image-in-comfyui-lo-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 345
