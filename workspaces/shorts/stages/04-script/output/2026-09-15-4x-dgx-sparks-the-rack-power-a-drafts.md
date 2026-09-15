# Drafts: 2026-09-15-4x-dgx-sparks-the-rack-power-a

Two blind drafts by Kimi K3 writers, judged blind by a third Kimi K3 call per judge-rubric.md.

## Drafts

### Draft A (worked-example)

| Scene | Role | Narration | On-screen |
|-------|------|-----------|------------|
| s01 | hook | Your DGX Spark just hit its ceiling. The newest open models grew past what your box can hold. | Your Spark hit a ceiling |
| s02 | foreshadow | An open model called GLM five point two just landed. Its card lists seven hundred fifty-three billion parameters, the stored dials a model reads to write. No single graphics card you can buy holds them all. | 753B |
| s03 | explain | Your Spark carries one hundred twenty-eight gigabytes of unified memory, one pool the processor and the graphics chip share. That was roomy last year. This model is roomier. | 128 GB, one shared pool |
| s04 | explain | So you cable four Sparks together. Tensor parallelism, the trick that splits one model across boxes, pools their memory into one heap. Four boxes give five hundred twelve gigabytes of pooled memory, and the giant finally fits. | 512 GB |
| s05 | explain | Here is the catch, straight from Petronella's measurements. Inside a box, memory feeds the chip over a wide road. The cable between boxes is about a tenth as wide. Every word pulls some weights through it. | Wide road in, thin road out |
| s06 | explain | Picture four movers with one piano. Together they lift it, but they keep stopping to call out the next step. | Four movers, one piano |
| s07 | explain | A benchmark team called Petronella ran four boxes on GLM five point three Flash, a smaller open model. On plain prose it decoded twenty-six point five tokens per second. A token is a chunk of a word, so that is reading pace. | 26.5 tok/s |
| s08 | explain | The piano picture bends for sparse models like Qwen three point eight Flash Next, a kind that wakes only a few small specialists per word. There, more boxes really do pay. | Sparse models: boxes pay |
| s09 | explain | Alex Ellis's team built this. They cabled four Sparks into a closed ring, with no network switch at all. They also patched the networking library that moves data between boxes, so neighbors relay. | A ring, no switch |
| s10 | explain | So what did four boxes buy? Not speed. The decode strolls at reading pace. They bought a model class your shelf could not hold yesterday. | Not a speed buy |
| s11 | payoff_close | Four Sparks buy memory, not speed. The model that outgrew your one box now fits on four, and it answers at the pace you read. | Memory, not speed |

### Draft B (myth-bust (rewritten from number-first after sameness failure))

| Scene | Role | Narration | On-screen |
|-------|------|-----------|------------|
| s01 | hook | You think a rack buys speed. Measured: twenty-six point five tokens per second from the whole ring. | 4x the speed? then 26.5 tok/s |
| s02 | explain | A team at Petronella wired four DGX Spark boxes into one cluster and ran a single model across all four. The trick is tensor parallelism, splitting one model's layers so each box holds a slice. It works. It just doesn't multiply speed. | one model, four slices |
| s03 | explain | Here is why. Inside a box, memory feeds the G B ten chip on a fast lane. Between boxes, everything crosses one cable, the slow lane, doing its patient best. Every word pulls some weights through it. | fast lane inside, slow lane between |
| s04 | explain | What four boxes multiply is memory. Pool four Sparks and the model sees five hundred twelve gigabytes of memory as one shared pool. NVIDIA's own clustering tools link up to four boxes this way. | 512 GB, one pool |
| s05 | explain | It is called G L M five point two. Seven hundred fifty-three billion parameters, the dials a model learns. No consumer card holds it. Alex Ellis's team bought four desk boxes that can. | GLM-5.2, 753B |
| s06 | explain | Picture moving a piano. One strong mover is fast on his feet, but he cannot lift it alone. Four ordinary movers lift it together, pausing at every doorway to coordinate. Slower each step, and the piano still moves. | four movers, one piano |
| s07 | foreshadow | The picture bends for sparse models like Qwen three point eight Flash Next, built from many small experts; splitting can quicken each stream. Everywhere else, memory grows with boxes and speed stays flat. The software is young: it died five different ways before its first word. | memory grows, speed stays flat |
| s08 | payoff_close | Four Sparks buy memory, not speed. You get the model no single card can hold, and it answers at the pace you read. | memory, not speed |

## Judge score table

| # | Row | A | B | Note |
|---|-----|---|---|------|
| 1 | Hook | 3 | 1 | A names DGX Spark plus a felt tension ('hit its ceiling') in five words; B's 'You think a rack buys speed' names no product or number, topic only. |
| 2 | Payoff timing | 1 | 3 | B's measured 26.5 tok/s break lands ~3.8s and pays the hook (scored from the break per fairness rule); A's first concrete number (753B) lands ~9s. |
| 3 | Specificity | 3 | 2 | A spends 753B, 128, 512, 'about a tenth as wide', 26.5 with none decorative; B drops the physics ratio entirely and its lane beat ('doing its patient best') carries no specific. |
| 4 | Voice | 3 | 3 | Both clean second-person with one wry beat that lands unexplained: A's 'This model is roomier', B's 'slow lane, doing its patient best'. |
| 5 | Navigation | 2 | 2 | Both have content-carrying chains but each keeps one deletable label ('Here is the catch' / 'Here is why'), so both sit at 2. |
| 6 | Difference | 3 | 0 | A's situation-hook worked-example differs from both recent shapes with a loop-anchor landing; B is number-first with a shock-number open, same shape and rhythm as the 09-12 ledger  |
| 7 | Repeat test | 2 | 2 | Both end on 'answers at the pace you read', so the repeatable line 'Four Sparks buy memory, not speed' is not literally the last thing heard in either. |
| 8 | Teaching | 2 | 3 | B states the causal chain ('Every word pulls some weights through it') so a viewer could predict never-split a model that fits on one box; A shows road width and pausing movers but |

**Totals: A 19, B 16. Winner: A.**

## Grafts

- From B: "Every word pulls some weights through it." into s05. Reason: A's catch scene names the road-width gap but never says why a thin cable taxes every token; this single sentence supplies the causal mechanism, adds no number, keeps person and structure, and slots after 'about a tenth as wide' with no surrounding rewrites.

## What the losing shape would have needed

B needed an opening rhythm that was not the shock-number reveal the channel aired three days earlier, since that sameness zeroed its difference score despite a strong payoff. It also needed a hook that names the Spark and the felt tension up front, because stating the myth abstractly ('a rack buys speed') cost it the row 1 points A won back.

## Process notes

- B v1 (number-first, price hook) failed the sameness gate two ways: structure repeated 2026-09-12's number-first, and the price hook classified number-shock (also 2026-09-12's pattern; the classifier's price rule fires on the currency token only when no earlier rule matches -- a "four" in the sentence fires number-shock first). B was rewritten as myth-bust under the same writer packet rules, with a wrong-diagnosis hook stripped of number words.
- A's gate fixes after the first write: hashtags trimmed to 3 with # forms, the 512 GB line gained its referent, the long benchmark scene split in two, NCCL replaced with "the networking library", the MoE scene named Qwen 3.8-Flash Next for specificity, and the judge's graft split the catch scene into physics + piano.
