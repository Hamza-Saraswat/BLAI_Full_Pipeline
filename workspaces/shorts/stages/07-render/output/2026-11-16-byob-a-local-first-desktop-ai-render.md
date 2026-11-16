---
slug: 2026-11-16-byob-a-local-first-desktop-ai
duration_s: 48.47
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.862485
---

# Render: 2026-11-16-byob-a-local-first-desktop-ai

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-16T13:46:00Z.

## Gates
- lint_video --final: pass (duration 48.47 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.862485)
- Length: 48.47 s; narration 47.36 s
- Scenes: 5/5 storyboard scenes rendered (s1, s2, s3, s4, s5)
- Captions: 123 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 6.32 | 6.33 | 2 | glm-5.3-flash |  |
| s2 | 12.15 | 12.17 | 3 | glm-5.3 |  |
| s3 | 11.81 | 11.83 | 2 | glm-5.3-flash |  |
| s4 | 9.27 | 9.30 | 4 | glm-5.3 |  |
| s5 | 8.81 | 8.83 | 1 | glm-5.3-flash |  |

## Assembly
- video total 48.47s vs narration 47.36s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-11-16-byob-a-local-first-desktop-ai/render/2026-11-16-byob-a-local-first-desktop-ai-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 359
