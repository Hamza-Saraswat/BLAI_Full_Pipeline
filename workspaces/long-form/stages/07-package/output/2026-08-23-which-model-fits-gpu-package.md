---
slug: 2026-08-23-which-model-fits-gpu
workspace: long-form
stage: 07-package
---

# Package: LLM GPU Requirements: Which Qwen Build Fits Your Card

## Titles

| # | Title | Type | Chars | Note |
|---|-------|------|-------|------|
| 1 | **LLM GPU Requirements: Which Qwen Build Fits Your Card** | searchable | 53 | **Chosen.** Primary keyword `llm gpu requirements` at char 0; names the product (Qwen) at char 28. |
| 2 | Why Your GPU Doesn't Care About Parameter Counts | intriguing | 48 | Opens the gap but buries the keyword and names no product. |
| 3 | Bigger Model, Fewer Bits: The Rule That Reverses | intriguing | 48 | The episode's actual reversal; too oblique for a channel this small to rank on. |

**Why the searchable one.** Stage 02 measured 37 autocomplete expansions on `llm gpu requirements`, the deepest of any candidate that could carry ten minutes, and recorded that the queries are overwhelmingly "can I run X on Y". Search-heavy topics take the searchable title. It also complements thumbnail 1 rather than repeating it: the thumbnail carries the contradiction (27 billion parameters, 6.19 GB), the title carries the decision.

**Accuracy check.** Chapters 1-3 are Qwen builds off Unsloth's table, so "which Qwen build" is literal. Chapter 4 widens to Ornith 1.5 9B and the answer sometimes turns out to be "not a Qwen build at all" — the episode over-delivers on the title, which is the safe direction.

## Description

```
LLM GPU requirements, worked out properly: what decides whether a model loads is the file size plus its cache, not the parameter count.

One Qwen model ships builds ranging from under 7 GB to over 29 GB, and the model page shows you none of it. This episode reads Unsloth's published file table, adds the KV cache using NVIDIA's own formula, and walks three contenders down to one decision rule — then shows the two places that rule breaks.

Nothing here was measured on our bench, and the episode says so in its first twenty seconds. Every figure names its publisher: Unsloth's file sizes, llama.cpp's bits-per-weight and perplexity deltas, NVIDIA's cache arithmetic. You can go and check each one.

Chapters
00:00 Which Build Actually Fits
01:46 File Plus Cache
04:30 More Parameters, Fewer Bits
06:46 Fewer Parameters, More Bits
09:29 The Rule And Its Exceptions

Sources
Unsloth's Qwen3.8-27B file table: https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
Ornith 1.5 9B file table: https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF
llama.cpp quantization figures: https://github.com/ggml-org/llama.cpp/discussions/2094
NVIDIA on KV cache size: https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/
Ollama context length docs: https://docs.ollama.com/context-length

More local AI on the channel: https://www.youtube.com/@BuildLocalAI

Written, sourced and voiced by me; animation and research assisted by an AI pipeline. Every number on screen carries the name of whoever published it.

#Qwen #LocalAI #GGUF
```

1539 characters, 1541 bytes. First 135 characters carry the keyword and the promise above the fold.

## Chapters

| Time | Label | First scene |
|------|-------|-------------|
| 00:00 | Which Build Actually Fits | s01 |
| 01:46 | File Plus Cache | s07 |
| 04:30 | More Parameters, Fewer Bits | s17 |
| 06:46 | Fewer Parameters, More Bits | s25 |
| 09:29 | The Rule And Its Exceptions | s35 |

Times are summed from the spec's `est_duration_s` at the pipeline's assumed 2.9 words per second. **Stage 10 overwrites them with measured times** and `publish.py --chapters` swaps the block into the description at upload. Labels are identical to the script's five `## Chapter N:` headings, checked mechanically.

## Rubric

| Check | Points | Awarded | Evidence |
|-------|--------|---------|----------|
| Title keyword and length | 20 | 20 | keyword at char 0; 53 chars (band 35-65); no emoji; `LLM`/`GPU` read as technical acronyms, not emphasis |
| Title type and complement | 10 | 10 | tagged searchable, matches a search-heavy topic; shares no words with thumbnail 1 |
| Description | 20 | 20 | keyword + promise in the first 135 chars; unique text; 1,539 chars; valid 5-line chapter block; 1,541 bytes |
| Hashtags | 5 | 5 | 3, product first, no spaces |
| Tags list | 5 | 5 | 13 tags, 231 chars, exact keyword present, 3 variants |
| Thumbnail | 15 | 15 | 3 concepts, each <= 4 words with 1 focus area. **Deferred:** `>= 1280x720` and `<= 2 MB` cannot be checked here — no PNG exists until stage 10 |
| First 30 s carry the promise | 10 | 10 | beat 1.1 states the contradiction and the question in the first ~16 s of narration |
| Compliance | 15 | 15 | flags below |
| **Total** | **100** | **100** | |

**The score is not worth much, and that is a finding, not a boast.** This rubric is scored by the same agent that wrote the package, and none of its eight rows tests either defect this stage actually found: that `TitleCard` renders no on-screen text, so the episode's own hook numbers are invisible for the first 34 seconds; or that the thumbnail row asks stage 07 to certify pixel dimensions of files stage 10 has not created yet. A gate that awards full marks to a package with two known visual defects is a formality. See findings 34 and 40 in `_design/test-findings-2026-08-23.md`.

## Compliance

| Flag | Value | Justification |
|------|-------|---------------|
| `contains_synthetic_media` | `false` | No realistic synthetic footage of real people, places or events. Typographic scenes, diagrams and tables are clearly unrealistic; a voice is explicitly exempt |
| `made_for_kids` | `false` | Always false per compliance.md |
| `notify_subscribers` | `true` | Long-form default |
| `privacy_status` | `private` | **Test artifact.** See below |
| `original_insight` | written | Everyone repeats "take a bigger model at lower precision"; this episode does the memory arithmetic from publishers' own file tables and llama.cpp's bits-per-weight figures, and shows the rung where that rule reverses — while stating up front that no number in it was measured on our bench. |
| YMYL | n/a | No health, legal, finance or political claim. Every figure is attributed on screen to its publisher |

**This package must not be published as-is.** Compliance rule 3 requires the creator's own cloned voice; this run is voiced by Kokoro because the ElevenLabs clone does not exist yet. `privacy_status` is `private` and `publish_slot_hint` is empty so that no scheduler can pick it up by accident.

**Related episodes:** none. `workspaces/long-form/published/` is empty, so the duplicate-title check and the two related-episode links the format asks for both had nothing to run against. The description links the channel instead.

## Manifest

```json
{
  "slug": "2026-08-23-which-model-fits-gpu",
  "format": "long",
  "title": "LLM GPU Requirements: Which Qwen Build Fits Your Card",
  "title_variants": [
    {
      "text": "LLM GPU Requirements: Which Qwen Build Fits Your Card",
      "type": "searchable"
    },
    {
      "text": "Why Your GPU Doesn't Care About Parameter Counts",
      "type": "intriguing"
    },
    {
      "text": "Bigger Model, Fewer Bits: The Rule That Reverses",
      "type": "intriguing"
    }
  ],
  "description": "LLM GPU requirements, worked out properly: what decides whether a model loads is the file size plus its cache, not the parameter count.\n\nOne Qwen model ships builds ranging from under 7 GB to over 29 GB, and the model page shows you none of it. This episode reads Unsloth's published file table, adds the KV cache using NVIDIA's own formula, and walks three contenders down to one decision rule \u2014 then shows the two places that rule breaks.\n\nNothing here was measured on our bench, and the episode says so in its first twenty seconds. Every figure names its publisher: Unsloth's file sizes, llama.cpp's bits-per-weight and perplexity deltas, NVIDIA's cache arithmetic. You can go and check each one.\n\nChapters\n00:00 Which Build Actually Fits\n01:46 File Plus Cache\n04:30 More Parameters, Fewer Bits\n06:46 Fewer Parameters, More Bits\n09:29 The Rule And Its Exceptions\n\nSources\nUnsloth's Qwen3.8-27B file table: https://huggingface.co/unsloth/Qwen3.8-27B-GGUF\nOrnith 1.5 9B file table: https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF\nllama.cpp quantization figures: https://github.com/ggml-org/llama.cpp/discussions/2094\nNVIDIA on KV cache size: https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/\nOllama context length docs: https://docs.ollama.com/context-length\n\nMore local AI on the channel: https://www.youtube.com/@BuildLocalAI\n\nWritten, sourced and voiced by me; animation and research assisted by an AI pipeline. Every number on screen carries the name of whoever published it.\n\n#Qwen #LocalAI #GGUF",
  "hashtags": [
    "#Qwen",
    "#LocalAI",
    "#GGUF"
  ],
  "tags": [
    "llm gpu requirements",
    "llm vram requirements",
    "gpu requirements for llm",
    "can i run this model",
    "gguf quantization",
    "kv cache vram",
    "qwen 27b",
    "unsloth gguf",
    "ollama vram",
    "local llm",
    "q4_k_m vs q8_0",
    "how much vram do i need",
    "run llm on 12gb"
  ],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "private",
  "notify_subscribers": true,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "thumbnail": "thumbnails/1.png",
  "chapters": [
    {
      "time": "00:00",
      "label": "Which Build Actually Fits"
    },
    {
      "time": "01:46",
      "label": "File Plus Cache"
    },
    {
      "time": "04:30",
      "label": "More Parameters, Fewer Bits"
    },
    {
      "time": "06:46",
      "label": "Fewer Parameters, More Bits"
    },
    {
      "time": "09:29",
      "label": "The Rule And Its Exceptions"
    }
  ],
  "publish_slot_hint": "",
  "related_long_form_url": "",
  "original_insight": "Everyone repeats \"take a bigger model at lower precision\"; this episode does the memory arithmetic from publishers' own file tables and llama.cpp's bits-per-weight figures, and shows the rung where that rule reverses \u2014 while stating up front that no number in it was measured on our bench.",
  "seo_score": 100,
  "reviewer_notes": "TEST ARTIFACT. privacy_status is private and publish_slot_hint is empty on purpose: this run is voiced by Kokoro, not the creator's ElevenLabs clone, so compliance rule 3 (the creator's own voice) is not satisfied and it must not be published as-is. Chapter times are estimates; stage 10 overwrites them with measured ones. Thumbnail pixel checks (>=1280x720, <=2 MB) cannot run until stage 10 renders the stills."
}
```
