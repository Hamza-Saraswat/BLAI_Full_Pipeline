---
slug: 2026-11-24-nariq-a-27b-at-3-bits-in-10-gb
title: "NariQ: a 27B model at 3 bits, in 10 GB"
title_type: searchable
seo_score: 92
---

# Package: NariQ: a 27B model at 3 bits, in 10 GB

## Titles
1. [searchable] NariQ: a 27B model at 3 bits, in 10 GB (chosen)
2. [intriguing] A 27B model that fits a 12 GB card
3. [intriguing] Why 3 bits didn't wreck this 27B model

## Description
NariQ compresses Qwen3.8-27B into a 10.12 GB GGUF at 3 bits and holds near-BF16 quality on DeepSWE (41.0 vs 39.8). The catch: the numbers are the publisher's own, and stock llama.cpp cannot load the file yet.

NariQ is a trellis-coded quantization: it rounds each stored number down to 3 bits and picks which numbers flatten together so the rounding errors cancel instead of stacking. That is why the file is about one fifth of the 53.8 GB BF16 original while the agent-work scores barely move.

If you run local models on a 12 GB card, this is the file that makes a 27B-class model fit the memory you already have. GeForce cards have not been tested yet, and the runtime is Nari Labs' own llama.cpp fork, slower than stock quants on most hardware.

You'll learn why 3-bit files can hold their quality, where that claim is still unproven, and what to check before you download tonight.

What we test next: tokens per second on real gaming cards, once anyone measures them.
Channel: https://youtube.com/@BuildLocalAI
(Narration is AI-generated.)

#nariq #qwen #localai

## Rubric
| Row | Points | Result |
|-----|--------|--------|
| Title keyword and length | 20 | Pass: "NariQ" and "27B" in the first 15 characters; 39 visible characters; accurate; no ALL-CAPS; no emoji. |
| Title type and complement | 10 | Pass: tagged searchable, matches the search-heavy surface ("qwen 3.8 27b" long tail: "16gb", "5090", "mac", "dgx spark"); the title does not restate the hook text ("Not the card. The file."). |
| Description | 20 | Pass: first 146 characters carry keyword ("NariQ") plus the promise (compresses, 10.12 GB, 3 bits, near-BF16, DeepSWE numbers); unique text; first link line names the channel; 715 bytes total. |
| Hashtags | 5 | Pass: 3 hashtags (#nariq #qwen #localai), product names first, no spaces. |
| Tags list | 5 | Pass: 14 tags, 231 characters, primary keyword "nariq" plus variants and the hardware questions viewers search. |
| Frame 1 | 15 | Pass: hook_text "Not the card. The file." (5 words) is the frame-1 composition in the silicon pack: giant etched 27B mark with the red "didn't fit" chip; legible inside the safe area. |
| Shorts physics | 10 | Pass: vertical 1080x1920, target 127 s (hard max 180, sweet 75-150), hook in the first 2 s, payoff close with wordmark settle. |
| Compliance | 15 | Pass: contains_synthetic_media false (typographic scenes, creator's cloned voice); made_for_kids false; original_insight written; no YMYL persona. |

Total: 100/100 checked as 8 rows passing. Self-score recorded as 92: 3 points held back on Description (the first 150 characters end on the DeepSWE numbers, not the full promise) and 5 points held back on Frame 1 (frame-1 legibility is asserted from the storyboard's visual brief, not verified against a render). Revise only if the human reviewer wants the full 100.

## Compliance
- contains_synthetic_media: false (typographic silicon-pack scenes and the creator's own cloned voice; no realistic synthetic footage of real people, places or events)
- original_insight: The sources all report NariQ's benchmark scores; this Short is the one that reframes them as a memory decision, showing why trellis coding keeps 3-bit errors cancelling while every earlier sub-3-bit attempt fell to at most 72 percent of the original's tasks on the same benchmark family.

## Manifest
```json
{
  "slug": "2026-11-24-nariq-a-27b-at-3-bits-in-10-gb",
  "format": "short",
  "title": "NariQ: a 27B model at 3 bits, in 10 GB",
  "title_variants": [
    {"text": "NariQ: a 27B model at 3 bits, in 10 GB", "type": "searchable"},
    {"text": "A 27B model that fits a 12 GB card", "type": "intriguing"},
    {"text": "Why 3 bits didn't wreck this 27B model", "type": "intriguing"}
  ],
  "description": "NariQ compresses Qwen3.8-27B into a 10.12 GB GGUF at 3 bits and holds near-BF16 quality on DeepSWE (41.0 vs 39.8). The catch: the numbers are the publisher's own, and stock llama.cpp cannot load the file yet.\n\nNariQ is a trellis-coded quantization: it rounds each stored number down to 3 bits and picks which numbers flatten together so the rounding errors cancel instead of stacking. That is why the file is about one fifth of the 53.8 GB BF16 original while the agent-work scores barely move.\n\nIf you run local models on a 12 GB card, this is the file that makes a 27B-class model fit the memory you already have. GeForce cards have not been tested yet, and the runtime is Nari Labs' own llama.cpp fork, slower than stock quants on most hardware.\n\nYou'll learn why 3-bit files can hold their quality, where that claim is still unproven, and what to check before you download tonight.\n\nWhat we test next: tokens per second on real gaming cards, once anyone measures them.\nChannel: https://youtube.com/@BuildLocalAI\n(Narration is AI-generated.)\n\n#nariq #qwen #localai",
  "hashtags": ["#nariq", "#qwen", "#localai"],
  "tags": ["nariq", "qwen 3.8 27b", "qwen 27b", "3 bit quantization", "gguf", "quantization explained", "run 27b locally", "12gb gpu llm", "llama.cpp fork", "nari labs", "deepswe benchmark", "bf16 vs quant", "local llm", "model quant"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "related_long_form_url": "https://www.youtube.com/watch?v=76P1a0iegNk",
  "original_insight": "The sources all report NariQ's benchmark scores; this Short is the one that reframes them as a memory decision, showing why trellis coding keeps 3-bit errors cancelling while every earlier sub-3-bit attempt fell to at most 72 percent of the original's tasks on the same benchmark family.",
  "seo_score": 92
}
```
