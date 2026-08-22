# Hub Note Template

Do NOT put placeholders here: this is per-run data, not system configuration. `tools/new-run.py` copies this file into `videos/<slug>.md` and fills the frontmatter. Every stage updates only its own fields; the Spark build agent and the Telegram bot update `status`, `feedback`, `youtube_url` and the build journal.

Frontmatter keys are flat scalars so Obsidian Bases and `tools/hubnote.py` can read them without a YAML library.

```markdown
---
slug: 2026-08-25-example-topic
workspace: shorts
title: ""
status: idea
pillar: ""
series: ""
structure: ""
format: ""
style_pack: ""
value_types: ""
created: 2026-08-25
updated: 2026-08-25T11:05:00Z
publish_slot: ""
seo_score: 0
feedback: ""
blocked_reason: ""
build_host: ""
preview_url: ""
youtube_url: ""
blotato_post_id: ""
---

# <working title>

## Artifacts
- Radar: [[stages/01-radar/output/2026-08-25-radar]]
- Ideas: [[stages/02-ideas/output/2026-08-25-ideas]]
- Brief: (filled by stage 03)
- Script: (filled by stage 04)
- Package: (filled by stage 05)
- Voice: (filled by stage 06)
- Render: (filled by stage 07)
- Publish: (filled by stage 08)

## Decisions
(each unattended checkpoint appends: stage, what was chosen, why, in two lines)

## Build journal
(the Spark appends one line per stage run: time, stage, result, duration)
```

Status values, in order: `idea`, `researched`, `scripted`, `ready-to-build`, `building`, `review`, `approved`, `scheduled`, `published`. Side states: `rejected`, `blocked`. Who sets which is in `shared/pipeline-overview.md`.
