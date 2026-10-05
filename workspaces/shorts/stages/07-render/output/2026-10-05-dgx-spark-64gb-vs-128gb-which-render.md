---
slug: 2026-10-05-dgx-spark-64gb-vs-128gb-which
duration_s: 38.43
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.921682
---

# Render: 2026-10-05-dgx-spark-64gb-vs-128gb-which

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-05T16:39:36Z.

## Gates
- lint_video --final: pass (duration 38.43 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.921682)
- Length: 38.43 s; narration 37.64 s
- Scenes: 6/6 storyboard scenes rendered (s1, s2, s3, s4, s5, s6)
- Captions: 106 words; sfx cues pop, tick, ding, pop; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 6.75 | 6.77 | 2 | glm-5.3-flash |  |
| s2 | 7.65 | 7.67 | 2 | glm-5.3-flash |  |
| s3 | 6.64 | 6.67 | 2 | glm-5.3-flash |  |
| s4 | 6.96 | 6.97 | 5 | glm-5.3 |  |
| s5 | 5.72 | 5.73 | 1 | glm-5.3-flash |  |
| s6 | 4.64 | 4.63 | 1 | glm-5.3-flash |  |

## Assembly
- video total 38.43s vs narration 37.64s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-05-dgx-spark-64gb-vs-128gb-which/render/2026-10-05-dgx-spark-64gb-vs-128gb-which-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 173
