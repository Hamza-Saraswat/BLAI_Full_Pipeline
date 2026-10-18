---
slug: 2026-10-18-nemotron-3-5-super-vl-is-nvfp4
duration_s: 44.80
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.853325
---

# Render: 2026-10-18-nemotron-3-5-super-vl-is-nvfp4

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-18T12:45:31Z.

## Gates
- lint_video --final: pass (duration 44.80 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.853325)
- Length: 44.80 s; narration 44.00 s
- Scenes: 6/6 storyboard scenes rendered (s1, s2, s3, s4, s5, s6)
- Captions: 123 words; sfx cues pop, tick, ding; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 5.68 | 5.70 | 2 | glm-5.3-flash |  |
| s2 | 6.11 | 6.10 | 3 | glm-5.3 |  |
| s3 | 8.69 | 8.70 | 4 | glm-5.3 |  |
| s4 | 11.20 | 11.20 | 4 | glm-5.3 |  |
| s5 | 4.90 | 4.90 | 3 | glm-5.3 |  |
| s6 | 8.10 | 8.10 | 2 | glm-5.3-flash |  |

## Assembly
- video total 44.70s vs narration 44.00s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-18-nemotron-3-5-super-vl-is-nvfp4/render/2026-10-18-nemotron-3-5-super-vl-is-nvfp4-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 240
