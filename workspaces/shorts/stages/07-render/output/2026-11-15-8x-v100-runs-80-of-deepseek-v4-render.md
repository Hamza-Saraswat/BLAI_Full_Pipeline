---
slug: 2026-11-15-8x-v100-runs-80-of-deepseek-v4
duration_s: 98.07
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.904528
---

# Render: 2026-11-15-8x-v100-runs-80-of-deepseek-v4

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-15T13:47:39Z.

## Gates
- lint_video --final: pass (duration 98.07 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.904528)
- Length: 98.07 s; narration 97.24 s
- Scenes: 8/8 storyboard scenes rendered (s1, s2, s3, s4, s5, s6, s7, s8)
- Captions: 307 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 6.32 | 6.33 | 1 | glm-5.3-flash |  |
| s2 | 14.44 | 14.47 | 2 | glm-5.3-flash |  |
| s3 | 10.74 | 10.77 | 2 | glm-5.3-flash | motion inside the first 0.5s (rule 10 stillness) |
| s4 | 12.05 | 12.07 | 2 | glm-5.3-flash |  |
| s5 | 15.59 | 15.60 | 2 | glm-5.3-flash |  |
| s6 | 14.73 | 14.73 | 5 | glm-5.3 |  |
| s7 | 13.13 | 13.13 | 3 | glm-5.3 |  |
| s8 | 10.96 | 10.97 | 1 | glm-5.3-flash |  |

## Assembly
- video total 98.07s vs narration 97.24s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-15-8x-v100-runs-80-of-deepseek-v4/render/2026-11-15-8x-v100-runs-80-of-deepseek-v4-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 356
