---
slug: 2026-09-08-mistral-raises-3b-euro-for-ope
stage: 04-script
generated: 2026-09-08
judge: kimi-k3 (blind, one packet)
winner: B (comparison-ladder)
---

# Drafts and scores: Mistral raises 3B euro for open-weight frontier AI

Two blind drafts, two structures (contrarian-take vs comparison-ladder), two hook patterns (number-shock vs named-contradiction). Both cleared validator (0 blockers) and all hard eval gates before judging.

## Draft A (contrarian-take, hook: number-shock)

TITLE: Mistral's EUR 3B open-weight pledge is already half true
PROMISE: After about 35 seconds you can say which half of Mistral's open-weight pledge already runs on your hardware tonight, and which half was never promised to it.

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | Three billion euros, and the open-weight pledge is already half true. You run open models on a gaming PC or Mac. | EUR 3B: the pledge is half true | Giant EUR 3B numeral legible at frame 1; scales up from 0.30 s on "three billion euros"; caption fades in on "already half true". | hyperframes | giant-number | 6.6 |
| s02 | foreshadow | One camp: nothing changes at home. The other: frontier models for everyone. Both wrong. | Nothing changes at home / Frontier models for everyone | Split screen; left panel fades in on "nothing changes", right on "frontier models"; both dim to gray on "Both wrong". | hyperframes | split-compare | 4.4 |
| s03 | explain | Open-weight: the files are published, you run them. The whole Mistral Three generation is Apache two point oh, free for commercial use. A three-billion-parameter Ministral is downloadable tonight. | Apache 2.0: free for commercial use / 3B Ministral: downloadable tonight | License card fades in on "Apache two point oh"; staged swap on "downloadable tonight" to a download glyph with the 3B label. | hyperframes | centered-stack | 8.8 |
| s04 | explain | The other half is datacenter-only. Large Three holds six hundred seventy-five billion total parameters. Compressed, it still targets an eight-GPU datacenter node. | 675B total parameters / 8xA100, 8xH100 node | Box label fades in on "Large Three"; parameter line draws under it; eight GPU rectangles rise in place as one group on "eight-GPU". | manim | diagram-flow | 6.9 |
| s05 | explain | On some benchmarks, Fortune puts it eighteen months behind OpenAI. And the pledge names no model and no date, from a company worth more than twenty-one billion euros. | 18 months behind, some benchmarks / No model, no date | Timeline fades in on "eighteen months" with dots for OpenAI and Mistral; dims as the "no model, no date" card fades in. | hyperframes | timeline | 6.9 |
| s06 | payoff_close | Mistral's bet: downloadable weights stay worth having. Your half downloads tonight. | Your half downloads tonight | Text rises in place on "downloads tonight"; wordmark settle with the EUR 3B motif echoing frame 1. | hyperframes | centered-stack | 3.4 |

Writer notes: Fortune's "on some benchmarks close to levels OpenAI achieved a year and a half ago" softened to "eighteen months behind" with the qualifier kept after an orchestrator fix; "fits your gaming GPU" (untraceable in the brief) replaced with "downloadable tonight". No analogy: each candidate's limit clause would have eaten the honesty beat.

## Draft B (comparison-ladder, hook: named-contradiction) -- WINNER

TITLE: Mistral tonight: Small 4 runs, Large 3 waits
PROMISE: After about 35 seconds you can repeat one rule for which Mistral model runs on your own hardware and which one needs a datacenter.

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | You can already run Mistral tonight. Just not the six hundred seventy-five billion one. | Run Mistral tonight. Not 675B. | Frame 1: two model cards; Small 4 scales in bright from 0.30 s on "run Mistral tonight"; Large 3 fades in greyed on "six hundred seventy-five billion". | hyperframes | split-compare | 4.4 |
| s02 | foreshadow | You run open models on a gaming PC or Mac. Mistral just raised three billion euros promising open weights, published files you run yourself. | EUR 3B for open weights | Desktop and laptop fade in on "gaming PC or Mac"; EUR 3B figure rises in place on "three billion euros"; download arrow lands on "published files". | hyperframes | giant-number | 7.5 |
| s03 | explain | Both are Apache two point oh, a license allowing free commercial use. | Apache 2.0, both models | Both cards return; license tag scales in on "Apache two point oh", bridging the two cards. | hyperframes | split-compare | 3.8 |
| s04 | explain | Both are mixtures of experts, an office lighting only the rooms in use, though you own the building. Small four lights six and a half billion parameters per word. | MoE: lit rooms, owned building / Small 4: 6.5B per word | Floor-plan grid fades in with a few rooms lit; Small 4 label rises with 6.5B beside a mostly-dark Large 3 floor. | manim | diagram-flow | 8.1 |
| s05 | explain | Now the totals. Small four, one hundred nineteen billion parameters, runs on your box. The six hundred seventy-five billion one wants eight datacenter GPUs. | 119B: your box / 675B: 8 datacenter GPUs | Small 4 card settles onto the desktop tower on "one hundred nineteen billion"; server rack fades in beside Large 3 on "eight datacenter GPUs". | hyperframes | split-compare | 7.5 |
| s06 | payoff_close | So the rule: fits your GPU, Small four. Needs a datacenter, Large three. | Fits your GPU: Small 4 | Small 4 card settles onto the desktop on "fits your GPU"; two-card frame rhymes with frame 1; wordmark settle, no further motion. | hyperframes | centered-stack | 3.4 |

Writer notes: "single 8xA100 or 8xH100 node" softened to "eight datacenter GPUs" for breath; screen keeps the verbatim node line. Orchestrator fix: "Large three lights forty-one billion" cut to stay inside the five-number cap (the mechanism stays: lit rooms vs owned building). The office analogy carries the brief's limit clause ("though you own the building"). The 256k context number was cut to stay inside 38 seconds.

## Judge score table (kimi-k3, blind)

| Row | A (contrarian-take) | B (comparison-ladder) |
|-----|-----|-----|
| 1 Hook | 3 | 3 |
| 2 Payoff timing | 2 | 1 |
| 3 Specificity without cramming | 3 | 3 |
| 4 Voice | 3 | 3 |
| 5 Navigation | 2 | 3 |
| 6 Difference | 1 | 2 |
| 7 The repeat test | 2 | 3 |
| 8 Teaching | 2 | 3 |
| TOTAL | 18 | 21 |

Winner: B by 3 points. Grafts: none.

What the losing shape would have needed (judge, two sentences): The contrarian-take needed to pay its "which half" promise faster after the break and to end on a landing that did not rhyme with yesterday's "so tonight pull" close. It also needed the middle rung and the active-versus-total mechanism, so the viewer could place any future Mistral model rather than only the two poles it named.
