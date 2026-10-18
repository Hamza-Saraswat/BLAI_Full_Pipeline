---
slug: 2026-10-18-nemotron-3-5-super-vl-is-nvfp4
stage: 04-script
generated_at: 2026-10-18
judge: kimi-k3 (blind, rubric as system file)
---

# Drafts: 2026-10-18-nemotron-3-5-super-vl-is-nvfp4

Both drafts passed all hard machine gates before judging (validator 0 blockers; eval gate1_ready true; soft advisories only: entity_spend/top2).

### Draft A: Nemotron NVFP4: your GPU might be too old (structure worked-example, hook You downloaded the wrong Nemotron.)

- s1 (hook, giant-number, 5.3s): You downloaded the wrong Nemotron. The seventy-five gigabyte file everyone grabbed may not run on your card.
- s2 (explain, diagram-flow, 5.9s): Inside, weights are quantized, stored in fewer bits, four each. Sixteen weights share a scale, which shrinks the file.
- s3 (explain, split-compare, 7.8s): Four-bit math at speed needs Blackwell tensor cores. Compute capability, your GPU's feature version, must read ten point zero. The blocker is generation, not size.
- s4 (explain, timeline, 9.1s): Below that version, grab a GGUF re-quant, the format llama.cpp tools load, rebuilt from the reference weights. The re-quant is a power adapter, except this one rebuilds the appliance.
- s5 (explain, giant-number, 3.4s): Unsloth's re-quant ladder starts at forty-six point one gigabytes of download.
- s6 (payoff_close, centered-stack, 6.9s): Check your card's compute capability: ten point zero takes the file, older takes the re-quant. Not a file size, a hardware commitment.

### Draft B: NVFP4 isn't just a quant: which file runs (structure myth-bust, hook Everyone says just quantize it.)

- s1 (hook, centered-stack, 5.3s): Everyone says just quantize Nemotron's four-bit file. llama.cpp's maintainers told one user: your converter can't unpack it.
- s2 (explain, diagram-flow, 5.6s): Quantization means storing weights in fewer bits. Each weight gets four bits. Sixteen values share a single scale.
- s3 (explain, giant-number, 6.9s): Only Blackwell tensor cores, NVIDIA's newest math silicon, run it at speed. The gate: compute capability, the hardware version, ten point zero.
- s4 (explain, timeline, 6.6s): Files that run anywhere are GGUF, llama.cpp's format, re-quantized from the sixteen-bit reference. Its four-bit-flavored re-quant is seventy-nine gigabytes of download.
- s5 (explain, split-compare, 7.8s): The re-quant is a power adapter, except this one rebuilds the appliance. On a Blackwell DGX Spark, the myth holds. Nemotron's checkpoint is the file.
- s6 (payoff_close, centered-stack, 2.2s): Not a file size. A hardware commitment.

## Score table

| # | Row | A | B | Reason |
|---|-----|---|---|--------|
| 1 | hook | 3 | 2 | A names the product and a viewer-felt accusation inside five words; B opens on a generic 'everyone says' claim whose product arrives at word five and whose tension only lands with the bust. |
| 2 | payoff_timing | 3 | 2 | A's 75 GB reveal and 'may not run on your card' land by about second four and are exactly what the hook promised; scored from the break per the fairness note, B's 'your converter can't unpack it' completes near second five. |
| 3 | specificity | 3 | 2 | A spends five numbers one per beat and ends on the actionable 46.1 GB floor; B spends its one size number on the less useful 79 GB flavor while its scene-4 visual brief cues 46.1 and 132 bars the narration never speaks. |
| 4 | voice | 2 | 3 | Both are clean and in the right person, but B's 'except this one rebuilds the appliance' is a wry beat that lands unexplained, while A has no wry beat and uses the 'not X' construction twice. |
| 5 | navigation | 3 | 2 | A's transitions each name what changed (inside the file, the gate, below the version, the caveat) and the order cannot be shuffled; B's adapter beat restates s4's point and could be deleted without breaking the script. |
| 6 | difference | 2 | 1 | A's accusation hook and check-your-card close differ from the last two scripts though the worked-example skeleton and 34-second length are familiar; B reruns the channel's recent myth-bust shape and closes on the same terse antithesis aphorism as 'the api was never the model.' |
| 7 | repeat_test | 2 | 3 | A's quotable line ('The blocker is generation, not size') sits mid-script while its actual payoff is a rule; B's payoff 'Not a file size. A hardware commitment.' is the repeatable line and the last thing heard. |
| 8 | teaching | 3 | 3 | Both show the four-bits-sixteen-to-a-scale mechanism concretely and hand the viewer a compute-capability-10.0-versus-GGUF rule that predicts cards the script never names. |

**Winner: A, 21 to 18.**

## Grafts applied
- From B into s4: "The re-quant is a power adapter, except this one rebuilds the appliance." -- Supplies the one landing wry beat A lacks and states the re-quant's rebuilt-weights limit exactly where the alternative is introduced.
- From B into s5: "Not a file size. A hardware commitment." -- Placed after the compute-capability rule it becomes the payoff, giving A a repeatable line as the last thing heard instead of a mid-script one.

## What the losing shape needed
B needed a hook that names the product with a viewer-felt tension in the first five words and a faster break, plus its one size number spent on the actionable 46.1 GB floor its own visual was already drawing. It also needed a landing that is not the same terse-antithesis aphorism the channel closed a myth-bust with three scripts ago, and the actionable check-your-compute-capability rule A ends on.
