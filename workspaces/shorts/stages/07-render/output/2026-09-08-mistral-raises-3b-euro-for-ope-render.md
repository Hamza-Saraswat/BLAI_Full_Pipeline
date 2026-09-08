---
slug: 2026-09-08-mistral-raises-3b-euro-for-ope
duration_s: 39.50
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.74771
---

# Render: 2026-09-08-mistral-raises-3b-euro-for-ope

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-08T14:44:52Z.

## Gates
- lint_video --final: pass (duration 39.50 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.74771)
- Length: 39.50 s; narration 38.80 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 116 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.08 | 5.10 | 3 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |
| s02 | 8.12 | 8.13 | 4 | glm-5.3 |  |
| s03 | 4.20 | 4.20 | 2 | glm-5.3-flash |  |
| s04 | 8.16 | 8.17 | 5 | glm-5.3 |  |
| s05 | 8.22 | 8.23 | 2 | glm-5.3-flash |  |
| s06 | 5.66 | 5.67 | 4 | glm-5.3 |  |

## Assembly
- video total 39.50s vs narration 38.80s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-08-mistral-raises-3b-euro-for-ope/render/2026-09-08-mistral-raises-3b-euro-for-ope-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 38
