---
slug: 2026-11-05-kimi-k3-1-pro-1-56-tb-of-weigh
stage: 04-script
winner: B (contrarian-take)
date: 2026-11-05
---

# Drafts: Kimi K3.1 Pro Is Free. Running It Isn't.

## Judge verdict (kimi-k3, blind)

```
WINNER: B

SCORES:
| # | Row | A | B |
|---|-----|---|---|
| 1 | Hook | 1 | 3 |
| 2 | Payoff timing | 2 | 0 |
| 3 | Specificity without cramming | 3 | 3 |
| 4 | Voice | 3 | 0 |
| 5 | Navigation | 2 | 3 |
| 6 | Difference | 0 | 3 |
| 7 | Repeat test | 2 | 3 |
| 8 | Teaching | 3 | 3 |

Totals: A 16, B 18.

ROW NOTES:
- Row 1: B names the product and collides "free" with "can't run" in one four-second breath; A's "the new open-weights frontier model" names only a topic, no product, no number.
- Row 2: A's 1.56 TB lands around six seconds and is exactly what the hook promised; B spends its first fourteen seconds on hook plus consensus restatement, so nothing concrete has landed by ten seconds — scored from the concrete, per the fairness note.
- Row 4: B runs an unlisted, extended analogy (receptionist, office floor, rent meters) with no limit clause anywhere — hard-constraint zero; a 22-word sentence in scene 4 is a second risk. A's hospital carries its paging/off-site limit clause and pays it off in the offload scene, and "Free to download, anyway" is a wry beat that lands.
- Row 6: A's situation hook matches did-it-read's hook pattern and its worked-example shape matches the Oct 31 entry — zero. B's contrarian-take shape, named-contradiction opening rhythm, and mirrored-aphorism landing appear nowhere in the ledger (its ~97 s runtime sits near the Nov 2 smooth-explainer, noted but not decisive).
- Row 7: B's repeatable line "The weights are free. The machine that runs them isn't." is the last line; A's equally repeatable "The weights are free now. The memory isn't." is followed by another sentence, capping it at 2.
- Row 5: B's "Speed comes from the few. The memory bill comes from all of them." is a hinge that names exactly what changed; A's "It's a mixture-of-experts model" is a mechanical topic announcement amid otherwise good transitions.

GRAFTS:
- A scene 3, two sentences ("The big expert weights ship four-bit, a compression the model was trained to expect. Everything outside them ships bigger, which is why the total on Moonshot's page looks like this.") -> into B immediately after scene 3. Reason: B never explains why 2.8T parameters land at 1.56 TB (claim 3, the brief's second myth-bust); A says it in one breath with no new spoken number, and it slots between B's size beat and its MoE beat without rewriting either neighbor.

LOSER ADVICE: A needed to name the product and a number with tension in its first line instead of an anonymous situation hook, which cost it rows 1 and 2. It also needed a shape and hook the ledger hasn't already shipped — worked-example plus situation-hook repeats two recent entries — and its best line deserved to be the last one.
```

## Draft A (worked-example, final gated version)

```
TITLE: Kimi K3.1 Pro: 1.56 TB of Free Weights That Fit Nothing You Own

HOOK: You download the new open-weights frontier model. Then you see the size.

SCENES:
| s1 | hook | You download the new open-weights frontier model. Then you see the size. | Kimi K3.1 Pro download | Frame 1 is a finished repo page, cursor already on Download, the size column cropped out of frame; on "Then you see the size" the page scrolls down and the byte counter slides into view within half a second | 4 |
| s2 | explain | Kimi K three point one Pro, from Moonshot: one point five six terabytes of model weights, free on Hugging Face, posted this week. Free to download, anyway. | 1.56 TB · free on Hugging Face | Anchor "one point five six terabytes": the repo page fills the frame, the byte counter ticks up and locks, shard list scrolling behind it | 10 |
| s3 | explain | The big expert weights ship four-bit, a compression the model was trained to expect. Everything outside them ships bigger, which is why the total on Moonshot’s page looks like this. | experts: 4-bit · rest: full precision | Anchor "ship four-bit": the shard list color-splits, a thin band of amber four-bit shards under a wide band of full-precision ones | 9 |
| s4 | explain | It's a mixture-of-experts model, hundreds of specialist networks, and each token wakes only a few. Picture a hospital packed with specialists. Any patient needs a handful, but the building must house all of them. | a few wake · all must fit | Anchor "each token wakes only a few": a grid of dim specialist tiles, a token pulse crossing and lighting a handful; on "the building must house all of them" the camera pulls back to show the whole ward lit faintly | 13 |
| s5 | foreshadow | And nobody knows who's next, so nobody gets sent home. A real hospital could page an off-site specialist, if you're willing to wait. Keep that in mind. | all of them, on standby | Anchor "nobody gets sent home": the dim tiles pulse once together, a pager icon appears at the edge; on "off-site specialist" a specialist tile appears outside the building outline | 8 |
| s6 | explain | Now aim the file at your hardware. A gaming card holds twenty-four gigabytes of video memory. The DGX Spark, the box built for exactly this, stops around a tenth of the file. | 24 GB vs 1.56 TB | Anchor "aim the file at your hardware": the towering 1.56 TB bar drops in from above; beside it a sliver of a bar for the gaming card, then a short tenth-bar for the Spark | 12 |
| s7 | explain | A maxed-out Mac Studio, the biggest memory Apple sells, holds about a third. As shipped, this file fits no machine that sits on a desk. | fits nothing on your desk | Anchor "about a third": a third-length bar draws beside the tower, the three machine bars flash red together on "fits no machine" | 9 |
| s8 | explain | So the community quant arrives, a third-party re-encoding of the weights at fewer bits. Unsloth's one-bit rebuild of the previous model, same architecture, lands at five hundred ninety-four gigabytes of weights. | Unsloth 1-bit: 594 GB | Anchor "five hundred ninety-four gigabytes": the tower bar compresses step by step down a ladder, stopping on a rung labeled 594 GB | 11 |
| s9 | explain | It kept most of its accuracy on the maker's own table. And no version for this model exists yet. Even that shrunken file still outweighs any Mac. | 78.875% top-1 · this model: none yet | Anchor "maker's own table": an accuracy table row highlights; on "outweighs any Mac" the 594 GB bar sits down beside the Mac bar and tops it | 11 |
| s10 | foreshadow | The other hatch is disk offload: keep the experts on fast storage and stream them in when tokens call. It fits. It crawls. That's the off-site specialist, finally arriving. | disk offload: fits, crawls | Anchor "stream them in": a storage stick feeds expert tiles one at a time into a memory tray, a token counter ticking slowly; the pager icon from earlier flashes on "finally arriving" | 9 |
| s11 | payoff_close | The weights are free now. The memory isn't. So run what fits tonight, and watch the community quant repos. | free weights · paid memory | Anchor "The memory isn't": the tower bar and the card bar side by side, the wordmark settling between them as both fade | 8 |
NARRATION_FULL: You download the new open-weights frontier model. Then you see the size. Kimi K three point one Pro: one point five six terabytes of model weights, free on Hugging Face, posted this week. Free to download, anyway. The big expert weights ship four-bit, a compression the model was trained to expect. Everything else ships bigger, which is why the total looks like this. It's a mixture-of-experts model: hundreds of specialist networks, and each token wakes only a few. Picture a hospital packed with specialists. Any patient needs a handful, but the building must house all of them. And nobody knows who's next, so nobody gets sent home. A real hospital could page an off-site specialist, if you're willing to wait. Keep that in mind. Now aim the file at your hardware. A gaming card holds twenty-four gigabytes of video memory. The DGX Spark, the box built for exactly this, stops around a tenth of the file. A maxed-out Mac Studio, the biggest memory Apple sells, holds about a third. As shipped, this file fits no machine that sits on a desk. So the community quant arrives, a third-party re-encoding of the weights at fewer bits. Unsloth's one-bit rebuild of the previous model, same architecture, lands at five hundred ninety-four gigabytes of weights. It kept most of its accuracy on the maker's own table. And no version for this model exists yet. Even that shrunken file still outweighs any Mac. The other hatch is disk offload: keep the experts on fast storage and stream them in when tokens call. It fits. It crawls. That's the off-site specialist, finally arriving. The weights are free now. The memory isn't. So run what fits tonight, and watch the community quant repos.
```

## Draft B (contrarian-take, final gated + grafted version)

```
TITLE: Kimi K3.1 Pro Is Free. Running It Isn't.

HOOK: Kimi K three point one Pro: free download, can't run.

SCENES:
| id | role | narration | on_screen_text | visual_brief | est_duration_s |
| s1 | hook | Kimi K three point one Pro: free download, can't run. | Kimi K3.1 Pro: free ≠ runnable | Frame 1 is the finished two-line card, "Kimi K3.1 Pro" with FREE already legible; on "can't run" the second line CAN'T RUN stamps in red and the card scales up a step within half a second | 3.4 |
| s2 | consensus | You've seen the claim behind every open-weights drop: the model is free, so anyone can run it. And the download really is free, sitting on Hugging Face right now. | Open weights = anyone can run it? | Feed of launch headlines on "every open-weights drop", settle on a Hugging Face repo page on "sitting on Hugging Face" | 10.0 |
| s3 | evidence_size | Here's what free weighs: one point five six terabytes of weights. That's storage, space on a drive. The big expert weights ship four-bit, a compression the model was trained to expect. Everything outside them ships bigger, which is why the total on Moonshot's page looks like this. | 1.56 TB of weights (storage) | experts: 4-bit, rest: full size | Anchor "one point five six terabytes": a drive-filling bar ticks up and locks, label reading storage, not memory; on "ship four-bit" the bar color-splits, a thin amber four-bit band under a wide full-size band | 16.2 |
| s4 | evidence_moe | Moonshot built it as a mixture-of-experts model, hundreds of specialist networks with a receptionist that wakes only the few each word needs. And the receptionist re-picks every word, not once per thought. | MoE: few wake, all stay resident | Office floor plan on "hundred specialist networks", a receptionist desk lighting a few rooms on "wakes only the few", the desk pulsing per word on "re-picks every word" | 11.0 |
| s5 | evidence_moe | Speed comes from the activated parameters, the few that wake. The memory bill comes from all of them. | speed: few · memory: all | The lit rooms dim and a speedometer rises on "speed comes from the few"; on "memory bill comes from all of them" every room's rent meter spins at once | 6.2 |
| s6 | evidence_card | Now hold that against your hardware. A top gaming card carries twenty-four gigabytes of video memory. That's about one part in sixty of the download. | 24 GB vs 1.56 TB ≈ 1/60 | A graphics card fades in on "your hardware", its memory chip highlighted as a thin sliver against the full bar on "one part in sixty" | 8.6 |
| s7 | evidence_machines | NVIDIA's DGX Spark, a desktop box built for serious local models, holds less than a tenth. The biggest Mac Studio Apple sells still holds only about a third. | DGX Spark < 1/10 · Mac Studio ≈ 1/3 | The Spark chassis on "DGX Spark" with its bar under one tick, then a Mac Studio on "Mac Studio" with its bar near a third | 9.7 |
| s8 | narrower_claim | So the honest version is smaller. The download is free. The memory to hold it is not. No machine you own comes close, not NVIDIA's DGX Spark, not Apple's Mac Studio. | Free download. Not free memory. | The launch headline shrinks to a small plain sentence on "the honest version is smaller", machines' bars all fall short on "comes close" | 10.7 |
| s9 | tradeoff_quant | A community quant, a third-party re-encode at fewer bits, is the usual escape. None exists for this model yet. | Community quant: none for K3.1 Pro | A vise compressing the model file on "re-encode at fewer bits", the vise stopping with a clunk on "none exists for this model yet" | 6.6 |
| s10 | tradeoff_quant | The previous model's smallest squeeze was five hundred ninety-four gigabytes of weights. That's bigger than any Mac, and it agrees with the original about four fifths of the time. | 594 GB 1-bit quant (K3 precedent) | The compressed bar drops in at 594 GB on "five hundred ninety-four", still towering over the Mac bar on "bigger than any Mac", a four-fifths meter filling on "four fifths of the time" | 10.0 |
| s11 | tradeoff_offload | There's disk offload, streaming experts from a fast drive as each word needs them. It works. It crawls. | Disk offload: works, crawls | Words trickling out one at a time on "as each word needs them", a progress bar barely moving on "it crawls" | 6.2 |
| s12 | payoff_close | Until a quant exists, renting it from Moonshot's API costs less than the drive you'd buy just to hold it. The weights are free. The machine that runs them isn't. | API < the drive to store it | A receipt beside a hard-drive price tag on "costs less than the drive", cut back to the frame-one card on "the machine that runs them isn't" | 10.3 |

NARRATION_FULL: Kimi K three point one Pro: free download, can't run. You've seen the claim behind every open-weights drop: the model is free, so anyone can run it. And the download really is free, sitting on Hugging Face right now. Here's what free weighs: one point five six terabytes of weights. That's storage, space on a drive. The big expert weights ship four-bit, a compression the model was trained to expect. Everything outside them ships bigger, which is why the total on Moonshot's page looks like this. Moonshot built it as a mixture-of-experts model, hundreds of specialist networks with a receptionist that wakes only the few each word needs. And the receptionist re-picks every word, not once per thought. Speed comes from the activated parameters, the few that wake. The memory bill comes from all of them. Now hold that against your hardware. A top gaming card carries twenty-four gigabytes of video memory. That's about one part in sixty of the download. NVIDIA's DGX Spark, a desktop box built for serious local models, holds less than a tenth. The biggest Mac Studio Apple sells still holds only about a third. So the honest version is smaller. The download is free. The memory to hold it is not. No machine you own comes close, not NVIDIA's DGX Spark, not Apple's Mac Studio. A community quant, a third-party re-encode at fewer bits, is the usual escape. None exists for this model yet. The previous model's smallest squeeze was five hundred ninety-four gigabytes of weights. That's bigger than any Mac, and it agrees with the original about four fifths of the time. There's disk offload, streaming experts from a fast drive as each word needs them. It works. It crawls. Until a quant exists, renting it from Moonshot's API costs less than the drive you'd buy just to hold it. The weights are free. The machine that runs them isn't.
```
