---
slug: 2026-10-09-ecosia-ditched-mistral-for-chi
stage: 03-research
topic: "Ecosia ditched Mistral for Chinese open weights: what it proves"
depth: standard
generated_at: 2026-10-09T11:38:07Z
sources: 12
hub: "[[videos/2026-10-09-ecosia-ditched-mistral-for-chi]]"
---

# Research brief: Ecosia ditched Mistral for Chinese open weights: what it proves

## Summary
The thesis lands as a myth-bust: the "hobby" weights just kept a real paying customer, a search engine used by public services, so open weights stopped being a tinkerer's lane the moment a bill-paying European product moved onto them. The most arresting number is CEO Christian Kroll's claim that the switch "roughly cut our costs in half while improving quality and performance." The strongest concrete case is Ecosia routing production search AI through the German host Melious onto Z.ai's GLM family, whose model cards anyone can open and whose smaller siblings a home viewer can download tonight. What could not be verified: no fetched page names which exact model now answers which Ecosia feature, nor whether the flip from Mistral is fully live in production. Conflict to handle on camera: POLITICO frames the move as betting on Chinese AI while Kroll insists it is about open models and price, not country of origin, and Z.ai's own card prints 320B total parameters in prose where the Hugging Face sidebar prints 321B params.

## Thesis
When Europe's climate search engine had to choose between the French AI champion and Chinese open weights, the open weights kept the paying customer, which is proof that downloadable models graduated from hobby to infrastructure.

## Explanation path
Start with the event as news: a Berlin search engine that built its brand on European independence has publicly dropped Europe's flagship AI lab, calling its models disappointing and a year behind. Establish what Ecosia actually pays for: answers at scale, not a model, which is why quality lag and cost are the two levers that forced the move, and why a roughly halved bill while quality improved is the sentence that stings Mistral. Introduce open weights as the thing that changed the deal: downloadable parameter files that anyone can serve, which is what let Ecosia reroute its traffic to Melious, a European platform that only runs models whose weights are public. Name the models that now carry a paying European product, Z.ai's GLM above all, with concrete sizes from the cards themselves, 753B params for GLM-5.3 and 320B total with just 18B active for GLM-5.3-Flash, and the ranking that made the choice rational: on Artificial Analysis's open-model table Mistral's Large 4 preview sits eighth and every model ahead of it is Chinese, and even Mistral's own platform now hosts GLM 5.3. Then land the reframe for the home viewer: the same family of weights a search engine pays to serve millions is pullable tonight, and the 30B-class GLM-4.7-Flash is a 19GB Ollama download with a 198K context window. Close on the honest catch: Ecosia rents European servers rather than running the weights at home, and open weights do not scrub training-data bias, they only change who is allowed to run and inspect the model.

## Claims
1. **Ecosia told POLITICO it is dropping its French AI partner Mistral, which it had chosen over OpenAI in May, because it is disappointed with the quality of models it calls a year behind the competition.**
   - Source: German search engine ditches Mistral, bets on Chinese open-source AI - POLITICO, https://www.politico.eu/article/germany-ecosia-search-engine-mistral-china-open-source-ai/
   - Tier: docs | Confidence: high | Accessed: 2026-10-09 | Via: web_extract
   - Quote: "We are disappointed with the quality of Mistral," Ecosia founder and CEO Christian Kroll said in an interview, stating that the models from France's flagship AI lab are now "a year behind" the competition. / "In May, it replaced the American giant OpenAI with Mistral as its AI provider."
2. **Moving its AI onto open-weight models through Melious roughly cut Ecosia's costs in half while quality and performance improved, according to CEO Christian Kroll.**
   - Source: German search engine ditches Mistral, bets on Chinese open-source AI - POLITICO, https://www.politico.eu/article/germany-ecosia-search-engine-mistral-china-open-source-ai/
   - Tier: docs | Confidence: high | Accessed: 2026-10-09 | Via: web_extract
   - Quote: "We've roughly cut our costs in half while improving quality and performance," Kroll said.
3. **Ecosia's own help center, last updated October 2, 2026, says its AI Overviews run on Mistral small 3.2 and its AI Chat on Mistral small 4, with alternative models under continuous exploration.**
   - Source: Generative AI on Ecosia Search - Ecosia Help Center, https://support.ecosia.org/article/1006-ai-search
   - Tier: primary | Confidence: high | Accessed: 2026-10-09 | Via: web_extract
   - Quote: "Currently, for AI Overviews we use Mistral small 3.2; for AI Chat we currently use Mistral small 4."
4. **Founder Christian Kroll says the move is about open models rather than their country of origin, naming Melious as a European company offering affordable AI inference powered by green electricity.**
   - Source: EXCLUSIVE: Ecosia founder clarifies move away from Mistral - It's about open models, not China - EU-Startups, https://www.eu-startups.com/2026/10/ecosia-founder-clarifies-move-away-from-mistral-its-about-open-models-not-china/
   - Tier: docs | Confidence: high | Accessed: 2026-10-09 | Via: web_extract
   - Quote: "We'll probably be using Melious.ai in future. Unlike Mistral, this is a European company that offers high-quality, affordable AI inference powered by green electricity," shared Christian in an exclusive interview.
5. **Melious, the platform Ecosia is partnering with, serves only open-weight models, and every model in its catalog has publicly downloadable weights across families including Qwen, GLM, DeepSeek, Kimi, Mistral and Llama.**
   - Source: Models - Melious, https://melious.ai/docs/concepts/models
   - Tier: primary | Confidence: high | Accessed: 2026-10-09 | Via: web_extract
   - Quote: "Every model we serve has publicly downloadable weights." Qwen, GLM, DeepSeek, Kimi, Mistral, Llama, FLUX, Whisper, Voxtral, and the rest.
6. **Z.ai's GLM-5.3-Flash model card lists 320B total parameters and just 18B active parameters, and says the model outperforms GLM-5.2 at one-tenth the price.**
   - Source: zai-org/GLM-5.3-Flash - Hugging Face, https://huggingface.co/zai-org/GLM-5.3-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-10-09 | Via: web_extract
   - Quote: "With 320B total parameters and just 18B active parameters, it outperforms GLM-5.2 across benchmarks and real-world workloads at one-tenth the price, while approaching Claude Opus 4.8 on coding and agentic benchmarks."
7. **Z.ai's GLM-5.3 model card lists a model size of 753B params and claims GLM-5.3 is the most capable open-weights model for coding, with a 50% improvement over GLM-5.2 on the in-house Z.ai Code Bench.**
   - Source: zai-org/GLM-5.3 - Hugging Face, https://huggingface.co/zai-org/GLM-5.3
   - Tier: primary | Confidence: high | Accessed: 2026-10-09 | Via: web_extract
   - Quote: "Stronger Coding: GLM-5.3 is the most capable open-weights model for coding, with a 50% improvement over GLM-5.2 on our in-house Z.ai Code Bench."
8. **The GLM family is already a home download: Ollama's library page for GLM-4.7-Flash, a 30B-A3B mixture-of-experts model, lists a 19GB q4_K_M build with a 198K context window.**
   - Source: glm-4.7-flash - Ollama, https://ollama.com/library/glm-4.7-flash
   - Tier: primary | Confidence: high | Accessed: 2026-10-09 | Via: web_extract
   - Quote: "GLM-4.7-Flash is a 30B-A3B MoE model." / "19GB · 198K context window · Text"
9. **On the Artificial Analysis-informed open-model ranking, Mistral's new Large 4 preview scores 38.4 on the Intelligence Index, placing it eighth, with all seven models ahead of it Chinese and Xiaomi's MiMo-V2.6-Pro at 46.3.**
   - Source: Search Engine Ecosia Swaps Mistral for Chinese A.I. - Trending Topics, https://www.trendingtopics.eu/ecosia-mistral-chinese-ai/
   - Tier: docs | Confidence: medium | Accessed: 2026-10-09 | Via: web_extract
   - Quote: "In the ranking of open models, Large 4 comes in eighth, and all seven models ahead of it are from China:" (table rows: "MiMo-V2.6-Pro | Xiaomi | 46.3" and "Mistral Large 4 (Preview) | Mistral | 38.4")
10. **Mistral itself now hosts Z.ai's GLM 5.3 on its own platform, meaning the French champion sells the very Chinese open weights Ecosia switched to.**
    - Source: Search Engine Ecosia Swaps Mistral for Chinese A.I. - Trending Topics, https://www.trendingtopics.eu/ecosia-mistral-chinese-ai/
    - Tier: docs | Confidence: medium | Accessed: 2026-10-09 | Via: web_extract
    - Quote: "In other words, Mistral offers its customers the very Chinese A.I. that Ecosia has now switched to."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Ecosia's AI cost change after the switch (CEO statement) | roughly cut our costs in half (about a 50% cost reduction) | https://www.politico.eu/article/germany-ecosia-search-engine-mistral-china-open-source-ai/ | "We've roughly cut our costs in half while improving quality and performance," Kroll said. |
| 2 | GLM-5.3 total parameters (Hugging Face model card) | 753B params | https://huggingface.co/zai-org/GLM-5.3 | "Model size 753B params" |
| 3 | GLM-5.3-Flash parameters, total and active | 320B total parameters and just 18B active parameters | https://huggingface.co/zai-org/GLM-5.3-Flash | "With 320B total parameters and just 18B active parameters, it outperforms GLM-5.2" |
| 4 | GLM-4.7-Flash download size and context via Ollama (q4_K_M) | 19GB · 198K context window | https://ollama.com/library/glm-4.7-flash | "19GB · 198K context window · Text" |
| 5 | Mistral Large 4 (Preview) Artificial Analysis Intelligence Index | 38.4 points | https://www.trendingtopics.eu/ecosia-mistral-chinese-ai/ | "Mistral Large 4 (Preview) | Mistral | 38.4" |
| 6 | MiMo-V2.6-Pro (top Chinese open model) Artificial Analysis Intelligence Index | 46.3 (Intelligence Index points) | https://www.trendingtopics.eu/ecosia-mistral-chinese-ai/ | "MiMo-V2.6-Pro | Xiaomi | 46.3" |
| 7 | Ecosia scale, users and trees planted (Ecosia's own page, 2021 figures) | 15 million users have planted over 120 million trees | https://blog.ecosia.org/ecosia-search-engine/ | "Our 15 million users have planted over 120 million trees, for free." |

## Analogy candidates
- **Published cookbook vs. restaurant meals**: A closed model is a restaurant: you pay per meal and the kitchen stays shut. Open weights are a published cookbook: Ecosia stopped buying meals from the French restaurant and hired a kitchen (Melious) that cooks from the Chinese-published books, at roughly half the catering bill, and a home cook can buy the same book tonight. Breaks when: a cookbook is not a meal, you still need a stove and skill to serve it (GPUs, serving software), and the dish tasting good depends on the cook, not just the recipe.

## Misconceptions
- Myth: Open-weight models are a hobby for tinkerers, nothing a real business would pay for. Reality: a paying European search engine serving millions of users just moved its production AI onto open weights and says it roughly cut costs in half doing it (claims 1 and 2).
- Myth: A European company choosing Chinese open weights betrays the EU sovereign-AI project. Reality: Ecosia's founder says the choice is about open models and price, not country of origin, and even Mistral's own platform now hosts Z.ai's GLM 5.3 (claims 4 and 10).

## Glossary
- **open weights**: A model whose learned parameter files anyone can download, inspect and run, versus a closed model reachable only through a vendor's paid API.
- **Mistral**: France's flagship AI lab and Europe's best-funded model developer, the vendor Ecosia dropped.
- **GLM**: Z.ai's family of Chinese open-weight models, including GLM-5.3 and GLM-5.3-Flash.
- **Melious**: A German inference platform that serves only open-weight models on servers inside the EU.
- **inference**: Running a trained model to produce answers, the thing you either buy per request or run on your own hardware.
- **mixture-of-experts (MoE)**: A model design where only a small slice of the total parameters fires on each token, so a very large model can run surprisingly cheaply.
- **quantization (q4_K_M)**: Shrinking a model file to fewer bits so it fits in ordinary VRAM or RAM, trading a little quality for a much smaller download.
- **context window**: How much text a model can hold in mind at once, measured in tokens.

## Unverified
- No page fetched this session names which exact model now powers each Ecosia feature after the switch.
- Whether Ecosia's AI Chat has fully flipped to the new open-weight setup in production or still runs Mistral small 4 for some users.
- Tokens-per-second and memory footprint for GLM-4.7-Flash on a viewer's specific GPU, which our own hardware has not measured.
- Whether Mistral's Large 4 weights actually ship on October 27 as reported by Cybernews, since only pre-release statements exist.
- Community chatter framing the switch as a win for local AI, which is Reddit sentiment and not a verified claim.

## Suggested outline
1. Ecosia, the Berlin search engine built on European independence, dumps Mistral and says the quiet part: the models are a year behind, and switching to open weights roughly cut costs in half.
2. What open weights are and why China owns the top of the board: GLM-5.3 at 753B params, GLM-5.3-Flash at 320B total with 18B active, Mistral's Large 4 preview eighth with every model ahead of it Chinese, and even Mistral hosting GLM 5.3.
3. The reframe for the home viewer: the weights a paying European company just bet on are pullable tonight, GLM-4.7-Flash at a 19GB Ollama download, with the honest catch that Ecosia rents servers and open weights do not remove bias.

## Viewer situation
You run AI at home on a gaming PC or a Mac, you have pulled a model with Ollama before, and you keep hearing that open-weight models are toys next to the big closed APIs.

## Has process
false

## Objection
Ecosia did not run anything locally: it swapped one hosted API for another hosted API, so a European middleman serving Chinese weights proves routing flexibility and price pressure, not that open weights beat closed ones on merit.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.politico.eu/article/germany-ecosia-search-engine-mistral-china-open-source-ai/ | German search engine ditches Mistral, bets on Chinese open-source AI - POLITICO | docs | web_extract | 2026-10-09 |
| 2 | https://www.eu-startups.com/2026/10/ecosia-founder-clarifies-move-away-from-mistral-its-about-open-models-not-china/ | EXCLUSIVE: Ecosia founder clarifies move away from Mistral - It's about open models, not China - EU-Startups | docs | web_extract | 2026-10-09 |
| 3 | https://www.trendingtopics.eu/ecosia-mistral-chinese-ai/ | Search Engine Ecosia Swaps Mistral for Chinese A.I. - Trending Topics | docs | web_extract | 2026-10-09 |
| 4 | https://cybernews.com/ai-news/ecosia-drops-mistral/ | Ecosia drops Mistral, eyes Chinese open-weight AI models - Cybernews | docs | web_extract | 2026-10-09 |
| 5 | https://support.ecosia.org/article/1006-ai-search | Generative AI on Ecosia Search - Ecosia Help Center | primary | web_extract | 2026-10-09 |
| 6 | https://melious.ai/docs/concepts/models | Models - Melious | primary | web_extract | 2026-10-09 |
| 7 | https://melious.ai/products/inference | Inference API - Melious | primary | web_extract | 2026-10-09 |
| 8 | https://huggingface.co/zai-org/GLM-5.3 | zai-org/GLM-5.3 - Hugging Face | primary | web_extract | 2026-10-09 |
| 9 | https://huggingface.co/zai-org/GLM-5.3-Flash | zai-org/GLM-5.3-Flash - Hugging Face | primary | web_extract | 2026-10-09 |
| 10 | https://ollama.com/library/glm-5.3-flash | glm-5.3-flash - Ollama | primary | web_extract | 2026-10-09 |
| 11 | https://ollama.com/library/glm-4.7-flash | glm-4.7-flash - Ollama | primary | web_extract | 2026-10-09 |
| 12 | https://blog.ecosia.org/ecosia-search-engine/ | The search engine that plants trees: what's Ecosia and how does it work? - Ecosia Blog | primary | web_extract | 2026-10-09 |

## Notes
FireCrawl returned HTTP 402 (out of credits) on every call, so discovery ran on web_search and every cited page was fetched and read with web_extract: 5 searches and 10 page fetches for 12 sources, all accessed 2026-10-09. Conflicts kept verbatim: the GLM-5.3-Flash card prose says 320B total parameters while the Hugging Face sidebar prints 321B params (the prose figure is used in claims); POLITICO frames the switch as betting on Chinese AI while Kroll told EU-Startups it is about open models, not country of origin. The Ecosia scale figure comes from Ecosia's own 2021 page, the freshest first-party number fetched this session. GLM-4.7-Flash is the small sibling of the 320B model Ecosia is buying inference for, and it is the honest local example: the 753B GLM-5.3 is not a home download.
