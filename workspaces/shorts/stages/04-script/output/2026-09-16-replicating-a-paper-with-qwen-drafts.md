---
slug: 2026-09-16-replicating-a-paper-with-qwen
stage: 04-script
generated_at: 2026-09-16
---

# Drafts: Replicating a paper with Qwen-2.5 at home

Two blind drafts on kimi-k3 (separate processes, no shared context). Draft A: how-to-three-moves, tonight hook. Draft B: myth-bust, named-contradiction hook. Judge: kimi-k3 with the rubric and both storyboards, blind to the writing process.

## Draft A (how-to-three-moves) -- full narration

Three moves and the Jev trick runs on your Mac tonight. You already run Qwen two point five in Ollama or LM Studio. You've watched it type out JSON one word at a time. All your app wanted was a yes or no and a category. A program wants a decision, not a paragraph. On the author's M four Max run, a twenty-eight field form slogs through three hundred twelve passes. Here's the turn: the speed isn't in the weights. Jev refuses to write. It returns a probability for every allowed answer in one parallel shot. The replication is public on Hugging Face, built on the Qwen two point five checkpoint you may already have. One point five billion parameters, run through MLX, Apple's framework for these chips. No new training. Picture a numbered menu at a lunch counter. Normal decoding is spelling your order to the cashier letter by letter. Parallel constrained decoding, scoring choices instead of writing, is the cashier holding up your menu. You point once. The limit: menu items are independent, but your JSON fields can depend on each other. Here's why a stock model can do this. Prefill the document once into the KV cache, the model's saved memory of what it read. One forward pass, one trip through the model, scores every field at the same time. Code assembles the JSON from the winners. Move one: clone and install. You need an Apple Silicon Mac running macOS fourteen or later. Add Python three point ten or newer. Clone the parallel constrained decoding repo, then install its requirements into a fresh virtual environment. Move two: load the stock checkpoint and define your fields. Load it through MLX, unchanged, nothing to train. Each field is a boolean or an enum, a fixed list of allowed answers. Twenty-eight fields in the Enterprise Support Triage preset. Move three: mask the vocabulary and run. The runner hides every token, every chunk of a word, except each field's legal choices. Call run parallel generation. Then python three dash m core dot benchmark. On the author's M four Max, the benchmark prints two hundred seventy milliseconds for the form. Sequential forward passes fall from three hundred twelve to one. Valid JSON every run, by construction. Guaranteed shape is not guaranteed truth. Route low-confidence fields to a human or a bigger model. Three moves, stock weights, and it runs on your Mac tonight.

## Draft B (myth-bust) -- full narration, WINNER (post-fix text as judged)

Jev's speed isn't in the weights. Your Qwen already has it. Three hundred twelve forward passes become one. You run a small open model like Qwen two point five in Ollama or LM Studio. You've watched it type JSON one word at a time when the app needed a yes and a category. The myth says Jev's speed lives in exotic weights no home machine could serve. Yesterday TypeSafe released Jev, the first System One Model. It gives up writing text and returns structured values with calibrated probabilities, honest scores of how sure it is. Yet an open replication on Hugging Face hits those numbers. It's free under the Apache license, and it runs the stock Qwen checkpoint you can already download. No new training. One MacBook. The win is in how you decode, not what you train. You write a schema beforehand: the list of fields and their allowed answers. The test form has twenty-eight fields. Each is a boolean, a yes or no, or an enum, a fixed menu of choices. The old way writes an essay, one token, a chunk of a word, at a time. The new way is a scantron sheet. Every bubble at the same instant. The limit: a scantron chooses with no doubt, the engine returns a probability for every option. It's called parallel constrained decoding, every field answered in one pass. The prompt is prefilled once into a KV cache, the model's short-term memory, and shared across all fields. Each field scores only its own candidate tokens. The rest of the vocabulary is masked off. On the replication author's M four Max MacBook, this form took nineteen hundred milliseconds the old way. The new decoding took two hundred seventy milliseconds. Sequential forward passes, full trips through the model, fell from three hundred twelve to one. Another belief to drop: structured output isn't asking the model to please answer in JSON. The model never writes the JSON. Code assembles it. So the shape is valid every single time, by construction. But guaranteed shape is not guaranteed truth. A valid answer can still be a wrong answer. A one point five billion parameter model can flip a boolean between runs. Route low-confidence fields to a human or a bigger model. The myth survives in one place: weights decide what a model knows, so judgment needs a stronger model. For typed answers, the speed was never in the weights. It was in refusing to let the model write.

## Judge scores

| Row | Draft A | Draft B |
|-----|---------|---------|
| 1. Hook | 2 -- number and product early, tension only at "tonight" | 3 -- product plus contradiction by word four |
| 2. Payoff timing | 0 -- first concrete number near second twenty-two | 3 -- break lands in sentence one, proof by second four |
| 3. Specificity | 2 -- one sentence crams two numbers | 3 -- every number has a job |
| 4. Voice | 0 -- two numbers in one sentence; unspoken 1,900 on screen | 3 -- clean, right person, wry beat lands |
| 5. Navigation | 2 -- "Here's the turn" carries content, move labels enumerate | 3 -- every transition names what changed |
| 6. Difference | 2 -- new shape, opening echoes recent situation rhythm | 3 -- new shape, rhythm, and close |
| 7. Repeat test | 2 -- "Jev refuses to write" repeatable, close less quotable | 3 -- payoff is the repeatable line and last sound |
| 8. Teaching | 2 -- mechanism shown, limit stated not predictable | 3 -- viewer can sort future cases |
| **Total** | **12** | **24** |

## Winner

Draft B, 24 to 12. It pays off its contradiction hook inside four seconds, stays inside every hard constraint, and lands on a repeatable aphorism. No grafts.

Note: the judge scored A's row 4 against a pre-fix artifact (the on-screen 1,900 ms had already been removed before judging); corrected, A scores 15 and B still wins 24.

## What the losing shape needed

The how-to shape needed its turn in the first four seconds, opening on the 312-to-1 reveal so the three moves pay off an anchored promise instead of arriving after twenty-six seconds of situation. It also needed hard-constraint hygiene: split the twenty-eight-field and three-hundred-twelve-pass sentence, speak or cut the on-screen 1,900 ms, and make the move labels carry information the following sentences do not already carry.

## Fixes applied to the winner after judging (orchestrator, gate-driven)

- number_spend cap: 1,900 ms removed from s08 on-screen text (still spoken; the matcher counts on-screen numbers, and the "two hundred seventy milliseconds" ghost-match against Jev's vendor 70-to-500 ms row made the cap arithmetic strict).
- Long-scene advisories: s02 and s06 trimmed under the 16 s advisory; s11 tail cut from three sentences after payoff to two (band allows two).
- Lexicon: say-entries added for JSON ("jason"), LM, LM Studio; normalizer self-test 138/138 after the edit.
- est_duration_s recomputed at the measured 2.9 wps; target 139 s. Final validator: 0 blockers, 0 advisories. Eval: all nine gates pass.
