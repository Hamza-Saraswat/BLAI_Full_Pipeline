# Chunking and voice settings

What `scripts/generate_audio.py` does and why. Source: research sections 3.1 and 3.6.

## Chunking

| Model | Per-request limit | Chunk cap used | Credits per char | Role |
|-------|-------------------|----------------|------------------|------|
| `eleven_multilingual_v2` | 10,000 chars | 4,500 | 1 | default (the stable model) |
| `eleven_v3` | 5,000 chars | 4,500 | 1 | Shorts test model (more expressive, audio tags) |
| `eleven_flash_v2_5` | 40,000 chars | 4,500 | 0.5 | cheap drafts, timing checks |

- Chunks break at paragraph boundaries (blank lines) and never exceed 4,500 characters; a paragraph that is alone longer than the cap is split at sentence ends, then at the last space. Write scripts with one idea per paragraph so the breaks land where a speaker would breathe.
- `--format short` sends the whole narration as one chunk (Shorts run 400-900 characters). If a "short" is longer than the model limit it is chunked with a warning.
- Every request carries `previous_text` (the last 600 characters of the previous chunk) and `next_text` (the first 600 of the next) so prosody carries over the seam.
- The same `seed` (`ELEVEN_SEED`, default 4242) and identical `voice_settings` go into every request. Determinism is not guaranteed by the vendor, but a pinned seed keeps regenerated chunks close to their neighbours.
- Chunk audio is decoded to 44.1 kHz mono WAV, measured, and concatenated with the ffmpeg concat demuxer. `--fade-ms 20` adds a 20 ms fade in/out per chunk at the seam when a click is audible; the default is a plain join.
- Character timestamps from each response are shifted by the accumulated duration of the previous chunks and stored once in `alignment.json`; a newline character with zero length marks each seam.

## Voice settings

| Setting | Value | Why |
|---------|-------|-----|
| `stability` | 0.5 | middle of the range; lower drifts, higher flattens. On v3 this is "Natural" (v3 only accepts 0.0, 0.5, 1.0) |
| `similarity_boost` | 0.8 | stay close to the clone without amplifying recording noise |
| `style` | 0.2 | a little expressiveness; above 0.4 long reads get unstable |
| `use_speaker_boost` | true | cleaner similarity on PVC |
| `speed` | 1.0 | pace is set in the script, not here; measure words per second and adjust the format bands instead |

Change a setting in one place (`VOICE_SETTINGS` in `generate_audio.py`) and note the date in the weekly retro; never per run.

## Output

- `output_format=mp3_44100_192` (Creator plan or higher). PCM output needs Pro; the decode to WAV is lossless enough for the mux, which re-encodes to AAC 48 kHz anyway.
- `narration.wav` is 44.1 kHz mono PCM 16-bit. The render skills resample as needed.
- `voice.json` is the cost ledger: `chars_sent` is what ElevenLabs bills (after aliases), `credits_estimate` is chars times the model's credit rate, `usd_estimate` uses $0.10 per 1k chars (v2, v3) or $0.05 (Flash).

## Test plan for the voice choice

Run the first 3-5 videos in both arms and compare in the weekly retro.

1. PVC + `eleven_multilingual_v2` (primary) versus a stock or Voice Design voice + the same model (control). Measure WER from `qa.json`, regeneration rate, and retention at 30 s and 50 %.
2. Shorts: IVC (or the PVC, if it sounds right) + `eleven_v3` versus PVC + Multilingual v2. v3 allows audio tags such as `[excited]` or `[slowly]` inside the text; keep them out of the script file and add them only in a Shorts-specific pass if the test wins.
3. Keep the loser's voice id on file as the outage hedge; the clone recordings also train a Cartesia or Inworld voice.
4. Concurrency: Creator allows 5 parallel requests; the script runs chunks sequentially on purpose (previous/next text needs order).

## Regenerating chunks

`generate_audio.py --only-chunks 3 --seed 4243 ...` re-synthesizes chunk 3 with a fresh seed, reuses `chunks/NN.mp3` and `chunks/NN.json` for the others, and rebuilds `narration.wav` and `alignment.json`. Use the same `--text`, `--model` and `--max-chars` as the first run so the chunk boundaries are identical.
