---
slug: 2026-11-05-kimi-k3-1-pro-1-56-tb-of-weigh
format: smooth-explainer
structure: contrarian-take
style_pack: silicon
value_types: TEACHES,REFRAMES
promise: After one hundred eight seconds you can decide what to do about Kimi K three point one Pro tonight: API now, community quant when it lands, offload never.
target_duration_s: 108
brief: 2026-11-05-kimi-k3-1-pro-1-56-tb-of-weigh-brief.md
drafts: 2026-11-05-kimi-k3-1-pro-1-56-tb-of-weigh-drafts.md
---

# Kimi K3.1 Pro Is Free. Running It Isn't.

## Decisions
- Structures tried: worked-example (draft A, the download carried end to end) vs contrarian-take (draft B, "the model is free" taken on). B won the judge 18-16 (21-16 after correcting the judge's row-4 miss: B's receptionist does state its limit, "the receptionist re-picks every word, not once per thought").
- Hook: named-contradiction "Kimi K three point one Pro: free download, can't run." (11 words, product in the first five). The situation hook lost rows 1, 2 and 6: no product in line one, payoff at 6 s, and situation + worked-example both repeat recent ledger entries.
- Draft B's first shape was number-first; withdrawn after its structural number-shock hook failed the sameness gate (repeat of 2026-11-03) and re-assigned contrarian-take before judging. Both drafts that reached the judge passed every gate.
- Graft: A's two sentences on MXFP4 composition ("The big expert weights ship four-bit...") into B's storage beat; judge-approved, no new spoken number.
- Numbers: three spent (one point five six terabytes, twenty-four gigabytes, five hundred ninety-four gigabytes). Seventy-eight point eight seven five percent spoken as "about four fifths" (rounded once). Spark and Studio kept as fractions ("less than a tenth", "about a third").
- Gates: validator zero blockers; two advisories deferred to the package stage (7 hashtags, 0 keyword tags -- package overwrites both). eval_short all nine gates pass, sameness clean.

## Hook candidates
1. You download the new frontier model. Then you see the size.
1. One point five six terabytes of open weights, too big for your machine.
1. Kimi K3.1 Pro is free. Your memory is not.
1. 1.56 TB of weights just landed. Nothing on your desk holds them.
1. The first frontier open-weights drop fits no gaming PC.
1. Your DGX Spark has 128 GB. This model needs 1.56 TB.
1. Free model, one and a half terabytes, no desk holds it.
1. Moonshot shipped a model you cannot run. Here's the math.
1. Too big for a 4090. Too big for a Spark. Quantize.
1. *Kimi K three point one Pro: free download, can't run.*

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s1 | hook | Kimi K three point one Pro: free download, can't run. | Kimi K3.1 Pro: free ≠ runnable | Frame 1 is the finished two-line card, "Kimi K3.1 Pro" with FREE already legible; on "can't run" the second line CAN'T RUN stamps in red and the card scales up a step within half a second | hyperframes | centered-stack | 3.4 |
| s2 | explain | You've seen the claim behind every open-weights drop: the model is free, so anyone can run it. And the download really is free, sitting on Hugging Face right now. | Open weights = anyone can run it? | Feed of launch headlines on "every open-weights drop", settle on a Hugging Face repo page on "sitting on Hugging Face" | hyperframes | giant-number | 10.0 |
| s3 | explain | Here's what free weighs: one point five six terabytes of weights. That's storage, space on a drive. The big expert weights ship four-bit, a compression the model was trained to expect. Everything outside them ships bigger, so the total on Moonshot's page looks like this. | 1.56 TB of weights (storage) | experts: 4-bit, rest: full size | Anchor "one point five six terabytes": a drive-filling bar ticks up and locks, label reading storage, not memory; on "ship four-bit" the bar color-splits, a thin amber four-bit band under a wide full-size band | hyperframes | split-compare | 15.5 |
| s4 | explain | Moonshot built it as a mixture-of-experts model, hundreds of specialist networks with a receptionist that wakes only the few each word needs. And the receptionist re-picks every word, not once per thought. | MoE: few wake, all stay resident | Office floor plan on "hundred specialist networks", a receptionist desk lighting a few rooms on "wakes only the few", the desk pulsing per word on "re-picks every word" | hyperframes | timeline | 11.0 |
| s5 | explain | Speed comes from the activated parameters, the few that wake. The memory bill comes from all of them. | speed: few · memory: all | The lit rooms dim and a speedometer rises on "speed comes from the few"; on "memory bill comes from all of them" every room's rent meter spins at once | hyperframes | grid | 6.2 |
| s6 | explain | Now hold that against your hardware. A top gaming card carries twenty-four gigabytes of video memory. That's about one part in sixty of the download. | 24 GB vs 1.56 TB ≈ 1/60 | A graphics card fades in on "your hardware", its memory chip highlighted as a thin sliver against the full bar on "one part in sixty" | hyperframes | diagram-flow | 8.6 |
| s7 | explain | NVIDIA's DGX Spark, a desktop box built for serious local models, holds less than a tenth. The biggest Mac Studio Apple sells still holds only about a third. | DGX Spark < 1/10 · Mac Studio ≈ 1/3 | The Spark chassis on "DGX Spark" with its bar under one tick, then a Mac Studio on "Mac Studio" with its bar near a third | hyperframes | split-compare | 9.7 |
| s8 | explain | So the honest version is smaller. The download is free. The memory to hold it is not. No machine you own comes close, not NVIDIA's DGX Spark, not Apple's Mac Studio. | Free download. Not free memory. | The launch headline shrinks to a small plain sentence on "the honest version is smaller", machines' bars all fall short on "comes close" | hyperframes | centered-stack | 10.7 |
| s9 | explain | A community quant, a third-party re-encode at fewer bits, is the usual escape. None exists for this model yet. | Community quant: none for K3.1 Pro | A vise compressing the model file on "re-encode at fewer bits", the vise stopping with a clunk on "none exists for this model yet" | hyperframes | timeline | 6.6 |
| s10 | explain | The previous model's smallest squeeze was five hundred ninety-four gigabytes of weights. That's bigger than any Mac, and it agrees with the original about four fifths of the time. | 594 GB 1-bit quant (K3 precedent) | The compressed bar drops in at 594 GB on "five hundred ninety-four", still towering over the Mac bar on "bigger than any Mac", a four-fifths meter filling on "four fifths of the time" | hyperframes | giant-number | 10.0 |
| s11 | explain | There's disk offload, streaming experts from a fast drive as each word needs them. It works. It crawls. | Disk offload: works, crawls | Words trickling out one at a time on "as each word needs them", a progress bar barely moving on "it crawls" | hyperframes | grid | 6.2 |
| s12 | payoff_close | Until a quant exists, renting it from Moonshot's API costs less than the drive you'd buy just to hold it. The weights are free. The machine that runs them isn't. | API < the drive to store it | A receipt beside a hard-drive price tag on "costs less than the drive", cut back to the frame-one card on "the machine that runs them isn't" | hyperframes | centered-stack | 10.3 |

## Notes for review
- The accuracy figure is spoken as "about four fifths of the time"; the brief's verbatim value is 78.875% top-1 agreement and stays off screen in the final board, so the rounded narration is the only claim.
- The Unsloth 594 GB build is for Kimi K3 (same 2.8T/104B base), spoken as "the previous model's smallest squeeze"; it is precedent, not product.
- Analogy limit is spoken in scene four ("the receptionist re-picks every word, not once per thought").
- Terminal-Bench conflict (65.7 vs 67%) was left out entirely; nothing in the script depends on it.
