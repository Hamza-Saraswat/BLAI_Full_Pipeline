# BLAI Full Pipeline

Two ICM workspaces that turn local-AI news and Hamza's DGX Spark work into YouTube Shorts (2 a day) and long-form videos (3 a week). Cloud routines run the thinking stages, the DGX Spark runs the build stages, and one Telegram tap per video approves publishing.

## Folder Map

```
BLAI/
├── CLAUDE.md              (you are here: root router)
├── CONTEXT.md             (which workspace handles which task)
├── brand-vault/           (identity, voice rules, pillars, value framework; own CONTEXT.md)
├── shared/                (platform specs, posting playbook, schemas, env template, pipeline overview)
├── skills/                (bundled skills: research, gates, narration, render, publish, telegram, obsidian)
├── workspaces/
│   ├── shorts/            (Shorts pipeline, stages 01-08)
│   └── long-form/         (long-form pipeline, stages 01-11)
├── build/                 (DGX Spark build agent: installer, systemd units, build loop, Telegram bot)
├── tools/                 (validate.py, hubnote.py, new-run.py, git-sync.sh)
├── analytics/             (weekly retro notes)
├── research/              (the two source documents; build-time reference only)
└── _design/               (workflow map, stage contracts, validation report)
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run `setup` inside each workspace (`workspaces/shorts`, `workspaces/long-form`) |
| `status` | Render the pipeline status of both workspaces (see each workspace `CLAUDE.md`) |

## Routing

| Task | Go To |
|------|-------|
| Anything about Shorts (ideas, research, script, package, build, publish) | `workspaces/shorts/CLAUDE.md` |
| Anything about long-form episodes | `workspaces/long-form/CLAUDE.md` |
| Change how the channel sounds or who it is for | `brand-vault/CONTEXT.md` |
| Change posting rules, timing, SEO rubric, compliance | `shared/playbook/` |
| Set up or debug the DGX Spark build agent or the Telegram bot | `build/README.md` |
| Configure cloud routines or the cloud environment | `shared/cloud-environment.md` |
| Check the workspace against the ICM conventions | `python3 tools/validate.py workspaces/<name> --allow-outputs` |

## Rules for every agent in this repo

1. `cd` into a workspace before producing anything. Its `CLAUDE.md` takes over and names exactly what to load.
2. Never write a secret (API key, token, voice id) into any committed file. Secrets live in the cloud environment or the Spark's `.env`; see `shared/env-template.md`.
3. Text outputs are committed (they are the audit trail and the Obsidian archive); audio, video and images never are. `.gitignore` enforces the split.
4. Commit and push with `tools/git-sync.sh "<message>"`; it rebases and retries so routines and the Spark can push the same morning.
5. Do not read other runs' outputs to learn how to write. Reference files are the source of quality (ICM Pattern 14). Reading `published/` for dedupe is the one allowed exception.
6. The research documents in `research/` are build-time references. Do not load them while producing a video.
