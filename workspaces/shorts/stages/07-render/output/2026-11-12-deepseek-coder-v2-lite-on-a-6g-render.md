---
slug: 2026-11-12-deepseek-coder-v2-lite-on-a-6g
duration_s: 39.23
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.9077
---

# Render: 2026-11-12-deepseek-coder-v2-lite-on-a-6g

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-12T13:54:06Z.

## Gates
- lint_video --final: pass (duration 39.23 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.9077)
- Length: 39.23 s; narration 38.44 s
- Scenes: 5/5 storyboard scenes rendered (s1, s2, s3, s4, s5)
- Captions: 112 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 5.43 | 5.43 | 1 | glm-5.3-flash |  |
| s2 | 10.48 | 10.50 | 2 | glm-5.3-flash |  |
| s3 | 9.75 | 9.77 | 5 | glm-5.3 |  |
| s4 | 3.27 | 3.30 | 1 | glm-5.3-flash |  |
| s5 | 10.23 | 10.23 | 4 | glm-5.3 |  |

## Assembly
- video total 39.23s vs narration 38.44s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-12-deepseek-coder-v2-lite-on-a-6g/render/2026-11-12-deepseek-coder-v2-lite-on-a-6g-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 347
