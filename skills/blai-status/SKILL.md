---
name: blai-status
description: Render the Shorts pipeline status and anything waiting on a human. Use for "status", "what's in the queue", "what needs me".
metadata: {tags: "blai, trigger, shorts, status"}
---

# blai-status

1. Run the workspace `status` trigger per `workspaces/shorts/CLAUDE.md`: scan `stages/*/output/` and `videos/*.md`.
2. Report: the stage row (COMPLETE/PENDING), every hub note by status, and the "needs me" set (`review`, `blocked`, `rejected`) with one line each.
3. Read-only; nothing is written or committed.
