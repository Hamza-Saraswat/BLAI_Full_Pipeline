---
slug: 2026-09-16-replicating-a-paper-with-qwen
stage: 03-research
topic: "Replicating a paper with Qwen-2.5 at home"
depth: standard
generated_at: 2026-09-16T11:45:50Z
sources: 11
hub: "[[videos/2026-09-16-replicating-a-paper-with-qwen]]"
---

# Research brief: Replicating a paper with Qwen-2.5 at home

## Summary
A replication published on Hugging Face within hours of TypeSafe's Jev launch rebuilds the "System One" decision model from nothing but stock Qwen-2.5-1.5B weights and a different decoding loop, Apache 2.0, no new training (thesis). The most arresting number: on a 28-field triage form, 312 sequential forward passes collapse to 1, cutting 1,900 ms to 270 ms on an M4 Max MacBook. The strongest concrete case: the model card's own benchmark table shows 5.6x to 7.0x latency reductions with 100% schema validity on hardware a viewer already owns. Could not verify: any GPU number, the author's "2 hours" effort claim, and a live GitHub URL (the model card's clone link is a placeholder). Conflict: the launch tweet says 5x while the model card table says 5.6x to 7.0x, and the same card prints 7.1x for the same 28-field preset in its CLI sample output -- trust the card's benchmark table over both.

## Thesis
The trick behind the new Jev decision model is not exotic weights: a stock Qwen-2.5-1.5B on a MacBook reproduces the 312-passes-to-1 speedup in an afternoon, because the win comes from how you decode, not what you trained.

## Explanation path
Start from the moment a program needs a decision rather than a paragraph, because that reframing is what makes the whole trick sensible. Establish that a normal model answers a JSON schema by writing it out token by token, one forward pass per token, so a 28-field form costs hundreds of passes before the content is even correct. Introduce the published result being copied: Jev, a model that refuses to write and instead returns a probability for every allowed answer in a single parallel shot. Then reveal the replication's insight, which the author states plainly: the ability already sits inside any stock model. Read the document once into the KV cache, mask the vocabulary down to each field's legal choices, and read off probabilities for all fields at once; the JSON is assembled by code, never written by the model. Land the numbers on hardware the viewer owns or can afford, then close on the boundary: guaranteed shape is not guaranteed truth, and the jobs that belong on this path (routing, triage, guardrail checks) are the ones where a wrong-but-valid answer is cheap to catch.

## Claims
1. **TypeSafe AI released Jev on 2026-09-15 as the first "System One Model": it gives up text generation and returns type-safe structured values with calibrated probabilities, priced at $0.042 / MTok for input tokens with output tokens free.**
   - Source: Introducing System One Models & Jev, https://typesafe.ai/blog/introducing-system-one-models-and-jev
   - Tier: primary | Confidence: high | Accessed: 2026-09-16 | Via: web_extract
   - Quote: "Input tokens: $0.042 / MTok ($42 per billion tokens). Output tokens: FREE (too cheap to meter)."
2. **TypeSafe publishes Jev's end-to-end response time as 70ms-500ms, which it says can range from 40x-200x faster than frontier LLMs for System One shaped queries.**
   - Source: Introducing System One Models & Jev, https://typesafe.ai/blog/introducing-system-one-models-and-jev
   - Tier: primary | Confidence: high | Accessed: 2026-09-16 | Via: web_extract
   - Quote: "End-to-end response time is 70ms-500ms for TypeSafe. This can range from 40x-200x faster for the same levels of frontier intelligence for System One shaped queries."
3. **An independent hands-on test by Every's head of evals had Jev read 37 documents and answer 21 questions on each, returning 777 judgments in less than 0.7 seconds for an estimated quarter of a cent.**
   - Source: Mini-Vibe Check: TypeSafe's Jev Judged Everything I've Written in 0.7 Seconds, https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds
   - Tier: benchmark | Confidence: medium | Accessed: 2026-09-16 | Via: web_extract
   - Quote: "In less than 0.7 seconds, Jev \"read\" all 37 documents and answered all 21 questions for each, returning 777 judgments, for an estimated quarter of a cent."
4. **The replication is published on Hugging Face as harshatheg/Qwen-2.5-1B-RLCD under Apache 2.0, and its engine is configured for a stock checkpoint: mlx-community/Qwen2.5-1.5B-Instruct-4bit run through MLX.**
   - Source: harshatheg/Qwen-2.5-1B-RLCD model card, https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD
   - Tier: primary | Confidence: high | Accessed: 2026-09-16 | Via: web_extract
   - Quote: "The engine is currently configured for `mlx-community/Qwen2.5-1.5B-Instruct-4bit`. ... License: Apache 2.0"
5. **The base model is a 1.54B-parameter instruction-tuned LLM with a 32,768-token context, squarely laptop-class.**
   - Source: Qwen/Qwen2.5-1.5B-Instruct model card, https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct
   - Tier: primary | Confidence: high | Accessed: 2026-09-16 | Via: web_extract
   - Quote: "Number of Parameters: 1.54B ... Context Length: Full 32,768 tokens and generation 8192 tokens"
6. **On an Apple Silicon M4 Max the replication delivers 5.6x to 7.0x latency reductions versus standard autoregressive decoding, with 100% schema validity and calibrated field-level confidence scores.**
   - Source: harshatheg/Qwen-2.5-1B-RLCD model card, https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD
   - Tier: primary | Confidence: high | Accessed: 2026-09-16 | Via: web_extract
   - Quote: "On an Apple Silicon M4 Max, it delivers 5.6x to 7.0x latency reductions compared to standard autoregressive decoding with 100% schema validity and calibrated field-level confidence scores."
7. **On the 28-field Enterprise Support Triage preset, latency falls from 1,900 ms (130 tok/s autoregressive) to 270 ms, and the card's benchmark output shows sequential forward passes dropping from 312 to 1.**
   - Source: harshatheg/Qwen-2.5-1B-RLCD model card, https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD
   - Tier: primary | Confidence: high | Accessed: 2026-09-16 | Via: web_extract
   - Quote: "Enterprise Support Triage | 28 fields | 1,900 ms (130 tok/s) | 270 ms | 7.0x | 100% guaranteed ... Autoregressive Baseline : 1894.2 ms | 312 tokens (131.2 tok/s) | Passes: 312 ... Parallel Constrained : 268.4 ms | 0 tokens (O(1)) | Passes: 1"
8. **The mechanism is pure decoding: the context is prefilled once into an MLX KV cache, that cache is broadcast across all schema fields, each field evaluates only its candidate token IDs with the rest of the vocabulary masked, and the output JSON is assembled programmatically instead of generated.**
   - Source: harshatheg/Qwen-2.5-1B-RLCD model card, https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD
   - Tier: primary | Confidence: high | Accessed: 2026-09-16 | Via: web_extract
   - Quote: "For each field, only candidate token IDs belonging to valid schema choices are evaluated. The remaining vocabulary is masked. ... Output JSON is constructed directly from verified values, guaranteeing 100% valid syntax without JSON parsing errors."
9. **Each schema field is a boolean or an enum supporting up to 255 choices, so one field can pick among 255 tariff codes in a single pass.**
   - Source: harshatheg/Qwen-2.5-1B-RLCD model card, https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD
   - Tier: primary | Confidence: high | Accessed: 2026-09-16 | Via: web_extract
   - Quote: "choices (for enum types, supporting up to 255 choices)"
10. **TypeSafe itself discloses that its workflow evals use the average of GPT-6 Astra and Fable 5.1 as reference answers, and that its headline 193.6x faster and 444.6x cheaper claims are expected to be "on the higher end of real world gains."**
    - Source: Introducing System One Models & Jev, https://typesafe.ai/blog/introducing-system-one-models-and-jev
    - Tier: primary | Confidence: high | Accessed: 2026-09-16 | Via: web_extract
    - Quote: "This is where the claims of 193.6x faster, 444.6x cheaper on our home page comes from, and we expect that these are on the higher end of real world gains."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | Latency reduction vs autoregressive on Apple Silicon M4 Max | 5.6x to 7.0x | https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD | "it delivers 5.6x to 7.0x latency reductions compared to standard autoregressive decoding" |
| 2 | Enterprise Support Triage (28 fields), autoregressive baseline | 1,900 ms (130 tok/s) | https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD | "Enterprise Support Triage \| 28 fields \| 1,900 ms (130 tok/s) \| 270 ms \| 7.0x \| 100% guaranteed" |
| 3 | Enterprise Support Triage (28 fields), parallel constrained | 270 ms | https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD | "Enterprise Support Triage \| 28 fields \| 1,900 ms (130 tok/s) \| 270 ms \| 7.0x \| 100% guaranteed" |
| 4 | Sequential forward passes on the 28-field preset, autoregressive vs parallel | 312 vs 1 | https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD | "Passes: 312 ... Passes: 1" |
| 5 | Schema validity of parallel constrained output | 100% guaranteed | https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD | "100% guaranteed" |
| 6 | Choices supported per enum field | up to 255 choices | https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD | "choices (for enum types, supporting up to 255 choices)" |
| 7 | Jev input token price, output tokens free (vendor pricing) | $0.042 / MTok ($42 per billion tokens) | https://typesafe.ai/blog/introducing-system-one-models-and-jev | "Input tokens: $0.042 / MTok ($42 per billion tokens). Output tokens: FREE (too cheap to meter)." |
| 8 | Jev end-to-end response time (vendor-published) | 70ms-500ms | https://typesafe.ai/blog/introducing-system-one-models-and-jev | "End-to-end response time is 70ms-500ms for TypeSafe." |

## Analogy candidates
- **Numbered menu at a counter**: Autoregressive generation is spelling your order out letter by letter; parallel constrained decoding is the cashier holding up a menu you wrote and you pointing once, with a confidence attached to every item at the same instant. Breaks when: menu items are independent but JSON fields can depend on each other (a reason field that must match the decision above it), and a thread commenter flagged exactly that dependent-field case as where independent sampling may not hold.
- **Scantron answer sheet**: Writing an essay versus bubbling one option per question; the engine reads the whole exam once and bubbles every answer in the same instant, so a stray mark outside the bubbles is impossible. Breaks when: a scantron picks exactly one bubble with no graded doubt, while the engine returns a full probability distribution over every option.

## Misconceptions
- Myth: Jev's speed comes from exotic new weights a home machine could never serve. Reality: the open replication hits 5.6x to 7.0x on a MacBook using the stock mlx-community/Qwen2.5-1.5B-Instruct-4bit checkpoint, no training at all (claims 4 and 6).
- Myth: Structured output means prompting a model to please answer in JSON. Reality: the speedup exists because the model never writes the JSON; one prefill, per-field logit slicing with the vocabulary masked, and code assembles the output, which is why validity is 100% by construction (claim 8).
- Myth: 100% schema validity means the answers are right. Reality: validity is guaranteed because the JSON is assembled, not generated, but correctness is untouched -- a 1.5B base model can flip a boolean between runs, and even TypeSafe's own eval grades against other models' answers rather than ground truth (claims 8 and 10).

## Glossary
- **Qwen-2.5**: a family of open-weight models from Alibaba's Qwen team, downloadable from Hugging Face in sizes from 0.5B to 72B parameters.
- **open weights**: the downloadable numbers that make up a trained model, so you can run it on your own machine instead of renting it through an API.
- **parameters (1.5B)**: the learned numbers inside a model; "1.5B" means about 1.5 billion of them.
- **Jev**: TypeSafe's first commercial System One model, which returns typed decisions and probabilities instead of writing text (named after economist William Stanley Jevons).
- **System One model**: TypeSafe's name for models built for fast, structured judgments that software calls directly, rather than chat replies.
- **structured output**: an answer that arrives in a fixed shape, like JSON fields, instead of a paragraph.
- **autoregressive decoding**: how normal LLMs write: one token at a time, each depending on the last.
- **parallel constrained decoding**: the replication's trick; read the document once, then score every field's allowed choices at the same time instead of writing them out.
- **KV cache**: the model's memory of what it just read, kept so it does not have to re-read the document for every field.
- **logit**: the raw score a model assigns to each possible next token before those scores become probabilities.
- **forward pass**: one trip of the input through the model's layers that produces the scores.
- **token**: a chunk of text, roughly a word or a piece of one, that models read and write in.
- **tokens per second (tok/s)**: how fast a model generates text; the measure of normal decoding speed.
- **quantization (4-bit)**: storing each model weight in 4 bits instead of 16 so the model fits in roughly a quarter of the memory.
- **MLX**: Apple's machine-learning framework for running models efficiently on Apple Silicon (M-series chips).
- **schema**: the written contract of fields and allowed answers you define before asking the model anything.
- **calibrated probability**: a probability that matches reality, meaning when the model says 90% it is right about 90% of the time.

## Unverified
- The author's "building in stealth for 2 hours" effort claim and the tweet's "5x faster" headline are self-reported with no published method.
- The author replied "order of mag better than this on GPUs" when asked about GPUs, but published no GPU numbers.
- No live GitHub repository was found this session; the model card's clone URL reads github.com/your-org/parallel-constrained-decoding, which is a placeholder.
- Real throughput on our own hardware (DGX Spark, Macs) is unmeasured; every latency number in the brief is the author's M4 Max run.
- Whether Jev's calibration holds in production is untested; the one independent hands-on (Every) was a self-described vibe check, not a calibration audit.

## Suggested outline
1. Open on the arrest: a 28-field support ticket that takes a normal model 1,900 ms of token-by-token typing comes back in 270 ms on a MacBook, because the replicated trick makes 1 forward pass instead of 312.
2. Explain the mechanism with the menu: stop asking the model to write JSON, read the document once into the KV cache, and score every field's legal choices in parallel, which is why the output is always valid and always carries a probability.
3. Equip for tonight: pull the stock Qwen-2.5-1.5B-Instruct-4bit checkpoint in MLX, define fields as booleans or enums up to 255 choices, run the benchmark, and route low-confidence fields to a human or a bigger model -- then the honest catch that a valid answer is not a correct one.

## Viewer situation
You already run a small open model like Qwen-2.5 in Ollama or LM Studio for chat on your own machine, and you have watched it type out JSON one word at a time when an app just needed a yes/no and a category.

## Has process
`true`

- Install the prerequisites on an Apple Silicon Mac: macOS 14.0 or later and Python 3.10+.
- Clone the parallel-constrained-decoding repository and install its requirements.txt into a fresh virtual environment.
- Load the stock mlx-community/Qwen2.5-1.5B-Instruct-4bit checkpoint through MLX.
- Define your decision schema: each field a boolean or an enum of up to 255 choices, with a plain-English description.
- Call run_parallel_generation on your context document and read the parsed JSON with a probability for every field.
- Run python3 -m core.benchmark to reproduce the autoregressive-versus-parallel comparison on your own machine.
- Set a confidence threshold in your code and route any field below it to a human or a larger model.

## Objection
A 1.5B model picking from a menu you wrote is not frontier intelligence, it is a classifier with extra steps, and even TypeSafe's own eval grades against other models' answers instead of ground truth.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/harshatheg/Qwen-2.5-1B-RLCD | harshatheg/Qwen-2.5-1B-RLCD model card (Parallel Constrained Decoding for Apple Silicon) | primary | web_extract | 2026-09-16 |
| 2 | https://typesafe.ai/blog/introducing-system-one-models-and-jev | Introducing System One Models & Jev | primary | web_extract | 2026-09-16 |
| 3 | https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct | Qwen/Qwen2.5-1.5B-Instruct model card | primary | web_extract | 2026-09-16 |
| 4 | https://qwenlm.github.io/blog/qwen2.5/ | Qwen2.5: A Party of Foundation Models! (Qwen blog) | primary | web_extract | 2026-09-16 |
| 5 | https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds | Mini-Vibe Check: TypeSafe's Jev Judged Everything I've Written in 0.7 Seconds | benchmark | web_extract | 2026-09-16 |
| 6 | https://docs.typesafe.ai/primitives | Primitives (Questions) - TypeSafe AI docs | primary | web_extract | 2026-09-16 |
| 7 | https://github.com/ml-explore/mlx-lm | ml-explore/mlx-lm: Run LLMs with MLX | primary | web_extract | 2026-09-16 |
| 8 | https://kingy.ai/blog/typesafe-jev-review-the-ai-model-that-doesnt-generate-text/ | TypeSafe Jev Review: The AI Model That Doesn't Generate Text | community | web_extract | 2026-09-16 |
| 9 | https://news.ycombinator.com/item?id=49717558 | Introducing System One Models and Jev (Hacker News discussion) | community | web_extract | 2026-09-16 |
| 10 | https://nitter.perennialte.ch/harshagundal/status/2100044305536889015 | Harsha Gundala announcement thread (radar lead hn-4dfe90f8a8) | community | web_extract | 2026-09-16 |
| 11 | https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding | Parallel Constrained Decision Engine (HF Space, paused at access) | primary | web_extract | 2026-09-16 |

## Notes
- The replicated artifact is a product launch with published evals, not a peer-reviewed paper; the script should say "replicating the launch result," not "replicating a paper."
- Conflict, speedup: the announcement tweet says 5x, the model card table says 5.6x to 7.0x, and the same card's CLI sample prints 7.1x for the same 28-field preset. Trust the card's benchmark table; all three are the author's own numbers and the table is the labeled benchmark.
- The radar lead (hn-4dfe90f8a8) resolves to the nitter mirror of the author's announcement tweet, which links the Hugging Face model card; the card is the primary source used throughout.
- Jev's own documented cardinality ceiling is also 255 options (TypeSafe blog FAQ), matching the replication's per-enum limit.
- The HF Space linked from the model card was paused at access; only the model card's numbers were used.
- The Qwen blog confirms the series context: sizes 0.5B through 72B, Apache 2.0 for all except the 3B and 72B variants, pretrained on up to 18 trillion tokens.
- A thread commenter (community tier) asked whether independent per-key sampling holds when one JSON field only makes sense given another; the author answered that large enough models probably handle it. Treat dependent fields as an open limit, which the scantron and menu analogies both flag.
- The Kingy review (community tier, no live API access) independently reached the same accuracy caveat this brief grounds in TypeSafe's own blog; it is listed for the reviewer, not cited for numbers.
