---
slug: 2026-11-17-unsloth-computer-use-train-a-v
format: smooth-explainer
structure: comparison-ladder
style_pack: halftone
value_types: TEACHES,EQUIPS
promise: after this Short you can decide, with numbers, whether a screen agent belongs in the cloud or on the card you already own.
target_duration_s: 105
brief: 2026-11-17-unsloth-computer-use-train-a-v-brief.md
drafts: 2026-11-17-unsloth-computer-use-train-a-v-drafts.md
---

# Unsloth computer use vs the cloud meter

## Decisions
- Structures tried: comparison-ladder (draft A) vs how-to-three-moves (draft B). The hub's ideation-time structure (worked-example) was rotation-blocked: the ledger's last two are worked-example (2026-11-15) and myth-bust (2026-11-16). Judge scored A 20, B 17; A wins. No grafts (B's hook ineligible; B's distinctive material would break A's number budget).
- Hook: candidate 1, decision pattern ("40 messages a month, or your GPU."), cleared the last two ledger hook patterns (situation, named-contradiction); frame-1 text tightened to seven words.
- Post-judge fixes: the judge flagged on-screen drift (MiniMax name under the 22 GB QLoRA beat); fixed by splitting that beat and giving MiniMax-H3-Image its own scene with accurate narration ("MiniMax's new image model"; the hyphenated exact name stays on screen, never spoken, because the digit 3 is not speakable).
- Gates: validator 0 blockers, 1 advisory (10 hashtags: the storyboard schema requires 8-12, the package stage narrows to 2-3 for upload). eval_short gate1_ready true, failures none; entity_spend soft advisory 0.13 vs 0.5 kept with reason: the brief carries 21 extracted entities and a Short that spent half of them would be a changelog read; both top-2 entities (Unsloth, MiniMax-H3-Image) are present. sameness ok, 5 comparisons, 0 violations. Normalizer scenes_changed 7 (digits and model tokens expanded for TTS).

## Hook candidates
1. Forty messages a month, or your own GPU. * (pick, draft A, decision)
2. Nineteen gigabytes. That's the whole agent. * (pick, draft B, number-shock)
3. You've got the card. Now teach it to click.
4. Anthropic bills every screenshot. Your GPU doesn't.
5. Train a vision agent tonight, on the card you own.
6. Your GPU already watches the screen. Now it can act.
7. Stop renting your agent by the message.
8. 19 GB in, agent out.
9. The datacenter myth, minus the datacenter.
10. LoRA: one skill bolted onto a frozen model, tonight.

## Script
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

## Notes for review
- The three spoken numbers are 40 messages a month, about 19 GB of memory, 22 GB of VRAM; each is verbatim from the brief and rounded nowhere.
- The two-of-six reliability line is Unsloth's own receipts test; the analogy's limit (re-reads every screenshot, long tasks drift) is stated in the same beat.
- The payoff line "Rent the rare jobs to the cloud. Run the routine ones on your own GPU." is the repeatable one and the last thing spoken.
