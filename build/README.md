# build/ : the DGX Spark build agent

The Spark runs the stages that need a GPU, a browser, a voice or a key: voice, capture, render, publish. Cloud routines produce the text; this folder turns it into video. Everything here is user-level (no root service), idempotent, and driven by hub-note statuses (`shared/pipeline-overview.md`).

## What is here

| File | Purpose |
|------|---------|
| `install.sh` | One-shot installer, safe to re-run. Node 22 (nvm), ffmpeg, asciinema, the Python venv, Claude Code, the render projects, manim, the deploy key, `.env`, the systemd units, the Telegram chat id helper. Prints a checklist of what still needs a human. |
| `build.py` | The loop: one pass every 5 minutes (lock, `git pull --rebase`, publish approved notes, poll scheduled ones, build one `ready-to-build` note). |
| `stage_runner.py` | The stage table: how each Spark stage is invoked, what it verifies, which note it writes. |
| `systemd/` | `blai-build.service` + `blai-build.timer` (every 5 min) and `blai-telegram-bot.service`, installed as user units. |
| `routines/` | The exact prompts of the five cloud routines and `sync.md` (how to create them with `RemoteTrigger`). |
| `.env.example` | The Spark block of `shared/env-template.md`; copied to `.env` (mode 600, gitignored). |
| `requirements.txt` | Python packages for `$HOME/blai/venv`. |
| `logs/`, `state/`, `locks/` | Runtime only, gitignored: daily logs, the Telegram offset, the build lock. |

## Install

```bash
# with sudo: sudo mkdir -p /srv/blai && sudo chown "$USER" /srv/blai && git clone <repo> /srv/blai/repo
# without:   git clone <repo> "$HOME/blai/repo"
cd /srv/blai/repo        # or $HOME/blai/repo
bash build/install.sh    # re-run any time; --dry-run prints the plan
```

The clone you run `install.sh` from becomes `BLAI_REPO_DIR`; `BLAI_BUILD_DIR` defaults to `$HOME/blai/builds`. Both are written into `build/.env`, which systemd and `build.py` read, so there is one source of truth. The installer prints the deploy key to add on GitHub (write access), the `.env` values still empty, and whether `claude` needs `/login`. It enables the units but starts them only when `.env` has no empty required value; fill `.env` and run it again.

Needs a human, always: the API keys, `claude` then `/login` once, the deploy key on GitHub, `TELEGRAM_CHAT_ID` (send the bot a message, re-run the installer, it prints the id). Needs sudo, or an admin: `apt` packages for ffmpeg (else a static BtbN build lands in `~/.local/bin`), manim's cairo/pango headers, the headless-browser libraries, `loginctl enable-linger` (without it the units stop at logout).

## Run and watch

```bash
systemctl --user status blai-build.timer blai-build.service blai-telegram-bot.service
systemctl --user list-timers                       # next run
journalctl --user -u blai-build.service -f         # live log of the passes
journalctl --user -u blai-telegram-bot.service -n 100
systemctl --user start blai-build.service          # force a pass now
systemctl --user restart blai-telegram-bot.service # after editing .env
tail -f build/logs/$(date -u +%F).log              # the same log, as a file
```

Manual passes (the venv python has the dependencies):

```bash
~/blai/venv/bin/python build/build.py --once --dry-run          # plan only, touches nothing
~/blai/venv/bin/python build/build.py --once                    # one real pass
~/blai/venv/bin/python build/build.py --once --slug <slug>      # this note only: rebuild a blocked one, publish an approved one
~/blai/venv/bin/python build/build.py --once --slug <slug> --fresh   # ignore earlier audio/captures/posts in the build dir
~/blai/venv/bin/python build/stage_runner.py --list             # the stage table
~/blai/venv/bin/python build/stage_runner.py --note workspaces/shorts/videos/<slug>.md --stage 06-voice --dry-run
python3 build/build.py --once --local                           # no keys, local voice: see the next section
```

## Local test run on a Mac

`--local` runs the whole build on a developer machine with **no API key at all**, so both formats can be rendered before ElevenLabs, Blotato, R2 or Telegram exist. It needs three things on disk: `ffmpeg` on PATH, a checkout that owns the Kokoro voice (`pipeline/models/kokoro-v1.0.onnx`, `voices-v1.0.bin`, `pipeline/.venv`, `pipeline/scripts/tts_local.py`), and, for word timings and the WER check, a built whisper.cpp with a ggml English model. Nothing is written into that checkout; it is only read and executed.

```bash
# 0. one-time check (the v1 repo is the default; move it with BLAI_KOKORO_ROOT or --kokoro-root)
V1=~/Documents/Projects/BLAI_Animator
ls "$V1/pipeline/models/kokoro-v1.0.onnx" "$V1/pipeline/.venv/bin/python"
ls "$V1/render/remotion/whisper.cpp/build/bin/whisper-cli" "$V1/render/remotion/whisper.cpp/ggml-base.en.bin"

# 1. what local mode changes, and the plan for the next ready-to-build note (writes nothing)
python3 build/stage_runner.py --list --local
python3 build/build.py --once --local --dry-run

# 2. one real local pass: the oldest ready-to-build note, voice then render
python3 build/build.py --once --local
python3 build/build.py --once --local --slug <slug>           # or pick the note yourself
python3 build/build.py --once --local --slug <slug> --fresh   # ignore audio from an earlier attempt

# 3. or one stage at a time (shorts 06-voice, 07-render; long-form 08-capture, 09-voice, 10-render)
python3 build/stage_runner.py --note workspaces/shorts/videos/<slug>.md --stage 06-voice --local
python3 build/stage_runner.py --note workspaces/shorts/videos/<slug>.md --stage 07-render --local

# 4. the result
open .local-builds/<slug>/render/final.mp4
afplay .local-builds/<slug>/voice/narration.wav     # the voice on its own
cat .local-builds/<slug>/voice/voice.json           # engine, duration, words per second
```

Only the voice, without the build agent:

```bash
OUT=.local-builds/<slug>/voice
python3 skills/elevenlabs-narration/scripts/generate_audio.py --text <narration.txt> --out "$OUT" --format short --engine kokoro
python3 skills/elevenlabs-narration/scripts/qa_transcribe.py --audio "$OUT/narration.wav" --script <narration.txt> --out "$OUT"
python3 skills/elevenlabs-narration/scripts/captions.py --alignment "$OUT/alignment.json" --script <narration.txt> --out "$OUT"
```

A long-form note that carries an experiment plan waits for the 01:00-06:00 CT capture window; set `capture_window: any` in its hub note to build it now. Without a plan, `08-capture` writes a "no experiment" note and moves on, which is the normal Mac case.

### What differs from a real run

| | Real run (Spark) | `--local` |
|---|---|---|
| Required `.env` | 11 values; an empty one stops the loop | none, only the paths are checked |
| Voice | ElevenLabs clone, `eleven_multilingual_v2`, credits billed | Kokoro `am_eric` at speed 1.05, free and offline, resampled to the same 44.1 kHz mono `narration.wav` |
| Word timings | ElevenLabs character timestamps | whisper.cpp word times mapped onto the script (`alignment.json` `"source": "whisper"`), or each chunk's measured duration split by word length (`"proportional"`) when no binary is built |
| WER gate | above 0.03 blocks the note | warns and journals instead; the local `ggml-base.en` model mishears homophones (`buy`/`by`, `Mac's`/`max`) and sets a floor near 0.03 by itself |
| Gate card | Telegram card with buttons | `send_card.py --dry-run` printed to stdout, note still set to `review` |
| Approval | you tap Approve or Reject in Telegram | edit `status:` in the hub note by hand (`review` to `approved`) |
| Publish | R2 upload plus a Blotato post, note goes to `scheduled` | `publish.py --dry-run` body printed, nothing uploaded, note stays at `approved` |
| Git | commit and push after every stage | skipped, and the log says so; the working tree is left as it was |
| Build dir | `$BLAI_BUILD_DIR` (`$HOME/blai/builds`) | `<repo>/.local-builds` (gitignored) |
| Pacing | ElevenLabs, provisionally 2.9 words per second | Kokoro `am_eric` at 1.05 measured at about 4.2 words per second, so a script cut for one engine is mis-cut for the other |

Everything else is the real thing: the same scripts, the same stage order, the same hub-note statuses, the same journal lines, the same `final.mp4`.

### Switching back

There is nothing to undo. Drop `--local` and the Spark path runs unchanged: `BLAI_REPO_DIR`, `BLAI_BUILD_DIR` and `build/.env` are read again, ElevenLabs is chosen as soon as `ELEVENLABS_API_KEY` and `ELEVEN_VOICE_ID` are both set, and publishing, cards and git-sync come back. Delete `.local-builds/` to reclaim the space, and re-run the voice stage with `--fresh` once the real voice exists, because Kokoro audio, captions and scene timings do not carry over. `BLAI_LOCAL=1` switches a whole shell into local mode, so `unset BLAI_LOCAL` if you exported it.

## What a pass does

1. Takes `build/locks/build.lock`; exits quietly if another pass holds it (the timer also never overlaps a running service).
2. Commits and pushes anything an interrupted pass left behind, then `git pull --rebase`. A failed pull ends the pass; the next one retries.
3. For every hub note with `status: approved`: runs the publish stage (`08-publish` or `11-publish`), which uploads to R2, posts to Blotato for the next slot (`shared/playbook/publish-timing.md`), writes `<slug>-publish.md` and `published/<slug>.md`, sets `status: scheduled`, and sends the checklist card.
4. For every `status: scheduled` note whose slot has passed: `publish.py --status`; on published sets `status: published` and `youtube_url` (also in `published/<slug>.md`).
5. Builds the oldest `status: ready-to-build` note, one per pass: sets `status: building` and `build_host`, pushes, then runs the workspace's stages in order and pushes after each. Shorts: `06-voice`, `07-render`. Long-form: `08-capture`, `09-voice`, `10-render`. The render stage sends the Telegram gate card and leaves `status: review`; the Telegram bot turns your tap into `approved` or `rejected`.
6. A long-form note with an experiment plan waits for the 01:00-06:00 CT capture window unless its hub note says `capture_window: any`.

Every stage appends `<stage> ok|fail <seconds>s` to the hub note's Build journal. A failed stage is retried once (voice and capture reuse what the first attempt produced, so the retry is cheap); then the note gets `status: blocked`, a `blocked_reason`, a journal line, a push and a Telegram blocked card. A stage that blocks the note itself (the capture reconcile rule when a measured number is out of tolerance) is not retried. Fix the cause, then `build.py --once --slug <slug>` (add `--fresh` after changing the pronunciation dictionary or the experiment plan). A blocked publish is retried from `approved` the same way; the post id of a successful Blotato call is kept in the build dir so a retry never posts twice.

Per-slug binaries: `$BLAI_BUILD_DIR/<slug>/{voice,capture,render,logs}/`. Nothing binary enters git; the markdown notes under `stages/*/output/` are the audit trail.

## Stage table

| Workspace | Stage | Kind | Runs |
|-----------|-------|------|------|
| shorts | `06-voice` | mechanical | `generate_audio.py --storyboard`, `qa_transcribe.py`, `captions.py`; writes `<slug>-voice.md` (duration, chars, chunks, WER, mismatches, pass/fail); a failed QA blocks with the mismatches |
| shorts | `07-render` | creative | `claude -p --dangerously-skip-permissions --output-format json --max-turns 200 "Run stage 07-render for <slug> in unattended mode. ..."` in `workspaces/shorts`; verifies `render/final.mp4`, `<slug>-render.md`, `status: review` |
| shorts | `08-publish` | mechanical | `publish.py --package stages/05-package/output/<slug>-package.md --video render/final.mp4 --slot auto` |
| long-form | `08-capture` | mixed | `capture.py --plan stages/03-research/output/<slug>-experiment.md --window <capture_window or night>`, then `claude -p` "Run stage 08-capture reconcile ..."; without an experiment file it writes a "no experiment" note and moves on |
| long-form | `09-voice` | mechanical | as `06-voice` with `--text stages/05-script/output/<slug>-narration.txt --format long` |
| long-form | `10-render` | creative | `claude -p` "Run stage 10-render ..."; verifies `final.mp4`, `thumbnails/1.png`, `<slug>-render.md`, `status: review` |
| long-form | `11-publish` | mechanical | as `08-publish` with `--thumbnail render/thumbnails/<thumbnail_pick or 1>.png` (the `.jpg` twin when the png exceeds 2 MB) and `--chapters render/chapters.json` (measured times) when present, package from `stages/07-package` |

`claude -p` runs with a 2 h timeout, stdout captured to the day log and to `$BLAI_BUILD_DIR/<slug>/logs/`. It needs a logged-in `claude` and `node` on the unit's PATH (`install.sh` links nvm's node into `~/.local/bin`).

## Telegram bot

`blai-telegram-bot.service` keeps `skills/telegram-gate/scripts/bot.py` running (long polling, restart after 15 s). It answers the card buttons, updates `status` and `feedback`, commits with `tools/git-sync.sh`, and fires the re-script API trigger (`ROUTINE_RESCRIPT_URL`). Its state (update offset, pending feedback) lives in `build/state/telegram-state.json`; the message ids of sent cards in `build/state/telegram-messages.json`.

## Troubleshooting

| Symptom | Check |
|---------|-------|
| Timer active, nothing builds | `build.py` refuses to work while `.env` has empty required values: `journalctl --user -u blai-build.service -n 20` names them |
| `git pull --rebase failed` in the log | the deploy key is not on GitHub with write access, or `ssh -T git@github-blai` fails |
| Render stage blocked with `claude -p failed` | `claude` not logged in (`claude` then `/login`), or `node` missing from `~/.local/bin`; the full `claude` output is in `$BLAI_BUILD_DIR/<slug>/logs/` |
| Voice stage blocked with `voice QA failed` | add the term to `skills/elevenlabs-narration/pronunciation_dictionary.json`, commit, then `build.py --once --slug <slug> --fresh` |
| Long-form note never starts | it has an experiment plan and waits for 01:00-06:00 CT; set `capture_window: any` in the hub note to run now |
| Units vanish after logout | `loginctl enable-linger $USER` (needs sudo once) |
| `--local` says `no voice engine` | the Kokoro model is not where it is expected: `python3 build/stage_runner.py --list --local` prints the repo it uses, and `BLAI_KOKORO_ROOT` or `generate_audio.py --kokoro-root` moves it |
| `--local` voice sounds right but the captions drift | `alignment.json` says `"source": "proportional"`, so no whisper.cpp binary was found; build one or set `WHISPER_CPP_BIN` and `WHISPER_CPP_MODEL` |
| `another pass holds build/locks/build.lock` | a pass is still running (renders take minutes, captures hours); `ps -ef \| grep build.py` |
