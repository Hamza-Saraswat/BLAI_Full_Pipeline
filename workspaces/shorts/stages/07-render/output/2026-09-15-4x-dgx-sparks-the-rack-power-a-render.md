---
slug: 2026-09-15-4x-dgx-sparks-the-rack-power-a
duration_s: 102.17
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.904732
---

# Render: 2026-09-15-4x-dgx-sparks-the-rack-power-a

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-09-15T19:06:16Z.

## Gates
- lint_video --final: pass (duration 102.17 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.904732)
- Length: 102.17 s; narration 101.12 s
- Scenes: 11/11 storyboard scenes rendered (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11)
- Captions: 331 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.44 | 5.47 | 2 | glm-5.3-flash |  |
| s02 | 11.95 | 11.97 | 2 | glm-5.3-flash |  |
| s03 | 10.76 | 10.77 | 3 | glm-5.3 |  |
| s04 | 11.77 | 11.80 | 2 | glm-5.3-flash |  |
| s05 | 10.76 | 10.77 | 5 | glm-5.3 |  |
| s06 | 5.27 | 5.27 | 2 | glm-5.3-flash |  |
| s07 | 12.42 | 12.43 | 3 | glm-5.3 |  |
| s08 | 9.45 | 9.47 | 1 | glm-5.3-flash |  |
| s09 | 9.30 | 9.30 | 4 | glm-5.3 |  |
| s10 | 7.36 | 7.37 | 1 | glm-5.3-flash |  |
| s11 | 7.56 | 7.57 | 1 | glm-5.3-flash |  |

## Assembly
- video total 102.17s vs narration 101.12s (segments win; check scene durations)
- scene s04: unknown sfx 'soft connector click' skipped
- scene s09: unknown sfx 'low warm hum swell' skipped
- props: /home/buildlocalai/blai/builds/2026-09-15-4x-dgx-sparks-the-rack-power-a/render/2026-09-15-4x-dgx-sparks-the-rack-power-a-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 66
