---
slug: 2026-11-13-llama-cpp-1-0-pin-it-before-b1
format: classic
structure: news-react-so-what
style_pack: terminal
value_types: TEACHES, EQUIPS
promise: after this Short you can tell which llama.cpp build you run and pin the v1.0.0 tag on purpose instead of riding whatever nightly was newest
target_duration_s: 37
brief: 2026-11-13-llama-cpp-1-0-pin-it-before-b1-brief.md
drafts: 2026-11-13-llama-cpp-1-0-pin-it-before-b1-drafts.md
---

# llama.cpp 1.0 shipped and master already moved

## Decisions
- Structures tried: news-react-so-what (draft A) and number-first (draft B). A won 20-17 (judge, no grafts): the wrong-diagnosis hook names the viewer's exact situation, one number per sentence, every transition carries content. Rotation rule cleared both (last two ledger entries: myth-bust, how-to-three-moves).
- Hook: "You're not on llama.cpp one point oh. You're on a nightly build." -- wrong-diagnosis pattern, candidate 1 of 10; scored 7/8 (payoff word early, product named, viewer situation, legible frame 1). Draft B took candidate 2 (number-shock, 347 vs 68) so the two drafts open on different patterns.
- No grafts: the judge found nothing in B that A says worse within the two-sentence limit.
- Style pack: rotation script picked halftone (LRU tie-break); overruled to terminal on topic fit (llama.cpp is terminal's named row; previous pack was silicon, so no repeat). Style-packs rule 2 allows the overrule; reason recorded here.
- Gates: winner validator 0 blockers 0 advisories; eval all hard gates pass; soft advisories entity_spend 0.077 and top2 (v1.0.0 present on screen, b1b770d absent) kept on purpose -- a commit hash is unreadable in a 37-second Short and the viewer-facing fact is the tag, not the sha; sameness clean vs last 5.
- wps note: est_duration_s derived at wps 2.9 (provisional voice.config value).

## Hook candidates
1. * You're not on llama.cpp one point oh. You're on a nightly build. (wrong-diagnosis; pick, draft A)
2. * Three hundred forty-seven build errors this month. The stable formula had sixty-eight. (number-shock; pick, draft B)
3. llama.cpp just hit one point oh. The crash report landed before lunch. (named-contradiction)
4. Your llama.cpp update breaks itself. The track you poured does. (wrong-diagnosis)
5. One point oh shipped this morning. The tag is not what you're running. (named-contradiction)
6. Thirty-one minutes. That's how long llama.cpp one point oh stayed unbroken. (number-shock)
7. Ride master, get master's bugs. Tonight, pin the tag instead. (tonight)
8. A certified release and a collapsed scaffold, same morning. Pin the certified one. (case)
9. Version one point oh or build twelve thousand three sixty? One is tested. (decision)
10. Your build number starts with b. That letter is the whole story. (wrong-diagnosis)

## Script

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | You're not on llama.cpp one point oh. You're on a nightly build, a daily cut of the development trunk. | You're not on llama.cpp 1.0 | Frame 1: terminal window, hook line already set, amber cursor blinking; second line types on "nightly build" | hyperframes | centered-stack | 7.0 |
| s02 | explain | This morning llama.cpp shipped its first stable tag, a snapshot frozen at one commit. One commit past it, the next nightly had a crash report. | stable tag, +1 commit, crash report | Node "stable tag" fades in on "first stable tag"; "+1 commit" rises on "One commit past it"; "crash report" scales in on "crash report" | hyperframes | timeline | 9.0 |
| s03 | explain | Homebrew tracked thirty days of build errors. The newest-code track logged three hundred forty-seven build errors. The stable formula logged sixty-eight build errors. | --HEAD: 347 errors | Split panel; "347" scales on "three hundred forty-seven build errors"; "68" fades on "sixty-eight"; caption fades on "thirty days" | hyperframes | split-compare | 8.3 |
| s04 | foreshadow | The tag has teeth. It removed thirty-five deprecated functions, old calls marked for deletion. Code built on them stops compiling. | 35 deprecated functions removed | Giant "35" scales in on "thirty-five deprecated functions"; caption fades beneath on "marked for deletion" | hyperframes | giant-number | 7.3 |
| s05 | payoff_close | Tonight, check your build. A b number means you didn't choose it, so pin the tag and choose every move after that. | $ pin v1.0.0 | Command line types on "pin the tag"; wordmark settle | hyperframes | centered-stack | 7.3 |

## Value lines
- TEACHES: s02 -- "This morning llama.cpp shipped its first stable tag, a snapshot frozen at one commit. One commit past it, the next nightly had a crash report."
- EQUIPS: s05 -- "A b number means you didn't choose it, so pin the tag and choose every move after that."

## Notes for review
- The "one commit past it" claim rests on the v1.0.0 release page's own commit counter against 2d8a325; GitHub's banner clocks disagree with the archive tag timestamps, the brief uses archive times (brief Notes). Nothing in the narration reads a clock.
- The crash report is one open issue on CPU-only Intel AMX systems, unreproduced at fetch time; the script says "had a crash report", not "is broken", which is exactly as far as the source goes.
- Homebrew's stable formula still pours 0.9.0, so "brew install llama.cpp" is not yet the pin the video implies; the payoff says "pin the tag", which on a Mac today means the v1.0.0 source archive, not the formula.
- est_duration_s uses the provisional wps 2.9; re-check pacing after the first render.
