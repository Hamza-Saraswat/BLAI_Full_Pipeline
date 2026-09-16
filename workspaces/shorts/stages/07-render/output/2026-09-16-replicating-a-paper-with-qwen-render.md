---
slug: 2026-09-16-replicating-a-paper-with-qwen
duration_s: 126.77
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.786075
---

# Render: 2026-09-16-replicating-a-paper-with-qwen

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-16T17:16:51Z.

## Gates
- lint_video --final: pass (duration 126.77 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.786075)
- Length: 126.77 s; narration 125.84 s
- Scenes: 11/11 storyboard scenes rendered (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11)
- Captions: 404 words; sfx cues type, ding, pop, tick; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 6.72 | 6.73 | 3 | glm-5.3 |  |
| s2 | 11.75 | 11.77 | 1 | glm-5.3-flash |  |
| s3 | 9.09 | 9.10 | 4 | glm-5.3 |  |
| s4 | 13.35 | 13.37 | 2 | glm-5.3-flash |  |
| s5 | 11.29 | 11.30 | 2 | glm-5.3-flash |  |
| s6 | 12.29 | 12.30 | 3 | glm-5.3 |  |
| s7 | 15.43 | 15.43 | 5 | glm-5.3 |  |
| s8 | 13.84 | 13.83 | 4 | glm-5.3 |  |
| s9 | 10.52 | 10.53 | 2 | glm-5.3-flash |  |
| s10 | 11.68 | 11.70 | 2 | glm-5.3-flash |  |
| s11 | 10.68 | 10.70 | 1 | glm-5.3-flash |  |

## Assembly
- video total 126.77s vs narration 125.84s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-09-16-replicating-a-paper-with-qwen/render/2026-09-16-replicating-a-paper-with-qwen-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 75
