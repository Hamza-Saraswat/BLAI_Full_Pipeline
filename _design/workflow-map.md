# Workflow Map (ICM discovery output)

## Overview

Two repeatable, sequential, human-reviewed pipelines for the Build Local AI YouTube channel: Shorts (two a day) and long-form episodes (three a week). User: one creator comfortable with AI tools, reviewing from a phone. Thinking stages run in cloud routines; build stages run on an always-on DGX Spark; the human gate is a Telegram card.

## Stages (Shorts)

| # | Stage | Input | Output artifact | Reference material | Creative or linear | Host |
|---|-------|-------|-----------------|-------------------|--------------------|------|
| 01 | radar | sources, input notes, archive | `[date]-radar.md/.json` | trend-radar skill, pillars | linear with a judgment line | cloud |
| 02 | ideas | radar | `[date]-ideas.md`, hub notes | keyword skill, value framework, selection rules | creative | cloud |
| 03 | research | ideas, hub notes | `[slug]-brief.md/.json` | research skill, scope | creative | cloud |
| 04 | script | brief, hub | `[slug]-script.md`, `[slug]-storyboard.json` | voice rules, structures, hooks, gates | creative | cloud |
| 05 | package | script, storyboard | `[slug]-package.md` | playbook, rubric | creative | cloud |
| 06 | voice | storyboard | `[slug]-voice.md` + audio | narration skill | linear | Spark |
| 07 | render | storyboard, voice | `[slug]-render.md` + final.mp4 | render-shorts skill, style packs | creative | Spark |
| 08 | publish | package, final.mp4 | `[slug]-publish.md`, published note | blotato skill, timing | linear | Spark |

## Stages (long-form)

| # | Stage | Input | Output artifact | Creative or linear | Host |
|---|-------|-------|-----------------|--------------------|------|
| 01 | radar | sources, input notes | `[date]-radar.md/.json` | linear | cloud |
| 02 | ideas | radar | `[date]-ideas.md`, hub note | creative | cloud |
| 03 | research | ideas, input note | `[slug]-brief.md/.json`, `[slug]-experiment.md` | creative | cloud |
| 04 | outline | brief, experiment | `[slug]-outline.md` | creative | cloud |
| 05 | script | outline, brief | `[slug]-script.md`, `[slug]-narration.txt` | creative | cloud |
| 06 | spec | script, outline | `[slug]-spec.json/.md` | creative (spec as contract) | cloud |
| 07 | package | script, spec | `[slug]-package.md` | creative | cloud |
| 08 | capture | experiment, narration | `[slug]-capture.md` + recordings; rewrites narration | linear + reconcile | Spark |
| 09 | voice | narration | `[slug]-voice.md` + audio | linear | Spark |
| 10 | render | spec, voice, capture | `[slug]-render.md` + final.mp4, thumbnails, chapters | creative | Spark |
| 11 | publish | package, render | `[slug]-publish.md`, published note | linear | Spark |

## Shared context

`brand-vault/` (identity, voice rules, pillars and series, value framework), `shared/platform-specs.md`, `shared/playbook/*`, `shared/schemas/*`, `shared/hub-note-template.md`, `shared/pipeline-overview.md`, `shared/env-template.md`, `shared/cloud-environment.md`.

## User-specific variables

Shipped configured for one creator; the questionnaires edit values in place (Shorts per day, format mix, preview delivery, publish slots; episodes per week, target length, capture window, enabled scene types, favored series). No `{{PLACEHOLDER}}` tokens.

## Optional stages

None removable. Long-form stage 08 passes through when no experiment plan exists. Scene types `mascot-talk` and `b-roll` are disabled by configuration until their assets exist.

## Tool prerequisites

| Tool | Stage | Required | Purpose |
|------|-------|----------|---------|
| Python 3.10+ | all | yes | scripts |
| FireCrawl MCP (`.mcp.json`) | radar, research | optional | search and scrape |
| YouTube Data API key | radar, ideas, analytics | optional | search, competition, stats |
| vidIQ MCP connector | ideas | optional | keyword volume and competition |
| Node 22, ffmpeg, Chrome headless shell | render stages | yes (Spark) | Remotion, HyperFrames |
| Manim | Shorts render | yes (Spark) | diagram scenes |
| faster-whisper | voice | yes (Spark) | transcript QA |
| ElevenLabs account + PVC | voice | yes (Spark) | narration |
| Blotato account, Cloudflare R2 | publish, render preview | yes (Spark) | upload and hosting |
| Telegram bot | ideas, render, publish | yes | FYI and gate cards |
| asciinema | capture | optional | terminal recordings |

## Selected skills

`skills/`: trend-radar, youtube-keyword-research, blai-research (ported), script-gates (ported), elevenlabs-narration, render-shorts (ported), render-longform, dgx-capture, blotato-publish, telegram-gate, obsidian-markdown and obsidian-bases (vendored from kepano/obsidian-skills), youtube-analytics.
