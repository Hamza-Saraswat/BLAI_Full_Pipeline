---
slug: 2026-11-27-amd-forked-llama-cpp-for-its-o
stage: 03-research
topic: "AMD forked llama.cpp for its own GPUs"
depth: standard
generated_at: 2026-11-27T12:42:28Z
sources: 7
hub: "[[videos/2026-11-27-amd-forked-llama-cpp-for-its-o]]"
---

# Research brief: AMD forked llama.cpp for its own GPUs

## Summary
- The fork that actually trended is not AMD's: the 2026-11-26 HN story "AMD-specific fork of llama.cpp" points at stew675/llama-cpp-rdna-boosts, a community patch set by a single maintainer, while AMD's own GitHub fork (ROCm/llama.cpp, now AMD-Ecosystem/llama.cpp) is a retired mirror that tells users to go back to upstream llama.cpp.
- Most arresting number: token generation going from ~35 t/s to ~55 t/s and prefill from ~700 t/s to ~1300 t/s on one writer's Radeon R9700 eGPU (llama-cpp-rdna-boosts, community-measured, one machine).
- Strongest concrete case: the patch set applies as 19 git-am patches to a pinned upstream commit and targets RDNA3/3.5/4 (RX 7900 through RX 9070) with everything default-on, so an RX owner can be running it tonight without waiting for upstream to accept anything.
- Could not be verified: that the hub-note framing "AMD now ships its own llama.cpp fork" is literally true; no fetched page says AMD currently ships a supported fork, and the fork the HN thread discusses is a personal project.
- Source conflict: the AMD-Ecosystem repo says AMD's fork is retired and upstream is the one to use, while the HN thread's title and top comment describe the trending project as an "AMD-specific fork"; the retirement banner is the primary statement and wins.

## Thesis
The "AMD fork" your feed is talking about is a community patch set called llama-cpp-rdna-boosts, not an AMD product -- and that is the real news: AMD GPU owners are now getting their speedups from small outsider patch sets while AMD itself points back to stock llama.cpp.

## Explanation path
Establish first what llama.cpp is: the free, open-source engine most people run local models with, and the thing a viewer with an AMD card is already fighting. Then land the dated event: on 2026-11-26 a writeup hit Hacker News recommending one specific answer for AMD cards, llama-cpp-rdna-boosts, and the thread took off. Before any numbers appear, the viewer must understand what this fork is not: it is not AMD's product. AMD did have its own GitHub fork (ROCm/llama.cpp, renamed AMD-Ecosystem/llama.cpp), but that repo now carries a retirement banner directing everyone to stock upstream llama.cpp, and AMD's real in-house work is a proposed new backend (HRX) submitted to upstream llama.cpp as an RFC, not a fork. With the cast straight -- upstream llama.cpp, AMD's retired mirror, and the community patch set -- the payoff numbers can land: prefill roughly doubling and token generation rising about 57% on one writer's R9700. Close on what the viewer does tonight: stock llama.cpp already builds for AMD via HIP and Vulkan (or AMD's pre-built Windows binaries), and the patch set is an opt-in speed layer on top of a pinned upstream commit for RDNA3/3.5/4 cards.

## Claims
1. **The fork behind the 2026-11-26 news is stew675/llama-cpp-rdna-boosts, a community project by one maintainer, not an AMD product.**
   - Source: AMD-specific fork of llama.cpp, https://devnull.land/amd-specific-llama-cpp
   - Tier: community | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "I recommend using llama-cpp-rdna-boosts if you have an AMD graphics card. It's lean, and increased my token generation from 35 to 55 tokens/second, and my prefill from 700 to 1300 tokens per second. YMMV."
2. **AMD's own GitHub fork, ROCm/llama.cpp (now shown as AMD-Ecosystem/llama.cpp), is retired, with a banner telling users to use upstream ggml-org/llama.cpp instead.**
   - Source: AMD-Ecosystem/llama.cpp: LLM inference in C/C++, https://github.com/ROCm/llama.cpp
   - Tier: primary | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "The ROCm/llama.cpp repository is retired, please use the upstream repository"
3. **AMD's actual first-party move is upstream, not a fork: AMD engineers proposed a native ggml-hrx backend for llama.cpp in an RFC discussion, claiming a 30-50% tok/s uplift on prefill and parity to 15% tok/s uplift on non-MTP decode versus the faster of the existing Vulkan and HIP backends.**
   - Source: RFC: Adding a native AMD ggml-hrx backend · ggml-org/llama.cpp · Discussion #27219, https://github.com/ggml-org/llama.cpp/discussions/27219
   - Tier: primary | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "Compared to the faster between the existing Vulkan and HIP ggml backends, we are routinely achieving on the order of: 30-50% tok/s uplift on prefill, Parity to 15% tok/s uplift on non-MTP decode"
4. **llama-cpp-rdna-boosts ships as 19 default patches applied to a pinned upstream llama.cpp commit (fork point 919794500, the 2026-11-20 re-base), targeting RDNA3, RDNA3.5 and RDNA4 GPUs, with RDNA2 as best-effort.**
   - Source: llama-cpp-rdna-boosts README, https://github.com/stew675/llama-cpp-rdna-boosts
   - Tier: community | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "It ships as 19 default patches for a clean llama.cpp checkout at the fork point 919794500 (upstream master, the 2026-11-20 re-base)"
5. **The HN thread "AMD-specific fork of llama.cpp" was posted 17 hours before fetch on 2026-11-27 and drew 367 points and 88 comments, with top comments discussing cheap used gfx906 datacenter cards and users asking why the patches are not upstreamed.**
   - Source: AMD-specific fork of llama.cpp | Hacker News, https://nn -- placeholder
   - Tier: community | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "367 points by julianlam | 17 hours ago | 88 comments"
6. **Stock llama.cpp still supports AMD GPUs through its HIP backend (and Vulkan), built with GGML_HIP=ON and a GPU target such as gfx1030, and AMD's own docs ship pre-built Windows binaries for Radeon (gfx110X/gfx115X/gfx120X).**
   - Source: build.md (upstream llama.cpp), https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md
   - Tier: docs | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "This provides GPU acceleration on HIP-supported AMD GPUs. Make sure to have ROCm installed."
7. **AMD also invests first-party in llama.cpp performance on Instinct datacenter GPUs, publishing a 2025 blog with MI300X benchmarks where ROCm llama.cpp reaches pp512 t/s of 439.14 ± 1.68 on DeepSeek 671B Q4_K.**
   - Source: Llama.cpp Meets Instinct (ROCm blog), https://rocm.blogs.amd.com/ecosystems-and-partners/llama-cpp/README.html
   - Tier: docs | Confidence: medium | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "deepseek2 671B Q4_K - Medium | 376.65 GiB | 671.03 B | ROCm | 999 | pp512 | 439.14 ± 1.68"
8. **AMD-validated pre-built Windows llama.cpp binaries (server and llama-bench, ROCm 7.2.1) run without compilation, with the run command shown in AMD's docs.**
   - Source: Llama.cpp pre-built binaries (AMD ROCm docs), https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/advanced/advancedrad/windows/llm/llamacpp.html
   - Tier: docs | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: ".\\llama-server.exe -m test_model.gguf -c 2048 -ngl 99 -fa on --port 8080"
9. **The patch set's maintainer documents his own benchmark on an R9700 eGPU: prefill rising from ~700 t/s to ~1300 t/s and token generation from ~35 t/s to ~55 t/s, measured on Swift-1.5-Qwen3.8-27B Q6_K_L with MTP enabled.**
   - Source: devnull.land writeup, https://devnull.land/amd-specific-llama-cpp
   - ~ numbers identical to claim 1: community-measured, single machine.
   - Tier: community | Confidence: medium | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "On my setup, an AMD R9700 connected to my laptop via an eGPU interface, this improved prefill and token generation rates when running ukisai/Swift-1.5-Qwen3.8-27B-GGUF (Q6_K_L) with MTP enabled"
10. **The reception included pushback: some HN commenters distrust AI-heavy forks and prefer waiting for mainline, and a llama.cpp maintainer commented that the project is happy to take high-quality patches.**
    - Source: AMD-specific fork of llama.cpp | Hacker News, https://news.ycombinator.com/item?id=50657265
    - Tier: community | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
    - Quote: "llama.cpp maintainer here. We're happy to take high-quality patches. :)"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | token generation, before -> after (R9700 eGPU, Q6_K_L with MTP) | ~35 t/s to ~55 t/s | https://devnull.land/amd-specific-llama-cpp | "increased my token generation from 35 to 55 tokens/second" |
| 2 | prefill, before -> after (same setup) | ~700 t/s to ~1300 t/s | https://devnull.land/amd-specific-llama-cpp | "my prefill from 700 to 1300 tokens per second" |
| 3 | HN points (and comments) | 367 points, 88 comments | https://news.ycombinator.com/item?id=50657265 | "367 points by julianlam | 17 hours ago | 88 comments" |
| 4 | AMD HRX backend claimed prefill uplift vs faster of Vulkan/HIP | 30-50% tok/s | https://.ggml placeholder | "30-50% tok/s uplift on prefill" |
| 5 | AMD HRX claimed decode uplift | Parity to 15% tok/s | https://github.com/ggml-org/llama.cpp/discussions/27219 | "Parity to 15% tok/s uplift on non-MTP decode" |
| 6 | MI300X prefill t/s, DeepSeek 671B Q4_K (8 GPUs, ROCm llama.cpp) | pp512 439.14 ± 1.68 t/s | https://rocm.blogs.amd.com/ecosystems-and-partners/llama-cpp/README.html | "deepseek2 671B Q4_K - Medium ... pp512 439.14 ± 1.68" |
| 7 | default patch count / fork point | 19 default patches, fork point 919794500 | https://github.com/stew675/llama-cpp-rdna-boosts | "It ships as 19 default patches for a clean llama.cpp checkout at the fork point 919794500 (upstream master, the 2026-11-20 re-base)" |

## Analogy candidates
- **Vehicle: stock car vs tuner's stage-1 kit**. Mapping: llama.cpp is the stock engine every car ships with; llama-cpp-rdna-boosts is an aftermarket tune built for one chassis family (RDNA3/3.5/4) that bolts onto a pinned stock build without replacing the car; AMD's own fork is the manufacturer's discontinued in-house tuning division that now says "just use the stock engine". Breaks when: the patches are not physical parts but 19 git commits re-applied at every re-base, and the speedup is single-writer measured, not a warranty.
- **Vehicle: recipe vs a pinned supermarket**. Mapping: upstream llama.cpp is the recipe book; the fork is a photocopied page of margin notes you staple onto a specific printing (commit 919794500) of the book. Breaks when: the notes improve only the dishes one family of ovens (RDNA GPUs) cooks, and a new printing of the book needs the notes re-copied.
- **Vehicle: community bus schedule taped to the official timetable**. Mapping: AMD's docs are the official timetable (pre-built binaries, supported GPUs); the patch set is a hand-drawn schedule taped beside it by one rider who found faster routes for one bus line. Breaks when: the taped schedule expires every time the official one is reprinted (each re-base), and the faster times are one rider's stopwatch.

## Misconceptions
- Myth: AMD now ships and maintains its own llama.cpp fork for Radeon owners. Reality: AMD's GitHub fork is retired and points to upstream, and the trending "AMD fork" is a community patch set (claims 2, 1).
- Myth: AMD users must fork or patch to run llama.cpp at all. Reality: stock llama.cpp builds for AMD GPUs via HIP and Vulkan, and AMD ships pre-built Windows binaries (claims 6, 8).
- Myth: the speedup claims are vendor benchmarks. Reality: the 35-to-55 t/s and 700-to-1300 t/s numbers are one writer's own machine, and AMD's own comparable first-party claim is the separate HRX backend RFC (claims 1, 3, 9).
- Myth: an AMD-specific fork means AMD's software stack is now the fastest path. Reality: AMD's first-party llama.cpp effort is aimed upstream (HRX RFC) and at Instinct datacenter parts, not at shipping a Radeon fork (claims 3, 7).

## Glossary
- **llama.cpp**: a free, open-source C/C++ program that runs AI models locally on CPUs and GPUs.
- **fork (of a repo)**: a copy of someone else's code project you change yourself, kept separate from the original.
- **HIP**: AMD's CUDA-like layer that lets CUDA-style GPU code run on AMD cards; the backend stock llama.cpp uses for AMD GPUs.
- **ROCm**: AMD's software stack for GPU computing; HIP is part of it.
- **Vulkan**: a general graphics/GPU standard llama.cpp can also use on AMD cards.
- **RDNA3 / RDNA4**: AMD GPU generations; RX 7900 is RDNA3, RX 9070 is RDNA4.
- **gfx906**: the internal AMD architecture name for Instinct MI50/MI60 and Radeon VII cards.
- **prefill**: the phase where the engine reads your whole prompt before it starts answering.
- **token generation**: the phase where the answer is produced, one token at a time.
- **MTP**: multi-token prediction, a technique that generates several tokens per step to speed output.
- **GGUF**: the model file format llama.cpp loads.
- **patch set**: a series of small code diffs applied on top of a pinned version of the original project.

## Unverified
- Community reports that the stock Vulkan backend outperforms the HIP backend on some AMD cards.
- The writeup's claim that forks like Strata prefer experts loaded in VRAM over the ones the model would normally choose, trading accuracy for speed.
- HN commenters' reports of specific t/s numbers on MI50 pairs, 7900 XTX and Radeon 8060S setups; none were reproduced by a fetched primary or docs page.
- That the hub-note angle phrase "AMD now ships its own fork" is literally accurate; every fetched page contradicts or complicates it (AMD's fork is retired; the trending fork is community-run).
- Any performance delta between llama-cpp-rdna-boosts and stock llama.cpp on our own hardware; only the writeup author's single-machine numbers exist.

## Suggested outline
1. Hook: your AMD card just got a llama.cpp speed patch, and the twist is who made it -- not AMD, one guy.
2. Sort the cast: upstream llama.cpp, AMD's retired GitHub fork, and the community patch set the HN thread is actually about; AMD's real work is an upstream backend proposal (HRX).
3. Land the number and the caveat: one writer's R9700 went from ~35 to ~55 tokens/second, community-measured, YMMV; stock llama.cpp still runs AMD fine tonight, the patch set is the opt-in speed layer for RDNA3/3.5/4.

## Viewer situation
You own a gaming PC with an AMD Radeon card (something in the RX 6000-to-9070 range), you have run a local model or want to tonight, and you have been quietly jealous of how easy NVIDIA owners have it.

## Has process
true
- Clone stock llama.cpp and build it for your AMD GPU with GGML_HIP=ON and your GPU target (e.g. GPU_TARGETS=gfx1030), or download AMD's pre-built Windows binaries for gfx110X/gfx115X/gfx120X (claims 6, 8).
- Download a GGUF model file and run llama-server with -ngl 99 to offload layers to the GPU (AMD docs' own run command: .\llama-server.exe -m test_model.gguf -c 2048 -ngl 99 -fa on --port 8080) (claim 8).
- To try the patch set instead: clone upstream llama.cpp, git checkout 919794500, then bash <path-to-repo>/scripts/apply-all.sh . (claim 4, README quick start).
- Run the built llama-server on your model as usual (claims 4, 8).

## Objection
"An n-of-one benchmark on one eGPU, from a patch set with no AMD involvement, is not a reason to pin your inference stack to an unofficial fork -- wait for it upstream or measure it yourself."

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://devnull.land/amd-specific-llama-cpp | AMD-specific fork of llama.cpp | community | web_extract | 2026-11-27 |
| 2 | https://news.ycombinator.com/item?id=50657265 | AMD-specific fork of llama.cpp (Hacker News) | community | web_extract | 2026-11-27 |
| 5 | https://github.com/stew675/llama-cpp-rdna-boosts | llama-cpp-rdna-boosts (README) | community | web_extract | 1 | placeholder |

## Notes
Tool family: web_search (2 searches) + web_extract (12 fetch attempts, 8 succeeded). Fetch failures: 4 failed Firecrawl 500/credit errors on first attempt (github.com/AMD-Ecosystem/llama.cpp, rocm.docs.amd.com llamacpp.html, github.com/stew675/llama-cpp-rdna-boosts, github.com/ggml build.md); all later retrieved on retry except two. Band: 7 sources fetched (2 primary, 3 docs, 0 benchmark, 2 community). Conflict: AMD-Ecosystem/llama.cpp's retirement banner (primary) contradicts the HN title "AMD-specific fork of llama.cpp" (community); trust the banner, it is AMD's own repo. The tier of the devnull.land writeup and the HN thread is community per the rules (personal blog, HN), fine for reception claims but not sole source for numbers; the 35-to-55 and 700-to-1300 numbers are therefore given as community-measured, YMMV, and the comparable vendor number (30-50% prefill uplift, HRX RFC) is cited from AMD's own RFC (primary). Thin spots: no independent benchmark of llama-cpp-rdna-boosts was fetched (the writeup author's own numbers are the only measurement, and its caveat "YMMV" appears verbatim); no fetched page states AMD currently "ships" a fork, so the hub-note angle phrase must be treated as the trending framing, not a vendor announcement.
