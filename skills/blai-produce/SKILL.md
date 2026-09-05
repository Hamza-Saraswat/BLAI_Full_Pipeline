---
name: blai-produce
description: Produce one Short end to end from an existing hub note at status idea (stages 03-08: research, script, package, voice, render, publish dry-run). Use when asked to produce, build, or render a picked Short.
metadata: {tags: "blai, trigger, shorts, produce"}
---

# blai-produce [slug]

A routing shim. The contracts are the stages', not this file's.

1. `cd workspaces/shorts`, read `CLAUDE.md`; run its trigger `produce` for the slug: stages `03-research` -> `04-script` -> `05-package` per their `CONTEXT.md`s, then the build half `06-voice` -> `07-render` -> `08-publish` per theirs.
2. Stage 04's two blind writers and the judge are three separate `tools/llm_call.py` calls on Kimi K3 (`--provider moonshot-k3 --model kimi-k3`), one packet each, in their own private `.local-builds/<slug>/draft-A|draft-B|judge/` directories -- never delegated subagents (see `blai-run`). Stages 06-08 are NOT yours: once the hub reaches `ready-to-build`, stop. `build/build.py --once` (the `blai-build` cron job) runs voice, `scene_worker.py` per scene, assembly, gates and the gate card as scripts (see `blai-run`).
3. Every gate the contracts name must pass before the next stage starts. The gate card at the end is the human's; never approve it yourself.
