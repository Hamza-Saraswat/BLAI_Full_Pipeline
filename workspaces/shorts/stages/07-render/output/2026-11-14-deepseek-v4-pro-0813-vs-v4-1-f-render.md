---
slug: 2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f
duration_s: 100.43
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.818478
---

# Render: 2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-14T14:10:09Z.

## Gates
- lint_video --final: pass (duration 100.43 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.818478)
- Length: 100.43 s; narration 99.44 s
- Scenes: 10/10 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10)
- Captions: 317 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 3.76 | 3.77 | 2 | glm-5.3-flash |  |
| s02 | 10.64 | 10.67 | 4 | glm-5.3 |  |
| s03 | 12.18 | 12.20 | 2 | glm-5.3-flash |  |
| s04 | 10.78 | 10.80 | 3 | glm-5.3 |  |
| s05 | 11.96 | 11.97 | 3 | glm-5.3 |  |
| s06 | 12.52 | 12.53 | 5 | glm-5.3 |  |
| s07 | 9.78 | 9.80 | 4 | glm-5.3 |  |
| s08 | 10.62 | 10.63 | 3 | glm-5.3 |  |
| s09 | 12.72 | 12.73 | 2 | glm-5.3-flash |  |
| s10 | 5.32 | 5.33 | 3 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |

## Assembly
- video total 100.43s vs narration 99.44s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f/render/2026-11-14-deepseek-v4-pro-0813-vs-v4-1-f-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 354
