---
name: blai-preflight
description: Verify every render/voice prerequisite on this machine before any build. Use before produce runs, after machine changes, and as the first step of every scheduled job.
metadata: {tags: "blai, trigger, preflight, tools"}
---

# blai-preflight

1. `python3 tools/preflight.py` from the repo root (add `--json` for machines).
2. Any REQUIRED failure stops the run: report it and do not start a build. Warnings are reported and the run may continue.
