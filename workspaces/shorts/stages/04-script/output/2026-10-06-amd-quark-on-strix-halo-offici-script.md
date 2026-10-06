---
slug: 2026-10-06-amd-quark-on-strix-halo-offici
format: smooth-explainer
structure: myth-bust
style_pack: terminal
value_types: EQUIPS,TEACHES
promise: After this you can quantize a model on your own Strix Halo box tonight, and you know why unified memory makes that possible.
target_duration_s: 118
brief: 2026-10-06-amd-quark-on-strix-halo-offici-brief.md
drafts: 2026-10-06-amd-quark-on-strix-halo-offici-drafts.md
---

# Your Strix Halo box can quantize now

## Decisions
- Structures: myth-bust (B) vs how-to-three-moves (A); both cleared the rotation rule (last two shipped: comparison-ladder 10-05, news-react-so-what 10-02). B won 19 to 15 on the judge rubric.
- Hook: candidate 2, Number shock ("Ninety-five gigabytes of unified memory. One laptop quantized a model with that much memory."); candidate 1 (Situation) went to draft A. Two different patterns, and neither repeats the last two shipped hooks (decision, tonight).
- Graft: one sentence from A's move-two beat into B's Quark scene ("It runs Round-To-Nearest: no calibration data, the bluntest method on the shelf.") -- names the method and lands the one wry beat; no numbers added.
- Value lines: EQUIPS lands on the Quark scene ("installed with pip into AMD ROCm... export... no conversion step") and the close; TEACHES lands on the unified-memory scene (one pool, 128 GB, why the job fits).
- Unattended checkpoints: structures + promise locked to the pick's angle (official recipe, not launch news); hooks 1 and 2 picked from the ten, two patterns.
- Gates: validator 0 blockers 0 advisories; eval gates all pass (number_spend 3 of max 3 on screen, hook_concrete, scene_specificity 9 of 11 with allow_generic 2, skeleton, positional_labels, sameness 0 violations over 5 comparisons); normalizer scenes_changed 7.
- Style pack: terminal (topic fit 5 keyword hits; previous pack signal). Two-draft eval JSONs were merged into the final [slug]-eval.json; draft-A board withdrawn after judging per the two-round rule (it passed all gates in round 1).

## Hook candidates
1. You run other people's quants. Your Strix Halo box can make its own. *
2. Ninety-five gigabytes of unified memory. One laptop quantized a model with that much memory. *
3. Seventy gigabytes in. Twenty-one gigabytes out. Same machine.
4. Your Strix Halo box just learned to quantize its own models.
5. Making a quant yourself used to need a data-center card. Not anymore.
6. AMD shipped an official recipe for quantizing on your Strix Halo machine.
7. Stop tweaking llama.cpp flags. AMD's official quantizer runs on the APU itself.
8. The box that runs your quants can now make them.
9. Quantize a thirty-five-billion-parameter model on the machine it runs on.
10. AMD Quark turns your Strix Halo box into its own quant factory.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Ninety-five gigabytes of unified memory. One laptop quantized a model with that much memory. | 95 GB / one laptop | Frame 1: giant amber "95 GB" fully legible on a dark field; motion onset at 0.4 s as the figure scales up and settles, caption "one laptop" fades in below on "One laptop". | hyperframes | giant-number | 4.5 |
| s02 | foreshadow | On a Strix Halo box, you run GGUF model files, the kind Ollama and LM Studio load. Someone else quantized them, compressed the numbers so the file shrinks. The rule everyone repeats: doing that yourself takes a data-center GPU, or a big discrete card. | GGUFs you download · rule: data-center GPU | Split screen on "you run GGUFs": left card "GGUFs you download" fades in (0.3s); on "The rule everyone repeats", right card "rule: data-center GPU" rises; thin divider fades between them. | hyperframes | split-compare | 15.2 |
| s03 | explain | How does a laptop have room for that? Strix Halo uses unified memory, one pool the processor and the graphics chip share. The big configs give that pool one hundred twenty-eight gigabytes of memory. Enough for the model, plus the working space quantizing needs. | 128 GB | Animated diagram on "one pool the processor and the graphics chip share": rounded pool shape scales in (0.5s), arrows rise from it to CPU and GPU blocks; "128 GB" fades in inside the pool on "one hundred twenty-eight gigabytes". | manim | diagram-flow | 15.2 |
| s04 | explain | And on this chip, size is speed. That one pool moves everything at two hundred fifty-six gigabytes per second. Generating tokens means streaming the weights through it, so a smaller file means faster tokens. | smaller file, faster tokens | Centered stack on "size is speed": headline scales in (0.4s); on "streaming the weights", a row of small weight blocks rises beneath the headline, one after another. | hyperframes | centered-stack | 12.1 |
| s05 | explain | Quantizing stores each weight as a four-bit integer, not a sixteen-bit float. Rounding pi to a few digits keeps most of the number. That is how your Ollama library got small. The loss isn't uniform, though. Exact math notices first, casual chat never does. | rounding pi · most accuracy survives | Split-compare on "rounding pi": left card "rounding pi" fades in (0.3s); right card "most accuracy survives" scales in on "keeps most of the number"; on "exact math notices first" the right card text fades to "loss isn't uniform". | hyperframes | split-compare | 14.8 |
| s06 | explain | Here's the measurement that breaks the rule. AMD's own walkthrough quantizes a Mixture-of-Experts model, one where only a slice fires per token. It happens entirely on a Strix Halo machine. The weights fall from seventy gigabytes to about twenty-one gigabytes of quantized model. | 70 GB -> 21 GB / quantized on-device | Giant number on "seventy gigabytes": "70 GB" scales in (0.4s); on "twenty-one gigabytes" it scales down as "-> 21 GB" scales in beside it; caption "quantized on-device" fades in on "on a Strix Halo machine". | hyperframes | giant-number | 14.8 |
| s07 | explain | The toolkit is Quark, AMD's open-source quantizer, installed with pip into AMD ROCm. You load the full-size model and run it. It runs Round-To-Nearest: no calibration data, the bluntest method on the shelf. The quant pass takes a minute and a half. | pip install · quantize | Horizontal timeline on "installed with pip": node "pip install" rises (0.3s); "quantize" rises on "run it"; the timer chip fades in on "a minute and a half". | hyperframes | timeline | 14.5 |
| s08 | explain | Export writes GGUF for your apps, or safetensors, the format the vLLM serving engine loads, with no conversion step. | export · no conversion step | Two-cell grid on "Export writes GGUF": cell "GGUF for your apps" fades in; cell "safetensors for vLLM" rises on "vLLM serving engine loads". | hyperframes | split-compare | 5.9 |
| s09 | foreshadow | Where is the old rule still right? Where memory is smaller: a sixty-four-gigabyte Framework Desktop can't fit that peak. Where quality matters: AMD's own tests show four-bit slipping on hard reasoning. | smaller memory · task-dependent quality | Two-cell grid: cell "smaller memory" fades in on "Where memory is smaller"; cell "task-dependent quality" rises on "Where quality matters". | hyperframes | grid | 11.7 |
| s10 | explain | And where the quant you want already exists: when Ollama ships the four-bit file, downloading beats spending twenty-two minutes on export. | downloading beats export | Split-compare: left card "download it now" fades in; right card "export for twenty-two minutes" rises on "twenty-two minutes". | hyperframes | split-compare | 10.0 |
| s11 | payoff_close | So tonight, the hidden half of local AI moves onto your own desk. The box that runs your quants can now make them. | runs your models · makes your quants | Centered stack on "runs your quants": line "runs your models" fades in (0.4s); on "can now make them", line "makes your quants" scales in beneath; hold to end. | hyperframes | centered-stack | 6.9 |

## Notes for review
- Hook "One laptop" against the brief's desktop boxes: the blog machine was an ASUS ROG Flow Z13 (a tablet/laptop), so "laptop" is defensible, but if review prefers precision swap to "one machine" (the 5-14 word hook sentence still passes).
- The "95 GB" hook number is the quantization peak, not a runtime footprint; the scene speaks it as memory used while quantizing ("quantized a model with that much memory"), which matches claim 3.
- Judge flagged that "that peak" (s09) leans on the hook's minute-old number; deliberate recall, the documented loop-anchor exception.
- Every number verbatim from the brief (95 GB, 128 GB, 256 GB/s, 70 GB -> 21 GB, 1.5 min, 22 min, 64 GB); nothing rounded.
- The RTN sentence is the graft from draft A and the script's one wry beat.
