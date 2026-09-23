https://forums.developer.nvidia.com/t/qwen3-8-27b-nvfp4-on-a-single-dgx-spark-up-to-1m-context-vllm-mtp-measurements/380244
Accessed: 2026-09-23

# Qwen3.8-27B-NVFP4 on a single DGX Spark -- up to 1M context, vLLM+MTP measurements - NVIDIA Developer Forums

## post by helge on Aug 14

"Qwen3.8-27B was released today, and unsloth put up an NVFP4 quantization the same afternoon. It runs on a single DGX Spark without any modification to vLLM. This is what I found getting it up, including a packaging bug in the checkpoint that silently truncates every prompt at 2048 tokens."

EDIT: Unsloth meanwhile uploaded a fixed version, so you can ignore the section about the tokenizer bug fix.

## Setup

|  |  |
| --- | --- |
| Hardware | DGX Spark, GB10, 121.63 GiB unified memory, driver 580.173.02 |
| Container | ghcr.io/spark-arena/dgx-vllm-eugr-nightly:latest (source tag nightly-20260801) |
| vLLM | 0.26.1rc1.dev244+gd6a593feb.d20260801 |
| FlashInfer | d020372b068f335e2fe427372e134977a2235c49 |
| Model | unsloth/Qwen3.8-27B-NVFP4, 23.4 GB download |

## The working command

vllm serve unsloth/Qwen3.8-27B-NVFP4 --host 0.0.0.0 --port 8000 --tensor-parallel-size 1 --gpu-memory-utilization 0.45 --max-model-len 262144 --max-num-seqs 4 --max-num-batched-tokens 8192 --enable-chunked-prefill --enable-prefix-caching --reasoning-parser qwen3 --tool-call-parser qwen3_xml --enable-auto-tool-choice --distributed-executor-backend mp --speculative-config '{"method":"mtp","num_speculative_tokens":5}'

"**Architecturally this is the same model as Qwen3.6-27B.** I diffed both config.json files field by field -- no difference in architecture... Dense, 64 layers, hidden 5120, 24 heads / 4 KV heads / head_dim 256, hybrid attention with 48 linear_attention + 16 full_attention layers, MLP in NVFP4 and attention in FP8, vision tower left in bf16."

## The tokenizer bug

"The unsloth repack of 3.6 sets 16384, the repack of 3.8 sets 2048." "With text it fails silently. No error, no warning -- the prompt is simply cut at 2048 tokens. A server advertising max_model_len: 262144 effectively stops listening after 2048."

## Memory

At --gpu-memory-utilization 0.45, from vLLM's own profiling output:

|  | GiB |
| Weights + non-torch | 26.16 |
| Peak activation | 1.80 |
| CUDA graphs | 0.15 |
| Fixed | 28.11 |
| KV cache | 27.56 |

"That gives **777,645 KV tokens, 2.97x concurrency at full 262k context**. Engine init took 220.5 s, 72.3 s of it compilation."

"The hybrid attention is what makes this comfortable: only the 16 full_attention layers grow with context, and they carry just 4 KV heads at head_dim 256. The 48 linear_attention layers hold a constant state per sequence."

Related threads visible: "Qwen3.8-27B at 34-38 tok/s on DGX Spark -- open-source one-command setup (SGLang + NVFP4 + DSpark)" (106 replies); "Qwen3.8-Flash-FP8 dual sparks" (65 replies).
