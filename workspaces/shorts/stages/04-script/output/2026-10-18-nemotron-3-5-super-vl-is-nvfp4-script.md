---
slug: 2026-10-18-nemotron-3-5-super-vl-is-nvfp4
format: classic
structure: worked-example
style_pack: silicon
value_types: TEACHES,REFRAMES
promise: after half a minute the viewer can check their GPU's compute capability and know whether to grab the NVFP4 checkpoint or a GGUF re-quant
target_duration_s: 37
brief: 2026-10-18-nemotron-3-5-super-vl-is-nvfp4-brief.md
drafts: 2026-10-18-nemotron-3-5-super-vl-is-nvfp4-drafts.md
---

# Nemotron NVFP4: your GPU might be too old

## Decisions
- Structures tried: worked-example (A) vs myth-bust (B); A won 21-18 on the judge rubric (hook, payoff timing, specificity, navigation; B took voice and repeat-test).
- Hook: "You downloaded the wrong Nemotron." (wrong-diagnosis, candidate 1); B's named-contradiction opener was the runner-up.
- Grafts from B: the power-adapter wry line into s4 (its limit clause stated in the same breath) and the "Not a file size, a hardware commitment." close, now the payoff line.
- Draft B needed two eval rounds (hook entity, key-number spend, specificity); split of A's 14 s beat produced this 6-scene shape.
- Soft gates kept with reason: entity_spend 0.065 and top2 (NVIDIA, Blackwell absent as literal tokens; the script says "NVIDIA's" once and "Blackwell tensor cores" once, the extractor misses possessive/plural forms) and B kept entity_spend 0.161. Hard gates all pass; sameness clean against the last five.
- Style pack silicon (4 keyword hits; previous video terminal). Recorded.

## Hook candidates
1. * You downloaded the wrong Nemotron.
2. Everyone says just quantize it.
3. Seventy-five gigabytes your GPU cannot read.
4. NVIDIA's new four-bit file skips your GPU.
5. Your GPU isn't too small. It's too old.
6. Check one number before you download Nemotron.
7. The most downloaded Nemotron won't run here.
8. Blackwell only: NVIDIA shipped a format gate.
9. Can your card do four-bit math?
10. A 120B model your 4090 can't touch.

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s1 | hook | You downloaded the wrong Nemotron. The seventy-five gigabyte file everyone grabbed may not run on your card. | You downloaded the wrong Nemotron. | 75 GB NVFP4 | Frame 1: dark canvas, hook line 'You downloaded the wrong Nemotron.' centered in the upper third, fully legible. At 0.35 s a file card labeled 'NVFP4' rises in place at center; on  | hyperframes | giant-number | 5.3 |
| s2 | explain | Inside, weights are quantized, stored in fewer bits, four each. Sixteen weights share a scale, which shrinks the file. | 4 bits per weight | 16 weights share a scale | Sixteen small square cells fade in as a row under 'weights are quantized'; on 'four each' each cell is stamped '4 bits'. On 'Sixteen weights share a scale' the stamps fade out, the | manim | diagram-flow | 5.9 |
| s3 | explain | Four-bit math at speed needs Blackwell tensor cores. Compute capability, your GPU's feature version, must read ten point zero. The blocker is generation, not size. | 4-bit math | compute capability 10.0 | Blackwell only | On 'needs Blackwell tensor cores' two GPU slabs fade in side by side: left labeled 'Blackwell' with lit amber traces, right dim gray labeled 'older'. On 'must read ten point zero'  | hyperframes | split-compare | 7.8 |
| s4 | explain | Below that version, grab a GGUF re-quant, the format llama.cpp tools load, rebuilt from the reference weights. The re-quant is a power adapter, except this one rebuilds the appliance. | GGUF re-quant | from BF16 reference | The gate line fades as a horizontal ladder base fades in on 'Below that version'. On 'grab a GGUF re-quant' three rung cards rise in place, the first labeled 'GGUF re-quant'. On 'r | hyperframes | timeline | 9.1 |
| s5 | explain | Unsloth's re-quant ladder starts at forty-six point one gigabytes of download. | Unsloth GGUF | from 46.1 GB | Giant amber '46.1 GB' types on over the dark slab as the narration says 'forty-six point one'; a thin capacity bar fills beneath it to the 'gigabytes of download' phrase, comparing | manim | giant-number | 3.4 |
| s6 | payoff_close | Check your card's compute capability: ten point zero takes the file, older takes the re-quant. Not a file size, a hardware commitment. | 10.0 -> NVFP4 | older -> GGUF | a hardware commitment | On 'A re-quant is different weights' the line 'different weights, not unpacked' fades in at center, then fades out on 'Check your card's compute capability' as two stacked cards fa | hyperframes | centered-stack | 6.9 |

## Notes for review
- The "wrong Nemotron" hook is an accusation; it lands only because the payoff line returns the agency (check compute capability, grab its file). If it reads harsh, candidate 5 keeps the shape.
- Seventy-five gigabytes is the repo storage figure (75,049,013,059 bytes); spoken as the rounded "seventy-five gigabyte file". 7,599 downloads last month is on screen in s1 but never spoken (number budget).
- The power-adapter analogy graft states its limit in the same sentence ("except this one rebuilds the appliance"); do not trim that clause.
- MMLU-ProX quality delta deliberately not spent (one-number-at-a-time budget); the honest catch is carried by "different weights, not the originals unpacked" in s6's screen text and the adapter limit.
- No tokens-per-second claim anywhere (Unverified in the brief).
