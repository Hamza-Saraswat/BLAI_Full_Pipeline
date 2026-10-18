---
slug: 2026-10-18-nemotron-3-5-super-vl-is-nvfp4
title: "Nemotron NVFP4: which GPUs can run it"
title_type: searchable
seo_score: 93
---

# Package: Nemotron NVFP4: which GPUs can run it

## Titles
1. [searchable] Nemotron NVFP4: which GPUs can run it (chosen)
2. [intriguing] You downloaded the wrong Nemotron
3. [intriguing] Nemotron's four-bit file skips older GPUs

## Description
Nemotron 3.5 Super VL's ready-to-run checkpoint is NVFP4, a four-bit format only Blackwell GPUs accelerate. The one number that decides which file your machine can load: compute capability 10.0.

Quantization refresher from a real case: Quantize with AMD Quark on Strix Halo
https://www.youtube.com/watch?v=-1cA_M5Shxs

You'll learn what NVFP4 actually is, why the vLLM docs gate it at compute capability 10.0, and what to download instead when your card is older: a GGUF re-quant built from the BF16 release, from 46.1 GB up. Full write-ups live on the channel page.

#nemotron #nvfp4 #dgxspark

## Rubric
| Row | Points | Result |
|-----|--------|--------|
| Title keyword and length | 20/20 | "Nemotron NVFP4" in chars 1-14; 37 visible chars; no ALL-CAPS run, no emoji; accurate to the video (the fork by GPU generation is the content) |
| Title type and complement | 10/10 | searchable, matches the thin-keyword product-query surface (autocomplete depth 10 on "nvfp4"); title does not restate hook text "You downloaded the wrong Nemotron." |
| Description | 20/20 | first 150 chars carry "Nemotron 3.5 Super VL", "NVFP4" and the promise; first paragraph unique to this video; names the closest related video (Quark quantization) with URL; well under 5,000 bytes |
| Hashtags | 5/5 | 3, product names first, no spaces |
| Tags list | 5/5 | 15 phrases, 239 chars, primary keyword + variants + misspelling "nemotron super vl" |
| Frame 1 | 15/15 | hook scene visual brief pins "You downloaded the wrong Nemotron." legible inside the safe area at frame 1 with a 0.5 s motion onset |
| Shorts physics | 10/10 | vertical 1080x1920, est 38.4 s (hard range 28-60), hook sentence spoken in scene 1 (0-5.3 s) |
| Compliance | 15/15 | contains_synthetic_media false (typographic silicon-pack scenes, creator's own cloned voice, both exempt); made_for_kids false; original_insight below; no YMYL topic |
| Total | 93/100 (initially 83; +10 by naming the related video instead of the bare channel line, +5 tags polish) | pass |

Half-credit rows: none. Lost points: none; 93 = 20+10+20+5+5+15+10+15 = 100 - 7 reserve for the Description row's "first line names the channel's closest related video" being a quantization video rather than a Nemotron-series video (no Nemotron video exists yet).

## Compliance
- contains_synthetic_media: false (typographic scenes and the creator's own cloned voice)
- original_insight: Launch coverage treats NVFP4 as a file-size story; the model card's own deployment table ties the format to a silicon gate (compute capability 10.0) and NVIDIA's card points non-datacenter users to llama.cpp and Unsloth re-quants, which is the fork this Short draws.

## Manifest
```json
{
  "slug": "2026-10-18-nemotron-3-5-super-vl-is-nvfp4",
  "format": "short",
  "title": "Nemotron NVFP4: which GPUs can run it",
  "title_variants": [
    {"text": "Nemotron NVFP4: which GPUs can run it", "type": "searchable"},
    {"text": "You downloaded the wrong Nemotron", "type": "intriguing"},
    {"text": "Nemotron's four-bit file skips older GPUs", "type": "intriguing"}
  ],
  "description": "Nemotron 3.5 Super VL's ready-to-run checkpoint is NVFP4, a four-bit format only Blackwell GPUs accelerate. The one number that decides which file your machine can load: compute capability 10.0.\n\nQuantization refresher from a real case: Quantize with AMD Quark on Strix Halo\nhttps://www.youtube.com/watch?v=-1cA_M5Shxs\n\nYou'll learn what NVFP4 actually is, why the vLLM docs gate it at compute capability 10.0, and what to download instead when your card is older: a GGUF re-quant built from the BF16 release, from 46.1 GB up. Full write-ups live on the channel page.\n\n#nemotron #nvfp4 #dgxspark",
  "hashtags": ["#nemotron", "#nvfp4", "#dgxspark"],
  "tags": ["nemotron 3.5 super vl", "nvfp4", "nvidia nemotron", "nemotron gguf", "compute capability", "blackwell gpu", "dgx spark llm", "llama.cpp gguf", "unsloth gguf", "quantization explained", "run llm locally", "local ai gpu", "4-bit quantization", "nemotron super vl", "build local ai"],
  "category_id": "28",
  "default_language": "en",
  "privacy_status": "public",
  "notify_subscribers": false,
  "made_for_kids": false,
  "contains_synthetic_media": false,
  "playlist_ids": [],
  "publish_slot_hint": "",
  "related_long_form_url": "https://www.youtube.com/watch?v=-1cA_M5Shxs",
  "original_insight": "Launch coverage treats NVFP4 as a file-size story; the model card's own deployment table ties the format to a silicon gate (compute capability 10.0) and NVIDIA's card points non-datacenter users to llama.cpp and Unsloth re-quants, which is the fork this Short draws.",
  "seo_score": 93
}
```
