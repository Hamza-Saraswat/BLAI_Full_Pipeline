<!-- url: https://wccftech.com/axera-ax8860-ai-chip-beat-dgx-spark-ai-llms-128-gb-memory-40w-less-cost/ -->
<!-- fetched via web_extract 2026-10-24, tier 2 (docs) -->

# Axera Claims AX8860 AI Chip Can Beat the DGX Spark in AI LLMs by 25%, Offering 273 GB/s Bandwidth, 128 GB LP5X Memory, All at 40W While A 4-Module PCIe Card Pumps Out Over 1000 TOPs

Hassan Mujtaba, Oct 13, 2026.

- "Chinese AI company Axera has unveiled its next-generation solutions designed to run AI LLMs and AI agents. The chip is the AX8860, which is based on a 16-core Arm Cortex-A55 CPU, an NPU with up to 256 TOPS of compute, and a 256-bit LPDDR5/5X controller. The chip has been designed on a 6nm process technology and features PCIe 5.0 connectivity."
- "The 256 TOPS figure is derived from pure FP4 without any sparsity involved."
- "the chip can be configured with up to 128 GB of LPDDR5X memory across the aforementioned 256-bit bus interface, driving a bandwidth of up to 273 GB/s, which puts it next to NVIDIA's DGX Spark"
- Clustering: 256 Gbps networking (vs DGX Spark 200 Gbps); 2x = 512 TOPS, 4x = 1024 TOPS at "a scaling efficiency of 80%".
- "The first is a dedicated module with a power rating of 40W."
- "They claim to have tested Qwen 27B at 25% faster prefill and 30% faster decode speeds than the NVIDIA DGX Spark. They also claim that the chip will be almost half the price of the DGX Spark"
- Sipeed tweet quote: "DGX spark 1000TOPS is fake \"sparse\", in fact this chip is 25% faster than dgx spark in real qwen 27B model test!" -- Sipeed (@SipeedLab) October 13, 2026
- "Sipeed also mentions that they will have a pre-order page for their devices, such as the MaixStation, open in 24 hours, and that it will be available within this year. On the software side, the chip supports many LLM development frameworks such as vLLM, SGLang, PyTorch, etc."
- Spec table: AX8860 "Up to 256 TOPS FP4 (no sparsity)"; DGX Spark "Up to ~1 PFLOP FP4 (with sparsity)"; both 273 GB/s (256-bit); AX8860 power "~40 W (dedicated module)".
- Pricing note: DGX Spark 128 GB "retails for over $7000 US, or the 64 GB configuration, which retails for $4999."
