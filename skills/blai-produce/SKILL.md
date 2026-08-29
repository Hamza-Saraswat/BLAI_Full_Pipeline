---
name: blai-produce
description: Produce one Short end to end from an existing hub note at status idea (stages 03-08: research, script, package, voice, render, publish dry-run). Use when asked to produce, build, or render a picked Short.
metadata: {tags: "blai, trigger, shorts, produce"}
---

# blai-produce [slug]

A routing shim. The contracts are the stages', not this file's.

1. `cd workspaces/shorts`, read `CLAUDE.md`; run its trigger `produce` for the slug: stages `03-research` -> `04-script` -> `05-package` per their `CONTEXT.md`s, then the build half `06-voice` -> `07-render` -> `08-publish` per theirs.
2. Stage 04's two blind writers and the judge, and stage 07's per-scene workers, are EPHEMERAL delegated subagents -- one per task, prompted from the stage contract, each in its own private `.local-builds/<slug>/...` directory. Never durable bots, never a shared scratch path.
3. Renders and voice runs go through `background=true` + the process tool; poll, never block a turn.
4. Every gate the contracts name must pass before the next stage starts. The gate card at the end is the human's; never approve it yourself.
