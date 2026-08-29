---
name: blai-rescript
description: Re-run script and package for a Short whose hub note carries reviewer feedback (after a Reject on the gate card). Use when asked to rescript, or when a hub note has non-empty feedback.
metadata: {tags: "blai, trigger, shorts, rescript, feedback"}
---

# blai-rescript <slug>

1. Read `workspaces/shorts/videos/<slug>.md`; require non-empty `feedback` frontmatter (set it from the argument if given: `python3 tools/hubnote.py set workspaces/shorts/videos/<slug>.md feedback="..."`).
2. Re-run stages `04-script` and `05-package` for the slug per their `CONTEXT.md`s; the feedback line is part of both writers' packets. The note must end at `status: ready-to-build`.
3. Commit with the scoped git-sync line the stages name.
