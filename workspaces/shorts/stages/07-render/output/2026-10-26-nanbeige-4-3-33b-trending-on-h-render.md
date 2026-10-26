---
slug: 2026-10-26-nanbeige-4-3-33b-trending-on-h
duration_s: 36.80
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.834352
---

# Render: 2026-10-26-nanbeige-4-3-33b-trending-on-h

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-26T12:32:57Z.

## Gates
- lint_video --final: pass (duration 36.80 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.834352)
- Length: 36.80 s; narration 35.88 s
- Scenes: 5/5 storyboard scenes rendered (s1, s2, s3, s4, s5)
- Captions: 103 words; sfx cues pop, tick, ding, tick; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 6.43 | 6.43 | 3 | glm-5.3 |  |
| s2 | 6.17 | 6.20 | 3 | glm-5.3 |  |
| s3 | 7.32 | 7.33 | 3 | glm-5.3 |  |
| s4 | 9.90 | 9.90 | 3 | glm-5.3 |  |
| s5 | 6.94 | 6.93 | 2 | glm-5.3-flash |  |

## Assembly
- video total 36.80s vs narration 35.88s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-26-nanbeige-4-3-33b-trending-on-h/render/2026-10-26-nanbeige-4-3-33b-trending-on-h-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 279
