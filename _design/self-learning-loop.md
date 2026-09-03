# Self-learning loop (design only, 2026-09-02)

Status: DOCUMENTED, NOT BUILT. The user chose to run the first Hermes iteration without any
self-modification. This is the design to build once a week of scheduled runs has produced real
journals, gate results and (with a YouTube key) analytics.

## Principle

The factory improves by editing its DOCUMENTS, never its memory (ICM Pattern 14; SOUL rule b).
Every proposed change is a diff against a file that a human can read, and nothing lands without
a Telegram Approve. Agent `memory` stays limited to operational facts (service names, failure
modes, run history); content rules, thresholds and taste live only in the repo.

## Layers Hermes provides (verified in the installed CLI: `learning`, `curator`, `skills`,
`memory`, `insights`, `/learn`)

1. **`/learn`** — turns a completed session into a skill. Target: after the first clean
   scheduled run, `/learn how the shorts pipeline just ran` -> `shorts-full-run` (a procedure,
   not a restatement of contracts). `skills.write_approval: true` already gates the write.
   Note: `skills/blai-run/SKILL.md` (human-written, 2026-09-02) covers the same ground today;
   `/learn`'s value is capturing the small on-box quirks a run discovers.
2. **`curator` / `learning`** — Hermes's own skill-refinement surface. Not yet probed on the
   box (the off-LAN ssh hang cut the probe short). Wire only behind write_approval, and only
   for skills under `skills/blai-*` and the repo's own skills (never SOUL.md).
3. **`insights`** — tokens/tools/cost per model and session. Feeds the budget line of the
   digest and the weekly retro below.

## The weekly retro (the one loop worth building first)

`hermes cron create "0 19 * * 0" --model glm-5.3 --provider zai --skill blai-run --deliver telegram`

Inputs (read-only): the week's hub-note journals, `_design/test-findings-*.md` additions, gate
failures from the render notes, `hermes insights --days 7`, and once `YT_API_KEY` exists the
`youtube-analytics` skill's weekly pull (viewed vs swiped, CTR, average view duration).

Output: at most THREE proposals, each a unified diff against exactly one of:
`shared/playbook/*.md` thresholds, the stage-04 hook library or structure weights,
`04-script/references/scene-constraints.md`, `skills/script-gates/voice.config.json`
(`voices_wps`), or a `skills/blai-*/SKILL.md`. Each proposal carries the evidence lines that
justify it. Delivered as a Telegram card with Approve/Reject per proposal.

Apply: Approve -> `git apply` + scoped `tools/git-sync.sh "retro: <file> <one-line why>"`.
Reject -> journaled with the reason so the next retro does not re-propose it.

## What the loop must never do

- Change SOUL.md, the model seat map, the delegation config or any credential.
- Touch a stage contract's Inputs/Outputs rows (the handoff shape is fixed by hand).
- Propose more than three changes a week, or the same change twice without new evidence.
- Lower a gate threshold to make a failing run pass; gates move only from analytics evidence.

## Preconditions before building

One week of scheduled runs; `YT_API_KEY` set (or the retro runs on gates and journals only);
the `/learn` skill reviewed once by the user; `curator` probed and its write path confirmed to
honour `skills.write_approval`.
