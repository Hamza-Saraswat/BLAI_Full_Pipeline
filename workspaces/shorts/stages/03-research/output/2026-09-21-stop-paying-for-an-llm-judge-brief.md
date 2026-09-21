---
slug: 2026-09-21-stop-paying-for-an-llm-judge
stage: 03-research
topic: "Stop paying for an LLM judge"
depth: standard
generated_at: 2026-09-21T11:37:21Z
sources: 10
hub: "[[videos/2026-09-21-stop-paying-for-an-llm-judge]]"
---

# Research brief: Stop paying for an LLM judge

## Summary
The video lands a swap, not a shrink: the verdict moves from a generated critique on a priced API to a typed probability out of local weights. The most arresting number is LangChain's cost table, $0.34 total versus $28.17 for Claude for the same 500 judgments, with the LLM judges showing 92x to 913x the score variance of the decision model. The strongest concrete case is Kev-4B, an Apache-2.0 LoRA adapter on Qwen3.5-4B-Base that serves judge decisions from about 9 GB of GPU memory on hardware the viewer already owns. Unverified: the zero-dollar Kev row in the jevals bench table is an estimate its authors labeled as such, and nothing here has been measured on our own hardware. One conflict: JevBench's archived run puts Jev at 80.3% accuracy on Banking77 while the jevals README quotes JevBench as finding "83 to 87%", so trust the run page that publishes its protocol.

## Thesis
The judge in your eval loop does not need to be a frontier API: distill the verdict into a tiny local decision model and the per-token bill becomes a one-time download.

## Explanation path
Start with the bill the viewer already pays: every LLM-as-judge call sends a trace and a rubric to a frontier API, which generates its verdict token by token and charges per million tokens on the way in and the way out. Make concrete what that judge actually returns: a paragraph of reasoning and a JSON blob, of which the software keeps only a label, plus the failure modes that ride along with generation, verdicts that swing across identical runs and flip when option order swaps. Introduce the decision model as a different shape of thing rather than a smaller version of the same thing: state plus typed questions in, calibrated probabilities out, computed in a single forward pass with nothing generated. Land Kev as the open-weights instance of that shape: a LoRA adapter and a pointer head on a small Qwen3.5 base, downloadable, Apache-2.0, serving from a machine the viewer owns, fine-tunable on a few hundred of their own labeled examples. Bring in jevals to show the shift arriving in tooling, where judging every trace inside the agent loop becomes affordable and sampling a sliver nightly stops being the default. Finish on the boundary the honest viewer needs: date arithmetic, broad knowledge, and multi-step critique still belong to the big model, so the win is replacing the judge on verdicts that are really classifications, not abolishing the API.

## Claims
1. **Kev is a family of small open-weight decision models built on Qwen3.5 bases, whose API matches TypeSafe's System One so existing SDKs point at a local server, and anyone can train their own.**
   - Source: GitHub - jaredpalmer/kev: tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own, https://github.com/jaredpalmer/kev
   - Tier: primary | Confidence: high | Accessed: 2026-09-21 | Via: web_extract
   - Quote: "Kev is a family of small decision models built on Qwen3.5 and based on the architecture described in Jev's Architecture Unmasked. You can use the pretrained weights or train your own. The API matches TypeSafe's System One, so you can point their Python SDK at your local server."
2. **Kev-4B is a LoRA adapter with r=16 and 33.8M trainable parameters plus a pointer head on Qwen/Qwen3.5-4B-Base, and it needs ~9 GB of GPU memory for serving in bf16, with training having taken 56 min on one H100 (peak 24.6 GB).**
   - Source: Kev-4B model card (jaredpalmer/kev docs), https://raw.githubusercontent.com/jaredpalmer/kev/main/docs/model-cards/kev-4b.md
   - Tier: primary | Confidence: high | Accessed: 2026-09-21 | Via: web_extract
   - Quote: "It is a LoRA adapter (r=16, 33.8M trainable parameters) plus a pointer head on Qwen/Qwen3.5-4B-Base (revision 1001bb4d), serving TypeSafe's public /v1/systemone contract." and "4B bf16 needs ~9 GB of GPU memory for serving; training took 56 min on one H100 (peak 24.6 GB)."
3. **Kev runs on the viewer's own hardware with no API key and no per-token bill: the 4B and 9B models fit a 32 GB Mac using bf16, and the server binds to 127.0.0.1 with no authentication.**
   - Source: GitHub - jaredpalmer/kev: tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own, https://github.com/jaredpalmer/kev
   - Tier: primary | Confidence: high | Accessed: 2026-09-21 | Via: web_extract
   - Quote: "Runs on CUDA and Apple Silicon. The 4B and 9B models fit a 32 GB Mac using bf16" and "The server binds to 127.0.0.1 and has no authentication. Keep it local unless you add authentication yourself."
4. **On the frozen out-of-domain suite, Kev-9B reached 0.837 and Kev-4B reached 0.832 accuracy on the locked test after the move to Qwen3.5 bases, up from 0.780 and 0.806, with lower Brier scores.**
   - Source: Releases · jaredpalmer/kev, https://github.com/jaredpalmer/kev/releases
   - Tier: primary | Confidence: high | Accessed: 2026-09-21 | Via: web_extract
   - Quote: "On the locked test, out of domain: Kev-9B 0.837 (Kev-8B was 0.780), Kev-4B 0.832 (was 0.806), with lower Brier scores."
5. **The LLM-judge status quo is measurable: running the four Ragas-equivalent metrics on gpt-4.1-mini costs 6.0 requests per sample and $2.60 per 1k samples, while the same metrics through a Jev decision model cost $0.03 per 1k samples in one request per sample (jevals bench, measured 2026-09-20).**
   - Source: GitHub - openlayer-ai/jevals: Agent evals and guardrails in one request. Built on Jev, Kev and Laya., https://github.com/openlayer-ai/jevals
   - Tier: primary | Confidence: high | Accessed: 2026-09-21 | Via: web_extract
   - Quote: "Ragas, gpt-4.1-mini | 6.0 LLM + embeddings | 4,390 | 530 | $2.60 | 22 to 35s" and "jevals, Jev | 1.0 | 824 | 148, not billed | $0.03 | 0.8s" and "All the evals for a trace go out as one request that costs a few thousandths of a cent and comes back in a few hundred milliseconds, so you can run them on every trace and inside the agent loop."
6. **Jev, the hosted decision model, is priced at $0.042 per million input tokens with output tokens free, which TypeSafe itself frames against LLM input prices of $0.20 to $10 per million tokens.**
   - Source: Introducing System One Models & Jev - TypeSafe AI Blog, https://typesafe.ai/blog/introducing-system-one-models-and-jev
   - Tier: primary | Confidence: high | Accessed: 2026-09-21 | Via: web_extract
   - Quote: "Input tokens: $0.042 / MTok ($42 per billion tokens). Output tokens: FREE (too cheap to meter)." (LLM column: "Input tokens: from $0.20 to $10 / MTok. Output tokens: ~5x more expensive than input tokens.")
7. **Named OpenAI judge models bill per million tokens at standard tier: gpt-5.6-luna lists $0.20 input and $1.20 output, and gpt-5.6-terra lists $2.00 input and $12.00 output, short context (OpenAI API pricing page, seen 2026-09-21).**
   - Source: Pricing | OpenAI API, https://platform.openai.com/docs/pricing
   - Tier: primary | Confidence: high | Accessed: 2026-09-21 | Via: web_extract
   - Quote: "| gpt-5.6-terra | $2.00 | $0.20 | $2.50 | $12.00 | $4.00 | $0.40 | $5.00 | $18.00 |" and "| gpt-5.6-luna | $0.20 | $0.02 | $0.25 | $1.20 | $0.40 | $0.04 | $0.50 | $1.80 |"
8. **On identical replayed traces, GPT and Claude judges showed 92x to 913x the score variance of Jev; Jev matched a human oracle on all 500 repeated pass/fail decisions against 80.0% for Claude Sonnet 4.6, and averaged $0.00035/call, $0.34 total versus $28.17 for Claude (LangChain experiment, 100 repetitions per judge).**
   - Source: Jev-as-a-Judge for Agent Evals (LangChain blog, 2026-09-20), https://www.langchain.com/blog/jev-agent-evals-langsmith
   - Tier: docs | Confidence: high | Accessed: 2026-09-21 | Via: web_extract
   - Quote: "For the binary does_pass score, Jev matched the oracle on all 500 repeated decisions. Terra matched on 99.8% of decisions, Luna on 96.4%, and Claude on 80.0%." and "Jev had the lowest observed mean per-case variance: 0.0000149. Luna was 433x higher, Terra was 913x higher, and Claude was 92x higher." and "It averaged 0.44s and $0.00035/call ($0.34 total vs. $28.17 for Claude)."
9. **LLM judges carry position bias: a quality ranking can be hacked just by altering the order responses appear in, letting Vicuna-13B beat ChatGPT on 66 over 80 tested queries with ChatGPT as the evaluator.**
   - Source: [2305.17926] Large Language Models are not Fair Evaluators, https://arxiv.org/abs/2305.17926
   - Tier: primary | Confidence: high | Accessed: 2026-09-21 | Via: web_extract
   - Quote: "We find that the quality ranking of candidate responses can be easily hacked by simply altering their order of appearance in the context. This manipulation allows us to skew the evaluation result, making one model appear considerably superior to the other, e.g., Vicuna-13B could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator."
10. **The tiny local judge has named gaps on the same frozen items: Kev-4B scores 0.55 on date arithmetic against Jev's 0.93, 0.70 on MMLU against 0.90, and 0.500 on MMLU-Pro 10-way against Jev's 0.840, and its out-of-domain probabilities are usable but not calibrated (raw ECE 0.130 dev, 0.102 test).**
    - Source: Kev-4B model card (jaredpalmer/kev docs), https://raw.githubusercontent.com/jaredpalmer/kev/main/docs/model-cards/kev-4b.md
    - Tier: primary | Confidence: high | Accessed: 2026-09-21 | Via: web_extract
    - Quote: "Date arithmetic (deadline 0.55 vs Jev 0.93), knowledge (MMLU 0.70 vs 0.90) and noisy-label emotion (0.54 vs 0.59) remain the gap to Jev." and "MMLU-Pro (10-way) 0.500 / 0.440 / 0.840" (Kev-4B / Qwen3 Kev-4B / Jev) and "Out-of-domain probabilities are usable but not calibrated (raw ECE 0.130 dev, 0.102 test); temperature fitted in-domain does not transfer."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Jev input price per million tokens (output tokens free) | $0.042 / MTok | https://typesafe.ai/blog/introducing-system-one-models-and-jev | "Input tokens: $0.042 / MTok ($42 per billion tokens). Output tokens: FREE (too cheap to meter)." |
| 2 | Four Ragas metrics on gpt-4.1-mini, per 1k samples (jevals bench, 2026-09-20) | $2.60 | https://github.com/openlayer-ai/jevals | "Ragas, gpt-4.1-mini | 6.0 LLM + embeddings | 4,390 | 530 | $2.60 | 22 to 35s" |
| 3 | Same four metrics through Jev, per 1k samples | $0.03 | https://github.com/openlayer-ai/jevals | "jevals, Jev | 1.0 | 824 | 148, not billed | $0.03 | 0.8s" |
| 4 | GPT and Claude judge score variance relative to Jev (100 repetitions) | 92x to 913x | https://www.langchain.com/blog/jev-agent-evals-langsmith | "Jev had the lowest observed mean per-case variance: 0.0000149. Luna was 433x higher, Terra was 913x higher, and Claude was 92x higher." |
| 5 | Total cost of 500 repeated quality judgments, Jev versus Claude Sonnet 4.6 | $0.34 total vs. $28.17 for Claude | https://www.langchain.com/blog/jev-agent-evals-langsmith | "It averaged 0.44s and $0.00035/call ($0.34 total vs. $28.17 for Claude)." |
| 6 | Kev-9B accuracy on the locked out-of-domain test (frozen suite) | 0.837 | https://github.com/jaredpalmer/kev/releases | "On the locked test, out of domain: Kev-9B 0.837 (Kev-8B was 0.780), Kev-4B 0.832 (was 0.806), with lower Brier scores." |
| 7 | Kev-4B bf16 GPU memory needed for serving | ~9 GB of GPU memory | https://raw.githubusercontent.com/jaredpalmer/kev/main/docs/model-cards/kev-4b.md | "4B bf16 needs ~9 GB of GPU memory for serving; training took 56 min on one H100 (peak 24.6 GB)." |
| 8 | Position-bias hack: queries where Vicuna-13B beat ChatGPT by order swap alone (ChatGPT as evaluator) | 66 over 80 tested queries | https://arxiv.org/abs/2305.17926 | "Vicuna-13B could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator." |

The most arresting number for the hook is #5, $0.34 total vs. $28.17 for Claude; #4 (92x to 913x variance) is the strongest myth-bust support.

## Analogy candidates
- **Hiring a courtroom lawyer to sort mail**: the LLM judge bills by the word for a written opinion on every envelope, while the decision model is a trained sorter that circles a routing slip in one glance. Breaks when: the sorter cannot write an opinion at all; anything needing reasoned critique or multi-step argument goes back to the lawyer.
- **A toll bridge versus a bike you own**: per-token judge pricing is a toll paid on every judgment, and local weights are the upfront purchase that makes each extra judgment free. Breaks when: the bike rides fixed routes, meaning rubric-shaped short-context verdicts, not long-document grading or open-ended critique.

## Misconceptions
- Myth: Judging an agent trace needs a frontier model that writes out its reasoning. Reality: most judge questions are a yes/no, a choice, or a rubric score, and a small decision model returns them as probabilities in one forward pass (claims 1, 5).
- Myth: The API bill is the whole cost of an LLM judge. Reality: generation also makes judges unstable, 92x to 913x the score variance of a decision model on identical traces, with verdicts that flip when option order swaps (claims 8, 9).
- Myth: A local 4B judge is a drop-in replacement for the big judge. Reality: Kev-4B scores 0.55 on date arithmetic where hosted Jev scores 0.93, and 0.500 on MMLU-Pro where Jev scores 0.840 (claim 10).

## Glossary
- **LLM-as-judge**: using a chat model to read another model's output and write the verdict, generated token by token and billed per token.
- **decision model**: a model that reads a state and returns typed answers with calibrated probabilities in a single forward pass, generating no text.
- **System One model**: TypeSafe's name for the model class that trades away text generation for fast, structured, probability-valued decisions.
- **LoRA adapter**: a small set of extra trainable weights attached to a frozen base model, so a big model can be specialized cheaply.
- **forward pass**: one trip of the input through the network to its outputs, with no token-by-token generation afterwards.
- **calibrated probability**: a probability that matches how often the model is actually right, so software can act on it.
- **per million tokens**: the unit API models bill by, charged separately for text sent in and text generated out.
- **Ragas**: a popular open-source eval library whose faithfulness and relevancy metrics are built on LLM judge calls.
- **position bias**: a judge flaw where swapping the order of the options changes the verdict.
- **variance**: how much a judge's score moves when it re-scores the identical trace.
- **out-of-domain**: test questions from dataset families the model never trained on.

## Unverified
- The jevals bench rows for Kev-4B ($0 per 1k samples, ~6s wall time) and Laya (~1s) are labeled estimates by the jevals authors and have not been run by them.
- No first-party measurement exists of Kev's tokens-per-second or latency on our own hardware, including the DGX Spark; the README's numbers are an M5 Mac and one H100.
- Whether TypeSafe's $0.042 per million input token price is sustainable is unknowable from outside; TypeSafe itself says it "can't prove it isn't subsidized".
- Whether position bias and judge variance actually bite in any specific viewer pipeline depends on their harness and prompt, not on the papers alone.

## Suggested outline
1. The judge bill is real and named: frontier judge models charge per million tokens for verdicts written token by token, while the same job done by a decision model costs a fraction of a cent per trace.
2. What a decision model is and what Kev puts on your machine: typed questions in, calibrated probabilities out, one forward pass, small open Qwen weights running local with no per-token bill.
3. The honest boundary: tiny judges lose at date arithmetic, world knowledge, and multi-step critique, so keep the big model for those and run the local judge on every trace.

## Viewer situation
You score your agent's traces with a frontier API judge and wince at the token bill every time the eval suite runs.

## Has process
`true`
- Clone the Kev repository and run `uv sync --extra serve` to install the server.
- Start the judge locally with `KEV_DTYPE=bf16 uv run --extra serve python -m kev.serve --run jaredpalmer/kev-4b --port 8009`.
- Send your trace as `state` plus typed `questions` to `localhost:8009/v1/systemone` and read back a probability per question.

## Objection
A 4B judge that scores 0.55 on date arithmetic where the hosted model scores 0.93 is a classifier dressed up as a judge, and its uncalibrated confidence can quietly automate the wrong decisions.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/jaredpalmer/kev | GitHub - jaredpalmer/kev: tiny Jev-like family of decision models built on top of Qwen3.5 | primary | web_extract | 2026-09-21 |
| 2 | https://github.com/jaredpalmer/kev/releases | Releases · jaredpalmer/kev | primary | web_extract | 2026-09-21 |
| 3 | https://github.com/openlayer-ai/jevals | GitHub - openlayer-ai/jevals: Agent evals and guardrails in one request | primary | web_extract | 2026-09-21 |
| 4 | https://raw.githubusercontent.com/jaredpalmer/kev/main/docs/model-cards/kev-4b.md | Kev-4B model card (jaredpalmer/kev docs) | primary | web_extract | 2026-09-21 |
| 5 | https://www.langchain.com/blog/jev-agent-evals-langsmith | Jev-as-a-Judge for Agent Evals (LangChain blog) | docs | web_extract | 2026-09-21 |
| 6 | https://jevbench.xyz/ | JevBench archive 001, Banking77 | benchmark | web_extract | 2026-09-21 |
| 7 | https://archerhume.com/posts/jevs-architecture-unmasked | Jev's Architecture Unmasked (archerhume) | community | web_extract | 2026-09-21 |
| 8 | https://arxiv.org/abs/2305.17926 | Large Language Models are not Fair Evaluators (arXiv) | primary | web_extract | 2026-09-21 |
| 9 | https://platform.openai.com/docs/pricing | Pricing | OpenAI API | primary | web_extract | 2026-09-21 |
| 10 | https://typesafe.ai/blog/introducing-system-one-models-and-jev | Introducing System One Models & Jev (TypeSafe AI Blog) | primary | web_extract | 2026-09-21 |

## Notes
FireCrawl returned 402 (credits out) for this run, so every page above was fetched with the hermes web_extract tool; Reddit was skipped (JSON 403) and YT_API_KEY is empty. Conflict: the jevals README cites JevBench putting Jev at "83 to 87% on Banking77 and CLINC150", while JevBench's own archived run reports 80.3% accuracy on Banking77 (3,080 cases); trust the run page, which publishes its protocol and failure cases. Scope caveat: LangChain's variance and cost numbers measured hosted Jev, not Kev, and Kev's accuracy numbers come from Jared Palmer's frozen suites (self-reported, with locked-test reads recorded once). Naming drift: the release badge says Kev-0.6B/Qwen3 while the current family is 0.8B/4B/9B on Qwen3.5; the release notes table is newer. The Qwen3.5 Kev models are slow on Apple Silicon (no fast DeltaNet kernels on MPS, 779 ms for a five-question request on the 4B on an M5); the Qwen3 checkpoints are the low-latency Mac option until an MLX backend ships.
