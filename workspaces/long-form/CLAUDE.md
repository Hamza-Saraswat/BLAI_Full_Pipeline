# BLAI Long-form

Three long-form episodes a week (8-20 minutes) for Build Local AI. Cloud routines run radar, ideas, research, outline, script, spec and package; the DGX Spark runs capture, voice, render and publish; one Telegram tap approves each finished episode.

## Folder Map

```
long-form/
├── CLAUDE.md                (you are here)
├── CONTEXT.md               (task routing)
├── setup/questionnaire.md   (run with "setup")
├── input/                   (curated project notes copied from Local Work; the priority lane)
├── videos/                  (one hub note per episode: the state machine; template in ../../shared/hub-note-template.md)
├── published/               (one note per published episode)
└── stages/
    ├── 01-radar/            (sweep + input notes -> digest)                 cloud
    ├── 02-ideas/            (episode candidates -> 1 pick)                  cloud
    ├── 03-research/         (deep brief + experiment plan)                  cloud
    ├── 04-outline/          (angle, value types, chapters, visual philosophy) cloud
    ├── 05-script/           (full script + narration.txt)                   cloud
    ├── 06-spec/             (scene list from the scene library + thumbnails) cloud
    ├── 07-package/          (titles, description with chapters, manifest)  cloud
    ├── 08-capture/          (run the experiment on the Spark, reconcile)    Spark
    ├── 09-voice/            (narration + captions)                          Spark
    ├── 10-render/           (Remotion episode + thumbnails -> gate card)    Spark
    └── 11-publish/          (approved -> Blotato -> YouTube)                Spark
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Walk through `setup/questionnaire.md` |
| `status` | Render the pipeline (same render as the Shorts workspace, eleven stages) |
| `ideas [--date YYYY-MM-DD] [--unattended]` | Run stages 01 and 02 |
| `produce [--date YYYY-MM-DD] [--unattended]` | Run stages 03 to 07 for the hub note of that date with status `idea` |
| `research [slug]`, `outline [slug]`, `script [slug]`, `spec [slug]`, `package [slug]` | One cloud stage |
| `build [slug]` | Stages 08 to 10 (normally the Spark build agent) |
| `publish [slug]` | Stage 11 (hub status must be `approved`) |
| `rescript [slug]` | Re-run stages 05 to 07 with the hub note's `feedback`; status back to `ready-to-build` |

## Where each stage runs

| Stages | Host | Started by |
|--------|------|-----------|
| 01-02 | cloud routine `blai-longform-ideas` (06:00 CT Mon/Wed/Fri) | cron |
| 03-07 | cloud routine `blai-longform-produce` (07:00 CT Mon/Wed/Fri) | cron, or the Telegram bot's re-script trigger |
| 08-10 | DGX Spark, `build/build.py` | hub status `ready-to-build` |
| 11 | DGX Spark, `build/build.py` | hub status `approved` |

## Unattended mode

As in the Shorts workspace: checkpoints are resolved by the agent and recorded under `## Decisions` in the output and the hub note. The single human gate is the Telegram card sent by stage 10. Documented deviation from ICM Pattern 11.

## Source of truth

Measured numbers from stage 08 beat researched numbers; the reconcile rule in `skills/dgx-capture/rules/reconcile.md` rewrites narration lines that cite them or blocks for re-script. Regenerated audio recomputes every caption and scene timing. See `../../shared/pipeline-overview.md`.

## Routing

| Task | Go To |
|------|-------|
| Sweep sources and input notes | `stages/01-radar/CONTEXT.md` |
| Pick this episode | `stages/02-ideas/CONTEXT.md` |
| Research and plan the experiment | `stages/03-research/CONTEXT.md` |
| Set the angle and chapters | `stages/04-outline/CONTEXT.md` |
| Write the script | `stages/05-script/CONTEXT.md` |
| Build the scene spec | `stages/06-spec/CONTEXT.md` |
| Package | `stages/07-package/CONTEXT.md` |
| Capture, voice, render, publish | `stages/08-capture/CONTEXT.md` to `stages/11-publish/CONTEXT.md` |

## What to Load

| Task | Load These | Do NOT Load |
|------|-----------|-------------|
| Sweep | `stages/01-radar/CONTEXT.md` and its Inputs | every later stage, `brand-vault/voice-rules.md` |
| Pick | `stages/02-ideas/CONTEXT.md` and its Inputs, the digest | `stages/03` onward |
| Research | `stages/03-research/CONTEXT.md` and its Inputs | the digest, `stages/04` onward |
| Outline | `stages/04-outline/CONTEXT.md` and its Inputs (brief, value framework, series section) | the radar and ideas notes, `stages/05` onward |
| Script | `stages/05-script/CONTEXT.md` and its Inputs (outline, brief, voice-rule sections) | `stages/06` onward, other slugs' outputs |
| Spec | `stages/06-spec/CONTEXT.md` and its Inputs (script, scene library) | the brief, `stages/07` onward |
| Package | `stages/07-package/CONTEXT.md` and its Inputs (script, spec, playbook) | the brief, `stages/08` onward |
| Capture, voice, render, publish | that stage's `CONTEXT.md` and its Inputs | every cloud stage's `references/` |

## Stage Handoffs and Git policy

Same as the Shorts workspace: outputs are committed, binaries are not, the hub note is the state, `../../tools/git-sync.sh "long-form: [slug] [stage]"` ends every unattended stage, and other runs' outputs are never read as templates.
