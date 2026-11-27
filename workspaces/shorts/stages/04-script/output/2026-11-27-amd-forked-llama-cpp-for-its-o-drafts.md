---
slug: 2026-11-27-amd-forked-llama-cpp-for-its-o
stage: 04-script
generated_at: 2026-11-27T14:05:00Z
---

# Drafts: 2026-11-27-amd-forked-llama-cpp-for-its-o

Both drafts passed the machine gates before judging (validator zero blockers, eval gate1_ready,
number_spend 2, sameness clean). Judge: kimi-k3, rubric-only packet, blind to drafting.

## Draft A (myth-bust) -- WINNER, 19/24

Hook: Your feed's AMD fork isn't from AMD.

Narration: Your feed's AMD fork isn't from AMD. llama.cpp is the free program that runs AI models locally. Everyone's sharing it as AMD's own fork, an in-house copy. The Hacker News thread pulled three hundred sixty seven points. Real upvotes, wrong vendor. The speedup is llama-cpp-rdna-boosts, one maintainer's patches on stock code. AMD's own fork is retired, pointing to the original. The original runs on Radeon; AMD posts ready-made Windows downloads. A single machine backs the speedup. One user measured thirty-five tokens a second, how fast answers appear, on his R-nine-seven-zero-zero card. Patched, he reports fifty-five tokens a second. Your mileage may vary. Your feed's Radeon fix came from a stranger, not AMD.

Scenes: s01 hook (centered-stack); s02 foreshadow (grid); s03 explain (diagram-flow); s04 explain (timeline); s05 explain (giant-number); s06 explain (split-compare); s07 payoff_close (centered-stack)

## Draft B (worked-example) -- 10/24

Hook: You speed up your Radeon tonight.

Narration: You speed up your Radeon tonight. Then you check who built it. Your Radeon already runs llama.cpp, the free local engine. Then an AMD fork, a copy you change yourself, tops the Hacker News thread. Three hundred sixty seven points. AMD's own fork is retired, pointing to the original. The speedup is llama-cpp-rdna-boosts, one maintainer's patches on stock code. Step one: clone the llama.cpp repository. Step two: pin the commit and apply the patches. Step three: build it for your Radeon. Nineteen patches from rdna-boosts now live in your engine. One author's Radeon made thirty-five tokens a second, how fast answers appear. Patched, it hit fifty-five tokens a second. Yours may differ. AMD's fix remains a proposal; your speedup came from one outsider's patches.

Scenes: s01 hook (centered-stack); s02 explain (diagram-flow); s03 foreshadow (split-compare); s04 explain (timeline); s05 explain (giant-number); s06 explain (split-compare); s07 payoff_close (centered-stack)

## Judge score table

| # | Row | Draft A | Draft B |
|---|-----|---------|---------|
| 1 | Hook | 3 | 2 |
| 2 | Payoff timing | 2 | 2 |
| 3 | Specificity without cramming | 3 | 1 |
| 4 | Voice | 0 | 0 |
| 5 | Navigation | 3 | 1 |
| 6 | Difference | 2 | 1 |
| 7 | The repeat test | 3 | 2 |
| 8 | Teaching | 3 | 1 |
| | **Total** | **19/24** | **10/24** |

Judge reasons (verbatim summary): A names the AMD fork and breaks it in the first five words; A
spends four numbers with unit and referent while B drifted the brief's hedges (the measurer is
one R9700 owner, not the patch author; the patch set is not AMD's proposal); A's transitions
name what changed while B's legal step-labels survive deletion; B's shape re-ran recent ledger
entries. Row 4 scored 0/0: A lacked the tokens-a-second definition (fixed post-judge), B left
"commit" unglossed and asserted unproven authorship.

## Grafts

- "The speedup is llama-cpp-rdna-boosts, one maintainer's patches on stock code." moved from
  B to A, replacing "What trended is one maintainer's patch set: nineteen changes on a pinned
  copy." Reason: the winner never named the one searchable artifact in the story; one-for-one
  swap keeps structure, person and number budget intact (the nineteen count survives on screen
  in s03).

## What the losing shape would have needed

The worked-example had to keep the brief's hedges intact (the measurer is one R9700 owner, not
the patch author; nothing here is AMD's proposal) and its three steps had to be a build the
viewer could actually finish tonight, anchored on the named patch set and a real target rather
than clone-pin-build gestures. Failing that, the shape should have worked the one verified
example, the owner's single-machine thirty-five-to-fifty-five run, and ended on the outsider
reveal instead of muddling it.
