# How to work out which local model actually fits the graphics card you own, and where the popular rule of thumb breaks: research brief

## Summary

The number that decides whether a model runs is the file size plus its cache, not the parameter count. The rule everyone repeats, take a bigger model at lower precision, holds for knowledge questions and reverses for reasoning.

## Thesis

The number that decides whether a model runs is the file size plus its cache, not the parameter count. The rule everyone repeats, take a bigger model at lower precision, holds for knowledge questions and reverses for reasoning.

## Explanation path

Open on the card the viewer owns and the question they actually type: can I run this. Establish that the parameter count is the wrong number and the file size is the right one, using one model whose quant ladder spans every card tier. Then add the second cost nobody budgets for, the cache that grows with the conversation, and give the arithmetic in a form a viewer can hold. Only then bring in the rule of thumb, because now they can see what it trades away, and show the measurement where it reverses. Close on the decision rule and on who should ignore it.

## Viewer situation

You have a graphics card with eight, twelve or twenty-four gigabytes, and a model page that tells you the parameter count and nothing you can act on.

## Has process

true

- Read the file size of the quant you want, not the parameter count
- Work out the cache cost for the context you actually run: two times layers times key-value heads times head dimension times bytes per value
- Subtract both from your card's memory and leave about a gigabyte of slack
- Pick the largest model that still fits at Q4_K_M or better, unless the work is reasoning or long context

Note: the long-form Transitions rule permits positional labels only in `build-along`, so this episode navigates by content regardless.

## Objection

Everyone says take the bigger model at lower precision, so why would I ever run a smaller model at higher precision?

## Claims

1. llama.cpp's own quantize table gives Llama-3.1-8B at F16 as 16.0005 bits per weight and 14.96 GiB, falling to Q4_K_M at 4.8944 bits per weight and 4.58 GiB. [primary, high] -- https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/quantize/README.md (accessed 2026-08-23)
2. Quantization labels are not their nominal bit width: Q4_K_M measures 4.8944 bits per weight, Q6_K 6.5633 and Q8_0 8.5008, because each carries block scales on top of the payload bits. [primary, high] -- https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/quantize/README.md (accessed 2026-08-23)
3. NVIDIA publishes the per-token cache formula as two times layers times heads times head dimension times bytes of precision, worked as roughly two gigabytes for Llama 2 7B at four thousand ninety-six tokens. [docs, high] -- https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ (accessed 2026-08-23)
4. That published formula uses attention heads, which is correct only for older multi-head models; a modern grouped-query model such as Qwen3-8B has thirty-two query heads but eight key-value heads, so using the printed formula overstates its cache by four times. [primary, high] -- https://huggingface.co/Qwen/Qwen3-8B/raw/main/config.json (accessed 2026-08-23)
5. A llama.cpp maintainer states there is no easy way to calculate the context size, and that the CUDA runtime needs memory that may not be accounted for elsewhere. [primary, medium] -- https://github.com/ggml-org/llama.cpp/discussions/10068 (accessed 2026-08-23)
6. Hugging Face states that all parameters of a mixture of experts must be loaded in memory, and that Mixtral 8x7B needs enough memory for a dense forty-seven billion parameter model while computing like a twelve billion one. [docs, high] -- https://huggingface.co/blog/moe (accessed 2026-08-23)
7. Ornith 1.5 9B ships a four-bit build at 5.63 GB and an eight-bit build at 9.53 GB, so its whole ladder through Q8_0 stays under ten gigabytes. [primary, high] -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF (accessed 2026-08-23)
8. Qwen3.8-27B is a dense twenty-seven billion parameter model whose published builds span 6.19 GB at UD-IQ1_S to 25.3 GB at UD-Q6_K_XL, so one model covers every consumer card tier. [primary, high] -- https://huggingface.co/unsloth/Qwen3.8-27B-GGUF (accessed 2026-08-23)
9. DeepSeek V4 Flash's smallest published quant is 82.5 GB, more than three times a twenty-four gigabyte card. [primary, high] -- https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF (accessed 2026-08-23)
10. NVIDIA's current consumer range runs from eight gigabytes at 448 GB/sec on the RTX 5060 to thirty-two gigabytes at 1792 GB/sec on the RTX 5090, so capacity and bandwidth move together across the range. [primary, high] -- https://www.nvidia.com/en-us/geforce/graphics-cards/compare/ (accessed 2026-08-23)
11. The DGX Spark pairs 128 GB of unified memory with 273 GB/s of bandwidth, which is less bandwidth than an eight gigabyte RTX 5050 at 320 GB/sec. [primary, high] -- https://www.nvidia.com/en-us/products/workstations/dgx-spark/ (accessed 2026-08-23)
12. Ollama does not refuse a model that does not fit; it splits the layers and reports the ratio, showing values such as forty-eight percent CPU and fifty-two percent GPU in ollama ps. [docs, high] -- https://docs.ollama.com/faq (accessed 2026-08-23)
13. llama.cpp's multi-GPU guide says lowering the GPU layer count is a last resort because the remaining layers run on CPU and inference will be much slower. [docs, high] -- https://github.com/ggml-org/llama.cpp/blob/master/tools/cli/README.md (accessed 2026-08-23)
14. Ollama warns that setting a larger context length increases the memory required, so context competes with weights for the same card. [docs, high] -- https://docs.ollama.com/context-length (accessed 2026-08-23)
15. The paper behind the four-bit rule of thumb concludes that four-bit precision is almost universally optimal for total model bits and zero-shot accuracy. [primary, high] -- https://arxiv.org/abs/2212.09720 (accessed 2026-08-23)
16. That result was measured on models from nineteen million to one hundred seventy-six billion parameters across BLOOM, OPT, NeoX/Pythia and GPT-2, on zero-shot accuracy only, with no instruction-tuned or reasoning evaluation and nothing released after 2022. [primary, high] -- https://arxiv.org/abs/2212.09720 (accessed 2026-08-23)
17. A 2025 controlled study across roughly seventeen hundred inference scenarios finds the opposite for reasoning: an eight billion parameter model at eight-bit consistently outperforms a fourteen billion model at four-bit, and a thirty-two billion model at four-bit is strictly dominated by both. [benchmark, medium] -- https://arxiv.org/abs/2510.10964 (accessed 2026-08-23)
18. Longer-trained models are more fragile under quantization: the measured degradation increases with training data size across all model sizes. [primary, high] -- https://arxiv.org/html/2411.04330 (accessed 2026-08-23)
19. Long context breaks four-bit hardest: eight-bit preserves accuracy to about a zero point eight percent drop while four-bit methods lose up to fifty-nine percent on long-context tasks. [benchmark, medium] -- https://arxiv.org/html/2505.20276v1 (accessed 2026-08-23)
20. On the llama.cpp perplexity table, Q8_0 costs plus zero point zero zero zero four perplexity at 7B and Q4_K_M costs plus zero point zero five three five, while Q2_K costs plus zero point eight six nine eight. [primary, high] -- https://github.com/ggml-org/llama.cpp/discussions/2094 (accessed 2026-08-23)
21. Compressed models can match a benchmark average and still change individual answers, flipping items from correct to incorrect and back. [benchmark, medium] -- https://arxiv.org/abs/2407.09141 (accessed 2026-08-23)

## Key numbers

- **Q4_K_M measured bits per weight**: 4.8944 -- https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/quantize/README.md
- **Llama-3.1-8B at F16 versus Q4_K_M**: 14.96 GiB to 4.58 GiB -- https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/quantize/README.md
- **Ornith 1.5 9B four-bit build**: 5.63 GB -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF
- **Qwen3.8-27B ladder, smallest to largest**: 6.19 GB to 25.3 GB -- https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
- **DeepSeek V4 Flash smallest published quant**: 82.5 GB -- https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF
- **RTX 5060 memory and bandwidth**: 8 GB GDDR7 at 448 GB/sec -- https://www.nvidia.com/en-us/geforce/graphics-cards/compare/
- **RTX 5090 memory and bandwidth**: 32 GB GDDR7 at 1792 GB/sec -- https://www.nvidia.com/en-us/geforce/graphics-cards/compare/
- **DGX Spark memory and bandwidth**: 128 GB LPDDR5x at 273 GB/s -- https://www.nvidia.com/en-us/products/workstations/dgx-spark/
- **Llama 2 7B cache at 4096 tokens**: ~2 GB -- https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/
- **Reasoning reversal, measured**: 8B at 8-bit beats 14B at 4-bit -- https://arxiv.org/abs/2510.10964
- **Long-context loss at four-bit**: up to 59% -- https://arxiv.org/html/2505.20276v1
- **Q4_K_M perplexity penalty at 7B**: +0.0535 ppl -- https://github.com/ggml-org/llama.cpp/discussions/2094

## Analogy candidates

- **packing a suitcase with a fixed weight allowance**: the card's memory is the allowance, the model file is the case itself, the cache is what you add on the way home, and the airline weighs the total not the case. Breaks when: a suitcase does not get heavier the longer the holiday runs, and the cache does: it grows with every word of the conversation

## Misconceptions

- **Myth**: A bigger model at lower precision always beats a smaller model at higher precision.  
  **Reality**: That holds for zero-shot knowledge questions on models from 2022, which is what the original paper measured. For reasoning the measured result reverses: an eight billion model at eight-bit beats a fourteen billion model at four-bit, and newer models degrade more under quantization than the ones the rule was derived from.
- **Myth**: A mixture of experts only needs memory for the parameters it activates.  
  **Reality**: Every expert has to be resident because the router can pick any of them for the next word. You budget memory for the total and get the speed of the active slice.
- **Myth**: The file size is the memory you need.  
  **Reality**: The file is the weights. The cache for your conversation sits on top and grows with the context, and the runtime takes its own slice that nobody publishes exactly.

## Glossary

- **quantization**: storing each of the model's numbers with fewer bits so the file gets smaller
- **GGUF**: the single-file format local runtimes read, holding the weights at a chosen precision
- **KV cache**: the running notes a model keeps on every word so far, held in memory beside the weights
- **grouped-query attention**: a design that shares the running notes between groups of attention heads, which cuts the cache several times over
- **mixture of experts**: a model split into many specialists where a router wakes only a few per word
- **memory bandwidth**: how fast the machine can move the model's weights out of memory, which sets how quickly words come out
- **offload**: putting the layers that do not fit on the graphics card into ordinary system memory, where the processor runs them slowly

## Unverified

- No primary source gives a quantified slowdown for CPU offload. llama.cpp says only 'much slower'. The three-to-five-times figures circulating are from SEO blogs with no measurements behind them; do not speak a multiple.
- Specific headroom advice such as 'leave 512 MiB' or 'leave ten to twenty percent' is folklore. The guide that carries it contains no benchmarks and no author measurements.
- The claim that four-bit is indistinguishable in normal conversation is unsourced. The perplexity delta is real; the perceptual claim is not measured, and one paper shows individual answers flip even at equal benchmark averages.
- The widely repeated 'Apple reserves twenty-five percent of unified memory' figure could not be confirmed from Apple. The only evidence found is a llama.cpp discussion implying about a third below thirty-two gigabytes and a quarter above.
- NVIDIA does not publish memory bandwidth for the RTX 4070, 4060, 3090 or 3070 on its consumer pages, only bus width.
- No NVIDIA statement was found on how much of the DGX Spark's 128 GB is usable for weights rather than reserved by the system.
- Ollama's context tiers are printed in GiB while GPU vendors print GB. A twenty-four gigabyte card sits just under Ollama's twenty-four GiB threshold, not at it. Check the unit before quoting a tier.
- The single-author preprint arXiv 2601.14277 is the source for the Q3 quality cliff and could not be confirmed as peer reviewed. Prefer the llama.cpp perplexity table for headline figures.
- Two Ornith model cards state eighty-gigabyte GPU requirements that their own file tables contradict, and one Qwen card lists a four-bit build at 1.68 GB beside another at 19 GB for the same model. Do not read a hardware line off a model card as fact.
- No first-party measurement was made for this episode. The DGX Spark was unreachable from the production machine, so every number here is published by somebody else and the episode must say so.

## Suggested outline

Chapter one: the card you own, the question you type, and the surprise that the parameter count is not the number that decides it. Chapter two: the file size is the real number, shown on one model whose ladder spans every card. Chapter three: the second cost, the cache that grows with the conversation, and the arithmetic in a form you can hold. Chapter four: the rule everyone repeats, and the measurement where it reverses. Chapter five: the decision rule, and who should ignore it.

## Sources

- https://arxiv.org/abs/2212.09720 -- Dettmers and Zettlemoyer, The case for 4-bit precision
- https://arxiv.org/abs/2407.09141 -- Accuracy is Not All You Need
- https://arxiv.org/abs/2510.10964 -- Not All Bits Are Equal: Scale-Dependent Memory Optimization
- https://arxiv.org/html/2411.04330 -- Scaling Laws for Precision (ICLR 2025)
- https://arxiv.org/html/2505.20276v1 -- Does quantization affect models' performance on long-context tasks?
- https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ -- NVIDIA: Mastering LLM Techniques, Inference Optimization
- https://docs.ollama.com/context-length -- Ollama context length docs
- https://docs.ollama.com/faq -- Ollama FAQ
- https://github.com/ggml-org/llama.cpp/blob/master/tools/cli/README.md -- llama.cpp CLI README
- https://github.com/ggml-org/llama.cpp/discussions/10068 -- llama.cpp discussion 10068
- https://github.com/ggml-org/llama.cpp/discussions/2094 -- llama.cpp discussion 2094, quantization comparison
- https://huggingface.co/Qwen/Qwen3-8B/raw/main/config.json -- Qwen3-8B config.json
- https://huggingface.co/blog/moe -- Hugging Face: Mixture of Experts Explained
- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF -- ornith-ai/Ornith-1.5-9B-GGUF
- https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF -- unsloth/DeepSeek-V4-Flash-0731-GGUF
- https://huggingface.co/unsloth/Qwen3.8-27B-GGUF -- unsloth/Qwen3.8-27B-GGUF
- https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/quantize/README.md -- llama.cpp quantize README
- https://www.nvidia.com/en-us/geforce/graphics-cards/compare/ -- NVIDIA GeForce graphics card comparison
- https://www.nvidia.com/en-us/products/workstations/dgx-spark/ -- NVIDIA DGX Spark product page

## Notes

No experiment plan: the DGX Spark is unreachable from the production machine, so value types are EQUIPS and TEACHES rather than PROVES, and the script must attribute every number to its publisher. The strongest single fact for the channel is that the Spark's 128 GB runs at 273 GB/s, less bandwidth than an 8 GB RTX 5050.
