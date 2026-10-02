---
slug: 2026-10-02-llama-cpp-shipped-three-builds
format: classic
structure: news-react-so-what
style_pack: terminal
value_types: TEACHES,EQUIPS
promise: After forty-two seconds you can say what llama.cpp's b-numbers actually are and re-pin your build tonight.
target_duration_s: 42
brief: 2026-10-02-llama-cpp-shipped-three-builds-brief.md
drafts: 2026-10-02-llama-cpp-shipped-three-builds-drafts.md
---

# llama.cpp moved ten builds today

## Decisions
- Structures: news-react-so-what (draft A) vs how-to-three-moves (draft B); both cleared rotation (last two were comparison-ladder and worked-example). Judge: A won 21-20 on voice and teaching; two grafts applied from B.
- Hook: "Rebuild tonight: ten tagged builds this morning" (Tonight pattern; number plus urgency, legible at 8 words). B ran "Your GGUF isn't broken" (Wrong diagnosis); patterns differ and neither repeats the ledger's decision/situation.
- Grafts from B: "fetch the tags" folded into the close (checkout fails without it) and "The GGUF that failed loads" to demonstrate the cure. Judge named both.
- Style pack: terminal (rotation pick; topic fit, previous was signal).

## Hook candidates
1. Rebuild tonight: ten tagged builds this morning *
2. Ten llama.cpp builds before lunch. Re-pin tonight.
3. Your GGUF isn't broken. Your llama.cpp is.
4. Your llama.cpp isn't slow. Your checkout is stale.
5. Ten nightlies in one morning. Pick one.
6. llama.cpp has no stable release. Just nightlies.
7. You cloned llama.cpp once. It's been quietly rotting.
8. A maintainer dated your recent build to January.
9. Free fixes, ten before lunch. Fetch once.
10. Ride master or pin the tag? Not tonight.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Rebuild tonight: ten tagged builds this morning. | rebuild tonight: 10 builds | Frame 1 finished terminal composition, typed prompt, amber cursor blinking from t=0.30 s; counter 10 stamps on "ten tagged builds". | hyperframes | centered-stack | 2.4 |
| s02 | explain | You built llama.cpp from source once and never updated. A release bot tagged ten builds before breakfast. Three landed within four hours and twenty-five minutes. | 3 builds in 4 h 25 min | Vertical timeline of release ticks types on per tagged build; bracket 4 h 25 min stamps on "twenty-five minutes". Hard cuts. | hyperframes | timeline | 8.6 |
| s03 | explain | Those b numbers are documented nightlies, automated development builds. The seven forty-two bus you board again tomorrow. Two builds can differ, not just schedules. | a tag is the 7:42 bus | Split panes: nightly tags stack left; bus timetable right with the 7:42 slot highlighted amber. | hyperframes | split-compare | 8.3 |
| s04 | explain | Your old binary rejects new GGUF files, single-file model containers. The file is fine. The binary predates the architecture. | old binary rejects new GGUF | GGUF block flows into binary block, stops at a gated edge on "rejects", reroutes green on "the file is fine". Rises in place. | hyperframes | diagram-flow | 5.9 |
| s05 | explain | The catch: a pinned commit pins code, not compiler or GPU flags. Builds target the hardware they see. | a tag pins code, not hardware | Tag chip locks to code block while compiler and GPU chips stay unlocked; stack scales in once on "the catch". | hyperframes | centered-stack | 5.5 |
| s06 | payoff_close | Tonight, read the build line, fetch the tags, check out one exact nightly, rebuild. The GGUF that failed loads, and your setup is only as reproducible as the tag you write down. | the tag you write down | Four-cell grid types on per move; on "loads" the frame-one error resolves to a clean prompt; wordmark settles on the last words. | hyperframes | grid | 11.4 |

## Notes for review
- Numbers spoken verbatim from the brief: "ten tagged builds" and "four hours and twenty-five minutes"; nothing rounded, "seven hours" never spoken (the pages contradict it).
- The bus analogy carries its limit in the same beat ("Two builds can differ, not just schedules"); one analogy only.
- Value delivery: TEACHES lands at s03-s04 (nightly channel; the binary predates the architecture); EQUIPS lands at s06 (the four-move re-pin).
