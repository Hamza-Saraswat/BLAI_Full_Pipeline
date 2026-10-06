# Qwen3.6-35B-A3B · int4\_wo\_32 → GGUF Q4\_0

## Quantization

| Item | Value |
| --- | --- |
| Model | [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) |
| Tool | Quark RTN (GPU / ROCm Strix Halo) |
| Scheme | `int4_wo_32` (symmetric int4, `group_size=32`) |
| Corresponding GGUF format | **Q4\_0** |
| Quark checkpoint | `int4-wo32/model.safetensors` |

### Reproduce quantization

```bash
cd /home/l/work/quantization_work/quark_llama_cpp_test/models/qwen3.6-35b-a3b-q4_0
./scripts/quantize_q4_0.py
```

This script always uses `int4_wo_32`. The intermediate Quark checkpoint is written to `int4-wo32/` and the final GGUF to `gguf-q4_0/`. You can override the default paths and device via `BASE_MODEL`, `QUANT_OUT`, `GGUF_OUT`, `QUARK_SRC`, `LLAMA_CPP_DIR`, `DEVICE`, `MULTI_GPU=1`. To produce only the Quark checkpoint, add `--skip-gguf-export`.

## GGUF export

The target GGUF format for this directory is `q4_0`, usually exported via the root-level script:

```bash
cd /home/l/work/quantization_work/quark_llama_cpp_test
PROFILE=qwen3.6-35b-q4_0 ./run_export.sh
```

Output is written to `gguf-q4_0/` by default.

## Evaluation: Perplexity (wikitext-2, llama.cpp)

All three were run with llama.cpp `llama-perplexity` on wikitext-2 test (`n_ctx=512`, 20 chunks, same data and same parameters), so they are directly comparable.

| Format | PPL | vs float | Size |
| --- | --- | --- | --- |
| F16 float (baseline) | 6.61 ±0.23 | — | 71 GB |
| Q4\_1 (UINT4 affine) | 6.73 ±0.24 | +1.8% | ~21 GB |
| **Q4\_0 (INT4 symmetric)** | **6.79 ±0.24** | **+2.7%** | **~21 GB** |

> Quantization is nearly lossless: Q4\_1 is only +1.8% over F16 and Q4\_0 only +2.7%, while the size is compressed to about 30% of the float model.
> Before fixing the `linear_attn` V-head reordering, Q4\_0 PPL was 2,619,116; after the fix it is 6.79.

## Evaluation: Open LLM Leaderboard v2

### How all 6 tasks are measured on the GGUF

> **Update (2026-08-06):** An earlier version of this card stated that only the 2 generative tasks (IFEval, MATH-hard) could be scored on the GGUF. That limitation has since been lifted by patching `llama-server`; the four multiple-choice tasks are now measured directly on this GGUF file (see below).

The six leaderboard-v2 tasks use two scoring methods in lm-eval:

- **Generative (`generate_until`)**: IFEval, MATH-hard. The model generates text freely, which is then matched against rules or the reference answer. Any backend that can generate can score these.
- **Multiple-choice (`multiple_choice` / loglikelihood)**: BBH, GPQA, MMLU-Pro, MuSR. Each candidate answer is appended to the question, and the model computes the sum of the per-position log-probabilities of that **already-fixed token sequence**, then picks the highest-scoring candidate. This requires the backend to return the **logprob of the input (prompt) tokens**.

Stock `llama-server` returns logprobs only for tokens the model itself generates, not for prompt tokens (both `/v1/completions` with `echo=true` and the native `/completion` with `n_probs` were tested), so the four multiple-choice tasks originally could not be scored. This was fixed by patching `llama-server` on branch **`hongweimeng/gguf-prompt-logprobs`**: `/v1/completions` with `echo=true` \+ `logprobs` now returns the legacy OpenAI logprobs format (`text_offset` / `tokens` / `token_logprobs` / `top_logprobs`) covering the **prompt tokens**. With that, lm-eval's `gguf` (GGUFLM) backend scores all four multiple-choice tasks directly on the GGUF. Logprob correctness was verified against `llama-perplexity` (matching PPL).

So all 6 leaderboard-v2 tasks are now measured on this GGUF file — no vLLM / safetensors substitution is needed.

### Results (updated 2026-08-08, all 6 tasks complete)

Backend for this GGUF: the 2 generative tasks (IFEval, MATH-hard) use `lm_eval --model local-completions` -\> `llama-server` (`/v1/completions`, `-c 32768 -np 4`, num\_concurrent=4), measured 2026-08-04. The 4 multiple-choice tasks use lm-eval's `gguf` (GGUFLM) backend against the **patched**`llama-server` (branch `hongweimeng/gguf-prompt-logprobs`, `-np 4 -c 131072`), measured 2026-08-06. The reference columns were measured with vLLM (`--tasks leaderboard`, 2026-07-22).

| Task | Metric | BF16 (base)¹ | INT4-GS128 (vLLM)¹ | **This GGUF (llama.cpp)** |
| --- | --- | :-: | :-: | :-: |
| IFEval | prompt\_level\_strict | 0.3235 | 0.3438 | **0.3752** |
| IFEval | inst\_level\_strict | 0.4580 | 0.4676 | **0.4976** |
| MATH-hard | exact\_match | 0.5287 | 0.5083 | **0.5234** |
| BBH | acc\_norm | 0.6546 | 0.6018 | **0.6506** ² |
| GPQA | acc\_norm | 0.4337 | 0.3431 | **0.4086** ² |
| MMLU-Pro | acc | 0.5968 | 0.5687 | **0.5825** ² |
| MuSR | acc\_norm | 0.4339 | 0.4630 | **0.4471** ² |

On both the generative and the multiple-choice tasks this GGUF tracks the BF16 baseline closely, indicating faithful quantization export.

¹ Reference only, **not measured on this GGUF file** (BF16 and vLLM numbers from `--tasks leaderboard`, 2026-07-22). `INT4-GS128` is a group\_size=128 sibling model, different from this group\_size=32 GGUF; shown for context.
² Multiple-choice / loglikelihood task, measured on this GGUF via the **patched**`llama-server` (branch `hongweimeng/gguf-prompt-logprobs`) \+ lm-eval `gguf` backend. BBH/GPQA/MuSR measured 2026-08-06; MMLU-Pro completed 2026-08-08 (~114k loglikelihood requests, 12,032 samples, memory-bandwidth bound at ~0.6 it/s).

Downloads last month

-

Downloads are not tracked for this model. [How to track](https://huggingface.co/docs/hub/models-download-stats)

Inference Providers [NEW](https://huggingface.co/docs/inference-providers)

This model isn't deployed by any Inference Provider. [🙋Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=amd/Qwen3.6-35B-A3B-Quark-INT4-G32-GGUF&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5Bamd%2FQwen3.6-35B-A3B-Quark-INT4-G32-GGUF%5D(%2Famd%2FQwen3.6-35B-A3B-Quark-INT4-G32-GGUF)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A(optional)%20Which%20providers%20are%20you%20interested%20in%3F%20(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6)%0A)

## Model tree for amd/Qwen3.6-35B-A3B-Quark-INT4-G32-GGUF

Base model

[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)

Quantized

( [863](https://huggingface.co/models?other=base_model:quantized:Qwen/Qwen3.6-35B-A3B))

this model