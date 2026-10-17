---
slug: 2026-10-17-hy-memory-30b-a3b-a-30b-that-r
duration_s: 38.83
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.880736
---

# Render: 2026-10-17-hy-memory-30b-a3b-a-30b-that-r

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-17T12:30:47Z.

## Gates
- lint_video --final: pass (duration 38.83 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.880736)
- Length: 38.83 s; narration 37.72 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 112 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 6.84 | 6.83 | 1 | glm-5.3-flash |  |
| s02 | 5.44 | 5.47 | 2 | glm-5.3-flash |  |
| s03 | 6.19 | 6.20 | 2 | glm-5.3-flash |  |
| s04 | 7.42 | 7.43 | 3 | glm-5.3 |  |
| s05 | 7.78 | 7.80 | 4 | glm-5.3 |  |
| s06 | 5.08 | 5.10 | 1 | glm-5.3-flash |  |

## Assembly
- video total 38.83s vs narration 37.72s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-17-hy-memory-30b-a3b-a-30b-that-r/render/2026-10-17-hy-memory-30b-a3b-a-30b-that-r-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 235
