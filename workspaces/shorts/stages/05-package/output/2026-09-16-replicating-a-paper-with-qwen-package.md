---
slug: 2026-09-16-replicating-a-paper-with-qwen
title: Qwen-2.5 replicates Jev's trick at home
title_type: searchable
seo_score: 100
---

# Package: Qwen-2.5 replicates Jev's trick at home

## Titles
1. [searchable] Qwen-2.5 replicates Jev's trick at home (chosen)
2. [intriguing] Jev's speed isn't in the weights
3. [intriguing] Qwen-2.5 already has Jev's trick

Chosen: searchable. The ideas note scored this pick on autocomplete depth 72 for "qwen 2.5" with task suffixes -- a search surface -- so the searchable title wins per titles-descriptions.md.

## Description

Qwen-2.5 already has Jev's speed trick: stop writing JSON, score every field in one pass. The open replication, and how to run it tonight.

TypeSafe's Jev model made headlines by refusing to generate text. An open replication on Hugging Face reproduces the launch numbers with the stock Qwen-2.5-1.5B-Instruct-4bit checkpoint and no new training: on a 28-field form, 312 forward passes become 1 and the run drops from 1,900 ms to 270 ms on a MacBook. Guaranteed shape is not guaranteed truth, so route low-confidence fields to a human or a bigger model.

Every measurement in the video is the replication author's published M4 Max run; source links in the pinned comment.

More local AI: https://youtube.com/@BuildLocalAI

#Qwen #Jev #LocalAI

## Rubric

| Row | Points | Result |
|-----|--------|--------|
| Title keyword and length | 20 | "Qwen-2.5" at char 1; 39 visible chars; accurate; no ALL-CAPS, no emoji |
| Title type and complement | 10 | searchable, matches the search-heavy surface; does not restate frame-1 text ("Not the weights. The decoding.") |
| Description | 20 | keyword + promise in the first 137 characters; unique text; channel line present; 617 bytes |
| Hashtags | 5 | 3 hashtags, product names first, no spaces |
| Tags list | 5 | 15 lowercase phrases, 231 chars with commas, primary keyword + variants |
| Frame 1 | 15 | hook text "Not the weights. The decoding." fully legible at frame 1 in the terminal window, 312-to-1 typing onset within 0.5 s |
| Shorts physics | 10 | vertical 1080x1920, 139 s estimate under the 180 s cap, hook in the first 2 s |
| Compliance | 15 | contains_synthetic_media false (typographic scenes, creator's own cloned voice); made_for_kids false; original_insight below; no YMYL topics |
| Total | 100 | pass (>= 80) |

## Compliance
- contains_synthetic_media: false (typographic terminal scenes and the creator's own cloned voice, both exempt)
- original_insight: This Short splits Jev's launch into two claims -- decoding speed, which stock Qwen-2.5 weights already deliver on a home Mac, and answer correctness, which no decoding trick fixes -- a boundary the vendor page leaves to the FAQ.

## Manifest
```json
{
  "slug": "2026-09-16-replicating-a-paper-with-qwen",
  "format": "short",
  "title": "Qwen-2.5 replicates Jev's trick at home",
  "title_variants": [
    {"text": "Qwen-2.5 replicates Jev's trick at home", "type": "searchable"},
    {"text": "Jev's speed isn't in the weights", "type": "intriguing"},
    {"text": "Qwen-2.5 already has Jev's trick", "type": "intriguing"}
  ],
  "description": "Qwen-2.5 already has Jev's speed trick: stop writing JSON, score every field in one pass. The open replication, and how to run it tonight.\n\nTypeSafe's Jev model made headlines by refusing to generate text. An open replication on Hugging Face reproduces the launch numbers with the stock Qwen-2.5-1.5B-Instruct-4bit checkpoint and no new training: on a 28-field form, 312 forward passes become 1 and the run drops from 1,900 ms to 270 ms on a MacBook. Guaranteed shape is not guaranteed truth, so route low-confidence fields to a human or a bigger model.\n\nEvery measurement in the video is the replication author's published M4 Max run; source links in the pinned comment.\n\nMore local AI: https://youtube.com/@BuildLocalAI\n\n#Qwen #Jev #LocalAI",
  "hashtags": ["#Qwen", "#Jev", "#LocalAI"],
  "tags": ["qwen 2.5", "jev", "typesafe jev", "parallel constrained decoding", "structured output llm", "qwen 2.5 local", "run qwen locally", "mlx", "mlx lm", "json schema llm", "local llm", "ollama qwen", "open weights model", "system one model", "small model structured output"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "11:00 CT",
  "related_long_form_url": "",
  "original_insight": "This Short splits Jev's launch into two claims -- decoding speed, which stock Qwen-2.5 weights already deliver on a home Mac, and answer correctness, which no decoding trick fixes -- a boundary the vendor page leaves to the FAQ.",
  "seo_score": 100
}
```
