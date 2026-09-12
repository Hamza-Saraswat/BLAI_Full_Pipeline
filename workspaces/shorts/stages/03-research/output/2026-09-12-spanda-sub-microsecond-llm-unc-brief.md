---
slug: 2026-09-12-spanda-sub-microsecond-llm-unc
stage: 03-research
topic: "Spanda: sub-microsecond LLM uncertainty explained"
depth: standard
generated_at: 2026-09-12T11:45:00Z
sources: 11
hub: "[[videos/2026-09-12-spanda-sub-microsecond-llm-unc]]"
---

# Research brief: Spanda -- sub-microsecond LLM uncertainty explained

## Summary
The thesis: comparing a local model's several answers to the same question exposes its guessing, and Spanda does that comparison so cheaply (652.1 nanoseconds on CPU, no GPU) the check can run on every reply. Most arresting number: 92,400 µs (92.4 ms) for the established neural detector versus 652.1 nanoseconds for Spanda's kernel, a gap the project calls ~90,000x. Strongest concrete case: a viewer already running Ollama can put the Rust gateway in front of it tonight (`spnda serve --upstream http://localhost:11434/v1`) and every reply comes back stamped with an uncertainty header at 0.076 ms (76.3 µs) of added latency. Could not be verified: every latency, memory and AUROC number is the author's own benchmark -- the Zenodo preprint shows 0 citations and no third party has replicated any of it. Conflict: the README claims parity with neural semantic entropy from 7B+ on structured reasoning, but its own table shows neural SE ahead on TriviaQA at 7B (0.755 vs 0.698), so parity holds for converging answers, not trivia recall.

## Thesis
A local model's guessing can be exposed by asking it the same question a few times and comparing answers, and Spanda turns that comparison into a 652.1-nanoscopecond CPU computation -- cheap enough to stamp every reply your machine generates.

## Explanation path
Start inside the viewer's existing experience: a local model answers in the same confident tone whether it knows the fact or is inventing it, and nothing on screen distinguishes the two. Give that invisible thing a name before any tool appears: epistemic uncertainty is the model's own not-knowing, the kind that more data would fix -- distinct from genuine randomness in the question itself. Make it physical next: ask the same question three times and look at the answers; when they scatter, the model was guessing. That observation is the whole trick, and it is the same intuition behind self-consistency decoding. Then bring in the establishment: Nature-published semantic entropy does this properly by clustering the sampled answers by meaning with a second neural network (a DeBERTa NLI judge), and that judge is why nobody runs it on every reply -- the README measures it at 92,400 µs (92.4 ms) of GPU work per query. Spanda's move is to cluster by exact text match instead of by meaning, which needs no second model at all: the scoring collapses to 652.1 nanoseconds on a CPU core, 2.98 MB of resident memory, and 0.076 ms of proxy overhead in front of Ollama. Explain what the speed buys: a check this cheap is always on, per reply, on hardware the viewer already owns. Close on the boundary as the honest catch, in two parts: the nanoseconds score the samples, they do not generate them (the model still runs K times); and at 120B scale the signal inverts (AUROC 0.091) because a heavily tuned model repeats one wrong answer unanimously -- agreement is evidence, not truth.

## Claims
1. **Spanda's Rust gateway scores epistemic uncertainty in 652.1 nanoseconds (0.65 µs) on a single CPU core, with no GPU required.**
   - Source: GitHub - Adarshent/Spnda: Zero-cost epistemic uncertainty quantification & hallucination detection for LLMs, https://github.com/Adarshent/Spnda
   - Tier: primary | Confidence: high | Accessed: 2026-09-12 | Via: plain fetch
   - Quote: "652.1 nanoseconds (0.65 µs)"
2. **Semantic entropy, the method Spanda replaces, was published at ICLR 2023 by Kuhn, Gal and Farquhar and measures uncertainty at the level of meaning, because different sentences can mean the same thing.**
   - Source: Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation, https://arxiv.org/abs/2302.09664
   - Tier: primary | Confidence: high | Accessed: 2026-09-12 | Via: plain fetch
   - Quote: "different sentences can mean the same thing"
3. **A Nature (2024) paper showed semantic entropy detects confabulations -- a subset of hallucinations that are arbitrary and incorrect generations -- without task-specific data.**
   - Source: Detecting hallucinations in large language models using semantic entropy | Nature, https://www.nature.com/articles/s41586-024-07421-0
   - Tier: primary | Confidence: high | Accessed: 2026-09-12 | Via: plain fetch
   - Quote: "proposing entropy-based uncertainty estimators for LLMs to detect a subset of hallucinations"
4. **The README benchmarks neural semantic entropy's DeBERTa-based clustering at 92,400 µs (92.4 ms) per query versus under 1 µs for its own kernel, and calls the gap 90,000x.**
   - Source: GitHub - Adarshent/Spnda, https://github.com/Adarshent/Spnda
   - Tier: primary | Confidence: high | Accessed: 2026-09-12 | Via: plain fetch
   - Quote: "90,000x faster than Semantic Entropy"
5. **Spanda clusters K sampled answers by exact match instead of using a neural judge; on GSM8K its AUROC rises with model size -- 0.577 at 1.5B, 0.706 at 7B, 0.889 at 27B -- and the README claims the same discriminative power as DeBERTa cross-encoders from 7B+ on structured reasoning.**
   - Source: GitHub - Adarshent/Spnda, https://github.com/Adarshent/Spnda
   - Tier: primary | Confidence: high | Accessed: 2026-09-12 | Via: plain fetch
   - Quote: "On mathematical reasoning (GSM8K), exact-match AUROC scales monotonically"
6. **Epistemic uncertainty -- the quantity being scored -- is the model's own uncertainty, the kind that can be explained away given enough data (Kendall and Gal, NIPS 2017).**
   - Source: What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?, https://arxiv.org/abs/1703.04977
   - Tier: primary | Confidence: high | Accessed: 2026-09-12 | Via: plain fetch
   - Quote: "uncertainty which can be explained away given enough data"
7. **At 120B frontier scale on TriviaQA the signal inverts to an AUROC of 0.091: the model hallucinates the exact same incorrect answer across all sampled paths, which the paper names Confident Mode Collapse.**
   - Source: Spanda: Zero-Cost Lexical Entropy Matches Neural Semantic Uncertainty--Until Frontier Models Break It | Zenodo, https://zenodo.org/records/22233648
   - Tier: primary | Confidence: high | Accessed: 2026-09-12 | Via: plain fetch
   - Quote: "the model hallucinates the exact same incorrect answer across all paths, causing AUROC to invert to 0.091"
8. **Trusting agreement across sampled answers is the same intuition as self-consistency decoding, which improved GSM8K by +17.9% when it was published (Wang et al., ICLR 2023).**
   - Source: Self-Consistency Improves Chain of Thought Reasoning in Language Models, https://arxiv.org/abs/2203.11171
   - Tier: primary | Confidence: high | Accessed: 2026-09-12 | Via: plain fetch
   - Quote: "GSM8K (+17.9%)"
9. **The Python SDK ships on PyPI as package `spnda` at version 0.3.0, described as sub-microsecond epistemic uncertainty quantification and a high-throughput LLM gateway, installable with `pip install spnda`.**
   - Source: spnda 0.3.0 -- PyPI, https://pypi.org/project/spnda/
   - Tier: primary | Confidence: high | Accessed: 2026-09-12 | Via: plain fetch
   - Quote: "Sub-microsecond epistemic uncertainty quantification & high-throughput LLM gateway for AI safety"
10. **Spanda arrived on Hacker News this week: the Show HN post sat at 13 points with 2 comments about 13 hours after posting.**
    - Source: Show HN: Spanda -- Sub-microsecond LLM epistemic uncertainty in Rust | Hacker News, https://news.ycombinator.com/item?id=49665875
    - Tier: community | Confidence: high | Accessed: 2026-09-12 | Via: plain fetch
    - Quote: "13 points by Bhupennayak"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Spanda Rust kernel latency | 652.1 nanoseconds (0.65 µs) | https://github.com/Adarshent/Spnda | "652.1 nanoseconds (0.65 µs)" |
| 2 | Neural semantic entropy latency (DeBERTa judge) | 92,400 µs (92.4 ms) | https://github.com/Adarshent/Spnda | "92,400 µs (92.4 ms)" |
| 3 | Claimed speedup over semantic entropy | 90,000x | https://github.com/Adarshent/Spnda | "90,000x faster than Semantic Entropy" |
| 4 | Kernel throughput, single core | 1,533,500 evals/sec | https://github.com/Adarshent/Spnda | "1,533,500 evals/sec" |
| 5 | Gateway idle memory (RSS) | 2.98 MB | https://github.com/Adarshent/Spnda | "2.98 MB" |
| 6 | Proxy net latency overhead per request | 0.076 ms (76.3 µs) | https://github.com/Adarshent/Spnda | "0.076 ms (76.3 µs)" |
| 7 | Spanda AUROC on GSM8K at 27B | 0.889 | https://github.com/Adarshent/Spnda | "0.889" (27B row, GSM8K) |
| 8 | Spanda AUROC on TriviaQA at 120B (inverted) | 0.091 | https://zenodo.org/records/22233648 | "causing AUROC to invert to 0.091" |

## Analogy candidates
- **Ask three friends the same question separately**: mapping -- the K sampled answers are three independent askings of the same model; identical answers mean trust it, scattered answers mean it was guessing, and the comparison itself is nearly free. Breaks when: the three friends share one brain -- a heavily tuned 120B model gives the same wrong answer every time (Confident Mode Collapse), so unanimity stops being evidence of truth.
- **The spell-check underline**: mapping -- the red squiggle flags a suspect word on every keystroke without slowing your typing; Spanda stamps every reply with an uncertainty flag for 0.076 ms of overhead. Breaks when: a spellchecker compares your word against a fixed dictionary; here there is no dictionary, only the model compared against itself.

## Misconceptions
- Myth: A confident-sounding answer means the model knows. Reality: tone carries no signal; agreement across repeated samples is the measurable tell, and even that fails when a 120B model collapses onto one wrong answer (AUROC 0.091) (claim 7).
- Myth: Detecting hallucinations needs a second neural network on a GPU. Reality: clustering sampled answers by exact match runs in 652.1 nanoseconds on CPU and the README claims neural-SE-level discrimination on structured reasoning from 7B+ (claims 1, 5).
- Myth: Sub-microsecond means the whole check is free. Reality: only the scoring arithmetic is sub-microsecond; the pipeline still generates K sampled answers through the model first, so end-to-end cost is bounded by sampling (claim 5; see Objection).

## Glossary
- **epistemic uncertainty**: the model's own lack of knowledge, the kind that more or better data would fix.
- **aleatoric uncertainty**: randomness built into the question or data itself, which no amount of training removes.
- **confabulation**: a made-up answer delivered as fact; the subset of hallucinations uncertainty scores can catch.
- **semantic entropy**: the ICLR 2023 / Nature 2024 method that measures uncertainty over meanings by clustering sampled answers with a second neural network.
- **K sampled paths**: asking the same prompt K times (Spanda's wrapper defaults to K=3) and keeping each answer.
- **exact-match clustering**: grouping those sampled answers by identical text instead of by meaning; the move that removes the second neural network.
- **NLI judge (DeBERTa)**: a second neural network that decides whether two sentences mean the same thing; DeBERTa-v3-base has 86M backbone parameters.
- **AUROC**: a 0-to-1 score for how well a signal separates right answers from wrong ones; 0.5 is a coin flip, 1.0 is perfect, below 0.5 is worse than chance.
- **R_sc**: Spanda's 0-to-1 risk score; near 0 means sampled answers agree, toward 1 means they diverge.
- **Rust**: a compiled systems programming language; here, the engine that does the scoring on CPU.
- **gateway (proxy)**: a small server that sits between your app and the model, stamping every reply as it passes through.

## Unverified
- Every latency, memory, throughput and AUROC number in this brief is the author's own benchmark; no third party has replicated any of them, and the Zenodo preprint shows 0 citations.
- Per-token uncertainty scoring is not demonstrated in the repo; the documented modes score K sampled completions per query, so the video should say per reply, not per token.
- Whether the claimed neural-SE parity holds for the quantized 7B-8B models viewers actually run at home; the README's own table shows neural SE ahead on TriviaQA at 7B (0.755 vs 0.698).
- Any tokens-per-second, memory or load-time figure on our own hardware; a first-party measurement on the Spark is pending.
- The name of the 120B frontier model tested is not given on the README's benchmark table, so "120B" cannot be attached to a specific downloadable model.
- Community traction is a snapshot: 13 points and 2 comments on a Show HN thread hours old, 17 stars on the repo.

## Suggested outline
1. Cold open inside the viewer's pain: your local model uses the same confident tone whether it knows or is inventing; this week a Show HN Rust tool scores the inventing in 652.1 nanoseconds on CPU, no second GPU model.
2. Make epistemic uncertainty physical: ask the same question three times and compare; scatter means guessing; the Nature-2024 detector needs a DeBERTa judge at 92,400 µs (92.4 ms) per query, exact-match clustering does the comparable job in 652.1 nanoseconds where answers converge (AUROC 0.889 at 27B on GSM8K).
3. What it buys locally tonight and where it breaks: a 2.98 MB gateway beside Ollama stamping every reply (X-Spanda-Rsc, 0.076 ms overhead); the honest catch -- only the scoring is sub-microsecond, sampling K=3 still costs full model runs, and at 120B unanimity inverts (AUROC 0.091), so agreement is evidence, not truth.

## Viewer situation
You've got Ollama (or another local model) on your gaming PC or Mac, and no way to tell which confident-sounding answers are made up.

## Has process
`true`
- Install the SDK with `pip install spnda` (Python 3.8+, zero third-party dependencies).
- Wrap your existing OpenAI-compatible client with `client = spanda.wrap(OpenAI(), k=3, threshold=0.35, block=False)`.
- Ask your question through the wrapped client and read `response.spanda.rsc`: near 0 means the sampled answers agreed, toward 1 means the model is guessing.
- Or run the Rust gateway beside your local server: `spnda serve --upstream http://localhost:11434/v1 --port 8080 --block --k 3`, then point your app at `http://localhost:8080/v1`.
- Watch the `X-Spanda-Rsc` header on every reply (`0.0000` = unanimous consensus).

## Objection
The 652.1 nanoseconds is only the scoring arithmetic -- you still generate K=3 sampled answers through the whole model first, and at 120B scale a heavily tuned model repeats the same wrong answer on every sample (AUROC 0.091), so cheap agreement is not truth.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/Adarshent/Spnda | GitHub - Adarshent/Spnda: Zero-cost epistemic uncertainty quantification & hallucination detection for LLMs | primary | plain fetch | 2026-09-12 |
| 2 | https://news.ycombinator.com/item?id=49663329 | Spanda: Sub-microsecond LLM epistemic uncertainty in Rust -- Hacker News | community | plain fetch | 2026-09-12 |
| 3 | https://arxiv.org/abs/2302.09664 | Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation | primary | plain fetch | 2026-09-12 |
| 4 | https://www.nature.com/articles/s41586-024-07421-0 | Detecting hallucinations in large language models using semantic entropy -- Nature | primary | plain fetch | 2026-09-12 |
| 5 | https://pypi.org/project/spnda/ | spnda 0.3.0 -- PyPI | primary | plain fetch | 2026-09-12 |
| 6 | https://zenodo.org/records/22233648 | Spanda: Zero-Cost Lexical Entropy Matches Neural Semantic Uncertainty--Until Frontier Models Break It -- Zenodo | primary | plain fetch | 2026-09-12 |
| 7 | https://huggingface.co/microsoft/deberta-v3-base | microsoft/deberta-v3-base -- Hugging Face | primary | plain fetch | 2026-09-12 |
| 8 | https://arxiv.org/abs/2203.11171 | Self-Consistency Improves Chain of Thought Reasoning in Language Models | primary | plain fetch | 2026-09-12 |
| 9 | https://arxiv.org/abs/1703.04977 | What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision? | primary | plain fetch | 2026-09-12 |
| 10 | https://ollama.com/ | Ollama | primary | plain fetch | 2026-09-12 |
| 11 | https://news.ycombinator.com/item?id=49665875 | Show HN: Spanda -- Sub-microsecond LLM epistemic uncertainty in Rust -- Hacker News | community | plain fetch | 2026-09-12 |

## Notes
Tools: FIRECRAWL_API_KEY was set but the FireCrawl API returned HTTP 402 (insufficient credits) on scrape and search; per rules/firecrawl-usage.md the run fell back to plain fetch (agent web_extract) for all 11 pages and 1 web search, all successful. Number variance to keep honest: three kernel figures appear in first-party text -- 652.1 ns (system table), 760 ns (HN text post), 767.9 ns (README bench output); treat "under 1 µs / 652.1 ns as published" as the robust form. Conflict: the README's parity claim ("At 7B+ parameters, Spanda achieves the exact same discriminative power") is about structured reasoning; its own Mistral-7B TriviaQA row has neural SE ahead 0.755 vs 0.698 -- the channel can defend "matches on converging, structured answers; not on trivia recall". Naming quirk for the writer: repo Spnda, PyPI package spnda, Python import spanda. DeBERTa-v3-base is 86M backbone parameters (HF model card) -- a concrete "second brain" size contrast against the 2.98 MB gateway. Ollama fetched for the local payoff ("Nothing you run locally ever leaves your machine"; "Local models are always free") -- supports the viewer-situation framing, no claim needed. Repo shows 21 commits, latest dated Sep 11, 2026, 17 stars; Zenodo preprint v1 published September 1, 2026.

## Decisions
- Checkpoint (stage 03): angle confirmed as "an LLM can tell you it is guessing in under a millionth of a second -- here is what that buys you locally"; confirmed per unattended rule.
- Source depth: 11 sources, 11 fetched via plain fetch (FireCrawl key present but HTTP 402 insufficient credits; fallback per rules/firecrawl-usage.md).
