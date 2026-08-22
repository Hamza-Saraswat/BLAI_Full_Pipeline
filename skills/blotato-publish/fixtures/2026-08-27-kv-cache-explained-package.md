# Package: KV cache explained (fixture, long-form)

Fixture with chapters, a thumbnail path and a slot hint, for `scripts/publish.py --dry-run`.

```json
{
  "slug": "2026-08-27-kv-cache-explained",
  "format": "long",
  "title": "Why your GPU's doorway matters: the KV cache from zero",
  "title_variants": [
    {"text": "KV cache explained for local LLMs", "type": "searchable"},
    {"text": "The number that decides your context length", "type": "intriguing"},
    {"text": "How much context fits on a DGX Spark", "type": "searchable"}
  ],
  "description": "One worked example, carried the whole way: a 32B model, a 128 GB box, and the cache that decides how much context fits.",
  "hashtags": ["#LocalAI", "#LLM"],
  "privacy_status": "private",
  "notify_subscribers": true,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": ["PLEXAMPLE"],
  "thumbnail": "thumbnails/2.png",
  "chapters": [
    {"time": "00:00", "label": "The doorway"},
    {"time": "02:10", "label": "What the cache stores"},
    {"time": "06:40", "label": "Measuring it on the Spark"}
  ],
  "publish_slot_hint": "2026-08-28T09:00:00-05:00",
  "original_insight": "Context length is a memory budget, not a model property; the cache size formula makes it a number you can plan around.",
  "seo_score": 74
}
```
