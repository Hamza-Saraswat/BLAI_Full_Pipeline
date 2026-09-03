---
name: blai-run
description: The token-lean way to run any shorts trigger (ideas, produce, build) as a scheduled or one-shot Hermes session. Load alongside the trigger's own shim. Use for every cron job and every unattended run.
metadata: {tags: "blai, hermes, cron, budget, routing"}
---

# blai-run — how a scheduled session behaves

The contracts live in `workspaces/shorts/**/CONTEXT.md`; this file only says how to *execute*
them without exploring or re-reading. The 2026-08-30 walk cost ~65M tokens because one session
carried every stage; these rules exist so that never repeats.

## Session shape

- One trigger per session: `ideas` (stages 01-02) or `produce <slug>` (03-05) or `build <slug>`
  (06-07 + gate card). Never chain triggers in one session; the cron jobs do the sequencing.
- **One slug per session.** The cron parent only launches `hermes -z "... <slug> ..." -m glm-5.3
  --provider zai --skill blai-run,blai-produce` as `terminal(background=true)` and waits with
  `process`; it never runs a stage itself. Context is the cost: the 2026-09-02 produce session
  carried two slugs and burned 15.8M tokens, most of it re-reading its own history.
- **Stage 03 fetches happen inside one `delegate_task`** whose only return is "brief written,
  validator exit N". Page contents must never enter the orchestrator's context.
- A quota or rate-limit error from the provider ends the session cleanly: hub status untouched,
  one line in the report. The next scheduled run picks the slug up again.
- Start by reading exactly two files: `workspaces/shorts/CLAUDE.md` and the stage `CONTEXT.md`
  you are about to run. Do not `ls`, `grep` or `find` to orient: every path is named in them.
- Never `read_file` a generated artifact to "check" it. Run the check the contract names
  (`tools/check_outputs.py`, the stage validator, `eval_short.py`, `lint_video.py`) and read
  its verdict. Read an artifact only to fix a named failure, and only the lines the failure names.
- Anything that can exceed 60 seconds (voice, render, assembly, whisper) runs as
  `terminal(background=true)` and is watched with the `process` tool. Never block a turn.
- Tail logs (`tail -n 40`), never `cat` them.
- Never type an em dash (U+2014) in any file; write `--`. `tools/validate.py` fails the
  workspace on it (the 2026-08-30 walk left two in the brief and drafts notes).

## Model routing (the seat map)

| Work | Runs on | How |
|---|---|---|
| This session (orchestrator) | GLM-5.3, coding plan | the cron job's `--model glm-5.3 --provider zai` |
| Stage 04 writer A, writer B, judge | Kimi K3 | three separate `tools/llm_call.py --provider moonshot-k3 --model kimi-k3` calls, one packet each (see stage 04 step 3 and 6); never `delegate_task` for these |
| Stage 07 scene workers, stage 03 fan-out | GLM-5.3 | `delegate_task` (the `delegation` config pins it); one worker per scene, private scratch dir |
| Anything else | this session | no delegation for mechanical steps |

## Caps and stop conditions

- Scene fix attempts: **3 per scene** (lint -> fix -> re-render). On the fourth failure, mark the
  scene failed in the render note and stop the build; the hub goes `blocked` with the reason.
- Research sources: the contract's 8-12; never re-fetch a URL already cached under `output/`.
- A stage whose gate fails twice ends the session with the hub `blocked` + `blocked_reason`;
  the digest surfaces it. No third try, no improvisation around a gate.
- Never approve a gate card, never set a hub to `approved`, never run publish from a session.

## Report (last message of every session)

Slug · stage reached · every checkpoint decision (two lines each, unattended rule) · every gate
result · output paths · one line of `hermes insights`-style usage if available. Nothing else.
