---
slug: 2026-11-05-kimi-k3-1-pro-1-56-tb-of-weigh
duration_s: 101.73
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.842723
---

# Render: 2026-11-05-kimi-k3-1-pro-1-56-tb-of-weigh

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-05T14:19:47Z.

## Gates
- lint_video --final: pass (duration 101.73 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.842723)
- Length: 101.73 s; narration 100.56 s
- Scenes: 12/12 storyboard scenes rendered (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12)
- Captions: 314 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 3.58 | 3.60 | 4 | glm-5.3 |  |
| s2 | 7.49 | 7.50 | 3 | glm-5.3 |  |
| s3 | 14.40 | 14.40 | 1 | glm-5.3-flash |  |
| s4 | 11.19 | 11.20 | 2 | glm-5.3-flash |  |
| s5 | 4.65 | 4.67 | 2 | glm-5.3-flash |  |
| s6 | 8.28 | 8.30 | 4 | glm-5.3 |  |
| s7 | 9.23 | 9.23 | 2 | glm-5.3-flash |  |
| s8 | 10.54 | 10.57 | 1 | glm-5.3-flash |  |
| s9 | 7.76 | 7.77 | 2 | glm-5.3-flash |  |
| s10 | 9.27 | 9.30 | 2 | glm-5.3-flash |  |
| s11 | 5.88 | 5.90 | 1 | glm-5.3-flash |  |
| s12 | 9.29 | 9.30 | 1 | glm-5.3-flash |  |

## Assembly
- video total 101.73s vs narration 100.56s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-05-kimi-k3-1-pro-1-56-tb-of-weigh/render/2026-11-05-kimi-k3-1-pro-1-56-tb-of-weigh-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 321
