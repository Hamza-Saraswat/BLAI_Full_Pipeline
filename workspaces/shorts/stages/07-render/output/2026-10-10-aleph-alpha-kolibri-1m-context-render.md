---
slug: 2026-10-10-aleph-alpha-kolibri-1m-context
duration_s: 47.47
gate_lint: pass
gate_safe_zone: pass
gate_loop: pass
loop_ssim: 0.903174
---

# Render: 2026-10-10-aleph-alpha-kolibri-1m-context

Scripted render (`scene_worker.py` per scene, `assemble.py`, `render_note.py`) at 2026-10-10T12:43:45Z.

## Gates
- lint_video --final: pass (duration 47.47 s)
- safe_zone_check: pass
- loop_check: similar (ssim 0.903174)
- Length: 47.47 s; narration 46.40 s
- Scenes: 6/6 storyboard scenes rendered (s01, s02, s03, s04, s05, s06)
- Captions: 122 words; sfx cues none; music none

## Scene timings and attempts

| Scene | Target s | Delivered s | Attempts | Model | Flags |
|-------|----------|-------------|----------|-------|-------|
| s01 | 4.11 | 4.13 | 1 | glm-5.3-flash | motion inside the first 0.5s (rule 10 stillness) |
| s02 | 7.85 | 7.87 | 2 | glm-5.3-flash |  |
| s03 | 9.30 | 9.30 | 1 | glm-5.3-flash |  |
| s04 | 7.77 | 7.80 | 2 | glm-5.3-flash |  |
| s05 | 8.73 | 8.73 | 2 | glm-5.3-flash |  |
| s06 | 9.64 | 9.63 | 1 | glm-5.3-flash |  |

## Assembly
- video total 47.47s vs narration 46.40s (segments win; check scene durations)
- props: /home/buildlocalai/blai/builds/2026-10-10-aleph-alpha-kolibri-1m-context/render/2026-10-10-aleph-alpha-kolibri-1m-context-props.json

## Decisions (unattended)
- scripted render: no checkpoint reached a human; every gate above is machine-decided

## Card
- gate card sent: message_id 198
