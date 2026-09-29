---
slug: 2026-09-29-the-dgx-spark-handbook-every-s
stage: 03-research
topic: "The DGX Spark Handbook by ExoLabs: what it settles, what it misses, and the second-Spark math"
depth: standard
generated_at: 2026-09-29T11:41:32Z
sources: 13
hub: "[[videos/2026-09-29-the-dgx-spark-handbook-every-s]]"
---

# Research brief: The DGX Spark Handbook by ExoLabs: what it settles, what it misses, and the second-Spark math

## Summary
ExoLabs published a DGX Spark Handbook on September 25 that collapses months of forum answers into one link, and its most arresting number is pricing: the $3,999 launch Spark is gone, with NVIDIA's own marketplace asking $7,999 on 21 September and the cheapest unit the author could find at about $5,000. The strongest concrete case for caution before clustering is Dataiku's teardown, where a ConnectX-7 firmware bug throttled a fresh two-Spark link to 26.6 Gbps until a full system upgrade restored 196 Gbps in one reported case. What could not be verified: the replies inside the NVIDIA forum thread that is driving the second-Spark question never rendered in the fetch, and every speed number in the handbook is the author's own single-user measurement with no standardized benchmark behind it. Sources conflict twice: NVIDIA's user guide caps a dual-Spark setup at 405B parameters while the product page markets up to 700B across four systems, and August's $4,699 MSRP predates September's $5,000 to $7,999 street reality.

## Thesis
ExoLabs' DGX Spark Handbook is now the one link that settles what a Spark really costs, what to run on day one, and why a second box buys capacity rather than speed.

## Explanation path
Start where the buyer stands: the price moved under them and the setup questions repeat on every forum, and that is the gap the handbook fills, so establish what it is and who wrote it before quoting it. Then give the machine's shape, because every later answer hangs on it: the Spark is a memory box, 128 GB of unified memory behind a 273 GB/s pipe, which is why it holds enormous models and still writes tokens slowly. With that shape understood, the single-Spark answers make sense: real prices, roughly twelve dollars a month to run, a one-hour path to a first model in LM Studio, and a 200-billion-parameter ceiling from NVIDIA's own docs. The second-Spark question then lands as capacity math rather than speed math: two boxes are a two-node cluster, not one merged machine, memory is not transparently pooled, and the 200 Gb/s link is why communication-heavy work scales sub-linearly. Before the viewer acts on any of it, the honest catches: fresh clusters can ship with a firmware bug that throttles the link until a full upgrade, and the handbook's own advanced sections are directions, not results, with no standardized benchmark run. Land on the verdict the handbook itself gives: for most people the sensible stopping point is two Sparks and a cable.

## Claims
1. **The DGX Spark Handbook is a Hugging Face community article published September 25, 2026 under the exolabs organization, written by 0xSero, that walks a buyer from the first Spark to a four-Spark cluster.**
   - Source: The DGX Spark Handbook, https://huggingface.co/blog/exolabs/the-dgx-spark-handbook
   - Tier: primary | Confidence: high | Accessed: 2026-09-29 | Via: web_extract
   - Quote: "The DGX Spark Handbook ... [Community Article] ... Published September 25, 2026"
2. **The handbook settles the real-price question: the Spark "originally listed at $3,999, and that was hiked to $4,699", the cheapest unit the author found is about $5,000, used units sell for around $6,000, and NVIDIA's site was asking $7,999 on 21 September.**
   - Source: The DGX Spark Handbook, https://huggingface.co/blog/exolabs/the-dgx-spark-handbook
   - Tier: primary | Confidence: high | Accessed: 2026-09-29 | Via: web_extract
   - Quote: "The DGX Spark originally listed at $3,999, and that was hiked to $4,699 ... The cheapest one I can find is about $5,000, used ones sell for around $6,000, and on 21 September I saw NVIDIA's site asking $7,999"
3. **The handbook's day-one setup answer is LM Studio first, downloading Qwen3.6-35B, which "takes about an hour", before moving to vLLM or SGLang recipes in the preinstalled Docker stack.**
   - Source: The DGX Spark Handbook, https://huggingface.co/blog/exolabs/the-dgx-spark-handbook
   - Tier: primary | Confidence: high | Accessed: 2026-09-29 | Via: web_extract
   - Quote: "Start with LM Studio. Follow NVIDIA's step-by-step guide, download Qwen3.6-35B, and start chatting. It takes about an hour."
4. **The handbook settles the electricity question: one Spark serving a model "uses about 90-200 watts (ServeTheHome)", which at 18 cents per kWh works out to "about $12 a month if you leave it on around the clock".**
   - Source: The DGX Spark Handbook, https://huggingface.co/blog/exolabs/the-dgx-spark-handbook
   - Tier: primary | Confidence: high | Accessed: 2026-09-29 | Via: web_extract
   - Quote: "One Spark running a model uses about 90-200 watts (ServeTheHome). That's about $12 a month if you leave it on around the clock."
5. **The handbook's buying verdict on a second unit: "Buy the second Spark and the cable when you want GLM-5.3-Flash or DeepSeek-V4.1-Flash. For most people, this is where to stop."**
   - Source: The DGX Spark Handbook, https://huggingface.co/blog/exolabs/the-dgx-spark-handbook
   - Tier: primary | Confidence: high | Accessed: 2026-09-29 | Via: web_extract
   - Quote: "Buy the second Spark and the cable when you want GLM-5.3-Flash or DeepSeek-V4.1-Flash. For most people, this is where to stop."
6. **NVIDIA's clustering docs say each Spark has two QSFP (ConnectX-7) ports rated "up to 200 Gigabits per second (Gb/s)" each, Ethernet configuration only, and the Cluster Assistant "supports up to three DGX Spark systems connected directly through cables, and up to four systems when using a switch".**
   - Source: ConnectX-7 Networking, DGX Spark User Guide, https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html
   - Tier: docs | Confidence: high | Accessed: 2026-09-29 | Via: web_extract
   - Quote: "Each port provides up to 200 Gigabits per second (Gb/s) ... The QSFP ports support Ethernet configuration only."
7. **NVIDIA's user guide sets the model ceilings at "AI models up to 200 billion parameters (or 405B for dual-Spark configuration)", while the product page markets "up to 700 billion parameters" across up to four connected systems.**
   - Source: Hardware Overview, DGX Spark User Guide, https://docs.nvidia.com/dgx/dgx-spark/hardware.html
   - Tier: docs | Confidence: high | Accessed: 2026-09-29 | Via: web_extract
   - Quote: "Support for AI models up to 200 billion parameters (or 405B for dual-Spark configuration)"
8. **Two Sparks do not merge into one machine: "You link them into a two-node cluster and then run software that can span nodes, such as vLLM with tensor parallelism, PyTorch distributed, NCCL, or llama.cpp's RPC backend. Memory isn't pooled transparently", and communication-heavy work scales sub-linearly because the 200 Gb/s RoCE link is slow next to each node's 273 GB/s memory bandwidth.**
   - Source: Two NVIDIA DGX Sparks, one cluster (Dataiku tech blog), https://www.dataiku.com/tech-blog/two-nvidia-dgx-sparks-one-cluster
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-29 | Via: web_extract
   - Quote: "You don't merge two DGX Sparks into one machine. You link them into a two-node cluster and then run software that can span nodes ... Memory isn't pooled transparently; the framework splits the model across both boxes and shuttles activations over the link."
9. **A ConnectX-7 firmware bug made fresh out-of-box clusters negotiate 200 Gb/s but deliver only about 13-27 Gb/s (one measured run showed "Speed: 26.6 Gbps"), because "The ConnectX-7 firmware was throttling itself based on a bogus 27-watt power report", and one user "went from 13 Gbps to 196 Gbps with an `apt full-upgrade` and a reboot".**
   - Source: Two NVIDIA DGX Sparks, one cluster (Dataiku tech blog), https://www.dataiku.com/tech-blog/two-nvidia-dgx-sparks-one-cluster
   - Tier: benchmark | Confidence: high | Accessed: 2026-09-29 | Via: web_extract
   - Quote: "Someone on the ASUS Ascent GX10, based on the NVIDIA DGX Spark, went from 13 Gbps to 196 Gbps with an `apt full-upgrade` and a reboot."
10. **NVIDIA's first-boot contract: "The DGX Spark device starts up immediately when power is applied", so all peripherals must be attached before power, and the initial image download "may reboot more than once", can keep working for "up to 10 minutes after the interface shows that the device is rebooting", and "powering down during updates can cause system damage".**
    - Source: Initial Setup - First Boot, DGX Spark User Guide, https://docs.nvidia.com/dgx/dgx-spark/first-boot.html
    - Tier: docs | Confidence: high | Accessed: 2026-09-29 | Via: web_extract
    - Quote: "The DGX Spark device starts up immediately when power is applied. Please attach all peripherals (display, keyboard, mouse, network, etc.) before connecting the power supply."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | hiked MSRP (launch price was $3,999) | $4,699 | https://huggingface.co/blog/exolabs/the-dgx-spark-handbook | "originally listed at $3,999, and that was hiked to $4,699" |
| 2 | NVIDIA site asking price, seen 21 September | $7,999 | https://huggingface.co/blog/exolabs/the-dgx-spark-handbook | "on 21 September I saw NVIDIA's site asking $7,999" |
| 3 | memory per Spark | 128 GB LPDDR5x unified system memory | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | "Memory | 128 GB LPDDR5x unified system memory, 256-bit interface, 4266 MHz, 273 GB/s bandwidth" |
| 4 | memory bandwidth per Spark | 273 GB/s bandwidth | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | "273 GB/s bandwidth" |
| 5 | inter-Spark link, per QSFP port | up to 200 Gigabits per second (Gb/s) | https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html | "Each port provides up to 200 Gigabits per second (Gb/s)" |
| 6 | model ceiling, single vs dual Spark | 200 billion parameters (or 405B for dual-Spark configuration) | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | "Support for AI models up to 200 billion parameters (or 405B for dual-Spark configuration)" |
| 7 | model ceiling, four systems (product page) | up to 700 billion parameters | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | "work with AI models of up to 700 billion parameters" |
| 8 | firmware-bug link speed, before vs after full upgrade | from 13 Gbps to 196 Gbps | https://www.dataiku.com/tech-blog/two-nvidia-dgx-sparks-one-cluster | "went from 13 Gbps to 196 Gbps with an `apt full-upgrade` and a reboot" |

## Analogy candidates
- **Two cars and a tow rope**: each Spark is a capable car with its own engine (273 GB/s of internal memory bandwidth); the QSFP cable is the rope that turns them into one convoy able to carry a single load too big for either (a 405B-class model split across both), but every coordination signal travels the rope, so the convoy moves slower per car than either car alone. Breaks when: the rope sounds worthless but the link is fast in absolute terms (the Cluster Assistant's pass threshold is 184 Gbit/s); it is slow only next to in-box memory bandwidth, and the analogy hides the real win, which is added capacity, not added speed.
- **Water tank behind a narrow pipe**: the Spark is a huge tank (128 GB of unified memory) feeding a narrow pipe (273 GB/s) with a strong pump behind it (up to 1 PFLOP at FP4 with sparsity); a desktop RTX 5090 is a small tank (32 GB) on a firehose (1,792 GB/s). Breaks when: reading prompts is pump-limited (compute), not pipe-limited, which is why the Spark reads long prompts far faster than it writes answers, so the "slow pipe" picture only describes token generation.

## Misconceptions
- Myth: A second Spark turns two boxes into one 256 GB computer. Reality: memory is not transparently pooled; you get a two-node cluster where the framework splits the model and shuttles activations over the 200 Gb/s link (claim 8).
- Myth: The DGX Spark still costs $3,999. Reality: MSRP was hiked to $4,699, NVIDIA's first-party marketplace is out of stock, the cheapest unit found is about $5,000, used units run around $6,000, and NVIDIA's site asked $7,999 on 21 September (claim 2).
- Myth: Clustering two Sparks is plug-and-play out of the box. Reality: a documented ConnectX-7 firmware bug throttled fresh units to roughly 13-27 Gb/s until a full system upgrade; one stale node caps the whole link (claim 9).
- Myth: nvidia-smi showing "Memory-Usage: Not Supported" means the driver install is broken. Reality: NVIDIA's Known Issues page says this is expected on the Spark's integrated GPU because iGPUs have no dedicated framebuffer memory; per-process GPU memory is still listed. (https://docs.nvidia.com/dgx/dgx-spark/known-issues.html)

## Glossary
- **DGX Spark**: NVIDIA's desk-side AI appliance, a GB10 Grace Blackwell chip with 128 GB of unified memory at 273 GB/s.
- **Unified memory**: CPU and GPU share one memory pool instead of the GPU having separate VRAM, which is why the Spark holds huge models but reports free memory differently than a discrete GPU.
- **QSFP cable**: the quad-copper cable that links Sparks through their two rear ConnectX-7 ports, rated up to 200 Gb/s each.
- **Tensor parallelism**: splitting a model's weights across machines so each machine reads only its share from its own memory, which is how linked Sparks divide one big model.
- **vLLM**: an inference framework that can span the two-node Spark cluster and split the model across both boxes.
- **Sub-linear scaling**: adding machines adds less than their full speed because communication over the interconnect, not memory or compute, becomes the bottleneck.

## Unverified
- The replies inside the NVIDIA Developer Forums thread "Is it worth buying a second DGX Spark now?" (started 23 September 2026) did not render in the fetch, so owner verdicts on the second-Spark question are unknown beyond the original post.
- Community wisdom says switching nvidia-smi power control to maximum performance is the first setting to change on a fresh Spark; no official DGX Spark docs page fetched this run confirms any user-selectable power or fan mode.
- DGX OS reportedly ships with NVIDIA driver 580.95.05, Docker, git and Python 3.12.3 preinstalled, seen only in Reddit search snippets, not a fetched page.
- Forum threads report boot loops after the first OS update and UEFI refusing recovery USB sticks; the official recovery procedure exists in the docs but the failure frequency is community sentiment only.
- The handbook's reviewer credits (author 0xSero, reviewers from EXO Labs and MiaAI Lab) appear only in X search snippets, not in any page fetched this run.
- Real dual-Spark generation throughput for a 400B-class model was not fetched; Dataiku's follow-up post was referenced but not read.

## Suggested outline
Hook on the price shock and the new one-link answer: the $3,999 Spark is dead, NVIDIA's own site was asking $7,999 on 21 September, and on September 25 ExoLabs published the handbook that settles the questions every Spark buyer keeps asking.
Establish what the handbook settles for the box you have or want: real street prices, about $12 a month to run, a first model in about an hour through LM Studio, and the machine's real shape, 128 GB of unified memory behind 273 GB/s holding up to 200B parameters.
Answer the second-Spark question the forums are asking, with the catches: two boxes are a cluster, not one merged machine, memory is not pooled, the 200 Gb/s link means capacity rather than speed, fresh clusters can ship with the link-throttling firmware bug, and the handbook's own verdict is that most people stop at two.

## Viewer situation
You've got a DGX Spark on your desk or one in a cart at a hiked price, and you keep hitting the same loop of questions: what it really costs, what to run first, and whether a second box is worth it.

## Has process
false

## Objection
It is one enthusiast's single-user measurements plus vendor-cited numbers with no standardized benchmark behind them, so the handbook's speed and scaling claims should not be quoted like NVIDIA's own specs.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/blog/exolabs/the-dgx-spark-handbook | The DGX Spark Handbook | primary | web_extract | 2026-09-29 |
| 2 | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | Hardware Overview, DGX Spark User Guide | docs | web_extract | 2026-09-29 |
| 3 | https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html | ConnectX-7 Networking, DGX Spark User Guide | docs | web_extract | 2026-09-29 |
| 4 | https://www.nvidia.com/en-us/products/workstations/dgx-spark/ | Personal AI Supercomputer Powered by Blackwell, NVIDIA DGX Spark product page | primary | web_extract | 2026-09-29 |
| 5 | https://docs.nvidia.com/dgx/dgx-spark/first-boot.html | Initial Setup - First Boot, DGX Spark User Guide | docs | web_extract | 2026-09-29 |
| 6 | https://docs.nvidia.com/dgx/dgx-spark/known-issues.html | Known Issues, DGX Spark User Guide | docs | web_extract | 2026-09-29 |
| 7 | https://docs.nvidia.com/dgx/dgx-spark/system-recovery.html | System Recovery, DGX Spark User Guide | docs | web_extract | 2026-09-29 |
| 8 | https://www.dataiku.com/tech-blog/two-nvidia-dgx-sparks-one-cluster | Two NVIDIA DGX Sparks, one cluster (Dataiku) | benchmark | web_extract | 2026-09-29 |
| 9 | https://akash.network/the-bid/m5-ultra-vs-dgx-spark-2026/ | M5 Ultra vs DGX Spark: Specs, Price & Which to Buy (Akash) | benchmark | web_extract | 2026-09-29 |
| 10 | https://forums.developer.nvidia.com/t/is-it-worth-buying-a-second-dgx-spark-now/384081 | Is it worth buying a second DGX Spark now? (NVIDIA Developer Forums) | community | web_extract | 2026-09-29 |
| 11 | https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/ | NVIDIA DGX Spark US marketplace listing | primary | web_extract | 2026-09-29 |
| 12 | https://www.youtube.com/watch?v=V17WkdXCH9U | DGX Spark Handbook (companion video) | primary | web_extract | 2026-09-29 |
| 13 | https://blog.exolabs.net/nvidia-dgx-spark | Combining NVIDIA DGX Spark + Apple Mac Studio for 4x Faster LLM Inference with EXO 1.0 | benchmark | web_extract | 2026-09-29 |

## Notes
Conflicts, kept separate on purpose. Model ceilings: NVIDIA's user guide says 200B single / 405B dual, while the product page markets up to 700B across four systems; quote the user guide for the dual-Spark number and attribute the 700B figure to the marketing page. Prices: the handbook (September, street) says about $5,000 cheapest, around $6,000 used, $7,999 on NVIDIA's site 21 September; Akash (August) still lists the $4,699 MSRP and the February 2026 hike from $3,999, and NVIDIA's marketplace is currently Out of Stock with no price shown. Trust the handbook for today's street reality, Akash for the hike date. Corroboration: the handbook's $3,999-to-$4,699 hike matches Akash's independent account. Alternatives math from Akash (August, medium confidence): two Sparks at "~$9,398 combined for 256GB" versus a Mac Studio M5 Ultra 512 GB at "$18,299 before tax", with M5 Ultra bandwidth at "1.2TB/s ... roughly 4.4x DGX Spark's 273GB/s". Why-now supports: the forums thread (10 likes, 8 users, about 1.0k views by fetch time) shows a buyer holding a second-Spark reservation at EUR 5,100 including VAT against EUR 3,200 for his March unit; sentiment unread, original post only. The companion video on 0xSero's channel (posted 28 September, 18:25 runtime, 1,469 views at fetch) covers the same ground; view counts will move. One overage to disclose: 13 pages were fetched against the standard band of 8-12 because the two NVIDIA docs fetches split across child budgets. Thin spots for the writer: attribute all tok/s and electricity figures to the handbook's own math ("the handbook's number is..."), keep the 700B figure labeled as the product page's claim, and do not present the power-mode folklore as a setting.
