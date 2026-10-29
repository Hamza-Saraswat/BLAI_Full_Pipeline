---
slug: 2026-10-29-deepseek-v4-1-flash-kv-cache-c
duration_s: 38.23
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.883636
---

# Render: 2026-10-29-deepseek-v4-1-flash-kv-cache-c

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-29T12:39:49Z.

## Gates
- lint_video --final: pass (duration 38.23 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.883636)
- Length: 38.23 s; narration 37.36 s
- Scenes: 5/5 storyboard scenes rendered (s1, s2, s3, s4, s5)
- Captions: 112 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 4.94 | 4.97 | 4 | glm-5.3 |  |
| s2 | 6.37 | 6.40 | 2 | glm-5.3-flash |  |
| s3 | 12.05 | 12.07 | 3 | glm-5.3 |  |
| s4 | 10.91 | 10.93 | 2 | glm-5.3-flash |  |
| s5 | 3.85 | 3.87 | 3 | glm-5.3 |  |

## Assembly
- video total 38.23s vs narration 37.36s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-29-deepseek-v4-1-flash-kv-cache-c/render/2026-10-29-deepseek-v4-1-flash-kv-cache-c-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 288
