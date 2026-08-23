---
slug: seventy-b-on-the-spark
series: my-dgx-spark-projects
structure: build-along
value_types: EQUIPS, PROVES
target_minutes: 5
words: 789
chapters: 5
---

# Serving a 70B model on the Spark

Fixture: a trimmed build-along used by `validate_longform.py`. Five chapters, three beats each, so the gate can be exercised without a full episode.

## Decisions
- Shape carried from the outline: `build-along`. The failure in chapter 3 is the content, so it keeps a full chapter.

## Chapter 1: The goal
| Beat | Narration (spoken form) | On-screen text | Visual intent | Scene hint | Capture cue |
|------|-------------------------|----------------|---------------|------------|-------------|
| 1.1 | I wanted to serve a seventy-billion-parameter model on the Spark and hand you one command. On paper it fits. The box carries a hundred and twenty-eight gigabytes of unified memory. The four-bit build weighs about forty gigabytes on disk. You have probably run that same arithmetic. | 128 GB / 40 GB | The two numbers land side by side and the smaller one slides inside the larger | stat-callout | |
| 1.2 | So the plan was small. Pull the four-bit weights and start the server. Point a client at it and read the tokens per second off the log. I gave myself one evening. I expected the boring kind of success. | 4 steps, 1 evening | Four short lines type themselves out as a checklist | kinetic-text | |
| 1.3 | What I expected was thirty tokens a second at a context of four thousand. That is roughly what the memory bandwidth on this box allows. I said the number out loud before I ran anything. | expect 30 tok/s | The predicted number sits alone, dimmed, waiting to be corrected | stat-callout | |
| 1.4 | The Spark is the interesting part here. It is one box, not a rack, and the memory is shared between the processor and the graphics side. That is why a model this size is even a conversation on a desk. | one box, shared memory | The box outline appears with a single shared memory pool inside it | diagram | |

## Chapter 2: The setup
| Beat | Narration (spoken form) | On-screen text | Visual intent | Scene hint | Capture cue |
|------|-------------------------|----------------|---------------|------------|-------------|
| 2.1 | The pull took eleven minutes on a wired connection. Ollama reported the model as ready. The server came up on its default port, and nothing in the log looked wrong. I want to be honest about how normal this felt. | pull 11 min | The terminal replays the pull, then the ready line | terminal-replay | cmd1 |
| 2.2 | First request, and the box thought about it. Six seconds of nothing. Then tokens, slowly, at about four a second. That is not a small miss. That is the wrong order of magnitude. | 4 tok/s | The counter crawls while the predicted thirty stays on screen | terminal-replay | cmd2 |
| 2.3 | The temptation here is to blame the model. I have done that before and wasted an afternoon. So I looked at memory first, because memory is the one thing on this box that fails quietly. | check memory first | A memory bar fills past its own edge and keeps going | diagram | |
| 2.4 | Two things were true at once, and that is what made this confusing. The server was healthy by every check I knew. The model answered every prompt correctly. Nothing crashed and nothing threw an error. The only symptom was time, and time is the symptom people ignore longest. | healthy, correct, slow | Three green checks, then a clock that keeps running | comparison-table | |

## Chapter 3: Where it fell over
| Beat | Narration (spoken form) | On-screen text | Visual intent | Scene hint | Capture cue |
|------|-------------------------|----------------|---------------|------------|-------------|
| 3.1 | Free memory said eighty-one gigabytes. Resident memory for the server said a hundred and nine. Those two numbers cannot both be comfortable at once. The box was swapping, quietly, and the swap file sat on slower storage. | 81 free / 109 resident | Two gauges disagree, and the overlap is shaded red | comparison-table | cmd3 |
| 3.2 | The cause was the context window. I had left it at a hundred and twenty-eight thousand tokens, the default from a config I copied. The cache for that context wanted about sixty gigabytes on its own [measured]. | KV cache 60 GB | The cache block grows until it shoves the weights off the bar | diagram | cmd3 |
| 3.3 | So the weights fit and the cache did not. Nothing in the log says that. The server starts, it answers, and it runs like a car stuck in the wrong gear. | weights fit, cache did not | The two blocks separate; only one is inside the memory outline | diagram | |
| 3.4 | Here is the shape of it in one sentence. The weights are a fixed cost you pay once. The cache is a running cost you pay per token of context. I had budgeted for the first and ignored the second. That is the most common way to lose an evening. | fixed cost vs running cost | Two bars, one static and one growing with every token | diagram | |

## Chapter 4: The fix and the number
| Beat | Narration (spoken form) | On-screen text | Visual intent | Scene hint | Capture cue |
|------|-------------------------|----------------|---------------|------------|-------------|
| 4.1 | Step one: drop the context to eight thousand tokens. That is one flag, and on a chat workload it costs you nothing. The cache fell from about sixty gigabytes to just under four. | ctx 8192 | The flag types into the command and the cache block collapses | code-typing | cmd4 |
| 4.2 | Step two: rerun the same prompt and read the log. Twenty-eight tokens a second at a context of eight thousand [measured]. Load time came down to nine seconds. That is inside the range I predicted. | 28 tok/s | The counter climbs to twenty-eight and parks next to the old four | terminal-replay | cmd5 |
| 4.3 | One number is worth holding on to. Twenty-eight tokens a second is faster than most people read. The box was never slow. The configuration was asking it to keep sixty gigabytes of scratch paper open. | 28 tok/s, never slow | The payoff number sits alone on screen for a beat | stat-callout | |
| 4.4 | Two flags mattered and one did not. Dropping the context did all the work. Switching the cache to eight-bit saved another two gigabytes, which changed nothing I could feel. I am naming it anyway. A flag that does not help is worth as much to you as one that does. | ctx: yes, kv8: no | Two flags on screen; one lights up, one greys out | code-typing | cmd6 |

## Chapter 5: What to copy
| Beat | Narration (spoken form) | On-screen text | Visual intent | Scene hint | Capture cue |
|------|-------------------------|----------------|---------------|------------|-------------|
| 5.1 | What I would do differently is check the cache math before the download, not after. Context length times layers times two, in bytes, gets you close enough to know whether an evening will work. | cache math first | The formula writes itself out and resolves to a number | kinetic-text | |
| 5.2 | What you should copy is the flag and the habit. Set the context to what your workload actually uses. Then watch resident memory during the first request, not the log line. Eight thousand tokens covers almost every chat you will actually have. | set ctx, watch RSS | Two lines of advice, one highlighted as you read it | kinetic-text | |
| 5.3 | One more habit is worth copying from this run. Write the number you expect before you start, out loud or in the note. When four tokens a second came back, I did not have to argue with myself. I had already said thirty. That is the cheapest instrument in this workflow. | write the number first | The predicted number returns and sits beside the measured one | stat-callout | |
| 5.4 | Tonight, set your context to eight thousand and rerun the model you already have. If your tokens per second jumps, you were paying for scratch paper that nobody ever read. | ctx 8192 tonight | The command sits alone, copyable, and the wordmark settles under it | end-card | |

## Notes for review
- Numbers rounded to whole tokens per second. The cache figure is measured, not computed.
