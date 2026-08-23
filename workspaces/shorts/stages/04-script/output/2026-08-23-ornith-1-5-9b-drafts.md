# Ornith 1.5 9B: draft judgment

Slug: `2026-08-23-ornith-1-5-9b`
Judged: 2026-08-23
Rubric: `stages/04-script/references/judge-rubric.md`
Brief: `stages/03-research/output/2026-08-23-ornith-1-5-9b-brief.md`

Both drafts pass the validator with zero blockers and clear every hard eval gate. The `entity_spend` and `top2` warnings fire on both drafts and are a known extractor defect; they were ignored and are not evidence about the writing.

---

## Draft A: `number-first`

Hook text: **5.63 GB fixes real bugs**
Six scenes, 36.5 s of scene budget against a 36 s target. Ten sentences, 101 words, longest 15, average 10.1.

> Just under six gigabytes on disk, and that's a whole coding model. You've got eight gigabytes on your card, and a standing rule that nothing serious fits. This one does. It's Ornith's nine-billion-parameter model, squeezed into that single file. On S W E bench Verified, it scores seventy point six. That test hands a model real bugs from real open-source projects. Ornith ran those numbers itself. Averaged over five runs, with the git history stripped and the network switched off. Nobody outside Ornith has reproduced that yet. So pull the file tonight and hand it a bug that already beat you.

## Draft B: `myth-bust`

Hook text: **6 GB file. It fits your card.**
Five scenes, 35.3 s of scene budget against a 36 s target. Twelve sentences, 98 words, longest 13, average 8.2.

> You have been told a frontier score needs frontier hardware. This one is under six gigabytes on disk. That's Ornith's four-bit build. Each stored number keeps fewer bits, so the file shrinks. It fits the mid-range gaming card you already own. Ornith reports seventy point six on the verified benchmark. Real bugs in real repositories. Ornith ran those numbers itself, averaged over five runs. No git history, no network. Stricter than most labs, and still their own. The myth survives on knowledge, not on hardware. A nine-billion-parameter model still will not know what a much bigger one knows.

---

## Scores

| # | Row | A | B |
|---|-----|:-:|:-:|
| 1 | Hook | **3** | **2** |
| 2 | Payoff timing | **3** | **2** |
| 3 | Specificity without cramming | **3** | **2** |
| 4 | Voice | **3** | **3** |
| 5 | Navigation | **3** | **2** |
| 6 | Difference | **3** | **1** |
| 7 | The repeat test | **3** | **2** |
| | **Total** | **21** | **14** |

### Row 1, Hook

**A = 3.** The hook line holds a number and a collision in exactly five words: 5.63 GB against "fixes real bugs". Spoken, the number lands at word two, and the tension the viewer actually feels is complete inside the first sentence, six gigabytes set against "a whole coding model". Caveat recorded: on a literal five-spoken-words reading the opener is "Just under six gigabytes on", which carries the number and not yet the tension. The score rests on the hook line, which is what is on screen at frame one.

**B = 2.** Names a number, in sentence two. The first five words are "You have been told a", which carries the tension but nothing concrete, and "frontier score needs frontier hardware" is the default opening sentence of this entire genre. Level 3 asks for both halves up front and B has one.

### Row 2, Payoff timing

**A = 3.** The first concrete thing is the first thing spoken, and it is the thing the hook promised: the hook says 5.63 GB, the narration opens on six gigabytes, the on-screen number is legible before anything moves.

**B = 2.** Lands by second 8, comfortably. Not by second 4: sentence one is an abstraction that must be spoken in full before "under six gigabytes" arrives at roughly second five. This is structural, not sloppy. A myth-bust cannot state the concrete before it states the myth.

### Row 3, Specificity without cramming

**A = 3.** Five spoken numbers, at the top of the classic band the brief allows, and each is spent once and left alone: six gigabytes (the surprise), eight gigabytes (the wall, and it is the viewer's own number, already in their head), nine billion (what it is), seventy point six (the reason to care), five runs (the rigour inside the catch). No sentence makes the viewer hold two new numbers. Nothing is decoration. The forbidden material stays unspent: no GPQA, no context window, no Terminal-Bench, no download count.

**B = 2.** Also five numbers, also cleanly separated, and B's four-bit beat is the best teaching in either draft: "Each stored number keeps fewer bits, so the file shrinks" is Hard Constraint 3 executed exactly. But two beats give their specific away. "Ornith reports seventy point six on the verified benchmark" refuses to name SWE-bench Verified, and "the verified benchmark" is a fog to the ear. The payoff lands on "a much bigger one", unnamed and unsized. Against that, B spends nine billion harder than A does: A spends it on identity, B spends it on the argument.

### Row 4, Voice

**A = 3.** No hard-constraint break. Second person throughout, no false "we" (correct, since the brief records no local run). Numbers as words, digits on screen only, "S W E bench" written the way it is said. Wry beat: "a standing rule that nothing serious fits", which lands on the situation, is not explained, and sits outside both the hook sentence and the payoff sentence. The rhythm is the most spoken of the two: 12, 15, then a three-word snap, then back up.

**B = 3.** No hard-constraint break either. Second person, no false "we", clean number handling. Its wry beat is the sharper of the two and the more textbook: "Stricter than most labs, and still their own" is one short sentence undercutting the one before it, exactly the form the voice rules prescribe. Held at 3 rather than dropped, because the row rewards a wry beat that lands, and B's does. The register is stiffer, though: zero contractions where A has three, "still will not know" where the voice rules invite "won't", and twelve full stops in thirty-five seconds reads clipped.

### Row 5, Navigation

**A = 3.** Every joint names what changed and most are anaphorically locked, so the beats cannot be reordered. "This one does" is only a sentence if it follows "nothing serious fits". "Those numbers" can only follow the score. "That" in "reproduced that yet" can only follow the five runs. The final "So" earns itself: nobody has verified this, so go be the verification.

**B = 2.** Transitions carry content, and "That's Ornith's four-bit build" is a clean anaphoric hand-off. Two joints do not. Size to score ("It fits the mid-range gaming card you already own" into "Ornith reports seventy point six") is a cold topic cut with nothing bridging it, and the score beat could move without breaking a reference. Catch to payoff is worse: "still their own" is about trust, "The myth survives on knowledge" is about capability, and the script jumps between two unrelated caveats without naming the change.

### Row 6, Difference

The ledger is empty, so this row could not be scored against history. **Both drafts were scored instead on how far each sits from the obvious treatment of this topic**, and that substitution is recorded here so the weekly retro does not read these numbers as repetition scores.

**A = 3.** Different shape, different opening rhythm, different landing. Opening on a bare quantity before the viewer knows what it measures, resolving it a beat later against their own card, then a three-word contradiction, is not the reach-for-it treatment. The close is not "go download it"; it is an instruction that names the viewer's own defeat.

**B = 1.** Myth-bust is the obvious treatment of exactly this topic, and "You have been told a frontier score needs frontier hardware" is the sentence this genre opens with by default. What keeps it off 0 is the landing, which is genuinely against the grain: closing on the limitation rather than the win is a move most Shorts would not make. One departing beat is not a different shape.

### Row 7, The repeat test

**A = 3.** "Hand it a bug that already beat you" is the line from this pair someone says out loud, it names a feeling every viewer in this audience has had, and it is the last thing they hear. Nothing follows it.

**B = 2.** There is one line a viewer could repeat, "Stricter than most labs, and still their own", but it sits at beat four. The payoff is a hedge, and the last thing heard is what the model cannot do.

---

## Winner

**Draft A, `number-first`, 21 to 14.** No tie, so row 6 was not needed as the tiebreak.

## Grafts

**None.** Both grafting rules were tested and both fail their own guard rails.

**Hook graft** requires the loser's hook to score at least two points higher on row 1. B scored 2 against A's 3. Not eligible.

**Sentence graft**, at most two sentences where a line in the loser says something the winner says worse. One candidate qualified on merit and was rejected on the rules:

> B s2: "That's Ornith's four-bit build. Each stored number keeps fewer bits, so the file shrinks."

A says this worse. A's only account of why the model is small is "squeezed into that single file", which is a gesture where B has a mechanism, and B's version is drawn almost verbatim from the brief's glossary. It was still not grafted, for three reasons, any one of which is disqualifying:

1. **It breaks the number budget.** A already spends five spoken numbers, the top of the band the brief allows for classic format. "Four-bit" is a sixth.
2. **It breaks Hard Constraint 5.** The graft's only landing site is A's s3, which already carries "nine-billion-parameter". Four-bit and nine billion in adjacent sentences makes the viewer hold two new numbers.
3. **It requires rewriting the surrounding beat.** To fit two sentences into s3 you must displace "squeezed into that single file", and s3's visual brief is built on that file dropping into the card slot, which s6 then calls back. The rubric says: if grafting would require rewriting the surrounding beats, do not graft.

Two further candidates were considered and rejected. B's "Stricter than most labs, and still their own" is not something A says worse; A covers the same ground with "Nobody outside Ornith has reproduced that yet", which is the more checkable claim, and importing a comparative A never sets up would soften the catch exactly where A wants it sharp. B's closing sentence is content A omits rather than content A says worse, and anything placed after A's payoff breaks Hard Constraint 7.

**Because no graft was applied, no surrounding beats moved and Draft A ships as written.**

## Brief fidelity

Nothing was invented in either draft. Every spoken claim traces to the brief: the 5.63 GB four-bit build (claim 2), nine billion dense parameters (claim 1), seventy point six on SWE-bench Verified (claim 3), the five averaged runs with git history stripped and network disabled (claim 6), what SWE-bench Verified measures (glossary), what a four-bit build does (glossary), and B's closing limitation (the analogy-breaks note). Both drafts leave the forbidden material unspent per the brief's closing note: no GPQA Diamond, no context window, no Terminal-Bench figure, no download count.

**The honest catch survived in both.** A gives it two full beats, s5 and the first sentence of s6, and it is the second-to-last thing the viewer hears. B gives it s4 and adds a second, separate caveat in the payoff.

One line to watch in the shipping draft: A's "Nobody outside Ornith has reproduced that yet" is a shade stronger than the brief's "No independent reproduction was found for the 9B." A's own description field states it correctly. The narration compresses an absence of evidence into an assertion. It is a small overstatement, it is not a gate failure, and it is recorded here rather than corrected, because the judge does not rewrite.

## What the losing shape needed

Myth-bust would have had to state its myth in four words or fewer and get five point six three gigabytes inside the first sentence, so that rows 1 and 2 stopped charging it points its writing had not actually lost. And it would have had to fuse its two caveats, the self-reported numbers and the knowledge ceiling, into one closing line, so that the last thing the viewer heard was the repeatable one instead of a hedge that arrives from a beat it does not connect to.

## Note for the retro

Four of B's seven-point deficit come from rows 1, 2 and 6, and all three of those rows are structurally hostile to myth-bust on this topic: a myth-bust cannot put the concrete in the first five words, cannot land it by second four, and is the obvious shape here by definition. On craft rows alone, 3, 4, 5 and 7, A leads 12 to 9. If a pattern of myth-bust losses shows up in this ledger, check whether the shape is losing or whether rows 1, 2 and 6 are pricing it.
