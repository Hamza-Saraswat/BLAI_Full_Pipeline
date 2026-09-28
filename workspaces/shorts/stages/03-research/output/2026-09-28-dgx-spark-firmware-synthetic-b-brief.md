---
slug: 2026-09-28-dgx-spark-firmware-synthetic-b
stage: 03-research
topic: "DGX Spark firmware update: synthetic benchmarks vs real LLM serving"
depth: standard
generated_at: 2026-09-28T12:05:00Z
sources: 10
hub: "[[videos/2026-09-28-dgx-spark-firmware-synthetic-b]]"
---

# Research brief: DGX Spark firmware update: synthetic benchmarks vs real LLM serving

## Summary
The thesis in one line: the firmware update that makes synthetic burn tests read about 11% lower made real LLM serving 4% to 8% faster, so benchmark what you actually run. The most arresting number: the fp16 burn fell from 88.6 to 91.4 TFLOPS to 77.6 to 81.3 TFLOPS on all eight units while single-user decode rose from 23.1 to 25.0 tokens per second. The strongest concrete case: Petronella's field report across eight GB10 units (four DGX Spark Founders Edition, four MSI EdgeXpert), three repetitions per point with run-to-run variation of 2.2% or less. Could not be verified: the mechanism (their compute-versus-memory explanation is, in their words, "a hypothesis, not a finding") and any third-party replication (the report is one day old). Conflict: a Japanese owner's before/after on a single just-recovered unit showed no burn change at all (97.6 to 97.9 TFLOP/s median), reconciled under Notes by starting state and method.

## Thesis
After the DGX Spark firmware update, synthetic burn tests read about 11% lower while real LLM serving got 4% to 8% faster, so benchmark the workload you actually run, not the synthetic one.

## Explanation path
Start with what the machine actually does when it serves a model: prefill reads the whole prompt and is compute-bound, while decode generates tokens and is bound by how fast it can re-read the model's weights from memory. Establish that a synthetic burn test exercises only the compute path, the same path prefill uses. Then the field report lands as a paradox with a resolution: eight machines, one firmware update, the burn down about 11% on every unit while decode rose 4% to 8% at every load level, at equal or higher clocks and the same watts. The resolution is that the two tests wait on different bottlenecks, and only the serving one is what the viewer feels. Keep the honest catch visible: prefill, which is compute-bound like the burn, was flat to slightly slower, so the update trades a little peak compute for smoother serving rather than being a free win. Land the rule the viewer can repeat: benchmark the workload you actually run, before and after, same settings, and trust that pair over any synthetic number. Petronella's own explanation for the divergence stays labeled a hypothesis in the narration.

## Claims
1. **Petronella Technology updated the firmware on all eight GB10 systems in their lab (four NVIDIA DGX Spark Founders Edition, four MSI EdgeXpert) on September 25, 2026, after discovering the units had been running at least four different firmware combinations.**
   - Source: DGX Spark Firmware Update: What We Learned on 8 GB10 Units, https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/
   - Tier: primary | Confidence: high | Accessed: 2026-09-28 | Via: web_extract
   - Quote: "Our eight GB10s had two embedded controller versions on the MSI side, three different readings on the Spark side, and one Spark reporting a placeholder value of 0x00000001 for its embedded controller, SoC firmware and USB-C power delivery controller."
2. **A synthetic 15-second fp16 matrix burn test read about 11% lower on every unit after the update: from 88.6 to 91.4 TFLOPS before to 77.6 to 81.3 TFLOPS after.**
   - Source: DGX Spark Firmware Update: What We Learned on 8 GB10 Units, https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/
   - Tier: primary | Confidence: high | Accessed: 2026-09-28 | Via: web_extract
   - Quote: "Our fp16 burn dropped from 88.6 to 91.4 TFLOPS before the update to 77.6 to 81.3 TFLOPS after."
3. **Real LLM serving on the same unit, same container and same settings got 4% to 8% faster: Qwen3.8-27B decode rose from 23.1 to 25.0 tokens per second at one user and from 303.2 to 315.0 tokens per second at 32 users.**
   - Source: DGX Spark Firmware Update: What We Learned on 8 GB10 Units, https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/
   - Tier: primary | Confidence: high | Accessed: 2026-09-28 | Via: web_extract
   - Quote: "Qwen3.8-27B decode on the same unit went from 23.1 to 25.0 tokens per second for one user and from 303 to 315 tokens per second at 32 users."
4. **The after-update burn ran at equal or higher clocks (2,236 to 2,340 MHz versus 2,164 to 2,268 MHz before) at the same 91 to 94 watts, so the drop is not a clock cap or a power cap.**
   - Source: DGX Spark Firmware Update: What We Learned on 8 GB10 Units, https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/
   - Tier: primary | Confidence: high | Accessed: 2026-09-28 | Via: web_extract
   - Quote: "That is a strange result: equal or higher clocks, the same power, and less arithmetic done."
5. **Compute-bound prefill did not share the decode gain: it was flat at 8,192-token input (2,400 to 2,409 tokens per second) and slightly slower at the two longest inputs (1,302 to 1,217 tokens per second at 131,040 tokens).**
   - Source: DGX Spark Firmware Update: What We Learned on 8 GB10 Units, https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/
   - Tier: primary | Confidence: high | Accessed: 2026-09-28 | Via: web_extract
   - Quote: "Prefill, which is compute bound like the burn, did not share the gain. It was flat at 8,192 tokens of input and slightly slower at the two longest inputs"
6. **Petronella's own conclusion: judged by a synthetic burn alone, you can talk yourself out of an update that makes your real workload faster; in their words, the burn said 11% slower, the serving benchmark said 4% to 8% faster, and only one of those is what users feel.**
   - Source: DGX Spark Firmware Update: What We Learned on 8 GB10 Units, https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/
   - Tier: primary | Confidence: high | Accessed: 2026-09-28 | Via: web_extract
   - Quote: "Our burn said 11% slower; our serving benchmark said 4% to 8% faster. Only one of those is what users feel."
7. **The GB10 chip in a DGX Spark gives the CPU and GPU 128 GB of unified LPDDR5x memory at 273 GB/s, with a 140W SoC thermal design power fed by a 240W external power supply.**
   - Source: Hardware Overview - DGX Spark User Guide, https://docs.nvidia.com/dgx/dgx-spark/hardware.html
   - Tier: docs | Confidence: high | Accessed: 2026-09-28 | Via: web_extract
   - Quote: "GB10 SOC Thermal Design Power (TDP) is 140W"
8. **An HP ZGX Nano G1n owner reports GB10 boxes hard-power-off under sustained vLLM vision-model serving with no Xid, NVRM or thermal errors in the logs, and locking clocks with sudo nvidia-smi -lgc 300,2200 stopped the shutdowns for over 96 hours.**
   - Source: GB10 abruptly powers off under heavy GPU load -- nvidia-smi -lgc 300,2200 prevents it, https://forums.developer.nvidia.com/t/gb10-abruptly-powers-off-under-heavy-gpu-load-nvidia-smi-lgc-300-2200-prevents-it/384492
   - Tier: community | Confidence: high | Accessed: 2026-09-28 | Via: web_extract
   - Quote: "After applying this limit, the shutdown issue stopped occurring in my testing, and it has been running without outage for over 96 hours."
9. **A Japanese owner's DGX Spark stuck at 611 MHz decoded at 20.0 tok/s (versus the 44-47 tok/s the recipe's README lists) and recovered to 42.3 tok/s after a full power cut; on that recovered unit, a firmware update moved the burn by 97.6 to 97.9 TFLOP/s median (+0.3%), no degradation.**
   - Source: Huh? My DGX Spark might be too slow, https://note.com/fukuro_99/n/n26895f3edaad?hl=en
   - Tier: community | Confidence: medium | Accessed: 2026-09-28 | Via: web_extract
   - Quote: "At the very least, no performance degradation due to the firmware update was confirmed within the scope of this measurement."
10. **Two-node DGX Spark testing found single-stream throughput of 21.11 output tok/s against 12.36 on one node (1.71x, 85.4% efficiency), and real coding-agent workloads dominated by prompt processing rather than token generation.**
    - Source: Two NVIDIA DGX Sparks, Three Open Models, and the Benchmark that Misled Us, https://techstrong.ai/features/two-nvidia-dgx-sparks-three-open-models-and-the-benchmark-that-misled-us/
    - Tier: docs | Confidence: high | Accessed: 2026-09-28 | Via: web_extract
    - Quote: "Single-stream, TP=2 delivers 21.11 output tok/s against 12.36 on one node: 1.71x, or 85.4% efficiency."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | fp16 burn decline after firmware update | about 11% lower on every unit | https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/ | "A synthetic GPU burn test then read about 11% lower on every unit" |
| 2 | fp16 burn before vs after update | 88.6 to 91.4 TFLOPS before the update to 77.6 to 81.3 TFLOPS after | https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/ | "Our fp16 burn dropped from 88.6 to 91.4 TFLOPS before the update to 77.6 to 81.3 TFLOPS after." |
| 3 | Qwen3.8-27B decode, 1 user | 23.1 to 25.0 tokens per second | https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/ | "Qwen3.8-27B decode on the same unit went from 23.1 to 25.0 tokens per second for one user" |
| 4 | Qwen3.8-27B decode, 32 users (aggregate) | 303.2 to 315.0 tokens per second | https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/ | "from 303 to 315 tokens per second at 32 users" |
| 5 | Real serving gain across load levels | 4% to 8% | https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/ | "real LLM serving on the same unit, same container and same settings got 4% to 8% faster" |
| 6 | GB10 unified memory bandwidth | 273 GB/s | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | "128 GB LPDDR5x unified system memory, 273 GB/s bandwidth" |
| 7 | Clock-lock range that stopped power-offs | 300,2200 (MHz by nvidia-smi convention) | https://forums.developer.nvidia.com/t/gb10-abruptly-powers-off-under-heavy-gpu-load-nvidia-smi-lgc-300-2200-prevents-it/384492 | "nvidia-smi -lgc 300,2200" |

## Analogy candidates
- **Drag-strip pass vs daily delivery route**: The 15-second fp16 burn is a drag-strip pass measuring peak engine output; LLM serving is the daily delivery route where fuel delivery (the 273 GB/s memory path) sets the pace, and the firmware update hurt the drag time while improving the route. Breaks when: the GB10 did less arithmetic at equal or higher clocks and equal power, which has no clean mechanical analogue, and Petronella never measured memory bandwidth before the update, so the remap story is their unverified hypothesis.
- **Dyno peak horsepower vs towing up a grade**: The burn test is dyno peak horsepower; serving is towing a load up a grade where torque delivery and gearing (memory bandwidth, not peak compute) govern speed. Breaks when: firmware is not a physical part swap, and the report itself concedes the mechanism is "a hypothesis, not a finding".

## Misconceptions
- Myth: The firmware update made the DGX Spark 11% slower. Reality: only the synthetic burn dropped; real serving got 4% to 8% faster at every load level, while compute-bound prefill was flat to slightly slower (claims 2, 3, 5).
- Myth: A synthetic GPU benchmark predicts how fast your models will run. Reality: decode waits on the 273 GB/s memory path, not peak compute, and real coding-agent workloads are dominated by prefill anyway (claims 3, 7, 10).
- Myth: The burn drop means the hardware regressed or the clocks were capped. Reality: the after-update burn ran at equal or higher clocks at the same watts; the drop has no verified mechanism (claim 4).
- Myth: The firmware update fixes the random GB10 power-offs. Reality: units powered off before and after the update; the only reported fix is a user's clock lock, and NVIDIA's docs document no such firmware fix (claim 8; NVIDIA Known Issues names only non-supplied power adapters).

## Glossary
- **GB10**: The Grace Blackwell system-on-chip inside DGX Spark that pairs an Arm CPU with a Blackwell GPU over 128 GB of unified LPDDR5x memory.
- **fp16 burn test**: A short synthetic matrix-multiply stress test (Petronella runs a 15-second one each session) measuring peak GPU compute in TFLOPS.
- **TFLOPS**: Trillions of floating-point operations per second, the unit a compute burn test reports.
- **Decode**: The token-generation part of LLM inference, measured in tokens per second and limited by memory bandwidth because every token requires re-reading the model's active weights.
- **Prefill**: The part of LLM inference that processes the input prompt before generation begins; like a burn test it is compute-bound.
- **NVFP4**: A 4-bit floating-point weight-quantization format in which Petronella served Qwen3.8-27B for the before/after firmware measurements.
- **vLLM**: An open-source engine for serving LLMs to many simultaneous users.
- **fwupdmgr**: The Linux Vendor Firmware Service client that delivered the firmware updates on all eight units, from the command line.
- **nvidia-smi -lgc**: nvidia-smi's lock-GPU-clocks flag that pins the GPU core clock to a min,max range (300,2200 in the forum report).
- **Embedded controller (EC)**: A board-level microcontroller whose firmware manages power and thermal behavior.
- **Unified memory**: A design where the GPU shares system DRAM with the CPU instead of having separate VRAM.

## Unverified
- Petronella's explanation that the new firmware hurt the compute path without hurting the memory path is, in their own words, "a hypothesis, not a finding"; they had no memory-bandwidth reading from before the update.
- That the 300,2200 values passed to nvidia-smi -lgc are in MHz is nvidia-smi convention only; the forum thread does not state units.
- That a GPU power spike causes the GB10 power-offs: the original poster explicitly declines to claim a root cause, and the thread holds no NVIDIA staff reply.
- The companion Petronella post's finding that updated units split into 262 to 263 GB/s and 238 to 242 GB/s read-bandwidth tiers is referenced in the report but that page was not fetched this run.
- The NVIDIA forum thread reporting a 50 to 60% system-wide slowdown after DGX OS 7.6.0, and the kho=off hotfix reply, are summarized inside the Petronella report; the thread itself was not fetched.
- How Qwen3.8-27B relates to other Qwen releases was not verified from a fetched page; the name appears only in the Petronella report and its linked community content.
- Whether the September 14, 2026 DGX OS 7.6.0 release changes power or clock behavior is unknown; the DGX Spark release notes contain no September 2026 entry.

## Suggested outline
1. Hook: the burn test said 11% slower; the serving test said 4% to 8% faster; same machines, same update.
2. What a burn test measures: peak fp16 compute, in TFLOPS, for 15 seconds.
3. What serving actually waits on: every generated token re-reads the model from the 273 GB/s unified memory, so decode is a memory test, not a compute test.
4. The field report: eight units, burn 88.6-91.4 down to 77.6-81.3 TFLOPS, decode up at every load level, at equal or higher clocks and the same watts.
5. The honest catch: prefill, compute-bound like the burn, was flat to slightly slower; this is a trade, not a free win.
6. The rule: benchmark the workload you actually run, before and after any firmware update, same model and settings.
7. Close: if your Spark hard-powers-off under load, that is a different problem with a different fix (lock the clocks), not a benchmark story.

## Viewer situation
You own or you are eyeing a DGX Spark, you run the firmware update when the Dashboard prompts you, and you check the machine with a GPU benchmark to make sure nothing broke.

## Has process
true
- Run the workload you actually serve (your model, your engine, your settings) and write down its tokens per second before updating
- Apply the firmware update through the DGX Dashboard or fwupdmgr
- Re-run the exact same workload, three repetitions, same model, container and settings
- Compare the two tokens-per-second numbers and trust that pair over any synthetic burn result

## Objection
Eight units in one lab, one model (Qwen3.8-27B), and a burn drop with no verified mechanism: that is not evidence the update helps my workload.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://petronellatech.com/blog/dgx-spark-firmware-update-what-we-learned-on-8-gb10-units/ | DGX Spark Firmware Update: What We Learned on 8 GB10 Units | primary | web_extract | 2026-09-28 |
| 2 | https://docs.nvidia.com/dgx/dgx-spark/release-notes.html | DGX Spark Release Notes - DGX Spark User Guide | docs | web_extract | 2026-09-28 |
| 3 | https://docs.nvidia.com/dgx/dgx-spark/known-issues.html | Known Issues - DGX Spark User Guide | docs | web_extract | 2026-09-28 |
| 4 | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | Hardware Overview - DGX Spark User Guide | docs | web_extract | 2026-09-28 |
| 5 | https://docs.nvidia.com/dgx/dgx-spark/os-and-component-update.html | OS and Component Update Guide - DGX Spark User Guide | docs | web_extract | 2026-09-28 |
| 6 | https://docs.nvidia.com/dgx/dgx-os-7-user-guide/release_notes.html | Release Notes - NVIDIA DGX OS 7 User Guide | docs | web_extract | 2026-09-28 |
| 7 | https://forums.developer.nvidia.com/t/gb10-abruptly-powers-off-under-heavy-gpu-load-nvidia-smi-lgc-300-2200-prevents-it/384492 | GB10 abruptly powers off under heavy GPU load -- nvidia-smi -lgc 300,2200 prevents it | community | web_extract | 2026-09-28 |
| 8 | https://note.com/fukuro_99/n/n26895f3edaad?hl=en | Huh? My DGX Spark might be too slow | community | web_extract | 2026-09-28 |
| 9 | https://techstrong.ai/features/two-nvidia-dgx-sparks-three-open-models-and-the-benchmark-that-misled-us/ | Two NVIDIA DGX Sparks, Three Open Models, and the Benchmark that Misled Us | docs | web_extract | 2026-09-28 |
| 10 | https://ollama.com/blog/nvidia-spark-performance | NVIDIA DGX Spark performance (Ollama blog) | docs | web_extract | 2026-09-28 |

## Notes
Conflict: note.com's before/after burn on a single just-recovered unit read 97.6 to 97.9 TFLOP/s (+0.3%, no degradation) versus Petronella's about 11% drop across eight units. The two start from different states (recovered from a 611 MHz stuck clock versus steady lab operation) and use different methods (a single 60-second benchmark versus the 15-second fp16 burn, three repetitions, variation 2.2% or less); we trust Petronella for the update effect on the unit count and repetition. NVIDIA's DGX Spark release notes carry no entry for the September firmware Petronella applied, and the Spark user guide's current-version table (DGX OS 7.5.0, driver 580.159.03) lags both the DGX OS 7 guide (7.6.0, September 14, 2026) and what the eight units ran (kernel 7.0.0-1019-nvidia, driver 580.178.04). A Medium piece on NVIDIA's January update was paywalled and is not cited. The burn-test tool is never named in the report.
