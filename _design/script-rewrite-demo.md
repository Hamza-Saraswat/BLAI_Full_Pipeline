# Script rewrite demo: DGX Spark or Mac Studio

One topic, written twice under the new rules, against the same research brief that produced the published version. The published version is the corpus's worst offender: four positional labels, one of which is the three-word sentence "Stage four, then."

Brief: `BLAI_Animator/out/title-dgx-spark-vs-mac-studio/research.json`. Format `smooth-explainer` (numbers capped at three). `has_process: false`, so positional labels are illegal in both drafts.

## What shipped (v1)

Its four transitions, in order:

- "In stage one, the machine reads."
- "In stage two, the machine writes."
- "Stage three is why it flips."
- "Stage four, then."

The first two are real: reading and writing are genuinely sequential. The third is an explanation of the first two, not a stage. The fourth is numbering inertia with no content at all.

## Draft A: `comparison-ladder`

You've narrowed it down to two boxes. The DGX Spark, or a Mac Studio.

Every spec sheet says the Spark wins. Every Mac owner says otherwise. They are both right, because you are not running one job. You are running two.

Paste a long document into a local model and ask for a summary. Before a single word comes back, the machine has to read everything you pasted. Only then does it write the answer, one word at a time. Two halves, one job, and they lean on completely different parts of the box.

EXO Labs ran the same model and the same long document on both machines. At reading, the Spark finished about four times sooner. At writing, the Mac finished about three times sooner. Almost a perfect mirror.

Here is why it flips. Reading your prompt is one big block of math, done all at once, so it is limited by raw compute, and the Spark has roughly four times the Mac's.

Writing is a different animal. For every single word, the machine drags the model's weights out of memory, so what limits it is how wide that memory pipe is. The Mac's is about three times wider.

The Spark has the stronger engine. The Mac has the wider doorway.

So neither one is the fast box. The only question is which half your day is made of. Long documents and short answers, agent runs that re-read their context every turn: that is reading, and that is the Spark. Short questions and long answers, chat that runs all afternoon: that is writing, and that is the Mac.

Look at what you actually paste, not at what the box promises.

## Draft B: `myth-bust` (the winner, after the gate loop)

The DGX Spark is sold on a petaflop of AI performance. The Mac Studio on your desk is not.

So the Spark should write your text faster. It does not, and the gap is not close.

Hand both machines the same model and the same long document, then watch the answer come out.

The Mac gets there first, and not by a little. That is not a bad driver or a tuning problem. It is the wrong number on the box.

Writing text is not a compute problem. To produce one word, the machine pulls the model's weights out of memory. Then it does it again for the next word, and again.

The weights do not fit in any cache, so there is no shortcut. Every word pays the same toll.

What limits you is how wide that memory pipe is, and the Mac's is about three times wider than the Spark's. The petaflops sit there, waiting.

Where the Spark's petaflop does show up is the other half of the job: reading what you pasted.

That is one big block of math, the Spark does it all at once, and it is not close.

So the myth is half true, which is exactly why it survives. The Spark really is the faster machine. It is faster at the half of the job nobody watches.

None of this is on NVIDIA's spec sheet, because a spec sheet has no idea what you paste.

Long documents and short answers, buy the Spark. Short questions and long answers, buy the Mac Studio.

## Judge

| # | Row | A | B | Note |
|---|-----|---|---|------|
| 1 | Hook | 3 | 3 | A names the viewer's decision and a tension; B names a product claim and breaks it in the third sentence |
| 2 | Payoff timing | 2 | 3 | A's first concrete lands around second 8; B's lands at "It does not, and the gap is not close" |
| 3 | Specificity without cramming | 3 | 3 | Two spoken numbers each, and each number does double duty (four times compute and four times reading; three times bandwidth and three times writing) |
| 4 | Voice | 2 | 3 | A has no wry beat; B has one that lands and is not explained: "The petaflops sit there, waiting." B's first draft opened without naming the viewer, which the new second-person advisory caught; "the Mac Studio on your desk" fixed it |
| 5 | Navigation | 3 | 3 | Both carry transitions in content. A's "Here is why it flips" is the published "Stage three is why it flips" with the label removed and nothing lost |
| 6 | Difference | 3 | 2 | Both differ from the published shape; A is further from a comparison the channel has run before |
| 7 | Repeat test | 3 | 3 | "Look at what you actually paste, not at what the box promises" and "buy the compute, buy the bandwidth" |
| | **Total** | **19** | **20** | |

**Winner: B.** Graft considered and declined: A's closing line is the stronger single sentence, but B already ends on its decision rule, and swapping it would mean rewriting the last beat. The rubric says do not graft when the surrounding beats have to move.

**What A would have needed to win:** one wry beat somewhere in the middle, and its first concrete fact moved forward by two sentences. The two-halves reveal is the payoff, and A spends four sentences setting it up.

## What the gates caught in my own draft

The first version of B passed the validator with zero blockers and then failed three eval gates. Every one of them was a real fault, not a false positive:

| Gate | What it said | What was actually wrong |
|------|--------------|--------------------------|
| `positional_labels` | clean, 0 hits | nothing: the label habit never appeared once the prose rules changed |
| second-person advisory | no `you` in the first three sentences | the hook opened on the product, not on the viewer. Fixed to "The Mac Studio on your desk" |
| `scene_specificity` | 7 of 12 scenes carried a specific, needed 10 | five beats named neither machine. The corpus's two best label-free scripts score 0.88 and 0.89 here, so the gate was right and the draft was thin. Naming the boxes in the closing decision rule made it more useful, not less |
| `number_spend` | the viewer hears 4 distinct numbers, cap is 3 | two on-screen beats showed `273 GB/s | 819 GB/s` and `4x` while the narration said "three times wider". Numbers on screen that are never spoken break the house rule, and the gate found them |

Final state: zero blockers, zero advisories, and one soft failure (`entity_spend`, 0.14) which is expected for a two-product myth-bust and is allowed to warn.

Two gate changes came out of this run, both made on evidence and both re-checked against the 38-board regression set:

1. **A scene counts as specific if it carries a glossary term from the brief**, not only a number or a named entity. A beat like "the machine pulls the model's weights out of memory" is the most specific sentence in the script and the gate could not see it.
2. **The number gates count distinct spoken phrases, not brief rows matched.** One spoken "about three times" was satisfying five separate rows in the brief and inflating the count. `spent` still reports coverage of the brief; `heard` is what the cap now uses.

## Notes for the retro

Both drafts spend two numbers where the published version spent six. The cap did that, not the writer. The `myth-bust` shape reached the payoff faster than `comparison-ladder` on a topic that looks like a comparison, which is the argument for writing two shapes rather than picking one on instinct.
