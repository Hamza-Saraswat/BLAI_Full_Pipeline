---
slug: 2026-11-22-qwen3-8-27b-overthinks-your-co
stage: 03-research
topic: "Qwen3.8-27B overthinks coding tasks: the knobs that cut the waste"
depth: standard
generated_at: 2026-11-22T12:40:00Z
sources: 10
hub: "[[videos/2026-11-22-qwen3-8-27b-overthinks-your-co]]"
---

# Research brief: Qwen3.8-27B overthinks coding tasks: the knobs that cut the waste

## Summary
The throttle is set wrong at the factory, not the engine: xhigh thinking is the chat template's fallback, one SVG prompt took 21 minutes and 22,276 reasoning tokens for 3,223 tokens of output, and setting effort to medium buys essentially the same code for a fraction of the cost (78.2 vs 78.8 median score, 8x the tokens, 11x the wall clock). The strongest concrete case is penberg.org's dwim-vs-OpenCode eval: the same model resolved 64% vs 52% of SWE-bench Verified Mini issues while thinking about a quarter as much (6,270 vs 22,610 median tokens) and taking 55 s vs 169 s, using a 2,048-token thinking cap plus act-don't-recall closing sentences. Qwen's own model card undercuts the free-lunch story: in multi-turn agentic tasks lower effort can cause retries that raise total time and tokens. The soft edge of the fix: reasoning_effort is an injected instruction phrase, not a hard linkage, so a thinking budget is the only mechanical backstop. The model itself runs local at 4-bit in 16-19GB, so a 24GB card or Mac covers the hardware bar.

## Thesis
Your Qwen3.8-27B isn't a slow coder -- it ships with its thinking dial glued to maximum, and one flag plus a hard cap turn it into a fast one.

## Explanation path
Start from the symptom a local coder already knows: you ask for a small edit, the model disappears into its thinking trace, and on a loaded context of 8,192 tokens the thinking alone can eat the window before any code appears. Name the actor before the knobs: Qwen3.8-27B is a dense 27B model that codes at the frontier of what runs at home (SWE-bench Pro 61.7, LiveCodeBench v6 90.3), so the viewer is not compensating for a weak model -- that fact earns respect for the machine before we criticize its default. Then show where the waste lives: thinking is on by default, the effort dial has three stops (xhigh, medium, low), and the template's fallback line hands every caller that sets nothing the most expensive stop; that is why IDE harnesses that never send the flag sit at roughly 60K thinking tokens per turn with 40+ second time-to-first-token. With the mechanism named, the first knob is almost anticlimactic: pass reasoning_effort low or medium and the same model answers in ~80 seconds instead of ~14 minutes, at the same median score. But honest coverage needs the second half: the dial is an injected instruction, not a hard linkage -- engines can ignore it, wrong keys silently fall back to xhigh -- so the mechanical fix is a thinking budget, a hard token cap like dwim's 2,048 or oMLX's tested 12,000, paired with what the model is told when the cap hits: act now, read the code, decide from the output already in context. Close on the boundary Qwen itself draws: lower effort is not always fewer total tokens in multi-turn agent runs, because retries; the dial and the cap are the right tools, used with eyes open.

## Claims
1. **Thinking mode is on by default and `reasoning_effort` has three levels, with `xhigh` the default.**
   - Source: Qwen/Qwen3.8-27B model card, https://huggingface.co/Qwen/Qwen3.8-27B
   - Tier: primary | Confidence: high | Accessed: 2026-11-22 | Via: web_extract
   - Quote: "Thinking mode is on by default and can be disabled per request; reasoning depth can be tuned with `reasoning_effort`"
2. **The xhigh default is a chat-template fallback line, so any caller that sets nothing silently gets maximum thinking.**
   - Source: Qwen3.8-27B has the best coding ceiling you can run at home, and it ships on maximum effort, https://llm-bench.io/guides/qwen3-8-27b-reasoning-effort
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-22 | Via: web_extract
   - Quote: "{%- set resolved_reasoning_effort = reasoning_effort|default('xhigh') %}"
3. **Simon Willison measured the xhigh default at 21 minutes and 22,276 reasoning tokens for 3,223 tokens of output on one prompt, versus 137s and 3,715 tokens with reasoning off.**
   - Source: Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things, https://simonw.substack.com/p/qwen-38-27b-is-excellent-but-it-defaults
   - Tier: community | Confidence: high | Accessed: 2026-11-22 | Via: web_extract
   - Quote: "It took **21 minutes** to generate, using 22,276 reasoning tokens to produce 3,223 tokens of output."
4. **On one M5 Max run, low and medium effort cost about the same (4,984 and 4,792 median tokens, 84 s and 77 s) while xhigh cost ~8x the tokens and ~11x the wall clock for ~0.5 median score gain (78.8 vs 78.2).**
   - Source: Qwen3.8-27B has the best coding ceiling you can run at home, and it ships on maximum effort, https://llm-bench.io/guides/qwen3-8-27b-reasoning-effort
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-22 | Via: web_extract
   - Quote: "It costs eight times the tokens and eleven times the wall clock, fourteen minutes a question instead of seventy-seven seconds. In return the median coding score moves from 78.2 to 78.8, about half a point."
5. **penberg.org's mitigations beat OpenCode with the same model: 64% vs 52% of 50 SWE-bench issues resolved, thinking about a quarter as much (median 6,270 vs 22,610 tokens) in about a third of the time (55 s vs 169 s).**
   - Source: Why Qwen3.8-27B Overthinks in Coding Tasks and How to Mitigate That, https://penberg.org/blog/qwen38-overthink.html
   - Tier: primary | Confidence: high | Accessed: 2026-11-22 | Via: web_extract
   - Quote: "dwim resolved 64% of the issues against OpenCode's 52%, while thinking about a quarter as much and taking a third of the time on the median issue."
6. **dwim's core mitigations are a 2,048-token hard thinking cap plus replacement closing sentences that push the model to act on what is in context rather than recall from memory.**
   - Source: Why Qwen3.8-27B Overthinks in Coding Tasks and How to Mitigate That, https://penberg.org/blog/qwen38-overthink.html
   - Tier: primary | Confidence: high | Accessed: 2026-11-22 | Via: web_extract
   - Quote: "In dwim, I ended up picking 2048 tokens as the hard limit based on what I empirically saw in SWE-bench thinking traces."
7. **The root failure mode is reasoning from memory about code it could simply read -- looping on "I think", "I recall", "wait" -- instead of acting on the code and tool output already in its context.**
   - Source: Why Qwen3.8-27B Overthinks in Coding Tasks and How to Mitigate That, https://penberg.org/blog/qwen38-overthink.html
   - Tier: primary | Confidence: high | Accessed: 2026-11-22 | Via: web_extract
   - Quote: "the model was rarely reasoning about code it had actually read or tool output it had in its context. Instead, it was recalling from memory how the code works"
8. **The academic grounding (Cuadron et al.) finds higher overthinking scores correlate with decreased performance, and simple mitigation improves performance by almost 30% while cutting computational costs by 43%.**
   - Source: The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks, https://arxiv.org/abs/2502.08235
   - Tier: benchmark | Confidence: high | Accessed: 2026-11-22 | Via: web_extract
   - Quote: "simple efforts to mitigate overthinking in agentic environments, such as selecting the solution with the lower overthinking score, can improve model performance by almost 30% while reducing computational costs by 43%."
9. **The same bug report shows the default is measurably fragile: empty-answer failures hit 18 of 93 calls (19.4%) at xhigh versus 0 of 47 at low and 0 of 48 at medium.**
   - Source: Qwen3.8-27B reasoning_effort="xhigh" (the default) returns an empty answer, https://github.com/QwenLM/Qwen3.8/issues/216
   - Tier: community | Confidence: high | Accessed: 2026-11-22 | Via: web_extract
   - Quote: "`xhigh` (default) | 93 | 18 (19.4%)"
10. **A 4-bit quant of the dense 27B model runs in 16-19GB total memory, fitting a 24GB RTX 4090/5080 or a 24GB-RAM Mac.**
   - Source: Qwen3.8 - How to Run Locally, https://unsloth.ai/docs/models/qwen3.8
   - Tier: docs | Confidence: high | Accessed: 2026-11-22 | Via: web_extract
   - Quote: "Qwen3.8-27B 4-bit quants work on 16-19GB VRAM like RTX 5080, 4090 or a Mac with 24GB RAM."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | xhigh SVG prompt cost (Willison) | 21 minutes; 22,276 reasoning tokens for 3,223 tokens of output | https://simonw.substack.com/p/qwen-38-27b-is-excellent-but-it-defaults | "It took **21 minutes** to generate, using 22,276 reasoning tokens to produce 3,223 tokens of output." |
| 2 | same prompt with reasoning off | 3,715 tokens; 137s | https://simonw.substack.com/p/qwen-38-27b-is-excellent-but-it-defaults | "This one produced **3,715 tokens** and took 137s" |
| 3 | median tokens and wall clock by effort (M5 Max) | low 4,984 tokens / 84 s; medium 4,792 tokens / 77 s; xhigh 36,188 tokens / 869 s | https://llm-bench.io/guides/qwen3-8-27b-reasoning-effort | "eight times the tokens and eleven times the wall clock" |
| 4 | dwim vs OpenCode (same model) | 64% vs 52% resolved; 6,270 vs 22,610 median thinking tokens; 55 s vs 169 s | https://penberg.org/blog/qwen38-overthink.html | "dwim resolved 64% of the issues against OpenCode's 52%" |
| 5 | dwim thinking cap | 2,048 tokens | https://penberg.org/blog/qwen38-overthink.html | "2048 tokens as the hard limit" |
| 6 | empty-answer rate at xhigh | 18 (19.4%) of 93 calls; low 0 of 47; medium 0 of 48 | https://github.com/QwenLM/Qwen3.8/issues/216 | "18 (19.4%)" |
| 7 | 4-bit memory footprint | 16-19GB total memory | https://unsloth.ai/docs/models/qwen3.8 | "Qwen3.8-27B 4-bit quants work on 16-19GB VRAM" |
| 8 | native context | 262,144 tokens | https://huggingface.co/Qwen/Qwen3.8-27B | "Context Length: 262,144 natively" |

## Analogy candidates
- **Kitchen blender with a glued dial**: every blend order arrives at maximum speed no matter what you meant to set -- the blades are fine, the dial is stuck on liquefy; the thinking budget is a timer that cuts power mid-blend even when the dial is ignored. Breaks when: hard problems genuinely need liquefy (xhigh's higher 89.2 ceiling), and a timer set too early makes chunky salsa.
- **Mechanic reciting the workshop manual from memory while the car sits there with the hood open**: the model recalls how code works instead of reading the code in its context; one glance under the hood settles it. Breaks when: memory is stale or wrong, or the read is not actually in context.

## Misconceptions
- Myth: You have to turn reasoning off entirely to stop the overthinking. Reality: "You don't have to turn reasoning off completely to fix that. Instead, the harness can keep the thinking short and push the model to act." (claim 5)
- Myth: More thinking tokens buy better coding results. Reality: "so far I did not see better results from Qwen3.8-27B with more thinking; quite the opposite." (claim 6)
- Myth: Setting reasoning_effort=low always fixes it. Reality: Qwen's own card warns lower effort can raise total latency and tokens in multi-turn agentic tasks via retries, and misconfigured harnesses silently fall back to xhigh. (claims 1, 2)
- Myth: The model is just slow by nature. Reality: the weights score a median ~78 at low/medium in ~80 s; the 14-minute answers come from a shipped xhigh default in the chat template, not the model's only gear.
- Myth: A bigger context window stops the overthinking. Reality: "Nothing changed, except that the loop ran longer before it died."

## Glossary
- **reasoning_effort**: Qwen3.8's official knob for reasoning depth and cost, with levels xhigh (default), medium, and low.
- **thinking budget**: A hard cap on how many tokens the model may spend reasoning, which stops deliberation without truncating the answer.
- **enable_thinking**: The per-request switch (inside chat_template_kwargs) that turns the thinking preamble off entirely for direct answers.
- **chat_template_kwargs**: The nested extra_body dict where Qwen3.8's per-request template flags must be passed, distinct from top-level completion parameters.
- **xhigh**: The highest of Qwen3.8's three reasoning-effort levels and the shipped default, "for complex tasks demanding thorough analysis".
- **overthinking**: A failure case where a reasoning model stalls because it thinks too much instead of acting on the environment.
- **TTFT**: Time to first token; community reports put Qwen3.8-27B at 40+ seconds under default xhigh effort in IDE harnesses.
- **SWE-bench Verified Mini**: The 50-issue Django and Sphinx subset of SWE-bench Verified used in the penberg.org dwim-vs-OpenCode evaluation.
- **dwim**: Pekka Enberg's local coding agent that bundles a model and a harness; source of the penberg.org mitigations and eval.
- **dense model**: A model where every parameter is used on every token (no expert routing), so active parameters equals total parameters.

## Unverified
- The penberg.org page itself shows only "November 2026" as its date; the Nov 21, 2026 publication timestamp comes from a third-party listing in search results, not from a fetched page.
- Whether specific harnesses like Claude Code send effort flags for local models is community speculation in the HF thread, not documented in a fetched primary source.
- Kaitchup's full off-vs-low-vs-medium-vs-xhigh accuracy benchmark is paywalled; only the setup was confirmed, not the per-benchmark numbers.
- Community reports of a llama.cpp "--reasoning-budget N" flag were not verified for syntax or effect.
- VentureBeat's report of Qwen3.8-27B scoring 51 on Artificial Analysis' Agentic Index is a search snippet only; page not fetched.
- Whether non-thinking mode retains the 90.3 LiveCodeBench v6 score: model-card benchmarks were run in thinking mode; no fetched page isolates non-thinking coding scores.

## Suggested outline
1. Open on the symptom: your local coder vanished into its own head -- 21 minutes, 22,276 thinking tokens, 3,223 tokens of code out.
2. Acquit the engine: dense 27B, SWE-bench Pro 61.7, fits 24GB at 4-bit (16-19GB) -- this is not a weak model.
3. Indict the default: xhigh thinking is the template fallback; effort is a three-stop dial; the flag is one line.
4. The honest catch: effort is a suggestion, not a linkage -- the hard fix is a thinking budget, and Qwen itself warns retries can eat the savings.
5. The payoff: 64% vs 52% resolved, a quarter of the thinking, a third of the time -- same model, better harness.

## Viewer situation
You've got Qwen3.8-27B running locally for coding -- LM Studio, Ollama, or your IDE's local hook -- and it thinks for minutes before touching your code.

## Has process
true
- Notice the stall: thinking trace looping on "I think", "I recall", "wait" while your code sits unread.
- Set the effort flag: pass reasoning_effort low or medium on every request instead of the default xhigh.
- Cap the thinking: set a hard thinking budget (dwim: 2,048 tokens; oMLX tested 12,000) so deliberation has a mechanical end.
- Tell it to act: when the cap hits, inject the closing sentence that says the answer is in the output already in context -- read, decide, edit.

## Objection
Any modern reasoning model overthinks sometimes; a hard cap just truncates reasoning and guts accuracy on hard problems -- and Qwen's own card says lower effort can cost more total time in agentic runs.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/Qwen/Qwen3.8-27B | Qwen/Qwen3.8-27B (model card) | primary | web_extract | 2026-11-22 |
| 2 | https://penberg.org/blog/qwen38-overthink.html | Why Qwen3.8-27B Overthinks in Coding Tasks and How to Mitigate That | primary | web_extract | 2026-11-22 |
| 3 | https://llm-bench.io/guides/qwen3-8-27b-reasoning-effort | Qwen3.8-27B has the best coding ceiling you can run at home, and it ships on maximum effort | benchmark | web_extract | 2026-11-22 |
| 4 | https://simonw.substack.com/p/qwen-38-27b-is-excellent-but-it-defaults | Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things | community | web_extract | 2026-11-22 |
| 5 | https://github.com/QwenLM/Qwen3.8/issues/216 | reasoning_effort="xhigh" (the default) returns an empty answer | community | web_extract | 2026-11-22 |
| 6 | https://huggingface.co/Qwen/Qwen3.8-27B/discussions/97 | A crazy thinking model (HF discussion 97) | community | web_extract | 2026-11-22 |
| 7 | https://huggingface.co/Qwen/Qwen3.8-27B/discussions/136 | Horrible model .... Overthink eats all context tokens (HF discussion 136) | community | web_extract | 2026-11-22 |
| 8 | https://unsloth.ai/docs/models/qwen3.8 | Qwen3.8 - How to Run Locally | docs | web_extract | 2026-11-22 |
| 9 | https://arxiv.org/abs/2502.08235 | The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks | benchmark | web_extract | 2026-11-22 |
| 10 | https://medium.com/@bikramjitsarkar2/qwen-3-8-27b-keeps-thinking-and-never-writes-code-heres-the-one-line-fix-51ac2d63dc6d | Qwen 3.8 27B Keeps Thinking and Never Writes Code | community | web_extract | 2026-11-22 |

## Notes
Conflicts: none material. Qwen's card (xhigh default, sampler profiles, retry caveat) and llm-bench.io agree on mechanism; llm-bench.io's independent M5 Max measurement is the only effort-level token/latency benchmark in hand. Thin spots: the only systematic effort-vs-accuracy comparison outside llm-bench.io is paywalled (Kaitchup), and non-thinking-mode coding scores are not isolated by any fetched source, so the brief does not claim them. The most arresting number is 21 minutes / 22,276 reasoning tokens for 3,223 tokens of output (hook-grade).
