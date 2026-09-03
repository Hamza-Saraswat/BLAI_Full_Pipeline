---
slug: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n
stage: 04-script
generated_at: 2026-09-03
judge: kimi-k3 via tools/llm_call.py
---

# Drafts: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n

## Draft A (news-react-so-what, Named contradiction hook) - WINNER

PROMISE: After watching, you can judge any desktop AI box by the one number that decides whether a coding agent keeps up with you, tokens per second in your workload, and you can name the two tricks that put a frontier model on a single DGX Spark.

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|---|---|---|---|---|---|---|---|
| 1 | hook | DGX Spark runs a frontier model at forty-three tokens a second. Word-pieces per second, from one owner's coding test. | DGX Spark: 43 tok/s in coding | Frame 1: black field, one GB10-style chip centered on a green PCB with thin traces. Within 0.5 s, on "forty-three tokens a second," a giant "43" scales in above the chip with "tok/s" beneath it. On "one owner's coding test," a small forum-post card with a code window fades in lower right. Fade and scale only. | hyperframes | giant-number | 6.6 |
| 2 | foreshadow | So a frontier coder keeps pace from your desk. The box is almost boring; two ideas do the work. | Frontier coding, from your desk | Centered stack: a small desktop box outline under a monitor. On "keeps pace," token chips rise from the box into a code editor at typing rhythm. On "almost boring," the box outline dulls to plain gray. On "two ideas," two glowing blocks fade in on the chip die, labeled Q and MTP. | hyperframes | centered-stack | 6.6 |
| 3 | explain | Quantization, storing weights in fewer bits, shrinks it from three hundred sixty gigabytes to one hundred thirty-five. It fits. | 360 GB → 135 GB: it fits | Diagram flow: on "three hundred sixty gigabytes," a tall weight stack labeled 360 GB fades in at left. On "shrinks," compression arrows scale it down to a short 135 GB block. On "It fits," the small block drops into a Spark memory-pool outline, spare headroom glowing green. Scale and fade only. | hyperframes | diagram-flow | 6.6 |
| 4 | explain | Multi-token prediction, a draft layer writing several tokens per step. Without it, the box stalls at twenty tokens a second. | 20 tok/s without MTP | Split compare: left lane, on "twenty tokens a second," a chip emits single tokens and a short bar labeled 20 tok/s rises. Right lane, on "several tokens per step," the same chip emits three tokens at once and a tall bar rises, labeled only "with MTP." Bars rise, never slide. | hyperframes | split-compare | 6.9 |
| 5 | payoff_close | The catch: one owner, an experimental model, four times the bandwidth on a Mac Studio Ultra. Tonight, judge boxes by tokens per second in your workload, not bandwidth. | Tok/s in your workload, not bandwidth | Grid: three small catch chips fade in as spoken, "one owner," "experimental model," and "Mac 4x bandwidth" beside a long bandwidth bar dwarfing a short one. On "Tonight," the grid dims to gray and the payoff line rises center frame. Fade and rise only. | hyperframes | grid | 9.7 |

VALUE LINES:
- TEACHES: "Quantization, storing weights in fewer bits, shrinks it from three hundred sixty gigabytes to one hundred thirty-five," paired with "Multi-token prediction, a draft layer writing several tokens per step."
- REFRAMES: "Tonight, judge boxes by tokens per second in your workload, not bandwidth."

## Draft B (comparison-ladder, Decision hook)

PROMISE: After watching, you can choose between a DGX Spark and a Mac Studio Ultra with one repeatable rule: tokens per second in your workload beats bandwidth on the box.

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|---|---|---|---|---|---|---|---|
| 1 | hook | DGX Spark or Mac Studio Ultra? One number decides. Tokens per second, the word pieces your model writes each second. | DGX Spark or Mac Studio Ultra? | Frame 1: dark silicon backdrop, two chip dies side by side, a GB10 superchip left labeled Spark, a large Ultra die right; within 0.5 s a thin ring scales up between them carrying the on-screen question. On "One number decides" both dies dim as a bare counter rises center frame. On "word pieces your model writes each second" small token blocks rise out of the counter, one per beat. | hyperframes | split-compare | 6.9 |
| 2 | explain | The full model needs three hundred sixty gigabytes. Quantization, storing weights in fewer bits, shrinks it to one hundred thirty-five gigabytes. It fits the Spark. | 360 GB → 135 GB | A giant die-grid block labeled 360 GB fills the frame on "three hundred sixty gigabytes." On "storing weights in fewer bits" each grid cell scales down and repacks tighter. On "one hundred thirty-five gigabytes" the whole block scales to a slim 135 GB slab. On "It fits the Spark" the slab rises and settles into a small desktop box outline labeled Spark. | hyperframes | giant-number | 8.6 |
| 3 | explain | Multi-token prediction, a draft layer writing several tokens at once, decides speed. Without it, twenty tokens a second. With it, one owner reports forty-three tokens a second. | 20 tok/s → 43 tok/s | On "Without it, twenty tokens a second" single token blocks rise one per beat, stacking to a short row labeled 20 tok/s. On "a draft layer writing several tokens at once" a slim draft-layer chip fades in beside the main die and fans out three tokens per beat. On "forty-three tokens a second" the stack rises to 43 tok/s, and a small tag reading "owner-measured" fades in beneath it. | hyperframes | centered-stack | 9.3 |
| 4 | explain | The catch: the Spark reads weights at two hundred seventy-three gigabytes a second. The Mac: one point two terabytes a second. Nobody has reproduced that forty-three. | 273 GB/s vs 1.2 TB/s | On "The catch" the frame splits into two empty vertical bandwidth bars. On "two hundred seventy-three gigabytes a second" the left bar labeled Spark 273 GB/s rises a short height. On "one point two terabytes a second" the right bar labeled Mac 1.2 TB/s rises roughly four times taller. On "Nobody has reproduced that forty-three" a forum-post card fades in over the old 43 tok/s tag and an "unreproduced" stamp scales onto it. | hyperframes | split-compare | 9.0 |
| 5 | payoff_close | Count tokens per second in your workload, not bandwidth on the box. | Count tok/s, not bandwidth. | On "Count tokens per second" the bars and dies fade out. On "in your workload" the first line of the rule rises center frame. On "not bandwidth on the box" the second line rises beneath it, ending on a clean centered frame holding only the rule. | hyperframes | centered-stack | 4.1 |

VALUE LINES:
- TEACHES: "Multi-token prediction, a draft layer writing several tokens at once, decides speed." (the fit half lands one scene earlier)
- REFRAMES: "Count tokens per second in your workload, not bandwidth on the box."

## Judge score table

| Row | Draft A | Draft B |
|-----|---------|---------|
| 1 Hook | 3 | 3 |
| 2 Payoff timing | 3 | 2 |
| 3 Specificity | 3 | 3 |
| 4 Voice | 3 | 2 |
| 5 Navigation | 3 | 2 |
| 6 Difference | 1 | 3 |
| 7 Repeat test | 3 | 3 |
| 8 Teaching | 3 | 3 |
| TOTAL | 22 | 21 |

WINNER: A

REASON (judge, verbatim): A cashes its hook inside four seconds with attribution attached in the same breath, its "two ideas" foreshadow makes every transition name what changed, and "the box is almost boring" is the only landed wry beat in either draft. B is the cleaner difference play yet never consummates its own "Spark or Mac?" question; the Mac's tok/s never appears, so the payoff arrives as a metric definition rather than the promised decision.

GRAFTS (judge, verbatim): B scene 4, "The Spark reads weights at two hundred seventy-three gigabytes a second. The Mac: one point two terabytes a second." -> A scene 5, replacing "four times the bandwidth on a Mac Studio Ultra." Reason: the loser states the catch in checkable figures where the winner uses a rounded, unanchored ratio. Hook graft not taken (row 1 level, below threshold).

Applied with one adjustment, recorded in the script note Decisions: the classic band caps spoken numbers at five, so the Mac figure is spoken as "a Mac Studio Ultra more than quadruples that" while the on-screen text carries 273 GB/s beside a visibly taller unlabeled Ultra bar.

LOSER_DIAGNOSIS (judge, verbatim): The comparison-ladder needed to pay its own bet; giving the Mac's tok/s (or stating plainly it cannot load this model) by scene 3 would have turned a late, partial payoff into an early, promised one. It also needed to mark its first rung change and find one wry beat.

FACTUAL_DRIFT: both drafts pass (judge, verbatim): A's hook's bare "forty-three tokens a second" is rescued in the same beat by "from one owner's coding test"; B keeps "one owner reports" and "Nobody has reproduced that forty-three."
