---
slug: 2026-10-11-gmktec-evo-x3-the-128gb-strix
duration_s: 42.97
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.920883
---

# Render: 2026-10-11-gmktec-evo-x3-the-128gb-strix

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-11T12:38:34Z.

## Gates
- lint_video --final: pass (duration 42.97 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.920883)
- Length: 42.97 s; narration 42.00 s
- Scenes: 7/7 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07)
- Captions: 118 words; sfx cues whoosh, pop, pop, tick, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 3.76 | 3.77 | 2 | glm-5.3-flash |  |
| s02 | 5.65 | 5.67 | 2 | glm-5.3-flash |  |
| s03 | 8.30 | 8.33 | 3 | glm-5.3 |  |
| s04 | 9.07 | 9.07 | 2 | glm-5.3-flash |  |
| s05 | 7.10 | 7.13 | 2 | glm-5.3-flash |  |
| s06 | 3.12 | 3.13 | 1 | glm-5.3-flash |  |
| s07 | 5.84 | 5.87 | 2 | glm-5.3-flash |  |

## Assembly
- video total 42.97s vs narration 42.00s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-11-gmktec-evo-x3-the-128gb-strix/render/2026-10-11-gmktec-evo-x3-the-128gb-strix-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 203
