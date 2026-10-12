---
slug: 2026-10-12-ai-agent-swarms-on-ollama-how
duration_s: 115.37
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.755651
---

# Render: 2026-10-12-ai-agent-swarms-on-ollama-how

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-12T13:05:55Z.

## Gates
- lint_video --final: pass (duration 115.37 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.755651)
- Length: 115.37 s; narration 114.52 s
- Scenes: 10/10 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10)
- Captions: 340 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 9.20 | 9.20 | 4 | glm-5.3 |  |
| s02 | 8.64 | 8.63 | 3 | glm-5.3 |  |
| s03 | 15.49 | 15.50 | 3 | glm-5.3 |  |
| s04 | 11.91 | 11.93 | 2 | glm-5.3-flash |  |
| s05 | 14.30 | 14.30 | 2 | glm-5.3-flash |  |
| s06 | 12.06 | 12.03 | 4 | glm-5.3 |  |
| s07 | 11.36 | 11.40 | 3 | glm-5.3 |  |
| s08 | 14.24 | 14.23 | 3 | glm-5.3 |  |
| s09 | 8.16 | 8.17 | 2 | glm-5.3-flash |  |
| s10 | 9.96 | 9.97 | 4 | glm-5.3 |  |

## Assembly
- video total 115.37s vs narration 114.52s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-12-ai-agent-swarms-on-ollama-how/render/2026-10-12-ai-agent-swarms-on-ollama-how-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 210
