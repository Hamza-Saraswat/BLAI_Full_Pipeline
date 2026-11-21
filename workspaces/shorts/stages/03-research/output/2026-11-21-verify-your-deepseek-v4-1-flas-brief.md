---
slug: 2026-11-21-verify-your-deepseek-v4-1-flas
stage: 03-research
topic: "Verify your DeepSeek v4.1-flash weights before you run them"
depth: standard
generated_at: 2026-11-21T12:33:29Z
sources: 8
hub: "[[videos/2026-11-21-verify-your-deepseek-v4-1-flas]]"
---

# Research brief: Verify your DeepSeek v4.1-flash weights before you run them

## Summary
- Core idea: a swapped-weights incident is invisible to capability benchmarks, so the only evidence about what you actually downloaded is a hash of the files themselves.
- Most arresting number: refusals fell from 98 of 100 prompts to 1 on JailbreakBench while GPQA Diamond and τ-bench scores were unaffected.
- Strongest concrete case: Prime Intellect's deepseek/deepseek-v4.1-flash endpoint served publicly available abliterated weights between November 8, 2026, at 01:24 UTC and November 10, 2026, at 06:35 UTC (advisory PI-SA-2026-001).
- Could not verify: any actual tampered local mirror (the incident was a hosted API deployment), any tokens-per-second on our own hardware, and the OpenRouter notification angle (its source sat behind a registration wall).
- Conflicts: none material; the ideas note listed the advisory at primeintellect.one, the canonical page fetched this run is primeintellect.ai with the same text.

## Thesis
Prime Intellect served a silently modified DeepSeek v4.1-flash for over two days and no capability benchmark noticed, and the same blind spot sits on your disk: only a hash of the shards tells you what you really downloaded, so verify before you load.

## Explanation path
Establish what actually happened before any tool appears: a hosted endpoint kept its name, chat template and tokenizer while different weights answered requests, and the substitution left capability benchmarks untouched while refusal behavior collapsed. That fact does the load-bearing work: scores cannot authenticate a model, so "it still benchmarks fine" is never evidence you are running the real thing. Then move the problem onto the viewer's side of the glass: someone running weights locally is in a stronger position than an API customer, because the artifact is a file on their own disk and can be checked offline, but only if they check it. Introduce the hash as the fingerprint of the exact bits, distinct from the model's name on the folder. Then the discipline itself: pin the exact revision before downloading, fetch the checksum manifest alongside the shards, verify before the first load, and know what a pass proves and what it cannot prove. Close on the limit so the video stays honest: a matching hash proves transport integrity against the repo you pulled from; it does not certify the repo itself, and no benchmark substitutes for that decision.

## Claims
1. **Between November 8, 2026, at 01:24 UTC and November 10, 2026, at 06:35 UTC, an unauthorized party replaced the deployment behind Prime Intellect's deepseek/deepseek-v4.1-flash endpoint with an abliterated copy.**
   - Source: Notice regarding deepseek/deepseek-v4.1-flash, 8 to 10 November 2026 | Prime Intellect, https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution
   - Tier: primary | Confidence: high | Accessed: 2026-11-21 | Via: WebFetch
   - Quote: "Between November 8, 2026, at 01:24 UTC and November 10, 2026, at 06:35 UTC, an unauthorised party replaced a deployment behind Prime Intellect's deepseek/deepseek-v4.1-flash endpoint with an abliterated copy"
2. **The substituted weights were publicly available abliterated weights of the same model, and only the weights changed: the chat template, tokenizer and serving configuration were not modified.**
   - Source: Notice regarding deepseek/deepseek-v4.1-flash, 8 to 10 November 2026 | Prime Intellect, https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution
   - Tier: primary | Confidence: high | Accessed: 2026-11-21 | Via: WebFetch
   - Quote: "The model was replaced with publicly available abliterated weights of deepseek/deepseek-v4.1-flash. The chat template, tokenizer and serving configuration were not modified."
3. **Capability was unchanged while refusals collapsed: refusals fell from 98 of 100 prompts to 1 on JailbreakBench, from 304 of 313 to 2 on StrongREJECT, and from 198 of 240 to none on HarmBench, with GPQA Diamond and τ-bench unaffected.**
   - Source: Notice regarding deepseek/deepseek-v4.1-flash, 8 to 10 November 2026 | Prime Intellect, https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution
   - Tier: primary | Confidence: high | Accessed: 2026-11-21 | Via: WebFetch
   - Quote: "We tested the modified weights and found that capability benchmarks (GPQA Diamond and τ-bench) were unaffected. Refusals fell from 98 of 100 prompts to 1 on JailbreakBench, from 304 of 313 to 2 on StrongREJECT, and from 198 of 240 to none on HarmBench."
4. **DeepSeek-V4.1-Flash is a multimodal Mixture-of-Experts model with 552B backbone parameters and support for contexts of up to one million tokens, which is why so many local users carry its files.**
   - Source: deepseek-ai/DeepSeek-V4.1-Flash · Hugging Face, https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
   - Tier: primary | Confidence: high | Accessed: 2026-11-21 | Via: WebFetch
   - Quote: "We introduce DeepSeek-V4.1-Flash, a multimodal Mixture-of-Experts (MoE) model with 552B backbone parameters and support for contexts of up to one million tokens."
5. **Unsloth's GGUF release lists its smallest 1-bit quant at 233 GB, says it runs on a 128GB+ RAM device, and shows 1,618,638 downloads last month.**
   - Source: unsloth/DeepSeek-V4.1-Flash-1017-GGUF · Hugging Face, https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-11-21 | Via: WebFetch
   - Quote: "Run on a 128GB+ RAM device for the smallest 1-bit, 3-bit on 256GB or full precision on 320GB."
6. **huggingface_hub confirms file size on download but does not compute sha256 checksums by default because of the time cost, and ships `hf cache verify` as the separate step that recomputes all checksums and verifies they match the Hub files.**
   - Source: Checksum validation with hf_hub_download on model files. · Issue #2364 · huggingface/huggingface_hub, https://github.com/huggingface/huggingface_hub/issues/2364
   - Tier: docs | Confidence: high | Accessed: 2026-11-21 | Via: WebFetch
   - Quote: "I don't want to do it by default, because of the extra overhead it would have for users (computing a sha256 file on GBs of data can takes minutes)" and "Closing this issue as we introduced a `hf cache verify` to recompute all checksums and verify they match the Hub files."
7. **The `hf download` CLI can pin an exact repository version by revision, and a commit hash used as the revision must be the full-length hash, not a 7-character one.**
   - Source: Download files from the Hub · Hugging Face, https://huggingface.co/docs/huggingface_hub/en/guides/download
   - Tier: docs | Confidence: high | Accessed: 2026-11-21 | Via: WebFetch
   - Quote: "Note: When using the commit hash, it must be the full-length hash instead of a 7-character commit hash."
8. **llama.cpp ships a dedicated hashing tool, llama-gguf-hash, which hashes a GGUF file with sha256 and verifies it against a manifest.**
   - Source: llama-gguf-hash(1) · llama.cpp-examples · Debian testing manpages, https://manpages.debian.org/testing/llama.cpp-examples/llama-gguf-hash.1.en.html
   - Tier: docs | Confidence: high | Accessed: 2026-11-21 | Via: WebFetch
   - Quote: "--sha256 use sha256 hash" ; "-c, --check <manifest> verify against a manifest"
9. **An independent mixed-Q2 repack of DeepSeek-V4.1-Flash (169.92 GB across five shards) publishes a SHA256SUMS manifest and reports all five shards matched when re-hashed after download from the Hub, at ~150-200 s per shard on a CPU pod.**
   - Source: apetersson/DeepSeek-V4.1-Flash-MixedQ2-GGUF · Hugging Face, https://huggingface.co/apetersson/DeepSeek-V4.1-Flash-MixedQ2-GGUF
   - Tier: benchmark | Confidence: medium | Accessed: 2026-11-21 | Via: WebFetch
   - Quote: "all five shards match SHA256SUMS (39.17/39.99/39.00/39.97/10.80 GB, ~150-200 s each)" ; "total 169,917,778,504 B = 169.92 GB (1,038 tensors, arch deepseek4)"
10. **The incident reached developer discussion as model spoofing, with commenters calling it a new class of attack rather than a routine outage.**
    - Source: Attacker swapped Prime Intellect's DeepSeek v4.1 Flash endpoint for 53 hours | Hacker News, https://news.ycombinator.com/item?id=50567236
    - Tier: community | Confidence: medium | Accessed: 2026-11-21 | Via: WebFetch
    - Quote: "model spoofing is here apparently..quite a new attack"

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | refusals on JailbreakBench, before vs after substitution | 98 of 100 prompts to 1 | https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution | "Refusals fell from 98 of 100 prompts to 1 on JailbreakBench" |
| 2 | refusals on HarmBench, before vs after substitution | 198 of 240 to none | https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution | "from 198 of 240 to none on HarmBench" |
| 3 | substitution window (UTC) | between November 8, 2026, at 01:24 UTC and November 10, 2026, at 06:35 UTC | https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution | "Between November 8, 2026, at 01:24 UTC and November 10, 2026, at 06:35 UTC" |
| 4 | backbone parameters, DeepSeek-V4.1-Flash | 552B backbone parameters | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | "a multimodal Mixture-of-Experts (MoE) model with 552B backbone parameters" |
| 5 | smallest unsloth 1-bit GGUF (UD-IQ1_S) | 233 GB | https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF | "Run on a 128GB+ RAM device for the smallest 1-bit" |
| 6 | unsloth GGUF downloads last month | 1,618,638 | https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF | "Downloads last month 1,618,638" |
| 7 | community mixed-Q2 pack, five shards total | 169.92 GB | https://huggingface.co/apetersson/DeepSeek-V4.1-Flash-MixedQ2-GGUF | "169,917,778,504 B = 169.92 GB (1,038 tensors, arch deepseek4)" |
| 8 | SHA256 re-hash time per ~40 GB shard on a CPU pod | ~150-200 s | https://huggingface.co/apetersson/DeepSeek-V4.1-Flash-MixedQ2-GGUF | "all five shards match SHA256SUMS (39.17/39.99/39.00/39.97/10.80 GB, ~150-200 s each)" |

## Analogy candidates
- **Vehicle**: Tamper-evident seal on a medicine bottle. **Mapping**: the seal never judges the pills, it proves nobody touched the bottle since it left the factory; a SHA-256 match proves the shards are the exact bits the repo published, nothing more. **Breaks when**: a seal only anchors to the factory that sealed it, so if the repo itself publishes bad weights the hash matches anyway; verification proves transport integrity, not trustworthiness.
- **Vehicle**: A restaurant that keeps the sign but swaps the kitchen. **Mapping**: Prime Intellect's endpoint kept its name, chat template and tokenizer while different weights answered, so every client vouched for the sign instead of the kitchen. **Breaks when**: a diner can walk in and inspect the kitchen, but an API client cannot inspect weights mid-conversation, which is exactly why the check has to happen on the files before loading.

## Misconceptions
- Myth: If the model still aces its benchmarks, it is the genuine weights. Reality: the substituted copy left GPQA Diamond and τ-bench unaffected while refusals fell from 98 of 100 prompts to 1 on JailbreakBench (claim 3).
- Myth: The Prime Intellect hack means my local GGUF could get remotely hacked the same way. Reality: the substitution happened behind a hosted API endpoint, not in viewers' files, so the local lesson is provenance discipline before loading, not incident response (claims 1, 6, 9).
- Myth: My download tool already verifies integrity for me. Reality: hf_hub_download confirms byte counts on retrieval and sha256 checksums are not computed by default; the shipped check is a separate `hf cache verify` run (claim 6).

## Glossary
- **abliterated**: a model copy edited to reduce or remove its refusal behavior.
- **SHA-256**: a fingerprint algorithm that turns any file into a fixed 64-character ID; identical bits always produce an identical ID.
- **checksum manifest**: a list of expected SHA-256 fingerprints for a set of files, such as a repo's SHA256SUMS.
- **GGUF**: the single-file weight format that llama.cpp-family tools load.
- **quantization**: shrinking model weights to fewer bits so the model fits in less memory, at some cost in quality.
- **commit hash (revision)**: the full-length identifier of one exact uploaded version of a repository, used to pin a download.
- **inference endpoint**: the server address an app sends prompts to; the model behind it can change while the address stays the same.

## Unverified
- No page fetched this run documents an actually tampered local mirror of DeepSeek-V4.1-Flash; the incident was a hosted API substitution, so the video must not claim local files were swapped.
- Tokens per second, load time and memory use for this model on the DGX Spark have not been measured by us; PROVES value stays reserved until a first-party number exists.
- How Ollama or LM Studio handle manifest verification was not researched this session; hedge or drop any mention of them.
- The OpenRouter private-notification angle (Theo Browne) was reported only behind a registration wall at runtimewire.com and is not cited; treat its details as unread.
- Aggregator headlines round the substitution window to 53 hours; the advisory states only the UTC timestamps, so the script should round from the timestamps, not the headline.

## Suggested outline
1. Cold open on the swap: same endpoint name, different weights, refusals fell from 98 of 100 prompts to 1 on JailbreakBench while capability scores did not move.
2. Move it onto the viewer's disk: GGUF shards are also files under a trusted name; pin the revision, download the manifest, run the hash check before the first load (hf cache verify, sha256sum -c, llama-gguf-hash).
3. Honest close: a matching hash proves you received the repo's bits, not that the repo deserved trust; make verification the habit before every load.

## Viewer situation
You run DeepSeek v4.1-flash on your own hardware from GGUF shards you pulled with hf download or a launcher app, and you have never hashed one of them.

## Has process
`true`
- Pin the exact revision (full-length commit hash) named by the model card or the source you trust.
- Download the shards together with the repo's SHA256SUMS manifest.
- Run `hf cache verify`, or `sha256sum -c SHA256SUMS`, before the first load.
- Hash GGUFs you converted or re-sharded yourself with `llama-gguf-hash --sha256`, keeping the manifest for later `-c` checks.
- Re-verify after any re-download, resume or disk move, and stop on any mismatch.

## Objection
A SHA-256 match only proves you received the bits Hugging Face hosts, so if the repo or its owner is the threat the check passes anyway and verification is theater.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution | Notice regarding deepseek/deepseek-v4.1-flash, 8 to 10 November 2026 | primary | WebFetch | 2026-11-21 |
| 2 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | deepseek-ai/DeepSeek-V4.1-Flash | primary | WebFetch | 2026-11-21 |
| 3 | https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF | unsloth/DeepSeek-V4.1-Flash-1017-GGUF | primary | WebFetch | 2026-11-21 |
| 4 | https://github.com/huggingface/huggingface_hub/issues/2364 | Checksum validation with hf_hub_download on model files. #2364 | docs | WebFetch | 2026-11-21 |
| 5 | https://huggingface.co/docs/huggingface_hub/en/guides/download | Download files from the Hub | docs | WebFetch | 2026-11-21 |
| 6 | https://manpages.debian.org/testing/llama.cpp-examples/llama-gguf-hash.1.en.html | llama-gguf-hash(1), llama.cpp-examples, Debian testing | docs | WebFetch | 2026-11-21 |
| 7 | https://huggingface.co/apetersson/DeepSeek-V4.1-Flash-MixedQ2-GGUF | apetersson/DeepSeek-V4.1-Flash-MixedQ2-GGUF | benchmark | WebFetch | 2026-11-21 |
| 8 | https://news.ycombinator.com/item?id=50567236 | Attacker swapped Prime Intellect's DeepSeek v4.1 Flash endpoint for 53 hours | community | WebFetch | 2026-11-21 |

## Notes
- Tooling: FireCrawl credits were exhausted (reset 2026-11-22T21:51Z), so per rules/firecrawl-usage.md the run used the WebSearch + WebFetch fallback: 4 searches, 8 page fetches, all 8 cited above.
- runtimewire.com (the OpenRouter notification angle) returned a registration wall and is not cited; the primary advisory covers the incident directly.
- No material source conflicts. The ideas note carried the advisory at primeintellect.one; the canonical fetched page is primeintellect.ai with matching text, and the brief cites the fetched URL.
- Thin spot: every fetched verification example (SHA256SUMS, hf cache verify, llama-gguf-hash) is generic or third-party; deepseek-ai's own repo does not publish a per-shard manifest page we fetched, so the video should show the manifest habit on whatever repo the viewer pulls from rather than claim DeepSeek ships one.
