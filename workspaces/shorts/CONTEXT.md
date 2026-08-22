# BLAI Shorts Workspace

Take a local-AI trend from the morning sweep to a scheduled YouTube Short, two a day.

## Task Routing

| Task Type | Go To | Description |
|-----------|-------|-------------|
| Sweep sources | `stages/01-radar/CONTEXT.md` | Scored, deduplicated digest of the last 48 hours |
| Pick topics | `stages/02-ideas/CONTEXT.md` | Candidates, keyword research, two picks, hub notes, morning FYI |
| Research a pick | `stages/03-research/CONTEXT.md` | Sourced brief (markdown + JSON) |
| Write the script | `stages/04-script/CONTEXT.md` | Script note and storyboard JSON that pass the gates |
| Package | `stages/05-package/CONTEXT.md` | Titles, description, flags, publish manifest |
| Voice | `stages/06-voice/CONTEXT.md` | Cloned-voice narration, QA, captions (Spark) |
| Render | `stages/07-render/CONTEXT.md` | Scenes, assembly, linters, Telegram gate card (Spark) |
| Publish | `stages/08-publish/CONTEXT.md` | Blotato upload and schedule, published note (Spark) |

## Shared Resources

| Resource | Location | Contains |
|----------|----------|----------|
| Brand context | `../../brand-vault/CONTEXT.md` | Routes to identity, voice rules, pillars, value framework |
| Platform specs | `../../shared/platform-specs.md` | Shorts canvas, bands, safe area |
| Playbook | `../../shared/playbook/` | Titles, hashtags, thumbnails, timing, compliance, rubric |
| Hub note helpers | `../../tools/hubnote.py`, `../../tools/new-run.py` | Read, update, create hub notes |
| Skills | `../../skills/` | trend-radar, youtube-keyword-research, blai-research, script-gates, elevenlabs-narration, render-shorts, blotato-publish, telegram-gate |
