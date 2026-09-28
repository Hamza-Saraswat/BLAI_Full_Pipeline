---
slug: 2026-09-28-dgx-spark-firmware-synthetic-b
stage: 04-script
format: smooth-explainer
structures-tried: myth-bust (A), worked-example (B)
generated_at: 2026-09-28T13:20:00Z
hub: "[[videos/2026-09-28-dgx-spark-firmware-synthetic-b]]"
---

# Drafts: DGX Spark firmware: synthetic benchmarks lie 11%

Both drafts written blind (kimi-k3, one packet each, separate scratch dirs), gates passed before judging: validator 0 blockers both; eval all 9 gates pass both (entity_spend/top2 soft advisories only: top2 wants "Real LLM", a capitalized-phrase false positive; the scripts say "serving" and "real workload" on purpose); sameness clean vs 5 ledger entries; normalizer 1 scene changed each.

## Hook candidates (10, scored per hook-library)

1. You updated your Spark. The benchmark lied. -- 7 pts, situation (PICK B)
2. Your benchmark says slower. Your models say faster. -- 6 pts, situation
3. DGX Spark update: burn test says slower, serving says faster -- 5 pts, named-contradiction
4. The burn test lied to you. Your DGX Spark got faster. -- 7 pts, wrong-diagnosis (PICK A)
5. Synthetic benchmarks lie to your DGX Spark -- 5 pts, named-contradiction
6. You benchmarked the wrong thing tonight. -- 4 pts, wrong-diagnosis
7. DGX Spark firmware: same watts, less math, faster models -- 5 pts, named-contradiction
8. Faster where it matters. Slower where it shows. -- 5 pts, situation
9. Trust the burn test and you will skip a faster Spark. -- 7 pts, wrong-diagnosis
10. The benchmark every Spark owner runs is the wrong one. -- 6 pts, wrong-diagnosis

Two picks from different patterns (wrong-diagnosis vs situation), both digit-free so the hook classifier does not fire the banned number-shock class (last two ledger entries: number-shock 09-26, price 09-27).

## Draft A (myth-bust, 10 scenes, 106 s)

| Scene | Role | Narration | On-screen | Est s |
|-------|------|-----------|-----------|-------|
| s01 | hook | The burn test lied to you. Your DGX Spark got faster. | The burn test lied to you. \| Your DGX Spark got faster. | 4.0 |
| s02 | explain | You updated when the Dashboard prompted, then ran a benchmark to check. The burn test is a short synthetic workout, pure matrix math, that measures the chip's top speed. Everyone runs it after an update. A lower number reads as a regression. That's the myth. | you updated; you benchmarked \| fp16 burn test = matrix math \| a drop reads as regression | 15.5 |
| s03 | explain | Here's what broke it. Petronella, a lab running machines built on the same chip as your Spark, updated the whole fleet. The burn dropped about eleven percent on every unit. Same watts. Same or higher clock speed. | fleet, one firmware \| -11% on every unit \| same watts, same clocks | 13.0 |
| s04 | explain | But serving the model, answering real requests, told the other story. Same unit, same container, same settings. Decode, the part that writes your answer word by word, gained eight percent when it's just you. Four percent at a full queue. | same unit, container, settings \| decode = answer, word by word \| +8% solo, +4% queued | 14.0 |
| s05 | explain | Now the strange part. The burn fell while the model sped up. Picture a kitchen. The chef chops instantly. Every ingredient arrives through a single narrow doorway. The chef is compute. The doorway is the memory bus, your unified memory. The ingredients are the model's weights, its stored knowledge. | chef = compute \| doorway = memory bus \| ingredients = model weights | 17.0 |
| s06 | explain | To write each word, decode reads the active weights in through that doorway. It isn't thinking. It's reading. The burn measures the chef. Your answers wait on the doorway. | each word: read the weights \| burn measures the chef \| answers wait on the doorway | 10.5 |
| s07 | explain | Where the myth still holds: prefill, the part that reads your whole prompt before answering. Reading your prompt is one big block of math, compute-bound like the burn. | prefill reads your prompt first \| one big block of math | 9.0 |
| s08 | explain | On very long prompts, prefill ran flat to slightly slower. If your work is prompt-heavy, the burn drop is real for you. | flat to slightly slower \| prompt-heavy? the drop is real | 8.0 |
| s09 | explain | So here's the rule. Run the workload you actually run, before and after, same settings. Note its tokens per second, its answer speed. Trust that pair over any synthetic number. | run your real workload \| before + after, same settings \| trust the pair | 10.5 |
| s10 | payoff_close | The burn said slower. Your model said faster. Benchmark the workload you actually run, and trust it. | burn: slower \| model: faster \| benchmark what you run | 6.0 |

## Draft B (worked-example, 11 scenes, 108 s)

| Scene | Role | Narration | On-screen | Est s |
|-------|------|-----------|-----------|-------|
| s01 | hook | You updated your DGX Spark, and the benchmark lied. The Dashboard prompted, you clicked yes, then you checked the machine. | You updated your Spark. \| The benchmark lied. | 6.5 |
| s02 | explain | You ran the GPU burn test, a quick synthetic stress run, to make sure nothing broke. The score came back lower. Same machine, same room, lower number. | fp16 burn test \| same machine. lower score. | 9.5 |
| s03 | explain | A burn test measures peak sixteen-bit math, the chip's top speed on a synthetic matrix trick, for a few seconds. Nothing about serving a model. | fp16 burn test \| measures TFLOPS, top speed | 8.5 |
| s04 | explain | Then a field report landed. A lab called Petronella updated its whole fleet of machines built on the chip inside your Spark. The burn dropped about eleven percent on every unit. Clocks the same or higher, watts the same. No throttling. | -11% on every unit \| clocks same, watts same | 14.0 |
| s05 | explain | But the lab measured what you actually do: serving. Decode, the part that writes your answer one word at a time, sped up. It went from twenty-three point one tokens a second to twenty-five with just you asking. Faster at every load. | 23.1 to 25.0 tok/s \| faster at every load | 14.5 |
| s06 | explain | Here the lab offers a hypothesis, not a finding. Picture a kitchen. The chef chops instantly, but every ingredient arrives through one narrow doorway. | a hypothesis, not a finding \| chef chops, doorway narrows | 8.5 |
| s07 | explain | The chef is your compute, the doorway is the memory bus, your unified memory, and the ingredients are the model's weights. To write one word, it reads the active weights out of memory. Not think. Read. | chef = compute \| doorway = memory bus \| ingredients = weights | 11.0 |
| s08 | explain | The honest catch. Prefill, the part that reads your whole prompt first, runs on raw math like the burn. There the doorway breaks: reading your prompt is one big block of math. | the doorway breaks \| prompt = one big block of math | 11.0 |
| s09 | explain | Prefill ran flat to a touch slower. Prompt-heavy work? That drop is real for you. | prefill flat to slightly slower \| the drop is real | 5.5 |
| s10 | explain | Your moves. Step one: benchmark your real workload before you update, and note the tokens per second. Step two: run the firmware update itself. Step three: re-run the same workload a few times. Trust that pair, before and after. | 1 benchmark before updating \| 2 update \| 3 re-run same workload \| trust the pair | 12.0 |
| s11 | payoff_close | The burn said eleven percent slower. Your model said faster. Only one of those is what you feel. | -11% \| your model: faster \| benchmark what you run | 6.0 |

Note: B's payoff_close narration was trimmed to "The burn said eleven percent slower. Your model said faster. Only one of those is what you feel." (from four sentences) to clear the ending-tail advisory; the "benchmark what you run" line moved to on-screen text only. B's "Step two: update." was expanded to "Step two: run the firmware update itself." for the 6-word label minimum.

## Judge verdict

## Scores
| Row | Draft A | Draft B |
|-----|---------|---------|
| 1 Hook | 3 | 2 |
| 2 Payoff timing | 3 | 1 |
| 3 Specificity | 3 | 2 |
| 4 Voice | 3 | 3 |
| 5 Navigation | 3 | 1 |
| 6 Difference | 3 | 3 |
| 7 Repeat test | 3 | 2 |
| 8 Teaching | 3 | 3 |
| Total | 24 | 17 |

- Row 1: A packs product and tension inside five words ("The burn test lied"); B names the Spark but parks "the benchmark lied" past the mark, then re-narrates the update.
- Row 2: Per the fairness note, A's break is the hook itself, landing by second four as promised; B's first concrete number waits until scene five, roughly second fifty.
- Row 3: A spends three numbers total, one per beat, none decorative; B's 23.1-to-25.0 crams two new numbers into one sentence and invents absolute rates the brief never gave.
- Row 4: Both hold clean second person with one dry, unexplained beat that lands: A's "It isn't thinking. It's reading," B's "Not think. Read."
- Row 5: A's transitions each name what changed and the order is load-bearing; B's "Step one/two/three" deletes with zero loss, so the mechanical-label cap holds at 1.
- Row 6: Both differ from the ledger's contrarian-take and comparison-ladder in shape, opening rhythm and landing; near-identical durations noted, but the three difference criteria are met.
- Row 7: A ends on the repeatable rule verbatim; B ends on "Only one of those is what you feel," which needs its antecedents and strands the actionable payoff upstream.
- Row 8: Both show chef/doorway/weights once, concretely, arming viewers to predict unmentioned cases like fine-tuning or RAG from the prefill/decode split.

## Winner
Draft A, 24–17, margin of seven. It pays its hook inside four seconds, navigates without a single deletable label, and leaves the repeatable rule as the last sound in the room.

## Grafts
One graft: **"Here the lab offers a hypothesis, not a finding."** (B, s06) — inserted in A's s05 after "The burn fell while the model sped up." and before "Picture a kitchen." Reason: A presents the kitchen mechanism as settled explanation while the brief supplies only the numbers; B's hedge states the causal story's true epistemic status at zero cost to A's structure, person, or number budget. No hook graft: B's hook scored lower. No second graft: B's tok/s pair would inflate A's three-number budget and import unbriefed absolutes, and B's closer would displace A's repeatable final line.

## Loser's path
B's worked-example spent four scenes re-earning a break its own hook had already announced; winning required the 23.1→25.0 evidence inside the first two scenes. It also needed its step labels to carry content or be cut, and a close ending on the repeatable rule rather than an antecedent-dependent kicker.
