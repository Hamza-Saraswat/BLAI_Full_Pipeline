---
slug: 2026-09-09-vllm-0-29-sizes-its-own-kv-cac
stage: 03-research
topic: "vLLM 0.29 sizes its own KV cache"
depth: standard
generated_at: 2026-09-09T11:49:23Z
sources: 8
hub: "[[videos/2026-09-09-vllm-0-29-sizes-its-own-kv-cac]]"
---

# Research brief: vLLM 0.29 sizes its own KV cache

## Summary
vLLM 0.29.0 landed the morning of Sep 9, 2026 with 594 commits, and it flips Model Runner V2 (MRV2) on for every model. The concrete change for a one-GPU operator: MRV2 now measures what CUDA graphs actually cost at startup and subtracts that before sizing the KV cache, closing a startup-OOM bug where the cache claimed "the whole gpu_memory_utilization budget". The most arresting number is the budget itself: one vLLM instance defaults to claiming 0.92 of your GPU's memory. The strongest concrete case is the Llama-3.1-70B FP8 config that booted on 0.23.0 and OOMed on 0.25.1+. Community-only figures (a ≈9.5 GiB graph reservation, an approximately 15 GiB oversized cache on B200) could not be corroborated by a tier 1-3 page and sit under Unverified; no fetched page shows the literal startup log wording, so that line stays Unverified too.

## Thesis
vLLM 0.29 turns on Model Runner V2 for every model and finally measures CUDA-graph memory before sizing the KV cache, so a one-GPU server boots without you guessing a memory budget.

## Explanation path
Start with the KV cache itself, because the audience does not know the term: it is the memory where the model stores keys and values for every token it has already read, so it does not recompute them for each new word. Then show the GPU as a pie that gets eaten in order: model weights first, CUDA graphs (pre-recorded replays of the compute that make generation fast but cost memory) second, and the KV cache gets whatever is left. Establish the old game before the news: you set a budget cap with --gpu-memory-utilization (default 0.92 of the GPU), vLLM profiled at startup and handed the leftover to the KV cache -- but since vLLM 0.25.1 the MRV2 runner's graph-memory probe was a placeholder returning 0, so the cache ate the entire budget and graph capture then OOMed at boot. That is why the standard advice was to guess a lower budget or disable graphs. Only then deliver 0.29: MRV2 is now the default for all models, and it bootstraps a minimal KV cache, captures graphs into a throwaway pool, measures the free-memory delta, and sizes the real cache with that headroom accounted for. Close on what the viewer does differently: same serve command, watch the startup log where vLLM prints the auto-sized value, and optionally feed the logged --kv-cache-memory back to skip the profiling pass on the next boot.

## Claims
1. **vLLM v0.29.0 shipped Sep 9, 2026 with 594 commits from 277 contributors (91 new), and Model Runner V2 is now the default for all models.**
   - Source: v0.29.0, https://github.com/vllm-project/vllm/releases/tag/v0.29.0
   - Tier: primary | Confidence: high | Accessed: 2026-09-09 | Via: firecrawl_scrape
   - Quote: "This release features 594 commits from 277 contributors (91 new)!" and "Model Runner V2 is now the default for all models"; the page shows it "released this 2 hours ago 09 Sep 08:54".
2. **MRV2 gained CUDA graph memory profiling that is factored into the KV cache auto-sizing, matching what MRV1 already did.**
   - Source: Profile CUDA graph memory usage in the V2 GPU model runner, https://github.com/vllm-project/vllm/pull/53306
   - Tier: primary | Confidence: high | Accessed: 2026-09-09 | Via: firecrawl_scrape
   - Quote: "Profile cuda graph memory usage at startup so that it can be factored into the kv cache auto-sizing, as MRV1 already does."
3. **Before the fix, MRV2's profiler was a placeholder returning 0, so the KV cache claimed the whole gpu_memory_utilization budget and capture_model() OOMed at startup on configs like Llama-3.1-70B FP8, TP=8 on L40S.**
   - Source: Profile CUDA graph memory usage in the V2 GPU model runner, https://github.com/vllm-project/vllm/pull/53306
   - Tier: primary | Confidence: high | Accessed: 2026-09-09 | Via: firecrawl_scrape
   - Quote: "with V2 no headroom was reserved for CUDA graph capture: the KV cache claimed the whole gpu_memory_utilization budget and capture_model() OOMed at startup (e.g. Llama-3.1-70B FP8, TP=8 on L40S)."
4. **The fix works by bootstrapping a minimal KV cache, capturing graphs into a throwaway pool, measuring the free-memory delta, then releasing the profiling state while keeping model weights.**
   - Source: Profile CUDA graph memory usage in the V2 GPU model runner, https://github.com/vllm-project/vllm/pull/53306
   - Tier: primary | Confidence: high | Accessed: 2026-09-09 | Via: firecrawl_scrape
   - Quote: "bootstrap a minimal KV cache, capture graphs into a throwaway pool (so their memory is reclaimed and does not pollute the persistent global pool), measure the free-memory delta, then release the profiling state while keeping model weights."
5. **The budget knob survives: --gpu-memory-utilization is the fraction of GPU memory for the model executor with a default of 0.92, and vLLM automatically infers the KV cache size from it unless --kv-cache-memory-bytes is set.**
   - Source: vLLM serve, https://docs.vllm.ai/en/stable/cli/serve/
   - Tier: docs | Confidence: high | Accessed: 2026-09-09 | Via: firecrawl_search
   - Quote: "If unspecified, will use the default value of 0.92." and "By default, this is set to None and vllm can automatically infer the kv cache size based on gpu_memory_utilization."
6. **On startup vLLM logs the exact --kv-cache-memory value that reproduces the current allocation; passing it back on the next boot skips the memory-profiling measurement and the CUDA-graph memory estimation pass, and if a boot OOMs after hardware or co-tenant changes you remove the flag to re-profile.**
   - Source: Optimization and Tuning, https://docs.vllm.ai/en/latest/configuration/optimization/
   - Tier: docs | Confidence: high | Accessed: 2026-09-09 | Via: firecrawl_search
   - Quote: "On startup, vLLM logs the exact `--kv-cache-memory` value that reproduces the current allocation. Passing it back on the next boot skips the memory-profiling measurement and the CUDA-graph memory estimation pass."
7. **MRV1 is not deleted: it remains in use for a few ROCm models and features MRV2 does not yet support.**
   - Source: Use MRV2 for all models by default, https://github.com/vllm-project/vllm/pull/53183
   - Tier: primary | Confidence: high | Accessed: 2026-09-09 | Via: firecrawl_scrape
   - Quote: "MRV1 is still used for certain specific features that aren't yet supported in MRV2." (the v0.29.0 release notes add: "MRV1 remains in use for a few ROCm models and features MRV2 does not yet support.")
8. **vLLM's own memory guide still teaches the old manual moves for a tight GPU: trim context length and batch size, cap CUDA graph capture sizes, or disable graphs entirely with enforce_eager.**
   - Source: Conserving Memory, https://docs.vllm.ai/en/latest/configuration/conserving_memory/
   - Tier: docs | Confidence: high | Accessed: 2026-09-09 | Via: firecrawl_scrape
   - Quote: "You can disable graph capturing completely via the `enforce_eager` flag" and "You can further reduce memory usage by limiting the context length of the model (`max_model_len` option) and the maximum batch size (`max_num_seqs` option)."
9. **Community reception tracks the bug, not the release: users reproduced the startup OOM on other hardware, used VLLM_USE_V2_MODEL_RUNNER=0 as a workaround, and the issue was closed as completed by the fix PR.**
   - Source: "[Bug]: Model Runner V2 (now default for dense models) skips CUDA graph memory reservation", https://github.com/vllm-project/vllm/issues/49224
   - Tier: community | Confidence: medium | Accessed: 2026-09-09 | Via: firecrawl_scrape
   - Quote: "Setting `VLLM_USE_V2_MODEL_RUNNER=0` on 0.25.1 makes it start successfully again."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | default fraction of GPU memory one vLLM instance claims (--gpu-memory-utilization) | 0.92 | https://docs.vllm.ai/en/stable/cli/serve/ | "If unspecified, will use the default value of 0.92." |
| 2 | commits in v0.29.0, from 277 contributors (91 new) | 594 commits | https://github.com/vllm-project/vllm/releases/tag/v0.29.0 | "This release features 594 commits from 277 contributors (91 new)!" |
| 3 | persistent-batch rows MRV2 pre-allocates (max_num_reqs) | 1024 by default on most platforms | https://docs.vllm.ai/en/latest/design/model_runner_v2/ | "Pre-allocate a fixed-size tensor with `max_num_reqs` rows (1024 by default on most platforms)." |
| 4 | per-step logits memory cut from MRV2 batch-sharded sampling | 1/TP | https://github.com/vllm-project/vllm/releases/tag/v0.29.0 | "batch-sharded sampling that cuts per-step logits memory by 1/TP" |

## Analogy candidates
- **Packing a moving truck**: the model weights and the CUDA graphs are furniture that must go in first; the KV cache is boxes that fill whatever space is left. Before 0.29 the packer never measured the furniture, filled the truck with boxes, and the couch was left on the curb (the startup OOM). 0.29 measures the furniture before loading boxes. Breaks when: the truck's total size is still your guess (the 0.92 cap), and the analogy implies you could repack mid-drive, which the KV cache cannot do once allocated at startup.
- **A restaurant's floor plan**: CUDA graphs are the kitchen equipment installed before opening; KV cache is diner table space sold against the same square footage. The old bug sold the equipment's floor space as tables, then opening night failed. Breaks when: a restaurant can turn tables away, while vLLM instead evicts diners mid-meal and makes them re-order from scratch (preemption and recomputation), which no restaurant would survive.

## Misconceptions
- Myth: vLLM 0.29 removed gpu_memory_utilization, so you never set memory again. Reality: the flag is still the budget cap with a default of 0.92; what changed is that CUDA-graph memory is now measured and subtracted before the KV cache is sized (claims 2, 3, 5).
- Myth: "KV cache auto-sizing" means the cache grows and shrinks while serving. Reality: the size is fixed once at startup by a profiling pass; if it runs short mid-serve, vLLM preempts requests and recomputes them later, and the docs' remedy is still to raise the budget knobs (claim 6; Optimization and Tuning's preemption section).

## Glossary
- **KV cache**: the memory where a model stores keys and values for every token it has already read, so it does not recompute them for each new word.
- **vLLM**: an open-source server that runs language models on your own GPU and serves them over an API.
- **CUDA graph**: a pre-recorded sequence of GPU operations that replays faster than issuing them one at a time, at the cost of extra GPU memory.
- **Model Runner V2 (MRV2)**: vLLM's rewritten execution core, now the default engine path for all models as of 0.29.
- **MRV1**: the older model runner, still used for a few ROCm models and features MRV2 does not yet support.
- **gpu_memory_utilization**: the vLLM setting that caps the fraction of GPU memory one server instance may use, 0.92 by default.
- **memory profiling**: a startup pass where vLLM measures what it actually needs before deciding the KV cache size.
- **OOM (out of memory)**: the crash when a program asks the GPU for more memory than is free.
- **preemption**: when vLLM pauses a request, drops its cached tokens, and recomputes it later to free KV cache space.

## Unverified
- The legacy V1 runner reserved "≈9.5 GiB" for CUDA graph memory in the Llama-3.1-70B FP8 TP=8 L40S case; the figure appears only in community-tier issue #49224 and no fetched docs page corroborates it.
- A DeepSeek-V4-Pro 861B run on B200 measured the KV cache oversized by "approximately 15 GiB", matching the CUDA-graph footprint; also community-tier only (issue #49224).
- The exact wording of the startup log line that prints the auto-sized KV cache value was not shown on any fetched page; capture it on a first boot before quoting it in narration.
- Whether the DGX Spark (GB10) hits the new profiling path identically is untested on our hardware; treat auto-sizing there as an expectation to measure, not a claim.

## Suggested outline
1. Open on the familiar failure: your vLLM box OOMs at startup and the advice was always "lower gpu-memory-utilization" -- that guess-the-headroom era is what 0.29 ends.
2. Define the KV cache in one sentence, then show the GPU pie: weights, CUDA graphs, cache -- and the bug where the cache ate the whole 0.92 budget because the graph probe returned 0.
3. The fix and the payoff: MRV2 default everywhere, graphs measured before sizing; upgrade, run the same serve command, read the startup log, and optionally pin the logged --kv-cache-memory to boot faster next time.

## Viewer situation
You run vLLM on one GPU box and you have already had to dial --gpu-memory-utilization down, or flip on enforce-eager, to stop a startup crash.

## Has process
true
- Upgrade the box to vLLM 0.29 with pip (the release ships as `pip install vllm` wheels).
- Start the server with the same `vllm serve <model>` command you already use.
- Watch the startup log for the KV cache size and the exact `--kv-cache-memory` value vLLM prints.
- Pass that `--kv-cache-memory` value back on the next boot only if you want to skip the profiling pass.
- If a boot OOMs after hardware or co-tenant changes, remove the pinned value so vLLM re-profiles.

## Objection
Auto-sizing was always there: 0.29 just fixes the CUDA-graph measurement inside the same 0.92 budget you still have to set, and a pinned value only holds on the same GPU with the same free memory.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/vllm-project/vllm/releases/tag/v0.29.0 | v0.29.0 (release notes) | primary | firecrawl_scrape | 2026-09-09 |
| 2 | https://github.com/vllm-project/vllm/pull/53306 | Profile CUDA graph memory usage in the V2 GPU model runner | primary | firecrawl_scrape | 2026-09-09 |
| 3 | https://github.com/vllm-project/vllm/pull/53183 | [Model Runner V2] Use MRV2 for all models by default | primary | firecrawl_scrape | 2026-09-09 |
| 4 | https://github.com/vllm-project/vllm/issues/49224 | [Bug]: Model Runner V2 skips CUDA graph memory reservation | community | firecrawl_scrape | 2026-09-09 |
| 5 | https://docs.vllm.ai/en/stable/cli/serve/ | vLLM serve (CLI reference) | docs | firecrawl_search | 2026-09-09 |
| 6 | https://docs.vllm.ai/en/latest/configuration/optimization/ | Optimization and Tuning | docs | firecrawl_search | 2026-09-09 |
| 7 | https://docs.vllm.ai/en/latest/design/model_runner_v2/ | Model Runner V2 Design Document | docs | firecrawl_search | 2026-09-09 |
| 8 | https://docs.vllm.ai/en/latest/configuration/conserving_memory/ | Conserving Memory | docs | firecrawl_scrape | 2026-09-09 |

## Notes
A Short speaks at most 3 numbers; the most arresting one is 0.92, the default fraction of GPU memory one vLLM instance claims (key number 1), with "594 commits" as the scale-of-release alternate. Two flag names exist for pinning the cache: the serve CLI documents `--kv-cache-memory-bytes` while the optimization guide writes `--kv-cache-memory`; quote whichever page you cite, do not merge them. The startup-log wording and the DGX Spark behavior are the two things to verify on first boot before narration locks. No source conflicts found; community issue #49224 is used only for reception and the workaround, never as the sole source of a number.
