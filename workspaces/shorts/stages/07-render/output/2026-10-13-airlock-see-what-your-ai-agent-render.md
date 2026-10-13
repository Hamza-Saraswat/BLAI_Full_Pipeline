---
slug: 2026-10-13-airlock-see-what-your-ai-agent
duration_s: 38.77
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.909637
---

# Render: 2026-10-13-airlock-see-what-your-ai-agent

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-13T12:27:48Z.

## Gates
- lint_video --final: pass (duration 38.77 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.909637)
- Length: 38.77 s; narration 37.96 s
- Scenes: 5/5 storyboard scenes rendered (s1, s2, s3, s4, s5)
- Captions: 112 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s1 | 5.83 | 5.83 | 1 | glm-5.3-flash |  |
| s2 | 7.84 | 7.87 | 2 | glm-5.3-flash |  |
| s3 | 8.81 | 8.83 | 3 | glm-5.3 |  |
| s4 | 8.52 | 8.53 | 2 | glm-5.3-flash |  |
| s5 | 7.68 | 7.70 | 2 | glm-5.3-flash |  |

## Assembly
- video total 38.77s vs narration 37.96s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-13-airlock-see-what-your-ai-agent/render/2026-10-13-airlock-see-what-your-ai-agent-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 215
