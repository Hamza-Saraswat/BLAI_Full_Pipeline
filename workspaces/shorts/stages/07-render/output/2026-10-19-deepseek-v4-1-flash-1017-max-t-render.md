---
slug: 2026-10-19-deepseek-v4-1-flash-1017-max-t
duration_s: 40.77
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.864634
---

# Render: 2026-10-19-deepseek-v4-1-flash-1017-max-t

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-19T12:46:22Z.

## Gates
- lint_video --final: pass (duration 40.77 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.864634)
- Length: 40.77 s; narration 39.76 s
- Scenes: 6/6 storyboard scenes rendered (s1, s2, s3, s4, s5, s6)
- Captions: 116 words; sfx cues whoosh, tick, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 6.08 | 6.10 | 4 | glm-5.3 | motion inside the first 0.5s (rule 10 stillness) |
| s2 | 6.00 | 6.00 | 2 | glm-5.3-flash |  |
| s3 | 9.82 | 9.83 | 2 | glm-5.3-flash |  |
| s4 | 8.24 | 8.27 | 4 | glm-5.3 |  |
| s5 | 4.34 | 4.37 | 2 | glm-5.3-flash |  |
| s6 | 6.20 | 6.20 | 4 | glm-5.3 |  |

## Assembly
- video total 40.77s vs narration 39.76s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-19-deepseek-v4-1-flash-1017-max-t/render/2026-10-19-deepseek-v4-1-flash-1017-max-t-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 245
