# Which model fits your GPU: outline judgment

Slug: `2026-08-23-which-model-fits-gpu`
Judged: 2026-08-23
Rubric: `stages/04-outline/references/judge-rubric.md`
Structures: `stages/04-outline/references/episode-structures.md`
Brief: `stages/03-research/output/2026-08-23-which-model-fits-gpu-brief.md`
Outline A: `buyers-guide`. Outline B: `concept-deep-dive`.

Neither outline file was modified by this judgement.

## How row 6 was scored

The episode ledger holds one entry, this slug, with `structure` empty. There is no history to be different from, and the rubric's fallback (a missing or empty ledger scores every outline 3) does not fit either: the ledger is present and this episode is already in it, it simply records no shape yet.

Row 6 was therefore scored as **distance from the obvious treatment**, and the obvious treatment was taken to be the brief's own `## Suggested outline`, which is the episode anybody handed these facts would write. That is a substitute scale and it is named here so a later reader does not mistake these two numbers for a rotation check. Neither outline can earn the row's third clause, a hook shape the last five do not use, because both hooks are the number-shock pattern built on the same number.

---

## Outline A, in full: `buyers-guide`

---
slug: 2026-08-23-which-model-fits-gpu
series: benchmarks
structure: buyers-guide
value_types: EQUIPS, TEACHES
target_minutes: 12
---

# Outline: Which build fits the card you own

## Angle
Fit is the file plus the cache, not the parameter count, and when two builds both fit, more bits beats more parameters on reasoning.

## Value brief
- EQUIPS: read the file size off the file table instead of the parameter count, add the cache from the published formula corrected for grouped-query attention, leave the runtime the slice nobody publishes, then take the largest build that still fits and spend anything left over on bits when the job is reasoning or long context. The check tonight is the split `ollama ps` prints.
- TEACHES: why "bigger model, fewer bits" was true when it was measured and does not transfer. It came from zero-shot knowledge scores on models released before 2022, longer-trained models degrade harder under quantization, and on reasoning the measured order reverses.
- Hook: "Twenty-seven billion parameters, in a file of six point one nine gigabytes."
- Payoff: "Take the biggest model whose file plus cache still leaves your card room to spare. If the job is reasoning or long context, spend that room on bits, not parameters."
- The number by 0:20: six point one nine gigabytes, the smallest published build of Qwen3.8-27B, spoken in the hook and shown on screen beside the parameter count it contradicts.

## Chapters
| # | Chapter | Target s | The one idea | Measurement shown | Muted viewer understands |
|---|---------|----------|--------------|-------------------|--------------------------|
| 1 | Which Build Actually Fits | 105 | The parameter count on the model page is not the number that decides whether the thing runs on your card, and the decision in front of you is which build to download, not which model to admire. For one person: you own one consumer card and you want the whole model resident on it. | Unsloth's published file table for Qwen3.8-27B, 6.19 GB at the bottom rung, on screen with its publisher named. Stated plainly: no number in this episode was measured here, the Spark was unreachable, so every figure carries the name of whoever published it. | A card's memory drawn as one bar. A parameter count on a model page gets struck through and a file size is written in its place. |
| 2 | File Plus Cache | 165 | The number that decides is gigabytes resident, and it has three parts: the file you download, the cache your conversation grows, and a slice the runtime takes that nobody publishes exactly. | NVIDIA's per-token cache formula, two times layers times heads times head dimension times bytes, worked by NVIDIA to roughly 2 GB for Llama 2 7B at 4,096 tokens. Qwen3-8B's config.json, 32 query heads against 8 key-value heads, so the printed formula overstates a modern model by four times. Ollama's own warning that a longer context costs more memory, and a llama.cpp maintainer saying there is no easy way to compute it. | The bar splits into a file block and a cache block, the cache block grows as a conversation extends, and a thin unlabelled band stays at the top that never gets a number. |
| 3 | More Parameters, Fewer Bits | 135 | Spend the budget on parameters and one model's ladder reaches every card tier, from 6.19 GB to 25.3 GB for the same twenty-seven billion parameters, and every rung down that ladder has a published price. | llama.cpp's quantize table: Q4_K_M measures 4.8944 bits per weight, Q6_K 6.5633, Q8_0 8.5008, because each block carries a scale on top of the payload bits. Unsloth's Qwen3.8-27B file table, 6.19 GB at UD-IQ1_S to 25.3 GB at UD-Q6_K_XL. llama.cpp's perplexity table at seven billion parameters: +0.0535 at Q4_K_M against +0.8698 at Q2_K. | Row A of the comparison table fills in across its six columns, and the ladder's rungs light up one at a time against 8, 12, 24 and 32 GB card marks. |
| 4 | Fewer Parameters, More Bits | 165 | Spend the same gigabytes on bits instead of parameters, and the rule everyone repeats reverses on the work most people actually run. | Ornith 1.5 9B's file table, 5.63 GB at four-bit and 9.53 GB at eight-bit, so the whole ladder through Q8_0 stays under ten gigabytes. arXiv 2212.09720's own stated scope: zero-shot accuracy only, models from 19M to 176B, nothing released after 2022, no reasoning evaluation. arXiv 2411.04330: degradation under quantization increases with training data size. arXiv 2510.10964, roughly 1,700 scenarios: 8B at eight-bit consistently beats 14B at four-bit, and 32B at four-bit is strictly dominated by both. | Row B fills in beside row A, same six columns, same units. The quality cell is the only one that flips which row reads better, and the older row's source date greys out. |
| 5 | The Rule And Its Exceptions | 150 | Fit first, then bits over parameters when the job is reasoning or long context, and here is who that rule is not for. | arXiv 2505.20276: eight-bit holds long-context accuracy to about a 0.8% drop while four-bit methods lose up to 59%. Hugging Face on mixture of experts: every expert stays resident, so Mixtral 8x7B needs memory for a dense 47B model while computing like a 12B one. Unsloth's DeepSeek V4 Flash, smallest published quant 82.5 GB, more than three times a 24 GB card. Ollama's FAQ: a model that does not fit is split, not refused, and `ollama ps` prints the ratio, such as 48% CPU against 52% GPU. llama.cpp's own guide on the cost of that split, in its own words, much slower. | The finished table with one row ringed. Three exception cards slide in and grey out beside it, then a single `ollama ps` line resolves to the last frame. |

## Visual philosophy
The dominant scene is one comparison table that starts empty in the second chapter and is still on screen in the last, gaining a row per contender and never once changing its six columns, with a memory-bar diagram beside it showing a card's gigabytes filling with file, cache and the runtime's unlabelled band. Terminal captures appear once and briefly, reproducing the shape of an `ollama ps` split from Ollama's own documentation, because nothing here ran on our bench and a replayed terminal would imply a measurement we did not make. Everything else stays typographic: published file tables shown with the publisher's name inside the frame, the cache formula written out as words multiplied by words rather than symbols, and a source line under every number the moment it appears.

## Decisions
- Angle chosen: fit is decided by gigabytes resident, and the parameters-versus-bits question only arrives after two builds both fit. It keeps one axis for chapters 3 and 4 and lets the reversal land as contender B's verdict rather than as a second thesis. Rejected: "the rule of thumb is wrong" as the spine, because it makes the episode an argument with a paper instead of a purchase decision, and the viewer still would not know what to download. Also rejected: opening on memory bandwidth, which is a different axis and would break the buyers-guide's same-axis discipline.
- Value types locked as EQUIPS and TEACHES. PROVES is unavailable: the DGX Spark was unreachable from the production machine, so there is no first-party capture and no number in this episode belongs to us. Attribution is therefore structural, not decorative, and it is named in chapter 1 and carried by a source line under every figure.
- Series deviation noted: the `benchmarks` row in `content-pillars.md` reads "measured by us". This episode cannot honour that and says so out loud in its first chapter rather than letting published figures pass as ours.
- Left out on purpose: the DGX Spark's 128 GB at 273 GB/s against an 8 GB RTX 5050 at 320 GB/s. It is the brief's strongest single fact for the channel, and it is about bandwidth, a second axis that would break the "same axis, same units, same table" rule that makes chapters 3 and 4 comparable. It wants its own episode.
- Also cut: Llama-3.1-8B's 14.96 GiB to 4.58 GiB drop, because Qwen3.8-27B's ladder makes the same point and the structure allows exactly one carried example; arXiv 2407.09141 on individual answers flipping at equal benchmark averages, cut for pacing in chapter 3 and available if a beat opens; the Q3 quality cliff from the single-author preprint arXiv 2601.14277, which the brief flags as unconfirmed, in favour of llama.cpp's perplexity table; Ollama's context tiers, because the brief warns they are printed in GiB while cards are sold in GB and a misquoted tier would be worse than silence.
- Headroom stays qualitative. The brief's process line says leave about a gigabyte of slack, but its own `Unverified` list calls specific headroom figures folklore from an unbenchmarked guide. Chapter 2 shows the runtime's slice as an unlabelled band and chapter 5 says no source publishes the right number, which is honest and still actionable: do not fill the card to the brim.
- No CPU-offload multiple is spoken anywhere. llama.cpp's "much slower" is quoted as llama.cpp's words, and the three-to-five-times figures circulating have no measurement behind them.
- No model card's hardware requirement line is read as fact in any chapter. The brief records two Ornith cards whose stated GPU requirements contradict their own file tables, and a Qwen card listing a four-bit build at 1.68 GB beside another at 19 GB. Only file tables are quoted, which is also the habit the episode is teaching.
- Positional labels are absent by design. Chapter breaks use content moves only: 1 to 2 answers the question chapter 1 raised, 2 to 3 jumps to the consequence, 3 to 4 names what changes, and 4 to 5 contradicts the expectation.
- Chapter 4 runs 30 seconds longer than chapter 3 despite the mirrored shape, because it carries the reversal and the provenance of the rule it reverses. The table columns and units stay identical, which is what the structure actually requires.
- Payoff sits last and nothing follows it. Chapter 5 gives the long-context evidence, then the exceptions, then the one-line check to run tonight, and the rule is the final spoken sentence.
- Hook and Payoff are written in spoken form, numbers as words, for the script stage to lift directly. Every other cell uses digits, which belong on screen. The payoff spends the script's single allowed "not X, but Y" on "bits, not parameters", so the script stage should not spend it again.

---

## Outline B, in full: `concept-deep-dive`

---
slug: 2026-08-23-which-model-fits-gpu
series: benchmarks
structure: concept-deep-dive
value_types: EQUIPS, TEACHES
target_minutes: 12
---

# Outline: Which model actually fits the card you own

## Angle
Whether a model fits your card is decided by its file size plus the cache it grows, never by its parameter count.

## Value brief
- TEACHES: what actually occupies a graphics card when a model loads, which is the weights file at its measured width, the cache computed on key-value heads rather than attention heads, and a runtime slice nobody publishes.
- EQUIPS: a rule for picking tonight's build from two numbers you can read off a page, plus the one command that tells you whether you got it right instead of guessing at headroom.
- Hook: "You own a card with twelve gigabytes on it. The model page says twenty-seven billion parameters, and that number cannot tell you whether it runs. Somebody has published that exact model as a file weighing six point one nine gigabytes."
- Payoff: "Take the biggest build whose file and cache both fit, then let the layer split settle it." (last spoken sentence; nothing follows it)
- The number by 0:20: six point one nine gigabytes, the smallest published build of the dense twenty-seven-billion-parameter Qwen3.8-27B, from the Unsloth model card. It arrives about sixteen seconds in and collides head on with the twenty-seven billion printed on the same page.

## Chapters
| # | Chapter | Target s | The one idea | Measurement shown | Muted viewer understands |
|---|---------|----------|--------------|-------------------|--------------------------|
| 1 | Two Files, One Model | 105 | The parameter count cannot answer "does it fit", because one model ships as many files of very different size. | Unsloth's Qwen3.8-27B file table: published builds from 6.19 GB (UD-IQ1_S) up to 25.3 GB (UD-Q6_K_XL) | A publisher's file table beside one capacity bar for a 12 GB card; the smallest row drops in and fits, the largest row drops in and overflows a 24 GB bar too. |
| 2 | Where The Arithmetic Breaks | 150 | Parameters times bits is the wrong sum twice, because the payload is not the whole file and the label is not the width. | llama.cpp's quantize table: Q4_K_M measures 4.8944 bits per weight (Q6_K 6.5633, Q8_0 8.5008, F16 16.0005); Llama-3.1-8B falls 14.96 GiB to 4.58 GiB | The label column and the measured bits-per-weight column set side by side, every row off by its block scales, with the hand-done sum crossed out beside them. |
| 3 | What Your Card Actually Holds | 195 | Three things occupy the card: the weights file, the cache that grows with the conversation, and a runtime slice nobody publishes. | NVIDIA's published cache formula worked to about 2 GB for Llama 2 7B at 4,096 tokens; Qwen3-8B's config.json showing 32 query heads against 8 key-value heads, so the printed formula overstates it fourfold | The bar fills in three blocks: a solid weights block, a cache block that grows as a chat scrolls beside it, then a hatched block at the top carrying no number at all. |
| 4 | Long Context And Experts | 165 | The same arithmetic bites in two places, where the cache line keeps growing and where the weights line is the whole expert set rather than the active slice. | Long-context study: about 0.8% accuracy drop at 8-bit against up to 59% loss for 4-bit methods; Hugging Face on Mixtral 8x7B, resident like a dense 47B while computing like a 12B; DeepSeek V4 Flash's smallest published quant at 82.5 GB | The same bar twice: first the cache block grows until it shoves the weights past the end, then the weights block widens to the full expert set with a single sliver lit. |
| 5 | What To Download Tonight | 105 | You pick the build from two numbers you can read, then let the runtime confirm it instead of trusting headroom folklore. | Ollama's documented layer split, values such as 48% CPU and 52% GPU in `ollama ps`; the 2025 study across roughly 1,700 scenarios where 8B at 8-bit beats 14B at 4-bit | The finished ledger with the chosen row ticked, then one quoted docs frame showing a CPU and GPU percentage split. |

Total 720 s (12:00), about 1,800 narration words at 150 wpm. Word budget by chapter: 260 / 375 / 490 / 415 / 260.

## Visual philosophy
One memory ledger carries the episode: a single capacity bar for a twelve-gigabyte card that fills, empties and refills from the opening frame to the closing one, with the publishers' own artefacts cut in beside it, a model card file table, the llama.cpp quantize table, a config file, never replacing the bar. Terminal frames appear only as sourced documentation excerpts, labelled with their publisher and never presented as our own run, because nothing in this episode was measured on our hardware and the episode says so out loud in the first chapter. Everything numeric stays typographic, with digits, units and the publisher's name set as on-screen type beside the bar, since the narration speaks every number as words and never reads a digit.

## Decisions
- Angle chosen: the deciding number is file size plus cache, not parameter count. It is one sentence a viewer repeats at a keyboard, it survives every model in the brief, and it is the only claim the episode can make without a first-party measurement. Rejected: "four-bit is a trap for reasoning work", which is a real result in the brief but is a myth-bust argument, not a mechanism, and would put the payoff in chapter four; rejected: "bandwidth, not capacity, is what you actually buy", which opens a second thesis this episode never closes.
- Worked example: Qwen3.8-27B against a twelve-gigabyte card. Its published ladder spans every consumer tier, so some rungs fit and some do not, which keeps a live decision on screen for twelve minutes, and a dense twenty-seven billion is where the naive parameter arithmetic is most badly wrong. Rejected as the carrier: Llama-3.1-8B, which fits everything so nothing is at stake, and Ornith 1.5 9B, whose whole ladder stays under ten gigabytes.
- The carried example is the ledger plus that one model, and it is never swapped. The llama.cpp table (measured on Llama-3.1-8B), NVIDIA's Llama 2 7B cache figure, Qwen3-8B's config and the Mixtral and DeepSeek exhibits appear beside the bar as cited evidence for a step in the arithmetic, and the bar itself stays Qwen3.8-27B on twelve gigabytes throughout, including in chapter four.
- Value types EQUIPS and TEACHES, not PROVES: the DGX Spark was unreachable, so every number here is published by somebody else. Chapter one states that on the record and every on-screen figure carries its publisher, which is a visual commitment, not a closing disclaimer, because nothing may follow the payoff.
- The hook uses the 6.19 GB build without implying it is a good build. It is named on screen as UD-IQ1_S, a one-bit-class build, and the quality cost lands in chapter two and again in the rule in chapter five.
- Nothing from the Unverified list is asserted. No headroom figure is spoken, so chapter five replaces the folklore gigabyte with the llama.cpp maintainer's statement that the runtime's slice is not calculable and with the `ollama ps` split as the check. No multiple is given for CPU offload, only llama.cpp's own "much slower". No claim that four-bit is indistinguishable in conversation. Units stay as published, GiB from llama.cpp and GB from the model cards, and are never mixed inside one comparison.
- No positional labels anywhere. Chapter breaks use one legal move each: into two, contradict the expectation ("That reads like a file size problem. The label lies too."); into three, jump to the consequence ("That is only the first line. The conversation writes the second."); into four, name what changes ("Now the context is long."); into five, answer the question the last chapter raised ("So which file do you actually pull?").
- Deliberately left out: the Spark's 128 GB at 273 GB/s bandwidth fact, the llama.cpp perplexity table, the Apple unified-memory reserve, and the contradictory model cards. The four-bit rule reversal is demoted from its own chapter to the qualifier inside the chapter five rule, because this structure spends chapter four on the two edge cases.
- Structure and series are paired by assignment: `benchmarks` would normally suggest `buyers-guide`, and the deep dive earns its place here because the brief carries a mechanism with one worked example rather than two contenders on a shared axis.

---

## Scores

| # | Row | A `buyers-guide` | B `concept-deep-dive` |
|---|-----|:-:|:-:|
| 1 | Hook strength | **3** | **1** |
| 2 | Promise inside 30 s | **3** | **3** |
| 3 | One idea per chapter | **2** | **3** |
| 4 | Payoff placement | **2** | **3** |
| 5 | Muted-viewer legibility | **3** | **2** |
| 6 | Difference | **3** | **2** |
| 7 | Repeat test | **2** | **2** |
| | **Total** | **18** | **16** |

## Row by row

**1. Hook strength. A = 3, B = 1.**

A: "Twenty-seven billion parameters, in a file of six point one nine gigabytes." Eleven words, one breath, the number-shock pattern, and the entire argument of the episode is folded inside it. A viewer says "wait, what" at second three. One thing for the script stage to watch, not a scoring matter: two numbers ride in one sentence, and Hard Constraint 5 says never make the viewer hold more than one new number at a time. The parameter count is the one they arrived with, which is why it survives here, but the line has no slack for a third.

B = 1, reasoning required: the concrete thing that stings, six point one nine gigabytes, is the third sentence and lands around second ten, while sentence one asserts a card size ("You own a card with twelve gigabytes on it") that two of the three cards the brief's viewer situation names are not, so the opening both delays the sting and mis-addresses part of the audience. A second reading is on the record: twelve gigabytes is a number with a unit in sentence one, which would make this a 2. It is scored 1 because the rubric's level-1 text describes the opening exactly, and because B's hook runs about fifty-five words, roughly twenty-two seconds, which spends most of the thirty-second budget before the promise has started.

**2. Promise inside 30 s. A = 3, B = 3.**

Both name one usable thing and both put the surprising number inside 0:20, so neither is failed under the rubric's send-it-back clause. A speaks it in sentence one, about second five. B times it explicitly at second sixteen. A's `EQUIPS` line is the more diffuse of the two, four moves in a sixty-word run-on; B's is the cleaner single sentence. Neither is scored down, because the row asks whether one usable thing is named and landed, not how tidily it is phrased in the value brief.

**3. One idea per chapter. A = 2, B = 3.**

No chapter in either outline is thin, and both allocate 720 s across five chapters with every chapter over 60 s.

A's chapter four carries contender B's memory ladder and, stacked on it, the provenance teardown of the rule it reverses: 2212.09720's zero-shot-only scope, 2411.04330 on longer-trained models degrading harder, and 2510.10964's reversal. That is a myth-bust nested inside a contender chapter, and A's own note that the chapter needs thirty seconds more than the chapter it mirrors is the tell.

B's chapters two and four each carry two sub-claims, but both are framed as one idea ("the wrong sum twice", "the same arithmetic bites in two places"), and chapter four's pairing of long context with mixture of experts is precisely what `concept-deep-dive` asks that chapter to hold.

**4. Payoff placement. A = 2, B = 3.**

Both put the payoff where their shape says.

A's decision rule closes chapter five and nothing follows it, which is correct for `buyers-guide` and correct under Hard Constraint 7. The spend is loose: the long-context evidence arrives in chapter five, so the second half of the rule gets its proof inside the payoff chapter, and chapter five then has to carry that evidence, three exceptions, the check and the rule in a hundred and fifty seconds.

B's mechanism lands at the end of chapter three, around seven and a half minutes, and the remaining four and a half are consequence in the shape's own terms. Two blemishes, neither fatal: B imports the 2025 reasoning result into chapter five as a qualifier, which is new argument in a chapter the structure says must not carry it, and B's `Payoff:` field names the closing rule rather than the mechanism, which a script writer reading that field literally could misplace.

**5. Muted-viewer legibility. A = 3, B = 2.**

A's six-column table is introduced empty in chapter two, gains row A in three, row B in four, and is ringed and finished in five, with the memory bar running beside it the whole way and never changing its columns. That is the comparison table filling in that `buyers-guide` names, and a muted viewer follows it from chapter two to the last frame.

B's carried object is one memory bar, and chapter two's on-screen cell does not contain it: the frame there is a label column against a measured-bits column with the hand arithmetic crossed out. That is a hundred and fifty seconds, a fifth of the episode, in which the one example the shape promises a muted viewer is not named as being on screen. B's visual philosophy asserts the artefacts are cut in beside the bar and never replace it; the chapter table does not carry that through. The same frame is also four named quantization formats set in a column, which is within reach of the trap `concept-deep-dive` names by name.

**6. Difference. A = 3, B = 2.**

Scored on distance from the obvious treatment, per the note above.

The brief's suggested outline runs: the parameter count is the wrong number, file size on one ladder, the cache, the rule and where it reverses, the decision rule and who ignores it. B holds three of those five chapters in place and substitutes at two, so it travels largely the obvious road carrying a new visual device. A collapses the brief's chapters two and three into one, spends two chapters turning the myth-bust into a purchase fork, promotes a model the brief mentions once (Ornith 1.5 9B, claim 7) into a full contender, and builds a two-row six-column table the brief never proposes.

Recorded against A's own score: neither outline earns the row's hook clause, and if the row is read strictly so that the unearned clause caps both at 2, this row stops separating them. It is the softest number in the table. See the retro note.

**7. Repeat test. A = 2, B = 2.**

The two payoffs are near-paraphrases of each other, which is where the convergence between these outlines shows most plainly.

A's operative sentence stands on its own at a keyboard ("Take the biggest model whose file plus cache still leaves your card room to spare") and the working title is visibly built from it, but the payoff as written is two sentences and level 3 asks for one. B's is one sentence of seventeen words, inside the twenty-word cap, but its second clause, "let the layer split settle it", is inert to anyone who has not watched the video, which is level 1's failure mode arriving inside an otherwise level-3 sentence. Both land at 2, for opposite reasons.

## Winner

**Outline A, `buyers-guide`, 18 to 16.**

No tie, so the Difference row was not needed as the tiebreak. That is fortunate: it could not have served as one, because both structures are new to a ledger that records no structure at all, and the rubric's second tiebreak, the shape the ledger has not seen longest, has nothing to read.

## Graft

**One chapter idea, from B's chapter two into A's chapter three: the viewer's own parameters-times-bits sum, shown crossed out, because the label is not the width.**

A strikes the parameter count through in chapter one and tells the viewer to read the file table instead, but never shows why the substitution is forced. A viewer who has just been told the parameter count is the wrong number will do the arithmetic themselves next, twenty-seven billion times four bits over eight, arrive at about thirteen and a half gigabytes, and trust it. A never intercepts that. B does, and it is B's best owned beat, the one idea in B that A has as an evidence line rather than as a beat.

The graft is cheap and requires no rewriting. A already cites the exact figures in chapter three (Q4_K_M measured at 4.8944 bits per weight, and the block scale that explains it), so no new source and no new claim enters. Chapter three is A's shortest at a hundred and thirty-five seconds. And the failed sum is the reason chapter three's rungs sit where they do, so it is evidence for that chapter's one idea rather than a second idea in it. Nothing in the surrounding chapters moves.

**Not grafted: B's hook line.** The rubric permits a hook graft; merit refuses it. B's hook scored two points below A's on row one, and A's hook is the strongest single line in either document.

This graft is recorded here. It still has to appear as one line under `## Decisions` when the winner is saved as `[slug]-outline.md`, which is the next step's file, not this one.

## Brief fidelity

Nothing was invented in either outline. Every figure in both traces to a numbered claim: the Unsloth ladder from 6.19 GB to 25.3 GB (claim 8), the llama.cpp measured bits per weight and the Llama-3.1-8B drop from 14.96 GiB to 4.58 GiB (claims 1 and 2), NVIDIA's cache formula at about 2 GB for Llama 2 7B (claim 3), Qwen3-8B's 32 query heads against 8 key-value heads (claim 4), the maintainer on the uncomputable runtime slice (claim 5), Mixtral 8x7B resident as a dense 47B (claim 6), Ornith 1.5 9B at 5.63 GB and 9.53 GB (claim 7, A only), DeepSeek V4 Flash at 82.5 GB (claim 9), Ollama's split and its 48/52 example (claim 12), llama.cpp's "much slower" (claim 13), Ollama on context cost (claim 14, A only), the 2212.09720 scope (claims 15 and 16, A only), the roughly 1,700-scenario reversal (claim 17), fragility with training data (claim 18, A only), the long-context 0.8 percent against up to 59 percent (claim 19), and the perplexity table (claim 20, A only).

**Both writers refused the brief's own process step, and both were right to.** `## Has process` says to leave about a gigabyte of slack; the same brief's `## Unverified` list calls specific headroom figures folklore from a guide with no benchmarks in it. Both outlines dropped the figure and both replaced it with something checkable, A with an unlabelled band that never gets a number plus "do not fill the card to the brim", B with the `ollama ps` split standing in for the folklore. This is recorded because a later reader will see the brief and both outlines disagree and should know the disagreement was deliberate on both sides. It is not a differentiator between them.

The `## Unverified` list is respected by both. A names five of its items explicitly in `## Decisions` (headroom, the offload multiple, model-card hardware lines, the GiB against GB tier trap, the unconfirmed 2601.14277 preprint) and B names five (headroom, the offload multiple, the "indistinguishable in conversation" claim, unit mixing, the Apple reserve), overlapping on three. The sixth item, that no number in this episode was measured here, is declared on the record inside chapter one by both, with the publisher named beside every on-screen figure, rather than parked in a closing disclaimer that Hard Constraint 7 would forbid anyway.

Both also cut the brief's self-declared strongest fact for the channel, the Spark's 128 GB at 273 GB/s against an 8 GB RTX 5050 at 320 GB/s, and both give the same reason: it is a second axis. It is now unspent and, as A says, it wants its own episode.

## What the losing shape would have needed

`concept-deep-dive` would have needed its collision in the first sentence rather than at second ten, with the twelve-gigabyte card named after the surprise instead of in front of it, so that row one stopped charging it two points that its chapter architecture had already earned back elsewhere. And it would have needed the memory bar named as on screen in chapter two, with the quantize table cut in beside it rather than taking the frame, so the one example the shape promises a muted viewer does not go missing for a fifth of the episode.

## Note for the retro

**The two outlines converge on six things and diverge on one.** Both picked six point one nine gigabytes for the 0:20 beat and built the hook on the same collision between a parameter count and a file size. Both wrote the same angle. Both locked EQUIPS and TEACHES and declared the missing first-party measurement in chapter one. Both cut the Spark bandwidth fact. Both refused the headroom instruction. Both closed on rules that read as two paraphrases of one sentence. The single real disagreement is shape.

The cause sits upstream of both writers. The brief's `## Summary` and `## Thesis` are the same sentence, word for word, and both outlines' `## Angle` lines are restatements of it. The angle was settled before this stage opened, so what two outlines could buy here was ordering and shape, not two readings of the topic.

**It still bought something.** The same collision is delivered in eleven words by A and in fifty-five by B, and that gap is only visible because both exist. On its own, B's opening reads as a competent hook rather than a slow one, and A's would have shipped without anyone knowing it was the better of two. One extra document to find that is worth it. But if the intent is two genuinely different episodes rather than two shapes for one, the divergence has to be forced at the brief, where one thesis sentence currently fills two fields.

**The margin is thinner than 18 to 16 looks.** A wins rows 1, 5 and 6 and loses rows 3 and 4. Two of A's winning points sit on rows with a defensible alternative reading: B's hook as a 2, and row 6's unearned hook clause capping both at 2. Under both alternative readings the totals reach 17 all, the Difference row ties at 2, and the ledger cannot break it. The pick survives because the hook gap is real and large, not because the arithmetic was comfortable.

**A is better where it counts first, B is better where it counts later.** A wins the two things that decide whether the episode is watched, the first ten seconds and a device a muted viewer can follow, and A's `## Decisions` is the more rigorous document, down to budgeting the script's single permitted "not X, but Y". B wins chapter architecture and payoff placement, which decide whether the episode holds up once watched. The rubric prices the opening and the closing line across three rows and chapter architecture across two, so it leans the way it leaned. The reason to accept the lean here is that A's architectural weakness, an overloaded chapter four, is fixable at the script stage, while B's hook problem is fixable too but its road being the brief's road is not.
