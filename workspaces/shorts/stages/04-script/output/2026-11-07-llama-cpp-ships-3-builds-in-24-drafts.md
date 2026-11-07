# Drafts: 2026-11-07-llama-cpp-ships-3-builds-in-24

Two blind drafts (kimi-k3 via llm_call.py, one packet each, private scratch dirs), judged by a third blind call on the judge rubric.

## Draft A (news-react-so-what, hook: number shock)
- [s01] Three llama.cpp releases in one hour. Yours is older.
- [s02] Your build is weeks old; you cannot name its number. The newest stamp reads eleven fifty-eight.
- [s03] Six releases landed before noon. Nothing pings you; your copy drifts.
- [s04] Each is one merged change: a Vulkan fix, a WebGPU kernel, a server scheduling change. And forty prebuilt downloads, ready to run.
- [s05] Asked if a stable release exists, the maintainer answered: not at the moment. That is the roadmap. Upstream publishes no speed gain.
- [s06] Tonight, download the newest release and re-run llama-bench, the included benchmark. The update is a number, not a vibe.

## Draft B (myth-bust, hook: named contradiction) -- WINNER 20:16
- [s01] There is no stable llama.cpp. There never was. You are waiting anyway; the maintainer: not at the moment.
- [s02] You downloaded a build weeks ago and cannot say which number. Nothing pings you; your copy drifts. Today stamped six releases; three inside one hour, eleven eleven to eleven fifty-eight.
- [s03] Each build is one named change: a Vulkan fix, a WebGPU kernel, a server scheduling fix. Each ships forty prebuilt downloads.
- [s04] Never measured? Then pinning costs nothing you can see. No upstream speed number exists, so yours comes from llama-bench, the tool that counts your tokens per second.
- [s05] Tonight: check, re-pin, re-run llama-bench. Old row, new row: the update is a number, not a vibe.

## Score table
| Row | A | B |
|-----|---|---|
| 1 Hook | 2 | 3 |
| 2 Payoff timing | 2 | 3 |
| 3 Specificity | 1 | 2 |
| 4 Voice | 3 | 3 |
| 5 Navigation | 2 | 3 |
| 6 Difference | 1 | 1 |
| 7 Repeat test | 3 | 2 |
| 8 Teaching | 2 | 3 |
| Total | 16 | 20 |

Winner reason (judge): B lands product plus tension in five words, pays the break immediately, stays inside the brief.

## Grafts
1. From A, sentence: "Nothing pings you; your copy drifts." -> B s02. Reason: adds the silent-staleness mechanism B skips; slots after B's second sentence without rewrites.
2. From A, sentence: "The update is a number, not a vibe." -> B s05 payoff. Reason: punchier repeatable payoff than B's final clause; swaps in without touching structure or numbers.

## What the losing shape would have needed (judge postmortem, with a correction)
Judge: "It needed the sting in five words; 'six before noon' invented a fact. Middle beats stacked with 'and' instead of causing each other." Correction: "six builds before noon" is grounded (brief claim 5: six builds on 07 Nov 2026, timestamps 09:17-11:58); even re-scoring A row 3 at 2, A totals 17 against B's 20. The "sting in five words" and causal-transition critiques stand.
