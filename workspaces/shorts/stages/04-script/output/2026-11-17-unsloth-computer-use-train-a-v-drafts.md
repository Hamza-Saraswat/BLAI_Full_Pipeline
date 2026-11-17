# Drafts: 2026-11-17-unsloth-computer-use-train-a-v

Judge: kimi-k3 blind call, rubric per judge-rubric.md. Winner: A (comparison-ladder), 20 to 17. No grafts.

## Score table
| Row | Draft A (comparison-ladder) | Draft B (how-to-three-moves) |
|-----|------|------|
| 1 Hook | 3 | 2 |
| 2 Payoff timing | 2 | 3 |
| 3 Specificity | 3 | 2 |
| 4 Voice | 3 | 0 |
| 5 Navigation | 2 | 2 |
| 6 Difference | 3 | 3 |
| 7 Repeat test | 3 | 2 |
| 8 Teaching | 3 | 3 |
| Total | 20 | 17 |

## Judge reason
B breaks the one-new-number-at-a-time constraint in "about one hundred seconds on their RTX Pro six thousand, a ninety-six gigabyte card" (three new figures in one breath), zeroing row 4. A wins the margin on row 1 (number plus felt tension inside five words) and row 7 (the rent-the-rare line is repeatable and last).

## Grafts
None. B's hook is ineligible (scores lower on row 1) and B's distinctive material (trigger word, the timed run) is outside A's scope and would break A's number budget.

## Drift found by the judge and resolved
- B: "The paid agents from the chat labs bill every screenshot" generalized Anthropic's billing to OpenAI; and "newer than November fourth" was invented. B did not ship; noted for the retro.
- A: on-screen "train MiniMax-H3-Image at home" sat under the 22 GB QLoRA beat (that figure is the 27B screen-model minimum, not the MiniMax estimate). Fixed before saving: the beat was split and MiniMax-H3-Image got its own scene with accurate narration.

## Draft A in full (winner, as saved)
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|--------------------------|-----------------|--------------|------|--------|-------|
| s01 | hook | The meter says forty messages a month. Your GPU has no meter. You've got a gaming card, and you've watched Claude and ChatGPT drive screens for a fee. Teaching one yourself doesn't take a datacenter. | 40 messages a month, or your GPU. | Frame 1: the hook line 'Forty messages a month, or your own GPU.' in 130 px bold type, centered in the upper t... | hyperframes | split-compare | 10.0 |
| s02 | explain | The meter is the first thing you pay. OpenAI caps its ChatGPT agent at forty messages a month on Plus, then folds it into ChatGPT Work. Hit the cap and the agent stops. | Plus plan: 40 messages a month | then folded into ChatGPT Work | On 'The meter', a small gauge icon rises in place at top center. On 'forty messages a month', a giant '40' sca... | hyperframes | giant-number | 11.4 |
| s03 | explain | Your side has no meter. Unsloth just shipped a computer-use beta, an agent that reads your screen and clicks with your approval. It ships off by default, under permission rules you set. | your card: no meter | Unsloth beta: off by default | Centered stack on dark slate. On 'no meter', the gauge icon fades in with a clean strike-through. On 'Unsloth'... | hyperframes | centered-stack | 11.0 |
| s04 | explain | Then there's what running it costs. Anthropic's computer use tool bills every screenshot it reads as image input. The agent looks, and the meter ticks. Long tasks look a lot. | every screenshot = billed image input | the meter ticks | Manim diagram, left to right, kept clear of the right 120 px. On 'Anthropic', a node labeled 'screenshot' fade... | manim | diagram-flow | 10.3 |
| s05 | explain | Your side downloads once. The best-rated open screen model is a GGUF, a packed file that runs on your own hardware. It takes about nineteen gigabytes of memory, vision file included. After that, looking is free. | GGUF: one packed file | about 19 GB, once | On 'downloads once', a single down-arrow icon rises in place at top center. On 'GGUF', a file card labeled 'GG... | hyperframes | giant-number | 12.4 |
| s06 | explain | Using it feels like a new hire leaning over your shoulder. It sees only the screen, it moves your mouse, and it asks before it clicks. Unlike a hire, it re-reads every screenshot from scratch, so long jobs can drift. | sees the screen, moves the mouse | asks before it clicks | Manim loop diagram in the safe zone. On 'new hire', a simple figure outline fades in, leaning over a monitor f... | manim | diagram-flow | 13.8 |
| s07 | explain | The full job needs twenty-two gigabytes of VRAM, your card's own memory, at minimum. And the add-on is yours to keep. | 22 GB VRAM minimum | adapter yours | On 'never hand you their weights', a cloud icon with a small lock fades in at left, labeled 'their weights'. O... | manim | giant-number | 7.2 |
| s08 | explain | MiniMax's new image model is the proof. Its weights download, and this week's Unsloth release trains them. | MiniMax-H3-Image: open | trains in Unsloth | On 'never hand you their weights', a cloud icon with a small lock fades in at left, labeled 'their weights'. O... | manim | timeline | 5.9 |
| s09 | explain | The full job needs twenty-two gigabytes of VRAM, your card's own memory, at minimum. And the add-on is yours to keep. | 22 GB VRAM minimum | adapter yours | On 'never hand you their weights', a cloud icon with a small lock fades in at left, labeled 'their weights'. O... | manim | grid | 7.2 |
| s10 | explain | One honest catch. It's a beta, and it behaves like one. In Unsloth's own test, two of six runs misread the screen or quit. It only drives apps on your own machine. | it's a beta: some runs misread | local apps only | Centered stack. On 'honest catch', a small caution triangle fades in at top center. On 'behaves like one', a c... | hyperframes | centered-stack | 11.0 |
| s11 | payoff_close | The meter, the memory, the weights. Rent the rare jobs to the cloud. Run the routine ones on your own GPU, with Unsloth. | rare: rent it | routine: run it on your GPU | Split compare that rhymes with frame 1: two cards side by side, left labeled 'rent it', right labeled 'run it ... | hyperframes | split-compare | 7.9 |

## Draft B in full
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|--------------------------|-----------------|--------------|------|--------|-------|
| s01 | hook | About nineteen gigabytes of memory. That's the whole agent, a vision model that reads screens and clicks. You've got a gaming card and assumed training takes a datacenter. | 19 GB | Nineteen gigabytes. That's the whole agent. | Frame 1: near-black background, giant '19 GB' digits at 300 px in the upper third, hook caption 'Nineteen giga... | manim | giant-number | 9.7 |
| s02 | explain | The paid agents from the chat labs bill every screenshot as image input. Unsloth's beta runs the same trick locally, computer use, meaning the model watches your screen and drives your mouse. | Cloud bills every screenshot | Unsloth: local, off by default | Split screen fades in on 'paid agents': left panel shows a cloud invoice with a meter ticking upward beside a ... | hyperframes | split-compare | 11.0 |
| s03 | explain | Think new hire over your shoulder, except it re-reads every screenshot, so long tasks drift. | new hire over your shoulder | Split screen fades in on 'paid agents': left panel shows a cloud invoice with a meter ticking upward beside a ... | hyperframes | centered-stack | 5.2 |
| s04 | explain | Move one: install the Unsloth beta on your machine. Clone the repo, run the local installer, and pick the release newer than November fourth. It pulls the screen model too, in GGUF, a compressed format that fits big models on one card. | clone the repo | run the local installer | On 'Move one', a horizontal three-node flow fades into the top half: folder icon, gear icon, checkmark. On 'Cl... | hyperframes | diagram-flow | 14.5 |
| s05 | explain | Move two: teach it your style with captioned images. Gather about sixty images of one style, and write a caption for each. Every caption carries your trigger word, a made-up word that summons the style later. | 60 captioned images, one style | trigger word in every caption | On 'Move two', a six by four grid of thumbnails in one consistent style, ink-wash cats, fades into the center ... | hyperframes | grid | 12.4 |
| s06 | explain | Move three: train the LoRA and deploy it. A LoRA is a small add-on that learns one skill while the base model stays frozen. | Move three: train it | LoRA: add-on, frozen base | On 'Move three', a training settings panel rises in place: model name row, a 'steps: 150' field, and a Start t... | hyperframes | centered-stack | 8.3 |
| s07 | explain | Leave the default one hundred fifty steps and click Start training. Training peaks at about twenty-four gigabytes of memory, by Unsloth's estimate. | Move three: train a MiniMax-H3-Image LoRA | On 'Move three', a training settings panel rises in place: model name row, a 'steps: 150' field, and a Start t... | hyperframes | timeline | 7.6 |
| s08 | explain | Unsloth timed that run at about one hundred seconds on their RTX Pro six thousand, a ninety-six gigabyte card. Yours will be slower, and that's fine. | about 100 seconds | RTX PRO 6000 · 96 GB card | On 'one hundred seconds', giant '100 s' numerals scale into the center over a stopwatch ring that sweeps one c... | manim | giant-number | 9.0 |
| s09 | foreshadow | Two honest caveats. The memory peak is an estimate, measured on a ninety-six gigabyte card. In Unsloth's own test, the screen agent misread or quit on two of six receipt runs. The agent's flakiness is real. Your training recipe is separate. | memory peak is an estimate | agent: 2 of 6 runs stumbled | Two stacked cards fade in on 'caveats'. Top card, on 'estimate': a memory gauge with a dotted outline and the ... | hyperframes | split-compare | 14.1 |
| s10 | payoff_close | Then click Deploy to Create, prompt with your trigger word, and watch. The image that comes back carries your style, trained in Unsloth, on the card you already own. | Deploy to Create | prompt: zynko, your trigger word | On 'Deploy to Create', a clean Create page rises in place: one prompt box, one generate button, nothing else. ... | hyperframes | centered-stack | 10.0 |

## What the losing shape would have needed
B's how-to needed the RTX PRO 6000 sentence split into separate breaths, one number each; that single pile-up zeroed its voice row. It also needed the hook's tension inside five words and tighter fact discipline (Anthropic alone bills per screenshot; no invented release dates).
