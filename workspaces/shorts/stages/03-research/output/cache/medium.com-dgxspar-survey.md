https://medium.com/@vito.rallo/coding-models-on-dgx-spark-state-of-the-art-of-september-2026-94cbaff6d1c9
Accessed: 2026-09-23

# Coding models on DGX-Spark, state of the art of September 2026 | by Vito Rallo | Sep, 2026 | Medium

Three inference servers, six models (one only on paper), a dozen configs, a stack of patches, one very warm box on my desk. Where the DGX Spark stands for local coding agents in September 2026.

Every few weeks a new open model shows up with a benchmark chart that makes you want to cancel your API subscriptions. September has been ridiculous. DeepSeek dropped V4.1 Flash on the 10th. GLM-5.3-Flash is all over the news. Qwen3.8 keeps getting better quantized exports. And antirez, yes, the Redis guy, has a tiny purpose-built inference engine called ds4 that picked up CUDA support for the Spark a few days ago.

I run coding agents against my DGX Spark every day and I do it a lot to provide an LLM to Foil, my security scanner (foil.peachstudio.be). But I also attach coding agents like Claude Code that talks to it through an Anthropic-compatible endpoint, pi talks to it through the OpenAI one. My daily driver was Qwen3.8-27B on SGLang with DFlash2 speculative decoding.

## Why I don't care about your peak tokens per second

Claude Code sends a 23,000-token prompt with a chunk of your repository in it. The model answers. You ask a follow-up. Now the agent sends those same 23,000 tokens again, plus the answer, plus your new question. And again, and again.

Three numbers decide whether that feels snappy or miserable:

1. Decode speed, the tokens per second while text streams. This is the number everyone quotes.
2. Cold prefill, how long the model chews on that big first prompt before it says anything.
3. Warm turns, how much of the growing conversation the engine pulls from its prefix cache (a saved copy of work it already did) instead of recomputing from scratch.

The third one is the silent killer. If your engine forgets the conversation between turns, you pay the full prefill every single time. A beautiful 50 tok/s decode means nothing if every turn starts with a 22-second stare at a blinking cursor.

## The box and the rules

The Spark is NVIDIA's little Grace Blackwell desktop: a GB10 chip and 128 GB of unified memory that the CPU, GPU and operating system all share. That sharing matters more than you'd think.

Here's the first trap. Crank the GPU memory fraction to 0.85, a number you'll see in plenty of recipes, and the OS is left with about 8 GB. That's exactly where DGX OS's out-of-memory killer starts shooting processes. The SGLang cookbook reports 15 of 48 boots killed at 0.85. I ran everything at 0.80 or lower and lost zero boots.

The contenders:

- SGLang (nightly, September 9 build)
- vLLM (0.28.1 nightly for aarch64)
- ds4, antirez's narrow, opinionated engine, built from source with `make cuda-spark`

And the models:

- Qwen3.8-27B, a dense 27B "thinking" model, NVFP4 quantized (about 21 GB)
- Qwen3-Coder-Next, an 80B mixture-of-experts coder with only ~3B parameters active per token (46 GB)
- Qwen3.8-Flash-Next, a 125B MoE whose NVFP4 checkpoint is bigger than the whole Spark. I ran it anyway, with a patched vLLM image and a few dirty tricks
- GLM-5.3-Flash, a Q2 GGUF on ds4 (96.5 GB on disk, which is a lot of Spark)
- DeepSeek V4.1 Flash, which I did not test. After a round of research my verdict was a no-go on a single Spark, and I'll show you why

One methodology note before the numbers, because it bit me. I started benchmarking with the servers' default sampling. Then I ran the exact same server twice and got 42.6 tok/s, then 53.6 tok/s. Same prompt. Same config. A 26% swing.

Speculative decoding speed depends on how many guessed tokens get accepted, and that depends on which tokens get randomly sampled. So a short sampled test can't tell you anything under a ~20% difference. I switched everything to greedy decoding (temperature 0), and repeat runs landed within 0.3% of each other.

## Round one: the cookbook recipe loses

Speculative decoding means a small, fast "draft" model guesses the next several tokens and the big model checks them all in one pass. When the guesses are good, you get several tokens for the price of one. DFlash2 and DSpark are two flavors of draft model for Qwen3.8-27B.

The SGLang cookbook recommends DSpark with an FP4 export. It didn't.

DSpark was 14% slower on code and 21% slower on prose. Same checkpoint, same prefill, same caching. A community benchmark on the same hardware found roughly the same thing, so it's not just my box being weird.

Then the cookbook's default for the recurrent state dtype. Qwen3.8 is a hybrid model: 48 of its 64 layers are Gated DeltaNet, a linear-attention design that carries a running "state" instead of a full attention cache. The cookbook defaults that state to float32 because the checkpoint declares it, and notes it can help speculative acceptance.

On the Spark: No acceptance benefit. No decode benefit. Just 40% slower prefill and 16 GB of memory gone, which also shrank the KV cache from 1.24M tokens to 822K. Use bfloat16 on a Spark. Don't argue with me about it.

(Funny footnote: the same bf16 switch did nothing for vLLM's prefill, 986 vs 1,042 tok/s. Its bottleneck lives somewhere else.)

## Round two: the win

The model's lm_head is the final matrix that turns the model's internal representation into a score for every word in the vocabulary. For Qwen3.8 that's 5,120 dimensions projected onto roughly 152,000 tokens. It runs for every token generated and, with DFlash2, for every draft candidate it has to score.

There are two NVFP4 exports of Qwen3.8-27B floating around. Identical 4-bit bodies. One keeps that head in BF16, the other packs it to FP4. I'd been running the BF16 one for weeks without thinking about it.

A 4-bit output head bought me more speed than a newer speculative decoder did. My guess at the mechanism: decode on the GB10 is limited by memory bandwidth, not compute, so reading a matrix four times smaller on every step pays off directly.

note: I measured speed, not quality. The cookbook's GSM8K numbers put both exports at 93-95%, which is reassuring, but it's not a coding eval. my dashboard reproduced it at 47.2 tok/s.

## Round three: SGLang vs vLLM

Same model, Qwen3.8-27B, on vLLM with its built-in MTP speculative head.

SGLang wins everywhere except acceptance, where vLLM's MTP head guesses right far more often and still loses on speed. A high acceptance rate means nothing if each verification step is expensive. Acceptance isn't speed. I'll say it again at parties.

vLLM's MTP acceptance by draft position went 88%, 72%, 56%, 45%, 35%. The last two positions rarely land, so I assumed MTP-3 would be faster. It was slower on code. Code is predictable enough that long drafts pay off even when they mostly miss at the tail.

I tried hard to close the prefill gap. bf16 state, fp32 state, fp8 KV cache, bf16 KV cache, MTP-3, MTP-5. vLLM prefilled this model at 990-1,070 tok/s in every single configuration. Nothing I could tune worked.

Even the best vLLM config only cached 16,160 of a possible ~22,600 tokens on turn 2. Checkpoints inside the final partial prefill step still weren't kept.

And then the gotcha that ate my afternoon. The interval has to be a multiple of a scheduler block size that vLLM computes at boot. That block size changes depending on your other flags: Pick a wrong interval and vLLM refuses to start, but only after spending several minutes loading weights. Three failed boots. Read the `Setting attention block size to N tokens` line in your log before you pick a number.

## The twist: the fastest thing on the box is the "worse" model

Qwen3-Coder-Next is an 80B mixture-of-experts coder with about 3B parameters active per token, and it doesn't think out loud. I ran it on vLLM with a GB10-calibrated NVFP4 checkpoint and an EAGLE3 draft model that's only 1 GB.

Holy-cow!!! 85 tokens per second on code, on a desk. A 21K-token repository context prefilled in under six seconds. EAGLE3 accepted only 1.63 tokens per step and still added 34% on code, because with just 3B active parameters.

Two more things I learned the hard way. The checkpoint card's Marlin kernel recipe was written for older vLLM; on 0.28 those environment variables are silently ignored. And checkpoint choice dwarfs flags: Same model, six times slower, depending on who quantized it. Also, the GB10 checkpoint's original repo is gated; there's an ungated byte-identical mirror if your downloads keep failing.

There's a catch on long contexts too. Qwen3.8-27B decodes at the same ~27 tok/s at 23K and 72K tokens deep (prefill drops ~27%, from 1,749 to 1,285 tok/s, so a 72K prompt takes 56 seconds). The community's GB10 numbers for Coder-Next show it falling off hard with depth: 72 tok/s at 2K, 38 at 33K, 14.5 at 131K, 8.8 at 250K. At 21K I still measured ~65.

So why isn't this my default? Because on the one benchmark both model cards report, SWE-bench Pro, Coder-Next scores 44.3 and Qwen3.8-27B scores 61.7. Those are vendor numbers, not mine, but a 17-point gap is a gap.

That's the real finding of the day. Speed vs quality on a Spark is no longer a hardware limit. It's a per-task choice. Boilerplate and tight edit-run loops go to the fast coder. Security reviews and gnarly refactors go to the model that thinks.

## Qwen3.8-Flash-Next: the model that doesn't fit, running anyway

Qwen3.8-Flash-Next is a 125B mixture-of-experts model with 6B parameters active per token, plus a 51B-parameter n-gram embedding table (Qwen calls it PLE). That table is a pure lookup: each token touches just 16 of its rows. The community NVFP4 checkpoint (RadixArk) is 122 GiB. The Spark's entire usable pool is 121 GiB. You can't fix that with --gpu-memory-utilization. It doesn't fit before you've allocated a single token of cache.

And no, vLLM's built-in VLLM_PLE_CPU_OFFLOAD doesn't save you. It moves the table to "host RAM." On a Spark, host RAM and GPU memory are the same physical chips. Offloading from your left pocket to your right pocket doesn't free anything.

There's no official way to run this model on one Spark yet. So I went the dirty way: a small community repo, blazux/qwen3.8-Flash-DGX, that takes vLLM's Flash-Next image and patches it. I vendored it at commit 209646c, read every patch before building, and verified that the upstream bugs it cites are real and still open.

Here's the bag of tricks: Turn on prefix caching, the most normal flag in the world, and without the patch you get confident, fluent, wrong output on every cache hit.

One more trap: the repo defaults to GPU_MEM=0.85. At that setting I had 11 GB of available memory and 2 GB of swap in use. At 0.80 I got 16 GB available and the same throughput. Same lesson as before: the Spark shares memory with the OS, so leave it room.

The numbers, from my smoke test and the engine's own logs. This run was on September 1, and it didn't go through the same benchmark script as the others: So: a model bigger than the machine, running at 23 tok/s, with ~1,170 tok/s prefill and working 1.4-second warm turns. Speed-wise that's in the same league as vLLM running the much smaller 27B (22.8 tok/s in agent turns). And it prefills faster than vLLM does on the 27B. Reading 44 GiB of weights off an SSD is not supposed to feel this usable.

Would I make it my daily driver? Not yet. Fifteen minutes to boot, a community quant, a stack of patches pinned to one commit, and a wrapper that exists because upstream hasn't caught up.

## ds4: the engine I want to love

ds4 is antirez's inference engine, and it's the opposite of vLLM in philosophy. No giant Python stack, no container, no plugin zoo. A narrow C codebase that supports a short list of model families and tries to run them really well. It builds with a single `make cuda-spark`. It served GLM-5.3-Flash with an Anthropic-compatible /v1/messages endpoint right away.

Before running anything I read the doc, because ds4 is picky about what it supports. GLM 5.2/5.3 have a real CUDA path. Qwen3.8-Flash-Next does not. I really wanted a second route for Flash-Next, so I downloaded antirez's 137 GiB Q2 GGUF anyway. (Only ~42 GiB of it stays resident, because ds4 reads the 95 GiB n-gram table straight from the file.) The server refused to start on CUDA: `Qwen3.8 requires single-host Metal (or --cpu --first-token-test)`. So for now, Flash-Next on ds4 is a Mac thing, and on a Spark it's the patched vLLM or nothing.

The good stuff on load was genuinely impressive. ds4 repacked the 96.5 GB Q2 GGUF into 372 aligned CUDA artifacts (86.9 GiB) in 14.3 seconds and was listening shortly after. Compare that to the 8-11 minutes vLLM spends loading Coder-Next. And GLM's compact sparse-attention cache needed only 0.18 GiB for a 16K context. That is tiny.

Then the numbers. This was a smoke test from the server log, not the full harness: There's no speculative decoding for GLM yet. The source literally says `--mtp-model is not supported for GLM yet`. So 17.6 tok/s is plain autoregressive decode on a Q2 quant that eats three quarters of the box. Ahh yes, I forgot to tell, it's a quant 2bit :) not 4 like the other models, mind that!

I didn't expect ds4 to win this, and it didn't. It's five times slower than Coder-Next on decode and doesn't reuse the prefix on repeated prompts. But we are running GLM 5.3 folks, it's a beasty model. Look at the trajectory. CUDA support for the Spark landed on September 13. Single-Spark prefill for DeepSeek V4.1 roughly doubled a day later. antirez ships fast, the codebase is small enough to actually read, and the boot time already embarrasses the big engines. When MTP and prefix rewind land, I'm re-running all of this; can't wait.

## DeepSeek V4.1 Flash: a no-go on one Spark, so I didn't test it, yet

DeepSeek V4.1 Flash is the hot one this month, and it was the first thing people asked me about. So let me save you an evening. I did the research before downloading anything, and the answer was clear enough that I never ran it. On one Spark, it's a no-go until antirez comes with some form of miracle like for GLM.

The reason is size, and it's not close.

It's a 552B mixture-of-experts backbone plus 196B of "Engram" lookup tables, around 763B stored parameters. The official checkpoint is 510 GB. ds4's Q2 GGUF is 341 GiB.

The Spark gives you about 121 GiB of usable memory. The smallest quant I found, llama.cpp's Q2_K, is 246 GiB, still twice that. The only single-box options stream weights from the SSD, and the community's numbers show what that costs. None of these are mine (community stats): Under 10 tok/s is not a coding agent. It's a screensaver. That's why I stopped at the research. For completeness, two Sparks can run a heavily compressed version at "patient human" speed, and nobody has measured what 2.9-bit quantization does to tool-call reliability. Four Sparks is the honest answer, and at that point you've bought a very expensive hobby.

Frontier-class open models have outgrown the single desktop box. That's not a knock on the Spark. It's just the math. Hope now goes to DGX-Station.

## The full scoreboard

Every greedy run from the day, in one place. Agent-turn decode is the mean across prime, turn 2 and turn 3.

Coder-Next's tokenizer encodes the same repository text as 21.4K tokens instead of 23.2K, so compare the TTFT seconds across models, not just tok/s.

## What's running on my desk tonight

One tip if you use Claude Code with a thinking model: Claude Code can't send `chat_template_kwargs`, so make non-thinking the server default with --default-chat-template-kwargs '{"enable_thinking": false}'. In my thinking-on check, a 200-token budget got spent entirely on reasoning before a single useful word came out. Thinking doesn't lower tok/s. It just spends your tokens on monologue.

## So, is the DGX Spark worth it in September 2026?

For one developer running coding agents locally, yes, and more than it was in the spring. A year ago the story was "it runs, slowly." Today I get 85 tok/s from a solid coder and a 27B reasoning model with sub-second warm turns, on a box that sits quietly next to my monitor and never sends my client's code to anyone's API. For security work, that last part isn't a nice-to-have.

But go in with your eyes open.

The hardware isn't the bottleneck anymore. Your configuration is. Every meaningful gain I found came from reading logs, checking checkpoints and distrusting defaults, including the defaults in the official cookbook. The difference between my worst and best 27B config was 22 seconds vs 0.3 seconds on a follow-up turn. Same box. Same model.

And the frontier is running away from it. DeepSeek V4.1 Flash needs two to four Sparks, or a quant nobody has evaluated for real coding work. Qwen3.8-Flash-Next only runs because a handful of people patched vLLM and moved 44 GiB of it onto an SSD. Clever, and it works, but it's not a supported product. If your plan is "run the newest DeepSeek on one box," the Spark will disappoint you.

_All numbers measured on a single DGX Spark (GB10), single stream, using SGLang nightly 708f51e44, vLLM 0.28.1rc1.dev199 and a ds4 build from the week of September 16, 2026, unless marked as community or vendor numbers. Qwen3.8-Flash-Next was measured on September 1 with the vLLM Flash-Next image patched by blazux/qwen3.8-Flash-DGX at commit 209646c. Speed only; I didn't run quality evals. Nightly builds move fast, so these numbers have a shelf life measured in days._

_Originally published at https://vitorallo.github.io/blog/2026/dgx-spark-coding-models/_
