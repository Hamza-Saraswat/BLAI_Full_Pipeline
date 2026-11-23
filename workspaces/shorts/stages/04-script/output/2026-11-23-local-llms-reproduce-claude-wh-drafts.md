---
slug: 2026-11-23-local-llms-reproduce-claude-wh
stage: 04-script
---

# Drafts: 2026-11-23-local-llms-reproduce-claude-wh

Two blind kimi-k3 writers (separate processes, separate scratch dirs, shared brief, private assignments). Judge: kimi-k3, rubric + last five ledger entries, no drafting involvement.

## Draft A (worked-example)

hook_text: CLAUDE AT HOME, FREE?

**s01 / hook / centered-stack / est 6.2s**
NARRATION: You pay for Claude every month. Then a post says you could run it at home for free.
SCREEN: CLAUDE AT HOME, FREE?

**s02 / foreshadow / diagram-flow / est 11.4s**
NARRATION: One developer actually tried it. His box is a home P C, two generations old, with a secondhand graphics card. It runs local models, A I stored as files on his own machine.
SCREEN: ONE DEVELOPER | HOME PC, SECONDHAND CARD

**s03 / explain / split-compare / est 9.7s**
NARRATION: His test was one hard job he built himself: rebuild a research simulation as working code. On that job, the local models landed very close to Claude Sonnet.
SCREEN: ONE HARD JOB, HIS OWN | CLAUDE SONNET VS LOCAL | VERY SIMILAR OUTPUTS

**s04 / explain / giant-number / est 8.3s**
NARRATION: So what did he measure? Claude's app usually streams sixty to eighty tokens a second, tokens being the little chunks of words it writes.
SCREEN: CLAUDE'S APP | 60-80 TOKENS/SEC

**s05 / explain / split-compare / est 8.3s**
NARRATION: His big local models? Thirty tokens a second. He says he's happy to get it. That's just under half the speed of a subscription.
SCREEN: LOCAL BIG MODELS: 30 TOK/SEC | HALF THE SPEED

**s06 / explain / diagram-flow / est 10.0s**
NARRATION: So how does a giant model fit on a gaming card? Quantization, storing the model's numbers with fewer bits, shrinks the file until it fits in your card's memory.
SCREEN: QUANTIZATION | FEWER BITS, SMALLER FILE

**s07 / explain / grid / est 8.3s**
NARRATION: The other trick is mixture of experts, waking only a few specialist parts per token. A huge model ends up running at small-model speed.
SCREEN: MIXTURE OF EXPERTS | FEW SPECIALISTS WAKE

**s08 / explain / centered-stack / est 18.3s**
NARRATION: Now the verdict he wrote. His best local models edge past last year's Claude and almost tie today's Sonnet. The keyword, he writes, is almost. No blind test, no head-to-head benchmark, and no drop-in replacement for the top Claude. In another engineer's test, a leaderboard favorite did nothing while a plainer model finished.
SCREEN: EDGES LAST YEAR'S CLAUDE | ALMOST TIES SONNET | NO BLIND TEST

**s09 / explain / grid / est 14.1s**
NARRATION: Think of a local model as a cover band that has rehearsed your setlist. On the songs it knows, it sounds like the record. His simulation job was one of those songs. Shout a request it never learned, and it fumbles.
SCREEN: COVER BAND | KNOWS YOUR SETLIST | NEW REQUEST? FUMBLES

**s10 / payoff_close / centered-stack / est 9.7s**
NARRATION: So Claude at home is real, and it's a trade, not a replacement. Even the man who ran it still pays ten dollars a month for the original.
SCREEN: CLAUDE AT HOME: REAL | A TRADE, NOT A REPLACEMENT | HE STILL PAYS $10/MO


## Draft B (contrarian-take)

hook_text: LOCAL AI REPRODUCES CLAUDE NOW

**s01 / hook / centered-stack / est 9.0s**
NARRATION: That headline isn't lying about Claude. Its Claude is the wrong one. You know the posts: run Claude at home, free, on your own graphics card.
SCREEN: LOCAL AI REPRODUCES CLAUDE NOW | the wrong Claude

**s02 / foreshadow / grid / est 12.1s**
NARRATION: So ask what reproduce would have to mean. Equal answers on any task, judged in a blind test, where nobody knows which model answered. That test was never run. Not in his experiment. Not anywhere.
SCREEN: same answers, any task | judged blind | that test: never run

**s03 / explain / diagram-flow / est 14.1s**
NARRATION: What exists is smaller. One developer. One home rig with a secondhand graphics card. And one hard task he built himself: turning a research simulation into an interactive web page. On it, his local models land very close to Claude's Sonnet.
SCREEN: one developer, secondhand rig | simulation becomes web page | outputs: very similar

**s04 / explain / split-compare / est 13.1s**
NARRATION: Now the receipts. Claude's app writes at sixty to eighty tokens a second, tokens being the little chunks of words it speaks. His big local tier reaches thirty tokens a second. He says he is happy with that.
SCREEN: Claude app: 60-80 tok/s | his rig: 30 tok/s | just under half

**s05 / explain / timeline / est 15.5s**
NARRATION: His own ceiling is plainer. His two most popular models almost tie Claude's current Sonnet. The keyword is almost. What they edge out is the Claude Opus from a year ago. In another engineer's test, a leaderboard favorite did nothing while a plainer model finished.
SCREEN: last year's Opus: edged out | today's Sonnet: almost | leaderboard favorite: no-op

**s06 / explain / grid / est 13.4s**
NARRATION: So why does any of this work at all? Quantization, storing the model's numbers with fewer bits, shrinks a giant model onto a gaming card. Mixture of experts, waking only a few specialist parts per token, keeps it fast.
SCREEN: quantization: fewer bits, smaller file | mixture of experts: a few wake

**s07 / explain / giant-number / est 19.7s**
NARRATION: So the claim shrinks. A local model is a cover band that rehearsed your setlist. Your weekly tasks sound like the record. A request it never learned does not. Still, the way in is real. His Goldilocks setup runs on a thirty sixty with twelve gigabytes of memory. That card may already sit in your P C.
SCREEN: rehearsed setlist: nailed | new request: stalls | 12 GB | RTX 3060

**s08 / payoff_close / centered-stack / est 15.5s**
NARRATION: So what got reproduced is last year's Claude, just under half the speed, on rehearsed work. The privacy is real, the card might be yours already, and the man who proved it still pays for Claude. Claude at home is a trade, not a replacement.
SCREEN: last year's Claude, rehearsed | just under half the speed | a trade, not a replacement


## Score table

| Row | A | B |
|-----|---|---|
| Hook | 3 | 3 |
| Payoff timing | 2 | 2 |
| Specificity | 3 | 1 |
| Voice | 3 | 3 |
| Navigation | 3 | 3 |
| Difference | 2 | 2 |
| Repeat test | 3 | 3 |
| Teaching | 3 | 3 |
| TOTAL | 22 | 20 |

## Winner

**A** (22 vs 20). A is factually clean against the brief and spends its tight number budget exactly on the viewer's tension, ending on the most repeatable line in either draft ('the man who ran it still pays ten dollars a month'). B is the livelier shape with a stronger hook twist, but its honest beat overclaims -- 'Not anywhere' speaks an absence of evidence as a universal assertion the brief never establishes, capping row 3 at 1 -- and its concrete payload lands a beat later than A's.

Factual drift (finding 17): B: 'That test was never run. Not in his experiment. Not anywhere.' -- the brief establishes only that THIS experiment was not a blind test; 'Not anywhere' asserts a universal absence of evidence as fact (finding 17), capping B's row 3 at 1. Lesser B drifts: 'his two most popular models' softens the brief's 'the two best,' and 'the man who proved it' overstates an experiment the script itself says proved no parity. A: none -- 'No blind test, no head-to-head benchmark' is scoped to the experiment, matching the brief.

## Grafts

- From B into A s08: "In another engineer's test, a leaderboard favorite did nothing while a plainer model finished." -- Row 8 and the honest beat: A's verdict rests entirely on one developer's word, which is precisely the objection; this sentence adds the brief's independent-engineer evidence that rank does not predict harness behavior. It appends cleanly to A's s08 verdict beat with no new numbers, no person shift, and no rewrite of surrounding beats.

## What the loser would have needed

B needed to keep its honest beat inside the evidence -- 'not in his experiment,' full stop -- because the 'Not anywhere' drift cap on row 3 was the entire margin of loss. It also needed its first concrete payload (what reproduce actually meant) to land within a breath of the break rather than after a beat of framing, and a runtime that didn't echo the 110-second script from three days earlier.
