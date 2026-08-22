# QA loop

Every narration is transcribed and compared with the script before it reaches the render stage. The loop catches dropped sentences, misread numbers and product names the clone cannot say. Source: research section 3.6.

## The gate

- `scripts/qa_transcribe.py --audio DIR/narration.wav --script FILE.txt --out DIR` writes `qa.json` with `wer`, `pass`, `reference` and `mismatches[{expected, heard, at_s}]`.
- Threshold: WER 0.03 (about one wrong word in 33). Above it the script exits 1 and the stage must not continue to render.
- The reference is compared as written and with the pronunciation aliases applied; the better score counts. A mismatch that survives both is real.
- Normalization before the diff: lowercase, punctuation stripped, digits spelled out (years as "twenty twenty six", prices as "twenty nine dollars", percent), spelled letters collapsed ("D G X" and "DGX" are the same word). Numbers are still the most common real miss; check them first.
- Engines: `faster-whisper` with `small.en` (CUDA float16 on the Spark, int8 on CPU); fallback `whisper-cli` from whisper.cpp with `WHISPER_CPP_MODEL`. Whisper errors exist too, so listen before acting on a single-word mismatch in a proper noun.

## What to do with a failure

1. Read `mismatches`. Each entry is a run of wrong words with `at_s`, the time in the narration where it starts.
2. Map `at_s` onto the chunk table in `alignment.json` (`chunks[].offset_s` and `duration_s`) to find the failing chunk indexes.
3. Decide the cause:
   - Dropped or garbled words, odd pauses, a sentence read twice: regenerate only those chunks with a new seed: `generate_audio.py ... --only-chunks 3,7 --seed 4243`. Re-run the QA. Two regenerations without improvement means the text is the problem (too long a sentence, a bracketed aside, a URL); fix the script and go back to the voice stage.
   - A product name or acronym read wrong: add an alias (see `pronunciation.md`), regenerate the affected chunks. Do not re-record and do not change voice settings for one run.
   - A number read wrong: the script should already spell numbers the way they are spoken (script-gates `normalize_narration.py`); if it does not, fix the script and regenerate.
   - The transcript is right and the script is wrong (typo in the script): fix the script file, because the script is the source of truth, then regenerate.
4. After a pass, run `scripts/captions.py` again: regenerating audio recomputes every caption and scene timing (shared/pipeline-overview.md, source of truth table).

## When to add a dictionary entry

- The same term fails in two different runs, or
- a term from `brand-vault/content-pillars.md` is about to appear for the first time (pre-empt it), or
- the creator hears it wrong even when the WER gate passes (the gate measures words, not vowels).

Do not add entries for ordinary English words, or for terms the voice already reads correctly; every alias changes the text that is billed and can make the phrase sound spelled out.

## Budget

The retry buffer is part of the plan (about 40 % on top of the script length). Watch `voice.json.credits_estimate` per run and the monthly total in the retro; a run that needs more than two regenerations of the same chunk is a script problem, not a credit problem.
