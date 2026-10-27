---
slug: 2026-10-27-transformers-v5-21-what-actual
stage: 04-script
generated_at: 2026-10-27T12:40:00Z
---

# Drafts: 2026-10-27-transformers-v5-21-what-actual

Both drafts written blind on kimi-k3 (one llm_call each) from the same packet inputs; both passed the validator (0 blockers) and all nine eval gates before judging.

# Verdict
WINNER: draft-B -- tied 18-18 on points, and the tiebreak goes to row 6, where B's how-to shape, count-promise hook, and quiet consequence landing are new on all three axes while A closes on the same aphorism move as the recent run; B also passes every hard constraint while A spends two new numbers in one sentence.

# Score table
| # | Row | A | B | Justification |
|---|-----|---|---|---------------|
| 1 | Hook | 3 | 2 | A: "You didn't upgrade. Transformers upgraded itself." names the product and a felt tension inside five words. B: names transformers, but the first five words ("Three moves tonight keep your") carry no tension; the stakes ("rebuilds pick for you") arrive a sentence late. |
| 2 | Payoff timing | 2 | 2 | A: the mechanism line "pip always pulls the newest version" completes around second five, inside eight. B: the hook previews the fix by second four, but the first concrete move (the version command) lands around second seven to nine; either reading is a 2. |
| 3 | Specificity without cramming | 2 | 2 | A: real specifics (torch two point eight, the five point two / five point five window, the five point twenty-one pin) but s04 spends two new numbers in one sentence. B: clean one-number-per-sentence discipline, but drops the five point two floor and visually pairs a torch floor with a transformers ceiling as if they were one window. |
| 4 | Voice | 0 | 3 | A: breaks hard constraint 5 (two new numbers in one breath, s04), says "unsloth-zoo" bare against constraint 3, and "Everyone assumes" brushes the person rule. B: clean second person, appositives done right ("Unsloth's helper package", "Pin it, lock one exact version"), and "pip solves around it" is a wry beat that lands on the thing and is not explained. |
| 5 | Navigation | 3 | 2 | A: no labels; every transition contradicts or answers the previous beat and the order is load-bearing. B: labels are legal (a real process, three of them, each naming the action, count opens in the hook and closes at move three) and the action names carry content, but enumeration still does some mechanical lifting. |
| 6 | Difference | 2 | 3 | A: contrarian shape and a number-free hook are new, but the roughly thirty-seven second length and the maxim close echo the run's aphorism landings (10-24, 10-25). B: how-to shape, count-promise opening, and a quiet consequence landing ("on a version you chose") differ from the last five on shape, rhythm, and landing. |
| 7 | Repeat test | 3 | 2 | A: "Upgrade on purpose, never by accident" is the repeatable line and it is the last thing heard. B: "or rebuilds pick for you" is repeatable but lives in the hook; the actual closer is softer. |
| 8 | Teaching | 3 | 2 | A: states the drift mechanism (unpinned pip pulls newest) plus a floor case and a ceiling case; the viewer can predict the next silent-rebuild breakage. B: teaches the procedure and shows one moved floor concretely, but never says why versions drift, so prediction stays shallow. |

Totals: A 18, B 18. Tie broken by row 6: B.

# Grafts
- Hook graft: not taken. A's hook scores one point higher than B's on row 1; the rule requires at least two.
- Graft 1: A's "Unpinned, pip always pulls the newest version." inserted into B's s02 after "the newest is five twenty-one." Reason: B gestures at drift with "rebuilds pick for you" but never states the mechanism, which is exactly what held its row 8 to 2; A's line is the mechanism in nine words, adds no numbers, keeps second person, and leaves the three-move count untouched. Cost: about three seconds on s02.
- Graft 2: A's "A pin delays fixes, so schedule the upgrade." inserted into B's s05 before the payoff sentence. Reason: the voice rules require the honest trade-off when one exists and B never states one; A's line is the brief's objection answered in eight words, and placing it before "It answers like before, on a version you chose" keeps the payoff last per hard constraint 7. No new numbers; the move structure is untouched.
- A's closing maxim was not grafted: swapping closers would force a rewrite of s05's lead-in and visual, which the grafting rules forbid.

# Loser's path
A needed to split the five point two / five point five window across two sentences, which would have cleared hard constraint 5, moved row 4 off zero, and won outright. It also needed a landing that was not another aphorism, because the ledger's recent closes are already maxims and that is what capped row 6 at 2 and handed the tie to B.

## Draft A (contrarian-take) in full

# Working title
Transformers drift: pin your version

# Promise
After about thirty-five seconds you can pin transformers to an exact version on purpose and say why that pin matters.

# Music mood
steady-build

# Analogy
vehicle: pinning a llama.cpp build tag, a numbered artifact you choose and keep / mapping: the discipline you already have on the llama.cpp side applied to the Python side, a pinned pip line instead of a float that drifts / limit: a pip pin is one line inside a dependency solver that must satisfy every other package, stated in-scene ("except a pip pin must satisfy every other package too")

# Script table
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|---|---|---|---|---|---|---|---|
| s01 | hook | You didn't upgrade. Transformers upgraded itself. Unpinned, pip always pulls the newest version. | You didn't upgrade. Transformers did. | Frame 1: centered two-line stack, "You didn't upgrade." over "Transformers did.", both fully legible, amber on the second line. Motion onset at t=0.30s: the second line scales 1.0 to 1.06 and settles. On "Transformers upgraded itself", an amber underline fades in beneath it. On "Unpinned, pip always pulls", staged swap (hard cut) to a mono line "pip install transformers" with a steady cursor; on "newest version" a small tag reading "newest" fades in above the line. | hyperframes | centered-stack | 5.2 |
| s02 | explain | Everyone assumes a patch bump is safe; if it breaks, you just upgrade. | Patch bump: safe. Upgrade: fixes it. | Split-compare, two halves staging the consensus. On "Everyone assumes", the left half fades in: "Patch bump" over an amber chip "safe". On "if it breaks, you just upgrade", the right half rises in place: "Upgrade" over a chip "fixes it". On the final word "upgrade", a thin amber strike draws through both chips after both halves are static. One text block animates at a time; strikes are the only second animation. | hyperframes | split-compare | 4.5 |
| s03 | explain | One patch raised the minimum: loading big models now demands torch two point eight. | One patch release. torch >= 2.8 | Giant-number composition. On "One patch raised the minimum", a small top label "one patch release" fades in. On "loading big models", the label hard-cuts to "model loading" (staged swap, no dissolve). On "torch two point eight", the giant line "torch >= 2.8" scales from 0.9 to 1.0 and holds; nothing else moves for the rest of the scene. The digits match the spoken floor. | hyperframes | giant-number | 4.8 |
| s04 | explain | Upgrading hits a ceiling. An Unsloth model demanded transformers five point two or newer; unsloth-zoo capped it at five point five. | model needs >= 5.2.0 zoo caps <= 5.5.0 | Split-compare, floor versus ceiling. On "demanded transformers five point two or newer", the left block fades in: "model needs" over ">= 5.2.0". On "unsloth-zoo capped it at five point five", the right block fades in: "zoo caps" over "<= 5.5.0". On the held beat after the sentence, two short amber arrows rise in place pointing into the gap between the blocks, marking the narrow window. At most two elements animate at once; arrows wait until both blocks are static. | hyperframes | split-compare | 7.2 |
| s05 | explain | You already pin llama.cpp build tags. Same idea, except a pip pin must satisfy every other package too. | llama.cpp tag pip pin others | Diagram-flow. On "You already pin llama.cpp build tags", a left node labeled "llama.cpp tag" fades in with a small pin dot holding it. On "Same idea", a center node "pip pin" rises in place. On "must satisfy every other package too", three dim nodes labeled "others" around it brighten as one group while thin connectors draw once, showing the pin living inside a solver. Two animation groups maximum, staggered by phrase; no node travels across the frame. | manim | diagram-flow | 6.2 |
| s06 | payoff_close | Pin what works: transformers equals five point twenty-one in the requirements file. A pin delays fixes, so schedule the upgrade. Upgrade on purpose, never by accident. | transformers==5.21.0 Upgrade on purpose. | Centered-stack. On "transformers equals five point twenty-one", a mono requirements-file window fades in carrying the single amber line "transformers==5.21.0". On "A pin delays fixes, so schedule the upgrade", a small calendar chip reading "upgrade: scheduled" fades in below the line. On "Upgrade on purpose", hard cut to the payoff stack "Upgrade on purpose." centered, mirroring the frame-1 composition; the wordmark settles in the final half second with no further narration. | hyperframes | centered-stack | 9.0 |

## Draft B (how-to-three-moves) in full, pre-graft

# Working title
Transformers pin: three moves, no drift

# Promise
After about thirty-five seconds you can pin transformers to an exact version in your requirements file, rebuild, rerun a known prompt, and say why the pin matters.

# Music mood
steady-build

# Analogy
vehicle: pinning a llama.cpp build tag / mapping: a numbered artifact you choose and keep, the same discipline moved from the binary side to the Python side / limit: a pip pin is one line inside a solver that must satisfy other packages, stated in-script as "pip solves around it"

# Script table

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Three moves tonight keep your transformers pipeline fixed. Pin it, lock one exact version, or rebuilds pick for you. | Three moves tonight: pin transformers | Frame 1: the five-word line fills a centered three-row stack inside the safe zone, amber on the word "pin", fully legible at 64 px-plus height. At t=0.35s an amber rule scales in beneath "pin". On "lock one exact version" the word "pin" gets an emphasis punch, text pre-sized to SAFE_W/1.12. On "rebuilds pick for you" the rest of the stack fades dim while "pin" stays bright. Entrances are scale and fade only; five words visible at peak. | hyperframes | centered-stack | 6.6 |
| s02 | explain | Move one: check the version you actually run. One command prints it; the newest is five twenty-one. | python -c "import transformers; print(transformers.__version__)" → 5.21.0 | Hard cut to a terminal window in split-compare: command pane major, output pane minor. On "check the version you actually run" the command typewrites in, wrapping to two lines at full text height inside the safe box. On "the newest is five twenty-one" the minor pane fades in showing 5.21.0 in amber with a steady block cursor; the minor word is six characters. One text block animates at a time, typewriter and fade only, six words visible at peak. | hyperframes | split-compare | 5.9 |
| s03 | explain | Move two: read the release notes for moved floors. One patch pushed the loader to torch two point eight. Unsloth's helper package caps it at five point five. | floor torch>=2.8 / ceiling <=5.5.0 | Hard cut to a two-cell manim grid. On "pushed the loader" the left cell fades in: "floor" above "torch>=2.8" with a small amber up-tick. On "caps it at five point five" the right cell scales in: "ceiling" above "<=5.5.0" with a flat amber bar. Entrances staggered so only one block moves at a time; each number is spoken exactly as its cell lands; four words visible at peak; cells hold static to the scene end. | manim | grid | 9.3 |
| s04 | explain | Move three: write the pin, rebuild, rerun one prompt. transformers equals equals five twenty-one, written in requirements. Pin it like your llama dot cpp build tag; pip solves around it. | transformers==5.21.0 / llama.cpp build tag | Hard cut to a requirements.txt editor frame. On "write the pin" a blank line rises in place; on "equals equals five twenty-one" the text transformers==5.21.0 typewrites in amber. On "llama dot cpp build tag" a small sharp-cornered chip fades in reading "llama.cpp build tag"; on "pip solves around it" the chip dims while the pin line stays bright. Fade and typewriter only, five words visible at peak, the spoken digit string matches the typed one. | hyperframes | centered-stack | 10.3 |
| s05 | payoff_close | Rebuild, rerun the prompt you know. It answers like before, on a version you chose. | known prompt → answer; transformers, pinned | Hard cut to a two-node diagram-flow. On "rerun the prompt you know" the "known prompt" node fades in left; on "answers like before" an amber arrow scales toward the "answer" node, which fades in as the arrow lands. On "a version you chose" the two-word caption "transformers, pinned" fades in beneath, rhyming with frame one's wording, no digits. Final half second: all motion stops and the wordmark settles centered; five words visible at peak; the video ends within a second of the last spoken word. | hyperframes | diagram-flow | 5.2 |
