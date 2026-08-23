# Judge Rubric

The judge reads two drafts written from two different structures, plus the voice rules and the last five entries of `output/script-ledger.json`. It has not seen either draft being written, and it does not rewrite them: it scores, picks, and grafts.

Score every row 0 to 3 for each draft. Maximum 21. The higher total wins. On a tie, the winner is the draft that scores higher on row 6 (difference), because two similar videos are worse than one imperfect one.

| # | Row | 0 | 1 | 2 | 3 |
|---|-----|---|---|---|---|
| 1 | **Hook** | generic enough to open any video on this topic | names the topic but nothing specific | names a product or a number | names a product or a number AND a tension the viewer feels in the first five words |
| 2 | **Payoff timing** | the promise is still unpaid at second 10 | first concrete thing lands after second 8 | lands by second 8 | lands by second 4, and it is the thing the hook promised |
| 3 | **Specificity without cramming** | vague throughout, or a wall of numbers nobody can hold | one specific carries the whole script | most beats carry a specific, at most one new number per sentence | every beat earns its specific, numbers are spent where they land hardest, none are decoration |
| 4 | **Voice** | breaks a hard constraint | no breaks, but reads like a manual | clean and in the right person | clean, in the right person, and one wry beat that lands and is not explained |
| 5 | **Navigation** | positional labels on things that are not steps | labels used legally but mechanically | transitions carry content | every transition names what changed, and the script could not be reordered without breaking |
| 6 | **Difference** | same structure or hook pattern as either of the last two scripts | same closing move or same duration as the recent run | recognisably a different shape | different shape, different opening rhythm, different landing |
| 7 | **The repeat test** | nothing here a viewer would say out loud | the fact is repeatable, the phrasing is not | one line a viewer could repeat to a friend | the payoff line is the repeatable one, and it is the last thing they hear |

## Grafting

After picking, the judge may take from the loser:
- the hook, if the loser's hook scores at least two points higher on row 1;
- at most two sentences, when a line in the loser says something the winner says worse.

Nothing else moves. A graft must not break the winner's structure, its person, or its number budget, and every graft is named in the report with the reason. If grafting would require rewriting the surrounding beats, do not graft.

## Report

Write `output/[slug]-drafts.md`: both drafts in full, the score table for each row and each draft, the winner, every graft with its justification, and two sentences on what the losing shape would have needed to win. This file is the record the weekly retro reads when a pattern of losses shows up in one structure.

## What the judge does not do

- It does not rewrite prose it merely dislikes. Taste changes go in the voice rules, not into one script.
- It does not overrule a gate. If both drafts fail a hard gate, both go back; the judge picks only between candidates that pass.
- It does not reward length, density or cleverness on their own. A shorter draft that lands wins.
