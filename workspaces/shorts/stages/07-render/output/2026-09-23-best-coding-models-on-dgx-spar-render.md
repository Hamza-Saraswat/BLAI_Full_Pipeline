---
slug: 2026-09-23-best-coding-models-on-dgx-spar
duration_s: 95.60
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.867343
---

# Render: 2026-09-23-best-coding-models-on-dgx-spar

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-23T13:26:51Z.

## Gates
- lint_video --final: pass (duration 95.60 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.867343)
- Length: 95.60 s; narration 94.48 s
- Scenes: 9/9 storyboard scenes rendered (s1, s2, s3, s4, s5, s6, s7, s8, s9)
- Captions: 268 words; sfx cues pop, ding, ding, tick, tick, pop; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 8.38 | 8.40 | 1 | glm-5.3-flash |  |
| s2 | 12.82 | 12.83 | 4 | glm-5.3 |  |
| s3 | 11.83 | 11.83 | 1 | glm-5.3-flash |  |
| s4 | 7.81 | 7.83 | 1 | glm-5.3-flash |  |
| s5 | 11.22 | 11.23 | 4 | glm-5.3 |  |
| s6 | 9.73 | 9.73 | 2 | glm-5.3-flash |  |
| s7 | 12.61 | 12.63 | 1 | glm-5.3-flash |  |
| s8 | 16.00 | 16.00 | 2 | glm-5.3-flash |  |
| s9 | 5.08 | 5.10 | 3 | glm-5.3 |  |

## Assembly
- video total 95.60s vs narration 94.48s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-23-best-coding-models-on-dgx-spar/render/2026-09-23-best-coding-models-on-dgx-spar-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 115
