---
slug: 2026-10-15-deepseek-outage-your-gguf-has
duration_s: 95.10
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.78475
---

# Render: 2026-10-15-deepseek-outage-your-gguf-has

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-15T13:05:11Z.

## Gates
- lint_video --final: pass (duration 95.10 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.78475)
- Length: 95.10 s; narration 94.60 s
- Scenes: 10/10 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10)
- Captions: 296 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 7.25 | 7.27 | 2 | glm-5.3-flash |  |
| s02 | 9.87 | 9.90 | 4 | glm-5.3 |  |
| s03 | 7.99 | 8.00 | 3 | glm-5.3 |  |
| s04 | 4.89 | 4.90 | 2 | glm-5.3-flash |  |
| s05 | 9.80 | 9.80 | 2 | glm-5.3-flash |  |
| s06 | 17.26 | 17.27 | 4 | glm-5.3 |  |
| s07 | 8.94 | 8.93 | 4 | glm-5.3 |  |
| s08 | 14.07 | 14.10 | 2 | glm-5.3-flash | motion inside the first 0.5s (rule 10 stillness) |
| s09 | 9.93 | 9.93 | 2 | glm-5.3-flash |  |
| s10 | 5.00 | 5.00 | 3 | glm-5.3 |  |

## Assembly
- no assembler warnings
- props: /home/buildlocalai/blai/builds/2026-10-15-deepseek-outage-your-gguf-has/render/2026-10-15-deepseek-outage-your-gguf-has-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 225
