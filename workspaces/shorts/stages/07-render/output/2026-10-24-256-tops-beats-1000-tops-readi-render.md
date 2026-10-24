---
slug: 2026-10-24-256-tops-beats-1000-tops-readi
duration_s: 39.90
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.747299
---

# Render: 2026-10-24-256-tops-beats-1000-tops-readi

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-24T13:16:30Z.

## Gates
- lint_video --final: pass (duration 39.90 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.747299)
- Length: 39.90 s; narration 39.04 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 105 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 2.64 | 2.67 | 3 | glm-5.3 |  |
| s02 | 10.01 | 10.03 | 3 | glm-5.3 |  |
| s03 | 5.10 | 5.10 | 2 | glm-5.3-flash |  |
| s04 | 7.55 | 7.57 | 3 | glm-5.3 |  |
| s05 | 8.85 | 8.87 | 2 | glm-5.3-flash |  |
| s06 | 5.65 | 5.67 | 2 | glm-5.3-flash |  |

## Assembly
- video total 39.90s vs narration 39.04s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-24-256-tops-beats-1000-tops-readi/render/2026-10-24-256-tops-beats-1000-tops-readi-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 270
