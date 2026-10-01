---
slug: 2026-10-01-llmxray-local-llm-observabilit
stage: 03-research
topic: "llmxray: local LLM observability you can install tonight"
depth: standard
generated_at: 2026-10-01T11:43:05Z
sources: 12
hub: "[[videos/2026-10-01-llmxray-local-llm-observabilit]]"
---

# Research brief: llmxray -- local LLM observability you can install tonight

## Summary
The thesis: one free command gives the local model you already run a live instrument panel, and the first thing it shows you is a cost you never knew you were paying. The most arresting number: an identical 324-token prompt where moving one timestamp turns 4 reused tokens into 290 and drops prefill from 64.6 ms to 18.6 ms, "3.5x faster, same words." The strongest concrete case is that exact scenario, measured by the tool's Cache Lab against the viewer's own running daemon, alongside the discovery that Ollama 0.33.3 silently broke the standard prefill math (4375 tok/s reported where the honest figure was 115 tok/s). What could not be verified: any tokens-per-second on real viewer hardware, the README's "30 seconds" install claim, whether the Docker image covers Apple Silicon, and community reception (Reddit would not load through the fetch tool). One conflict matters to the writer: the pick says the tool was open-sourced about 22 h ago, but the repo's first release is dated 2026-03-14 -- what is 22 h old is the author's fresh Hacker News post, and the GitHub and npm README snapshots also disagree on the verified Ollama version (0.34.x vs 0.33.x).

## Thesis
One command, npx llmxray, gives the Ollama model already on your PC an instrument panel: every token colored by speed, quiet failures badged, and what your prompt's layout costs each turn measured in milliseconds on your own hardware.

## Explanation path
Start inside the viewer's blind spot: they chat with a local model and see only finished words, so establish the token as the unit of watching -- a model writes one small chunk at a time, and how fast each chunk arrives is information a normal chat window throws away. Once the unit exists, Ollama stops being a mystery download and becomes an engine that already publishes gauges on localhost: token counts, timings, and cache-reuse numbers. LLMxRay is then simply the dashboard that reads those gauges: it starts with one command, it colors each token by how fast it arrived, and it raises a badge only when something is actually wrong (repetition, refusal, gibberish, empty, truncation). The scenario that carries the whole script is the timestamp: a single changing value near the top of a prompt forfeits all KV-cache reuse below it, and Cache Lab measures that cost against the viewer's own daemon -- 64.6 ms of prefill against 18.6 ms for identical words. Land the honesty the channel owes before the close: the confidence coloring is a timing approximation rather than real probabilities (real logprobs appear only in the benchmark path), and Ollama's 0.33.3 metric change means naive prefill math over-reports 38x, which is exactly why seeing the raw numbers beats assuming them.

## Claims
1. **LLMxRay installs and runs with one command, `npx llmxray`, then serves a local web UI at http://localhost:5174.**
   - Source: GitHub - LogneBudo/llmxray: LLMxRay -- Local LLM Observatory, https://github.com/LogneBudo/llmxray
   - Tier: primary | Confidence: high | Accessed: 2026-10-01 | Via: web_extract
   - Quote: "npx llmxray ... Open http://localhost:5174 and start chatting. That's it."
2. **The prerequisite is Ollama running locally with at least one model pulled, for example `ollama pull llama3.2`.**
   - Source: GitHub - LogneBudo/llmxray: LLMxRay -- Local LLM Observatory, https://github.com/LogneBudo/llmxray
   - Tier: primary | Confidence: high | Accessed: 2026-10-01 | Via: web_extract
   - Quote: "Prerequisite: Ollama running locally with at least one model pulled (ollama pull llama3.2)."
3. **In the chat view, tokens arrive one by one colored by generation speed, showing where the model hesitates.**
   - Source: GitHub - LogneBudo/llmxray: LLMxRay -- Local LLM Observatory, https://github.com/LogneBudo/llmxray
   - Tier: primary | Confidence: high | Accessed: 2026-10-01 | Via: web_extract
   - Quote: "Chat Diagnostics -- Watch tokens arrive one by one, coloured by speed. See where the model hesitates, and what it was unsure about."
4. **The chat confidence coloring is an approximation inferred from inter-token latency and labeled as such; real logprobs are used only by the benchmark, via the OpenAI-compatible endpoint.**
   - Source: GitHub - LogneBudo/llmxray: LLMxRay -- Local LLM Observatory, https://github.com/LogneBudo/llmxray
   - Tier: primary | Confidence: high | Accessed: 2026-10-01 | Via: web_extract
   - Quote: "Token confidence -- Approximated from inter-token latency (faster = more confident). Clearly labeled as approximation. Benchmarks use real logprobs via OpenAI-compatible endpoint."
5. **Cache Lab, new in 0.6.0, measures KV-cache reuse against your own daemon; on the maintainer's real 324-token prompt, a timestamp at the front left 4 tokens reused and 64.6 ms of prefill, while at the back 290 were reused and 18.6 ms, "3.5x faster, same words."**
   - Source: GitHub - LogneBudo/llmxray: LLMxRay -- Local LLM Observatory, https://github.com/LogneBudo/llmxray
   - Tier: primary | Confidence: high | Accessed: 2026-10-01 | Via: web_extract
   - Quote: "Measured on a real 324-token prompt: 4 tokens reused and 64.6 ms of prefill with the timestamp at the front, 290 reused and 18.6 ms with it at the back. 3.5x faster, same words. Requires Ollama 0.33.3+."
6. **Ollama 0.33.3 redefined `prompt_eval_duration` to cover only uncached prompt tokens, so the standard prefill formula over-reports: the maintainer's own tooling showed 4375 tok/s where the honest figure was 115 tok/s, a 38x over-report.**
   - Source: Ollama 0.33.3 changed what prompt_eval_duration measures | LLMxRay, https://lognebudo.github.io/llmxray/docs/en/articles/ollama-prefill-metrics.html
   - Tier: primary | Confidence: high | Accessed: 2026-10-01 | Via: web_extract
   - Quote: "On a warm cache, my own tooling reported 4375 tok/s where the honest figure was 115 tok/s. That's a 38x over-report, with no error, no warning, and no version signal beyond the presence of a new field."
7. **The maintainer posted the project to Hacker News as "Local LLM Observability" about 22 hours before this fetch, where it sat at 1 point with no comments.**
   - Source: Local LLM Observability | Hacker News, https://news.ycombinator.com/item?id=49908457
   - Tier: community | Confidence: medium | Accessed: 2026-10-01 | Via: web_extract
   - Quote: "1 point by lognebudo 22 hours ago"
8. **The project is older than the fresh attention: the changelog dates the initial 0.1.0 release to 2026-03-14 and Cache Lab's 0.6.0 release to 2026-09-14.**
   - Source: llmxray/CHANGELOG.md at master, https://github.com/LogneBudo/llmxray/blob/master/CHANGELOG.md
   - Tier: primary | Confidence: high | Accessed: 2026-10-01 | Via: web_extract
   - Quote: "[0.1.0] -- 2026-03-14 ... Initial release: real-time chat with token streaming, confidence coloring, session history, introspection visualizations, and prompt anatomy analysis ... [0.6.0] -- 2026-09-14"
9. **The mainstream alternative for observing Ollama models, documented by Langfuse, sends traces to Langfuse Cloud or a self-hosted Langfuse server, while LLMxRay's pitch is no cloud, no API keys, everything on localhost.**
   - Source: Ollama Observability and Tracing for Local LLMs - Langfuse, https://langfuse.com/integrations/model-providers/ollama
   - Tier: docs | Confidence: high | Accessed: 2026-10-01 | Via: web_extract
   - Quote: "Use Langfuse Cloud (hosted by Langfuse, free tier, no infrastructure to run) or self-host it. ... For this example, we will use the Langfuse cloud version."
10. **LLMxRay also ships as an 88.8 MB Docker image, djovaneli/llmxray, serving on port 5174 with OLLAMA_URL defaulting to http://host.docker.internal:11434.**
    - Source: djovaneli/llmxray - Docker Image, https://hub.docker.com/r/djovaneli/llmxray
    - Tier: primary | Confidence: high | Accessed: 2026-10-01 | Via: web_extract
    - Quote: "Size 88.8 MB ... OLLAMA_URL | http://host.docker.internal:11434 | Ollama instance URL"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | prefill, timestamp at front of a 324-token prompt | 64.6 ms | https://github.com/LogneBudo/llmxray | "4 tokens reused and 64.6 ms of prefill with the timestamp at the front" |
| 2 | prefill, same prompt with timestamp at the back | 18.6 ms | https://github.com/LogneBudo/llmxray | "290 reused and 18.6 ms with it at the back" |
| 3 | prompt tokens reused, timestamp at front | 4 tokens | https://github.com/LogneBudo/llmxray | "4 tokens reused and 64.6 ms of prefill with the timestamp at the front" |
| 4 | prompt tokens reused, timestamp at back | 290 tokens | https://github.com/LogneBudo/llmxray | "290 reused and 18.6 ms with it at the back" |
| 5 | prefill speedup from moving one timestamp, identical words | 3.5x | https://github.com/LogneBudo/llmxray | "3.5x faster, same words." |
| 6 | prefill throughput by the old formula, warm cache (qwen2.5:7b, 37 of 38 tokens cached) | 4375 tok/s | https://lognebudo.github.io/llmxray/docs/en/articles/ollama-prefill-metrics.html | "my own tooling reported 4375 tok/s where the honest figure was 115 tok/s" |
| 7 | honest prefill throughput for that same request | 115 tok/s | https://lognebudo.github.io/llmxray/docs/en/articles/ollama-prefill-metrics.html | "my own tooling reported 4375 tok/s where the honest figure was 115 tok/s" |
| 8 | Ollama's stated developer scale | 8.9 million developers | https://ollama.com/blog | "Serving 8.9 million developers, Ollama has raised $88M from Benchmark, Theory Ventures, 8VC, Y Combinator, and many incredible angel investors." |

## Analogy candidates
- **Vehicle: the car dashboard and OBD-II scanner**. Mapping: the engine (your Ollama model) already has sensors; the dashboard and a cheap scanner just make them readable. LLMxRay reads numbers Ollama already emits on localhost and turns them into gauges and warning lights. Breaks when: a dashboard can only display what a sensor reports -- it cannot fix the engine, and its "confidence" gauge is inferred from timing rather than read from a real probability sensor.
- **Vehicle: the X-ray in the project's own name**. Mapping: an X-ray sees through the polished surface of an answer to the structure underneath: tokens, per-token timing, cache reuse. Breaks when: an X-ray shows structure, not intent -- colored tokens show where generation slowed, never why the model chose a word, so the script must not claim it reads the model's mind.

## Misconceptions
- Myth: The token colors show the model's real confidence, like a probability meter. Reality: chat coloring approximates confidence from how fast each token arrived, and the app labels it as an approximation; real logprobs appear only in the benchmark path (claim 4).
- Myth: Prompt layout is cosmetic -- the model just reads whatever you send, fresh, every turn. Reality: KV-cache reuse survives only while the prompt still matches from its very first token, so one changing timestamp near the top forfeits everything below it (claim 5).
- Myth: Observing an LLM means piping traces to a cloud dashboard. Reality: the documented mainstream path does exactly that (Langfuse Cloud or a self-hosted server), while LLMxRay claims no cloud, no API keys, no cost, all on localhost (claim 9).

## Glossary
- **token**: A chunk of text, usually part of a word, that a language model reads and writes one at a time.
- **tokens per second**: How many of those chunks the model produces each second on your hardware -- the local speedometer.
- **Ollama**: A free app that downloads and runs language models on your own machine and serves them on a local address, localhost:11434.
- **observability**: Tooling that shows what a system is doing while it runs, not just what it finally outputs.
- **prefill**: The work a model does reading your prompt before it writes the first token of its answer.
- **KV cache**: The model's saved memory of having read your prompt; it can be reused only while the prompt still matches from its very first token.
- **logprobs**: The actual numeric probabilities a model assigns to each candidate token -- the honest version of a confidence score.
- **npx**: A command bundled with Node.js that downloads and runs a package once, without a permanent install.
- **time to first token (TTFT)**: How long you wait after sending a prompt before the first token appears.

## Unverified
- How many tokens per second the viewer's own GPU or Mac will actually show; nothing was measured on our hardware this run.
- That `npx llmxray` really finishes in 30 seconds on a typical machine; that is the README's claim, not a timed install.
- That the Docker image djovaneli/llmxray runs on Apple Silicon; the Docker Hub page fetched lists no CPU architectures.
- Community reception of the tool beyond the author's own posts; Reddit threads would not load through the fetch tool, so no sentiment was read.

## Suggested outline
1. Hook on the hidden cost: the same 324-token prompt, one timestamp moved, 4 reused tokens become 290 and 64.6 ms of prefill becomes 18.6 ms -- 3.5x faster, same words, and no normal chat window ever shows you this.
2. Name the blind spot and the instrument: your Ollama model already reports what it is doing on localhost, and llmxray is the free panel that reads it -- one command, npx llmxray, tokens arriving colored by speed, badges only when something is wrong.
3. Honest catch and payoff: the colors are a speed-based approximation, not real probabilities, and Ollama's own metric change quietly inflated naive prefill math to 4375 tok/s where the truth was 115 tok/s -- and still, the whole rig runs on your box, no cloud, no API keys, installed tonight.

## Viewer situation
You already run Ollama with a small model like llama3.2 on your own gaming PC or Mac, you chat with it in a plain window, and you have never seen a single number about what it is doing underneath.

## Has process
`true`
- Install Ollama from ollama.com and pull a model with `ollama pull llama3.2`.
- Check that Node.js 18 or newer is installed (needed for the npx route).
- Run `npx llmxray` in a terminal (or `docker run -p 5174:5174 djovaneli/llmxray`).
- Open http://localhost:5174 in a browser and confirm the header shows Connected.
- Send a chat message and watch tokens arrive colored by generation speed.
- Open Cache Lab, measure a prompt that has a changing value near the top, and read the reuse numbers on your own daemon.

## Objection
Anyone can read these numbers straight from Ollama's API with two curl calls, and the token "confidence" is just latency re-labeled, so this is a convenience UI, not new instrumentation.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://github.com/LogneBudo/llmxray | GitHub - LogneBudo/llmxray: LLMxRay -- Local LLM Observatory | primary | web_extract | 2026-10-01 |
| 2 | https://news.ycombinator.com/item?id=49908457 | Local LLM Observability \| Hacker News | community | web_extract | 2026-10-01 |
| 3 | https://hn.algolia.com/api/v1/search?query=llmxray | hn.algolia.com search: llmxray (story dates) | community | web_extract | 2026-10-01 |
| 4 | https://www.npmjs.com/package/llmxray | llmxray - npm | primary | web_extract | 2026-10-01 |
| 5 | https://lognebudo.github.io/llmxray/docs/en/articles/ollama-prefill-metrics.html | Ollama 0.33.3 changed what prompt_eval_duration measures \| LLMxRay | primary | web_extract | 2026-10-01 |
| 6 | https://hub.docker.com/r/djovaneli/llmxray | djovaneli/llmxray - Docker Image | primary | web_extract | 2026-10-01 |
| 7 | https://ollama.com/blog | Blog - Ollama | primary | web_extract | 2026-10-01 |
| 8 | https://github.com/LogneBudo/llmxray/blob/master/CHANGELOG.md | llmxray/CHANGELOG.md at master | primary | web_extract | 2026-10-01 |
| 9 | https://langfuse.com/integrations/model-providers/ollama | Ollama Observability and Tracing for Local LLMs - Langfuse | docs | web_extract | 2026-10-01 |
| 10 | https://news.ycombinator.com/item?id=47424349 | Show HN: LLMxRay an open-source observability tool for LLMs \| Hacker News | community | web_extract | 2026-10-01 |
| 11 | https://ollama.com/library/llama3.2 | llama3.2 - Ollama library | primary | web_extract | 2026-10-01 |
| 12 | https://lognebudo.github.io/llmxray/docs/en/guide/installation.html | Installation \| LLMxRay | primary | web_extract | 2026-10-01 |

## Notes
- Why-now conflict: the pick says llmxray "was open-sourced about 22 h ago," but the changelog dates the first release to 2026-03-14 and npm shows 0.6.0 published 17 days before this fetch; what is about 22 h old is the author's HN post "Local LLM Observability" (2026-09-30 13:11 UTC per HN's search API). The script should say "just posted to Hacker News," never "released yesterday."
- HN traction at fetch time was 1 point and 0 comments, so "being discussed on Hacker News" is thin; an earlier Show HN for the same project exists from 2026-03-18, also at 1 point.
- Version conflict: the GitHub README says tested against Ollama 0.34.x (verified on 0.34.0, September 2026); the npm README snapshot still says 0.33.x (verified on 0.33.3). Trust the GitHub README as the newer statement; either way Cache Lab needs Ollama 0.33.3+.
- The 3.5x figure is the maintainer's own illustration: his Limits section says one model, one daemon, one prompt size, llama.cpp runner, and that the specific ratio is "an illustration, not a benchmark." Quote it only with that hedge.
- The maintainer states the whole prefill finding is reproducible without his tool: "two curl calls and prompt_eval_cached_count reproduce every table here" -- useful for the objection beat.
- The Reddit r/ollama thread "How I handle LLM observability and evals with Ollama" could not be fetched (scraper blocked), so it is a lead, not a source.

## Decisions
- Stage-03 checkpoint: angle confirmed as "llmxray makes what a local Ollama model is doing visible token by token on your own box," serving the how-to pick with one carry scenario (the cache-killing timestamp) for the smooth explainer; slug unchanged.
- Source depth: 12 sources fetched via web_search discovery + web_extract one at a time (FIRECRAWL_API_KEY absent), yielding 10 claims and 8 key numbers, within the standard band.
