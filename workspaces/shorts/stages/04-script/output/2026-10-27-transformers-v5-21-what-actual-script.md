---
slug: 2026-10-27-transformers-v5-21-what-actual
format: classic
structure: how-to-three-moves
style_pack: blueprint
value_types: TEACHES,EQUIPS
promise: After this, you can pin transformers on purpose and say why the pin matters.
target_duration_s: 43
brief: 2026-10-27-transformers-v5-21-what-actual-brief.md
drafts: 2026-10-27-transformers-v5-21-what-actual-drafts.md
---

# transformers v5.21: pin it like llama.cpp

## Decisions
- Structures tried: contrarian-take (A) vs how-to-three-moves (B). Judge tie 18-18; row-6 tiebreak to B (different shape, opening rhythm and landing than the last five). A's voice row was 0 (two new numbers in one sentence; bare "unsloth-zoo").
- Hook: two picks from two different patterns -- candidate 3 "You didn't upgrade. Transformers upgraded itself." (named-contradiction) went to draft A; candidate 7 "Three moves tonight: pin transformers, sleep well." (tonight) went to draft B, whose how-to shape needs the count-promise opening. Neither pick is number-shock (banned: 10-26) nor decision (banned: 10-25).
- Grafts taken from A per the judge: "Unpinned, pip always pulls the newest version." into s03 (states the drift mechanism, B's row-8 gap); "A pin delays fixes, so schedule the upgrade." into s05 (the honest trade-off, the brief's objection) -- placed at the end of s05 rather than inside the close scene so the payoff line stays last (hard constraint 7 and the ending-tail advisory).
- Label check: three labels, ascending from one, each naming an action; the count opened in the hook closes at move three.
- Duration: 43 s, five words over the 32-38 s sweet window; cause is the two judge-ordered grafts. Kept: the grafts carry the rubric's mechanism and trade-off fixes, not padding. Sameness checks pass (opener Jaccard, closing move, hook pattern).
- Value delivery: TEACHES lands in s03's "Unpinned, pip always pulls the newest version." (the drift mechanism); EQUIPS lands in s04's "transformers equals equals five twenty-one in requirements." plus s06's rerun-the-known-prompt close (the act-on-it-tonight move).
- Gates: validator 0 blockers, 1 advisory (0 YouTube keyword tags; stage 05 owns the tags box); eval exit 0 with all nine gates passing; entity_spend and top2 are soft advisories (the literal version strings "v5.21"/"v5.21.0" are not natural spoken entities; "Unsloth's helper package" is spoken instead of the bare "unsloth-zoo").
- s04 split into s04 + s05 after the grafts (scene-length advisory fix); adjacent layouts still alternate.

## Hook candidates
1. Transformers v5.21 landed. Your pipeline changed silently.
2. Three million installs a day. None of them pinned.
3. You didn't upgrade. Transformers upgraded itself. *
4. Your library updates itself. Your code didn't agree.
5. Patch releases are safe. This one moved your floors.
6. Pin it like llama.cpp. Floats break pipelines.
7. Three moves tonight: pin transformers, sleep well. *
8. Your model won't load. The version did it.
9. Unsloth demanded 5.2.0. The cap was 5.5.0.
10. New transformers, same requirements file, different behavior.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Three moves tonight keep your transformers pipeline fixed. Pin it, lock one exact version, or rebuilds pick for you. | 3 moves tonight: pin transformers | Frame 1: the five-word line fills a centered three-row stack inside the safe zone, amber on the word "pin", fully legible at 64 px-plus height. Motion onset at t=0.35s: an amber rule scales in beneath "pin". On "lock one exact version" the word "pin" gets an emphasis punch, text pre-sized to SAFE_W/1.12. On "rebuilds pick for you" the rest of the stack fades dim while "pin" stays bright. Entrances are scale and fade only; five words visible at peak. | hyperframes | centered-stack | 6.6 |
| s02 | explain | Move one: check the version you actually run. One command prints it; the newest is five twenty-one. Unpinned, pip always pulls the newest version. | python -c "import transformers;"|print(transformers.__version__)|-> 5.21.0 | Hard cut to a terminal window in split-compare: command pane major, output pane minor. On "check the version you actually run" the command typewrites in, wrapping to two lines at full text height inside the safe box. On "the newest is five twenty-one" the minor pane fades in showing 5.21.0 in amber with a steady block cursor; the minor word is six characters. One text block animates at a time, typewriter and fade only, six words visible at peak. | hyperframes | split-compare | 8.3 |
| s03 | explain | Move two: read the release notes for moved floors. One patch pushed the loader to torch two point eight. Unsloth's helper package caps it at five point five. | floor torch>=2.8 / ceiling <=5.5.0 | Hard cut to a two-cell manim grid. On "pushed the loader" the left cell fades in: "floor" above "torch>=2.8" with a small amber up-tick. On "caps it at five point five" the right cell scales in: "ceiling" above "<=5.5.0" with a flat amber bar. Entrances staggered so only one block moves at a time; each number is spoken exactly as its cell lands; four words visible at peak; cells hold static to the scene end. | manim | grid | 9.7 |
| s04 | explain | Move three: write the pin, rebuild, rerun one prompt. transformers equals equals five twenty-one in requirements. | transformers==5.21.0 | Hard cut to a requirements.txt editor frame, one line wide. On 'write the pin' a blank amber line rises in place inside the editor. On 'equals equals five twenty-one' the text transformers==5.21.0 typewrites into that line, cursor steady, digits matching the spoken words exactly. On 'rerun one prompt' the editor dims and a small prompt chip fades in beside it; one text block animates at a time, entrances are typewriter and rise only, four words visible at peak. | hyperframes | centered-stack | 6.6 |
| s05 | explain | Pin it like your llama dot cpp build tag; pip solves around it. A pin delays fixes, so schedule the upgrade. | llama.cpp tag | pip pin | Split-compare, two halves. On 'Pin it like your llama dot cpp build tag' the left half fades in: 'llama.cpp tag' over a small numbered tag chip with a pin dot. On 'pip solves around it' the right half rises in place: 'pip pin' over three dim package chips that brighten as one group, connectors drawing once to show the solver working around the locked line. On 'schedule the upgrade' a thin amber calendar tick marks the right chip. Two animation groups maximum, staggered by phrase; no element travels across the frame. | hyperframes | split-compare | 6.9 |
| s06 | payoff_close | Rebuild, rerun the prompt you know. It answers like before, on a version you chose. | known prompt → answer; transformers, pinned | Hard cut to a two-node diagram-flow. On "rerun the prompt you know" the "known prompt" node fades in left; on "answers like before" an amber arrow scales toward the "answer" node, which fades in as the arrow lands. On "a version you chose" the two-word caption "transformers, pinned" fades in beneath, rhyming with frame one's wording, no digits. Final half second: all motion stops and the wordmark settles centered; five words visible at peak; the video ends within a second of the last spoken word. | hyperframes | diagram-flow | 5.2 |

## Notes for review
The drift mechanism ("Unpinned, pip always pulls the newest version") is the load-bearing teaching line; check it first. The trade-off ("A pin delays fixes, so schedule the upgrade") answers the brief's objection; confirm it reads as honest, not hedging. The analogy limit is stated in-scene: a pip pin must satisfy every other package too (the solver beat in s05). Numbers rounded for the ear exactly once: "five twenty-one" for 5.21.0, "five point two" / "five point five" for the floor/ceiling window.
