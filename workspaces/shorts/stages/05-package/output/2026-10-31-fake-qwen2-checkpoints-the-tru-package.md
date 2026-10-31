---
slug: 2026-10-31-fake-qwen2-checkpoints-the-tru
title: "Fake Hugging Face models: Qwen2 trap"
title_type: searchable
seo_score: 100
---

# Package: Fake Hugging Face models: Qwen2 trap

## Titles

1. [searchable] Fake Hugging Face models: Qwen2 trap (chosen: the ideas gap is a defensive
   checklist people search for after malware news; keyword "fake huggingface model" depth 29)
2. [intriguing] This Qwen2 download was 42 bytes
3. [intriguing] The scan said clean. The org said no.

Chosen: 1. Search-heavy surface (defensive how-to after a disclosure), and it names both
products (Hugging Face, Qwen2). Title does not restate the frame-1 text ("You click trust.
The repo runs first.").

## Description

Fake Hugging Face models looked like Qwen2 test checkpoints. Here is the check that catches them before you load anything.

Pluto Security tracked 31 of them across seven accounts. This video walks one fake repo end to end: the copied model card, the 42-byte weights file, and the one flag that runs a stranger's Python before any weights load. Check the org, open the files page, keep trust_remote_code off unless you read the code. Your GPU stays yours.

Channel: https://youtube.com/@BuildLocalAI

#HuggingFace #Qwen2 #LocalAI

## Rubric

| Row | Points | Result |
|-----|--------|--------|
| Title keyword and length | 20/20 | keyword "Fake Hugging Face models" chars 1-24; 37 visible chars; accurate; no ALL-CAPS run; no emoji |
| Title type and complement | 10/10 | tagged searchable; search-heavy topic; complements, does not repeat, the frame-1 text |
| Description | 20/20 | keyword + promise in first 126 chars; unique text; channel line present; ~430 bytes |
| Hashtags | 5/5 | 3 hashtags, product names first |
| Tags list | 5/5 | 12 phrases, 218 chars, primary keyword + variants |
| Frame 1 | 15/15 | hook text typewriters at frame 1 inside the safe area, caret motion from 0.30 s |
| Shorts physics | 10/10 | vertical 1080x1920, 44 s, hook is sentence one |
| Compliance | 15/15 | contains_synthetic_media false (typographic scenes, creator's own cloned voice); made_for_kids false; original_insight below |

## Compliance

- contains_synthetic_media: false (typographic terminal scenes and the creator's own cloned
  voice, both explicitly exempt per compliance.md)
- original_insight: Maps each of Pluto's disclosure indicators onto a pre-download check the
  viewer runs on the model page itself, turning a security report into a tonight checklist.

## Manifest

```json
{
  "slug": "2026-10-31-fake-qwen2-checkpoints-the-tru",
  "format": "short",
  "title": "Fake Hugging Face models: Qwen2 trap",
  "title_variants": [
    {"text": "Fake Hugging Face models: Qwen2 trap", "type": "searchable"},
    {"text": "This Qwen2 download was 42 bytes", "type": "intriguing"},
    {"text": "The scan said clean. The org said no.", "type": "intriguing"}
  ],
  "description": "Fake Hugging Face models looked like Qwen2 test checkpoints. Here is the check that catches them before you load anything.\n\nPluto Security tracked 31 of them across seven accounts. This video walks one fake repo end to end: the copied model card, the 42-byte weights file, and the one flag that runs a stranger's Python before any weights load. Check the org, open the files page, keep trust_remote_code off unless you read the code. Your GPU stays yours.\n\nChannel: https://youtube.com/@BuildLocalAI\n\n#HuggingFace #Qwen2 #LocalAI",
  "hashtags": ["#HuggingFace", "#Qwen2", "#LocalAI"],
  "tags": ["fake huggingface model", "hugging face malware", "qwen2", "trust_remote_code", "safetensors", "fake model checkpoint", "hugging face security", "crypto mining malware", "local llm safety", "model verification", "pluto security load mine", "run llm at home"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "related_long_form_url": "",
  "original_insight": "Maps each of Pluto's disclosure indicators onto a pre-download check the viewer runs on the model page itself, turning a security report into a tonight checklist.",
  "seo_score": 100
}
```
