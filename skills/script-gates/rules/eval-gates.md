# Eval Gates

`eval_short.py` asks one question: did the storyboard spend the specifics the research brief found? The writer may tell the story any way it likes; it may not throw away the concrete material. Seven gates, read from `<slug>-brief.json` and `<slug>-storyboard.json`. Exit 0 when all seven pass, 4 when any fails; the soft distinction below is caller policy, not exit code. Detail lives in the eval JSON: `overall.failures`, `overall.detail`, `board_metrics`.

## The seven gates

| # | Gate | Passes when | classic | smooth-explainer | Hard or soft |
|---|------|-------------|---------|------------------|--------------|
| 1 | `number_spend` | key numbers spent (spoken or on screen) >= min(3, ceil(0.5 x key numbers in the brief)) | floor as stated | cap instead: at most 3 key numbers spent, each on its own beat | hard |
| 2 | `entity_spend` | at least 50 % of the brief's named entities (products, companies, cases, people) appear in narration or on screen | same | same | soft |
| 3 | `top2` | both top-ranked entities (by source tier, then how many claims cite them, then frequency) appear | same | same | soft |
| 4 | `hook_concrete` | `hook_text` plus the first sentence carries a digit, a key number or an entity | required | waived (the hook opens on a situation) | hard |
| 5 | `scene_specificity` | every scene but one carries a key number or an entity | same | same | hard |
| 6 | `skeleton` | share of sentences opening with First / Second / Third / Then / Next / So / Finally / Lastly / And then is at most 0.15 | same | same | hard |
| 7 | `validator` | `validate_storyboard.py` reports zero blockers (advisories allowed) | same | same | hard |

Without a brief (no `--research`, or the file is missing) gates 1, 2, 3 and 5 read as not applicable rather than failed; only the hook, skeleton and validator gates run.

## Soft gates

In the v1 autopilot, `entity_spend` and `top2` were soft: a failure was surfaced to the human and logged, but did not stop the run, because the entity extractor is heuristic (it reads capitalised vocabulary as names and can rank a generic phrase top-2). Keep that behaviour: the script still exits 4, but when `overall.failures` contains only these two names the script stage may proceed with a written reason in the hub note `## Decisions` ("top2 wants 'Business Associate Agreement'; the script says 'signed data agreement' on purpose"). A failure of any hard gate means rewrite, then re-run.

## Reading a failure

- `overall.detail.number_spend`: `spent`, `need`, `total`; `board_metrics.number_spend.detail[]` lists every key number with `spent`, `matched_in` (narration, on_screen, both) and the scene ids that carry it. Unspent rows are the material left on the table.
- `overall.detail.entity_spend` and `top2`: `board_metrics.entity_spend.missing` names what the brief has and the script lacks; `found` what it used.
- `hook_concrete.via` says what made the hook concrete (`digit`, `number:<value>`, `entity:<name>`); empty means nothing did.
- `scene_specificity.scenes[]` marks each scene `specific` true or false with its hits; the generic scene is usually the close, which is allowed once.
- `skeleton.offenders` lists the sentences that open with a connective; rewrite those, do not just delete the connective.
- `language`: `fk_grade`, `words`, `sentences`, `est_speech_s` at the pinned `wps`, `vo_band_ok` against the band's `vo_band_s`.

## How numbers are matched

A key number `value` such as `273 GB/s`, `$4,000`, `30.5B`, `2%` or `July 11, 2026` generates candidate spoken and written forms: digits with and without thousands separators, number words with hyphens or spaces, rounded and truncated forms, magnitude roundings ("two point two million", "2.2M"), unit synonyms ("gigabytes a second", "tokens per second", "percent", "times", "twice"), currency forms and month-day or month-ordinal dates. A candidate with a unit or currency matches anywhere; a bare number needs a word from the key number's label within three words on either side. Write numbers the way `rules/number-and-term-rules.md` says and they match.

## Thresholds live in the script

`GATES_BY_FORMAT` in `eval_short.py` holds the numbers above; `formats.json` holds the bands the language block uses. Change a threshold there, in lockstep with the baseline diffs, and update the table here.
