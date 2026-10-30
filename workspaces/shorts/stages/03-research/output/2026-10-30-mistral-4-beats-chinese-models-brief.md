---
slug: 2026-10-30-mistral-4-beats-chinese-models
stage: 03-research
topic: "Mistral 4 beats Chinese models: run the receipt"
depth: standard
generated_at: 2026-10-30T11:36:34Z
sources: 9
hub: "[[videos/2026-10-30-mistral-4-beats-chinese-models]]"
---

# Research brief: Mistral 4 beats Chinese models: run the receipt

## Summary
The thesis: a CEO claim is not a benchmark, and on the morning the weights land the verifiable record reads tied on coding, ahead on cyber, behind on the overall index, and far too big for a home gaming PC. The most arresting number is the floor under the model: the smallest published quantization is 233 GB, so no 24 GB gaming GPU and not even a 128 GB machine can hold it. The strongest concrete case is Mistral's own model card printing an Artificial Analysis Intelligence Index score of 26 and stating in the next breath that "the leading open-weight models from China score higher on this aggregate index". What could not be verified: any measured local tokens-per-second on consumer hardware, and which Chinese models the CEO actually meant, because he named none. Conflict: the October 6 preview blog printed a Coding Agent Index of 49.8% ahead of DeepSeek V4 Pro 0813 and Qwen3.8 Max, while the October 29 model card prints 48% "effectively tied" with GLM-5.3; both are Mistral's own pages describing different checkpoints and comparison sets, so this brief carries the October 29 numbers as current.

## Thesis
"Mistral's CEO said Large 4 beats the Chinese models; the morning the weights land, the receipt reads tied on coding at 48%, ahead on cyber at 51%, behind on the overall index at 26 -- and at 233 GB for the smallest quant, it does not fit on your gaming PC."

## Explanation path
Start with the quote as a quote: on stage in Abu Dhabi the CEO said the new model is "above the Chinese models on certain aspects", and Reuters recorded that he named no model and no benchmark, so the claim was unfalsifiable for three weeks while only the API existed. Establish what a model card is: the vendor's own primary record published beside the weights, the first place a claim becomes checkable. Read the card the way an engineer would: it prints an independent aggregate score, 26 on the Artificial Analysis Intelligence Index, and admits the leading Chinese open-weight models score higher; the wins are per-task, coding tied at 48% with GLM-5.3 and cyber ahead at 51%. Before the hardware beat lands, the viewer needs the two halves of a Mixture-of-Experts model: about 1T parameters exist but only about 52B compute per token, and every expert still has to sit in memory. Then the consequence: the smallest official quant is 233 GB, so the claim "you can run this at home" narrows to machines most viewers do not own. Payoff: the habit, not the verdict -- when a CEO says "beats", ask which benchmark, which model, whose measurement, and at what memory.

## Claims
1. **Mistral's CEO claimed the new model beats Chinese models on October 6, 2026, without naming which models or benchmarks; the quote names "certain aspects, including cyber".**
   - Source: France's Mistral launches AI model it says outperforms some Chinese rivals, https://www.reuters.com/world/china/mistral-ceo-says-new-ai-model-beats-chinese-ones-some-areas-2026-10-06/
   - Tier: docs | Confidence: medium | Accessed: 2026-10-30 | Via: web_extract
   - Quote: "\"The model we're actually announcing today is actually above the Chinese models on certain aspects, including cyber. So the narrative that Europe cannot compete is something that is not true,\" CEO Artur Mensch said at a launch event in Abu Dhabi, without specifying which Chinese models or benchmarks he was referring to."
2. **Mistral's own model card states the architecture as "~1T total / ~52B active parameters", a Mixture-of-Experts with 128 routed experts of which 4 are active per token plus 1 shared expert, and a 1M token context window.**
   - Source: Mistral Large 4 - Le Chonk (model card), https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B
   - Tier: primary | Confidence: high | Accessed: 2026-10-30 | Via: web_extract
   - Quote: "~1T total / ~52B active parameters: granular Mixture-of-Experts with 128 routed experts (4 active per token) and 1 shared expert." and "1M context length, for long-context workloads."
3. **The model card itself prints an Artificial Analysis Intelligence Index v5 score of 26 and states that the leading Chinese open-weight models score higher on that aggregate index.**
   - Source: Mistral Large 4 - Le Chonk (model card), https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B
   - Tier: primary | Confidence: high | Accessed: 2026-10-30 | Via: web_extract
   - Quote: "On the Artificial Analysis Intelligence Index v5, Mistral Large 4 scores 26, the highest among western open-weight models. The leading open-weight models from China score higher on this aggregate index, but Mistral Large 4 is particularly strong on coding and cybersecurity"
4. **On coding the card prints 48% on the Artificial Analysis Coding Agent Index, "effectively tied" with the Chinese model GLM-5.3, while using 47% fewer tokens per task.**
   - Source: Mistral Large 4 - Le Chonk (model card), https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B
   - Tier: primary | Confidence: high | Accessed: 2026-10-30 | Via: web_extract
   - Quote: "On the Artificial Analysis Coding Agent Index, ML4 scores 48%, effectively tied with the leading open-weight model, GLM-5.3, while using 47% fewer tokens per task on average."
5. **Independent harness Artificial Analysis confirms the 26 score and lists the model at 1.1T total / 52B active parameters, with output speed of 161.3 tokens per second measured on Mistral's API, not local hardware.**
   - Source: Mistral Large 4 (high) - Intelligence, Performance & Price Analysis, https://artificialanalysis.ai/models/mistral-large-4
   - Tier: benchmark | Confidence: high | Accessed: 2026-10-30 | Via: web_extract
   - Quote: "Mistral Large 4 (High) scores 26 on the Artificial Analysis Intelligence Index, placing it above average among comparable models (median: 23)." and "Mistral Large 4 (High) generates output at 161.3 tokens per second (based on Mistral's API)"
6. **The open-weight release post claims the verifiable per-task win, cyber: 51% on the Artificial Analysis Cyber Index, alongside a 96.6% average refusal rate on malicious cyber requests.**
   - Source: Mistral Large 4 (Le Chonk) is now open weight, https://mistral.ai/news/mistral-large-4-oss/
   - Tier: primary | Confidence: high | Accessed: 2026-10-30 | Via: web_extract
   - Quote: "Mistral Large 4 scores 51% on the Artificial Analysis Cyber Index" and "achieving an average refusal rate of 96.6% on malicious cyber requests, the highest we measure among open models."
7. **The smallest published GGUF quantization is 233 GB (1-bit) needing a 256 GB RAM device; 2-bit runs 302-378 GB on 384-512 GB; near full precision Q8 is 1.1 TB on 1.2 TB+.**
   - Source: unsloth/Mistral-Large-4-1T-A52B-GGUF, https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-10-30 | Via: web_extract
   - Quote: "Run the smallest 1-bit (233 GB) on a 256GB RAM device, 2-bit (302-378 GB) on 384-512GB, or near full precision (Q8, 1.1 TB) on 1.2TB+."
8. **Transformers shipped day-one support in release v5.22.0 titled "Mistral Large 4 (Le Chonk)", published 29 Oct 14:15, the same day the weights landed.**
   - Source: Releases: huggingface/transformers, https://github.com/huggingface/transformers/releases
   - Tier: primary | Confidence: high | Accessed: 2026-10-30 | Via: web_extract
   - Quote: "v5.22.0: Mistral Large 4 (Le Chonk)" (release list entry; release page shows "released this 17 hours ago 29 Oct 14:15")

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | architecture, total vs active parameters | ~1T total / ~52B active parameters | https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B | "~1T total / ~52B active parameters: granular Mixture-of-Experts with 128 routed experts (4 active per token) and 1 shared expert." |
| 2 | Artificial Analysis Intelligence Index v5 score (model card) | 26 | https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B | "Mistral Large 4 scores 26, the highest among western open-weight models." |
| 3 | Artificial Analysis Coding Agent Index score | 48% | https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B | "ML4 scores 48%, effectively tied with the leading open-weight model, GLM-5.3" |
| 4 | token efficiency vs GLM-5.3 on coding tasks | 47% fewer tokens per task on average | https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B | "while using 47% fewer tokens per task on average" |
| 5 | Artificial Analysis Cyber Index score | 51% | https://mistral.ai/news/mistral-large-4-oss/ | "Mistral Large 4 scores 51% on the Artificial Analysis Cyber Index" |
| 6 | smallest 1-bit GGUF quant, whole model on disk | 233 GB | https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-GGUF | "Run the smallest 1-bit (233 GB) on a 256GB RAM device" |
| 7 | Q8 GGUF quant, whole model on disk | 1.1 TB | https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-GGUF | "near full precision (Q8, 1.1 TB) on 1.2TB+" |
| 8 | output throughput, Artificial Analysis measurement on Mistral's API | 161.3 tokens per second | https://artificialanalysis.ai/models/mistral-large-4 | "generates output at 161.3 tokens per second (based on Mistral's API)" |

## Analogy candidates
- **Title fight with three scorecards**: one benchmark is one judge's card, another judge scores it for the other side, and the CEO quote is the promoter's press conference, not the decision. Breaks when: a title fight still crowns one winner, while aggregate-vs-per-task benchmarks can both be true at once, so "beats" depends on which card you are shown.
- **All-star roster vs the eleven on the pitch**: about 1T parameters are the squad, about 52B active are who actually touches each token, and a bigger squad costs more to keep under contract. Breaks when: benched players cost nothing on match day, whereas every one of the 1T weights must sit in your RAM even though only ~52B compute per token.

## Misconceptions
- Myth: "Mistral 4 beats the Chinese models." Reality: Mistral's own model card says the leading Chinese open-weight models score higher on the aggregate Artificial Analysis Intelligence Index v5 than its 26; the honest version is per-task -- tied with GLM-5.3 on coding at 48%, ahead on cyber at 51% (claims 3, 4, 6).
- Myth: "If it's open weights, you can run it like you run Qwen." Reality: the smallest published GGUF is 233 GB at 1-bit, which does not fit a 24 GB gaming GPU or a 128 GB machine; open weights here means downloadable, not runnable at home (claim 7).

## Glossary
- **open weights**: the downloadable numbers a model is made of, so anyone can run it on their own hardware instead of renting access through the maker's API.
- **mixture of experts (MoE)**: an architecture that splits a model into many specialist sub-networks ("experts") and routes each token through only a few of them.
- **active parameters**: the slice of the model that actually computes for a given token, e.g. about 52B of about 1T total.
- **model card**: the document a vendor publishes beside the weights listing architecture, license, and benchmark scores; the primary record for any claim.
- **Artificial Analysis**: an independent benchmarking site that runs named harnesses across models and publishes scores like its Intelligence Index v5.
- **aggregate index**: one blended score built from many benchmarks, which can rank a model mid-pack even when it wins single tasks.
- **quantization**: shrinking model weights to fewer bits each so the file gets smaller, at some cost in quality.
- **GGUF**: the single-file format llama.cpp tools load, with size names like Q8_0 (8-bit) that tell you the bits and rough quality tier.

## Unverified
- No measured local tokens-per-second for Mistral Large 4 on consumer hardware existed as of the morning the weights landed; the only throughput number found is API-based, so any at-home speed figure is an expectation.
- Which Chinese models the CEO meant is unconfirmed: he named none, and GLM-5.3 is the leader named on the Coding Agent Index, not a confirmed referent of the quote.
- Whether the 1-bit 233 GB quant actually fits and runs within 256 GB once the KV cache at long context is added is unstated in the sources fetched.
- The CEO quote is verified only through Reuters' text; no video transcript was fetched.

## Suggested outline
1. The quote with nothing under it: "above the Chinese models on certain aspects", no model named, no benchmark named, and for three weeks nobody outside Mistral could check.
2. Run the receipt on the model card's own numbers: Intelligence Index 26 with Chinese open-weight leaders above it, coding tied at 48% with GLM-5.3, cyber won at 51% -- "beats" is true per-task and false overall.
3. What "open weights" costs you: about 1T total with ~52B active means every expert sits in memory; 233 GB at 1-bit, 1.1 TB at Q8, so no 24 GB GPU and no 128 GB Mac -- and next time a CEO says "beats", ask which benchmark, which model, whose measurement.

## Viewer situation
You have a gaming PC or a Mac, you saw the headline that a French model beats the Chinese ones, and you have never opened a model card to check a claim like that yourself.

## Has process
false

## Objection
An aggregate index is itself just a weighted bucket of someone's chosen benchmarks, so trading the 26 for a per-task 51% is cherry-picking in the opposite direction.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.reuters.com/world/china/mistral-ceo-says-new-ai-model-beats-chinese-ones-some-areas-2026-10-06/ | France's Mistral launches AI model it says outperforms some Chinese rivals (Reuters) | docs | web_extract | 2026-10-30 |
| 2 | https://www.reuters.com/legal/litigation/mistral-ai-publicly-releases-large-4-targets-cybersecurity-users-2026-10-29/ | Mistral AI publicly releases Large 4, targets cybersecurity users (Reuters) | docs | web_extract | 2026-10-30 |
| 3 | https://mistral.ai/news/mistral-large-4/ | Introducing Mistral Large 4 (preview, Oct 6) | primary | web_extract | 2026-10-30 |
| 4 | https://mistral.ai/news/mistral-large-4-oss/ | Mistral Large 4 (Le Chonk) is now open weight (Oct 29) | primary | web_extract | 2026-10-30 |
| 5 | https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B | Mistral Large 4 - Le Chonk (model card) | primary | web_extract | 2026-10-30 |
| 6 | https://huggingface.co/blog/mistral-large4 | Welcome Le Chonk: Mistral Large 4 on Hugging Face (Oct 29) | docs | web_extract | 2026-10-30 |
| 7 | https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-GGUF | unsloth/Mistral-Large-4-1T-A52B-GGUF | primary | web_extract | 2026-10-30 |
| 8 | https://artificialanalysis.ai/models/mistral-large-4 | Mistral Large 4 (high) - Intelligence, Performance & Price Analysis | benchmark | web_extract | 2026-10-30 |
| 9 | https://github.com/huggingface/transformers/releases | Releases: huggingface/transformers (v5.22.0) | primary | web_extract | 2026-10-30 |

## Notes
Conflicts, recorded not averaged: the October 6 preview blog prints "combined Coding Agent Index score of 49.8%" ahead of DeepSeek V4 Pro 0813 and Qwen3.8 Max, while the October 29 model card and OSS post print 48% "effectively tied" with GLM-5.3; these describe different checkpoints (three more weeks of reinforcement learning) and different comparison sets, and the October 29 figures are treated as current. Artificial Analysis lists total parameters as 1.1T where the model card says ~1T; both are kept verbatim, each attributed. Thin spot: most benchmark numbers on the model card are vendor-cited even when the harness is named; the only independently measured page fetched is Artificial Analysis, and its 161.3 tokens-per-second is API-based, not local. Reuters spells the CEO "Artur Mensch" (Oct 6 story) and "Arthur Mensch" (Oct 29 story); each quote keeps its own story's spelling.

## Decisions
- checkpoint: angle restated as "CEO quote vs verifiable numbers on the morning the weights land"; slug 2026-10-30-mistral-4-beats-chinese-models confirmed; continued unattended.
- thesis chosen: the tied/ahead/behind split plus the 233 GB memory floor, because each element sits on a tier 1 or tier 3 page fetched today and together they make "run the receipt" a demonstrable habit instead of an opinion about Mistral.
