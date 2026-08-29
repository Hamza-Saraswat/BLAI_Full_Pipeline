# Package: Spark vs 5090 myth (fixture)

Fixture package note for `scripts/publish.py --dry-run`. The manifest block below follows `shared/schemas/publish-manifest.schema.json`.

## Manifest

```json
{
  "slug": "2026-08-25-spark-vs-5090-myth",
  "format": "short",
  "title": "You do not need a 4090 to run a 30B model at home",
  "title_variants": [
    {"text": "DGX Spark vs RTX 5090 for local LLMs", "type": "searchable"},
    {"text": "The 4090 myth, measured", "type": "intriguing"},
    {"text": "Run a 30B model without a 4090", "type": "searchable"}
  ],
  "description": "I loaded Qwen 3 at Q4 on the DGX Spark and measured it against the RTX 5090. One user: the 5090 wins. A room full of users: the Spark does.\n\nMore local AI on the channel: https://www.youtube.com/@BuildLocalAI",
  "hashtags": ["#Shorts", "#LocalAI", "#DGXSpark"],
  "tags": ["dgx spark", "rtx 5090", "local llm", "qwen"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "private",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "original_insight": "Single-stream speed and served throughput answer different questions; the 4090 myth conflates them.",
  "seo_score": 82,
  "reviewer_notes": "Fixture only."
}
```

## Reviewer notes

Fixture only.
