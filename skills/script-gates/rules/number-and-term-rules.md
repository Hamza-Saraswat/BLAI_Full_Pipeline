# Number and Term Rules

Narration is read aloud by a voice engine and heard once. `brand-vault/voice-rules.md` (Hard Constraints 4 and 5) owns the rule; this file owns how the machine checks it and what the writer does to pass. `narration` is spoken, `on_screen_text` is seen: they are different languages.

## Narration versus on-screen

| Narration (spoken) | On-screen beat (seen) |
|--------------------|------------------------|
| "twenty-seven billion parameters" | `27B params` |
| "twenty-four gigabytes of memory" | `24 GB` |
| "two hundred seventy-three gigabytes a second" | `273 GB/s` |
| "four thousand dollars" | `$4,000` |
| "H two hundred" | `H200` |

- Digits belong on screen, never in narration. The on-screen beat carries `27B | 17GB` at the moment the narration says the words; that pairing is what works.
- Each `on_screen_text` beat (split on `|`) is at most 8 words; `hook_text` is at most 7 words, 3-5 ideal.
- The same number appears in both at the same moment, or it is not on screen at all. A number on screen that is never spoken is a render-stage loop-back.

## Spoken numbers

- Write every number as words: "twenty-seven billion", "two point seven", "ninety percent", "twenty twenty-six" for a year, "four thousand dollars" for money. Hyphenated or spaced tens both pass.
- Every number names its unit and its referent: "twenty-four gigabytes of memory", "thirty-two billion parameters". "Holds twenty-four gigabytes." fails (gigabytes of what?). Rate phrases ("gigabytes a second") and money ("thousand dollars") already carry the referent.
- Round to what a listener can hold: "about forty-one gigabytes" for 41.42 GB. `eval_short.py` accepts rounded and truncated forms, so rounding never costs a spend point.
- One new number at a time. A listener cannot rewind; two numbers in one sentence is a rewrite.
- Dates: "July eleventh" or "twenty twenty-six", never "7/11/2026".

## Acronyms and product names

- Spell a token the way it is said: "H two hundred", "R T X forty ninety", "F P eight", "mixture of experts" (not "MoE"), "sequel" (SQL), "chwen" (Qwen), "oh-lah-mah" (Ollama).
- If a token has no obvious spoken form, rewrite the line or add a `say` entry to `tts_lexicon.json`. Do not leave it for the normalizer to guess.
- `keep` lists tokens the engine already says correctly (AI, GPU, CPU, RAM, LLM, NVIDIA, US, EU, PDF). Anything else in ALL-CAPS with no `say` entry is spelled letter by letter by the normalizer, and the validator raises an advisory naming it.
- Model names with digits ("Llama 3.1", "Qwen3-30B-A3B") are spoken in full words in narration ("Qwen three thirty B A three B" is unreadable; say "the thirty-billion Qwen three model that wakes three billion"). Put the exact name on screen.

## The lexicon and the normalizer

- `tts_lexicon.json` has three tables. `say`: exact token to spoken form, longest key first, case-sensitive, word-bounded, multi-word keys allowed ("RTX 4090"). `keep`: tokens left as is. `units`: numeric suffix to unit name, matched as number plus optional space or hyphen plus unit ("24GB", "273 GB/s", "7200-RPM").
- Values in `say` contain no digits and no ALL-CAPS run that is not in `keep`, or a later pass re-processes them. `--self-test` checks this.
- `normalize_narration.py` runs: `say` map, money, number plus unit, letter plus digits model tokens (A100, K3), decimals, years, comma integers, bare integers, then the ALL-CAPS safety net. Output is idempotent: normalizing twice equals normalizing once, and no digit survives.
- The normalizer is a safety net, not permission. The writer owns the phrasing because "twenty-seven billion parameters" reads better than whatever the lexicon produces for "27B".
- After every lexicon edit: `python3 skills/script-gates/scripts/normalize_narration.py --self-test` and re-validate the current board.

## What the validator checks (tier)

| Check | Tier | Message starts with |
|-------|------|---------------------|
| A digit string in a scene's narration | advisory | `<scene>: digits in narration:` |
| A scale or capacity word ending its clause with no referent ("gigabytes.", "billion,") | advisory | `<scene>: number without referent:` |
| An ALL-CAPS token with no `say` entry and not in `keep` | advisory | `<scene>: acronym '<tok>' has no spoken form` |
| An ALL-CAPS token the lexicon will expand | warning | `<scene>: '<tok>' will be spoken via` |
| An on-screen beat over 8 words | advisory | `<scene>: on-screen beat >8 words:` |
| `hook_text` over 7 words | advisory | `hook_text >7 words:` |
| A hashtag that is not `#Alnum` | advisory | `hashtags must all match` |

Advisories never block the pipeline, but every one of them is a line the voice engine may mangle; clear them before voice, or write the reason for keeping the line in the hub note.

## Read it aloud

Before keeping a line, read it aloud. If you run out of breath or have to back up to parse it, it fails. Contractions are welcome. Hard cap 20 words a sentence; the band sets the average.
