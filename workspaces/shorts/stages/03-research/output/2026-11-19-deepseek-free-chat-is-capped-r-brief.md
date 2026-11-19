---
slug: 2026-11-19-deepseek-free-chat-is-capped-r
stage: 03-research
topic: "DeepSeek capped its free chat: run the open weights locally instead"
depth: standard
generated_at: 2026-11-19T12:38:47Z
sources: 12
hub: "[[videos/2026-11-19-deepseek-free-chat-is-capped-r]]"
---

# Research brief: DeepSeek free chat is capped: run the weights instead

## Summary
This week DeepSeek's free app and web chat hit limits users cannot pay past: no published rules, no subscription, just in-app notices. The most arresting number is the smallest one on the page: 8.99 GB, the Q4_K_M GGUF download that puts a DeepSeek R1 distill on a 16 GB gaming PC tonight, in LM Studio or with one Ollama command. The strongest concrete case is the 14B distill itself -- a 9 GB file, 128k context, unmetered, MIT-licensed. What could not be verified: the exact daily message count and whether the caps hit every account the same way. Sources conflict on the inactivity cutoff: notices said more than seven days, some users reported 72 hours, and reset times vary by account.

## Thesis
DeepSeek capped its free chat because its compute ran short, but the weights it already open-sourced run on your gaming PC tonight with no quota, no key and no bill.

## Explanation path
Open on the thing that changed: between November 15 and 16, 2026, the free app and website began refusing work they used to do -- long conversations inactive for more than seven days could no longer be resumed, single prompts were capped at around 40,000 Chinese characters, and a usage-limit notice appeared when the day's quota ran out, for some accounts in less than two hours of continuous chatting. Establish why before any fix: the notices blame insufficient computing capacity, and the load is record-setting -- 59.2 trillion tokens in one week on this exact model, first in the world -- so waiting it out or paying is not currently an option; there is no paid consumer tier, and the API that serves the same model is billed per token. Then the reframe: DeepSeek also gives its models away as weights, MIT-licensed, and has for a long time -- the 671B R1 plus six distills from 1.5B to 70B. Land the consequence on the viewer's hardware: a GGUF at Q4_K_M is 8.99 GB for the 14B distill and 19.9 GB for the 32B, sizes a 16 or 24 GB gaming PC already handles, loadable tonight in LM Studio or with a single Ollama command. Close honest: a distill is a student of the big model, not the big model -- and the current chat model's own open weights are a 552B-backbone project no gaming PC is running this week.

## Claims
1. **Between November 15 and 16, 2026, DeepSeek's free app and web chat began enforcing usage caps: long conversations inactive for more than seven days could no longer be resumed, single prompts were capped at around 40,000 Chinese characters, and a usage-limit message appeared at the daily quota.**
   - Source: DeepSeek users report chat limits as the service cites capacity constraints, https://technode.com/2026/11/16/deepseek-users-report-chat-limits-as-the-service-cites-capacity-constraints/
   - Tier: docs | Confidence: high | Accessed: 2026-11-19 | Via: web_extract
   - Quote: "Some received a notice saying that long conversations inactive for more than seven days could no longer be resumed because of insufficient computing capacity. Users also reported that individual prompts were capped at around 40,000 Chinese characters and that the service displayed a usage-limit message when they reached their daily quota."
2. **Product notifications blamed insufficient computing capacity, some users hit the daily-quota notice after less than two hours of continuous chatting, and DeepSeek currently offers no paid option for the consumer app.**
   - Source: Yicai: DeepSeek starts limiting free usage, https://www.yicai.com/news/103441951.html
   - Tier: docs | Confidence: high | Accessed: 2026-11-19 | Via: web_extract
   - Quote: "部分用户甚至在使用不到两小时后，就收到了额度耗尽的提示。"
3. **In the week of November 9 to 15, DeepSeek V4.1 Flash 1017 handled 59.2万亿 tokens (59.2 trillion tokens), the most of any model globally according to OpenRouter data cited by Yicai.**
   - Source: Yicai: DeepSeek starts limiting free usage, https://www.yicai.com/news/103441951.html
   - Tier: docs | Confidence: medium | Accessed: 2026-11-19 | Via: web_extract
   - Quote: "在11月9日至11月15日这一周，DeepSeek V4.1 Flash 1017完成59.2万亿Token调用，居全球首位。"
4. **The model behind the official web and app chat is DeepSeek-V4.1-Flash-1017, served on the API as deepseek-flash with a 1M-token context.**
   - Source: Change Log, DeepSeek API Docs, https://api-docs.deepseek.com/updates/
   - Tier: primary | Confidence: high | Accessed: 2026-11-19 | Via: web_extract
   - Quote: "DeepSeek V4.1 Flash has been upgraded to DeepSeek-V4.1-Flash-1017. The official web and APP models have also been updated to the new version."
5. **On the paid API, that same model bills $0.15 per 1M input tokens (cache miss, off-peak) and $0.6 per 1M output tokens (off-peak), with peak rates double.**
   - Source: Models & Pricing, DeepSeek API Docs, https://api-docs.deepseek.com/quick_start/pricing
   - Tier: primary | Confidence: high | Accessed: 2026-11-19 | Via: web_extract
   - Quote: "1M INPUT TOKENS (CACHE MISS) OFF-PEAK $0.15 / PEAK $0.3; 1M OUTPUT TOKENS OFF-PEAK $0.6 / PEAK $1.2 (deepseek-flash column)"
6. **DeepSeek publishes open weights: the R1 model card lists DeepSeek-R1 at 671B total and 37B activated parameters with 128K context, plus six distilled checkpoints from 1.5B to 70B, under MIT license.**
   - Source: deepseek-ai/DeepSeek-R1, https://huggingface.co/deepseek-ai/DeepSeek-R1
   - Tier: primary | Confidence: high | Accessed: 2026-11-19 | Via: web_extract
   - Quote: "We open-source distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series to the community."
7. **The DeepSeek-R1-Distill-Qwen-14B GGUF downloads 8.99 GB at Q4_K_M (7.92 GB at Q3_K_L) and supports 128k context.**
   - Source: lmstudio-community/DeepSeek-R1-Distill-Qwen-14B-GGUF, https://huggingface.co/lmstudio-community/DeepSeek-R1-Distill-Qwen-14B-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-11-19 | Via: web_extract
   - Quote: "4-bit Q4_K_M 8.99 GB; 3-bit Q3_K_L 7.92 GB; Supports context length of 128k."
8. **The 32B distill GGUF downloads 19.9 GB at Q4_K_M (17.2 GB at Q3_K_L), the realistic ceiling for a 24 GB machine.**
   - Source: lmstudio-community/DeepSeek-R1-Distill-Qwen-32B-GGUF, https://huggingface.co/lmstudio-community/DeepSeek-R1-Distill-Qwen-32B-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-11-19 | Via: web_extract
   - Quote: "4-bit Q4_K_M 19.9 GB; 3-bit Q3_K_L 17.2 GB"
9. **Ollama ships the same distills as one-command pulls with a 128K context window: deepseek-r1:7b is 4.7GB, deepseek-r1:14b is 9.0GB, deepseek-r1:32b is 20GB.**
   - Source: deepseek-r1, Ollama Library, https://ollama.com/library/deepseek-r1
   - Tier: docs | Confidence: high | Accessed: 2026-11-19 | Via: web_extract
   - Quote: "deepseek-r1:7b 4.7GB 128K; deepseek-r1:14b 9.0GB 128K; deepseek-r1:32b 20GB 128K"
10. **LM Studio's own guidance: with 16GB of RAM you can run the 7B or 8B distills; the full 671B model needs roughly 192GB or more.**
    - Source: DeepSeek R1: open source reasoning model, LM Studio Blog, https://lmstudio.ai/blog/deepseek-r1
    - Tier: docs | Confidence: high | Accessed: 2026-11-19 | Via: web_extract
    - Quote: "if you have 16GB of RAM, you can run the 7B or 8B parameter distilled models. If you have ~192GB+ of RAM, you can run the full 671B parameter model."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | single-input cap, free chat | around 40,000 Chinese characters | https://technode.com/2026/11/16/deepseek-users-report-chat-limits-as-the-service-cites-capacity-constraints/ | "individual prompts were capped at around 40,000 Chinese characters" |
| 2 | long-conversation inactivity cutoff | more than seven days | https://technode.com/2026/11/16/deepseek-users-report-chat-limits-as-the-service-cites-capacity-constraints/ | "long conversations inactive for more than seven days could no longer be resumed" |
| 3 | continuous use before daily-quota notice, some users | less than two hours (不到两小时) | https://www.yicai.com/news/103441951.html | "在使用不到两小时后，就收到了额度耗尽的提示" |
| 4 | weekly token volume, DeepSeek V4.1 Flash 1017, week of Nov 9-15 | 59.2万亿 Token (59.2 trillion tokens) | https://www.yicai.com/news/103441951.html | "完成59.2万亿Token调用，居全球首位" |
| 5 | deepseek-flash API input price, cache miss, off-peak | $0.15 per 1M tokens | https://api-docs.deepseek.com/quick_start/pricing | "1M INPUT TOKENS (CACHE MISS) OFF-PEAK $0.15" |
| 6 | deepseek-flash API output price, off-peak | $0.6 per 1M tokens | https://api-docs.deepseek.com/quick_start/pricing | "1M OUTPUT TOKENS OFF-PEAK $0.6" |
| 7 | DeepSeek-R1-Distill-Qwen-14B GGUF at Q4_K_M | 8.99 GB | https://huggingface.co/lmstudio-community/DeepSeek-R1-Distill-Qwen-14B-GGUF | "4-bit Q4_K_M 8.99 GB" |
| 8 | DeepSeek-R1-Distill-Qwen-32B GGUF at Q4_K_M | 19.9 GB | https://huggingface.co/lmstudio-community/DeepSeek-R1-Distill-Qwen-32B-GGUF | "4-bit Q4_K_M 19.9 GB" |

## Analogy candidates
- **All-you-can-eat buffet installing a ticket machine while giving away the cookbook**: the hosted chat is the restaurant, someone else's GPUs with portions rationed when the kitchen overheats; the open weights are the cookbook plus your own stove (the gaming PC), where nobody counts your plates. Breaks when: a cookbook copies for free and cooks identically, while a 9 GB distill is a real download that cooks a smaller menu than the 671B chef, and your stove size caps which recipes fit at all.
- **Gym installing a turnstile vs taking the barbell home**: the cap is the gym limiting visits during a capacity crunch; the weights are the barbell you take home and lift whenever you like. Breaks when: a barbell taken home lifts exactly the same as the gym's, but a local distill is a lighter barbell than the one the hosted chat uses.

## Misconceptions
- Myth: DeepSeek started charging everyone or broke entirely. Reality: the free chat got caps whose notices cite insufficient computing capacity, and as of November 17 no paid consumer tier exists to remove them (claims 1, 2).
- Myth: If the chat is capped, DeepSeek is off the table. Reality: the R1 weights and its six distills are MIT-licensed downloads that run unmetered on your own GPU (claims 6, 7, 9).
- Myth: Running DeepSeek locally means running the same model you chatted with. Reality: on 16 to 24 GB you run a 14B or 32B distill trained to imitate R1, not the 671B original, which needs roughly 192GB+ of RAM (claims 6, 10).

## Glossary
- **GGUF**: a single packaged file of model weights that runtimes like LM Studio, Ollama and llama.cpp load directly.
- **Quantization (Q4_K_M)**: shrinking weights to about 4 bits each to cut file size and memory use, at a small accuracy cost.
- **Distill**: a smaller open model (Qwen or Llama) fine-tuned on a big model's outputs to imitate it at a fraction of the size.
- **Usage quota**: DeepSeek's server-side allowance of free chat turns, enforced per account and shown as a usage-limit message.

## Unverified
- Whether the caps apply identically to every account; reports vary and DeepSeek has published no unified rules.
- The exact daily message count; no fetched page states one, only per-account reset times.
- A 72-hour inactivity cutoff some users described, alongside the seven-day notices.
- Tokens per second for the 14B or 32B distill on a 16-24 GB gaming GPU; this needs our own measurement before the script cites a speed.
- Press speculation that a paid consumer subscription is coming, based on Coding Plan strings reportedly found in the web front-end; nothing official.

## Suggested outline
1. Open on the notice: usage limit reached, old chats locked after more than seven days inactive, inputs capped around 40,000 Chinese characters -- and no paid tier to escape it.
2. Explain the squeeze: record load of 59.2万亿 tokens in a week against insufficient computing capacity, and the per-token API is the only official way to pay ($0.15 in, $0.6 out per 1M, off-peak).
3. Land the move: the weights are already free -- 8.99 GB for the 14B distill, 19.9 GB for the 32B, one command in Ollama or a search in LM Studio -- and be honest that a distill is the student, not the 671B teacher.

## Viewer situation
You use DeepSeek's free app or website for long chats, this week it started telling you the usage limit was reached, and the gaming PC next to you has 16 to 24 GB of memory doing nothing about it.

## Has process
true
- Install LM Studio from lmstudio.ai (or Ollama from ollama.com) on the gaming PC.
- Search the model catalog for DeepSeek-R1-Distill-Qwen-14B GGUF.
- Pick Q4_K_M: 8.99 GB fits 16 GB; pick the 32B at 19.9 GB if you have 24 GB.
- Download, load the model in the chat tab, and ask away with no quota and no API key.
- Or open a terminal and run ollama run deepseek-r1:14b (9.0GB).

## Objection
A 14B distill is not the 671B DeepSeek you were talking to, and the current chat model's own open weights (V4.1-Flash, 552B backbone parameters) are nowhere near a gaming PC -- local means a smaller student model, and nobody has measured its speed on my card.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://offloop.org/learn/deepseek-usage-limit | DeepSeek Adds Free Chat Limits. Here's How to Keep Chatting | docs | web_extract | 2026-11-19 |
| 2 | https://technode.com/2026/11/16/deepseek-users-report-chat-limits-as-the-service-cites-capacity-constraints/ | DeepSeek users report chat limits as the service cites capacity constraints | docs | web_extract | 2026-11-19 |
| 3 | https://www.yicai.com/news/103441951.html | 调用量冲上全球第一，DeepSeek开始对免费用户"限额"了 (Yicai) | docs | web_extract | 2026-11-19 |
| 4 | https://api-docs.deepseek.com/quick_start/pricing | Models & Pricing, DeepSeek API Docs | primary | web_extract | 2026-11-19 |
| 5 | https://api-docs.deepseek.com/updates/ | Change Log, DeepSeek API Docs | primary | web_extract | 2026-11-19 |
| 6 | https://huggingface.co/deepseek-ai | deepseek-ai org page, Hugging Face | primary | web_extract | 2026-11-19 |
| 7 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | deepseek-ai/DeepSeek-V4.1-Flash model card | primary | web_extract | 2026-11-19 |
| 8 | https://huggingface.co/deepseek-ai/DeepSeek-R1 | deepseek-ai/DeepSeek-R1 model card | primary | web_extract | 2026-11-19 |
| 9 | https://huggingface.co/lmstudio-community/DeepSeek-R1-Distill-Qwen-14B-GGUF | lmstudio-community/DeepSeek-R1-Distill-Qwen-14B-GGUF | primary | web_extract | 2026-11-19 |
| 10 | https://huggingface.co/lmstudio-community/DeepSeek-R1-Distill-Qwen-32B-GGUF | lmstudio-community/DeepSeek-R1-Distill-Qwen-32B-GGUF | primary | web_extract | 2026-11-19 |
| 11 | https://ollama.com/library/deepseek-r1 | deepseek-r1, Ollama Library | docs | web_extract | 2026-11-19 |
| 12 | https://lmstudio.ai/blog/deepseek-r1 | DeepSeek R1: open source reasoning model, LM Studio Blog | docs | web_extract | 2026-11-19 |

## Notes
No DeepSeek page states the caps. The official API change log's latest entry (2026-11-13) covers the new application APIs and an open-source demo chat client that imports your exported chat history -- but that client runs on the paid API, so continuing a rescued conversation bills per token. Conflict on the inactivity cutoff: seven-day notices (TechNode, Yicai) versus 72-hour user reports (Yicai); treat both as reported, not universal. The current chat model's own weights are open (DeepSeek-V4.1-Flash, 552B backbone parameters, 8B activated per token during prefill and 16B during decode), but the model card states the release does not include a Jinja-format chat template and points to a local inference folder for weight conversion -- not a tonight project, which is why the distills carry the how-to. Thin spots: no first-party tokens-per-second on consumer GPUs, and the exact quota mechanics are unpublished. Trust Yicai and TechNode over aggregator rewrites for the event details; both are dated, bylined, and cite the product notifications.
