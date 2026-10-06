---
slug: 2026-10-06-amd-quark-on-strix-halo-offici
duration_s: 124.07
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.893245
---

# Render: 2026-10-06-amd-quark-on-strix-halo-offici

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-06T13:18:25Z.

## Gates
- lint_video --final: pass (duration 124.07 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.893245)
- Length: 124.07 s; narration 123.08 s
- Scenes: 11/11 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11)
- Captions: 359 words; sfx cues pop, ding, type; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.68 | 5.70 | 1 | glm-5.3-flash |  |
| s02 | 15.27 | 15.30 | 1 | glm-5.3-flash |  |
| s03 | 13.24 | 13.23 | 3 | glm-5.3 |  |
| s04 | 10.78 | 10.80 | 2 | glm-5.3-flash |  |
| s05 | 14.44 | 14.47 | 4 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |
| s06 | 15.45 | 15.47 | 3 | glm-5.3 |  |
| s07 | 15.78 | 15.80 | 2 | glm-5.3-flash |  |
| s08 | 7.66 | 7.67 | 4 | glm-5.3 |  |
| s09 | 11.38 | 11.40 | 1 | glm-5.3-flash |  |
| s10 | 7.46 | 7.47 | 4 | glm-5.3 |  |
| s11 | 6.74 | 6.77 | 1 | glm-5.3-flash |  |

## Assembly
- video total 124.07s vs narration 123.08s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-06-amd-quark-on-strix-halo-offici/render/2026-10-06-amd-quark-on-strix-halo-offici-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 178
