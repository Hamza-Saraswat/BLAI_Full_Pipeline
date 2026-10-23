# Drafts: 2026-10-23-8-dgx-sparks-1-tb-frontier-mod

Both drafts written blind by separate kimi-k3 calls (one packet each), both gated to zero
blockers before judging. Judge was a third blind kimi-k3 call; rubric per judge-rubric.md.

## Draft A -- news-react-so-what (assigned hook: number shock)

| Scene | Narration |
|-------|-----------|
| s01 hook | One terabyte of memory just shrank to your desk. |
| s02 | NVIDIA now supports linking eight DGX Sparks, desk-side AI computers, into one shared pool. Your gaming PC or Mac watched models this size from a browser tab. |
| s03 | That pool runs G L M five point three, seven hundred fifty-three billion parameters. The whole model is one four hundred seventy gigabyte file on a desk. |
| s04 | The catch: the cable between boxes is eleven times slower than the memory inside each one. You buy room, not speed. |
| s05 close | And yet it types at thirty-one tokens per second in NVIDIA's own test, no cloud account. The frontier moved from their building to your desk. |

## Draft B -- number-first (assigned hook: named contradiction; wrote number-first instead)

| Scene | Narration (final, after gate fixes and graft) |
|-------|-----------|
| s01 hook | Eight DGX Sparks pool one terabyte of memory. They are desk boxes. A terabyte meant a building you rent. |
| s02 | GLM five point three runs across all eight. Seven hundred fifty-three billion parameters. Squeezed to four bits a weight: about four hundred seventy gigabytes of model. |
| s03 | NVIDIA measured thirty-one tokens per second for one user. That is how fast the model writes: about reading speed. |
| s04 | The catch is the cable. A Spark's own memory outruns its ConnectX seven link, the cable between boxes, eleven times over. Eight boxes buy room, not speed. |
| s05 close | So the biggest models stopped being rentals. The frontier moved from their building to your desk. (graft from A) |

Gate fix rounds: B failed scene_specificity round 1 (3/5); fixed by naming the cable (ConnectX seven) in s04 and the viewer in s05. B advisories cleared round 2-3: gigabytes referent, second person moved into s01, tail sentence cut, hook scene trimmed under 7 s, s02 brief given a mid-scene visual change. A passed gates unmodified.

## Judge scores

| Row | A | B | Why |
|-----|---|---|-----|
| 1 Hook | 3 | 3 | Both name numbers with fast felt tension; A's shrink paradox on screen at second 0, B names the product and pooling tension by word 4 |
| 2 Payoff timing | 3 | 3 | Both pay the hook's promise with a concrete inside four seconds |
| 3 Specificity | 3 | 3 | A spends six numbers, one per sentence, all earning; B spends more but the extras are mechanism and benchmark honesty; zero drift on either side |
| 4 Voice | 3 | 3 | Both clean, correct person, one unexplained wry beat that lands |
| 5 Navigation | 3 | 2 | A's transitions each name what changed and the chain cannot reorder; B's "NVIDIA measured" is a flat topic cut and s02/s03 could swap |
| 6 Difference | 1 | 2 | A re-ships the news-react-so-what skeleton from three days ago at the same ~37 s; B's number-first shape, staccato opening and reframe landing are new to the run |
| 7 Repeat test | 3 | 2 | A's payoff line is repeatable and last; B's most repeatable line was penultimate (fixed by the graft) |
| 8 Teaching | 2 | 3 | A shows the 11x mechanism once then states its conclusion; B adds the four-bit squeeze, a sizing tool a viewer can transfer to models never mentioned |
| Total | 21 | 21 | Tie: B wins on row 6 (difference), per the rubric's tie-break |

## Graft

A's closer "The frontier moved from their building to your desk." replaces B's final sentence
"A frontier checkpoint now runs on your desk." Same beat, same person, no numbers; makes the
repeatable payoff line the last thing heard. A's browser-tab line was not grafted: no beat in B
absorbs it without rewriting, and B is already over its 32 s target.

## What the losing shape would have needed

A re-used the news-react-so-what skeleton shipped 2026-10-20 at the same ~37 s duration as two
other recent videos; it needed a different shape, length or opening rhythm to clear row 6. It
also stated 470 GB as a bare fact where spending the four-bit squeeze mechanism (as B did) gives
viewers a reusable sizing tool instead of one number.
