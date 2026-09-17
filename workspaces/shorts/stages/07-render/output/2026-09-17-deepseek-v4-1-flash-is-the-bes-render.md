---
slug: 2026-09-17-deepseek-v4-1-flash-is-the-bes
duration_s: 103.30
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.860569
---

# Render: 2026-09-17-deepseek-v4-1-flash-is-the-bes

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-17T14:48:30Z.

## Gates
- lint_video --final: pass (duration 103.30 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.860569)
- Length: 103.30 s; narration 102.12 s
- Scenes: 12/12 storyboard scenes rendered (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12)
- Captions: 314 words; sfx cues whoosh, tick, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 7.39 | 7.40 | 1 | glm-5.3-flash |  |
| s2 | 9.40 | 9.40 | 2 | glm-5.3-flash |  |
| s3 | 6.73 | 6.73 | 3 | glm-5.3 |  |
| s4 | 6.26 | 6.27 | 1 | glm-5.3-flash |  |
| s5 | 6.73 | 6.73 | 2 | glm-5.3-flash |  |
| s6 | 8.33 | 8.33 | 2 | glm-5.3-flash |  |
| s7 | 11.99 | 12.00 | 3 | glm-5.3 |  |
| s8 | 5.82 | 5.83 | 5 | glm-5.3 |  |
| s9 | 9.75 | 9.77 | 1 | glm-5.3-flash |  |
| s10 | 9.52 | 9.53 | 3 | glm-5.3 |  |
| s11 | 11.87 | 11.90 | 2 | glm-5.3-flash |  |
| s12 | 9.33 | 9.33 | 1 | glm-5.3-flash |  |

## Assembly
- video total 103.23s vs narration 102.12s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-17-deepseek-v4-1-flash-is-the-bes/render/2026-09-17-deepseek-v4-1-flash-is-the-bes-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 81
