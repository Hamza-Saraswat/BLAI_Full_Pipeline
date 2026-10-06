---
slug: 2026-10-06-amd-quark-on-strix-halo-offici
judge: kimi-k3 (blind, third call)
date: 2026-10-06
---

# Drafts: 2026-10-06-amd-quark-on-strix-halo-offici

Both drafts written blind from the same brief (two kimi-k3 calls, private scratch dirs). Draft A: how-to-three-moves, situation hook, 9 scenes, 99 s. Draft B: myth-bust, number-shock hook, 11 scenes, 118 s. Both passed validator (0 blockers) and all eval gates before judging.

## Draft A (how-to-three-moves, situation hook) -- full table

```
TITLE: AMD Quark quantizes on your Strix Halo
NARRATION_WORDS: 284
EST_TOTAL_S: 98.0

| id | role | tool | layout_archetype | narration | on_screen_text | est_s |
| s01 | hook | hyperframes | centered-stack | You run other people's quants. Your Strix Halo box can make its own. AMD's Quark, an open-source quantization toolkit, runs the whole job on the machine itself. | Your Strix Halo makes its own quants | 9.3 |
| s02 | explain | manim | diagram-flow | Quantization, squashing sixteen-bit weights down to four-bit ones, is the step you never see. Think rounding pi to fewer digits. The number stays itself for almost everything. Exact arithmetic notices first, casual chat never does. | fewer digits same number | 12.1 |
| s03 | explain | hyperframes | split-compare | Your chip keeps everything in unified memory, one pool shared by processor and graphics. On your one hundred twenty-eight gigabyte machine, smaller weights stream faster. The pool feeds tokens at two hundred fifty-six gigabytes per second. | one pool shared by everything | 12.4 |
| s04 | foreshadow | hyperframes | centered-stack | Move one: install Quark into a Python environment with ROCm, AMD's GPU stack. Then load the sixteen-bit checkpoint with transformers, the model-loading library. Pick a thirty-five billion parameter Mixture-of-Experts, where only a slice of weights fires per token. | pip install amd-quark | 13.1 |
| s05 | foreshadow | hyperframes | grid | Move two: pick symmetric four-bit with group size thirty-two, and run the quantizer. Group size is how many weights share one scale. Round-To-Nearest, no calibration data, the bluntest method on the shelf. The run takes a minute and a half. | group size thirty two then 1.5 min | 13.8 |
| s06 | explain | hyperframes | giant-number | While it runs, memory use peaks at ninety-five gigabytes of the shared pool. That is the whole quantization, inside your machine, no data-center card. | 95 GB peak memory | 8.3 |
| s07 | explain | hyperframes | split-compare | The model drops from roughly seventy gigabytes to about twenty-one gigabytes of quantized weights. AMD's own accuracy runs say the cost depends on the task. No four-bit recipe wins everywhere. | 70 GB -> 21 GB | 10.0 |
| s08 | foreshadow | hyperframes | timeline | Move three: export GGUF, the file format llama.cpp loads, with no conversion step. llama.cpp is the engine under Ollama and LM Studio. Or export safetensors, the checkpoint format the vLLM serving engine loads. | export GGUF no conversion step | 11.4 |
| s09 | payoff_close | hyperframes | centered-stack | Lemonade, the AMD-supported local chat app, serves your GGUF and the model answers. Other people's quants got you this far. This one is yours. | this one is yours | 8.3 |
```

## Draft B (myth-bust, number-shock hook) -- full table (winner, after graft)

```
TITLE: Your Strix Halo box can quantize now
NARRATION_WORDS: 359
EST_TOTAL_S: 118

| id | role | tool | layout_archetype | narration | on_screen_text | est_s |
| s01 | hook | hyperframes | giant-number | Ninety-five gigabytes of unified memory. One laptop quantized a model with that much memory. | 95 GB / one laptop | 4.5 |
| s02 | foreshadow | hyperframes | split-compare | On a Strix Halo box, you run GGUF model files, the kind Ollama and LM Studio load. Someone else quantized them, compressed the numbers so the file shrinks. The rule everyone repeats: doing that yourself takes a data-center GPU, or a big discrete card. | GGUFs you download · rule: data-center GPU | 15.2 |
| s03 | explain | manim | diagram-flow | How does a laptop have room for that? Strix Halo uses unified memory, one pool the processor and the graphics chip share. The big configs give that pool one hundred twenty-eight gigabytes of memory. Enough for the model, plus the working space quantizing needs. | 128 GB | 15.2 |
| s04 | explain | hyperframes | centered-stack | And on this chip, size is speed. That one pool moves everything at two hundred fifty-six gigabytes per second. Generating tokens means streaming the weights through it, so a smaller file means faster tokens. | smaller file, faster tokens | 12.1 |
| s05 | explain | hyperframes | split-compare | Quantizing stores each weight as a four-bit integer, not a sixteen-bit float. Rounding pi to a few digits keeps most of the number. That is how your Ollama library got small. The loss isn't uniform, though. Exact math notices first, casual chat never does. | rounding pi · most accuracy survives | 14.8 |
| s06 | explain | hyperframes | giant-number | Here's the measurement that breaks the rule. AMD's own walkthrough quantizes a Mixture-of-Experts model, one where only a slice fires per token. It happens entirely on a Strix Halo machine. The weights fall from seventy gigabytes to about twenty-one gigabytes of quantized model. | 70 GB -> 21 GB / quantized on-device | 14.8 |
| s07 | explain | hyperframes | timeline | The toolkit is Quark, AMD's open-source quantizer, installed with pip into AMD ROCm. You load the full-size model and run it. It runs Round-To-Nearest: no calibration data, the bluntest method on the shelf. The quant pass takes a minute and a half. | pip install · quantize | 14.5 |
| s08 | explain | hyperframes | split-compare | Export writes GGUF for your apps, or safetensors, the format the vLLM serving engine loads, with no conversion step. | export · no conversion step | 5.9 |
| s09 | foreshadow | hyperframes | grid | Where is the old rule still right? Where memory is smaller: a sixty-four-gigabyte Framework Desktop can't fit that peak. Where quality matters: AMD's own tests show four-bit slipping on hard reasoning. | smaller memory · task-dependent quality | 11.7 |
| s10 | explain | hyperframes | split-compare | And where the quant you want already exists: when Ollama ships the four-bit file, downloading beats spending twenty-two minutes on export. | downloading beats export | 10.0 |
| s11 | payoff_close | hyperframes | centered-stack | So tonight, the hidden half of local AI moves onto your own desk. The box that runs your quants can now make them. | runs your models · makes your quants | 6.9 |
```

## Judge scores

| Row | Draft A | Draft B |
|-----|---------|---------|
| 1 Hook | 3 | 2 |
| 2 Payoff timing | 1 | 3 |
| 3 Specificity | 3 | 2 |
| 4 Voice | 0 | 0 |
| 5 Navigation | 1 | 3 |
| 6 Difference | 2 | 3 |
| 7 Repeat test | 3 | 3 |
| 8 Teaching | 2 | 3 |
| **Total** | **15** | **19** |

Verdict verbatim (kimi-k3, 2026-10-06):

- WINNER: B
- GRAFT: one sentence from A s05 into B s07 ("It runs Round-To-Nearest: no calibration data, the bluntest method on the shelf.") -- B never names the method or that it needs no calibration data; carries the one wry beat B lacks; adds no number, fits person and sentence cap, mid-script wit placement.
- LOSER_POSTMORTEM: "The how-to buried its own result behind sixty seconds of setup, so the hook's promise stayed unpaid past second ten, and its Move one/two/three labels survive deletion untouched, which is mechanical filler. To win it needed the seventy-to-twenty-one on-device result front-loaded as the hook, transitions that carry the steps instead of numbering them, and no out-of-brief claims like Lemonade."
- Row notes: r2 A's promise unpaid at second ten (lands ~s07), B lands within seconds of the break; r5 A's move-labels fail the deletion test, B's question transitions name what changed; r6 A's situation hook repeats the 2026-10-01 script, B's shape/opening/close are all new; r8 B enumerates where the old rule still holds so the viewer can predict unmentioned cases.

Orchestrator note on the postmortem: "out-of-brief claims like Lemonade" is wrong -- Lemonade is claim-2/claim-13 glossary material in the brief. The scores stand; no draft change from this remark.

## What the losing shape would have needed

Per the judge: the on-device result front-loaded into the hook, content-carried transitions instead of move labels, and payoff by second 4. The how-to shape remains the right pick when the process is the story (a shorter, classic-band how-to); for this topic the myth ("you need a data-center card") was the stronger opening because the measurement breaks it immediately.
