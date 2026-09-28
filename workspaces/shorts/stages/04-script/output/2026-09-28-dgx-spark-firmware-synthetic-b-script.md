---
slug: 2026-09-28-dgx-spark-firmware-synthetic-b
format: smooth-explainer
structure: myth-bust
style_pack: signal
value_types: TEACHES,EQUIPS
promise: After this Short you can benchmark your own Spark with the workload you actually run, and know which number to trust after a firmware update.
target_duration_s: 111
brief: 2026-09-28-dgx-spark-firmware-synthetic-b-brief.md
drafts: 2026-09-28-dgx-spark-firmware-synthetic-b-drafts.md
---

# The Burn Test Lied to You

## Decisions
- Structures tried: myth-bust (A) vs worked-example (B), both clear of the ledger's last two (contrarian-take, comparison-ladder). A won 24-17: it pays the hook inside four seconds, navigates with zero deletable labels, and ends on the repeatable rule. One graft from B: "Here the lab offers a hypothesis, not a finding." inserted before the kitchen analogy, keeping the mechanism at its briefed epistemic status.
- Hook: candidate 4 of 10, "The burn test lied to you. Your DGX Spark got faster." (wrong-diagnosis pattern, 7 points). Digit-free on purpose: the classifier fires number-shock on any number word and the last two ledger entries were number-shock and price. B took candidate 1 (situation).
- Soft advisories kept with reason: top2 wants "Real LLM" (a capitalized-phrase false positive from the heuristic extractor; the script deliberately says "serving" and "real workload"); entity_spend 0.13 with the same extractor caveat. Hard gates all pass; validator 0 blockers 0 advisories; variety ok vs 5 ledger entries; normalizer scenes_changed 1 (lexicon expansions).
- Value types delivered: TEACHES via the decode-is-memory-bound mechanism shown once (kitchen doorway); EQUIPS via the before-and-after rule scene and the spoken close "Benchmark the workload you actually run, and trust it."

## Hook candidates
1. Your benchmark says slower. Your models say faster. -- 6 pts
2. DGX Spark update: burn test says slower, serving says faster -- 5 pts
3. Synthetic benchmarks lie to your DGX Spark -- 5 pts
4. The burn test lied to you. Your DGX Spark got faster. -- 7 pts *
5. You benchmarked the wrong thing tonight. -- 4 pts
6. DGX Spark firmware: same watts, less math, faster models -- 5 pts
7. Faster where it matters. Slower where it shows. -- 5 pts
8. Trust the burn test and you will skip a faster Spark. -- 7 pts
9. The benchmark every Spark owner runs is the wrong one. -- 6 pts
10. You updated your Spark. The benchmark lied. -- 7 pts (assigned to draft B)

(The two picks are candidates 4 and 10 in this list; both scored 7, different patterns: wrong-diagnosis for A, situation for B.)

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|---------------------------|----------------|--------------|------|--------|-------|
| s1 | hook | The burn test lied to you. Your DGX Spark got faster. | The burn test lied to you.  /  Your DGX Spark got faster. | Frame 1: full-bleed near-black field, the words 'The burn test lied to you.' already composed and fully legible in the signal pack's kinetic headline style, amber underline under 'lied'. Motion onset at 0.4s: beat two 'Your DGX Spark got faster.' rises in place on 'faster' with the amber underline scaling under it. First and last 8 frames stable. | hyperframes | centered-stack | 4.0 |
| s2 | explain | You updated when the Dashboard prompted, then ran a benchmark to check. The burn test is a short synthetic workout, pure matrix math, that measures the chip's top speed. Everyone runs it after an update. A lower number reads as a regression. That's the myth. | you updated; you benchmarked  /  fp16 burn test = matrix math  /  a drop reads as regression | Update-prompt card fades in on "Dashboard prompted"; terminal card fades in on "benchmark to check"; amber tag "the myth" scales in on "That's the myth". One text block animating at a time. | hyperframes | grid | 15.5 |
| s3 | explain | Here's what broke it. Petronella, a lab running machines built on the same chip as your Spark, updated the whole fleet. The burn dropped about eleven percent on every unit. Same watts. Same or higher clock speed. | fleet, one firmware  /  -11% on every unit  /  same watts, same clocks | Machine-row silhouettes fade in on "the whole fleet"; giant amber "-11%" scales in on "eleven percent"; caption chip rises in place on "Same watts". At most two elements moving. | hyperframes | giant-number | 13.0 |
| s4 | explain | But serving the model, answering real requests, told the other story. Same unit, same container, same settings. Decode, the part that writes your answer word by word, gained eight percent when it's just you. Four percent at a full queue. | same unit, container, settings  /  decode = answer, word by word  /  +8% solo, +4% queued | Baseline card fades in on "Same unit"; "+8% solo" digit scales in on "eight percent"; "+4% full queue" scales in on "Four percent". Digits appear sequentially, never together. | hyperframes | split-compare | 14.0 |
| s5 | explain | Now the strange part. The sixteen-bit burn test fell while the model sped up. Here the lab offers a hypothesis, not a finding. | fp16 burn test fell  /  serving sped up  /  a hypothesis, not a finding | On 'burn fell', a falling burn line and a rising serving line cross; on 'a hypothesis', the cross fades to a question-marked plate. Motion onset after 0.3s; stable close. | hyperframes | giant-number | 8.0 |
| s6 | explain | Picture a kitchen. The chef chops instantly. Every ingredient arrives through a single narrow doorway. The chef is compute. The doorway is the memory bus, your unified memory. The ingredients are the model's weights, its stored knowledge. | chef = compute  /  doorway = memory bus  /  ingredients = model weights | Line-art kitchen rises in place on "Picture a kitchen"; chef label fades in on "chef is compute"; amber doorway glow scales in on "memory bus"; ingredient blocks fade in on "model's weights". Labels land one at a time. | hyperframes | diagram-flow | 13.0 |
| s7 | explain | To write each word, decode reads the active weights in through that doorway. It isn't thinking. It's reading. The burn measures the chef. Your answers wait on the doorway. | each word: read the weights  /  burn measures the chef  /  answers wait on the doorway | One loop group of weight blocks drifts through the doorway, onset on "reads the active weights" (after 0.3s); "the burn measures the chef" text fades in on that phrase. Loop settles for stable final frames. | hyperframes | centered-stack | 10.0 |
| s8 | explain | Where the myth still holds: prefill, the part that reads your whole prompt before answering. Reading your prompt is one big block of math, compute-bound like the burn. | prefill reads your prompt first  /  one big block of math | On 'one big block of math', a wide prompt bar scales in as a single block across the frame, amber edge. One beat; stable first and last 8 frames. | hyperframes | timeline | 9.5 |
| s9 | explain | On very long prompts, prefill ran flat to slightly slower. If your work is prompt-heavy, the burn drop is real for you. | flat to slightly slower  /  prompt-heavy? the drop is real | Result line rises in place on 'flat to slightly slower', flat then dipping slightly; amber flag fades in on 'real for you'. Stable close. | hyperframes | grid | 7.5 |
| s10 | explain | So here's the rule. Run the workload you actually run, before and after, same settings. Note its tokens per second, its answer speed. Trust that pair over any synthetic number. | run your real workload  /  before + after, same settings  /  trust the pair | Two-panel before/after checklist rises in place on "before and after"; amber check scales in on "Trust that pair". Only the check animates after panels settle. | hyperframes | split-compare | 10.5 |
| s11 | payoff_close | The burn said slower. Your model said faster. Benchmark the workload you actually run, and trust it. | burn: slower  /  model: faster  /  benchmark what you run | "slower" card and "faster" card fade in on their spoken phrases; final line rises in place on "Benchmark the workload you actually run". Hold stable to the end. | hyperframes | centered-stack | 6.0 |

## Notes for review
- Judge graft applied: "Here the lab offers a hypothesis, not a finding." (from draft B) keeps the kitchen mechanism at its true epistemic status; the brief lists the compute-vs-memory explanation as unverified.
- Numbers rounded once for the ear: the burn decline (about eleven percent) and the serving range (spoken as eight percent and four percent) are the brief's verbatim figures; the 23.1-to-25.0 tok/s pair was deliberately NOT spoken (one number per beat, cap of three).
- The doorway analogy's limit is stated in scene 8 ("reading your prompt is one big block of math").
- Scene 2's "That's the myth" and scene 8's "where the myth still holds" are the myth-bust frame; the myth is named, never mocked.
