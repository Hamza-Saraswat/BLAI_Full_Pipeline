---
slug: 2026-10-14-lfm2-5-24b-a2b-a-24b-moe-that
title: "LFM2.5-24B-A2B: a 24B that runs like 2B"
title_type: searchable
seo_score: 100
---

# Package: LFM2.5-24B-A2B, a 24B MoE that runs like a 2B

## Titles
1. [searchable] "LFM2.5-24B-A2B: a 24B that runs like 2B" (chosen)
2. [intriguing] "Why LFM2.5 wakes only 2.45B per word"
3. [intriguing] "184 tok/s from a 24B, on a laptop"

Chosen: the searchable one. A two-day-old model means high search intent on the product name (the stage-02 keyword was "lfm2 24b"); intriguing variants open the gap for feed viewers but the product-name query is the surface this wins.

## Description
LFM2.5-24B-A2B explained: 24B parameters stored, only 2.45B compute each token, so a laptop runs it at 184 tok/s. Liquid's own numbers, the honest catch (agent wins, knowledge losses), and the one-line way to run it today.

Closest related: we ran an MoE daily on the Spark -- https://www.youtube.com/watch?v=FxdhJ7wKpT0

Total is what memory pays for; active is what speed pays for. All speed, memory and benchmark figures are Liquid's measurements (llama.cpp, Q4_K_M); no independent benchmark of this exact model exists yet. Full run command in the pinned comment.

#lfm2 #liquidai #localai

## Rubric
| Row | Points | Result |
|---|---|---|
| Title keyword and length | 20/20 | keyword at char 0, 40 visible chars, accurate, one product-name caps token, no emoji |
| Title type and complement | 10/10 | searchable, matches search-heavy surface; title does not restate the hook text |
| Description | 20/20 | keyword + promise in first 150 chars, unique text, first line names the closest related video, well under 5,000 bytes |
| Hashtags | 5/5 | 3, product names first, no spaces |
| Tags list | 5/5 | 11 phrases, about 120 chars, primary keyword plus variants |
| Frame 1 | 15/15 | hook text centered and legible at frame 1 inside the safe area, motion onset 0.40 s |
| Shorts physics | 10/10 | vertical 1080x1920, target 105 s, hook in the first 2 s |
| Compliance | 15/15 | synthetic media false (typographic scenes, creator voice clone), made-for-kids false, original insight written |
| Total | 100/100 | |

## Compliance
- contains_synthetic_media: false (typographic axon scenes and the creator's own cloned voice; no realistic synthetic footage)
- original_insight: the one-number decode of the "runs like a 2B" claim -- memory pays the 24.0B total bill while speed pays only the 2.45B active bill, with Liquid's own table showing the trade (agent wins, knowledge losses); no source frames the release that way.

## Manifest
```json
{
  "slug": "2026-10-14-lfm2-5-24b-a2b-a-24b-moe-that",
  "format": "short",
  "title": "LFM2.5-24B-A2B: a 24B that runs like 2B",
  "title_variants": [
    {"text": "LFM2.5-24B-A2B: a 24B that runs like 2B", "type": "searchable"},
    {"text": "Why LFM2.5 wakes only 2.45B per word", "type": "intriguing"},
    {"text": "184 tok/s from a 24B, on a laptop", "type": "intriguing"}
  ],
  "description": "LFM2.5-24B-A2B explained: 24B parameters stored, only 2.45B compute each token, so a laptop runs it at 184 tok/s. Liquid's own numbers, the honest catch (agent wins, knowledge losses), and the one-line way to run it today.\n\nClosest related: we ran an MoE daily on the Spark -- https://www.youtube.com/watch?v=FxdhJ7wKpT0\n\nTotal is what memory pays for; active is what speed pays for. All speed, memory and benchmark figures are Liquid's measurements (llama.cpp, Q4_K_M); no independent benchmark of this exact model exists yet. Full run command in the pinned comment.\n\n#lfm2 #liquidai #localai",
  "hashtags": ["#lfm2", "#liquidai", "#localai"],
  "tags": ["lfm2.5-24b-a2b", "lfm2 24b", "lfm2.5", "liquid ai", "mixture of experts", "local llm", "run llm locally", "llama.cpp", "lm studio", "local ai", "lfm2"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "related_long_form_url": "",
  "original_insight": "The one-number decode of the runs-like-a-2B claim: memory pays the 24.0B total bill while speed pays only the 2.45B active bill, and Liquid's own table shows the trade (agent wins, knowledge losses).",
  "seo_score": 100
}
```
