# Citation Rules

A claim the writer cannot trace is a claim the video cannot make (`brand-vault/voice-rules.md`, Hard Constraint 6). These rules decide what may appear under Claims and Key numbers.

## Source tiers (`source_quality` in the JSON)

| Tier | Value | What counts | Typical pages |
|------|-------|-------------|---------------|
| 1 | `primary` | first-party and primary documents: the vendor's release notes or model card, the paper, official docs, the official pricing page, a court filing, a regulator's published text | `huggingface.co/<org>/<model>`, `github.com/<org>/<repo>/releases`, `arxiv.org/abs/...`, vendor docs, eur-lex, a court's PDF |
| 2 | `docs` | reputable secondary material with an editorial process: a runtime's maintained documentation, an explainer by a named organisation (Hugging Face blog, NVIDIA technical blog), major tech press with a byline and a date | docs sites, organisation blogs, reported news |
| 3 | `benchmark` | measured numbers from a named harness or reviewer whose method is shown and reproducible | Artificial Analysis, LMArena, llama.cpp discussions with commands and hardware listed, independent reviews with methodology |
| 4 | `community` | reddit, Hacker News, X posts, forums, personal blogs, YouTube comments | sentiment, anecdotes, "people report"; never the sole source of a number |

- A number under Key numbers needs a tier 1-3 page. A tier 4 number goes under Unverified unless a tier 1-3 page corroborates it, in which case cite the corroborating page.
- Prefer the most primary page that states the fact. A blog post quoting a model card is tier 2; the model card is tier 1; fetch the model card.
- Conflicts: record both sources, say which you trust and why under Notes. Do not average them.
- `confidence`: `high` when a tier 1-2 page states the fact directly; `medium` when it is inferred, dated, secondary, or the page hedges.

## What counts as fetched

- A page counts as fetched only when a tool returned its content in this session (`firecrawl_scrape` markdown, a `WebFetch` result) and the agent read the passage that supports the claim.
- Does not count: a search result snippet, training knowledge, a URL seen in another page's link list, a page that returned an error or an empty body, a summary cached from a previous run, a subagent saying it "knows" the page.
- Never invent, guess, shorten or "reconstruct" a URL. If you cannot fetch it, it does not exist for this brief.
- `accessed` is the run date in ISO form. Record the URL actually fetched (the final URL after redirects when the tool reports it), stripped of tracking parameters.
- The Sources table lists only fetched pages and which tool fetched each. Every URL under Claims and Key numbers appears in Sources.

## Verbatim-number rule

- Every number under Claims, Key numbers and in the JSON `key_numbers[].value` is copied exactly as the page states it: same digits, same unit, same qualifier ("up to", "about", "per million tokens", "at Q4_K_M").
- Keep the page's unit in the brief. The script stage rounds for the ear and the storyboard validator checks the referent. When two sources use different units, give the verbatim form first and a converted form in parentheses: `273 GB/s (0.273 TB/s)`.
- No number without its unit and referent: `3.3B active parameters per token`, not `3.3B`. A price carries the plan and the date it was seen: `$0.14 per million input tokens (API pricing page, 2026-08-25)`.
- Each numeric claim in the markdown carries the quote, the sentence the number came from. In the JSON the claim text itself states the number verbatim and `key_numbers[].value` repeats it.
- Benchmarks carry the harness and the setting (`MMLU-Pro 78.1 (5-shot)`); throughput carries the hardware and quantisation; memory carries the context length when the page gives it.

## What goes under Unverified

- Beliefs and common knowledge the agent did not fetch a page for.
- Numbers found only in community sources.
- Claims from a page that would not load or returned an empty body.
- Anything our own hardware should measure (tokens per second on the Spark, load time, memory). Phrase it as the expectation; `skills/dgx-capture` supplies the measurement and the reconcile step rewrites the narration line.
- Write each as one plain sentence the writer can hedge or drop, never as a claim with a fake source.
