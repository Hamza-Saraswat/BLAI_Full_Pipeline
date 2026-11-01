# Drafts: 2026-11-01-deepseek-launches-a-claude-cod

Two blind drafts, kimi-k3 writers, one packet each; judged by a third blind kimi-k3 call on
the judge rubric. Both passed all nine eval gates and the storyboard validator before
judging.

## Draft A (myth-bust, hook pattern wrong-diagnosis) -- WINNER

promise: After 35 seconds you can decide whether to clone DeepSeek's new agent repo and point
it at your own server, or skip it.

| Scene | Role | Narration | On-screen text | Est s |
|-------|------|-----------|----------------|-------|
| s01 | hook | You think DeepSeek launched an app. It's a repo, and it's yours. | You think it's an app \| It's a repo | 4.5 |
| s02 | explain | Bloomberg's own sentence calls it the new open-source offering. The thing itself is dsh-superagent, an MIT repo you run on your gaming PC. | Bloomberg: the new open-source offering | 8.3 |
| s03 | explain | It's a profile of DeepSeek Harness, the scaffolding that lets a model call tools. No brain included: you pick the model provider, even your own self-hosted server. | Harness profile \| no brain included | 9.3 |
| s04 | explain | A Router talks to people; Workers each take one Ticket in its own directory. DeepSeek's reason: you can follow only three to five sessions. | Router -> Workers \| 3-5 sessions | 8.3 |
| s05 | explain | DeepSeek's fifteen point seven minute figure is a synthetic simulation, not a benchmark. | 15.7 min \| synthetic simulation | 4.5 |
| s06 | payoff_close | The repo fences itself: research prototype, not a product, with danger-full-access to your user account. | research prototype \| full account access | 5.2 |

## Draft B (contrarian-take, hook pattern number-shock)

promise: You'll see why DeepSeek's headline agent is an MIT repo you run yourself, why its
speed numbers are synthetic, and what it's actually worth.

| Scene | Role | Narration | On-screen text | Est s |
|-------|------|-----------|----------------|-------|
| s01 | hook | DeepSeek's Claude Code rival runs on the box you already own. | Runs on the box you already own | 4.1 |
| s02 | explain | Headlines call it a hosted Claude Code killer. The repo's read-me file says research prototype, not an official DeepSeek product. | headline: killer \| docs: research prototype | 8.3 |
| s03 | explain | The speed claim is a vendor simulation: synthetic messages, simulated tools, no real coding. In DeepSeek's runs, ninety-five percent of tasks reached completion inside fifteen point seven minutes. The single-session baseline took twenty-nine point five minutes. | 15.7 vs 29.5 min \| vendor simulation | 11.0 |
| s04 | explain | It's an MIT-licensed repo. A Router session talks to people; isolated Workers run one job each in separate directories. You choose the brain, even a self-hosted model server. | Router talks, Workers run \| you pick the model | 10.0 |
| s05 | payoff_close | It ships in observe mode, just recording, with danger-full-access to your account. Worth cloning, not worth marrying. | observe mode: records only \| full account access | 7.6 |

## Judge scores (kimi-k3, blind, rubric rows 0-3)

| Row | A | B | Reason (judge's line) |
|-----|---|---|------------------------|
| 1 hook | 3 | 2 | A's "You think" lands tension in word one and names DeepSeek; B's surprise waits for the end of the sentence. |
| 2 payoff timing | 3 | 2 | A's break lands at about 2s (scored from the break per the fairness note); B's first concrete lands by 6s. |
| 3 specificity | 3 | 2 | A spends one number per beat, both earn their place; B packs two figures into one sentence plus an unneeded 95% gloss. |
| 4 voice | 2 | 3 | A clean but no wry beat; B's "worth cloning, not worth marrying" lands and is never explained. |
| 5 navigation | 3 | 2 | A's transitions each name what changed and cannot be reordered; B's middle scenes could swap without loss. |
| 6 difference | 1 | 3 | A is a myth-bust three days after a myth-bust shipped; B's shape, opening rhythm, and landing differ from the last three days. |
| 7 repeat test | 2 | 3 | A buries its repeatable line mid-script; B's payoff is the repeatable line and last heard. |
| 8 teaching | 3 | 2 | A shows the why (3-5 session attention limit); B names Router/Workers without the rationale. |
| TOTAL | 20 | 19 | A wins. |

## Graft

One graft, from B to A: B's closing verdict "Worth cloning, not worth marrying." appended to
A's payoff_close after "danger-full-access to your user account." Reason: it is the verdict
A's fence-close reaches for but never states, costs no numbers, makes the repeatable line the
last thing heard, and requires no rewriting of surrounding beats. The hook does not move (the
rubric requires a two-point row-1 gap; B's hook scored lower).

## Loser postmortem (judge's two sentences)

The contrarian shape needed its tension inside the first five words instead of a
headline-style sentence whose surprise waits for the final clause, and it needed the
architecture's why (the 3-5 session limit) so the Router/Worker beat taught rather than just
described. Its wry verdict was the best single line in either draft, but one great last line
could not outscore a script that was winning the first eight seconds.
