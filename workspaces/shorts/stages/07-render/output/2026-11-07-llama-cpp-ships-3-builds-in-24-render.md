---
slug: 2026-11-07-llama-cpp-ships-3-builds-in-24
duration_s: 40.07
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.884582
---

# Render: 2026-11-07-llama-cpp-ships-3-builds-in-24

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-07T13:34:30Z.

## Gates
- lint_video --final: pass (duration 40.07 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.884582)
- Length: 40.07 s; narration 39.00 s
- Scenes: 5/5 storyboard scenes rendered (s01, s02, s03, s04, s05)
- Captions: 113 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 6.12 | 6.13 | 2 | glm-5.3-flash |  |
| s02 | 9.55 | 9.57 | 4 | glm-5.3 |  |
| s03 | 7.16 | 7.17 | 3 | glm-5.3 |  |
| s04 | 8.73 | 8.73 | 2 | glm-5.3-flash | motion inside the first 0.5s (rule 10 stillness) |
| s05 | 8.44 | 8.47 | 3 | glm-5.3 |  |

## Assembly
- video total 40.07s vs narration 39.00s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-07-llama-cpp-ships-3-builds-in-24/render/2026-11-07-llama-cpp-ships-3-builds-in-24-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 327
