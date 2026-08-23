---
slug: quantization-formats-tour
series: local-ai-for-dummies
structure: concept-deep-dive
value_types: TEACHES, REFRAMES
target_minutes: 3
words: 500
chapters: 3
---

# A tour of the quantization formats

Fixture: a deliberately bad script for `validate_longform.py`. Six positional labels in a `concept-deep-dive`, one ninety-word beat, a spoken call to action, and no second person anywhere. Do not copy anything here.

## Chapter 1: What quantization is
| Beat | Narration (spoken form) | On-screen text | Visual intent | Scene hint | Capture cue |
|------|-------------------------|----------------|---------------|------------|-------------|
| 1.1 | In this video we will look at quantization from the ground up. Quantization is a family of techniques for storing model weights in fewer bits. There are many formats. Most people encounter four of them, and the differences between those four are mostly historical rather than practical. | 4 formats | A list of format names fades in | kinetic-text | |
| 1.2 | The taxonomy is the usual starting point. There is round to nearest, there is group-wise scaling, there is the k-quant family, and there is the newer four-bit floating point work. Each of these has a paper, a repository, and a set of benchmark tables that mostly agree with each other. | taxonomy | Four boxes appear in a grid | diagram | |
| 1.3 | The reason all of this matters is that memory is finite, and a model that does not fit does not run at all, which is a fact that gets rediscovered constantly in forums and issue threads and comment sections, usually by someone who has just spent an hour downloading a file. The arithmetic is not complicated. Parameters times bits per parameter divided by eight gives bytes. Everything else in this space is an argument about how much accuracy is acceptable to lose in exchange for that arithmetic coming out smaller. | params x bits / 8 | The formula writes itself out | kinetic-text | |

## Chapter 2: The formats in order
| Beat | Narration (spoken form) | On-screen text | Visual intent | Scene hint | Capture cue |
|------|-------------------------|----------------|---------------|------------|-------------|
| 2.1 | Stage one. The weights arrive as sixteen-bit floating point numbers from the original training run. This is the reference that every other format is measured against, and it is the baseline for the tables below. | FP16 baseline | A full-width bar labelled sixteen bit | diagram | |
| 2.2 | Stage two. Group-wise scaling splits the tensor into blocks of thirty-two and stores one scale factor per block. Stage three. The k-quant family mixes precisions inside a single file, which is why its names have letters in them. | blocks of 32 | The bar splits into blocks | diagram | |
| 2.3 | Stage four is the strange one. Four-bit floating point keeps an exponent, which matters for outliers in the attention layers. Nothing about this ordering is sequential, and none of these stages happens after another one in any real pipeline. | FP4 keeps an exponent | A bit layout diagram | diagram | |
| 2.4 | Stage five. Benchmarks for all of these land within two percentage points of each other on the common evaluation suites, which is a result that surprises people who expected the newer formats to win by a wide margin. | within 2 points | A bar chart with four nearly equal bars | chart | |

## Chapter 3: Which one to use
| Beat | Narration (spoken form) | On-screen text | Visual intent | Scene hint | Capture cue |
|------|-------------------------|----------------|---------------|------------|-------------|
| 3.1 | Stage six. Selection in practice comes down to what the runtime supports, not to what the papers recommend, and most runtimes support two of these formats well and the rest badly. | runtime support | A support matrix fills in | comparison-table | |
| 3.2 | A user who wants the smallest file will pick the k-quant family. A user who wants the best accuracy per gigabyte on newer hardware will pick the four-bit floating point build. Neither choice is wrong, and both are widely deployed today. Both appear in the same download menus. | two live choices | Two rows highlight | comparison-table | |
| 3.3 | The honest summary is that the format matters less than the context length, which is where the memory actually goes on a long conversation. Most of the debate in this area is about a few percentage points of file size. | context beats format | A context bar dwarfs the weights bar | diagram | |
| 3.4 | That is the landscape. Subscribe if a deeper walk through the k-quant naming scheme would be useful, because that is the natural follow-up to this material and it deserves its own episode. | more to come | The wordmark settles | end-card | |
