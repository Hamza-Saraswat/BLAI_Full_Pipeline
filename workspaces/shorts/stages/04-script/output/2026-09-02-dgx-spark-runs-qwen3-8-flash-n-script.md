---
slug: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n
format: classic
structure: news-react-so-what
style_pack: silicon
value_types: TEACHES,REFRAMES
promise: After watching you can judge any desktop AI box by tokens per second in your own workload, and name the two tricks that put a frontier model on one DGX Spark.
target_duration_s: 38
brief: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n-brief.md
drafts: 2026-09-02-dgx-spark-runs-qwen3-8-flash-n-drafts.md
---

# DGX Spark runs Qwen3.8-Flash-Next at 43 tok/s in coding

## Decisions
- Structures tried: news-react-so-what (draft A) vs comparison-ladder (draft B); A won 22 to 21 on the judge rubric. Both cleared rotation (last two shipped: number-first, myth-bust).
- Hook: Named contradiction ("DGX Spark runs a frontier model at forty-three tokens a second") over Decision; judge scored row 1 level (3/3), so no hook graft.
- Graft taken: B's concrete bandwidth figures replaced A's rounded "four times the bandwidth" clause. Adjusted: the Mac figure is spoken as "more than quadruples that" because the classic band caps spoken numbers at five (43, 360, 135, 20, 273 already spent); the judge's two-number form would have broken the number budget the rubric itself protects.
- The catch was split into its own scene so the payoff line stands alone as the last spoken sentence (ending rule).
- Unattended checkpoint calls: structures A/B as above; hook pick 1 of 10; promise as in frontmatter.

## Hook candidates
1. DGX Spark runs a frontier model at forty-three tokens a second. * (pick, Named contradiction, draft A)
2. DGX Spark or Mac Studio Ultra? One number decides. * (pick, Decision, draft B)
3. Forty-three tokens a second, from a box on your desk. (Number shock)
4. One hundred eighty billion parameters. One desktop box. (Number shock)
5. You run local models. This box runs the frontier. (Situation)
6. Your Mac is not too slow. Its doorway is. (Wrong diagnosis)
7. Three hundred sixty gigabytes, squeezed into one hundred thirty-five. (Number shock)
8. A forum post just moved the local-AI goalposts. (Case)
9. Twenty tokens a second, then forty-three. One trick apart. (Number shock)
10. The bandwidth war is over. Nobody told your workload. (Named contradiction)

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | DGX Spark runs a frontier model at forty-three tokens a second. Word-pieces per second, from one owner's coding test. | DGX Spark: 43 tok/s in coding | Frame 1: black field, one GB10-style chip centered on a green PCB with thin traces, fully legible. Within 0.5 s, on "forty-three tokens a second", a giant 43 scales in above the chip with tok/s beneath it. On "one owner's coding test", a small forum-post card with a code window fades in lower right. Fade and scale only. | hyperframes | giant-number | 6.6 |
| s02 | foreshadow | So a frontier coder keeps pace from your desk. The model is Qwen three point eight Flash Next. Two ideas do the work. | Qwen3.8-Flash-Next, from your desk | Centered stack: a small desktop box outline under a monitor. On "keeps pace", token chips rise from the box into a code editor at typing rhythm. On "Qwen three point eight Flash Next", the model name settles in as a label beside the editor. On "two ideas", two glowing blocks fade in on the chip die, labeled Q and MTP. | hyperframes | centered-stack | 8.3 |
| s03 | explain | Quantization, storing weights in fewer bits, shrinks it from three hundred sixty gigabytes to one hundred thirty-five. It fits. | 360 GB to 135 GB: it fits | Diagram flow: on "three hundred sixty gigabytes", a tall weight stack labeled 360 GB fades in at left. On "shrinks", compression arrows scale it down to a short 135 GB block. On "It fits", the small block drops into a Spark memory-pool outline, spare headroom glowing green. Scale and fade only. | hyperframes | diagram-flow | 6.6 |
| s04 | explain | Multi-token prediction, a draft layer writing several tokens per step. Without it, twenty tokens a second. | 20 tok/s without MTP | Split compare: left lane, on "twenty tokens a second", a chip emits single tokens and a short bar labeled 20 tok/s rises. Right lane, on "several tokens per step", the same chip emits three tokens at once and a tall bar rises, labeled only "with MTP". Bars rise, never slide. | hyperframes | split-compare | 5.5 |
| s05 | explain | One owner, one experimental build. The Spark reads weights at two hundred seventy-three gigabytes a second; a Mac Studio Ultra more than quadruples that. | One owner. Spark 273 GB/s | Grid: on "one owner, one experimental build", two small caveat chips fade in, "one owner" and "experimental build". On "two hundred seventy-three gigabytes a second", a short bandwidth bar rises beside a tall Ultra bar roughly four times higher, unlabeled numerically, Ultra marked only by its name. Fade and rise only. | hyperframes | grid | 8.3 |
| s06 | payoff_close | Judge boxes by tokens per second in your workload. Not bandwidth. | tok/s in your workload. Not bandwidth | On "tokens per second", the grid dims to gray. On "in your workload", the payoff line rises center frame. On "Not bandwidth", the qualifier drops in beneath it, wordmark settling on a clean centered frame that rhymes with frame 1's single focal phrase. Fade and rise only. | hyperframes | centered-stack | 4.5 |

## Notes for review
- The forty-three figure is one forum owner's measurement; the script attributes it twice ("one owner's coding test", "one owner"). Do not let a future edit drop the attribution.
- "More than quadruples that" compresses 273GB/s versus 1.2TB/s; the brief's exact figures are on record if the channel prefers to spend a sixth number and leave the classic band.
- The 200k context and the 2.6x NVIDIA claim were left unspent; both are in the brief if a re-script wants them.
