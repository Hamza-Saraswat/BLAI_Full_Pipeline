# Voice Note Format

```
---
slug: [slug]
duration_s: 37.4
chars: 812
chunks: 1
wer: 0.012
model: eleven_multilingual_v2
---

# Voice: [slug]

## Timing
| Scene | Starts at | Ends at | Seconds |
(one row per scene, computed from captions.json by matching each scene's first and last word)

## QA
- WER: 0.012 (threshold 0.03)
- Mismatches: "Kwen" heard as "Queen" at 12.4 s (dictionary entry added: Qwen -> Kwen)

## Normalizer expansions
- "27B" -> "twenty-seven billion" (scene s02): fix in the script next time

## Rounds
1. generated 1 chunk, 37.4 s, QA pass
```

Rules: numbers in this note are copied from `voice.json` and `qa.json`; the Timing table is what the render stage uses to size scenes.
