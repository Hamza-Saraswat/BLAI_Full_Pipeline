---
slug: 2026-10-20-fine-tune-deepseek-v4-1-with-u
duration_s: 99.23
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.828384
---

# Render: 2026-10-20-fine-tune-deepseek-v4-1-with-u

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-20T12:49:27Z.

## Gates
- lint_video --final: pass (duration 99.23 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.828384)
- Length: 99.23 s; narration 98.36 s
- Scenes: 10/10 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10)
- Captions: 299 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 4.91 | 4.93 | 1 | glm-5.3-flash |  |
| s02 | 10.48 | 10.50 | 2 | glm-5.3-flash |  |
| s03 | 9.43 | 9.43 | 3 | glm-5.3 |  |
| s04 | 10.58 | 10.57 | 3 | glm-5.3 |  |
| s05 | 10.97 | 10.97 | 2 | glm-5.3-flash |  |
| s06 | 9.00 | 9.00 | 2 | glm-5.3-flash |  |
| s07 | 9.28 | 9.30 | 2 | glm-5.3-flash |  |
| s08 | 9.26 | 9.27 | 1 | glm-5.3-flash |  |
| s09 | 17.74 | 17.77 | 2 | glm-5.3-flash |  |
| s10 | 7.47 | 7.50 | 1 | glm-5.3-flash |  |

## Assembly
- video total 99.23s vs narration 98.36s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-20-fine-tune-deepseek-v4-1-with-u/render/2026-10-20-fine-tune-deepseek-v4-1-with-u-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 250
