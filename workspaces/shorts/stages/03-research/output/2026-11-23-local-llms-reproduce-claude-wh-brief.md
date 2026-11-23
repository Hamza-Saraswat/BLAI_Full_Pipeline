---
slug: 2026-11-23-local-llms-reproduce-claude-wh
stage: 03-research
topic: "Local LLMs reproduce Claude: what the experiments show"
depth: standard
generated_at: 2026-11-23T12:55:00Z
sources: 9
hub: "[[videos/2026-11-23-local-llms-reproduce-claude-wh]]"
---

# Research brief: Local LLMs reproduce Claude: what the experiments show

## Summary
The "local LLMs reproduce Claude" story traces to one developer's self-published experiment plus a beginner guide that both landed November 22, and the honest version of the claim is a lot smaller than the headline. The most arresting measured number: the experimenter's own big-model tier runs at 30 tps against Claude's 60-80 tokens per second -- "just under half the speed of a subscription" on hardware two generations old. The strongest concrete case is his NetLogo-to-TypeScript simulation harness, where "Sonnet, Deepseek and GLM all manage very similar outputs." What could not be verified: no blind test, win rate, or benchmark against any Claude model exists anywhere in the fetched record, and Emergent's summary adds figures (16GB to 32GB of RAM feasibility, response times within 2-3x of cloud APIs) the primary never states. One real conflict: the secondary write-up says local "can match or exceed cloud alternatives in specific domains" while the primary caps it at "almost" tying Claude Sonnet 5.5.

## Thesis
What actually got reproduced at home is last year's Claude, at half the speed, on workloads the experimenter rehearsed -- not today's Claude, and not drop-in.

## Explanation path
Start with the words "reproduce Claude" and ask what they would have to mean: identical quality on any task, proven blind, or something weaker. Then bring in the actual experiment: one developer, a two-generation-old PC with a secondhand graphics card, and a table of speeds -- his comparison method is one hard build task where local models land outputs similar to Sonnet's, not a blind test. With the bar defined, show the measured gaps: speed (30 tps versus 60-80 tokens per second), reach (a fast small model that loses a hidden fact past 32k tokens), and consistency (a leaderboard-strong model that no-ops on the real job while a plainer one does it first try). Only then explain the two ideas that make home AI work at all -- quantization shrinking a 56GB model into a file a gaming card can hold, and mixture-of-experts running a huge model at small-model speed -- because those are why the story is partly true. Land the reframe: the beginner door is a graphics card many viewers already own, the small-model tier is genuinely fast, privacy is real, and even the man who ran the experiment keeps a subscription -- so "Claude at home" is a trade, not a replacement.

## Claims
1. **On November 22, 2026 a vendor news item spread the "local reproduces Claude" story, claiming experiments by "developer Yudhanjaya" demonstrate "Claude-level AI performance using locally deployed language models" -- a 2-minute summary of a guide published the same day.**
   - Source: Local LLM Experiments Reproduce Claude Performance at Home, https://emergent.sh/news/local-llm-experiments-reproduce-claude
   - Tier: docs | Confidence: medium | Accessed: 2026-11-23 | Via: web_extract
   - Quote: "A comprehensive technical guide published today demonstrates how developers can achieve Claude-level AI performance using locally deployed language models. The experiments, documented by developer Yudhanjaya, provide detailed benchmarks and implementation strategies for running production-quality AI without cloud dependencies."
2. **The underlying experiment is "Honey, We Have Claude at Home" by developer Yudhanjaya Wijeratne, run on "Leviathan", a Ryzen 5800 X3D PC with 64 GB of DDR4-3200 RAM, a secondhand RTX 3080 plus a 4080, both power-limited to 220 W.**
   - Source: Honey, We Have Claude at Home, https://yudhanjaya.com/docs/experiments/local-llms-experiments/
   - Tier: primary | Confidence: high | Accessed: 2026-11-23 | Via: web_extract
   - Quote: "my RAM is DDR4, at 3200 Mhz. My 3080 (bought secondhand) is on the x4 slot ... My GPUs are power-limited to 220w"
3. **"Reproduce" in the experiment means one author-built workload, not a blind test or benchmark parity: a harness that converts a NetLogo economic simulation to TypeScript, checks for 1:1 parity, pulls OpenStreetMap data and builds an interactive HTML simulation -- and on that task the local models land near Claude.**
   - Source: Honey, We Have Claude at Home, https://yudhanjaya.com/docs/experiments/local-llms-experiments/
   - Tier: primary | Confidence: high | Accessed: 2026-11-23 | Via: web_extract
   - Quote: "This is a fairly challenging task, and Sonnet, Deepseek and GLM all manage very similar outputs."
4. **The experimenter's own ceiling: the big local models are "slightly better than Claude Opus 4.5 (November 24, 2025)", the two best "almost tie with Claude Sonnet 5.5, but the keyword is almost", and he explicitly disclaims a drop-in replacement for Claude Opus 5.5.**
   - Source: Honey, We Have Claude at Home, https://yudhanjaya.com/docs/experiments/local-llms-experiments/
   - Tier: primary | Confidence: high | Accessed: 2026-11-23 | Via: web_extract
   - Quote: "I dare say that the two most popular models on this list Deepseek 4.1 and GLM 5.3 Flash - almost tie with Claude Sonnet 5.5, but the keyword is almost."
5. **Speed is the measured gap: Claude's desktop app doles out tokens at 60-80 tokens per second, his big-model local tier reaches 30 tps ("just under half the speed of a subscription"), while the fast small tier hits 141.9 tok/s decode on a quantized 125B/6B model.**
   - Source: Honey, We Have Claude at Home, https://yudhanjaya.com/docs/experiments/local-llms-experiments/
   - Tier: primary | Confidence: high | Accessed: 2026-11-23 | Via: web_extract
   - Quote: "Claude, via the desktop app, usually doles out its tokens at somewhere between 60-80 tokens per second ... On my hardware, I'm happy to get 30 tps."
6. **The entry door is real: his Goldilocks setup (Qwen 3.8 Flash-Next via the Strata engine) runs on a 12 GB RTX 3060 with as little as 16 GB of VRAM if you have an NVMe drive.**
   - Source: Honey, We Have Claude at Home, https://yudhanjaya.com/docs/experiments/local-llms-experiments/
   - Tier: primary | Confidence: high | Accessed: 2026-11-23 | Via: web_extract
   - Quote: "Qwen 3.8 Flash-Next can be run on as a 12 GB 3060 with as little as 16 gigs of VRAM if you have an NVME drive."
7. **The person who ran the experiment still pays for the cloud: he writes it "often makes more sense to have a $10 subscription" giving access to these same big models than to serve them at home, because they demand his entire system's resources.**
   - Source: Honey, We Have Claude at Home, https://yudhanjaya.com/docs/experiments/local-llms-experiments/
   - Tier: primary | Confidence: high | Accessed: 2026-11-23 | Via: web_extract
   - Quote: "it often makes more sense to have a $10 subscription that gives me access to these models and to let them shepherd smaller models to do complex tasks."
8. **Long-context recall is where fast small local models break: LFM3-Omni-2B found a hidden needle at 11,000 tokens and at 32k, "but at 88k, it simply couldn't", and in his testing "has not been good past the 32k context window".**
   - Source: Honey, We Have Claude at Home, https://yudhanjaya.com/docs/experiments/local-llms-experiments/
   - Tier: primary | Confidence: high | Accessed: 2026-11-23 | Via: web_extract
   - Quote: "LFM was able to find the needle at 11,000 tokens. It was able to find the needle at 32k, but at 88k, it simply couldn't."
9. **The new small open model at the center of the beginner wave, Thinking Machines Lab's Inkling 2 Mini, is 26.4B total parameters with 5.4B effective active parameters per token (8 of 128 experts, looped layers), a 1M-token context, released November 20, 2026 under Apache 2.0 -- and its first-party evals compare it to same-size open peers, never to Claude.**
   - Source: Inkling 2 Mini model card, https://huggingface.co/thinkingmachines/Inkling-2-Mini
   - Tier: primary | Confidence: high | Accessed: 2026-11-23 | Via: web_extract
   - Quote: "In each layer, each token is routed to 8 of 128 experts ... there are 5.4B effective active parameters per token."
10. **An independent engineer's local Claude Code replacement experiment found benchmark rank does not predict harness behavior: Ornith-1.0-35B exited cleanly having done nothing while Qwen3.6-35B-A3B worked on the identical first try.**
    - Source: Can Local LLMs replace Claude Code? Personal Experience and Fine Tuning., https://softwarearchitectureweekly.substack.com/p/can-local-llms-replace-claude-code
    - Tier: benchmark | Confidence: medium | Accessed: 2026-11-23 | Via: web_extract
    - Quote: "Benchmark leaderboards, it turns out, tell you almost nothing about whether a model will actually follow a long, detailed operating manual."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Claude desktop app speed (subscription baseline) | 60-80 tokens per second | https://yudhanjaya.com/docs/experiments/local-llms-experiments/ | "usually doles out its tokens at somewhere between 60-80 tokens per second" |
| 2 | big-model local tier on the experimenter's hardware | 30 tps | https://yudhanjaya.com/docs/experiments/local-llms-experiments/ | "I'm happy to get 30 tps. This is just under half the speed of a subscription" |
| 3 | fast small-tier decode (Swift 1.5 IQ2_XS, 125B/6B, RTX 4080) | 141.9 tok/s | https://yudhanjaya.com/docs/experiments/local-llms-experiments/ | table: "Swift 1.5 ... IQ2_XS ... 141.9" |
| 4 | NVIDIA RTX 5090 starting price (32 GB GDDR7) | $1999 | https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/ | "equipped with 32 GB of super-fast GDDR7 memory ... Starting at $1999" |
| 5 | Claude Pro subscription, annual billing | $17 per month ($20 if billed monthly) | https://www.anthropic.com/pricing | "Per month with annual subscription discount ($200 billed up front). $20 if billed monthly." |
| 6 | recommended 4-bit Inkling 2 Mini file (UD-Q4_K_XL) | 17.6 GB | https://unsloth.ai/docs/models/inkling-2-mini | "The recommended quant is UD-Q4_K_XL (17.6 GB)." |
| 7 | entry card for the Goldilocks local setup | 12 GB 3060 with 16 GB VRAM | https://yudhanjaya.com/docs/experiments/local-llms-experiments/ | "can be run on as a 12 GB 3060 with as little as 16 gigs of VRAM if you have an NVME drive" |
| 8 | needle-in-haystack reach of LFM3-Omni-2B | found at 11,000 tokens and 32k; lost at 88k | https://yudhanjaya.com/docs/experiments/local-llms-experiments/ | "It was able to find the needle at 32k, but at 88k, it simply couldn't." |

## Analogy candidates
- **Cover band**: a local model is a cover band that has rehearsed your setlist -- on the tasks you repeat every week it is hard to tell from the original recording. Breaks when: the audience shouts a request it never learned (a novel long-context agent task), or the venue doubles in size (context past what the model can hold), or you need the original's release-day speed.
- **Folding laundry for a smaller suitcase**: quantization packs the same clothes into a bag that actually fits under your seat, which is the experimenter's own image. Breaks when: the fold lines show -- some fabrics (workloads) wrinkle badly at 2-3 bits while others come out unchanged, and no fold adds clothes you did not pack.

## Misconceptions
- Myth: the November 2026 experiments proved local models now equal Claude. Reality: the experimenter's own words cap it at "almost" tying Claude Sonnet 5.5 and beating only 2025's Claude Opus 4.5, at half the speed, with no blind test run (claim 4).
- Myth: buy the graphics card once and your home AI replaces the subscription. Reality: the experimenter himself keeps a $10 subscription because it "often makes more sense", since the big local models demand his entire system's resources while running (claim 7).

## Glossary
- **local LLM**: an AI model stored as a file on your own machine and run on your own graphics card, instead of rented from a company's servers.
- **quantization**: storing the model's numbers with fewer bits so it fits in less memory, trading a little accuracy for size and speed.
- **VRAM**: the memory on your graphics card; the model plus its working memory has to fit there to run fast.
- **tokens per second (tps / tok/s)**: how fast the model writes its answer -- the at-home version of how snappy a chat app feels.
- **open weights**: the model's learned numbers are published as a downloadable file anyone can run, like an open-source program.
- **mixture of experts (MoE)**: a model that keeps many specialist sub-networks on disk but activates only a few per token, so a huge model runs at small-model speed.
- **context window**: how much of the conversation and documents the model can keep in mind at once, measured in tokens.
- **KV cache**: the model's working memory for the current conversation; it grows with context and competes with the model for VRAM.
- **inference engine**: the program that loads the model file and runs it on your hardware, such as llama.cpp, Strata or Unsloth Desktop.
- **GGUF**: the single-file format quantized models ship in -- the thing you actually download.
- **prefill**: the work of reading your input before writing; slow prefill means a long wait after pasting a big document.
- **harness**: the software wrapped around a model that gives it tools and instructions; which harness you use can matter more than which model.

## Unverified
- Emergent's summary claims local deployment is feasible "on systems with 16GB to 32GB of RAM" and that response times are "within 2-3x of cloud APIs for most queries"; neither figure appears in the primary write-up, so treat both as the summarizer's, not the experimenter's.
- The claim that operating costs after hardware are "essentially zero" ignores electricity; the experimenter's near-zero energy cost comes from offgrid solar panels most viewers do not have.
- Hacker News sentiment calls this "the plasma TV phase of local AI" needing "~5 years" to mature and says 48 GB Macs are "barely enough" -- community opinion, usable as vibe, not as fact.
- One HN commenter reports Inkling 2 on an M5 Max finding codebase issues "Claude didn't find in previous audits" and being faster than Claude; a single anonymous anecdote with no methodology.
- No blind test, win rate, Elo score, or head-to-head benchmark against any Claude model exists in any fetched source; if the script needs one, it does not exist in this record.

## Suggested outline
1. Open on the weekend's headline -- "local LLMs reproduce Claude" -- and immediately show the experimenter's own hedge ("almost tie ... the keyword is almost"), promising the receipts.
2. Walk the experiment: the aging PC, the one hard simulation task where local outputs land near Sonnet's, then the measured gaps -- 30 tps versus 60-80 tokens per second, the needle lost at 88k, the leaderboard model that no-opped -- with quantization and mixture-of-experts explained as the reason any of this works at all.
3. Land the reframe and the door: last year's Claude at home for free-ish versus today's Claude by subscription is a trade, not a replacement; the starter door is a 12 GB 3060 many viewers already own, the small tier is genuinely fast, and the man with the receipts still pays $10 a month.

## Viewer situation
You have a gaming PC or a Mac with a decent graphics card, you pay for Claude every month, and you keep seeing posts saying you could just run the thing at home for free.

## Has process
false

## Objection
One developer judging his own rig on his own workload is not evidence of parity -- where is the blind test or a single head-to-head benchmark against Claude?

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://yudhanjaya.com/docs/experiments/local-llms-experiments/ | Honey, We Have Claude at Home | primary | web_extract | 2026-11-23 |
| 2 | https://emergent.sh/news/local-llm-experiments-reproduce-claude | Local LLM Experiments Reproduce Claude Performance at Home | docs | web_extract | 2026-11-23 |
| 3 | https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth | A beginner's guide to Local AI with Inkling, Qwen, and Unsloth | docs | web_extract | 2026-11-23 |
| 4 | https://news.ycombinator.com/item?id=50603845 | A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth (HN thread) | community | web_extract | 2026-11-23 |
| 5 | https://unsloth.ai/docs/models/inkling-2-mini | Inkling 2 Mini - Run Locally Guide | docs | web_extract | 2026-11-23 |
| 6 | https://huggingface.co/thinkingmachines/Inkling-2-Mini | thinkingmachines/Inkling-2-Mini model card | primary | web_extract | 2026-11-23 |
| 7 | https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/ | GeForce RTX 5090 | primary | web_extract | 2026-11-23 |
| 8 | https://www.anthropic.com/pricing | Plans & pricing - Claude by Anthropic | primary | web_extract | 2026-11-23 |
| 9 | https://softwarearchitectureweekly.substack.com/p/can-local-llms-replace-claude-code | Can Local LLMs replace Claude Code? Personal Experience and Fine Tuning. | benchmark | web_extract | 2026-11-23 |

## Notes
Conflicts: (a) Emergent says local models "can match or exceed cloud alternatives in specific domains" and calls local "a production-ready alternative"; the primary says "almost" tying Claude Sonnet 5.5 and no drop-in Opus 5.5 replacement -- trust the primary, it is the experimenter's own page, and the gap is the video's spine. (b) The gpupartner guide dates Inkling 2 Mini's release to November 17, 2026 while the Thinking Machines model card says November 20, 2026; trust the model card. (c) The HN thread's score moved between fetches (544 points live, 566 via HN's API, 556 in stage 02's note) because it was still voting; cite it as approximate and moving. The Software Architecture Weekly post is paywalled past its midpoint; only first-half facts are used, hence medium confidence.
