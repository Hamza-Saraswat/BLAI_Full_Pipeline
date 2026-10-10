# Drafts: 2026-10-10-aleph-alpha-kolibri-1m-context

Judge: kimi-k3, blind, rubric 8 rows x 3. Both drafts passed all machine gates before judging.

## Draft A (news-react-so-what, hook: named-contradiction)
| Scene | Role | Narration | On-screen | Layout | Est s |
|-------|------|-----------|-----------|--------|-------|
| s01 | hook | Kolibri promises a million tokens. Its own card says don't. | A million tokens isn't the whole story | centered-stack | 3.4 |
| s02 | foreshadow | A week of million-token headlines, your gaming PC. Aleph Alpha, a German enterprise AI shop, shipped open weights, yours to keep. | Million-token headlines, all week | Aleph Alpha: open weights, yours to keep | split-compare | 7.6 |
| s03 | explain | Your graphics card stops deciding. It's a mixture of experts, waking three point four six billion parameters per word. All seventy-eight billion parameters stay in memory. | 3.46B wake per word | 78B sit in memory | diagram-flow | 9.3 |
| s04 | explain | Native training stops at two hundred sixty-two thousand tokens, word chunks. It stretches to a million without retraining. The vendor says keep complex work under that. | trained: 262,144 | validated: 1,048,576 | vendor: keep work under 262,144 | giant-number | 9.0 |
| s05 | explain | Tonight you grab the community build, forty-seven and a half gigabytes of download. It runs on patched llama dot cpp. Ollama and LM Studio just stare. | 47.5 GB | patched llama.cpp | Ollama, LM Studio: wait | grid | 8.6 |
| s06 | payoff_close | Check your RAM before you trust the million-token promise. | Check your RAM first. | centered-stack | 2.8 |

## Draft B (number-first, hook: number-shock) -- WINNER
| Scene | Role | Narration | On-screen | Layout | Est s |
|-------|------|-----------|-----------|--------|-------|
| s01 | hook | A million tokens of context, forty-seven gigabytes of download. | 1M tokens | 47 GB | giant-number | 3.5 |
| s02 | foreshadow | That's Kolibri, a German model with open weights, files you run yourself. You've seen million-token headlines all week and asked if it fits your machine. | Kolibri | open weights | centered-stack | 7.0 |
| s03 | explain | Context is how much text it reads at once. Aleph Alpha itself says stay at two hundred sixty-two thousand tokens or below for complex work. The headline's own footnote. | ≤ 262,144 tokens | split-compare | 7.5 |
| s04 | explain | It's a mixture of experts: each word, a receptionist wakes the few specialists needed. All seventy-eight billion parameters sit in memory. | 78B parameters in memory | diagram-flow | 6.5 |
| s05 | explain | The community file needs a patched llama.cpp, the local runner, modified by hand. Ollama and LM Studio just stare. | patched llama.cpp only | Ollama, LM Studio: not yet | grid | 6.0 |
| s06 | payoff_close | One measured llama.cpp setup needed one hundred twenty-eight gigabytes of system RAM. Count yours before you trust the headline. | 128 GB system RAM | giant-number | 5.5 |

## Score table
| Row | A | B | Why |
|-----|---|---|-----|
| 1 | 3 | 2 | A's first five words -- 'Kolibri promises a million tokens' -- carry product, number, and a raised eyebrow, and the snap ('Its own card says don't') lands inside the 3.4s hook. B's first five words ('A million tokens of context') spend a number with no product named and no felt tension; the 47GB counterweight arrives at word eight and Kolibri isn't named until s02. B clears 'names a number' but not the first-five-words tension bar. |
| 2 | 2 | 3 | A's hook asserts the contradiction by 3.4s, but the promised substance -- what the card actually says -- waits until s04 (~22s); first concrete beyond the hook (Aleph Alpha, open weights) lands ~7-11s, so 'lands by 8s' but never the by-4s payoff. B must define context before it breaks; scored from the break per the fairness note, its break (the vendor's own 262,144 cap, 'the headline's own footnote') lands at the first beat the shape allows and is exactly the payoff the number-shock set up. |
| 3 | 3 | 3 | Both spend exactly five key numbers, none decorative. A: 1M / 3.46B / 78B / 262,144 / 47.5GB, one new number per sentence, all spoken exact. B: 1M / 47GB / 262,144 / 78B / 128GB, saving its hardest number for the close; the hook's two-number sentence is the number-shock design landing where it hits hardest. Drift check: B's hook rounds 47.5 down to 'forty-seven gigabytes' (flagged in its notes, conservative); A is exact. Neither speaks a hedged claim as assertion -- both keep the cap attributed to the vendor, and B's 128GB is properly hedged as one measured setup. |
| 4 | 3 | 3 | Both clean second person, no hard-constraint breaks, one wry beat each that lands unexplained: A's 'Ollama and LM Studio just stare' and B's 'The headline's own footnote.' B leans on definitional appositives ('the local runner, modified by hand') but they stay spoken and structural, not manual-toned. |
| 5 | 2 | 2 | A's hinges carry content -- 'Your graphics card stops deciding' names the ownership-to-architecture change, 'Tonight you grab' names the shift to action -- but s03 and s04 (mechanism vs. token limits) could swap without damage. B has tight anaphora ('That's Kolibri,' the llama.cpp handoff into the close) but jumps from context limits to architecture with no named change. Both transitions carry content; neither script is un-reorderable. |
| 6 | 2 | 2 | Both structures are absent from the last five ledger entries and neither matches the last two hooks, clearing rung 2. But A reuses named-contradiction (10-07) and closes on the run's familiar imperative hardware-audit ('Check your RAM' sits beside 'name your biggest real model'); B reuses number-shock (10-06) and closes on the same audit family ('Count yours'). Neither reaches rung 3's different-opening-rhythm-plus-different-landing bar. |
| 7 | 3 | 3 | A's payoff close -- 'Check your RAM before you trust the million-token promise' -- is last, repeatable, and bookends the hook's verb. B's 'Count yours before you trust the headline' is last, short, and quotable, with the 128GB sentence feeding it. In both, the line a viewer would repeat to a friend is the payoff line and it is last. |
| 8 | 2 | 3 | A shows the mechanism once concretely (3.46B waking, 78B resident, tile-bank visual) but never quantifies the consequence, so the viewer is told to check RAM with no way to extend the chain to a new case. B's receptionist-with-repick model plus 'all 78B sit in memory' plus one measured 128GB setup lets a viewer predict cases the script never mentions -- e.g., that a smaller quant or a bigger future MoE changes the download but not the residency problem. |

Totals: A 20, B 21. Winner: B.

## Grafts
- sentence into s05: "Ollama and LM Studio just stare." -- B's 'can't load it yet' states the fact flatly; A's line says the same thing in the channel's wry register. One-for-one swap at the same beat: no numbers spent, no person change, structure untouched, and s05's on-screen 'Ollama, LM Studio: not yet' keeps the explicit fact so nothing is lost. No surrounding rewrites needed.

## What the losing shape needed
A's news-react shape snaps early but then lets the promise hang unpaid -- the card's actual cap doesn't arrive until ~22s in, so it needed the 262,144 caveat pulled forward into the foreshadow scene to keep the break from going quiet through two full scenes. It also spends its fifth number on the download size and so can't quantify the RAM consequence it warns about; giving the close the measured footprint (and letting 3.46B live on screen only) would have turned 'check your RAM' from instruction into teaching.
