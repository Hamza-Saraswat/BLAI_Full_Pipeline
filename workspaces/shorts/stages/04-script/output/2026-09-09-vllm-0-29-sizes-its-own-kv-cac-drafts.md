---
slug: 2026-09-09-vllm-0-29-sizes-its-own-kv-cac
stage: 04-script
winner: A
totals: "A 21, B 20"
---

# Drafts: vLLM 0.29 sizes its own KV cache

Two blind writers (kimi-k3 via tools/llm_call.py, separate scratch dirs, one packet each).
Draft A: worked-example, hook pattern named-contradiction. Draft B: number-first, hook
pattern number-shock. Post-write gate fixes inside each draft (named below) were the only
non-writer edits: each draft spent one key number only, so number_spend (classic, min 2)
needed a second; A s05 and B s04 each gained one clause spending "594 commits" verbatim.
B s01 was trimmed 26 -> 15 words (hook scene 7 s advisory) with the moved fact landing in
B s02; A s06 and B s01 sentence splits and the A s04/s06 entity mentions fixed remaining
advisories. Both boards pass validate_storyboard (0 blockers, 0 advisories) and all nine
eval gates.

## Judge score table (row 0-3 each; max 24)

| row | A | B | reason |
|-----|---|---|--------|
| 1 Hook | 3 | 2 | A names product plus felt tension inside five words; B's number only becomes tension later |
| 2 Payoff timing | 2 | 2 | both land the 0.92 default claim between seconds 5 and 8 |
| 3 Specificity | 3 | 3 | at most three spoken numbers, no unverified GiB figures, no quoted log line |
| 4 Voice | 3 | 3 | clean second person, one dry beat each ("less a measurement than a shrug" / "Very thorough.") |
| 5 Navigation | 2 | 3 | B fuses pivot and fix; A's release sentence drops a number before naming the change |
| 6 Difference | 2 | 1 | A's shape/opening/landing are new; B reruns the Sept 6 number-first shape at the most recent ship's exact 37 s |
| 7 Repeat test | 3 | 3 | both end on a repeatable payoff aphorism |
| 8 Teaching | 3 | 3 | viewer could predict the unmentioned case (bigger graphs, smaller cache) |
| TOTAL | 21 | 20 | |

Winner: A, by 1. No grafts (loser's hook not 2+ points higher on row 1; no sentence moved).

What B would have needed: a shape the ledger has not shipped (number-first at exactly 37 s
repeats the Sept 6 script), and hook tension landing inside the first five words instead
of at "the share you lowered to stop crashes".

## Draft A (winner, worked-example)

- s01 hook: "vLLM stopped guessing your GPU memory budget. Crash at boot, lower the flag, retry." (on screen: vLLM stopped guessing your memory)
- s02 explain: "One server claims ninety-two percent of GPU memory by default. Weights eat first, then CUDA graphs, pre-recorded replays that trade memory for speed." (0.92 of GPU memory by default)
- s03 explain: "The KV cache, memory of what the model already read, gets leftovers." (weights -> graphs -> KV cache: leftovers)
- s04 explain: "vLLM's graph check returned zero, less a measurement than a shrug. The cache claimed the whole budget. Startup ran out of memory." (graph check = 0 -> cache takes all -> OOM)
- s05 explain: "This morning's release is five hundred ninety-four commits. The new engine, default for every model, measures graphs first, then sizes the cache to fit." (594 commits | engine now default)
- s06 payoff_close: "Same vLLM command, same budget cap. The log prints the cache it picked, and the guessing was the bug." (same command -> logged cache size)

## Draft B (number-first)

- s01 hook: "Ninety-two percent of your GPU. vLLM finally counts what it takes. The share you lowered to stop crashes." (92% of your GPU)
- s02 explain: "One server claims it by default. Weights load first. Then CUDA graphs, recorded replays that cost memory. The KV cache, memory for tokens already read, takes the leftovers." (weights - CUDA graphs - KV cache)
- s03 explain: "The old probe reported nothing. Very thorough. The cache ate the whole budget, and boot ran out of memory." ($ vllm serve <model> / CUDA out of memory)
- s04 explain: "In zero point two nine, five hundred ninety-four commits, the runner measures graphs, then sizes the cache around them. The budget cap stays yours." (v0.29 - 594 commits - measure, then size)
- s05 payoff_close: "The log prints the cache size to pin for next boot. Same serve command, and it boots: leftovers, not the budget." (same command - KV cache: leftovers)

Full boards with visual briefs: `.local-builds/2026-09-09-vllm-0-29-sizes-its-own-kv-cac/draft-A/storyboard.json` and `draft-B/storyboard.json`; blind packets in the same tree. Judge packet: `judge/` (system, user, verdict).
