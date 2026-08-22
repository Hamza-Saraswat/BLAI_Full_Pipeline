# BLAI Full Pipeline

Two workspaces, one brand. Pick the workspace by the deliverable.

## Task Routing

| Task Type | Go To | Description |
|-----------|-------|-------------|
| Produce or debug a YouTube Short | `workspaces/shorts/CONTEXT.md` | Radar, ideas, research, script, package (cloud); voice, render, publish (Spark) |
| Produce or debug a long-form episode | `workspaces/long-form/CONTEXT.md` | Radar, ideas, research, outline, script, spec, package (cloud); capture, voice, render, publish (Spark) |
| Operate the build agent | `build/README.md` | Spark install, systemd units, build loop, Telegram bot |

## Shared Resources

| Resource | Location | Contains |
|----------|----------|----------|
| Brand context | `brand-vault/CONTEXT.md` | Routes to identity, voice rules, pillars, value framework |
| Platform specs | `shared/platform-specs.md` | Canvas, duration, safe areas per format |
| Posting playbook | `shared/playbook/` | Titles, descriptions, hashtags, thumbnails, timing, compliance, SEO rubric |
| Schemas | `shared/schemas/` | Hub note, storyboard, long-form spec, publish manifest |
| Pipeline overview | `shared/pipeline-overview.md` | Status machine, hosts, source of truth, loop-back table |
| Environment | `shared/env-template.md`, `shared/cloud-environment.md` | Secrets by host; cloud allowlist and connectors |
| Skills | `skills/*/SKILL.md` | Bundled domain knowledge and scripts |
