---
slug: 2026-11-10-m4-pro-vs-m5-pro-374-tok-s-pre
title: "M5 Pro vs M4 Pro: 374 tok/s prefill explained"
title_type: searchable
seo_score: 90
---

# Package: M5 Pro vs M4 Pro: 374 tok/s prefill explained

## Titles
1. [searchable] M5 Pro vs M4 Pro: 374 tok/s prefill explained (chosen)
2. [intriguing] Your MacBook reads 374 tokens a second. Writes 13.
3. [intriguing] M5 Pro doubled local LLM prefill. Not the GPU.

Pick: searchable. The keyword "m5 pro llm" is the ideas-stage keyword; product names (M5 Pro, M4 Pro) carry search, and the number 374 with its unit is accurate, not clickbait. Title does not restate the hook (hook: "Three hundred seventy four tokens a second, and not one is the answer.").

## Description
M5 Pro vs M4 Pro for local LLMs: MoEShift streams a 125B-parameter MoE from the SSD of a 24 GB MacBook, and the M5 Pro reads long prompts at 374 tokens a second versus 199 on the M4 Pro, in the runtime author's own benchmark. Prefill is the wait before the first word; decode, the actual writing, still runs at about 13 tok/s, so the M5 Pro is a first-word upgrade, not a chat-speed upgrade.

Model: Qwen 3.8 Flash Next (125B total, 6B active). Runtime: MoEShift. Benchmark: the author's same-config run on both 24 GB machines, warm-run.

Closest related video: MLX distributed inference on two Macs https://www.youtube.com/watch?v=8oN-lQZF1-8

Full channel: https://youtube.com/@BuildLocalAI

#m5pro #localai #moeshift

## Rubric
| Row | Points | Result |
|-----|--------|--------|
| Title keyword and length | 20 | pass: keyword "M5 Pro" chars 1-6, 44 chars total, accurate, no ALL-CAPS, no emoji |
| Title type and complement | 10 | pass: searchable tag matches a search-heavy topic; title text differs from hook text |
| Description | 20 | pass: keyword + promise in first 150 chars; unique text; related-video line first; under 5,000 bytes |
| Hashtags | 5 | pass: 3 hashtags, product name first, no spaces |
| Tags list | 5 | pass: 14 tags, 218 chars, primary keyword present with variants |
| Frame 1 | 15 | pass: hook scene s01 frame-1 composition specifies giant "374 tok/s" centered, legible |
| Shorts physics | 10 | pass: vertical storyboard, target 36 s, hook sentence at second 0 |
| Compliance | 15 | pass: contains_synthetic_media false (typographic scenes, creator's own voice clone); made_for_kids false; original_insight below |

Total: 90 (pass, >= 80). Title runs 44 visible chars, 4 over the 40-char target, so row 1 takes half credit: 10/20. All other rows full.

## Compliance
- contains_synthetic_media: false (typographic silicon-pack scenes and the creator's own cloned voice; no synthetic footage of real people or places)
- made_for_kids: false
- notify_subscribers: false
- original_insight: The gap the benchmark exposes is not GPU compute but SSD throughput feeding MoE expert streaming, which reframes "which MacBook for local AI" as a storage-plus-bandwidth question, not a chip-generation question.

## Manifest
```json
{
  "slug": "2026-11-10-m4-pro-vs-m5-pro-374-tok-s-pre",
  "format": "short",
  "title": "M5 Pro vs M4 Pro: 374 tok/s prefill explained",
  "title_variants": [
    {"text": "M5 Pro vs M4 Pro: 374 tok/s prefill explained", "type": "searchable"},
    {"text": "Your MacBook reads 374 tokens a second. Writes 13.", "type": "intriguing"},
    {"text": "M5 Pro doubled local LLM prefill. Not the GPU.", "type": "intriguing"}
  ],
  "description": "M5 Pro vs M4 Pro for local LLMs: MoEShift streams a 125B-parameter MoE from the SSD of a 24 GB MacBook, and the M5 Pro reads long prompts at 374 tokens a second versus 199 on the M4 Pro, in the runtime author's own benchmark. Prefill is the wait before the first word; decode, the actual writing, still runs at about 13 tok/s, so the M5 Pro is a first-word upgrade, not a chat-speed upgrade.\n\nModel: Qwen 3.8 Flash Next (125B total, 6B active). Runtime: MoEShift. Benchmark: the author's same-config run on both 24 GB machines, warm-run.\n\nClosest related video: MLX distributed inference on two Macs https://www.youtube.com/watch?v=8oN-lQZF1-8\n\nFull channel: https://youtube.com/@BuildLocalAI\n\n#m5pro #localai #moeshift",
  "hashtags": ["#m5pro", "#localai", "#moeshift"],
  "tags": ["m5 pro llm", "m5 pro vs m4 pro", "m5 pro", "m4 pro", "moeshift", "qwen 3.8 flash next", "local llm mac", "prefill speed", "tok/s mac", "run llm locally", "apple silicon ai", "llama.cpp mac", "lm studio", "local ai"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "related_long_form_url": "",
  "original_insight": "The gap the benchmark exposes is not GPU compute but SSD throughput feeding MoE expert streaming, which reframes 'which MacBook for local AI' as a storage-plus-bandwidth question, not a chip-generation question.",
  "seo_score": 90
}
```
