[Writing](https://runtimenotes.com/blog/)/ [AI](https://runtimenotes.com/tags/)

# Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10

flag 033Nov 27, 2026ai [#ai](https://runtimenotes.com/tags/ai/) [#infrastructure](https://runtimenotes.com/tags/infrastructure/) [#engineering](https://runtimenotes.com/tags/engineering/) [#vllm](https://runtimenotes.com/tags/vllm/) [#homelab](https://runtimenotes.com/tags/homelab/) 18 min read

Contents8

Contents [How a request runs on Inkling](https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/#how-a-request-runs-on-inkling) [The starting point](https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/#the-starting-point) [Ideas from the GB10 community](https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/#ideas-from-the-gb10-community) [Tuning vLLM](https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/#tuning-vllm) [The results](https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/#the-results) [An approach to tuning inference](https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/#an-approach-to-tuning-inference) [Running the configuration](https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/#running-the-configuration) [What’s next](https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/#what-s-next)

On the trail [034 · Next post](https://runtimenotes.com/) [033 · Getting 101 tok/s from Inkling 2 Mini in vLLM on one GB10](https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/) [032 · Taking Inkling 2 Mini for a spin on NVIDIA GB10](https://runtimenotes.com/blog/inkling-2-mini-on-nvidia-gb10/) [031 · Building a home AI lab on NVIDIA GB10: setup, fail-safes and benchmarks](https://runtimenotes.com/blog/building-a-home-ai-lab-on-nvidia-gb10/) [See it on the mountain →](https://runtimenotes.com/#flag-getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10)

196 tok/s across four concurrent requests, a 9.7-second 32K prefill and room for a second model.

After [taking Inkling 2 Mini for a spin](https://runtimenotes.com/blog/inkling-2-mini-on-nvidia-gb10/) on my GB10, I wanted to make it faster without leaving vLLM, removing Qwen3.8-27B from the machine or shrinking Inkling’s 131,072-token context.

A few days of tuning later, Inkling runs at:

- 101 tok/s for a single request.
- 195.7 tok/s in aggregate for four concurrent requests.
- 9.7 seconds to the first token on a 32K prompt.

On [tonyd2wild’s Inkling benchmark](https://github.com/tonyd2wild/Inkling-2-Mini-NVFP4-DGX-Spark), that’s the fastest single-request vLLM result I know of. On the same benchmark tonyd2wild’s [TensorFold](https://github.com/ashhart/TensorFold) port measured 105.5 tok/s and knapcio’s SGLang recipe 112.0. With four requests at once my setup beats both of tonyd2wild’s published setups.

Inkling still uses 36% of the GB10’s memory. Qwen3.8-27B stayed loaded but idle while I measured.

The work covered vLLM settings, speculative decoding, CUDA graphs and the GPU kernels behind Inkling’s experts.

## How a request runs on Inkling

A request runs in two phases. Prefill reads the prompt in chunks of 4,096 tokens and produces the first token. Decode generates the rest of the reply, several tokens per step.

Decode uses speculative decoding. A small draft model proposes 7 tokens and Inkling checks all of them in one pass. The rejection sampler keeps the proposals up to the first one Inkling rejects, plus one token of Inkling’s own, so every step keeps 1 to 8 tokens.

Mapping changes against the request path:

![Inkling 2 Mini request path with changes 1 to 5 marked.](https://runtimenotes.com/inkling-engine-request-map.png)One Inkling request, prefill then decode and the change map.

Common terms:

| Term | What it means here |
| --- | --- |
| Prefill | Reading the prompt in 4,096-token chunks, up to the first token |
| Decode | Generating the reply after the first token, one step at a time |
| Draft model | A small model that guesses Inkling’s next 7 tokens: DSpark ships with Inkling, DFlash2 replaced it |
| Verify rows | The 8 positions Inkling checks in each decode step: the last kept token plus the 7 guesses |
| Experts | Inkling’s 128 feed-forward blocks per layer, of which each token uses 8 |
| GEMM | A matrix multiply; the experts’ GEMMs are the largest GPU cost |
| CUDA graph | A recorded sequence of GPU kernel launches that vLLM replays every decode step, with fixed shapes |

The routed experts take 53% of a decode step and 44% of a 32K prefill:

![Share of GPU kernel time by kernel type, decode step and 32K prefill.](https://runtimenotes.com/inkling-engine-time-breakdown.png)GPU kernel time per decode step and per 32K prefill, before the changes.

## The starting point

The machine is an MSI EdgeXpert, MSI’s version of NVIDIA’s DGX Spark, with one GB10 chip and 128 GB of memory shared by the CPU and GPU. [Building a home AI lab on NVIDIA GB10](https://runtimenotes.com/blog/building-a-home-ai-lab-on-nvidia-gb10/) covers the setup and [Taking Inkling 2 Mini for a spin on NVIDIA GB10](https://runtimenotes.com/blog/inkling-2-mini-on-nvidia-gb10/) the first look at the model.

vLLM settings for Inkling:

| Setting | Value |
| --- | --- |
| Inference engine | vLLM |
| Inkling memory allocation | 36% |
| Qwen3.8-27B memory allocation | 34% |
| Maximum context length | 131,072 tokens |
| KV cache | FP8 |
| Maximum concurrent sequences | 8 |
| Maximum batched tokens | 4,096 |

That gives Inkling about 44 GiB, including a KV cache that holds 1.85 full 131,072-token requests.

Tuning steps so far, from DSpark (the draft model that ships with Inkling) to DFlash2:

| Step | Change | Effect |
| --- | --- | --- |
| 1 | `--max-num-batched-tokens` from 8,192 to 4,096 | KV cache capacity nearly doubled, decode unchanged |
| 2 | Eager weight loading and a persistent compilation cache | Startup from 257 to 42 seconds |
| 3 | Drafting 4 tokens instead of 7, only while one request runs | −1 to +11%, depending on the workload |
| 4 | DFlash2 draft model with tonyd2wild’s vLLM patches | 90.3 tok/s for one request, 163.8 for four |

When incoai released [DFlash2](https://huggingface.co/incoai/Inkling-2-Mini-DFlash2), tonyd2wild published the vLLM patches to run it. On their benchmark it lifted one request from 61.4 to 88.2 tok/s. With the same patches I measured 90.3.

On my everyday prompts (one coding, one prose and one reasoning prompt at the model’s default settings) the gain was smaller. Reasoning ran 24 to 26% faster and four requests at once 10 to 14% faster. Prose stayed flat.

With four requests at once, though, my setup fell behind: 163.8 tok/s in aggregate against tonyd2wild’s 180.4.

## Ideas from the GB10 community

Most of my changes started from ideas other GB10 owners had published:

| Who | Idea | What I took into vLLM |
| --- | --- | --- |
| tonyd2wild’s TensorFold port, 105.5 tok/s | Cheaper drafting (FP8 draft layers, a 4-bit copy of the output head) and letting the draft’s probabilities decide how many tokens to verify | Both ideas: INT8 draft copies and adaptive verify width |
| [sxuff](https://github.com/sxuff/inkling-2-mini-spark) | INT8 copies of DSpark’s weights for drafting only, with an INT8 matrix-vector kernel | The kernel, for DFlash2’s copies |
| [knapcio’s SGLang recipe](https://github.com/knapcio/Inkling-2-Mini-1x-DGX-Spark) | Lower-precision draft layers and a verify-width cap whose cut rows do no expert work | Skipping expert work for cut rows |
| vLLM pull request [#69288](https://github.com/vllm-project/vllm/pull/69288), open | Fewer kernel compilations for new prompt lengths | Applied as an overlay |
| [Mia’s TensorFold recipe](https://github.com/MiaAI-Lab/Inkling-2-Mini-DGX-Spark-TensorFold) | DFlash2 by default since 24 November, with the 4-bit head and verify width from tonyd2wild’s patch | A comparison point for the results |

## Tuning vLLM

Mapping the changes I made to the request:

| # | Change | Where it acts | Problem | Result |
| --- | --- | --- | --- | --- |
| 1 | Compile-stall fix | Prefill, on new prompt lengths | Fresh prompts waited a median 2.3 s for their first token | Stalls cut by 67 to 90% |
| 2 | INT8 draft copies | Draft model | Drafting cost about 8.5 ms per step | +4.3 to 4.9% for one request |
| 3 | Probabilistic drafting | Rejection sampler | Sampled requests accepted fewer drafts than the draft’s probabilities allow | +14 to 20% on sampled requests |
| 4 | Adaptive verify width | Verify rows | Drafts likely to be rejected still read 8 experts per row | +5.2 to 5.4%, then +1.7 to 2.2% from a lower threshold |
| 5 | Prefill GEMM configuration | Experts during prefill | Expert GEMMs ran at about 8% of the chip’s FP4 peak | 32K first token from 12.2 to 9.7 s |

### 1\. Removing compilation stalls on new prompts

My first run of tonyd2wild’s benchmark showed fresh prompts waiting a median 2.3 seconds for their first token, mostly while GPU kernels compiled.

Inkling’s expert planner computes `max_ctas`, the most blocks of GPU work the experts could need, from the token count. Triton receives it as a compile-time constant and compiles a new kernel for each new value. So almost every new prompt length recompiled about ten kernels while the request waited.

The open pull request rounds the value up to a power of two, so all prompt lengths share 12 to 15 compiled variants. On twelve prompt lengths the server hadn’t seen, it cut the stalls by 67 to 90%. Outputs and decode speed didn’t change.

### 2\. Making drafting cheaper with INT8

Drafting has its own cost. Each decode step runs the draft’s layers plus a second pass through Inkling’s 926 MB output head, which took about 8.5 milliseconds per step in a microbenchmark.

I added INT8 copies of DFlash2’s 21 linear layers and the shared output head, read through sxuff’s INT8 matrix-vector kernel. Only drafting uses them. Inkling still verifies with its original weights, so its output doesn’t change.

Gradual gains in stages:

1. The microbenchmark predicted 7 to 8% more throughput.
2. The first build gave 1.8%.
3. I profiled real decode steps with and without the copies. The output head never ran in INT8, because DFlash2 calls it with FP32 output, a case my code didn’t handle.
4. With that fixed, two runs gained 4.3 to 4.9%, from 90.6 to 94.8 tok/s, for 843 MB of copies. The temperature-0 output of my three check prompts stayed identical.

The profile without the copies also showed the bigger cost: the routed experts took 31.2 of the step’s 58.4 milliseconds.

### 3\. Probabilistic drafting

vLLM drafts greedily by default. For a sampled request, its rejection sampler then treats each drafted token as certain instead of using the draft’s real probabilities, so it accepts fewer drafts than it could.

Setting `draft_sample_method` to `probabilistic` gives the sampler those probabilities. Inkling’s output distribution stays the same either way.

Greedy against probabilistic drafting on my everyday prompts, at the default temperature of 1.0:

| Concurrent requests | Greedy drafting, aggregate | Probabilistic drafting, aggregate |
| --- | --- | --- |
| 1 | 56.4 tok/s | 64.1 tok/s |
| 4 | 89.1 tok/s | 106.7 tok/s |
| 8 | 150.5 tok/s | 177.6 tok/s |

That’s 14 to 20% faster for sampled requests. Temperature-0 requests ran the same, so tonyd2wild’s benchmark would never have shown this gain.

### 4\. Adaptive verify width

The routed experts took 53% of the profiled decode step, so I looked for expert work to skip.

Every verify row reads 8 experts in every layer, yet drafts are accepted in order. Once one is rejected, every row after it was wasted work. The draft’s own probabilities can predict where that will happen, which is how TensorFold and knapcio’s SGLang recipe already cut verification.

#### Working within CUDA graph constraints

vLLM has its own adaptive verification, but it needs CUDA graphs that allow different verify widths within one batch. Inkling’s attention backends don’t support them.

So I kept all eight rows and changed what they do. Inkling’s MoE layer already sends padding rows to no expert. Marking low-confidence rows as padding skips their expert reads and leaves the CUDA graph shapes unchanged.

The cut point comes from the running product of the draft’s token probabilities. Rows after the point where that product falls below a threshold become padding. The runner then keeps at most as many tokens as there are live rows. The threshold started at 0.4 at temperature 0 and is 0.1 for sampled requests.

Example step at a threshold of 0.3, where the product drops below it at draft 5:

![One decode step with adaptive verify width, example values.](https://runtimenotes.com/inkling-engine-verify-rows.png)One decode step with adaptive verify width (example values).

#### Measuring before implementing

Offline test before building:

1. I logged the draft probabilities and accepted token counts for 8,600 decode steps.
2. The probability product predicted acceptance well, with an AUC of 0.91 to 0.94 at temperature 0, where 1.0 is a perfect ranking.
3. I measured step time at fixed verify widths, with the INT8 copies already in.
4. Replaying thresholds on the logged steps with those step times predicted a 7.8% gain.
5. Then I wrote the runner changes and tested them end to end.

Step time at fixed verify widths:

| Verify rows | Time per step |
| --- | --- |
| 8 | 53.02 ms |
| 6 | 48.83 ms |
| 4 | 43.29 ms |
| 2 | 36.52 ms |

In two end-to-end runs it gained 5.2 to 5.4%, from 95.0 to 100.0 tok/s. On average only about 4.8 of the eight rows still read experts.

Coding and counting gained little at first. DFlash2 predicts those tokens so well that early cuts threw away tokens that would have been accepted. Lowering the temperature-0 threshold from 0.4 to 0.3 recovered some of it, mostly on coding, which went from 98 to 103 tok/s.

It stays on for concurrent requests too, where it made little difference: −0.9 to +3.1% at four requests.

### 5\. Faster long-context prefill

A fresh 32,751-token prompt took 12.2 seconds to produce its first token.

Bigger prefill chunks helped but shrank the KV cache. At 6,144 tokens it held only 1.33 full requests. At 8,192 the service wouldn’t start. With two models on the machine and full 131,072-token requests as a requirement, I kept 4,096-token chunks.

A profile of a 32K prefill put the expert GEMMs at 44% of the time. Attention’s share grew with the context, from 11% early in the prompt to 27% at the end.

The expert GEMMs reached about 38 TFLOP/s, roughly 8% of the GB10’s FP4 peak. Memory bandwidth wasn’t the limit, so the kernel’s launch configuration was worth a look.

A launch configuration sets how the multiply is cut into tiles: the size of each block and how many values along the inner K dimension each step takes. For 4,096-token chunks, Inkling’s Triton expert kernel used blocks of 128 by 64 with 512 values per step along K.

I timed 72 configurations at the shape of a real chunk, 32,768 routed rows across 128 experts. Wider blocks with smaller steps, 128 by 256 with 256 values per step, about halved the time. Both projections gave bit-identical output.

| Expert projection | Original configuration | Tuned configuration |
| --- | --- | --- |
| Gate and up | 9.16 ms | 4.39 ms |
| Down | 4.85 ms | 2.59 ms |

The change is a few lines in the prefill branch; decode keeps its own tiles.

End to end, the 32K time to first token fell from 12.2 to 9.8 seconds in the A/B runs and to 9.7 on the live service. The first long prompt after a restart fell from 14.1 to 9.9 seconds.

## The results

### Decode performance

tonyd2wild’s benchmark runs five prompts in each of eight categories (coding, math, JSON, HTML, prose, narrative, summarization and counting) at temperature 0 with thinking off and 1,024 output tokens. Its decode speed excludes time to first token. I ran it unchanged apart from an API key header and a sandbox for its code grading.

![Single-request decode progression and four-request throughput on tonyd2wild’s benchmark.](https://runtimenotes.com/inkling-engine-progression.png)Decode speed after each change and with four requests at once, against published results.

The bars are A/B runs. The finished service measured 101.0 and 100.7 tok/s in two runs.

| Configuration | One request, tok/s | Four at once, aggregate tok/s |
| --- | --- | --- |
| Published vLLM + DSpark | 61.4 | 125 |
| Published vLLM + DFlash2 | 88.2 | 180.4 |
| Published TensorFold + optimized DFlash2 | 105.5 | 165.0 |
| Mia’s TensorFold defaults, measured by knapcio | 100.5 |  |
| knapcio’s SGLang recipe v2.9.7, measured by knapcio | 112.0 |  |
| Local vLLM + DFlash2 baseline | 90.3 | 163.8 |
| Final local vLLM configuration | 101.0 | 195.7 |

With four requests at once, my setup went from 9% behind tonyd2wild’s vLLM result to 8% ahead. It also beats their TensorFold result there. For a single request tonyd2wild’s TensorFold run still leads, by 4.5% instead of 20%.

knapcio’s [same-harness comparison](https://github.com/knapcio/inkling-2-mini-spark-bench) ran this benchmark on two other Sparks, where tonyd2wild’s vLLM setup reproduced within 1 to 3%. There Mia’s TensorFold defaults measured 100.5, about level with mine. knapcio’s own SGLang recipe led at 112.0.

These numbers compare whole setups on the GB10. tonyd2wild’s vLLM setup used 80% of the memory and a BF16 KV cache; mine uses 36% and FP8. TensorFold also implements speculative decoding differently.

### Everyday workloads

My everyday prompts run at the model’s defaults (reasoning effort medium, temperature 1.0), four to six times each. The score is the geometric mean of the three speeds.

| Configuration | Score |
| --- | --- |
| Tuned DSpark | 48.8 tok/s |
| DFlash2 and the decode changes, run 1 | 69.8 tok/s |
| DFlash2 and the decode changes, run 2 | 70.7 tok/s |

That’s 43 to 45% faster than tuned DSpark on sampled requests.

### Prefill performance

The GEMM change raised my 32K prefill from 2,679 to 3,371 tok/s. The other bars come from [niklaslenz\_ai’s engine comparison](https://x.com/niklaslenz_ai/status/2125493942733201560) for the vLLM and SGLang container images, Mia’s README at [commit `3b210d1f`](https://github.com/MiaAI-Lab/Inkling-2-Mini-DGX-Spark-TensorFold/tree/3b210d1f) and knapcio’s [own benchmarks](https://github.com/knapcio/Inkling-2-Mini-1x-DGX-Spark/blob/main/docs/benchmarks.md).

![Prefill speed for a 32K-token prompt across setups.](https://runtimenotes.com/inkling-engine-prefill.png)32K prefill speed, mine against published GB10 setups. Mia's figure uses her lossy default prefill path.

Mine are the median of three fresh 32,751-token prompts after a warm-up, so none hit the prefix cache. The others used their own prompts and boxes. Mia’s and knapcio’s recipes each have the whole machine to themselves.

Mia’s prefill rose from 3,072 to 3,772 tok/s with her latest patches, which include the 8,192-token chunks my memory budget can’t fit. Her default prefill path is also lossy: it runs on FP4 and FP8 tensor cores and agrees with the exact path on 96.3% of top-1 tokens. My GEMM change is bit-identical.

knapcio’s 5,085 tok/s shows how much prefill speed is still left on this hardware.

### Comparing with sparkDash

Mia publishes her TensorFold results from her own tool, [sparkDash](https://github.com/MiaAI-Lab/sparkDash). Her current README runs DFlash2 with the 4-bit head and verify width and reports only prose.

sparkDash runs as a privileged container, so I reimplemented its test from commit `86f972e` as a plain client. It samples at temperature 0.7 with thinking on, forces 400 output tokens per stream and uses Mia’s `top_k` of 20.

![sparkDash’s prose decode test, my setup against Mia’s README.](https://runtimenotes.com/inkling-engine-sparkdash.png)sparkDash prose decode test at top\_k 20. Eight-stream bars are aggregate.

One prose stream is close, 66.0 against 64.3 tok/s. With eight streams mine is 14% ahead, 224.2 against 196.4 in aggregate. Prefill goes the other way. Under the same test her lossy path is 11% faster, 3,772 against my 3,395 tok/s.

The setups differ. Mia runs Inkling-2-Mini-Derisked, a variant described as having most safety refusals removed, on a Spark to itself, using about 60 GiB plus an 18.5 GiB prompt cache. Mine uses about 44 GiB beside an idle Qwen3.8-27B.

## An approach to tuning inference

The process carries over to other models and engines:

1. Start with the service you want to run. Fix the memory budget, context length and concurrency before optimizing throughput. Here that ruled out bigger prefill chunks and pushed the work into the kernel.
2. Use a published benchmark and your own workloads. The published one gives a common reference point. Your own catch gains it can’t see, as probabilistic drafting did at temperature 1.0.
3. Profile complete inference steps. A microbenchmark promised 7 to 8% for the INT8 copies. Only a profile of real steps showed why the first build gave 1.8%.
4. Measure the opportunity before building. The logged draft probabilities and the measured cost of a skipped row predicted the verify-width gain before I wrote the runner.
5. Keep experiments controlled. Write the acceptance rules before each A/B test, run the unchanged setup before and after each candidate, hash the temperature-0 output of fixed prompts and run probe prompts.
6. On unified memory, watch the other models. One run that overlapped Qwen3.8-27B activity saw Inkling’s counting speed halve, so I discarded it.
7. Make the modifications reproducible. Pin every overlay file by hash and build each from one exact source file, so an upstream change fails the build instead of quietly changing the service.

## Running the configuration

The setup uses vLLM’s `inkling-2-mini` container image pinned by digest, with the [Inkling checkpoint](https://huggingface.co/thinkingmachines/Inkling-2-Mini) at revision `ed40e7da625f`.

The changes are eight files mounted read-only over the image. They add the DFlash2 patches, sxuff’s INT8 kernel, the INT8 draft copies, the compile-stall fix, adaptive verify width and the prefill GEMM configuration. The [overlay README](https://github.com/runtimenoteslabs/home-ai-lab/blob/main/vllm/overlay/README.md) lists each file with its source, SHA-256 hash and build steps.

The launch command, abridged:

```bash
docker run -d --name vllm-inkling --gpus all --ipc host --network host \
  -v "$MODELS:/models:ro" \
  "${OVL_ARGS[@]}" \
  "$IMAGE" \
  vllm serve /models/Inkling-2-Mini \
    --gpu-memory-utilization 0.36 \
    --max-model-len 131072 \
    --max-num-seqs 8 \
    --max-num-batched-tokens 4096 \
    --kv-cache-dtype fp8 \
    --safetensors-load-strategy eager \
    --speculative-config '{"method":"dflash","model":"/models/Inkling-2-Mini-DFlash2","num_speculative_tokens":7,"kv_cache_dtype":"auto","draft_sample_method":"probabilistic"}'
```

`OVL_ARGS` holds the read-only mounts and these switches.

| Environment variable | Value | Purpose |
| --- | --- | --- |
| `AILAB_DFLASH2_Q8` | 1 | INT8 draft copies |
| `AILAB_B` | 1 | Adaptive verify width |
| `AILAB_B_THETA0` | 0.3 | Threshold at temperature 0 |
| `AILAB_B_THETA1` | 0.1 | Threshold for sampled requests |

The full launch script, overlay builders and benchmark scripts are in the [home-ai-lab](https://github.com/runtimenoteslabs/home-ai-lab) repository.

## What’s next

On TensorFold, Mia’s README measures the 4-bit head and verify width adding 33% on code and 18% on prose for one stream at temperature 0. My versions added about 12% on tonyd2wild’s benchmark. The benchmarks differ, but the gap in the size of the gains suggests TensorFold’s versions go further than mine. knapcio’s 112.0 on SGLang shows there is more decode speed to find on this hardware.

Next experiments, prefill first:

1. Prefill attention, which took 2.3 seconds of the 32K profile and grows with the context.
2. The dense projections, some still on CUTLASS kernels built for Ampere rather than Blackwell.
3. A 4-bit copy of the output head for drafting.
4. Verifying fewer rows outright instead of skipping their experts, which needs more work around vLLM’s CUDA graphs.
5. Verify width for text DFlash2 already predicts well, such as counting.

[↓ Descend · 032Taking Inkling 2 Mini for a spin on NVIDIA GB10](https://runtimenotes.com/blog/inkling-2-mini-on-nvidia-gb10/) [↑ Climb · 034Not written yet](https://runtimenotes.com/)