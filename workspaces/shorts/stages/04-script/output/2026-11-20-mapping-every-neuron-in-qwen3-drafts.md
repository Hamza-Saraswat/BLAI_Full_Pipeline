---
slug: 2026-11-20-mapping-every-neuron-in-qwen3
stage: 04-script
generated_at: 2026-11-20
judge: kimi-k3 (blind, rubric per judge-rubric.md)
---

# Drafts and scores: 2026-11-20-mapping-every-neuron-in-qwen3

## Draft A (worked-example) -- WINNER 21
**s01 (hook, centered-stack, 9.3s)**
Narration: Your Qwen isn't a mystery anymore. Every neuron inside it got mapped. You run it in Ollama or LM Studio, and when it does something weird, you shrug and re-prompt.
On-screen: Qwen's neurons: mapped | Ollama · LM Studio · shrug → re-prompt

**s02 (explain, diagram-flow, 14.1s)**
Narration: Inside, your Qwen is a stack of identical layers. Every word it writes climbs through every layer before the next word appears. Each layer is packed with neurons, the small calculators inside it. Until now, that whole climb was invisible to you.
On-screen: a tall stack of identical layers | every word climbs them all

**s03 (explain, centered-stack, 10.3s)**
Narration: That map is built on one rude little move. A push means adding a fixed amount to one neuron's number at every word. No prompt. No fine-tune. One number, changed.
On-screen: push = +constant at every word | no prompt · no fine-tune

**s04 (explain, split-compare, 15.5s)**
Narration: Isn't poking a neuron just brain damage? Often, yes. A verified switch is a push that changes exactly one behaviour, like which language your copy answers in. It must beat a panel of matched random neurons and keep working on questions it has never seen.
On-screen: random pushes barely move it | a switch moves one behaviour

**s05 (explain, grid, 15.5s)**
Narration: Fermion Research ran that test on every neuron. Picture a mixing desk: four hundred forty-two thousand faders, one per neuron. About one fader in a hundred does one clear job. The rest do nothing you can name. One hundred thirty-two faders are verified switches.
On-screen: 442,368 faders | 132 verified switches

**s06 (explain, giant-number, 11.7s)**
Narration: One fader is labelled German. Unpushed, it writes German seven percent of the time. Pushed a single notch, it answers in German a hundred percent of the time. A couple of notches later, it babbles.
On-screen: L5.N5224 German | 7% to 100% in one notch

**s07 (explain, diagram-flow, 6.2s)**
Narration: That's the limit: faders are independent and linear, neurons interact. Push past the sweet spot and the whole desk squeals.
On-screen: faders: independent | neurons: they interact

**s08 (explain, split-compare, 13.4s)**
Narration: Now the honest catch, because a cute German trick is not understanding. These switches set who is speaking and how. None of them sets whether the speaker is telling the truth. The map admits what it did not find.
On-screen: switches set: who & how | truthfulness: no switch found

**s09 (foreshadow, timeline, 10.7s)**
Narration: And no, this is not a chat-party trick. The same switches still fire in the raw pretrained model. The switch-hunting framework is promised, not shipped. The atlas itself is public tonight.
On-screen: still fires pre-trained | framework: promised | atlas: public

**s10 (payoff_close, centered-stack, 7.9s)**
Narration: Your black box just grew a labelled panel. The next time Qwen does something weird, you don't re-prompt it. You look it up.
On-screen: you look it up | Fermion Research

## Draft B (myth-bust) -- 20
**s01 (hook, giant-number, 8.3s)**
Narration: Four hundred forty-two thousand neurons. One of them speaks German. You run Qwen locally, and when it does something weird, you shrug and re-prompt.
On-screen: 442,368 neurons. One speaks German.

**s02 (foreshadow, split-compare, 13.8s)**
Narration: The belief goes like this: a local model is a black box. You cannot point at the part that does a thing; you can only re-prompt and hope. Fermion Research just put that belief on a bench and measured it.
On-screen: the belief: local model = black box

**s03 (explain, diagram-flow, 13.8s)**
Narration: A neuron is one of the small calculators inside a layer. Your Qwen is a tall stack of layers, and every word climbs through all of them. A push adds a fixed amount to one neuron's number at every word.
On-screen: neuron = small calculator in a layer

**s04 (explain, timeline, 11.0s)**
Narration: One neuron leans German. Unpushed, it writes German seven percent of the time. Pushed a single notch, it answers in German a hundred percent of the time. Two notches later, it babbles.
On-screen: 7% German | one notch: 100%

**s05 (explain, centered-stack, 14.5s)**
Narration: That is a verified switch: one push that moves exactly one behaviour. It must beat thirty matched random neurons and survive questions it never saw. The atlas lists a hundred thirty-two of them. The box, it turns out, has a labelled panel.
On-screen: verified switch = one behaviour | 132 found

**s06 (explain, grid, 14.5s)**
Narration: Picture a city of four hundred forty-two thousand buildings. A hundred thirty-two carry verified plaques; a slim scatter carry scribbled notes. Unlike a paper map, this one is not read-only: touch a building and the city changes. And most buildings stay blank.
On-screen: city of 442,368 buildings | 132 plaques

**s07 (explain, split-compare, 14.5s)**
Narration: The switches set who is speaking and how. They still fire in the raw pretrained model, so this is no chat trick. None sets whether the speaker is telling the truth. Most neurons do nothing clear; the middle layers stay fog.
On-screen: who speaks + how | honesty: none found

**s08 (explain, grid, 10.7s)**
Narration: So the honest catch: a hundred thirty-two switches is a small map, and it serves no tokens tonight. The steering framework is promised, not shipped; the atlas itself is readable tonight.
On-screen: 132 switches | framework: promised | atlas: open

**s09 (payoff_close, centered-stack, 10.0s)**
Narration: But next time your model does something weird, you get to point, not shrug. Most of the box is still dark, but now you own a map of its dials.
On-screen: point, don't shrug | you own the map

## Scores: draft A
| Row | Score | Note |
|-----|-------|------|
| row1_hook | 3 | 'Your Qwen isn't a mystery anymore' names the product in word two and the tension (the shrugging viewer's black box) inside five words; 'Every neuron inside it got mapped' pays it  |
| row2_payoff | 3 | The hook's promise (end of mystery) is paid by sentence two at ~3s with the total-map claim, which is the thing the hook promised. Deeper artifacts (132, German) arrive later, but  |
| row3_specificity | 2 | Most beats earn a specific and the headline numbers land hard, but 'from seven percent German replies to a hundred percent' crams two new numbers into one sentence, and total spoke |
| row4_voice | 2 | Second person throughout, terms defined in-breath ('neurons, the small calculators'), no em dashes, no hype, and 'Often, yes.' is a model wry beat. Held at 2 because the 7%-to-100% |
| row5_navigation | 3 | No positional labels; nothing to deletion-test. Every transition names what changed ('That map is built on one rude little move', 'That's the limit', 'Now the honest catch'), and t |
| row6_difference | 2 | Worked-example repeats 11-15's structure and the NC hook echoes 11-16, but against the last two scripts (short classics: how-to-three-moves, contrarian-take) the shape, opening rhy |
| row7_repeat | 3 | The payoff line is the repeatable one and it is the last thing heard: 'You look it up.' 'Your black box just grew a labelled panel' is a second quotable line one sentence earlier,  |
| row8_teaching | 3 | The mechanism is shown concretely (push = one number at every word; switch must beat matched randoms) and the analogy's limit is taught and tied to evidence (faders independent, ne |
| **total** | **21** | |

## Scores: draft B
| Row | Score | Note |
|-----|-------|------|
| row1_hook | 2 | 'Four hundred forty-two thousand neurons' names a number but no product and no tension; the intrigue ('One of them speaks German') lands at words 6-10, outside the first five, and  |
| row2_payoff | 3 | Fairness note applied: scored from the break, not the s02 myth statement. The break lands in the hook itself at ~3.4s ('One of them speaks German'), a concrete promised artifact by |
| row3_specificity | 2 | Per-sentence number discipline is exemplary (7% and 100% split across sentences, 132 callbacks are not new spends), but five new quantities still exceed the three-number band, and  |
| row4_voice | 3 | Clean second person, terms defined in-breath, no em dashes, sentence discipline visibly better than A's on the money beat, and 'The box, it turns out, has a labelled panel' is a wr |
| row5_navigation | 3 | No positional labels; transitions carry content ('That is a verified switch', 'So the honest catch'), and the order is load-bearing (the demo must precede the switch definition it  |
| row6_difference | 2 | Myth-bust repeats 11-16's shape and the number-shock open echoes 11-17, but against the last two scripts the shape, rhythm, and landing are all different; 110s breaks the short-cla |
| row7_repeat | 2 | The most repeatable line in the draft, 'One of them speaks German', is the hook, not the payoff; the close ('Most of the box is still dark, but now you own a map of its dials') is  |
| row8_teaching | 3 | Teaches the mechanism concretely and adds a genuine why A lacks: the atlas is causal, not correlational ('Unlike a paper map... touch a building and the city changes'), and the pla |
| **total** | **20** | |

## Winner
Draft A, 21 to 20. The graft below was applied before saving.

## Grafts
- From B into A's s06: replace "One notch takes your copy from seven percent German replies to a hundred percent." with "Unpushed, it writes German seven percent of the time. Pushed a single notch, it answers in German a hundred percent of the time." Reason: B says the winner's weakest beat better; the two numbers are spent one per sentence, no new numbers, structure and person unchanged.

## What the losing shape would have needed
The verdict's loser_needs field was truncated at the model's 32k completion cap; the fragment: the myth-bust needed a hook that put the product and the viewer's tension inside the first five words instead of spending them on a bare digit, and it needed its close to be the earworm ("point, not shrug" stranded in the penultimate sentence while the flatter "map of its dials" closed).
