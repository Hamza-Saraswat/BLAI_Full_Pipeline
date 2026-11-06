---
slug: 2026-11-06-offline-ai-on-a-usb-stick-loca
duration_s: 39.40
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.826762
---

# Render: 2026-11-06-offline-ai-on-a-usb-stick-loca

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-11-06T13:52:06Z.

## Gates
- lint_video --final: pass (duration 39.40 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.826762)
- Length: 39.40 s; narration 38.68 s
- Scenes: 5/5 storyboard scenes rendered (s01, s02, s03, s04, s05)
- Captions: 113 words; sfx cues type; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 5.28 | 5.30 | 3 | glm-5.3 |  |
| s02 | 8.05 | 8.07 | 2 | glm-5.3-flash |  |
| s03 | 10.20 | 10.20 | 3 | glm-5.3 |  |
| s04 | 10.35 | 10.37 | 2 | glm-5.3-flash |  |
| s05 | 5.46 | 5.47 | 1 | glm-5.3-flash |  |

## Assembly
- video total 39.40s vs narration 38.68s (segments win; check scene durations)
- scene s02: unknown sfx 'blip' skipped
- scene s03: unknown sfx 'blip' skipped
- scene s04: unknown sfx 'blip' skipped
- props: /home/buildlocalai/blai/builds/2026-11-06-offline-ai-on-a-usb-stick-loca/render/2026-11-06-offline-ai-on-a-usb-stick-loca-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 323
