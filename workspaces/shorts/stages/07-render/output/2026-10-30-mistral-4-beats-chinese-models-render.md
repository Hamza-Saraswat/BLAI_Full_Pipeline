---
slug: 2026-10-30-mistral-4-beats-chinese-models
duration_s: 42.13
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.749494
---

# Render: 2026-10-30-mistral-4-beats-chinese-models

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-30T12:55:58Z.

## Gates
- lint_video --final: pass (duration 42.13 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.749494)
- Length: 42.13 s; narration 41.56 s
- Scenes: 7/7 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07)
- Captions: 122 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 3.28 | 3.30 | 2 | glm-5.3-flash |  |
| s02 | 6.77 | 6.80 | 2 | glm-5.3-flash | motion inside the first 0.5s (rule 10 stillness) |
| s03 | 6.18 | 6.20 | 3 | glm-5.3 |  |
| s04 | 8.79 | 8.80 | 2 | glm-5.3-flash |  |
| s05 | 5.98 | 6.00 | 2 | glm-5.3-flash |  |
| s06 | 6.41 | 6.43 | 3 | glm-5.3 |  |
| s07 | 4.59 | 4.60 | 2 | glm-5.3-flash |  |

## Assembly
- video total 42.13s vs narration 41.56s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-30-mistral-4-beats-chinese-models/render/2026-10-30-mistral-4-beats-chinese-models-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 296
