---
slug: 2026-09-26-ollaya-runs-decision-models-th
stage: 03-research
topic: "Ollaya: run open Jev-style decision models locally through an Ollama-style CLI"
depth: standard
generated_at: 2026-09-26T11:36:44Z
sources: 9
hub: "[[videos/2026-09-26-ollaya-runs-decision-models-th]]"
---

# Research brief: Ollaya runs decision models through the Ollama CLI

## Summary
Ollaya is a one-binary Apache-2.0 runtime that pulls and serves open decision models on your own machine, and its whole pitch is speed: the homepage claims a five-question laya request runs in "8–10ms" on an RTX 4090 against "236–276ms" for hosted TypeSafe Jev, and its hero demo shows decider:2b flagging a force-push as destructive at 0.90 probability in "178 ms". The concrete case is that agent-safety demo: a 1.9B model catching `git push --force` before it happens, entirely offline. What could not be verified: any first-party number on our own hardware, Ollaya's production adoption beyond the Show HN thread (426 points, 114 comments), and the laya-versus-Jev prior-art dispute. One conflict to flag: Ollaya's latency chart compares its local GPU numbers against Jev's hosted API latency including network, which Ollaya itself calls "an order-of-magnitude comparison", and TypeSafe's own 193.6x/444.6x speedup claims come with the vendor's own hedge that they are "on the higher end of real world gains".

## Thesis
The small, repeated decisions inside your AI app do not need a chatbot: Ollaya runs open decision models on your own GPU that answer typed questions in single-digit milliseconds, entirely offline.

## Explanation path

Open with the distinction every viewer already half-knows: an LLM writes, and sometimes you do not need writing, you need a decision with a number attached. Establish decision models through the Jev moment: TypeSafe shipped Jev on September 15, 2026 as a "System One Model" that never generates text; it returns a typed answer (a choice, a score, or a noul, which is a yes/no probability) with calibrated probabilities, and TypeSafe claims two orders of magnitude speed over LLMs on decision-shaped work. Before any Ollaya screen appears the viewer must understand what a single forward pass buys: no token-by-token generation, so cost does not scale with answer length, and the probabilities are the product you threshold on. Then bring in the local turn: Jev is a closed, hosted API, and roughly two weeks later Ollaya arrived as the open local answer, billed as "Ollama for decision models": one Apache-2.0 binary that pulls open weights (laya, decider, nli, gliclass, qwen3guard, kev, von) from their authors' Hugging Face repositories, pinned to a commit and sha256-checked. Show the drop-in compatibility trick as the payoff move: set `TYPESAFE_BASE_URL=http://localhost:11435` and the official TypeSafe SDK works unchanged against the local server, the port sitting one digit off Ollama's 11434. Land the concrete demo early: a five-question request to laya in about 10 ms end to end, and decider catching a destructive force-push. Close on the honest limits: the encoder models are small (322m to 439m parameters), laya is near chance zero-shot on typed decisions (0.362 base versus 0.766 fine-tuned), choice questions with more than about 20 options degrade, and the raw checkpoints ship over-confident until temperatures are refit on your own labelled data.

## Claims
1. **Ollaya is an open-source (Apache-2.0) runtime that downloads and serves open decision models locally, with a desktop app, a CLI and Docker for macOS, Windows and Linux.**
   - Source: Ollaya · Run decision models locally, https://ollaya.dev/
   - Tier: primary | Confidence: high | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "macOS, Windows, Linux and Docker · Apache-2.0 · GitHub"
2. **Ollaya claims a five-question request to laya takes "8–10ms" end to end through the HTTP API on an RTX 4090, against "236–276ms" for TypeSafe's hosted Jev, a comparison it itself frames as order-of-magnitude.**
   - Source: Ollaya · Run decision models locally, https://ollaya.dev/
   - Tier: primary | Confidence: medium (vendor's own benchmark, hedged on the page) | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "8–10ms / Laya on Ollama / RTX 4090, five questions, end to end" and "Setups differ, so read it as an order-of-magnitude comparison."
3. **Ollaya's hero demo shows decider:2b judging a force-push request: "destructive yes 0.90", "action block 0.53", "answered in 178 ms on an RTX 4090".**
   - Source: Ollaya · Run decision models locally, https://ollaya.dev/
   - Tier: primary | Confidence: medium (single hero run) | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "Real output: decider:2b answered in 178 ms on an RTX 4090."
4. **Ollaya serves `/v1/systemone` and `/v1/models` with TypeSafe's request and response shapes, and "The official TypeSafe Python SDK 0.7.1 works unchanged against a local server."**
   - Source: Ollaya · Run decision models locally, https://ollaya.dev/
   - Tier: primary | Confidence: high | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "The official TypeSafe Python SDK 0.7.1 works unchanged against a local server."
5. **TypeSafe AI released Jev on September 15, 2026 as its first System One Model: it gives up string generation for typed probabilistic decisions and, in TypeSafe's words, "can't" hallucinate.**
   - Source: Introducing System One Models & Jev - TypeSafe AI Blog, https://typesafe.ai/blog/introducing-system-one-models-and-jev
   - Tier: primary | Confidence: high | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "While Jev gives up string generation, it's optimized for structured outputs and _can't_ hallucinate."
6. **TypeSafe's launch table puts Jev's end-to-end response time at "70ms-500ms" and its price at "$0.042 / MTok ($42 per billion tokens)" input with output tokens "FREE (too cheap to meter)".**
   - Source: Introducing System One Models & Jev - TypeSafe AI Blog, https://typesafe.ai/blog/introducing-system-one-models-and-jev
   - Tier: primary | Confidence: high | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "Input tokens: $0.042 / MTok ($42 per billion tokens). Output tokens: FREE (too cheap to meter)."
7. **Jev returns exactly three answer kinds: nouls (how true something is), scores (a graded rubric) and choices (multiple-choice).**
   - Source: Jev decision model touted as quicker, cheaper LLM alternative - TechTarget, https://www.techtarget.com/it-infrastructure/news/366650696/Jev-decision-model-touted-as-quicker-cheaper-LLM-alternative
   - Tier: docs | Confidence: high | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "It can only return nouls (how true something is), scores (a graded rubric) and choices (multiple-choice question)."
8. **laya is Convai Innovations' open Apache-2.0 decision-model family on encoder backbones: laya:en is ModernBERT-large at 421M parameters, laya:multilingual is mmBERT-base at 322M covering 100+ languages.**
   - Source: laya · Ollaya, https://ollaya.dev/library/laya
   - Tier: primary | Confidence: high | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "laya:en | ModernBERT-large | 421M | 512 | English | Guardrails, email triage"
9. **decider is Mapika's open decision-model family on Qwen3.5 bases; decider:2b (1.9B parameters) scores 0.591 on typed decisions and "needs about 8 GB of memory at fp32".**
   - Source: decider · Ollaya, https://ollaya.dev/library/decider
   - Tier: primary | Confidence: high | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "`2b` needs about 8 GB of memory at fp32."
10. **Ollaya "never re-hosts" weights: they come from the authors' Hugging Face repositories, "pinned to a commit and checked against sha256".**
   - Source: Ollaya · Run decision models locally, https://ollaya.dev/
   - Tier: primary | Confidence: high | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "Weights come from their authors' Hugging Face repositories, pinned to a commit and checked against sha256. Ollaya never re-hosts them, and the runtime is Apache-2.0."
11. **Ollaya's Show HN thread reached "426 points" with "114 comments" within about 13 hours of posting.**
   - Source: Ollaya – Ollama for open-source, Jev-style decision models | Hacker News, https://news.ycombinator.com/item?id=49848269
   - Tier: community | Confidence: high | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "426 points by Ardakilic 13 hours ago | 114 comments"
12. **The laya-typed-decisions checkpoint reaches 0.766 accuracy on the typed-decisions benchmark against "0.362 for the base English checkpoint", and laya falls to 0.425 on Banking77's 77 options against 0.870 for Jev.**
   - Source: convaiinnovations/laya · Hugging Face, https://huggingface.co/convaiinnovations/laya
   - Tier: primary | Confidence: high | Accessed: 2026-09-26 | Via: web_extract
   - Quote: "the fine-tuned laya-typed-decisions checkpoint scores 0.766 accuracy, against 0.362 for the base English checkpoint on the same decisions."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | laya five-question request, end to end, RTX 4090 | 8–10ms | https://ollaya.dev/ | "8–10ms Laya on Ollaya RTX 4090, five questions, end to end" |
| 2 | hosted TypeSafe Jev median request (third-party benchmark) | 236–276ms | https://ollaya.dev/ | "236–276ms TypeSafe Jev Hosted API, median request" |
| 3 | decider:2b demo answer time, RTX 4090 | 178 ms | https://ollaya.dev/ | "Real output: decider:2b answered in 178 ms on an RTX 4090." |
| 4 | Jev input price | $0.042 / MTok ($42 per billion tokens) | https://typesafe.ai/blog/introducing-system-one-models-and-jev | "Input tokens: $0.042 / MTok ($42 per billion tokens)." |
| 5 | Jev end-to-end response time | 70ms-500ms | https://typesafe.ai/blog/introducing-system-one-models-and-jev | "End-to-end response time is 70ms-500ms for TypeSafe." |
| 6 | laya:en parameters (ModernBERT-large) | 421M | https://ollaya.dev/library/laya | "laya:en \| ModernBERT-large \| 421M \| 512 \| English" |
| 7 | decider:2b typed-decisions accuracy | 0.591 | https://ollaya.dev/library/decider | "decider:latest, decider:2b \| Qwen3.5-2B \| 1.9B \| 0.591" |
| 8 | Show HN traction at ~13 hours | 426 points / 114 comments | https://news.ycombinator.com/item?id=49848269 | "426 points by Ardakilic 13 hours ago \| 114 comments" |
| 9 | laya-typed-decisions accuracy vs base checkpoint | 0.766 vs 0.362 | https://huggingface.co/convaiinnovations/laya | "scores 0.766 accuracy, against 0.362 for the base English checkpoint" |

## Analogy candidates
- **Vehicle**: The triage nurse and the specialist. Mapping: the decision model is the nurse at the front desk who takes one look and routes you; the LLM is the specialist who does the actual work afterward. Fast, structured, cheap, on every door. Breaks when: the nurse cannot write you a letter or explain a diagnosis; a decision model has no answer type for anything open-ended. It also hides that you define the desks (the option set) yourself.
- **Vehicle**: The smoke detector and the fire department. Mapping: laya is the smoke detector: one sensor, one yes/no, mounted locally, costs nothing per ping; the LLM is the fire department: expensive and slow but able to actually handle the fire. Breaks when: a smoke detector asks one fixed question, while laya takes your questions and option sets and returns calibrated probabilities, not an alarm.

## Misconceptions
- Myth: Decision models are a brand-new 2026 invention. Reality: ML veterans in the HN thread call them repackaged classifiers ("anyone with basic ML knowledge could've built this in a few hours"); what is new is the product shape: typed API, calibrated probabilities, one-command local runtime (claim 11 thread; analogy to BERT-era classifiers).
- Myth: Jev or Ollaya replaces your LLM. Reality: TypeSafe's own table keeps "Human-in-the-loop tasks (chatbots, copilots, coding agents)" with LLMs, and TechTarget's analysts split the work: decisions and routing to the decision model, text generation to the LLM (claims 5, 7).
- Myth: Ollaya's milliseconds will hold on your hardware. Reality: every Ollaya latency figure is an RTX 4090 benchmark or hero demo, and Ollaya itself calls the Jev comparison "an order-of-magnitude comparison"; treat 8-10 ms as the vendor's number until measured locally (claims 2, 3).

## Glossary
- **decision model**: a model that reads a state plus typed questions and returns a typed answer with calibrated probabilities in one forward pass, never generating text.
- **System One Model**: TypeSafe's class name for models built for fast, structured decisions software can use directly, borrowed from Kahneman's fast intuitive thinking.
- **Jev**: TypeSafe AI's closed, hosted decision model released September 15, 2026, named after the economist William Stanley Jevons.
- **laya**: Convai Innovations' open Apache-2.0 decision-model family on encoder backbones (322M-421M parameters), the fastest model Ollaya ships.
- **decider**: Mapika's open decision-model family on Qwen3.5 bases that reads option-letter logits; Ollaya calls it the most accurate open decision model it ships.
- **choice**: a question type whose answer is one option from a set you define, returned with a probability per option.
- **score**: a question type whose answer is a level on an ordered rubric of 2 to 10 levels you define.
- **noul**: a yes/no question type returning the probability that a statement holds; TypeSafe's coinage, kept by Ollaya.
- **calibrated probabilities**: probabilities that mean what they say, so a 0.90 is right about nine times in ten; refittable on your own labelled data.
- **forward pass**: one run of an input through the network to its outputs; a decision model answers in a single pass instead of generating a token at a time.
- **ONNX Runtime**: the cross-platform inference engine Ollaya uses to run the encoder models on CPU or NVIDIA GPU.
- **ECE (expected calibration error)**: a score for how far a model's stated probabilities sit from its actual hit rate; lower is better.

## Unverified
- Any latency or throughput figure on the channel's own DGX Spark or consumer GPUs; Ollaya's published numbers are RTX 4090 benchmarks and must stay attributed until a first-party measurement exists.
- That 8-10 ms holds at production batch sizes or on CPU-only machines; decider's page says both decider models "are slow on the CPU", and laya CPU latency was not published on the pages fetched.
- The laya-versus-Jev prior-art dispute linked in the HN thread; we did not fetch the linked rebuttal and take no side.
- Byte-perfect TypeSafe SDK compatibility across every endpoint; the compatibility guide page was not fetched.
- Ollaya adoption beyond the Show HN thread and the GitHub repo's visible stars; no download counts were fetched.
- Whether Ollama itself absorbs decision-model support, which the HN thread asks and nobody answers.
- Which models ship in the default install versus separate pulls (winnow, kev tags).

## Suggested outline
1. Hook: your app is burning LLM tokens on questions with known answers; this force-push was flagged destructive at 0.90 by a 1.9B-parameter model in 178 ms, offline.
2. What a decision model is: a state plus typed questions in; a choice, a score or a noul with probabilities out; one forward pass; no generation, nothing to parse.
3. The Jev moment: TypeSafe shipped the closed hosted version on September 15, claiming 70ms-500ms and $0.042 per million input tokens with output free, and half of HN says it is just a classifier; the new part is the product shape, not the math.
4. The local turn: Ollaya is Ollama for decision models; one Apache-2.0 binary; pulls laya, decider, nli, gliclass, qwen3guard from the authors' Hugging Face repos, sha256-pinned; serves the TypeSafe-compatible `/v1/systemone` on port 11435.
5. Payoff on screen: `ollaya run laya`, the triage preset answering five questions in about 10 ms, and the TYPESAFE_BASE_URL swap that points an existing TypeSafe app at localhost.
6. Honest catch: the encoders are tiny; base laya is near chance on typed decisions (0.362) until you use the fine-tuned checkpoint (0.766) or decider (0.591); more than about 20 options degrades accuracy; refit calibration before trusting a threshold.
7. Close: the decisions layer is becoming its own tier in the local stack; the move tonight is one binary and one command.

## Viewer situation
You run Ollama on a gaming PC or a Mac, and more than once you have pasted a support ticket or a code diff into a cloud chat box just to get a one-word answer back.

## Has process
true
- Install the Ollaya binary for your platform (macOS, Windows, Linux or Docker).
- Pull and run a decision model with one command: `ollaya run laya`.
- Ask a typed question from the CLI using a preset, for example `ollaya run decider --preset agent`.
- Point the official TypeSafe SDK at the local server with `TYPESAFE_BASE_URL=http://localhost:11435` and `TYPESAFE_API_KEY=local`.
- Refit calibration on your own labelled data with a Modelfile before trusting probability thresholds.

## Objection
"It is a zero-shot classifier with a REST wrapper; BERT did this years ago, the encoder is a few hundred million parameters, and the headline milliseconds are the vendor's own RTX 4090 benchmark compared against a hosted API's network-inclusive latency."

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://ollaya.dev/ | Ollaya · Run decision models locally | primary | web_extract | 2026-09-26 |
| 2 | https://ollaya.dev/library/laya | laya · Ollaya | primary | web_extract | 2026-09-26 |
| 3 | https://ollaya.dev/library/decider | decider · Ollaya | primary | web_extract | 2026-09-26 |
| 4 | https://github.com/ollaya-dev/ollaya | ollaya-dev/ollaya on GitHub | primary | web_extract | 2026-09-26 |
| 5 | https://huggingface.co/convaiinnovations/laya | convaiinnovations/laya · Hugging Face | primary | web_extract | 2026-09-26 |
| 6 | https://typesafe.ai/blog/introducing-system-one-models-and-jev | Introducing System One Models & Jev - TypeSafe AI Blog | primary | web_extract | 2026-09-26 |
| 7 | https://www.techtarget.com/it-infrastructure/news/366650696/Jev-decision-model-touted-as-quicker-cheaper-LLM-alternative | Jev decision model touted as quicker, cheaper LLM alternative | docs | web_extract | 2026-09-26 |
| 8 | https://news.ycombinator.com/item?id=49848269 | Ollaya – Ollama for open-source, Jev-style decision models \| Hacker News | community | web_extract | 2026-09-26 |
| 9 | https://hanxiao.io/all-about-jev/ | All about Jev -- replications, models, runtimes & benchmarks | benchmark | web_extract | 2026-09-26 |

## Notes
- Conflicts: (1) Ollaya's latency chart compares its local GPU numbers against Jev's hosted API latency, "which includes the network"; Ollaya itself says "read it as an order-of-magnitude comparison". Trust the shape, not the digits. (2) TypeSafe's 193.6x/444.6x claims are from the vendor's own workflows, and its own nuance section expects they are "on the higher end of real world gains"; the independent claim-audit row in the Jev tracker (hanxiao.io, fetched) reports independent tests at ~5x faster and 8.6x cheaper than Mistral Small 4. Keep the video on the conservative numbers. (3) The laya prior-art dispute in the HN thread is unresolved; take no side.
- TechTarget reports Vercel saw "13% of its paid AI Gateway users" try Jev within 24 hours of launch; secondhand reporting of a Vercel blog we did not fetch, so it stays here rather than under Claims.
- The GitHub page was fetched for license, packaging and repo structure but its star count was read from the page header at fetch time and is volatile; traction is cited from the Show HN thread instead.
- FireCrawl tools were not attached to this session; the WebSearch/WebExtract fallback defined in rules/firecrawl-usage.md was used, one page fetched at a time, all nine pages read in-session.
