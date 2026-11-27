---
slug: 2026-11-27-amd-forked-llama-cpp-for-its-o
stage: 03-research
topic: "AMD forked llama.cpp for its own GPUs"
depth: standard
generated_at: 2026-11-27T12:42:28Z
sources: 8
hub: "[[videos/2026-11-27-amd-forked-llama-cpp-for-its-o]]"
---

# Research brief: AMD forked llama.cpp for its own GPUs

## Summary
- The "AMD-specific fork of llama.cpp" that trended is a one-maintainer community patch set, stew675/llama-cpp-rdna-boosts, while AMD's own GitHub fork is retired with a banner pointing back to upstream, and AMD's first-party push is a backend proposal to upstream, not a shipped fork.
- Most arresting number: 367 points and 88 comments on Hacker News in roughly 17 hours; the writeup's hook number, token generation going from 35 to 55 tokens/second on one R9700 eGPU, is a single user's measurement and no fetched primary or docs page corroborates it.
- Strongest concrete case: 19 default patches applied to a pinned upstream commit (fork point 919794500, the 2026-11-20 re-base) covering RDNA3, RDNA3.5 and RDNA4 cards, everything default-on, applicable tonight with one script.
- What could not be verified: that AMD currently ships, endorses or maintains a llama.cpp fork for Radeon owners; every primary page fetched points the other way (retired repo, upstream RFC, pre-built stock binaries).
- Source conflict: the HN title says "AMD-specific fork" but the project it discusses is community-run, and AMD's retired fork banner says use upstream; trust the repo banners over the headline, they are the primary statements.

## Thesis
The "AMD fork" your feed is talking about is a one-maintainer community patch set called llama-cpp-rdna-boosts, not an AMD product, and that is the real news: Radeon owners are getting their speedups from outsider patches pinned to stock llama.cpp while AMD itself points back upstream.

## Explanation path
Open on the machine the viewer already owns: a gaming PC with a Radeon card and a copy of llama.cpp, the free engine that runs models locally. Establish the pain before any news appears: stock llama.cpp speaks NVIDIA's CUDA best, and AMD owners have historically patched, pinned and prayed. Land the dated event: a writeup recommending one specific answer, llama-cpp-rdna-boosts, hit Hacker News around 2026-11-26 and drew 367 points. Sort the cast the headline blurs before any numbers appear: stock upstream llama.cpp, which still builds for AMD GPUs through HIP and Vulkan and even ships as AMD-validated pre-built Windows binaries; AMD's own GitHub fork, which is retired and points back upstream; and the community patch set the thread is actually about, 19 patches pinned to one upstream commit. With the cast straight, the payoff can land: the writeup's author reports token generation going from 35 to 55 tokens/second on his R9700, one machine, YMMV. Close on what AMD is actually doing, an HRX backend proposed upstream, and what the viewer does tonight: build stock or pull pre-built binaries, and treat the patch set as an opt-in speed layer, not a new engine.

## Claims
1. **The fork behind the news is llama-cpp-rdna-boosts, a community patch collection maintained by GitHub user stew675, which ships as 19 default patches applied to a pinned upstream llama.cpp checkout at fork point 919794500 (the 2026-11-20 re-base), targeting RDNA3, RDNA3.5 and RDNA4 GPUs with RDNA2 as best-effort.**
   - Source: stew675/llama-cpp-rdna-boosts, https://github.com/stew675/llama-cpp-rdna-boosts
   - Tier: primary | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "It ships as 19 default patches for a clean llama.cpp checkout at the fork point 919794500 (upstream master, the 2026-11-20 re-base)"
2. **The devnull.land writeup that trended recommends llama-cpp-rdna-boosts to AMD card owners and credits it with raising the author's token generation from 35 to 55 tokens/second and his prefill from 700 to 1300 tokens per second on an R9700 eGPU, a single-machine result the author himself flags as YMMV.**
   - Source: AMD-specific fork of llama.cpp (devnull.land), https://devnull.land/amd-specific-llama-cpp
   - Tier: community | Confidence: medium | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "I recommend using llama-cpp-rdna-boosts if you have an AMD graphics card. It's lean, and increased my token generation from 35 to 55 tokens/second, and my prefill from 700 to 1300 tokens per second. YMMV."
3. **The writeup hit Hacker News as "AMD-specific fork of llama.cpp" around 2026-11-26 and drew 367 points and 88 comments within roughly 17 hours of posting.**
   - Source: AMD-specific fork of llama.cpp | Hacker News, https://news.ycombinator.com/item?id=50657265
   - Tier: community | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "367 points by julianlam | 17 hours ago | 88 comments"
4. **AMD's own GitHub llama.cpp fork, ROCm/llama.cpp (now displayed as AMD-Ecosystem/llama.cpp), is retired, with a banner directing users to the upstream ggml-org/llama.cpp repository.**
   - Source: AMD-Ecosystem/llama.cpp: LLM inference in C/C++, https://github.com/AMD-Ecosystem/llama.cpp
   - Tier: primary | Confidence: high | Accessed: 2026-11-27 | Via: web_extract (fetched via redirect from https://github.com/ROCm/llama.cpp)
   - Quote: "The ROCm/llama.cpp repository is retired, please use the upstream repository"
5. **AMD's first-party llama.cpp work goes upstream rather than into a fork: the ggml-hrx backend RFC by AMD engineers claims a 30-50% tok/s uplift on prefill and Parity to 15% tok/s uplift on non-MTP decode compared to the faster of the existing Vulkan and HIP backends.**
   - Source: RFC: Adding a native AMD ggml-hrx backend · ggml-org/llama.cpp · Discussion #27219, https://github.com/ggml-org/llama.cpp/discussions/27219
   - Tier: primary | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "Compared to the faster between the existing Vulkan and HIP ggml backends, we are routinely achieving on the order of: 30-50% tok/s uplift on prefill, Parity to 15% tok/s uplift on non-MTP decode"
6. **Stock llama.cpp still supports AMD GPUs through its HIP backend, built with GGML_HIP=ON and a GPU target such as gfx1030, alongside a Vulkan backend.**
   - Source: build.md (upstream llama.cpp docs), https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md
   - Tier: docs | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "This provides GPU acceleration on HIP-supported AMD GPUs. Make sure to have ROCm installed."
7. **AMD publishes AMD-validated pre-built Windows llama.cpp binaries (rocm-rel-7.2.1 for gfx110X, gfx115X and gfx120X) and documents running llama-server with -ngl 99 to offload all layers to the GPU.**
   - Source: Llama.cpp pre-built binaries (Use ROCm on Radeon and Ryzen), https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/advanced/advancedrad/windows/llm/llamacpp.html
   - Tier: primary | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: ".\\llama-server.exe -m test_model.gguf -c 2048 -ngl 99 -fa on --port 8080"
8. **AMD also invests first-party in llama.cpp on Instinct datacenter GPUs, publishing MI300X benchmarks where DeepSeek 671B Q4_K reaches pp512 439.14 ± 1.68 t/s across 8 MI300X GPUs.**
   - Source: Llama.cpp Meets Instinct: A New Era of Open-Source AI Acceleration (ROCm blog), https://rocm.blogs.amd.com/ecosystems-and-partners/llama-cpp/README.html
   - Tier: docs | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "deepseek2 671B Q4_K - Medium | 376.65 GiB | 671.03 B | ROCm | 999 | pp512 | 439.14 ± 1.68"
9. **HN reception included pushback on speed-chasing forks, with one commenter arguing that changes like Strata's can degrade the model's performance, while a self-identified llama.cpp maintainer replied that the project is happy to take high-quality patches.**
   - Source: AMD-specific fork of llama.cpp | Hacker News, https://news.ycombinator.com/item?id=50657265
   - Tier: community | Confidence: high | Accessed: 2026-11-27 | Via: web_extract
   - Quote: "llama.cpp maintainer here. We're happy to take high-quality patches. :)"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | HN thread score (roughly 17 hours after posting) | 367 points | https://news.ycombinator.com/item?id=50657265 | "367 points by julianlam \| 17 hours ago \| 88 comments" |
| 2 | HN thread comments | 88 comments | https://news.ycombinator.com/item?id=50657265 | "367 points by julianlam \| 17 hours ago \| 88 comments" |
| 3 | AMD HRX claimed prefill uplift vs faster of Vulkan/HIP | 30-50% tok/s uplift on prefill | https://github.com/ggml-org/llama.cpp/discussions/27219 | "30-50% tok/s uplift on prefill" |
| 4 | AMD HRX claimed non-MTP decode uplift | Parity to 15% tok/s uplift on non-MTP decode | https://github.com/ggml-org/llama.cpp/discussions/27219 | "Parity to 15% tok/s uplift on non-MTP decode" |
| 5 | MI300X pp512 t/s, DeepSeek 671B Q4_K, 8 GPUs, ROCm llama.cpp | 439.14 ± 1.68 t/s | https://rocm.blogs.amd.com/ecosystems-and-partners/llama-cpp/README.html | "deepseek2 671B Q4_K - Medium \| 376.65 GiB \| 671.03 B \| ROCm \| 999 \| pp512 \| 439.14 ± 1.68" |
| 6 | rdna-boosts default patch count (fork point 919794500) | 19 default patches | https://github.com/stew675/llama-cpp-rdna-boosts | "It ships as 19 default patches for a clean llama.cpp checkout at the fork point 919794500 (upstream master, the 2026-11-20 re-base)" |

## Analogy candidates
- **Vehicle: an aftermarket tune for one engine family**. Mapping: llama.cpp is the stock engine everyone gets; llama-cpp-rdna-boosts is a tuner's kit that bolts onto one specific production run of that engine (commit 919794500) and is re-fitted each time the factory reprints it; AMD's own fork is the manufacturer's discontinued in-house tuning shop whose door now says "use the stock engine". Breaks when: the tune is 19 software patches maintained by one person, not parts you buy once, and the advertised gains are one driver's stopwatch, not a dyno sheet.
- **Vehicle: handwritten margin notes on a pinned printing of a cookbook**. Mapping: upstream llama.cpp is the cookbook every kitchen uses; the patch set is a photocopied page of margin notes you staple to a specific printing, good only for the ovens in one family (RDNA3/3.5/4). Breaks when: a new printing arrives every re-base and the notes must be re-copied, and the notes improve only some dishes, not the whole book.
- **Vehicle: a hand-drawn faster bus route taped beside the official timetable**. Mapping: AMD's docs are the official timetable (pre-built binaries, supported cards); the patch set is one rider's hand-drawn shortcut taped next to it. Breaks when: the tape peels off every timetable reprint, and the "faster" times are that rider's own commute, not the transit authority's.

## Misconceptions
- Myth: AMD now ships and maintains its own llama.cpp fork for Radeon owners. Reality: AMD's GitHub fork is retired and points to upstream, and the trending "AMD fork" is one maintainer's patch set (claims 4, 1).
- Myth: AMD owners must use a fork or patch set to run llama.cpp at all. Reality: stock llama.cpp builds for AMD GPUs via HIP and Vulkan, and AMD itself ships pre-built Windows binaries (claims 6, 7).
- Myth: the token-generation gains being shared are official benchmarks. Reality: they are one blogger's own single-machine measurement, flagged YMMV; AMD's own first-party performance claim is the separate, upstream HRX backend RFC (claims 2, 5).
- Myth: an "AMD-specific fork" means AMD's software stack is now the fastest supported path for Radeon. Reality: AMD's first-party llama.cpp effort targets an upstream backend (HRX) and Instinct datacenter parts, not a shipped Radeon fork (claims 5, 8).

## Glossary
- **llama.cpp**: a free, open-source C/C++ program for running AI models locally on your own CPU and GPU.
- **fork**: a copy of someone else's open-source project that you change yourself, kept separate from the original.
- **patch set**: a series of small code changes designed to be applied on top of a specific version of the original project.
- **HIP**: AMD's translation layer that lets CUDA-style GPU code run on AMD cards; the backend stock llama.cpp uses for AMD GPUs.
- **ROCm**: AMD's software stack for GPU computing; HIP is part of it.
- **Vulkan**: a general graphics-and-compute standard that llama.cpp can also use to run on AMD cards.
- **RDNA3 / RDNA4**: AMD GPU generations; RX 7900-series cards are RDNA3, RX 9070-series are RDNA4.
- **prefill**: the phase where the engine reads your whole prompt before it starts answering.
- **token generation**: the phase where the answer is produced, one token at a time; its speed is the "t/s" number.
- **MTP**: multi-token prediction, a technique that generates several tokens per step to speed up output.
- **GGUF**: the model file format llama.cpp loads.
- **eGPU**: a desktop graphics card connected to a laptop through an external enclosure.

## Unverified
- The devnull.land author's gains, token generation from 35 to 55 tokens/second and prefill from 700 to 1300 tokens per second, are his own single-machine measurement, and no primary or docs page fetched corroborates them.
- The writeup's claim that forks like Strata trade model quality for speed by preferring experts loaded in VRAM over the ones the model would normally choose.
- HN commenters' throughput reports on their own hardware (MI50 pairs, 7900 XTX, Radeon 8060S, R9700 with other engines) were not corroborated by any primary or docs page.
- The claim by some HN commenters that the Vulkan backend outperforms HIP on certain AMD cards.
- That the hub-note framing "AMD now ships its own llama.cpp fork" is literally accurate; every primary page fetched complicates or contradicts it.
- Any throughput delta between llama-cpp-rdna-boosts and stock llama.cpp on our own hardware; nothing was measured first-party this session.

## Suggested outline
1. Hook: your Radeon can get a real llama.cpp speedup tonight, and the twist is who made it: not AMD, whose own fork is retired, but one guy's 19-patch set that just pulled 367 points on Hacker News.
2. Sort the three things the headline blurs: stock llama.cpp already runs AMD via HIP and Vulkan with AMD's own pre-built Windows binaries; AMD's GitHub fork is retired; the trending rdna-boosts patch set is a community speed layer pinned to one upstream commit for RDNA3/3.5/4 cards.
3. Land the honest number and the catch: one R9700 owner reports token generation going from 35 to 55 tokens/second on his own machine, YMMV; the patch set is default-on but unofficial, AMD's own speed push (HRX) is still an upstream proposal, and llama.cpp maintainers say they are happy to take high-quality patches.

## Viewer situation
You have a gaming PC with an AMD Radeon card (something in the RX 6000 through RX 9070 range), you run a local model or want to tonight, and you have watched NVIDIA owners get the easy path.

## Has process
true
- Install ROCm, then clone stock llama.cpp and build it with -DGGML_HIP=ON and -DGPU_TARGETS set to your card (upstream build docs use gfx1030 as the example).
- Download AMD's pre-built Windows llama.cpp binaries (rocm-rel-7.2.1, gfx110X/gfx115X/gfx120X) and extract the zip if you would rather not compile.
- Download a GGUF model file (AMD's walkthrough uses gpt-oss-20b-mxfp4.gguf).
- Run llama-server with your model and -ngl 99 to offload all layers to the GPU (AMD's example: .\llama-server.exe -m test_model.gguf -c 2048 -ngl 99 -fa on --port 8080).
- Clone upstream llama.cpp, check out commit 919794500, and run bash <path-to-repo>/scripts/apply-all.sh . from the rdna-boosts repo to apply the 19 patches before building.

## Objection
A single-maintainer patch set with a one-machine benchmark is not a foundation for your inference stack; stock llama.cpp plus AMD's own validated binaries is the supported path, and speed claims should wait for upstream acceptance or your own measurement.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://devnull.land/amd-specific-llama-cpp | AMD-specific fork of llama.cpp (devnull.land) | community | web_extract | 2026-11-27 |
| 2 | https://news.ycombinator.com/item?id=50657265 | AMD-specific fork of llama.cpp \| Hacker News | community | web_extract | 2026-11-27 |
| 3 | https://github.com/stew675/llama-cpp-rdna-boosts | stew675/llama-cpp-rdna-boosts | primary | web_extract | 2026-11-27 |
| 4 | https://github.com/AMD-Ecosystem/llama.cpp | AMD-Ecosystem/llama.cpp: LLM inference in C/C++ | primary | web_extract | 2026-11-27 |
| 5 | https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md | Build llama.cpp locally (docs/build.md) | docs | web_extract | 2026-11-27 |
| 6 | https://github.com/ggml-org/llama.cpp/discussions/27219 | RFC: Adding a native AMD ggml-hrx backend · Discussion #27219 | primary | web_extract | 2026-11-27 |
| 7 | https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/advanced/advancedrad/windows/llm/llamacpp.html | Llama.cpp pre-built binaries (Use ROCm on Radeon and Ryzen) | primary | web_extract | 2026-11-27 |
| 8 | https://rocm.blogs.amd.com/ecosystems-and-partners/llama-cpp/README.html | Llama.cpp Meets Instinct: A New Era of Open-Source AI Acceleration | docs | web_extract | 2026-11-27 |

## Notes
Tool family: web_search for discovery (2 searches) and web_extract for page reads (12 fetch attempts, 8 pages returned content). Failures: 4 attempts errored (Firecrawl keyless 500s and credit-exhaustion) on the first pass; the AMD-Ecosystem repo, the AMD docs page, the rdna-boosts repo and build.md all succeeded on retry, and the 12-attempt budget was reached exactly. The ROCm/llama.cpp URL redirects to AMD-Ecosystem/llama.cpp; the final URL is recorded. The devnull writeup quotes a "379 points" figure nowhere; the live HN page read 367 points at fetch, and the radar snapshot's approximate figure was not used. Conflicts: the HN headline frames the project as an "AMD-specific fork" while AMD's retired-repo banner (primary) and the project's own README (primary) show a community patch set; the primary pages are trusted over the headline. Thin spots: no independent or first-party benchmark of llama-cpp-rdna-boosts was fetched, so the writeup's 35-to-55 tokens/second figure stays attributed and hedged, and the key-numbers table carries only primary/docs-sourced numbers plus the HN thread's own score. The original angle phrase "AMD now ships its own fork" does not survive the sources; the script should land the twist rather than the literal claim.
