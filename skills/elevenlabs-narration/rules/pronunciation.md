# Pronunciation

How product names and acronyms get said right. The file is `pronunciation_dictionary.json` in this skill; the loop-back rule in `shared/pipeline-overview.md` points here when a term is misread.

## How aliases work

- `generate_audio.py` replaces every dictionary key in the narration text with its alias before the request. Matching is case-sensitive and whole-word: `DGX` matches, `dgx` and `DGXs` do not; `AI` inside `OpenAI` is never touched; `GB` next to digits (`128GB`) is not replaced, so write `128 GB` in scripts.
- Longer keys win (`KV cache` before `KV`, `RTX 5090` before `RTX`), and the replacement is a single pass, so an alias never triggers another rule.
- The alias is what the voice reads and what ElevenLabs bills. The alignment therefore contains the alias characters; `captions.py` matches them back onto the script words, so captions show `DGX` with the timing of "D G X".
- `qa_transcribe.py` scores the transcript against the script both with and without aliases and keeps the better, so aliases do not count as errors.

## Writing an alias

- Spell it the way a careful speaker says it, in plain letters: `Kwen`, `coo-da`, `D G X`. Spaced capitals are read as letters; a hyphen inside a word nudges the stress (`Un-sloth`).
- Keep numbers spoken: `R T X fifty ninety`, `G B ten`, `F P eight`.
- Add plural and possessive forms as separate keys when they occur (`GPU`, `GPUs`).
- Multi-word keys are fine and preferred when the phrase has a set reading (`tok/s` to `tokens per second`).
- Do not alias ordinary words, and do not alias a term the voice already reads well; every alias is a small risk of sounding spelled out.

## Testing an entry

1. Put one sentence with the term in a temp file and run `generate_audio.py --text that.txt --out /tmp/pron --dry-run`; the log shows `alias hits` and `voice.json.aliases_applied` lists the substitutions.
2. Run it without `--dry-run` (a few hundred characters, a few credits) and listen.
3. Commit the dictionary change with the slug that triggered it in the message.

## Upgrade path: ElevenLabs pronunciation dictionaries

When the alias list passes 150 entries or an alias cannot fix a term, move to the vendor feature:

- Create a PLS file from the `aliases` map (alias rules), upload it with `POST /v1/pronunciation-dictionaries/add-from-file`, and pass `pronunciation_dictionary_locators: [{pronunciation_dictionary_id, version_id}]` in each request (up to 3 per request).
- Alias rules work on every model. Phoneme rules (IPA or CMU) only work on Flash v2, Turbo v2 and English v1, not on Multilingual v2 or v3, so the alias approach stays the base.
- Keep `pronunciation_dictionary.json` as the source of truth and regenerate the PLS from it; never edit the vendor copy by hand.

## Known limits

- Aliases cannot change stress on a single vowel reliably; if a name still sounds off after two tries, rewrite the sentence so the name is not the stressed word.
- Whisper may transcribe an alias literally ("Kwen"); that is expected and handled by the aliased reference in QA.
