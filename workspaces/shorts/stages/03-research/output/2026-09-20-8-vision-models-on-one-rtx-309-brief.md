---
slug: 2026-09-20-8-vision-models-on-one-rtx-309
stage: 03-research
topic: "8 vision models benchmarked on one RTX 3090 (24 GB)"
depth: standard
generated_at: 2026-09-20T11:48:26Z
sources: 9
hub: "[[videos/2026-09-20-8-vision-models-on-one-rtx-309]]"
---

# Research brief: 8 vision models benchmarked on one RTX 3090 (24 GB)

## Summary
The video lands one decision: for vision workloads, the five-year-old card stays in the tower. The most arresting number is a vision model with 30.8B-A3B total parameters decoding at 139.3 tok/s on 2020 silicon. The strongest concrete case is the r/LocalLLaMA test posted 2026-09-20 that loaded eight video VLMs, from Cosmos-Reason2-2B up to InternVL3.5-30B-A3B, on a single RTX 3090 at concurrency 1 and measured prefill 745-4,737 tok/s and decode 13.8-139.3 tok/s. What could not be verified: per-model VRAM at rest or peak, which two models' outputs were rejected in the submission, the inference runtime used, and used prices outside the US. The conflict: the author himself calls the numbers "not a benchmark in any real sense, but can be seen as an anecdotal reference", and his Task 1 table's top prefill (4,745 tok/s) edges the ceiling his own title quotes (4,737 tok/s, Task 2), so this brief quotes the author's title range.

## Thesis
A five-year-old RTX 3090 with 24 GB still runs every vision model in this eight-model test, some at 139.3 tok/s, so the upgrade question for vision work is speed and patience, not capability.

## Explanation path
Start with what a vision-language model actually is: a language model with eyes, where a vision encoder turns frames into tokens and the language model reads them, so what fits in memory decides what runs at all before speed ever enters. Establish the card's two numbers from its vendor and from reporting: 24 GB of G6X memory and 936GB/s of memory bandwidth, the figure inference leans on hardest. Then bring the receipt: one tester, one RTX 3090, eight video VLMs spanning 2B to a 30.8B-A3B mixture-of-experts, every one loaded and answering, decode spanning 13.8 to 139.3 tok/s. Explain the twist before the limit: the biggest model by total parameters was the fastest decoder, because a mixture-of-experts wakes only a slice of its weights per token, so total parameters set what fits while active parameters set the pace. Close on the honest ceiling so the myth-bust stays credible: the wait for a first answer stretches to 5.73 s, 70B-class models do not fit even quantized to four or eight bit, and long video contexts eat the KV cache. Land on the decision the viewer came for: if the workload is vision, the old card is not the blocker, and a used one still costs real money that a new midrange card with less memory does not displace.

## Claims
1. **NVIDIA's own spec page lists the RTX 3090 with 24 GB of G6X memory, 10,496 CUDA cores, and a 1.70 GHz boost clock.**
   - Source: 3090 & 3090 Ti Graphics Cards, https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/
   - Tier: primary | Confidence: high | Accessed: 2026-09-20 | Via: web_extract
   - Quote: "a staggering 24 GB of G6X memory to deliver high-quality performance for gamers and creators"; specs table: "NVIDIA CUDA Cores | 10752 | 10496", "Boost Clock | 1.86 GHz | 1.70 GHz", "Memory Size | 24 GB | 24 GB" (RTX 3090 column)
2. **The Register reports the RTX 3090 offers 936GB/s of memory bandwidth and 142 teraFLOPS of dense FP16, calling bandwidth the key decider for LLM inference.**
   - Source: Benchmarks show even an old Nvidia RTX 3090 is enough to serve LLMs to thousands, https://www.theregister.com/on-prem/2024/08/23/old-rtx-3090-enough-to-serve-thousands-of-llm-users/1366649
   - Tier: docs | Confidence: high | Accessed: 2026-09-20 | Via: web_extract
   - Quote: "it boasts 142 teraFLOPS of dense FP16 performance and offers 936GB/s of memory bandwidth, the latter being a key decider of performance in LLM inferencing workloads"
3. **A tester posting to r/LocalLLaMA on 2026-09-20 ran eight video VLMs of different parameter sizes and architectures on a single RTX 3090, at concurrency 1, as part of a NIST/TREC visual question-answering submission.**
   - Source: How fast do video VLMs actually run on a 3090? I measured 8 VLMs of different parameter sizes and architecture, https://www.reddit.com/r/LocalLLaMA/comments/1wkmzwi/how_fast_do_video_vlms_actually_run_on_a_3090_i/
   - Tier: benchmark | Confidence: medium | Accessed: 2026-09-20 | Via: web_extract (pullpush.io mirror; result tables read from preview.redd.it images via OCR)
   - Quote: "I have been taking part in a NIST/TREC submission for visual Q&A."; "Concurreny=1 and this is not a batched inference" (sic); "TTFT includes the vision encoder and any server-side video decode."
4. **Across the eight models the tester reported prefill throughput of 745-4,737 tok/s and decode throughput of 13.8-139.3 tok/s.**
   - Source: Prefill/decode throughput for 8 video VLMs on one 3090: 745-4,737 tok/s prefill, 13.8-139.3 decode (author's crosspost to r/LocalLLM), https://www.reddit.com/r/LocalLLM/comments/1wkmfq8/prefilldecode_throughput_for_8_video_vlms_on_one/
   - Tier: benchmark | Confidence: medium | Accessed: 2026-09-20 | Via: web_extract (pullpush.io mirror)
   - Quote: "Prefill/decode throughput for 8 video VLMs on one 3090: 745–4,737 tok/s prefill, 13.8–139.3 decode"
5. **In the test's tables the fastest decoder was InternVL3.5-30B-A3B at 139.3 tok/s (Task 2) and the slowest was Qwen3.8-27B INT4 at 13.8 tok/s, with time-to-first-token spanning 1.80 s (VideoLLaMA3-7B) to 5.73 s (Muse Glimmer 30B).**
   - Source: How fast do video VLMs actually run on a 3090?, https://www.reddit.com/r/LocalLLaMA/comments/1wkmzwi/how_fast_do_video_vlms_actually_run_on_a_3090_i/
   - Tier: benchmark | Confidence: medium | Accessed: 2026-09-20 | Via: web_extract (pullpush.io mirror; preview.redd.it table images via OCR)
   - Quote: table rows: "InternVL3.5-30B-A3B | 1,764 | 139.3 | 4,508 | 44 | 32-44 | 2.57"; "Qwen3.8-27B INT4 | 999 | 13.8 | 4,761 | 256 | 256-256 | 4.91"; "VideoLLaMA3-7B ... 1.80"; "Muse Glimmer 30B ... 5.73"
6. **The InternVL3.5-30B-A3B model card lists 0.3B vision parameters plus 30.5B language parameters, for 30.8B-A3B total.**
   - Source: OpenGVLab/InternVL3_5-30B-A3B, https://huggingface.co/OpenGVLab/InternVL3_5-30B-A3B
   - Tier: primary | Confidence: high | Accessed: 2026-09-20 | Via: web_extract
   - Quote: "| InternVL3.5-30B-A3B | 0.3B | 30.5B | 30.8B-A3B |"
7. **The Qwen3-VL-8B-Instruct model card lists the model at 9B params in BF16 and advertises native 256K context, expandable to 1M.**
   - Source: Qwen/Qwen3-VL-8B-Instruct, https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct
   - Tier: primary | Confidence: high | Accessed: 2026-09-20 | Via: web_extract
   - Quote: "Model size: 9B params, Tensor type: BF16"; "Long Context & Video Understanding: Native 256K context, expandable to 1M; handles books and hours-long video with full recall and second-level indexing."
8. **The Register notes the card's honest ceiling: 24GB of GDDR6x rules out 70B-class models even quantized to four or eight bit.**
   - Source: Benchmarks show even an old Nvidia RTX 3090 is enough to serve LLMs to thousands, https://www.theregister.com/on-prem/2024/08/23/old-rtx-3090-enough-to-serve-thousands-of-llm-users/1366649
   - Tier: docs | Confidence: high | Accessed: 2026-09-20 | Via: web_extract
   - Quote: "With 24GB of GDDR6x memory, you aren't going to be running models like Llama 3 70B or Mistral Large even if you quantized them to four or eight bit precisions."
9. **ModelFit pegs the used RTX 3090 at $800-1000 (about $900 street, September 2026), says its 24 GB handles up to 32B-parameter models at Q4 (about 0.6 GB of VRAM per billion parameters), and estimates an RTX 4090 is only 20% faster (104 vs 87 tok/s on 8B) at about $3,494.**
   - Source: RTX 3090 24GB for Local LLMs: Runs 32B Q4, Used ~$900, https://modelfit.io/gpu/rtx-3090/
   - Tier: benchmark | Confidence: medium | Accessed: 2026-09-20 | Via: web_extract
   - Quote: "At $800-1000 on the used market, its 24GB VRAM handles 32B models that $999 16GB cards cannot."; "a Q4 model needs about 0.6 GB of VRAM per billion parameters"; "The RTX 4090 is 20% faster (an estimated 104 vs 87 tok/s on 8B) with the same 24GB VRAM."; comparison table: "RTX 4090 | 24 GB | 104 tok/s | 1008 GB/s | $3,494"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | RTX 3090 memory (NVIDIA spec page) | 24 GB of G6X memory | https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/ | "a staggering 24 GB of G6X memory" |
| 2 | RTX 3090 memory bandwidth | 936GB/s | https://www.theregister.com/on-prem/2024/08/23/old-rtx-3090-enough-to-serve-thousands-of-llm-users/1366649 | "offers 936GB/s of memory bandwidth" |
| 3 | decode throughput span, 8 video VLMs on one 3090, concurrency 1 | 13.8-139.3 tok/s (author's title: "13.8–139.3 decode") | https://www.reddit.com/r/LocalLLM/comments/1wkmfq8/prefilldecode_throughput_for_8_video_vlms_on_one/ | "13.8–139.3 decode" |
| 4 | fastest decode, InternVL3.5-30B-A3B, Task 2 | 139.3 tok/s | https://www.reddit.com/r/LocalLLaMA/comments/1wkmzwi/how_fast_do_video_vlms_actually_run_on_a_3090_i/ | "InternVL3.5-30B-A3B | 1,764 | 139.3 | ..." |
| 5 | InternVL3.5-30B-A3B total parameters | 30.8B-A3B | https://huggingface.co/OpenGVLab/InternVL3_5-30B-A3B | "| InternVL3.5-30B-A3B | 0.3B | 30.5B | 30.8B-A3B |" |
| 6 | used RTX 3090 street price (US, September 2026) | ~$900 | https://modelfit.io/gpu/rtx-3090/ | "Price ~$900* Used market price" |

## Analogy candidates
- **A five-year-old pickup with the big bed vs a new sports car with a small trunk**: vision models are bulky cargo; the old card's 24 GB carries them even though the newer vehicle is quicker per trip. Breaks when: the job is many small fast trips (high-concurrency serving or chasing peak tok/s), where the newer card's bandwidth and headroom win.

## Misconceptions
- Myth: A five-year-old consumer GPU cannot handle today's vision models; local VLM work needs a current-gen card. Reality: all eight video VLMs in the 2026-09-20 test, from Cosmos-Reason2-2B to a 30.8B-A3B mixture-of-experts, loaded and answered on one RTX 3090 (claims 3, 4, 6).
- Myth: The biggest model will be the slowest on old hardware. Reality: the largest by total parameters, InternVL3.5-30B-A3B at 30.8B-A3B, was the fastest decoder at 139.3 tok/s, because a mixture-of-experts activates only a slice of its weights per token (claims 5, 6).
- Myth: 24 GB means the card has no ceiling. Reality: 70B-class models do not fit even quantized to four or eight bit, and long-context KV caches eat what is left (claims 7, 8).

## Glossary
- **VLM (vision-language model)**: a language model that also reads images or video by turning them into tokens it can process.
- **video VLM**: a VLM tuned to answer questions about video clips, not just single images.
- **prefill**: the phase where the model reads your prompt (and the visual tokens) before it writes anything.
- **decode**: the phase where the model generates its answer, one token at a time.
- **tok/s (tokens per second)**: how many text chunks per second the model generates; faster feels snappier.
- **TTFT (time to first token)**: how long you wait after sending a prompt before the first word appears.
- **mixture-of-experts (MoE)**: a model that stores many specialist sub-networks but activates only a few per token, so total size and speed decouple; "30.8B-A3B" means 30.8B total parameters with about 3B active.
- **quantization (INT4, Q4)**: shrinking model weights to fewer bits so they fit in less memory, trading some accuracy for capacity.
- **VRAM**: the memory on the GPU itself; models must fit here to run fast.
- **KV cache**: the memory the model fills as a conversation or video gets longer; long context eats it.
- **concurrency 1**: one request at a time, no batching; the tester's stated setting.

## Unverified
- Per-model VRAM at rest or peak was not stated in the test post, so the brief carries no fetched number for it.
- Which two of the eight models produced output rejected in the final NIST/TREC submission is not named in the post text.
- Whether the 3090 was stock or power-tuned, and which inference runtime served each model, is not stated in the post.
- Used RTX 3090 prices outside the US market (ModelFit lists US references only).
- No fetched benchmark compares the 3090 against newer cards on vision workloads specifically; ModelFit's 104 vs 87 tok/s is a text-model estimate, not a VLM measurement.

## Suggested outline
1. Eight vision models, one five-year-old RTX 3090, nothing failed: the biggest one decoded at 139.3 tok/s.
2. The receipt: name the eight (Cosmos-Reason2-2B through InternVL3.5-30B-A3B at 30.8B-A3B), the decode spread of 13.8-139.3 tok/s at concurrency 1, and why the biggest model was the fastest (mixture-of-experts activates a slice per token).
3. The honest catch and the decision: first tokens wait up to 5.73 s, 70B-class weights and giant contexts still do not fit, but for vision the card stays, and a used one runs about $900.

## Viewer situation
You've got a five-year-old RTX 3090 with 24 gigs of VRAM sitting in a gaming PC you already own, and every upgrade video keeps telling you it's obsolete for AI.

## Has process
false

## Objection
One concurrency-1 anecdote whose author calls it "not a benchmark in any real sense" does not prove the card, and a 3090 still cannot hold 70B-class weights or long video contexts, so "runs vision" is not "runs everything".

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.reddit.com/r/LocalLLaMA/comments/1wkmzwi/how_fast_do_video_vlms_actually_run_on_a_3090_i/ | How fast do video VLMs actually run on a 3090? I measured 8 VLMs of different parameter sizes and architecture | benchmark | web_extract (pullpush.io mirror; preview.redd.it result-table images downloaded and read via OCR) | 2026-09-20 |
| 2 | https://www.reddit.com/r/LocalLLM/comments/1wkmfq8/prefilldecode_throughput_for_8_video_vlms_on_one/ | Prefill/decode throughput for 8 video VLMs on one 3090: 745-4,737 tok/s prefill, 13.8-139.3 decode | benchmark | web_extract (pullpush.io mirror) | 2026-09-20 |
| 3 | https://news.ycombinator.com/item?id=49772566 | Testing 8 VLMs on a single 3090 GPU | Hacker News | community | web_extract | 2026-09-20 |
| 4 | https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/ | 3090 & 3090 Ti Graphics Cards | NVIDIA GeForce | primary | web_extract | 2026-09-20 |
| 5 | https://www.theregister.com/on-prem/2024/08/23/old-rtx-3090-enough-to-serve-thousands-of-llm-users/1366649 | Benchmarks show even an old Nvidia RTX 3090 is enough to serve LLMs to thousands | The Register | docs | web_extract | 2026-09-20 |
| 6 | https://huggingface.co/OpenGVLab/InternVL3_5-30B-A3B | OpenGVLab/InternVL3_5-30B-A3B | Hugging Face model card | primary | web_extract | 2026-09-20 |
| 7 | https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct | Qwen/Qwen3-VL-8B-Instruct | Hugging Face model card | primary | web_extract | 2026-09-20 |
| 8 | https://huggingface.co/DAMO-NLP-SG/VideoLLaMA3-7B | DAMO-NLP-SG/VideoLLaMA3-7B | Hugging Face model card | primary | web_extract | 2026-09-20 |
| 9 | https://modelfit.io/gpu/rtx-3090/ | RTX 3090 24GB for Local LLMs: Runs 32B Q4, Used ~$900 | ModelFit | benchmark | web_extract | 2026-09-20 |

## Notes
Reddit blocks direct fetches (403), so the post and crosspost were read through the pullpush.io mirror, and the result tables are preview.redd.it images the agent downloaded and OCR'd; per-model numbers carry medium confidence for that reason, and the author's own crosspost title (plain text, no OCR) independently confirms the 745-4,737 prefill and 13.8-139.3 decode spans. The Task 1 table's top prefill OCRs as 4,745 tok/s while the author's title ceiling is 4,737 tok/s (the Task 2 figure); the brief quotes the author's title. The author's hedge ("This is not a benchmark in any real sense, but can be seen as an anecdotal reference") is the conflict the script must own in the honest-catch beat; keep the numbers attributed to the tester, not stated as lab results. TechPowerUp returned a bot-check page (no content), so GPU specs come from NVIDIA's own page plus The Register. The eighth model in the tables, LLaVA-Video-7B, decoded at 46.7-48.0 tok/s; its card was not fetched within budget, so it appears unnamed in claims. The post's method is shown (hardware, tasks, concurrency, TTFT definition), which is why it is tiered benchmark rather than community, but it is one tester's single card: the writer should say "one tester measured", never "benchmarks prove".
