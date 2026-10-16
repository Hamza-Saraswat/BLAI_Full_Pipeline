---
slug: 2026-10-16-mlx-distributed-inference-two
format: smooth-explainer
structure: how-to-three-moves
style_pack: signal
value_types: TEACHES,REFRAMES
promise: After this you can wire two Macs into one MLX box tonight, and you know the desk, not the machine, is now the unit of local AI.
target_duration_s: 87
brief: 2026-10-16-mlx-distributed-inference-two-brief.md
drafts: 2026-10-16-mlx-distributed-inference-two-drafts.md
---

# MLX distributed inference: two Mac Studios as one

## Decisions

- Structures tried: how-to-three-moves (draft A) and contrarian-take (draft B); both cleared
  the rotation rule (last two shipped: worked-example, myth-bust). Judge: A wins 23-17.
- Hook: candidate 1 of 10, "Three moves, and Muse Spark Open runs on your desk tonight."
  (tonight pattern; names the product and the deadline in five words). Draft B drew a
  wrong-diagnosis hook to force divergence.
- Graft from the loser: B's tensor-mechanism sentence replaced A's "Tensor split" naming line
  in s05 ("Tensor mode slices every layer, and both Macs compute each layer together, in
  sync."), per the judge; no numbers moved, person and structure unchanged.
- Number budget: three on-screen numbers (816B, 493GB, 24.99); the 7.70 Mistral figure,
  the 1.6TB BF16 figure, 120Gb/s and the Qwen pair were dropped after the first eval round
  failed number_spend at five distinct heard.
- Value delivery: TEACHES lands on the three moves and "It shards the model across both
  automatically" (s03-s05); REFRAMES lands on the payoff "The unit of local AI is no longer
  the machine. It is the desk."
- Gates: validate_storyboard 0 blockers, 2 advisories kept on purpose (YouTube tags are the
  package stage's to write; s05 narration ~18s on screen kept because splitting move three
  would break the how-to shape, and the scene carries two hard-cut visual beats); eval_short
  gate1_ready, failures none, soft advisories entity_spend and top2 (top-2 Muse Spark Open
  and Mac both present; entity_spend 0.29 kept: the how-to spends its names on the commands
  and the model, not on every vendor in the brief).
- Normalizer: 2 scenes adjusted for spoken forms (acronym expansions); no manual edits needed.

## Hook candidates

1. Three moves, and Muse Spark Open runs on your desk tonight. *
2. Your Mac Studio isn't the machine. Your desk is.
3. Two Mac Studios just became one computer, over a cable.
4. Apple shipped a way to double your model memory tonight.
5. Muse Spark Open: 816 B parameters, zero data center.
6. Your MLX memory ceiling just moved to a second desk.
7. A 493 GB model, two Macs, one command tonight.
8. Apple just gave MLX its own NCCL, pronounced jackal.
9. You don't need a bigger Mac. You need a second one.
10. One command now shards a model across your Macs.

## Script

| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | Three moves, and Muse Spark Open runs on your desk tonight. Eight hundred sixteen billion parameters. Your Mac hit its memory ceiling; tonight you go through it. | Muse Spark Open, on your desk tonight | 816B parameters | Frame 1: title card fully legible, motion onset at 0.3s as a slow scale pulse begins. At "eight hundred sixteen billion" a hard cut swaps in a giant 816B rising in place. | hyperframes | giant-number | 9.5 |
| s02 | foreshadow | Quantization to four bits shrinks the weights. Even quartered, they take about four hundred ninety-three gigabytes of model weights. Add working memory and it tips past what one Studio holds. It does not fit. | 493GB | NVFP4: a four-bit format | On "four hundred ninety-three gigabytes" a weight bar fades in beside a slightly taller bar labeled Mac Studio ceiling. At "does not fit" the weight bar flashes once and the text swaps to does not fit. | hyperframes | split-compare | 11.0 |
| s03 | explain | Move one: cable the pair and switch on RDMA, remote direct memory access. One Mac writes straight into the other's memory. The wire is Thunderbolt Five, the port already on your Studio. Two cables double the bandwidth. macOS twenty six point two shipped it. | RDMA = remote direct memory access | On "cable the pair" two Studio boxes fade in and two cable lines draw between them. At "writes straight into the other's memory" a dot pulses along one cable into the second box. | manim | diagram-flow | 13.5 |
| s04 | explain | Move two: install the MLX build with JACCL. You want version zero point thirty point one or later. MLX is Apple's framework for models on Apple silicon. JACCL is the collectives layer: two Macs talking as one cluster. | JACCL, pronounced jackal | On "install the MLX build" a terminal-style line fades in and the version tag pops on. At "two Macs talking as one cluster" two small nodes scale up and a link draws between them under the JACCL label. | hyperframes | centered-stack | 14.0 |
| s05 | explain | Move three: launch one command with a hostfile, a list of your two machines. It shards the model across both automatically. Tensor mode slices every layer, and both Macs compute each layer together, in sync. Muse Spark Open writes back at twenty four point nine nine tokens, word-pieces, a second. | mlx.launch --hostfile hosts.json | 24.99 tokens/s | On "launch one command" the command fades in as a single line. At "writes back" a hard cut swaps to the giant 24.99 landing center while token ticks pop beneath it. | hyperframes | giant-number | 15.0 |
| s06 | explain | Pipeline mode splits by depth, each Mac holding consecutive layers. Like an assembly line. Mistral Medium writes at the same speed on one Mac or two, pipelined. | capacity, not speed | On "assembly line" two station blocks fade in side by side. At "same speed" two equal-height bars pop up under labels one Mac and two Macs, staying level. | manim | split-compare | 9.0 |
| s07 | explain | A real line fills up and gets faster; decode never does. Capacity, not speed. Same trick NVIDIA clusters have run for years. The desk cable is the new part. | same trick, new cable | A filling progress bar appears on "fills up and gets faster" and stalls flat on "decode never does" as the text swaps to capacity, not speed. On "NVIDIA clusters" a data-center tag fades in, then dissolves on "desk cable". | manim | timeline | 8.5 |
| s08 | payoff_close | The unit of local AI is no longer the machine. It is the desk. | The unit is the desk. | Frame 1 of the scene holds both Studio outlines; on "no longer the machine" they fade into one shared rounded frame, motion onset 0.3s. At "It is the desk" the frame settles into a desk silhouette, then the wordmark settles for the final half second. | hyperframes | centered-stack | 6.0 |

## Notes for review

- 24.99 tokens per second is Apple's measured two-machine tensor-parallel decode at
  8,192-token context; the script rounds nothing.
- The 493GB NVFP4 figure technically fits a 512GB Studio before working memory; s02 says
  "tips past what one Studio holds" so the claim stays true with context on top.
- RDMA enablement per the MLX docs (macOS recovery, rdma_ctl enable), not the WWDC Settings
  toggle; the brief records the conflict and trusts the docs.
- The assembly-line analogy carries the pipeline limit ("a real line fills up and gets
  faster; decode never does"), which is also the honest catch: two Studios buy capacity,
  not speed.
