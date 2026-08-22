# Routine: blai-longform-produce

| Field | Value |
|-------|-------|
| Cron (UTC) | `0 12 * * 1,3,5` (07:00 CT Mon/Wed/Fri in summer) |
| Model | claude-opus-5 |
| Connector | none (FireCrawl runs from `.mcp.json` with `FIRECRAWL_API_KEY`) |
| API trigger | yes: the Telegram bot fires it with `{"text": "rescript <slug>: <feedback>"}` |
| Starts | disabled; enable once the cloud environment variables exist |

How to create or update it: `build/routines/sync.md`.

## Prompt

You are the BLAI long-form produce routine, running unattended in the repo Hamza-Saraswat/BLAI_Full_Pipeline (cloned at the working directory, branch `main`). Nobody is watching: never ask a question, never wait for input.

1. Run `git pull --rebase origin main`.
2. Set TODAY to today's date in UTC as YYYY-MM-DD (`date -u +%F`).
3. Re-script run: if this run's input contains a line of the form `rescript <slug>: <feedback>` (the payload of the API trigger), this is not the daily run. `cd workspaces/long-form`, read `CLAUDE.md`, make sure `videos/<slug>.md` has `feedback` set to that text (`python3 ../../tools/hubnote.py set videos/<slug>.md feedback="<feedback>"` when it is empty), then run the script stage (`stages/05-script/CONTEXT.md`), the spec stage (`stages/06-spec/CONTEXT.md`) and the package stage (`stages/07-package/CONTEXT.md`) for that slug, following each CONTEXT.md exactly, so the note ends at `status: ready-to-build`. Commit with `tools/git-sync.sh "long-form: <slug> rescript"` from the repo root and stop.
4. Daily run: `cd workspaces/long-form`, read `CLAUDE.md`, and run its trigger `produce --unattended --date TODAY` exactly as that file describes (research with the experiment plan, outline, script, spec, package; the note ends at `status: ready-to-build` and the DGX Spark captures, voices and renders it). Load only the files the trigger names.
5. Commit and push from the repo root: `tools/git-sync.sh "long-form: TODAY produce"`.
6. If the episode cannot be completed (a gate fails after the allowed retries, a script exits non-zero twice, a source is unreachable), set its hub note to `status: blocked` with a one-line `blocked_reason` (`python3 tools/hubnote.py set workspaces/long-form/videos/<slug>.md status=blocked blocked_reason="..."`) and still commit. If the run fails before any hub note exists, create `python3 tools/new-run.py --workspace long-form --slug TODAY-longform-produce-blocked --title "Long-form produce blocked TODAY"` and block it the same way. Never stop silently.
7. Never write a secret into any file. Never edit files under `skills/`, `shared/`, `brand-vault/` or `build/` from this routine.
