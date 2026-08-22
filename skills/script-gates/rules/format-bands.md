# Format Bands

`skills/script-gates/formats.json` is the single source of truth for the two Shorts bands. `validate_storyboard.py` and `eval_short.py` read it at run time; this file explains what each knob means so a writer aims for the band instead of guessing. Change a number there, never here.

## Which band applies

- `script_format` in the storyboard picks the band. Absent means `classic` (kept from v1 so old boards still validate). An unknown value degrades to `classic` with an advisory, never a blocker.
- `target_duration_s` must sit inside the band's hard range or the board blocks. Inside the hard range but outside the sweet range is a warning.
- The hub note `format` field and the storyboard `script_format` must agree; the package stage copies the storyboard's value.

## Classic (default)

Dense, fast, first person plural ("we run this at home"). One idea per beat, the payoff by second four, an abrupt ending.

| Knob | Value | How the validator uses it |
|------|-------|---------------------------|
| `target_s` | hard 28-60, sweet 32-38 | outside hard: blocker; outside sweet: warning |
| `words` | 70-130, aim ~85-110 | outside: warning (pacing is judged by seconds, not words) |
| `narration_max_chars` | 1200 | schema bound; the band hint |
| `scene_count` | 3-7 | outside: blocker |
| `scene_long_advisory_s` | 12 | a scene with a longer `est_duration_s` is an advisory (split the beat) |
| `scene_narration_advisory_s` | 13 | a scene whose narration runs longer than this at `wps`: advisory |
| `hook.first_sentence_words` | 5-12 | outside: advisory; `hook.scene_max_s` 7: hook scene longer is an advisory |
| `hook.concrete_required` | true | `eval_short.py`: the hook must carry a digit, a key number or an entity |
| `sentence` | cap 20, avg <= 15, no share allowed over cap | every sentence over 20 words is named; average over 15: advisory |
| `numbers` | policy `spend`, min 3, ratio 0.5 | `eval_short.py`: spent >= min(3, ceil(0.5 x key numbers)) |
| `person` | we | not machine-checked for classic |
| `ending` | abrupt | writer's rule; the render lint checks the wordmark settle |
| `vo_band_s` | 20-58 | `eval_short.py` `vo_band_ok`; `final_max_s` 60 and `final_warn_s` 28-47 belong to the render lint |
| `est_sum_tolerance` | 0.8-1.25 | sum of scene `est_duration_s` versus target: advisory outside |
| `wps_fallback` | 2.6 | used only when `voice.config.json` has no `wps` |

## Smooth explainer

One worked example advanced in labelled stages, second person ("you download it, then you hit the wall"), a resolution that answers the opening. Numbers are capped, not spent.

| Knob | Value | How the validator uses it |
|------|-------|---------------------------|
| `target_s` | hard 60-180, sweet 75-150 | as classic |
| `words` | 250-450 | warning outside |
| `narration_max_chars` | 3000 | schema bound |
| `scene_count` | 5-12 | blocker outside |
| `scene_long_advisory_s` / `scene_narration_advisory_s` | 16 / 16 | advisories as classic |
| `hook.first_sentence_words` | 5-14; `scene_max_s` 10 | advisories; `concrete_required` false: the hook opens on a situation, `eval_short.py` waives the concrete-hook gate |
| `sentence` | cap 20, up to 20 % of sentences may exceed it, avg <= 16, runaway 28 | the share over cap is one advisory; any sentence over 28 words is named |
| `numbers` | policy `cap`, max 3 | `eval_short.py`: spending more than 3 key numbers fails the gate |
| `person` | you | more than three "we / our / us" uses: advisory |
| `ending` | resolution-or-recap | writer's rule |
| `vo_band_s` | 60-165; `final_max_s` 180; `final_warn_s` 70-155 | eval and render lint |
| `wps_fallback` | 3.35 | used only when `voice.config.json` has no `wps` |

## Shared knobs

- `wps` comes from `voice.config.json` (2.9, provisional for the ElevenLabs clone) and beats the band fallback. Estimated speech = words / wps; it must land within 0.75-1.25 x `target_duration_s` or the validator raises an advisory. Re-measure `wps` after the first three renders.
- Both bands share the universal checks: hook first and `payoff_close` last (blockers), the concat rule (blocker), `est_duration_s` 2-25 per scene (blocker), adjacent scenes must differ in `layout_archetype` (advisory), at most 6 sfx cues (advisory), FK grade over 8 (advisory), banned hype, spoken CTA, openers, closers and filler density (advisories).

## Structure is independent of the band

- `structure` (storyboard field and hub note field) names the narrative shape from `workspaces/shorts/stages/04-script/references/script-structures.md`: worked-example, myth-bust, comparison-ladder, news-react-so-what, how-to-three-moves, contrarian-take, story-first, number-first.
- The band sets the physics: seconds, words, sentence caps, number policy, person. The structure sets the order of beats. Any structure can be told in either band; a myth-bust can be a 35-second classic or a 100-second smooth explainer.
- The validator never rejects a structure. The `structures` list in `formats.json` is informational; a value outside it produces a warning (exit code unchanged) so a typo stays visible. Rotation (not the same structure as the previous day) is the ideas stage's job, not this skill's.
- `value_types` travels the same way: carried in the storyboard and the hub note for the script audit, never validated here.
