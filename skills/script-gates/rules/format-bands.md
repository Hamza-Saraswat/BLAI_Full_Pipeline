# Format Bands

`skills/script-gates/formats.json` is the single source of truth for the two Shorts bands **and for every `eval_short.py` gate threshold**. `validate_storyboard.py` and `eval_short.py` read it at run time; this file explains what each knob means so a writer aims for the band instead of guessing. Change a number there, never here, then re-run `tests/corpus_regression.py`. The gate rows are cross-referenced in `rules/eval-gates.md`.

## Which band applies

- `script_format` in the storyboard picks the band. Absent means `classic` (kept from v1 so old boards still validate). An unknown value degrades to `classic` with an advisory, never a blocker.
- `target_duration_s` must sit inside the band's hard range or the board blocks. Inside the hard range but outside the sweet range is a warning.
- The hub note `format` field and the storyboard `script_format` must agree; the package stage copies the storyboard's value.

## Classic (default)

Dense, fast, second person ("you run this at home"). One idea per beat, the payoff by second four, an abrupt ending. "We" is reserved for our own measurements.

| Knob | Value | How the validator uses it |
|------|-------|---------------------------|
| `target_s` | hard 28-60, sweet 32-38 | outside hard: blocker; outside sweet: warning |
| `words` | 70-130, aim ~85-110 | outside: warning (pacing is judged by seconds, not words) |
| `narration_max_chars` | 1200 | `narration_full` longer than this: advisory |
| `scene_count` | 3-7 | outside: blocker |
| `scene_long_advisory_s` | 12 | a scene with a longer `est_duration_s` is an advisory (split the beat) |
| `scene_narration_advisory_s` | 13 | a scene whose narration runs longer than this at `wps`: advisory |
| `hook.first_sentence_words` | 5-12 | outside: advisory; `hook.scene_max_s` 7: hook scene longer is an advisory |
| `hook.concrete_required` | true | `eval_short.py`: the hook must carry a digit, a key number or an entity |
| `sentence` | cap 20, avg <= 15, no share allowed over cap | every sentence over 20 words is named; average over 15: advisory |
| `numbers` | policy `band`, min 2, max 5 | `eval_short.py`: at least 2 key numbers spent (clamped to the brief's own total) and at most 5 |
| `scene_specificity` | `allow_generic` 1 | `eval_short.py`: every scene but one must carry a number or a named entity |
| `skeleton` | `max_density` 0.15 | `eval_short.py`: share of sentences opening with a connective |
| `positional_labels` | `allowed_structures` how-to-three-moves, worked-example; `max_labels` 3; `min_label_words` 6 | `eval_short.py`: "stage one, stage two" is a hard fail outside those structures |
| `person` | you | more than three "we / our / us" uses: advisory. No "you / your / you're" in the first three sentences: advisory |
| `ending` | abrupt | at most **one** sentence after the payoff line: advisory. The render lint checks the wordmark settle |
| `vo_band_s` | 20-58 | `eval_short.py` `vo_band_ok`; `final_max_s` 60 and `final_warn_s` 28-47 belong to the render lint |
| `est_sum_tolerance` | 0.8-1.25 | sum of scene `est_duration_s` versus target: advisory outside |
| `wps_fallback` | 2.6 | used only when `voice.config.json` has neither `wps_by_format["classic"]` nor `wps` |

## Smooth explainer

One worked example advanced in 3-5 turns, each named by what changes; second person ("you download it, then you hit the wall"); a resolution that answers the opening; numbers capped, not spent. Navigation is carried by content, never by numbering the beats: see `brand-vault/voice-rules.md` Hard Constraint 10 and its Navigation section, and the `worked-example` row in `workspaces/shorts/stages/04-script/references/script-structures.md`.

| Knob | Value | How the validator uses it |
|------|-------|---------------------------|
| `target_s` | hard 60-180, sweet 75-150 | as classic |
| `words` | 250-450 | warning outside |
| `narration_max_chars` | 3000 | `narration_full` longer than this: advisory |
| `scene_count` | 5-12 | blocker outside |
| `scene_long_advisory_s` / `scene_narration_advisory_s` | 16 / 16 | advisories as classic |
| `hook.first_sentence_words` | 5-14; `scene_max_s` 10 | advisories; `concrete_required` false: the hook opens on a situation, `eval_short.py` waives the concrete-hook gate |
| `sentence` | cap 20, up to 20 % of sentences may exceed it, avg <= 16, runaway 28 | the share over cap is one advisory; any sentence over 28 words is named |
| `numbers` | policy `cap`, max 3 | `eval_short.py`: spending more than 3 key numbers fails the gate; there is no floor |
| `scene_specificity` | `allow_generic` 2 | every scene but **two** must be specific; the extra beat is where a wry line or direct address goes |
| `skeleton` | `max_density` 0.15 | as classic |
| `positional_labels` | `allowed_structures` how-to-three-moves, worked-example; `max_labels` 3; `min_label_words` 6 | as classic |
| `person` | you | more than three "we / our / us" uses: advisory. No "you / your / you're" in the first three sentences: advisory |
| `ending` | resolution-or-recap | at most **two** sentences after the payoff line: advisory |
| `vo_band_s` | 60-165; `final_max_s` 180; `final_warn_s` 70-155 | eval and render lint |
| `wps_fallback` | 3.35 | used only when `voice.config.json` has neither `wps_by_format["smooth-explainer"]` nor `wps` |

## Shared knobs

- Words per second comes from `voice.config.json`, in this order: `wps_by_format[script_format]`, then the flat `wps`, then the band's `wps_fallback`. Both scripts (`validate_storyboard.py` and `eval_short.py`) use that same order. The shipped values are all 2.9 and all **provisional** for the ElevenLabs professional clone: they must be re-measured from the first three renders (rendered audio seconds divided by narration word count, per format) and written back into `wps_by_format`. Estimated speech = words / wps; it must land within 0.75-1.25 x `target_duration_s` or the validator raises an advisory.
- `ending` and `narration_max_chars` are enforced, as advisories, by `validate_storyboard.py`. The payoff line is anchored deterministically at the **first sentence of the final `payoff_close` scene**; every sentence after it in that scene counts as tail. `abrupt` allows one tail sentence, `resolution-or-recap` two. It is a proxy, not a semantic reading of the script, and it is an advisory precisely because of that: a close that earns its third sentence ships with a line in the hub note `## Decisions`.
- Both bands share the universal checks: hook first and `payoff_close` last (blockers), the concat rule (blocker), `est_duration_s` 2-25 per scene (blocker), adjacent scenes must differ in `layout_archetype` (advisory), at most 6 sfx cues (advisory), FK grade over 8 (advisory), banned hype, spoken CTA, openers, closers and filler density (advisories).

## Structure is independent of the band

- `structure` (storyboard field and hub note field) names the narrative shape from `workspaces/shorts/stages/04-script/references/script-structures.md`: worked-example, myth-bust, comparison-ladder, news-react-so-what, how-to-three-moves, contrarian-take, story-first, number-first.
- The band sets the physics: seconds, words, sentence caps, number policy, person. The structure sets the order of beats. Any structure can be told in either band; a myth-bust can be a 35-second classic or a 100-second smooth explainer.
- The validator never rejects a structure. The `structures` list in `formats.json` is informational; a value outside it produces a warning (exit code unchanged) so a typo stays visible. Rotation (not the same structure as the previous day) is the ideas stage's job, not this skill's.
- `value_types` travels the same way: carried in the storyboard and the hub note for the script audit, never validated here.
