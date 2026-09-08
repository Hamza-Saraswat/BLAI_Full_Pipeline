# Q2 — What open-weight actually gets a local runner with Mistral today
Slug: 2026-09-08-mistral-raises-3b-euro-for-ope | Researched: 2026-09-08 | Budget used: 2 searches, 4 fetches (HF org page, mistral.ai/news/mistral-3, MNPL-0.1.md, Mistral-Small-4-119B-2603 model card). The €3B announcement page was NOT fetched (owned by another subagent).

FINDINGS: claim (one sentence) | verbatim quote | url | page title | tier | confidence high/medium | fetched via | accessed date

FINDINGS: The entire Mistral 3 generation — Ministral 3B/8B/14B and Mistral Large 3 — is downloadable under Apache 2.0 | "All models are released under the Apache 2.0 license." | https://mistral.ai/news/mistral-3 | Introducing Mistral 3 | Mistral AI | primary | high | web_extract | 2026-09-08
FINDINGS: Mistral Large 3 is a sparse mixture-of-experts with 675B total and 41B active parameters, released in both base and instruct versions under Apache 2.0 | "Mistral Large 3 – our most capable model to date – a sparse mixture-of-experts trained with 41B active and 675B total parameters." | https://mistral.ai/news/mistral-3 | Introducing Mistral 3 | Mistral AI | primary | high | web_extract | 2026-09-08
FINDINGS: Ministral 3 comes in 3B, 8B, and 14B dense sizes, each with base, instruct and reasoning variants including image understanding, all Apache 2.0 | "For edge and local use cases, we release the Ministral 3 series, available in three model sizes: 3B, 8B, and 14B parameters." | https://mistral.ai/news/mistral-3 | Introducing Mistral 3 | Mistral AI | primary | high | web_extract | 2026-09-08
FINDINGS: Mistral explicitly targets consumer/edge hardware for Ministral: NVIDIA-optimized deployments on DGX Spark, RTX PCs and laptops, and Jetson devices | "On the edge, delivers optimized deployments of the Ministral models on DGX Spark, RTX PCs and laptops, and Jetson devices, giving developers a consistent, high-performance path to run these open models from data center to robot." | https://mistral.ai/news/mistral-3 | Introducing Mistral 3 | Mistral AI | primary | high | web_extract | 2026-09-08
FINDINGS: Even compressed, Mistral Large 3 is a datacenter-class download — the NVFP4 checkpoint targets an 8-GPU node, not a gaming PC | "This optimized checkpoint lets you run Mistral Large 3 efficiently on Blackwell NVL72 systems and on a single 8×A100 or 8×H100 node using vLLM." | https://mistral.ai/news/mistral-3 | Introducing Mistral 3 | Mistral AI | primary | high | web_extract | 2026-09-08
FINDINGS: A reasoning-tuned Large 3 was already promised as next weights in the pipeline as of Dec 2025 | "We release both the base and instruction fine-tuned versions of Mistral Large 3 under the Apache 2.0 license... A reasoning version is coming soon!" | https://mistral.ai/news/mistral-3 | Introducing Mistral 3 | Mistral AI | primary | high | web_extract | 2026-09-08
FINDINGS: Mistral runs a second, non-commercial license track (MNPL) under which models are downloadable but restricted to testing, research, personal and evaluation use in non-production environments | "You shall only use the Mistral Models and Derivatives (whether or not created by Mistral AI) for testing, research, Personal, or evaluation purposes in Non-Production Environments" | https://mistral.ai/licenses/MNPL-0.1.md | Mistral AI Non-Production License | primary | high | web_extract | 2026-09-08
FINDINGS: MNPL models cannot be supplied commercially in any form — free or paid, hosted or behind a software layer — without a separate Mistral license | "You shall not supply the Mistral Models or Derivatives in the course of a commercial activity, whether in return for payment or free of charge, in any medium or form, including but not limited to through a hosted or managed service (e.g. SaaS, cloud instances, etc.), or behind a software layer." | https://mistral.ai/licenses/MNPL-0.1.md | Mistral AI Non-Production License | primary | high | web_extract | 2026-09-08
FINDINGS: Even under MNPL, whatever the model generates is yours — Mistral claims no ownership of outputs | "We claim no ownership rights in and to the Outputs." | https://mistral.ai/licenses/MNPL-0.1.md | Mistral AI Non-Production License | primary | high | web_extract | 2026-09-08
FINDINGS: The weights live on the official mistralai Hugging Face organization, which hosts 75 models and commits to releasing all new checkpoints there | "Welcome to the official Hugging Face Mistral AI organization! New checkpoints will be released in this organization." | https://huggingface.co/mistralai | mistralai (Mistral AI_) | primary (HF org) | high | web_extract | 2026-09-08
FINDINGS: Mistral also maintains a second Hugging Face org for experimental checkpoints | "For more checkpoints also see mistral-experimental." | https://huggingface.co/mistralai | mistralai (Mistral AI_) | primary (HF org) | high | web_extract | 2026-09-08
FINDINGS: The current local-runner sweet spot, Mistral Small 4, is an Apache 2.0 MoE with 119B total / 6.5B active parameters and a 256k context window | "**119B parameters**, with **6.5B activated per token**." and "**256k context length**." | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 | mistralai/Mistral-Small-4-119B-2603 · Hugging Face | primary (model card) | high | web_extract | 2026-09-08
FINDINGS: Mistral Small 4's Apache 2.0 covers commercial use, and the card routes local runners to llama.cpp (Unsloth GGUFs), LM Studio, and vLLM | "**Apache 2.0 License**: Open-source license for both commercial and non-commercial use." | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 | mistralai/Mistral-Small-4-119B-2603 · Hugging Face | primary (model card) | high | web_extract | 2026-09-08
FINDINGS: Small 4 ships in safetensors with BF16 and F8_E4M3 tensor types, and the ecosystem adds 33 community quantization repos (incl. GGUF) and 16 finetunes | "Tensor type BF16 · F8_E4M3" / "Quantizations [33 models]" | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603 | mistralai/Mistral-Small-4-119B-2603 · Hugging Face | primary (model card) | high | web_extract | 2026-09-08
FINDINGS: Official download appetite as of today: Medium 3.5 128B ~115k and Small 4 119B ~55.6k monthly pulls on the org page, while the 675B Large 3 sits at ~2.21k — big models get downloaded, small ones get run | "119B•Updated Jul 15• 55.6k• 421" / "128B•Updated Jul 15• 115k• 437" / "675B... 2.21k• 248" | https://huggingface.co/mistralai | mistralai (Mistral AI_) | primary (HF org) | medium | web_extract | 2026-09-08
FINDINGS: Derived disk math from verified param counts (2 bytes/param BF16, ~0.5 bytes/param 4-bit): Large 3 ≈ 1,350 GB BF16 / ~337.5 GB 4-bit; Medium 3.5 ≈ 256 GB BF16; Small 4 ≈ 238 GB BF16 / ~59.5 GB 4-bit; Ministral 14B ≈ 28 GB BF16 / ~7 GB 4-bit; 8B ≈ 16 GB / 4 GB; 3B ≈ 6 GB / 1.5 GB — so a 24 GB gaming GPU or 32 GB Mac runs Ministral comfortably, Small 4 only quantized | "a sparse mixture-of-experts trained with 41B active and 675B total parameters" (param basis) | https://mistral.ai/news/mistral-3 | Introducing Mistral 3 | primary params / derived math | medium | web_extract + computation | 2026-09-08

NUMBERS: label | verbatim value with unit | url
NUMBERS: Mistral Large 3 total parameters | "675B total parameters" | https://mistral.ai/news/mistral-3
NUMBERS: Mistral Large 3 active parameters | "41B active" | https://mistral.ai/news/mistral-3
NUMBERS: Large 3 training compute | "trained from scratch on 3000 of NVIDIA's H200 GPUs" | https://mistral.ai/news/mistral-3
NUMBERS: Ministral 3 sizes | "three model sizes: 3B, 8B, and 14B parameters" | https://mistral.ai/news/mistral-3
NUMBERS: Ministral 3 14B reasoning score | "85% on AIME '25 with our 14B variant" | https://mistral.ai/news/mistral-3
NUMBERS: Large 3 NVFP4 hardware target | "a single 8×A100 or 8×H100 node" | https://mistral.ai/news/mistral-3
NUMBERS: Mistral Small 4 total parameters | "119B params" | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
NUMBERS: Mistral Small 4 active parameters | "6.5B activated per token" | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
NUMBERS: Mistral Small 4 MoE config | "MoE: 128 experts, 4 active." | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
NUMBERS: Mistral Small 4 context | "256k context length" | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
NUMBERS: Mistral Small 4 downloads | "Downloads last month 56,192" | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
NUMBERS: Community quantizations of Small 4 | "33 models" (quantization repos) | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
NUMBERS: HF org model count | "75" ("View 75 models") | https://huggingface.co/mistralai
NUMBERS: Mistral Medium 3.5 128B org-page downloads | "115k" | https://huggingface.co/mistralai
NUMBERS: Mistral Large 3 org-page downloads | "2.21k" | https://huggingface.co/mistralai
NUMBERS: Ministral-3-8B org-page downloads | "19.3k" | https://huggingface.co/mistralai
NUMBERS: Voxtral-Mini-4B-Realtime org-page downloads | "2.24M" | https://huggingface.co/mistralai
NUMBERS: Large 3 API price | "Input (/M tokens) $0.5" / "Output (/M tokens) $1.5" | https://mistral.ai/news/mistral-3
NUMBERS: Ministral 3 8B API price | "Input (/M tokens) $0.15" / "Output (/M tokens) $0.15" | https://mistral.ai/news/mistral-3
NUMBERS: DERIVED, not quoted: Large 3 disk at BF16 | ~1,350 GB (675B × 2 bytes) | https://mistral.ai/news/mistral-3
NUMBERS: DERIVED, not quoted: Large 3 disk at 4-bit | ~337.5 GB | https://mistral.ai/news/mistral-3
NUMBERS: DERIVED, not quoted: Small 4 disk at BF16 / 4-bit | ~238 GB / ~59.5 GB | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
NUMBERS: DERIVED, not quoted: Medium 3.5 128B disk at BF16 | ~256 GB | https://huggingface.co/mistralai
NUMBERS: DERIVED, not quoted: Ministral 3B / 8B / 14B disk at BF16 | ~6 GB / ~16 GB / ~28 GB (4-bit: ~1.5 / 4 / 7 GB) | https://mistral.ai/news/mistral-3

ANALOGY CANDIDATES: vehicle | mapping | where it breaks
ANALOGY CANDIDATES: Blu-ray vs streaming | Apache-2.0 weights = owning the disc: download once, runs offline forever, no per-token bill, no server shutdown can brick it | Breaks because a license still rides along — MNPL discs play at home but can't be screened commercially, and the disc is the weights only (no training-data "bonus features")
ANALOGY CANDIDATES: Car with a welded hood vs engine you can rebuild | Open weights = you get the full engine (parameters) to tune, quantize, fine-tune, and inspect; closed API = the hood is welded shut and you pay per mile | Breaks because "open-weight" ≠ "open-source": you get the finished engine, not the factory (training data, code, recipe) that built it
ANALOGY CANDIDATES: Giant office building where you only light the rooms in use (MoE) | Mistral Small 4: a 119B-parameter building but only 6.5B lights on per token — that's why it feels fast despite its size | Breaks because you still have to buy the whole building: disk and VRAM must hold all 128 experts even though only 4 fire at a time
ANALOGY CANDIDATES: IKEA flat-pack vs ready-made furniture | Quantized GGUF/NVFP4 checkpoints = the flat-pack version of the model, small enough for a gaming trunk (24 GB GPU) or Mac | Breaks because compression trades a little quality, and some packs (NVFP4 Large 3) still only fit in a warehouse (8×H100 node)

MISCONCEPTIONS: myth | reality | url
MISCONCEPTIONS: "Everything Mistral posts on Hugging Face is free for any use" | Mistral dual-tracks: the Mistral 3 family and Small 4 are Apache 2.0, but models under the Non-Production License bar any commercial supply without a separate grant | https://mistral.ai/licenses/MNPL-0.1.md
MISCONCEPTIONS: "Open weights = open source, datasets and all" | The Apache 2.0 grant covers the downloadable artifact — weights plus inference/eval code as defined per license; no fetched Mistral page claims training data or training code ships with it | https://mistral.ai/news/mistral-3
MISCONCEPTIONS: "675B parameters means a 675 GB download" | 675B is the parameter count; in BF16 that's ~1,350 GB, and Mistral's compressed NVFP4 checkpoint targets "a single 8×A100 or 8×H100 node" — either way it's multi-GPU-server territory, not a gaming PC | https://mistral.ai/news/mistral-3
MISCONCEPTIONS: "If I can download it, I can build a product on it" | Under MNPL you may run it personally and keep the outputs ("We claim no ownership rights in and to the Outputs"), but you may not supply the model itself commercially in any form | https://mistral.ai/licenses/MNPL-0.1.md
MISCONCEPTIONS: "A Mac can't run Mistral models" | The Small 4 card explicitly lists llama.cpp (via Unsloth GGUFs) and LM Studio as supported deployment paths — both run on Apple Silicon; only the huge checkpoints are out of reach | https://huggingface.co/mistralai/Mistral-Small-4-119B-2603

GLOSSARY: term | one-sentence definition
GLOSSARY: Open weights | The trained numerical parameters of a model are published for download (typically on Hugging Face), even if the training data, training code, or full open-source license are not included.
GLOSSARY: Apache 2.0 | A permissive OSI-approved license granting royalty-free use, modification, and distribution — including commercial — with attribution and notice retention, and it is what Mistral's 3-generation models ship under.
GLOSSARY: MNPL (Mistral Non-Production License) | Mistral's research-and-personal license: you may download, run, and modify the model, but only in non-production environments and never supply it commercially without a separate grant.
GLOSSARY: Community license (usage-threshold style) | A bespoke vendor license (as with Llama-style models) that permits wide use, including commercial, until a scale threshold (e.g. monthly active users) or territorial clause is hit. (No Mistral repo under this tier was verified this session.)
GLOSSARY: MoE (mixture-of-experts) | An architecture that stores many specialist "expert" sub-networks but routes each token through only a few, so total parameter count is huge while per-token compute stays small.
GLOSSARY: Active parameters | The subset of a MoE's weights that actually process a given token — e.g. 6.5B of Mistral Small 4's 119B, or 41B of Large 3's 675B.
GLOSSARY: NVFP4 | A 4-bit floating-point quantization format (NVIDIA) that shrinks checkpoints roughly 4× versus BF16 for efficient serving on modern datacenter GPUs.
GLOSSARY: GGUF | The single-file quantized model format used by llama.cpp and LM Studio, the standard route for running models locally on consumer GPUs and Apple Silicon Macs.
GLOSSARY: BF16 | Bfloat16, the 2-bytes-per-parameter training/serving precision that sets the "full-size" download: multiply parameter count by 2 to approximate disk in GB.
GLOSSARY: Safetensors | A safe, fast serialization format for tensor data that is the standard weight-file format on Hugging Face.

UNVERIFIED: plain sentences
UNVERIFIED: Which specific current mistralai repos carry the MNPL rather than Apache 2.0 — a search snippet said Codestral was the first MNPL model, but a snippet is not a fetch and no per-repo license check fit the budget; the org page shows no license column.
UNVERIFIED: Whether Mistral still maintains a separate "Community License" tier (MRL/MCL-era terms like the 1M-MAU clause) alongside Apache 2.0 and MNPL today — no such license page was fetched this session.
UNVERIFIED: What the €3B announcement explicitly pledges about the NEXT frontier model's weights — any named model, release window, or conditions; the announcement page was owned by another subagent and deliberately not fetched here, so the orchestrator should merge the q1 packet for that quote.
UNVERIFIED: Actual per-repo file sizes in GB/TB on Hugging Face (the safetensors file trees were not fetched); all disk figures above are derived from parameter counts, not quoted from a page.
UNVERIFIED: Any Mac-specific (MLX) builds or minimum-RAM guidance from Mistral itself — the llama.cpp and LM Studio links on the Small 4 card are generic, and no Apple-Silicon-specific claim appeared on a fetched page.
UNVERIFIED: Whether a Mistral Large 3 reasoning checkpoint has actually shipped since the December 2025 "coming soon" promise — not checked within budget.

NOT FOUND: what you searched for and did not find
NOT FOUND: A per-repo license table for the 75 models on the mistralai HF org (org listing exposes sizes and downloads but not licenses; per-model checks exhausted the fetch budget).
NOT FOUND: Official GB/TB weight-file sizes for any Mistral checkpoint (would require fetching each repo's Files tree; not done).
NOT FOUND: A fetched page naming the next frontier model or restating the €3B pledge's weight commitments — excluded by task rules since another subagent owns the announcement URL.
NOT FOUND: Any Mac/Apple-Silicon-specific deployment statement from Mistral (only generic llama.cpp / LM Studio pointers found on the Small 4 card).
