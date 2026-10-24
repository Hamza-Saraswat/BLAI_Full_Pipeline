---
slug: 2026-10-24-256-tops-beats-1000-tops-readi
stage: 03-research
topic: "256 TOPS beats 1000 TOPS? Reading the box that claims to beat DGX Spark"
depth: standard
generated_at: 2026-10-24T12:30:00Z
sources: 10
hub: "[[videos/2026-10-24-256-tops-beats-1000-tops-readi]]"
---

# Research brief: 256 TOPS beats 1000 TOPS? Reading the box that claims to beat DGX Spark

## Summary
The claim is real and quotable: Sipeed's MaixStation, a 40 W box built on Axera's AX8860P, says its 256 TOPS beats the DGX Spark's 1,000-class TOPS on Qwen 27B prefill, and the reason it can even be argued is that NVIDIA's bigger number is sparse FP4 theory footnoted on nvidia.com itself. The most arresting number is the tie nobody advertises: both machines have exactly 273 GB/s of memory bandwidth, so the part of inference you feel while chatting is capped on both. The strongest concrete case is llama.cpp's independent DGX Spark run on qwen3moe 30B.A3B Q8_0: 2986.97 ± 18.87 t/s prefill against 61.06 ± 0.23 t/s decode, prefill and decode living two orders of magnitude apart. What could not be verified: the bar values on Sipeed's benchmark chart (it is an image), any independent test of the MaixStation hardware, and the exact tok/s margins. Conflict to flag: the 25% faster prefill and 30% faster decode in Sipeed's tweet versus TechRadar and CNX both reading the published chart as only slightly ahead.

## Thesis
A 256-TOPS box can honestly chart ahead of a 1,000-TOPS box because the 1,000 is a sparse paper figure and the race was run on prefill, while the speed you feel in chat, decode, is capped by a 273 GB/s memory ceiling both machines share.

## Explanation path
Open on the two labels: a DGX Spark advertising Up to 1 PFLOP FP4 at $6,949.99, and a 40 W Sipeed MaixStation claiming its 256 TOPS beats it on Qwen. Before any benchmark appears, establish what a TOPS figure is: the peak matrix-multiply rate a chip could sustain in one ideal second, and NVIDIA's own footnote concedes the bigger number is theoretical FP4 using the sparsity feature, a 2:4 trick where at least two of every four values are zero. Then split inference into its two jobs: prefill, which digests your whole prompt in one compute-heavy pass, and decode, which emits tokens one at a time and is bounded by memory bandwidth rather than math. That sets up the punchline that both boxes sit on exactly 273 GB/s, so their decode ceilings are similar no matter whose TOPS is bigger, which Sipeed's own page admits with the rule tok/s is effective bandwidth divided by model size. With that machinery in place, read the claim the way an engineer would: vendor-measured, Qwen 27B at FP4, speculative decoding disabled on both sides, 25% faster prefill and 30% faster decode in the tweet, but a published chart that TechRadar and CNX both read as only slightly ahead, and no independent test of the hardware yet. Anchor the scale with llama.cpp's own DGX Spark numbers on a Qwen model, where prompt processing runs at thousands of tokens per second while generation runs at dozens. Land the rule the viewer keeps: judge a local-AI box by tokens per second on the model and quant you actually run, never by TOPS on the tin.

## Claims
1. **Sipeed's MaixStation is built on Axera's AX8860P, a SoC with a 16x Arm Cortex-A55 CPU, up to 128GB of 256-bit LPDDR5x memory delivering 273GB/s bandwidth, and power consumption of About 40 Watts under load.**
   - Source: Axera AX8860P 16-core Cortex-A55 SoC takes on NVIDIA DGX Spark at fraction of the cost, https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/
   - Tier: docs | Confidence: high | Accessed: 2026-10-24 | Via: web_extract
   - Quote: "AI – Up to 256 TOPS ... Memory – Up to 128GB 256-bit LPDDR5x with 273GB/s bandwidth ... Power Consumption – About 40 Watts under load"
2. **The AX8860P's compute figure is up to 256 TOPS and it is a dense number: the 256 TOPS figure is derived from pure FP4 without any sparsity involved.**
   - Source: Axera Claims AX8860 AI Chip Can Beat the DGX Spark in AI LLMs by 25% (Wccftech), https://wccftech.com/axera-ax8860-ai-chip-beat-dgx-spark-ai-llms-128-gb-memory-40w-less-cost/
   - Tier: docs | Confidence: high | Accessed: 2026-10-24 | Via: web_extract
   - Quote: "The 256 TOPS figure is derived from pure FP4 without any sparsity involved."
3. **NVIDIA's DGX Spark product page lists tensor performance of Up to 1 PFLOP FP4, footnoted as Theoretical FP4 TOPS using the sparsity feature, alongside Memory Bandwidth of 273 GB/s and a GB10 TDP of 140 W.**
   - Source: Personal AI Supercomputer Powered by Blackwell (NVIDIA DGX Spark product page), https://www.nvidia.com/en-us/products/workstations/dgx-spark/
   - Tier: primary | Confidence: high | Accessed: 2026-10-24 | Via: web_extract
   - Quote: "| Tensor Performance1 | Up to 1 PFLOP FP4 | ... | Memory Bandwidth | 273 GB/s | ... 1 Theoretical FP4 TOPS using the sparsity feature."
4. **NVIDIA's own user guide states the same figure as Up to 1,000 TOPS (trillion operations per second) inference and up to 1 PFLOP (petaFLOP) at FP4 precision with sparsity.**
   - Source: Hardware Overview, DGX Spark User Guide, https://docs.nvidia.com/dgx/dgx-spark/hardware.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-24 | Via: web_extract
   - Quote: "AI Compute: Up to 1,000 TOPS (trillion operations per second) inference and up to 1 PFLOP (petaFLOP) at FP4 precision with sparsity"
5. **Sparse TOPS come from 2:4 structured sparsity: among each group of four contiguous values, at least two must be zero, which is a 50% sparsity rate, letting sparse Tensor Cores skip the zeroed work.**
   - Source: Structured Sparsity in the NVIDIA Ampere Architecture and Applications in Search Engines (NVIDIA Technical Blog), https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/
   - Tier: docs | Confidence: high | Accessed: 2026-10-24 | Via: web_extract
   - Quote: "Among each group of four contiguous values, at least two must be zero, which is a 50% sparsity rate."
6. **The performance claim as reported: Sipeed tested Qwen 27B at 25% faster prefill and 30% faster decode speeds than the NVIDIA DGX Spark.**
   - Source: Axera Claims AX8860 AI Chip Can Beat the DGX Spark in AI LLMs by 25% (Wccftech), https://wccftech.com/axera-ax8860-ai-chip-beat-dgx-spark-ai-llms-128-gb-memory-40w-less-cost/
   - Tier: docs | Confidence: high | Accessed: 2026-10-24 | Via: web_extract
   - Quote: "They claim to have tested Qwen 27B at 25% faster prefill and 30% faster decode speeds than the NVIDIA DGX Spark."
7. **Reading Sipeed's published chart, TechRadar reports the 128GB configuration slightly exceeds the DGX Spark's performance, that the comparison ran with speculative decoding through multi-token prediction disabled, and that the reported advantage remains relatively small pending independent testing.**
   - Source: 'Dense beats sparse': Sipeed and Axera challenge Nvidia DGX Spark with 128GB MaixStation AI computer (TechRadar), https://www.techradar.com/pro/plucky-chinese-startup-claims-to-beat-nvidia-dgx-spark-mac-mini-on-qwen-says-its-256-tops-beats-1000-tops-in-prefill-running-16-core-cortex-a55-soc-on-40w
   - Tier: docs | Confidence: high | Accessed: 2026-10-24 | Via: curl + raw-HTML extraction
   - Quote: "Sipeed's published Qwen results indicate that its 128GB configuration slightly exceeds the DGX Spark's performance ... The comparisons were conducted with speculative decoding through multi-token prediction disabled ... the reported advantage remains relatively small, and independent testing would be necessary"
8. **On price, the 128GB MaixStation should remain under $4,000 while Nvidia's DGX Spark reportedly sells for $6,949.99, up from its original $3,000 to $4,000 pricing announced during March 2025.**
   - Source: 'Dense beats sparse': Sipeed and Axera challenge Nvidia DGX Spark with 128GB MaixStation AI computer (TechRadar), https://www.techradar.com/pro/plucky-chinese-startup-claims-to-beat-nvidia-dgx-spark-mac-mini-on-qwen-says-its-256-tops-beats-1000-tops-in-prefill-running-16-core-cortex-a55-soc-on-40w
   - Tier: docs | Confidence: high | Accessed: 2026-10-24 | Via: curl + raw-HTML extraction
   - Quote: "the 128GB configuration should remain under $4,000. By comparison, Nvidia's DGX Spark reportedly sells for $6,949.99, considerably above its original $3,000 to $4,000 pricing announced during March 2025."
9. **Independent llama.cpp measurements put the DGX Spark at pp2048 of 2986.97 ± 18.87 tokens per second and tg32 of 61.06 ± 0.23 tokens per second running qwen3moe 30B.A3B Q8_0, showing prefill and decode living on different scales.**
   - Source: llama.cpp benches/dgx-spark/dgx-spark.md (ggml-org, updated 2026-02-05), https://github.com/ggml-org/llama.cpp/blob/master/benches/dgx-spark/dgx-spark.md
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-24 | Via: web_extract
   - Quote: "| qwen3moe 30B.A3B Q8_0 | ... | pp2048 | 2986.97 ± 18.87 |" and "| qwen3moe 30B.A3B Q8_0 | ... | tg32 | 61.06 ± 0.23 |"
10. **Sipeed's own page explains the decode ceiling under the question Same 273 GB/s. Why is decode faster?, answering that bandwidth sets the ceiling and publishing the rule tok/s ≈ effective bandwidth ÷ model size.**
    - Source: MaixStation, The Best Local AI at Every Scale (Sipeed product page), https://sipeed.com/maixstation/index.html
    - Tier: primary | Confidence: high | Accessed: 2026-10-24 | Via: web_extract
    - Quote: "Bandwidth sets the ceiling. Architecture decides how close you get. Every token reads the whole model once, and MaixStation keeps more of those 273 GB/s busy." and "tok/s ≈ effective bandwidth ÷ model size"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | DGX Spark advertised AI performance (the 1,000-class figure, sparse) | Up to 1 PFLOP FP4 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | "Tensor Performance1: Up to 1 PFLOP FP4 ... 1 Theoretical FP4 TOPS using the sparsity feature." |
| 2 | MaixStation AX8860P NPU, dense FP4 (the hook: 256 against 1,000) | 256 TOPS | https://sipeed.com/maixstation/index.html | "AX8860P · 256 TOPS FP4" |
| 3 | DGX Spark dense FP4 compute, as Sipeed frames NVIDIA's number | 500 TOPS | https://www.techradar.com/pro/plucky-chinese-startup-claims-to-beat-nvidia-dgx-spark-mac-mini-on-qwen-says-its-256-tops-beats-1000-tops-in-prefill-running-16-core-cortex-a55-soc-on-40w | "Although Nvidia's dense FP4 performance approaches 500 TOPS theoretically, Sipeed maintains that its architecture uses available processing resources more efficiently during prefill." |
| 4 | Memory bandwidth, identical on both machines | 273 GB/s | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | "Memory Bandwidth: 273 GB/s" |
| 5 | MaixStation power draw | About 40 Watts | https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/ | "Power Consumption – About 40 Watts under load" |
| 6 | DGX Spark price, October 2026 (reportedly) | $6,949.99 | https://www.techradar.com/pro/plucky-chinese-startup-claims-to-beat-nvidia-dgx-spark-mac-mini-on-qwen-says-its-256-tops-beats-1000-tops-in-prefill-running-16-core-cortex-a55-soc-on-40w | "Nvidia's DGX Spark reportedly sells for $6,949.99" |
| 7 | DGX Spark prefill, qwen3moe 30B.A3B Q8_0, llama.cpp pp2048 | 2986.97 ± 18.87 t/s | https://github.com/ggml-org/llama.cpp/blob/master/benches/dgx-spark/dgx-spark.md | "pp2048: 2986.97 ± 18.87" |
| 8 | DGX Spark decode, same model, llama.cpp tg32 | 61.06 ± 0.23 t/s | https://github.com/ggml-org/llama.cpp/blob/master/benches/dgx-spark/dgx-spark.md | "tg32: 61.06 ± 0.23" |

## Analogy candidates
- **Engine horsepower against the speed limit**: TOPS is peak horsepower measured on a bench at ideal RPM; memory bandwidth is the road, and decode is city driving where anything past the limit buys you nothing, so a 1,000-horsepower rig and a 256-horsepower box both cruise at the same 273 GB/s ceiling. Breaks when: horsepower genuinely wins the drag race: at batch prefill the compute-heavy job, big TOPS do pull ahead, so the number is not useless, just not the one that sets your chat speed.
- **Speed-reading a document versus reciting it back**: prefill is speed-reading the whole prompt in one pass, which rewards raw compute; decode is reciting the answer one word at a time, and each new word forces a fresh walk past every shelf of the library, which is bandwidth. Breaks when: a human does not literally re-read the entire book before saying each next word; a language model does re-read its weights for every token, which is why decode tracks the memory number.

## Misconceptions
- Myth: TOPS on the box equals AI speed. Reality: TOPS is peak matrix-multiply theory; NVIDIA's own spec footnote says it is theoretical FP4 using the sparsity feature, where half of every group of four values is zero (claims 3, 4 and 5).
- Myth: More TOPS always wins. Reality: Decode, the part you feel while reading a reply, is capped by memory bandwidth, and both boxes have exactly 273 GB/s; Sipeed itself publishes tok/s ≈ effective bandwidth ÷ model size (claims 1 and 10).
- Myth: Prefill is the whole story. Reality: The headline claim is a prefill chart with speculative decoding off; on the Spark a Qwen-class model prefills at 2986.97 t/s but generates at 61.06 t/s, two different jobs with two different bottlenecks (claims 6 and 9).

## Glossary
- **TOPS**: Trillions of operations per second, the peak number of matrix-multiply operations a chip could do in one ideal second, not the speed it runs a model at.
- **Sparsity (2:4 structured)**: A hardware trick where at least two of every four contiguous weight values are zero, letting the chip skip half the math and advertise up to double the TOPS.
- **Dense vs sparse compute**: Dense counts every multiplication with no zeros skipped, the honest floor; sparse counts the accelerated rate only a specially pruned model can touch.
- **FP4**: A 4-bit number format for model weights that shrinks the model and doubles math throughput at some accuracy cost.
- **NPU**: A neural processing unit, a chip block built only for the matrix math neural networks need, like the AX8860P's accelerator.
- **Prefill**: The first half of answering, where the model digests your entire prompt in one compute-heavy pass.
- **Decode (token generation)**: The second half, where the model emits tokens one at a time, each one requiring a pass over the weights, so its speed tracks memory bandwidth.
- **Memory bandwidth**: How many bytes per second the chip can pull from memory, the hard ceiling on decode speed for a model that fits in RAM.
- **MTP (speculative decoding)**: A technique where a small draft model guesses several tokens and the big model verifies them in one pass, boosting decode speed beyond the baseline; Sipeed switched it off on both machines for a fair chart.
- **tok/s (tokens per second)**: Tokens per second, the number that actually tells you how fast a model runs on a given box and quantization.

## Unverified
- The exact tokens-per-second values on Sipeed's benchmark chart, because the chart is an image and neither CNX nor TechRadar printed the bar values.
- That the MaixStation ships at its target price and performance, since the Kickstarter is still months out and no independent reviewer has touched the hardware.
- A claim seen only in a search snippet that a separate report put the prefill edge at about 23% instead of 25%; the underlying page was not fetched.
- Community reaction beyond Sipeed's own tweet, including Reddit and Hacker News threads that were not fetched this session.
- What the MaixStation's decode and prefill numbers look like with MTP switched on, which Sipeed says lifts both sides similarly but shows no chart for.

## Suggested outline
1. Hook on the box and its boast: a 40 W machine targeting under $4,000 says its 256 TOPS beats the $6,949.99 DGX Spark's 1,000 TOPS on Qwen, and the fine print of what was measured is the whole video.
2. Teach the label: TOPS is peak sparse math, NVIDIA's own footnote says theoretical, dense is around 500 against the NPU's dense 256, and inference splits into compute-bound prefill and bandwidth-bound decode where both boxes sit on the same 273 GB/s.
3. Land the reframe: the vendor chart with MTP off reads only slightly ahead against the 25% tweet, llama.cpp's independent Spark numbers show prefill in the thousands and decode in the dozens, so compare boxes by tok/s on your model, never by TOPS on the tin.

## Viewer situation
You are comparing local-AI boxes by the TOPS printed on the label and assuming the 1,000-TOPS machine is roughly four times faster than the 256-TOPS one in the headline.

## Has process
false

## Objection
This is one vendor's own benchmark with speculative decoding switched off on a single Qwen model, and the chart Sipeed itself published shows only a slight edge, so nothing independent supports the win yet.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.techradar.com/pro/plucky-chinese-startup-claims-to-beat-nvidia-dgx-spark-mac-mini-on-qwen-says-its-256-tops-beats-1000-tops-in-prefill-running-16-core-cortex-a55-soc-on-40w | 'Dense beats sparse': Sipeed and Axera challenge Nvidia DGX Spark with 128GB MaixStation AI computer (TechRadar) | docs | curl + web_extract | 2026-10-24 |
| 2 | https://wccftech.com/axera-ax8860-ai-chip-beat-dgx-spark-ai-llms-128-gb-memory-40w-less-cost/ | Axera Claims AX8860 AI Chip Can Beat the DGX Spark in AI LLMs by 25% (Wccftech) | docs | web_extract | 2026-10-24 |
| 3 | https://www.cnx-software.com/2026/10/19/axera-ax8860p-16-core-cortex-a55-soc-takes-on-nvidia-dgx-spark-at-fraction-of-the-cost/ | Axera AX8860P 16-core Cortex-A55 SoC takes on NVIDIA DGX Spark at fraction of the cost (CNX Software) | docs | web_extract | 2026-10-24 |
| 4 | https://sipeed.com/maixstation/index.html | MaixStation · The Best Local AI at Every Scale (Sipeed product page) | primary | web_extract | 2026-10-24 |
| 5 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | Personal AI Supercomputer Powered by Blackwell (NVIDIA DGX Spark product page) | primary | web_extract | 2026-10-24 |
| 6 | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | Hardware Overview, DGX Spark User Guide (docs.nvidia.com) | primary | web_extract | 2026-10-24 |
| 7 | https://github.com/ggml-org/llama.cpp/blob/master/benches/dgx-spark/dgx-spark.md | llama.cpp benches/dgx-spark/dgx-spark.md (ggml-org, updated 2026-02-05) | benchmark | web_extract | 2026-10-24 |
| 8 | https://www.hardware-corner.net/first-dgx-spark-llm-benchmarks/ | First Nvidia DGX Spark LLM Benchmarks Are In: Does It Beat Strix Halo (Hardware Corner) | benchmark | web_extract | 2026-10-24 |
| 9 | https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/ | Structured Sparsity in the NVIDIA Ampere Architecture and Applications in Search Engines (NVIDIA Technical Blog) | docs | web_extract | 2026-10-24 |
| 10 | https://github.com/ggml-org/llama.cpp/discussions/16578 | Performance of llama.cpp on NVIDIA DGX Spark · Discussion #16578 (ggml-org) | benchmark | web_extract | 2026-10-24 |

## Notes
Tool family: FireCrawl was out of credits (HTTP 402 on both search calls), so discovery ran on web_search and every cited page was fetched with web_extract; TechRadar resisted plain extraction and its body was recovered from the raw HTML via curl. 6 searches, 10 fetches, all cached under output/fetch-cache. Conflicts: Sipeed's tweet and Wccftech say 25% faster prefill and 30% faster decode, while TechRadar and CNX, both looking at Sipeed's published chart, call it slightly exceeds and only slightly faster; the brief reports both and never asserts the vendor's margin as fact. One Wccftech comparison table gives DGX Spark 128 GB pricing as roughly $4,700 to $6,950-plus while CNX and TechRadar both state $6,949.99, which the brief uses as the October 2026 figure. Tom's Hardware coverage of the same announcement never rendered a body through extraction and is not cited.
