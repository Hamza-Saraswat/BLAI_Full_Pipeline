---
slug: 2026-09-30-best-local-coding-llm-what-act
stage: 04-script
generated_at: 2026-09-30
judge: kimi-k3 (blind, rubric-only)
---

# Drafts: Best local coding LLM: what actually fits 128 GB

Both drafts written blind by separate kimi-k3 calls from the same brief; structures assigned by fit and rotation (comparison-ladder, contrarian-take).

### Draft A (winner, comparison-ladder): comparison-ladder
  s1 [hook/centered-stack] gpt oss or G L M? File size decides. You've got one hundred twenty-eight gigabytes of unified memory, one shared pool, and a coding habit to feed tonight.
  s2 [explain/diagram-flow] Unified memory means one pool. Your model weights live in it. So does the K V cache, the scratchpad that grows with every line of context. So does your operating system. The file has to fit with room left over, or nothing runs.
  s3 [explain/split-compare] Total parameters decide whether it fits. Active parameters decide how fast it thinks. The two numbers pull in opposite directions.
  s4 [explain/diagram-flow] It's a mixture of experts, a model that wakes a small slice of itself for each word. All of it sits in your memory. Only the slice does the thinking.
  s5 [explain/giant-number] Start with cost. Ollama ships gpt oss in exactly one quant, a single sixty-five-gigabyte download, and one command starts it. A quant is just a compression setting, fewer bits per weight. Sixty-five gigabytes leaves real headroom.
  s6 [explain/split-compare] Now speed, because fitting is not flying. The llama dot cpp maintainer measured this model on this exact class of hardware. It reads back at forty-five point three four tokens a second. That's typing speed, not waiting speed.
  s7 [explain/timeline] G L M four point five Air is the other survivor. Its recommended quant, the file the makers suggest, still fits with room to spare, and a richer quant fits too.
  s8 [explain/giant-number] Its decode speed here? Nobody has measured it on this hardware. What you get instead is more quality per gigabyte of memory.
  s9 [explain/grid] Now the honest catch. On the software engineering benchmark, a board built from real GitHub fixes, the open leaders score far above gpt oss. No page we found has measured them here.
  s10 [explain/diagram-flow] Those leaders are full-size models, G L M, Kimi, DeepSeek. Whether any of them fits your box at all, nobody has measured it.
  s11 [payoff_close/centered-stack] pull gpt oss tonight, the measured, one-command pick. Switch to G L M four point five Air when you want more quality per gigabyte of memory. The crown stays in the cloud; the coding stays on your desk.

### Draft B (contrarian-take): contrarian-take
  s1 [hook/centered-stack] Your leaderboard isn't wrong about skill. Your memory math is. You've got one hundred twenty-eight gigabytes of unified memory, one shared pool, and a coding habit to feed tonight.
  s2 [explain/giant-number] Here's the problem. The top open coder family on the software engineering benchmark is MiniMax. Its recommended download is one hundred thirty-eight point five nine gigabytes of model file.
  s3 [explain/split-compare] Your whole machine is one hundred twenty-eight gigabytes of unified memory. It does not fit.
  s4 [explain/grid] What about the leaders themselves, MiniMax M two point five, G L M five, Kimi K two point five? Nobody has measured them on a machine like yours. Their fit here is a blank page.
  s5 [explain/split-compare] Total parameters decide whether it fits. Active parameters decide how fast it thinks. Fit and speed are different numbers, and they pull apart.
  s6 [explain/diagram-flow] It's a mixture of experts, a model that wakes a small slice of itself for each word. All of it must sit in memory. Only the slice does the work.
  s7 [explain/giant-number] So take the OpenAI oss model. It ships as one sixty-five gigabyte download, one command in Ollama, and nothing to pick: the runtime ships exactly one quant, M X F P four.
  s8 [explain/timeline] On this class of machine it was measured at forty-five point three four tokens a second. That's reading speed, not waiting speed.
  s9 [explain/giant-number] Now the honest part. On that same board, the oss model posts twenty-six point zero zero. The leaders post seventy-five point eight zero.
  s10 [explain/centered-stack] That gap is real, so buy it with open eyes. You trade the leaderboard crown for a coder that runs where you sit. Ollama starts it, no API key, nothing leaves the desk.
  s11 [explain/split-compare] There's a solid runner-up: G L M four point five Air also fits, and it's the quality pick per gigabyte of memory.
  s12 [payoff_close/centered-stack] The best local coding model isn't the best coding model. It's the best one that fits and still flies. On your machine that's the oss one twenty b, and one command in Ollama starts the download tonight.

## Judge scores (0-3 per row)

| Row | A | B | Why A | Why B |
|-----|---|---|-------|-------|
| hook | 3 | 1 | names both products and the decision tension inside the first five words, 'File size decides' lands the stakes immediately | no product or number; 'your leaderboard isn't wrong' could open any benchmark-distrust video |
| payoff_timing | 1 | 2 | no concrete number until the 65GB rung around second 40, and the 128GB premise is never spoken at all | the break lands at ~2s and the 128GB premise number lands by ~5s, concrete before second 8 |
| specificity | 1 | 1 | capped by drift: 'Nobody has measured it' speaks an absence as assertion; numbers otherwise well spent, SWE-bench gap left qualitative | capped by the same drift ('Nobody has measured them'); otherwise the best number work in either draft, six figures each with unit and referent |
| voice | 0 | 0 | the 45.34 t/s sentence runs 24 spoken words, breaking the 20-word hard cap | sentences of 26 and 22 spoken words break the hard cap, and the 'not X but Y' move fires three times |
| navigation | 2 | 3 | transitions mostly carry content ('Now speed, because fitting is not flying') but 'Start with cost' is a rung label and the ladder rungs could swap order | break, blank leaders, mechanism, pick, honest cost is a causal chain that resists reordering, and 'So take the OpenAI oss model' is a true consequence jump |
| difference | 1 | 1 | comparison-ladder repeats the 09-27 structure and 111s repeats the 09-28 duration; hook pattern is new | contrarian-take repeats the 09-26 structure and 111s repeats the recent run's duration; wrong-diagnosis hook is new |
| repeat_test | 3 | 2 | 'The crown stays in the cloud; the coding stays on your desk' is the payoff, the quotable line, and the last thing heard | 'fits and still flies' is the quotable line but the command sentence, not the aphorism, is the last thing heard |
| teaching | 3 | 3 | pool-sharing plus total-vs-active parameters lets the viewer predict fit and speed for any future MoE or dense model | same mechanism as A plus a rerunnable check, recommended file size against your memory, that the viewer can apply to the next hot model |

**Totals: A 14, B 13. Winner: A, margin 1.**

## Grafts
- Applied, from B: the 128 GB premise sentence into A's hook (A never spoke the number its whole argument depends on).
- Declined: B's 26.00/75.80 score pair for A's qualitative catch; the number cap was already spent.

## What B would have needed
The contrarian shape needed its break to carry a name or a number in the first five words, and its own candidate list held exactly that hook ('One hundred thirty-nine gigabytes. Your whole machine is one hundred twenty-eight.'); it also needed to end on its repeatable aphorism ('fits and still flies') instead of demoting it behind the command sentence. Splitting its two over-cap sentences (twenty-six and twenty-two words) and reconciling notes that contradict its own narration (65GB called 'unspoken' while spoken, scene IDs off by two) would have brought the package up to A's cleanliness.
