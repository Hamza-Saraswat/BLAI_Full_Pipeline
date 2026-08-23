---
name: elevenlabs-narration
description: Turn a narration script into a 44.1 kHz voice track with ElevenLabs (Professional Voice Clone) or with a local Kokoro model when no key is set, keep word timestamps for captions, and gate the result with a Whisper WER check.
metadata:
  tags: "voice, elevenlabs, kokoro, tts, captions, qa, whisper, local"
---

# ElevenLabs narration

## When to Use

- The voice stage of either workspace (Shorts stage 06, long-form stage 08) on the DGX Spark, after the script and storyboard passed the script gates.
- Regenerating narration after a script fix, a QA failure or a pronunciation-dictionary change.
- Producing `captions.json` and `captions.srt` for the render skills and for the YouTube caption upload.

Not for: recording or training the clone (that is a one-time manual task, see `rules/recording-a-dataset.md`), or for any stock-voice experiment outside the A/B plan.

## What You Need Before Calling

- `build/.env` on the Spark with `ELEVENLABS_API_KEY`, `ELEVEN_VOICE_ID`, `ELEVEN_MODEL_ID` (default `eleven_multilingual_v2`) and `ELEVEN_SEED` (default 4242). Never pass or print these. A local test run needs none of them, see "Engines" below.
- The narration as a text file or a storyboard JSON with `narration_full` (numbers already spelled the spoken way by the script gates).
- `ffmpeg` and `ffprobe` on PATH; `faster-whisper` installed (or a built `whisper-cli` with a ggml model) for the QA step.
- An output directory for this slug (for example `$BLAI_BUILD_DIR/<slug>/voice`).

## Engines

`--engine auto` (the default) takes ElevenLabs when `ELEVENLABS_API_KEY` and `ELEVEN_VOICE_ID` are both set, else the local Kokoro model when its file is present, else it exits naming both options. Whichever ran is printed to stderr as one line and recorded in `voice.json` as `engine`.

- **elevenlabs**: the Professional Voice Clone, character timestamps straight from the API, credits billed. The production engine.
- **kokoro**: free, offline, no key. It runs the v1 checkout's `pipeline/scripts/tts_local.py` in that repo's own venv, once per chunk (default voice `am_eric` at speed 1.05, `--kokoro-voice` and `--kokoro-speed` to change it, `--kokoro-root` or `BLAI_KOKORO_ROOT` when that checkout moves). Word times come from whisper.cpp when a built binary is found and otherwise from each chunk's measured duration split by word length; `alignment.json` records which as `source` and `voice.json` as `alignment_source`. Same `narration.wav` (44.1 kHz mono), same `alignment.json`, same `captions.json`, so no later stage changes. Only for local test runs: it is not the creator's voice, and it speaks at a different rate, so a duration measured on Kokoro says nothing about the ElevenLabs cut. `build/README.md` has the whole local flow.

## How It Works

1. `scripts/generate_audio.py --text FILE.txt --out DIR [--format long|short] [--engine auto|elevenlabs|kokoro]` applies `pronunciation_dictionary.json`, chunks at paragraph boundaries (<= 4,500 chars, one chunk for Shorts), synthesizes each chunk with the chosen engine (ElevenLabs: `/v1/text-to-speech/{voice}/with-timestamps` with `previous_text`, `next_text`, a pinned seed and fixed voice settings), then writes `DIR/chunks/NN.mp3` or `NN.wav`, `DIR/narration.wav` (44.1 kHz mono), `DIR/alignment.json` (`words[{word,start,end}]`, `source`, and character times) and `DIR/voice.json` (`duration_s`, `chars`, `chunks`, `credits_estimate`, `model`, `engine`, `alignment_source`, `words_per_second`, `voice_id_hint`).
2. `scripts/qa_transcribe.py --audio DIR/narration.wav --script FILE.txt --out DIR` transcribes with Whisper, normalizes both texts, computes the word-level WER and writes `DIR/transcript.json` and `DIR/qa.json` (`wer`, `pass`, `mismatches[{expected, heard, at_s}]`). Exit 1 above the 0.03 threshold.
3. On failure, find the chunk from `at_s` and re-run step 1 with `--only-chunks N --seed <new>`; add a dictionary entry when a term, not the take, is the problem (`rules/qa-loop.md`).
4. `scripts/captions.py --alignment DIR/alignment.json --script FILE.txt --out DIR` turns the alignment (its `words` array when it has one, else the character times) into `captions.json` (`[{word, start, end}]`, script spelling, voice timing) and `captions.srt` (3-4 words per cue, max 1.8 s).
5. Every script supports `--help` and `--dry-run` (no network and no engine: 3 s of silence plus a synthetic alignment so steps 2-4 still run), logs to stderr, and exits 0/1.

Example: `python3 skills/elevenlabs-narration/scripts/generate_audio.py --storyboard out/<slug>-storyboard.json --out builds/<slug>/voice --format short`

Local test run: `... --out .local-builds/<slug>/voice --format short --engine kokoro` (no key, no credits).

## Rules

- `rules/recording-a-dataset.md`: the seven steps for a PVC dataset that sounds like the creator (length, levels, register, coverage, verification, archive).
- `rules/chunking-and-settings.md`: chunk caps per model, previous/next text, seed, the fixed voice settings, output format, and the PVC + v2 versus v3 test plan.
- `rules/qa-loop.md`: the WER gate, how to regenerate only failing chunks, and when a failure means a dictionary entry or a script fix.
- `rules/pronunciation.md`: how aliases work, how to write and test one, and the ElevenLabs dictionary upgrade path.

## After the Call

- Write the stage note `<slug>-voice.md` from `voice.json` and `qa.json` (duration, chunks, credits, WER, regenerations) and link it from the hub note's Artifacts list.
- Hand `narration.wav`, `alignment.json` and `captions.json` to the render skill; regenerating audio invalidates every caption and scene timing, so rerun captions and render after any regeneration.
- Audio files never enter git (`.gitignore`); the text outputs do.
- Append a build-journal line to the hub note via `tools/hubnote.py journal` with the WER and credit count.
