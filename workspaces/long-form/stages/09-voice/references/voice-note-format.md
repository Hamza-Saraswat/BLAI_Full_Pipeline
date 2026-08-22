# Voice Note Format (long-form)

```
---
slug: [slug]
duration_s: 734.2
chars: 11840
chunks: 9
wer: 0.014
model: eleven_multilingual_v2
---

# Voice: [slug]

## Chapters (measured)
| Chapter | Starts at | Seconds |
(from captions.json: the first word of each chapter's first beat)

## Chunks
| Chunk | Chars | Seconds | WER | Regenerated |

## Mismatches
- "Kwen" heard as "Queen" at 312.4 s (dictionary entry added)

## Rounds
1. 9 chunks, 734.2 s, QA pass
```

The Chapters table is what the render stage uses for chapter cards and what the publish stage uses for the description's chapter block.
