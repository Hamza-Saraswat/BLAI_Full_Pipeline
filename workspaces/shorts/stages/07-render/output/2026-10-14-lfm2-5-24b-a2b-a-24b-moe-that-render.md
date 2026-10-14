---
slug: 2026-10-14-lfm2-5-24b-a2b-a-24b-moe-that
duration_s: 101.93
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.91235
---

# Render: 2026-10-14-lfm2-5-24b-a2b-a-24b-moe-that

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-14T12:55:58Z.

## Gates
- lint_video --final: pass (duration 101.93 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.91235)
- Length: 101.93 s; narration 100.92 s
- Scenes: 10/10 storyboard scenes rendered (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10)
- Captions: 319 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 8.15 | 8.17 | 1 | glm-5.3-flash |  |
| s2 | 12.49 | 12.50 | 2 | glm-5.3-flash |  |
| s3 | 7.38 | 7.40 | 1 | glm-5.3-flash |  |
| s4 | 9.13 | 9.13 | 1 | glm-5.3-flash |  |
| s5 | 13.79 | 13.80 | 1 | glm-5.3-flash |  |
| s6 | 14.99 | 15.00 | 2 | glm-5.3-flash |  |
| s7 | 6.84 | 6.87 | 1 | glm-5.3-flash |  |
| s8 | 7.96 | 7.97 | 1 | glm-5.3-flash |  |
| s9 | 12.41 | 12.43 | 1 | glm-5.3-flash |  |
| s10 | 8.66 | 8.67 | 1 | glm-5.3-flash |  |

## Assembly
- video total 101.93s vs narration 100.92s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-14-lfm2-5-24b-a2b-a-24b-moe-that/render/2026-10-14-lfm2-5-24b-a2b-a-24b-moe-that-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 220
