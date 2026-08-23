---
slug: quantization-formats-tour
series: local-ai-for-dummies
structure: concept-deep-dive
value_types: TEACHES, REFRAMES
target_minutes: 3
---

# Outline: A tour of the quantization formats

Fixture: the outline `bad-script.md` was written from. Trimmed to three target minutes.

## Angle
The quantization formats are a taxonomy, and the taxonomy is what everyone teaches.

## Value brief
- TEACHES: what each named format does to a tensor
- REFRAMES: the context length costs more memory than the format choice
- Hook: there are four formats and the differences are mostly historical
- Payoff: pick what the runtime supports
- The number by 0:20: four formats

## Chapters
| # | Chapter | Target s | The one idea | Measurement shown | Muted viewer understands |
|---|---------|----------|--------------|-------------------|--------------------------|
| 1 | What quantization is | 76 | Fewer bits per weight | none | a formula resolving |
| 2 | The formats in order | 62 | Four named formats | benchmark spread | four bars, nearly equal |
| 3 | Which one to use | 61 | The runtime decides | none | a support matrix |

## Decisions
- Kept the taxonomy shape on purpose: this fixture exists to fail the gate.
