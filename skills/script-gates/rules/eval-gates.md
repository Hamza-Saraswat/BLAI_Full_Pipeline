# Eval Gates

`eval_short.py` asks two questions: did the storyboard spend the specifics the research brief found, and does it sound like the last five videos? The writer may tell the story any way it likes; it may not throw away the concrete material, navigate by numbering beats, or ship the same video twice. Nine gates, read from `<slug>-brief.json`, `<slug>-storyboard.json` and (optionally) the script ledger. Exit 0 when all pass, 4 when any fails; the soft distinction below is caller policy, not exit code. Detail lives in the eval JSON: `overall.failures`, `overall.detail`, `board_metrics`.

## The nine gates

| # | Gate | Passes when | classic | smooth-explainer | Hard or soft |
|---|------|-------------|---------|------------------|--------------|
| 1 | `number_spend` | key numbers spent (spoken or on screen) sit inside the band | at least 2, at most 5 | cap only: at most 3, each on its own beat | hard |
| 2 | `entity_spend` | at least 50 % of the brief's named entities (products, companies, cases, people) appear in narration or on screen | same | same | soft |
| 3 | `top2` | both top-ranked entities (by source tier, then how many claims cite them, then frequency) appear | same | same | soft |
| 4 | `hook_concrete` | `hook_text` plus the first sentence carries a digit, a key number or an entity | required | waived (the hook opens on a situation) | hard |
| 5 | `scene_specificity` | every scene but the allowance carries a key number or an entity | all but one | all but two | hard |
| 6 | `skeleton` | share of sentences opening with First / Second / Third / Then / Next / Finally / Lastly / And then is at most 0.15 | same | same | hard |
| 7 | `positional_labels` | the script does not navigate by "stage one, stage two" (below) | same | same | hard |
| 8 | `sameness` | not the same shape, hook, ending, length or sentence rhythm as the last five ledger entries (`rules/variety.md`) | same | same | hard |
| 9 | `validator` | `validate_storyboard.py` reports zero blockers (advisories allowed) | same | same | hard |

Without a brief (no `--research`, or the file is missing) gates 1, 2, 3 and 5 read as not applicable rather than failed. Without a ledger (no `--ledger`) gate 8 **does not run at all**: `overall.detail.sameness.checked` is `false` with a reason and the report chip reads "not checked (no ledger)". Silence there is not a pass.

The floor in `number_spend` is clamped to the brief's own total, so a two-key-number brief cannot make the bar unreachable. The cap is the recalibration that matters: v1's research named this gate as one of "the two rules that hurt most" and cited a board that spends nine numbers in 132 words, collectively unfollowable.

`skeleton` no longer lists **so**. It opens ~5.8 % of sentences in both formats, it is natural speech rather than scaffolding, and banning it is what pushed the writer into "Stage two:". The 0.15 density cap is unchanged.

## `positional_labels`

Matches, per sentence of `narration_full`, an opening `stage | step | part | phase` plus an ordinal (`one`…`ten` or a digit), optionally behind a leading `And ` / `But `, an `in ` and a `that's`.

- If the storyboard's `structure` is absent or is not `how-to-three-moves` or `worked-example`, the gate fails on the first hit. Labels are for a process the viewer will actually perform; anything else navigates by content.
- If the structure is one of those two, the gate fails when there are more than three labels, when the ordinals are not strictly ascending from one, when any label sentence is under six words, or when a label sentence names no action.

"Names an action" uses a deliberately generous stdlib heuristic, because a false failure here blocks a good script. A label sentence carries an action verb when it contains **either** a word from the `ACTION_VERBS` list in `eval_short.py` (measure, shrink, load, run, cap, send, swap, quantize, install, pull, set, open, close, check, build, write, read plus the common irregulars) **or** any word ending in `-s`, `-ed` or `-ing` that is not in `NON_VERB_STOP`. That stop list holds only copulas, auxiliaries, pronouns and function words (is, was, has, does, this, its, thus, plus, during, nothing, thing, indeed, …) and never ordinary nouns. Contractions are judged on their head, so "That's" is not read as a verb. The effect: "Step two, cap the context window at four thousand tokens." passes; "Stage three.", "Stage four, then." and "Stage four is the strange one." fail.

`overall.detail.positional_labels` carries `count`, `structure`, `allowed_structures`, the offending sentences and a human-readable `reason` naming which ones and why.

The prose side of this rule lives in `brand-vault/voice-rules.md` (Hard Constraint 10 and its Navigation section, which names the legal transition moves) and in `workspaces/shorts/stages/04-script/references/script-structures.md`.

## Soft gates

In the v1 autopilot, `entity_spend` and `top2` were soft: a failure was surfaced to the human and logged, but did not stop the run, because the entity extractor is heuristic (it reads capitalised vocabulary as names and can rank a generic phrase top-2). Keep that behaviour: the script still exits 4, but when `overall.failures` contains only these two names the script stage may proceed with a written reason in the hub note `## Decisions` ("top2 wants 'Business Associate Agreement'; the script says 'signed data agreement' on purpose"). A failure of any hard gate means rewrite and re-run, or a Decisions block that names the gate and why the run proceeded anyway (`rules/variety.md` shows the shape).

## Reading a failure

- `overall.detail.number_spend`: `spent`, `total`, `min`, `max`, `need`, `mode` (`band` or `cap`) and a `reason` when it fails; `board_metrics.number_spend.detail[]` lists every key number with `spent`, `matched_in` (narration, on_screen, both) and the scene ids that carry it. Unspent rows are the material left on the table.
- `overall.detail.entity_spend` and `top2`: `board_metrics.entity_spend.missing` names what the brief has and the script lacks; `found` what it used.
- `hook_concrete.via` says what made the hook concrete (`digit`, `number:<value>`, `entity:<name>`); empty means nothing did.
- `scene_specificity.scenes[]` marks each scene `specific` true or false with its hits; the generic scene is usually the close.
- `skeleton.offenders` lists the sentences that open with a connective; rewrite those, do not just delete the connective.
- `positional_labels.offenders` and `.reasons`: the label sentences and what is wrong with each.
- `sameness.violations[]`: one row per broken rule with the ledger entry it clashes with; `sameness.advisories[]` carries the repeated-phrase notes.
- `language`: `fk_grade`, `words`, `sentences`, `est_speech_s` at the pinned `wps`, `vo_band_ok` against the band's `vo_band_s`.

## How numbers are matched

A key number `value` such as `273 GB/s`, `$4,000`, `30.5B`, `2%` or `July 11, 2026` generates candidate spoken and written forms: digits with and without thousands separators, number words with hyphens or spaces, rounded and truncated forms, magnitude roundings ("two point two million", "2.2M"), unit synonyms ("gigabytes a second", "tokens per second", "percent", "times", "twice"), currency forms and month-day or month-ordinal dates. A candidate with a unit or currency matches anywhere; a bare number needs a word from the key number's label within three words on either side. Write numbers the way `rules/number-and-term-rules.md` says and they match.

## Thresholds live in formats.json

`skills/script-gates/formats.json` is the single source of truth for every threshold in the table above: `numbers.min_count` and `numbers.max_count`, `scene_specificity.allow_generic`, `skeleton.max_density`, `positional_labels.allowed_structures` (plus `max_labels` and `min_label_words`), `entity_spend.min_ratio`, `top2.required`, `hook.concrete_required` and `validator.max_blockers`. `gates_for()` in `eval_short.py` reads them and falls back to the in-code `GATE_FALLBACKS` dict only for a key the file does not carry; those fallbacks mirror the shipped values and are a safety net, not a second opinion. Change a number in `formats.json`, in lockstep with the baseline diffs, then update this table and re-run `tests/corpus_regression.py`.

## Two counting rules worth knowing

**Specificity counts glossary terms.** A scene is specific when it carries a key number, a named entity, or a term from the brief's glossary. The third was added on 2026-08-22 after a script failed the gate on "the machine pulls the model's weights out of memory", which is its most specific sentence. This deliberately differs from the entity gates, which filter glossary terms out: a defined term is not a named example, but it is a specific.

**The number gates count what the viewer hears.** `heard` is the number of distinct spoken phrases matched; `spent` is how many rows of the brief those phrases satisfy. One spoken "about three times" can satisfy a ratio, two bandwidth figures and a second ratio, so `spent` over-counts and `heard` is what the floor and the cap use. A number that appears only in `on_screen_text` still counts, which is how the gate catches on-screen figures that the narration never speaks.
