# BLAI Shorts

Two YouTube Shorts a day for Build Local AI. Cloud routines run radar, ideas, research, script and package; the DGX Spark runs voice, render and publish; one Telegram tap approves each finished cut.

## Folder Map

```
shorts/
├── CLAUDE.md                (you are here)
├── CONTEXT.md               (task routing)
├── setup/questionnaire.md   (run with "setup")
├── input/                   (optional seed notes you drop in; read by stage 01)
├── videos/                  (one hub note per Short: the state machine; template in ../../shared/hub-note-template.md)
├── published/               (one note per published Short: dedupe and analytics)
└── stages/
    ├── 01-radar/            (48 h sweep -> scored digest)                 cloud
    ├── 02-ideas/            (candidates -> keyword research -> 2 picks)   cloud
    ├── 03-research/         (pick -> sourced brief)                       cloud
    ├── 04-script/           (brief -> two drafts -> judged script)        cloud
    ├── 05-package/          (script -> title, description, manifest)      cloud
    ├── 06-voice/            (storyboard -> narration + captions)          Spark
    ├── 07-render/           (scenes -> final.mp4 -> Telegram card)        Spark
    └── 08-publish/          (approved -> Blotato -> YouTube)              Spark
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Walk through `setup/questionnaire.md` |
| `status` | Render the pipeline (below) |
| `ideas [--date YYYY-MM-DD] [--unattended]` | Run stages 01 and 02 for the date (default: today, UTC) |
| `produce [--date YYYY-MM-DD] [--unattended]` | Run stages 03, 04, 05 for every hub note of that date with status `idea`, honoring `stages/02-ideas/output/[date]-picks.md` |
| `research [slug]`, `script [slug]`, `package [slug]` | Run one cloud stage for one Short |
| `build [slug]` | Run stages 06 and 07 (normally the Spark build agent does this) |
| `publish [slug]` | Run stage 08 (hub status must be `approved`) |
| `rescript [slug]` | Re-run stages 04 and 05 using the hub note's `feedback`; status back to `ready-to-build` |

### How `status` works

List hub notes with `python3 ../../tools/hubnote.py find . [status]` for each status, then render today's runs. A stage is COMPLETE for a slug when its output file exists:

```
Pipeline Status: shorts  (2026-08-25)

  [01-radar] --> [02-ideas] --> [03-research] --> [04-script] --> [05-package] --> [06-voice] --> [07-render] --> [08-publish]
   COMPLETE       COMPLETE        COMPLETE          COMPLETE         COMPLETE        PENDING        PENDING         PENDING
  (2026-08-25-radar.md) (2026-08-25-ideas.md) ([slug]-brief.md) ([slug]-script.md) ([slug]-package.md)  (empty)  (empty)  (empty)
```

## Where each stage runs

| Stages | Host | Started by |
|--------|------|-----------|
| 01-02 | cloud routine `blai-shorts-ideas` (06:00 CT) | cron |
| 03-05 | cloud routine `blai-shorts-produce` (07:00 CT) | cron, or the Telegram bot's re-script trigger |
| 06-07 | DGX Spark, `build/build.py` | hub status `ready-to-build` |
| 08 | DGX Spark, `build/build.py` | hub status `approved` (the Telegram tap) |

## Unattended mode

Every routine and build run passes `--unattended`. The agent still reaches every checkpoint in the stage contracts, but instead of waiting it makes the call the checkpoint asks for, writes two lines under `## Decisions` in the stage output and in the hub note (what was chosen, why), and continues. Interactive runs from Claude Code pause as normal. This is a documented deviation from ICM Pattern 11; the single human gate is the Telegram card sent by stage 07.

## Routing

| Task | Go To |
|------|-------|
| Sweep sources | `stages/01-radar/CONTEXT.md` |
| Pick today's two topics | `stages/02-ideas/CONTEXT.md` |
| Research a pick | `stages/03-research/CONTEXT.md` |
| Write the script and storyboard | `stages/04-script/CONTEXT.md` |
| Package title, description, manifest | `stages/05-package/CONTEXT.md` |
| Voice, render, publish | `stages/06-voice/CONTEXT.md`, `stages/07-render/CONTEXT.md`, `stages/08-publish/CONTEXT.md` |
| Configure | `setup/questionnaire.md` |

## What to Load

| Task | Load These | Do NOT Load |
|------|-----------|-------------|
| Sweep sources | `stages/01-radar/CONTEXT.md` and its Inputs | `stages/02` to `stages/08`, `brand-vault/voice-rules.md` |
| Pick topics | `stages/02-ideas/CONTEXT.md` and its Inputs, the day's radar digest | `stages/03` onward, `brand-vault/voice-rules.md` |
| Research | `stages/03-research/CONTEXT.md` and its Inputs | the radar digest, `stages/04` onward, `brand-vault/voice-rules.md` |
| Script | `stages/04-script/CONTEXT.md` and its Inputs (brief, voice-rule sections, signature analogies, structures, hooks, judge rubric, the ledger's last 5) | the radar and ideas notes, `stages/05` onward, other slugs' outputs |
| Package | `stages/05-package/CONTEXT.md` and its Inputs (script, playbook) | the brief, `stages/06` onward |
| Voice, render, publish | that stage's `CONTEXT.md` and its Inputs | every cloud stage's `references/`, other slugs' build folders |

## Stage Handoffs and Git policy

Each stage writes to its own `output/` and updates the hub note in `videos/`. The next stage reads whatever is there, edits included. Text outputs are committed (audit trail and Obsidian archive); audio, video and images never are. In unattended mode every stage ends with `../../tools/git-sync.sh "shorts: [slug] [stage]"`. Other runs' outputs are never read as templates (ICM Pattern 14); `published/` is read for dedupe only.
