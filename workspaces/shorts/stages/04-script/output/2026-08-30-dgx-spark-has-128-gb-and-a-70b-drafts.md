# Draft judgment: 2026-08-30-dgx-spark-has-128-gb-and-a-70b

- stage: 04-script, judge pass
- candidates: Draft A (worked-example / situation hook) vs Draft B (myth-bust / wrong-diagnosis hook)
- rubric: `stages/04-script/references/judge-rubric.md` — 8 rows, 0-3 each, max 24; tie-break on row 6 (difference)
- ledger context (row 6): one prior entry — `2026-08-29-glm-5-3-just-went-open-weight`, structure number-first, hook number-shock, closing move "before you download read your total", 35 s
- both drafts passed every machine gate before judging; this pass only scores, picks, and grafts

## Score table

| # | Row | A | B |
|---|-----|---|---|
| 1 | Hook | 2 | 3 |
| 2 | Payoff timing | 2 | 3 |
| 3 | Specificity without cramming | 3 | 3 |
| 4 | Voice | 3 | 3 |
| 5 | Navigation | 2 | 3 |
| 6 | Difference | 2 | 2 |
| 7 | The repeat test | 3 | 2 |
| 8 | Teaching | 3 | 3 |
|   | **Total** | **20** | **22** |

## Justifications

**Row 1 — Hook.** A (2): names the Spark and a seventy B, but the felt tension ("and wait. And wait.") lands at words 8-10, past the five-word bar a 3 requires. B (3): "Your Spark isn't slow. Its doorway is narrow." names the product and the viewer's own felt problem inside the first five words.

**Row 2 — Payoff timing.** A (2): the 2.7 tok/s measurement lands inside the hook, but the two "And wait." beats push it to roughly second 6-7 — by second 8, not by second 4. B (3): fairness note applied — scored from the break, not the stated myth; the break lands at scene 3 ("Same box, same model, two speeds") and the 803 / 2.7 measurement lands within about two seconds of it, and it is exactly the evidence the hook promised.

**Row 3 — Specificity without cramming.** A (3): every beat carries an earned specific; the paraphrases are accurate against the brief ("just under four" = the 3.9 ceiling, "climbs past four" = 4.423); no factual drift; the 200B capacity line is explicitly attributed ("says NVIDIA"). B (3): every beat carries a specific; 128 GB, 803/2.7 and 273 all match the brief, "under four tokens a second" matches the 3.9 ceiling, and scene 7's number-free MoE beat spends nothing it doesn't need; no drift on any brief number (the 200B line drops NVIDIA's name — noted, but the figure is the brief's claim 3 and the claim itself is true to it).

**Row 4 — Voice.** A (3): no hard-constraint breaks, second person throughout, one wry beat ("It fits. It just takes its time.") that lands on the box, outside hook and payoff, unexplained. B (3): no breaks; jargon defined in the same breath as an appositive ("a mixture of experts, a model that wakes only a few specialists per word"); two wry beats ("slower than your group chat types", "It printed the doorway's width in smaller type"), correctly spaced, never in hook or payoff.

**Row 5 — Navigation.** A (2): transitions carry content ("The same seventy B, stored smaller." / "Keep the bytes. Wake less of the model."), but scenes 7 and 8 are two parallel byte-shrinking fixes that swap without breaking anything, so the order is not load-bearing. No labels, so no deletion-test cap. B (3): every transition names what changed ("Why the gap." answers the question scene 3 raised; "The spec sheet did not lie." opens the resolution); belief → measurement → mechanism → analogy → rule → fixes → scope → payoff cannot be reordered without breaking.

**Row 6 — Difference.** A (2): worked-example shape, situation hook and 110 s are all clearly different from yesterday's number-first / number-shock / 35 s, but the close repeats yesterday's exact closing move ("before your next download, run the division yourself" vs "before you download read your total"), which blocks a 3. B (2): myth-bust shape and wrong-diagnosis hook are a different shape with a different opening rhythm, but its close opens on the same gambit ("Before you download a model for this box, find the gigabytes…") — same move, same cap.

**Row 7 — The repeat test.** A (3): the payoff line is the repeatable one and it is the last thing heard — "On this box you shop by active bytes per token, not by parameter count." B (2): the repeatable line is "Capacity picks what loads. Bandwidth picks how it talks." (scene 8), but the actual payoff sentence ("That one number tells you the chat speed before the download starts.") is functional, not quotable.

**Row 8 — Teaching.** A (3): the mechanism is shown once concretely (each written token re-reads the weights; 273 ÷ 70 lands under four) and the close hands the viewer the division, so they can predict models the script never mentions. B (3): same mechanism shown concretely, plus the explicit active-weights definition ("the slice the model actually uses") that lets the viewer predict quant and MoE cases; the close hands over the same division.

## Draft A (verbatim, worked-example / situation hook)

# Draft A: worked-example / situation hook

- slug: 2026-08-30-dgx-spark-has-128-gb-and-a-70b
- structure: worked-example
- hook_pattern: situation
- band: smooth-explainer
- target_duration_s: 110
- promise: after this video the viewer can predict whether any model will chat fast on a DGX Spark before downloading it.
- value_types: TEACHES (each written token re-reads the weights, so tokens/sec = bandwidth / bytes read), REFRAMES (shop by active bytes per token, not parameter count)
- analogy: the doorway (a chef who chops instantly, every ingredient through one narrow doorway); limit stated in scene 4, one clause: "Reading arrives in one wide pass, where the picture breaks."
- key_numbers_spent (3): 2.7 tps decode (row 3); 273 GB/s (row 1); 41.14 tok/s GPT-OSS-120B (row 5)

## Script

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|---|---|---|---|---|---|---|---|
| 1 | hook | You unbox the Spark, feed it a seventy B, and wait. And wait. L M S Y S timed the reply at two point seven tokens a second. | You unbox the Spark, feed it a 70B… then 2.7 tok/s | Frame 1: hook line fully legible, cursor blinking within half a second. On "feed it a seventy B" a model card lands beside the small box; on "And wait" the reply cursor creeps; on "two point seven" a counter freezes. | hyperframes | hook_text_scene | 8.4 |
| 2 | turn: capacity vs carrying speed | The spec sheet leads with capacity: room for enormous models, up to two hundred billion parameters, says NVIDIA. It fits. It just takes its time. The quieter line is memory bandwidth: two hundred seventy-three gigabytes per second, the chip's carrying speed. | up to 200B parameters / 273 GB/s | On "spec sheet" a product page scrolls; on "two hundred billion parameters" the capacity line highlights; on "quieter line" the highlight slides down to 273 GB/s. | hyperframes | spec_sheet_scroll | 12.2 |
| 3 | turn: the job splits | Here is what changes when you hit enter. Reading your prompt is one big block of math, done in one pass. The Spark is quick at it. Writing the answer is the other job: one chunk of text at a time, each token re-reading the model's weights. | Read: one wide pass / Write: one token at a time | On "Reading your prompt" the prompt flies in as a single block; on "Writing the answer" letters appear one by one while a weight stack pulses once per token. | manim | split_read_write | 14.0 |
| 4 | turn: the doorway | Picture a chef who chops instantly, but every ingredient arrives through one narrow doorway. The chef is the compute. The doorway is that two hundred seventy-three gigabytes per second. Reading arrives in one wide pass, where the picture breaks. Writing walks every ingredient through, one per token. | one narrow doorway / 273 GB/s | On "chops instantly" the knife blurs; on "one narrow doorway" ingredients squeeze through a tight door; on "one wide pass" a whole shelf slides through a wide opening; on "one per token" single items file through. | hyperframes | analogy_kitchen | 14.0 |
| 5 | turn: the division | So do the division the spec sheet skips. A seventy B in F P eight, one byte per weight, is about seventy gigabytes of weights. Two hundred seventy-three divided by seventy lands just under four tokens a second. | 273 ÷ 70 → under 4 tok/s | On "do the division" the equation builds term by term; on "one byte per weight" each weight shrinks to a single block; on "just under four" the result settles below a line marked 4. | manim | equation_build | 11.3 |
| 6 | turn: the ceiling named | Two point seven is that ceiling with overhead, not a misconfiguration. Tokens per second is bandwidth divided by bytes read. That is the whole mechanism. | 2.7 = ceiling + overhead / tok/s = bandwidth ÷ bytes | On "Two point seven" a measured bar stops just under the ceiling line; on "bandwidth divided by bytes read" the formula locks into place. | manim | bar_vs_ceiling | 7.5 |
| 7 | turn: the bytes shrink | The same seventy B, stored smaller. q4 K M keeps each weight in about half a byte, half the traffic through the doorway. On Ollama the same model climbs past four tokens a second. You give up a little accuracy, and casual chat never notices. | q4_K_M ≈ ½ byte per weight / 4+ tok/s | On "stored smaller" the weight blocks shrink to half size; on "half the traffic" the doorway empties faster; on "climbs past four" the speed needle crosses the line marked 4. | hyperframes | shrink_compare | 13.4 |
| 8 | turn: less of the model wakes | Keep the bytes. Wake less of the model. G P T O S S one twenty B holds a hundred twenty billion parameters. It wakes only a slice per token. The same Spark writes it at forty-one point one four tokens a second. Fewer bytes per token, and the doorway clears. | GPT-OSS-120B / 41.14 tok/s | On "a hundred twenty billion parameters" a grid of 120 tiles fills; on "wakes only a slice" a few tiles light per step; on "forty-one point one four" the counter sprints. | manim | moe_tile_grid | 15.2 |
| 9 | payoff_close | So before your next download, run the division yourself. Find the bytes each token reads, and split two hundred seventy-three by that number. Under ten tokens a second, chat feels like watching someone type. On this box you shop by active bytes per token, not by parameter count. | shop by active bytes per token | On "run the division yourself" the formula returns as a two-line checklist; on "shop by active bytes" the desk from frame 1 returns and the wordmark settles. | hyperframes | payoff_checklist | 14.3 |

## Writer notes

- TEACHES delivered by: "Tokens per second is bandwidth divided by bytes read." (scene 6)
- REFRAMES delivered by: "On this box you shop by active bytes per token, not by parameter count." (scene 9; it is the last spoken sentence, zero sentences follow it)
- Key numbers spent (3): 2.7 tps decode (brief row 3), 273 GB/s (brief row 1), 41.14 tok/s GPT-OSS-120B (brief row 5).
- Check lines for the reviewer:
  - "climbs past four tokens a second" paraphrases 4.423 (row 4) and "just under four" paraphrases the 3.9 ceiling (row 7); both are deliberate paraphrases to stay under the 3-number cap. Flag if the gate counts paraphrases.
  - "up to two hundred billion parameters" is brief claim 3 (NVIDIA marketing line), not a key-number row; scene 2 also carries 273, so it holds two numbers at once. Split if judged a constraint-5 breach.
  - "Under ten tokens a second, chat feels like watching someone type" is the brief's glossary definition of tok/s, not a benchmark.
  - "one byte per weight" (F P eight) and "half a byte" (q4 K M) come from the brief's glossary.
  - The 128 GB capacity figure is never spoken or shown, to protect the number cap; capacity is carried by "room for enormous models".

## Draft B (verbatim, myth-bust / wrong-diagnosis hook)

# Draft B: 2026-08-30-dgx-spark-has-128-gb-and-a-70b

```yaml
slug: 2026-08-30-dgx-spark-has-128-gb-and-a-70b
draft: B
structure: myth-bust
hook_pattern: wrong-diagnosis
script_format: smooth-explainer
target_duration_s: 110
promise: after this video the viewer can predict whether any model will chat fast on a DGX Spark before downloading it
value_types: [TEACHES, REFRAMES]
analogy: the doorway (kitchen with one narrow door = memory bandwidth); limit stated in scene 5: the picture breaks for reading your prompt, which arrives in one wide delivery
wps: 3.35
```

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|--------------------------|------------------------------------------|--------------|------|--------|-------|
| 1 | hook | Your Spark isn't slow. Its doorway is narrow. LMSYS measured two point seven tokens a second from a seventy-billion-parameter model on one. | Your Spark isn't slow. Its doorway is narrow. / 2.7 tok/s, LMSYS | On "Your Spark isn't slow" the hook line sits over a Spark on a desk; on "two point seven tokens a second" a chat bubble stalls mid-word and 2.7 tok/s snaps in beneath the hook line. | hyperframes | hero_text | 6.6 |
| 2 | belief | You ordered the Spark for a hundred twenty-eight gigabytes of unified memory, or the order page is still open. The plan writes itself: load the biggest model that fits, expect chat speed. Everyone's math says fitting is the whole game. | 128 GB unified memory / fits = fast? | On "a hundred twenty-eight gigabytes" the spec sheet line 128 GB highlights; on "load the biggest model that fits" a giant model box drops cleanly into the memory pool; on "the whole game" a checkmark appears beside "fits = fast?" and wobbles. | hyperframes | split_spec | 11.9 |
| 3 | measurement | Same box, same model, two speeds. It reads your prompt at eight hundred three tokens a second. It writes the answer at two point seven, slower than your group chat types. | reads: 803 tok/s / writes: 2.7 tok/s | On "reads your prompt" the prompt whooshes in as one fast bar labeled 803 tok/s; on "writes the answer" the reply types out letter by letter under 2.7 tok/s, stalling between words. | hyperframes | side_by_side | 9.3 |
| 4 | mechanism | Why the gap. Reading is one wide pass of math, and the Spark's compute eats it. Writing is one token at a time, and each token re-reads the model's weights from memory. The compute barely works during decode. The memory does the hauling. | every token re-reads the weights | On "one wide pass" the whole prompt lights up as a single block flowing into the chip; on "each token re-reads" a loop arrow cycles from memory to chip once per written word, the weight stack pulsing each cycle; on "the memory does the hauling" the arrow thickens while the compute block idles. | manim | flow_loop | 12.8 |
| 5 | analogy | Picture a kitchen where the chef chops instantly and every ingredient fits through one narrow door. The chef is the compute. The door is the memory bus: two hundred seventy-three gigabytes a second. For reading your prompt, one wide delivery, the picture breaks. | doorway = 273 GB/s | On "chef chops instantly" the knife blurs through a pile; on "one narrow door" ingredients queue single file through a small door labeled 273 GB/s on "two hundred seventy-three"; on "the picture breaks" one wide prompt crate skips the door entirely. | hyperframes | split_diagram | 12.8 |
| 6 | ceiling_rule | So the speed ceiling is one division. Bandwidth divided by the gigabytes each token re-reads. A dense seventy-billion model in eight-bit re-reads about seventy gigabytes per token. The ceiling sits under four tokens a second. Two point seven is that ceiling with overhead. | ~70 GB/token, ceiling < 4 tok/s / 2.7 = ceiling + overhead | On "one division" a fraction assembles; on "about seventy gigabytes" the divisor fills with ~70 GB/token; on "under four tokens a second" the result line draws at < 4 tok/s; on "Two point seven" a measured bar lands just beneath that line. | manim | formula_center | 12.8 |
| 7 | turn_active_bytes | What a token re-reads is the active weights, the slice the model actually uses. Quantize to four-bit and each token carries half the bytes. Or a mixture of experts, a model that wakes only a few specialists per word. GPT-OSS one twenty B is bigger on paper and chats comfortably. | 4-bit: half the bytes / GPT-OSS-120B: bigger, chats | On "carries half the bytes" the parcel moving through the door shrinks to half size; on "wakes only a few specialists" a grid of expert cells stays dark while three light up per word; on "GPT-OSS one twenty B" its chat bubble types out smoothly. | hyperframes | grid_moe | 14.9 |
| 8 | myth_scope | The spec sheet did not lie. It printed the doorway's width in smaller type. A model that does not fit does not run. And those hundred twenty-eight gigabytes are why a two-hundred-billion-parameter model loads on a desk at all. Capacity picks what loads. Bandwidth picks how it talks. | 128 GB decides what loads / 200B-class, on a desk | On "does not fit" an oversized model box bounces off the Spark outline; on "loads on a desk" the 200B-class box settles inside the 128 GB pool; on "Bandwidth picks" a speed gauge hand rises beside the memory pool. | hyperframes | balance_two | 14.3 |
| 9 | payoff_close | Before you download a model for this box, find the gigabytes it re-reads per token. Divide two hundred seventy-three by it. That one number tells you the chat speed before the download starts. | GB re-read per token / 273 / that = your tok/s | On "find the gigabytes" the active-bytes line on a model card highlights; on "Divide two hundred seventy-three" the mini formula fills with 273 over that number; on "chat speed" the result lands in the green; the doorway line from frame 1 settles back with the wordmark. | hyperframes | hero_formula | 9.9 |

## Writer notes

- TEACHES lands in scene 4: "Writing is one token at a time, and each token re-reads the model's weights from memory." (the mechanism: decode re-reads weights per token, so it is bandwidth work).
- REFRAMES lands in scene 8: "Capacity picks what loads. Bandwidth picks how it talks." backed by scene 7's parameter-count to active-bytes turn ("What a token re-reads is the active weights").
- Key numbers spent (3 rows of the brief's table): 128 GB unified memory; 803 / 2.7 tps prefill/decode (one key-number row, scenes 1 and 3); 273 GB/s bandwidth.
- Check me, reviewer: scene 6 speaks derived figures from claim 5 ("about seventy gigabytes per token", "under four tokens a second") without quoting the 3.9 tok/s key-number row verbatim; if the gate counts those as a fourth key number, swap scene 6's last two sentences for "Do the division and two point seven stops looking like a misconfiguration."
- Check me, reviewer: scene 8's "two-hundred-billion-parameter model" comes from claim 3 (NVIDIA's advertising line), not from the key-numbers table.
- Wry beats: scene 3 ("slower than your group chat types") and scene 8 ("It printed the doorway's width in smaller type"); none in hook or payoff.
- Analogy limit is stated in scene 5 ("For reading your prompt, one wide delivery, the picture breaks"). No sentence from the analogies file is reused.
- "We/our/us" count: zero. No em dashes. No positional labels.

## Verdict

**Winner: Draft B, 22-20 (margin 2).** No tie, so the row-6 tie-break is not invoked. B's edge comes from row 1 (tension inside the first five words), row 2 (the break pays its evidence immediately, per the fairness note) and row 5 (a strictly ordered myth-bust chain); A takes only row 7 (its payoff line is the repeatable one).

## Grafts

1. **Hook graft: none.** The loser's hook must score at least two points higher on row 1; A's hook scored lower (2 vs 3), so no hook moves.
2. **Sentence graft (one of at most two):** from Draft A, scene 7 — "You give up a little accuracy, and casual chat never notices." — inserted into Draft B, scene 7, immediately after "Quantize to four-bit and each token carries half the bytes." Reason: B's quantize beat states the benefit with no cost, and the voice rules require the honest trade-off to ride along ("the trade-off always rides along"); A's sentence says exactly that. It carries no number, keeps the second person, and does not touch B's structure or its three-number budget.
3. **No second graft.** A's "forty-one point one four tokens a second" says B's soft "chats comfortably" better, but moving it would add a fourth key number to B and break its number budget. A's closing maxim ("shop by active bytes per token, not by parameter count") duplicates content B already lands as well in scene 8 ("Capacity picks what loads. Bandwidth picks how it talks."), and swapping B's final sentence would rewrite the payoff beat, not graft it.

## What the losing shape would have needed

The worked-example needed its tension inside the first five words — the number and the wait arrive only after "And wait. And wait." — and it needed scenes 7 and 8 to depend on each other causally instead of standing as two swappable fixes, which cost it rows 1, 2 and 5. It also closed on yesterday's exact "before you download, check the math" move, so even a perfect middle would have kept row 6 capped at 2; a different landing was required to win outright.
