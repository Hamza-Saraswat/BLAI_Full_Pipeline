# Test findings: local dry run, 2026-08-23

Everything the dry run catches, in the order it was caught. Branch `test/dry-run-2026-08-23`.

Severity: **blocker** stops a real run; **quality** ships bad work; **friction** costs time or trust; **blocked** cannot be tested here.

| # | Stage | Severity | Finding | Status |
|---|-------|----------|---------|--------|
| 1 | 01 radar | quality | No relevance gate: Hacker News ranks by discussion volume, so a missing-crypto-executive story scored 49 and a marathon-medal story 38, both with no product and no AI topic, and both landed in the top 10 | **fixed** |
| 2 | 01 radar | quality | Lane assignment classifies the *source*, not the video you could make: 54 of 64 items landed in `news-react` because GitHub releases and HN posts are news-shaped. A llama.cpp release is equally a how-to or a myth-bust | open |
| 3 | 01 radar | blocked | Reddit returns 403 without OAuth. r/LocalLLaMA is where myth-bust and explainer material lives, so without it the radar is a release feed, which is most of the cause of finding 2 | blocked on credentials |
| 4 | 02 ideas | blocked | No YouTube key and no vidIQ connector, so competition and volume are unmeasured and every competition z-score is 0.00. Opportunity collapses to autocomplete depth, which rewards broad brand keywords | blocked on credentials |
| 5 | 02 ideas | quality | **Search demand is structurally blind to breaking news, and credentials will not fix it.** "ollama claude desktop" scored depth 1 and ranked last of 11; the Ollama and Claude Desktop integration shipped three hours before the sweep and is arguably the biggest story in the window. vidIQ volume for a one-day-old phrase is also near zero | open |

| 6 | 03 research | friction | Research depth is real but source count is below the contract: 4 fetched sources per pick against the 8-12 the scope file asks for. Without FireCrawl every source is one WebFetch, so depth costs wall-clock rather than money | open |
| 7 | 03 research | quality | **The two briefs each surfaced a source contradiction the writer would otherwise have spoken as fact.** Unsloth: the release notes describe LAN access as shipped while issue 9207 still reads open and unresolved. Ornith: Terminal-Bench 2.1 is 46.2 on the model card and 47.0 in secondary coverage, and the card claims a single 80GB GPU while giving the BF16 size as ~19 GB | working as designed |

## Detail

### 1. Radar relevance gate (fixed)

Live run, 82 candidates. `Four Years Ago, a Crypto Boss Went Missing` scored 49 on 50 points and 16 comments; `Sydney Marathon medal mistakenly depicts Munich stadium` scored 38. Both had `products: []` and an empty summary. Fix: an item must name a known product or carry one topic term (about 35 patterns: llm, local ai, gpu, vram, quantization, kv cache, tokens per second, inference, mixture of experts and the rest) in its title, summary or URL. Re-run dropped 17 of 81. Deliberately generous: `ai` alone passes.

Files: `skills/trend-radar/scripts/scoring.py` (`relevance()`, `TOPIC_TERMS`), `scripts/radar.py` (gate after dedupe, count on the stats line), `rules/scoring.md`.

### 2. Lane assignment classifies the source (open)

Observed spread: news-react 54, how-to 2, explainer 2, enterprise-privacy 2, myth-bust 0, comparison 0. The selection rules require the two daily picks to come from different lanes with at most one news-react, so on this digest the second pick had six items to choose from. It did not block the run because the ideas stage assigns a lane per candidate, but a one-dimensional digest biases the writer toward news-react.

Proposed fix, not yet applied: the radar should tag an item with the lanes it *could* serve rather than the one its source implies, or drop lane grouping from the digest and let the ideas stage own it entirely.

### 3. Reddit dead without OAuth (blocked)

`[radar] reddit: every subreddit failed`. The public `.json` endpoint answers 403 to this client regardless of user agent. Moves Reddit credentials up the priority list: free, and the cheapest fix for topic variety.

### 4 and 5. Opportunity scoring (blocked, and open)

Live autocomplete depths: unsloth 57, ornith 1.5 34, deepseek api pricing 17, abliterated model 16, local llm quality 14, local whisper dictation 14, sglang 12, local text to speech 10, qwen 3.8 27b 7, ollama claude desktop 1, ollama time to first token 0. With competition unmeasured, `opportunity = 50 + 15 x z(depth) + 10 for a named product`, so the ranking is a popularity contest between keywords.

The structural half of the problem: a story that broke this morning has no search history, so both autocomplete and vidIQ score it near zero forever. Proposed fix, not yet applied: measure demand per lane. Evergreen lanes keep autocomplete and vidIQ volume; `news-react` uses the story's spread, which the radar already computes as `signals.signal` and the ideas stage currently discards.

### 6. Research depth without FireCrawl (open)

Each brief cites 4 distinct fetched URLs and 7 claims. `shorts-research-scope.md` asks for 8-12 sources at standard depth. Nothing failed, because `validate_research.py` enforces claim count and URL presence rather than source count, but the briefs are thinner than production would be. With a FireCrawl key the search-and-scrape loop gets cheaper and wider; without it every source is a separate fetch and depth is bounded by patience rather than by budget.

### 7. Contradictions surfaced rather than swallowed (working as designed)

This is the research stage doing its job, and it is worth recording as evidence rather than as a defect.

**Unsloth.** The v0.1.801-beta release notes describe LAN Remote Access as shipped in preview with a Settings section, QR codes and a forced password change. Issue 9207, which asked for exactly this feature, still reads as open with no maintainer response and a user-documented batch-file workaround. One of the two is stale. The brief's `unverified` list says so and tells the writer not to claim the issue was closed by the release.

**Ornith.** Terminal-Bench 2.1 is 46.2 on the model card and 47.0 in secondary coverage, so the brief forbids speaking the number without picking one. The same card says the model "serves on a single 80GB GPU" in BF16 while giving the BF16 size as ~19 GB; the 80GB line looks inherited from the 397B family member. Every benchmark is self-reported, though with unusually strict controls (five runs averaged, git history stripped, network disabled during solving), and the brief records both halves of that.

Both briefs also carry the three new writer fields. `has_process` is true for Unsloth with four real steps and false for Ornith, which means positional labels are legal in one script and banned in the other. That is the first live exercise of the label rule.
