# Episode Structures

A structure is the shape of the episode, not its length (length lives in the outline stage's `outline-format.md` and in the long-form row of `shared/platform-specs.md`). The outline stage ranks these by fit, writes the top two as competing outlines, and judges them; this stage writes the winner and carries its name in the script frontmatter. Three shapes today.

| Structure | Shape | Payoff sits | A muted viewer follows | Series it fits |
|-----------|-------|-------------|------------------------|----------------|
| `concept-deep-dive` | One idea from zero, one worked example carried the whole way, two edge cases | end of chapter 3 | one example transforming | `local-ai-for-dummies`, `inference-engineering-at-home` |
| `build-along` | I set out to do a thing on the Spark; here is what happened, including what broke | chapter 4, the measurement | terminal replays and one number changing | `my-dgx-spark-projects`, `dgx-spark-specific` |
| `buyers-guide` | Which box or which model you should actually run | chapter 5, the decision rule | a comparison table filling in | `benchmarks`, `beyond-llms` |

## concept-deep-dive

| Chapter | Carries |
|---------|---------|
| 1 | The viewer's situation, the promise, and the surprising number by 0:20 |
| 2 | The naive model everyone holds, and the moment it breaks |
| 3 | The real mechanism, built on the single example |
| 4 | Two edge cases where it bites |
| 5 | What to do tonight |

- Payoff: the mechanism lands at the end of chapter 3. Chapters 4 and 5 are consequence, not new argument.
- One example enters in chapter 1 and is still on screen in chapter 5. It is never swapped for a second example.
- Trap: teaching the taxonomy instead of the mechanism (four named quantization formats instead of what quantization does to one tensor), and listing every edge case instead of the two that bite.

## build-along

| Chapter | Carries |
|---------|---------|
| 1 | The goal, why it should work, what I expected |
| 2 | The setup as it really went |
| 3 | The failure and the diagnosis |
| 4 | The fix and the measurement |
| 5 | What I would do differently, and what you should copy |

- Payoff: the measurement in chapter 4. Chapter 5 spends it, and never re-argues it.
- Person: first person singular for what I ran, second person for what you should copy.
- Trap: narrating every command (the terminal is doing that work already), and hiding the failure. The failure is the content. An episode where nothing broke is a `concept-deep-dive` wearing a terminal.

## buyers-guide

| Chapter | Carries |
|---------|---------|
| 1 | The decision, and who it is for |
| 2 | The one axis that really decides it |
| 3 | Contender A measured on that axis |
| 4 | Contender B measured on the same axis |
| 5 | The decision rule, plus who should ignore it |

- Payoff: the decision rule in chapter 5, in one sentence a viewer can repeat at a keyboard.
- Chapters 3 and 4 use the same axis, the same units and the same table; only the numbers change.
- Trap: reading spec sheets (a spec sheet is not a measurement), and refusing to give an answer. "It depends" is a chapter 5 failure. Name who should ignore the rule instead.

## Choosing

Match the brief and the series, not the mood. A concept with one carriable example suggests `concept-deep-dive`; a research brief with an experiment plan and a real failure suggests `build-along`; two named things and a shared axis suggest `buyers-guide`. The series row in `brand-vault/content-pillars.md` is the tiebreak. Both structures the outline stage writes must differ from the last two entries in the episode ledger; when two shapes fit equally, take the one the ledger has not seen longest.

`benchmark-showdown` (many contenders, one harness, one leaderboard) and `myth-bust-long` (the belief, the measurement that breaks it, when it is still right) are the next two to add.

## Transitions

Chapters are navigated by content, never by positional labels. The legal moves, one per chapter break:

| Move | Example |
|------|---------|
| Name what changes | "Now the weights are four-bit." |
| Answer the question the last chapter raised | "So which one actually fits? Neither, at full precision." |
| Contradict the expectation | "That reads like a win. The load time says otherwise." |
| Jump to the consequence | "That number is what you pay every time the context grows." |
| Zoom out to the stakes | "That gap is the difference between a box you use and a box you tolerate." |

Hard rule: positional labels (stage, step, part or phase, plus a number) are allowed only in `build-along`, only for steps the viewer performs themselves, at most three in an episode, and each label must name the action ("Step two: quantize it", never "Step two."). Everywhere else they are a defect, and `validate_longform.py` flags them. Chapter cards carry the label on screen; the narration never reads a chapter title aloud.
