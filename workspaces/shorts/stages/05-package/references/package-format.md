# Package Note Format

```
---
slug: [slug]
title: [chosen title]
title_type: searchable | intriguing
seo_score: 86
---

# Package: [chosen title]

## Titles
1. [searchable] ...
2. [intriguing] ... (chosen)
3. [intriguing] ...

## Description
(the exact text that will be uploaded)

## Rubric
| Row | Points | Result |
(one row per rubric line, with the reason for any lost points)

## Compliance
- contains_synthetic_media: false (typographic scenes and the creator's own cloned voice)
- original_insight: one sentence naming what this Short adds that the sources did not say

## Manifest
```json
{
  "slug": "2026-08-25-deepseek-v4-flash-128gb",
  "format": "short",
  "title": "Can DeepSeek V4 Flash run on 128 GB?",
  "title_variants": [
    {"text": "How to run DeepSeek V4 Flash on a DGX Spark", "type": "searchable"},
    {"text": "Can DeepSeek V4 Flash run on 128 GB?", "type": "intriguing"},
    {"text": "DeepSeek V4 Flash vs 128 GB of memory", "type": "intriguing"}
  ],
  "description": "DeepSeek V4 Flash on a DGX Spark: what fits in 128 GB and how fast it runs.\n\nFull episode: https://youtube.com/@BuildLocalAI\n\n#deepseek #dgxspark #localai",
  "hashtags": ["#deepseek", "#dgxspark", "#localai"],
  "tags": ["deepseek v4 flash", "dgx spark", "local llm", "run llm locally", "deepseek local"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "related_long_form_url": "",
  "original_insight": "Measured on our own Spark: the FP8 build leaves 40 GB free for context, which no review mentioned.",
  "seo_score": 86
}
```
```

The manifest is what `skills/blotato-publish/scripts/publish.py` reads; its schema is `shared/schemas/publish-manifest.schema.json`. The description string in the manifest is the source of truth; the "Description" section above is for reading in Obsidian and must match it.
