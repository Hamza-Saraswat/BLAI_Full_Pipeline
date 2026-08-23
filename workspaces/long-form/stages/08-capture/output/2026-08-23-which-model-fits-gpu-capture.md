---
slug: 2026-08-23-which-model-fits-gpu
workspace: long-form
stage: 08-capture
experiment: none
captures: 0
---

# Capture: no experiment

The episode has no experiment plan and no first-party measurement, by design. Stage 03 recorded that the DGX Spark was unreachable from the machine that makes these videos, and the script says so out loud at beat 1.2 before any number is spoken.

Consequences, all verified rather than assumed:

- The spec contains **zero `terminal-replay` scenes and zero `capture_ref` fields**. Stage 05 refused `terminal-replay` for beats 5.7 and 5.9 on the grounds that replaying published documentation would dress it as a measurement (finding 31), and stage 06 had nothing left to downgrade.
- `render_longform.py` was run without `--captures`. Nothing rendered as a placeholder, and the stage 10 audit's capture row passes trivially.
- Every figure in the episode names its publisher on screen.

**This stage skipping cleanly is itself a test result.** The Spark being unreachable did not block the run, did not need a stub file, and did not leave a gap anywhere downstream.
