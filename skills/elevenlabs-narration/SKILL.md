---
name: elevenlabs-narration
description: Turn a narration script into a 44.1 kHz voice track with ElevenLabs (Professional Voice Clone), keep character timestamps for captions, and gate the result with a Whisper WER check.
metadata:
  tags: "voice, elevenlabs, tts, captions, qa, whisper"
---

# ElevenLabs narration

## When to Use

- The voice stage of either workspace (Shorts stage 06, long-form stage 08) on the DGX Spark, after the script and storyboard passed the script gates.
- Regenerating narration after a script fix, a QA failure or a pronunciation-dictionary change.
- Producing `captions.json` and `captions.srt` for the render skills and for the YouTube caption upload.

Not for: recording or training the clone (that is a one-time manual task, see `rules/recording-a-dataset.md`), or for any stock-voice experiment outside the A/B plan.

## What You Need Before Calling

- `build/.env` on the Spark with `ELEVENLABS_API_KEY`, `ELEVEN_VOICE_ID`, `ELEVEN_MODEL_ID` (default `eleven_multilingual_v2`) and `ELEVEN_SEED` (default 4242). Never pass or print these.
- The narration as a text file or a storyboard JSON with `narration_full` (numbers already spelled the spoken way by the script gates).
- `ffmpeg` and `ffprobe` on PATH; `faster-whisper` installed (or `whisper-cli` on PATH with `WHISPER_CPP_MODEL`) for the QA step.
- An output directory for this slug (for example `$BLAI_BUILD_DIR/<slug>/voice`).

## How It Works

1. `scripts/generate_audio.py --text FILE.txt --out DIR [--format long|short]` applies `pronunciation_dictionary.json`, chunks at paragraph boundaries (<= 4,500 chars, one chunk for Shorts), calls `/v1/text-to-speech/{voice}/with-timestamps` per chunk with `previous_text`, `next_text`, a pinned seed and fixed voice settings, then writes `DIR/chunks/NN.mp3`, `DIR/narration.wav` (44.1 kHz mono), `DIR/alignment.json` (character times offset per chunk) and `DIR/voice.json` (`duration_s`, `chars`, `chunks`, `credits_estimate`, `model`, `voice_id_hint`).
2. `scripts/qa_transcribe.py --audio DIR/narration.wav --script FILE.txt --out DIR` transcribes with Whisper, normalizes both texts, computes the word-level WER and writes `DIR/transcript.json` and `DIR/qa.json` (`wer`, `pass`, `mismatches[{expected, heard, at_s}]`). Exit 1 above the 0.03 threshold.
3. On failure, find the chunk from `at_s` and re-run step 1 with `--only-chunks N --seed <new>`; add a dictionary entry when a term, not the take, is the problem (`rules/qa-loop.md`).
4. `scripts/captions.py --alignment DIR/alignment.json --script FILE.txt --out DIR` turns the character alignment into `captions.json` (`[{word, start, end}]`, script spelling, voice timing) and `captions.srt` (3-4 words per cue, max 1.8 s).
5. Every script supports `--help` and `--dry-run` (no network: 3 s of silence plus a synthetic alignment so steps 2-4 still run), logs to stderr, and exits 0/1.

Example: `python3 skills/elevenlabs-narration/scripts/generate_audio.py --storyboard out/<slug>-storyboard.json --out builds/<slug>/voice --format short`

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
