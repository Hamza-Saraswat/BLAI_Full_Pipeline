---
slug: 2026-10-16-mlx-distributed-inference-two
stage: 04-script
generated_at: 2026-10-16
winner: A (how-to-three-moves)
score: A 23, B 17
---

# Drafts: MLX distributed inference, two Mac Studios as one

Both drafts written blind by separate kimi-k3 writers from the same brief, different
structures, different assigned hook patterns. Gates before judging: both boards zero
blockers; A eval failures none (2 numbers heard), B eval failures none after number-budget
trim (3 heard).

## Draft A (how-to-three-moves, hook pattern: tonight) -- WINNER

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | Three moves, and Muse Spark Open runs on your desk tonight. Eight hundred sixteen billion parameters. Your Mac hit its memory ceiling; tonight you go through it. | Muse Spark Open, on your desk tonight / 816B parameters | Frame 1: title card fully legible, motion onset at 0.3s as a slow scale pulse begins. At "eight hundred sixteen billion" a hard cut swaps in a giant 816B rising in place. | hyperframes | giant-number | 9.5 |
| s02 | foreshadow | Quantization to four bits shrinks the weights. Even quartered, they take about four hundred ninety-three gigabytes of model weights. Add working memory and it tips past what one Studio holds. It does not fit. | 493GB / NVFP4: a four-bit format | On "four hundred ninety-three gigabytes" a weight bar fades in beside a slightly taller bar labeled Mac Studio ceiling. At "does not fit" the weight bar flashes once and the text swaps to does not fit. | hyperframes | split-compare | 11.0 |
| s03 | explain | Move one: cable the pair and switch on RDMA, remote direct memory access. One Mac writes straight into the other's memory. The wire is Thunderbolt Five, the port already on your Studio. Two cables double the bandwidth. macOS twenty six point two shipped it. | RDMA = remote direct memory access | On "cable the pair" two Studio boxes fade in and two cable lines draw between them. At "writes straight into the other's memory" a dot pulses along one cable into the second box. | manim | diagram-flow | 13.5 |
| s04 | explain | Move two: install the MLX build with JACCL. You want version zero point thirty point one or later. MLX is Apple's framework for models on Apple silicon. JACCL is the collectives layer: two Macs talking as one cluster. | JACCL, pronounced jackal | On "install the MLX build" a terminal-style line fades in and the version tag pops on. At "two Macs talking as one cluster" two small nodes scale up and a link draws between them under the JACCL label. | hyperframes | centered-stack | 14.0 |
| s05 | explain | Move three: launch one command with a hostfile, a list of your two machines. It shards the model across both automatically. Tensor mode slices every layer, and both Macs compute each layer together, in sync. Muse Spark Open writes back at twenty four point nine nine tokens, word-pieces, a second. | mlx.launch --hostfile hosts.json / 24.99 tokens/s | On "launch one command" the command fades in as a single line. At "writes back" a hard cut swaps to the giant 24.99 landing center while token ticks pop beneath it. | hyperframes | giant-number | 15.0 |
| s06 | explain | Pipeline mode splits by depth, each Mac holding consecutive layers. Like an assembly line. Mistral Medium writes at the same speed on one Mac or two, pipelined. | capacity, not speed | On "assembly line" two station blocks fade in side by side. At "same speed" two equal-height bars pop up under labels one Mac and two Macs, staying level. | manim | split-compare | 9.0 |
| s07 | explain | A real line fills up and gets faster; decode never does. Capacity, not speed. Same trick NVIDIA clusters have run for years. The desk cable is the new part. | same trick, new cable | A filling progress bar appears on "fills up and gets faster" and stalls flat on "decode never does" as the text swaps to capacity, not speed. On "NVIDIA clusters" a data-center tag fades in, then dissolves on "desk cable". | manim | timeline | 8.5 |
| s08 | payoff_close | The unit of local AI is no longer the machine. It is the desk. | The unit is the desk. | Frame 1 of the scene holds both Studio outlines; on "no longer the machine" they fade into one shared rounded frame, motion onset 0.3s. At "It is the desk" the frame settles into a desk silhouette, then the wordmark settles for the final half second. | hyperframes | centered-stack | 6.0 |

Note: s05's tensor sentence ("Tensor mode slices every layer, and both Macs compute each
layer together, in sync.") is the judge's graft from draft B, applied before saving.

## Draft B (contrarian-take, hook pattern: wrong-diagnosis)

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | Your Mac Studio isn't the machine. Your desk is. Yesterday Apple published the recipe that breaks that wall: two Studios, one model. | Your desk is. / Two Studios, one model. | Frame 1 holds "Your desk is." fully legible; motion onset at 0.3s as it rises in place. On "two Studios, one model," two Studio outlines fade in joined by a cable drawing between them, all above the caption band. | hyperframes | centered-stack | 8.5 |
| s02 | foreshadow | The old advice was simple: buy the biggest single machine you can afford. Splitting a model across boxes was a cluster thing, NVIDIA's game, not a desk thing. And for years, it was right. | Buy the biggest single machine. / Cluster thing, not desk thing. | On "biggest single machine," a lone tower scales up at left. On "cluster thing," two gray racks fade in at right as the text swaps by hard cut. | hyperframes | split-compare | 11.5 |
| s03 | explain | Meet Muse Spark Open: eight hundred sixteen billion parameters. In a four-bit format that shrinks the weights, it needs about four hundred ninety-three gigabytes before any working memory. No single Mac holds all of that. | 816B parameters / 493GB in NVFP4 | On "eight hundred sixteen billion parameters," 816B scales in giant. On "four hundred ninety-three gigabytes," a memory bar draws up filling to a 493GB mark, past a ceiling line labeled one Mac that pulses once. | hyperframes | giant-number | 12.5 |
| s04 | explain | Here's what changed. macOS twenty-six point two added RDMA, remote direct memory access: a Mac writing straight into another's memory. MLX, Apple's framework on Apple silicon, added communication collectives named JACCL. The wire is Thunderbolt Five, the port already on your Studio. | RDMA: into another's memory / JACCL, pronounced jackal | On "writing straight into another's memory," two Mac nodes fade in and a line draws between them. On "named JACCL," a tag pops onto the line; on "Thunderbolt Five," the line thickens into a cable and pulses once. | manim | diagram-flow | 15.0 |
| s05 | explain | MLX distributed inference splits a model two ways. Pipeline mode is an assembly line: each Mac holds a block of layers and passes half-finished work to its neighbor. Tensor mode slices every layer, and both Macs compute each layer together, in sync. Same trick NVIDIA clusters run. | Pipeline: blocks of layers in a row / Tensor: every layer sliced in two | On "assembly line," left panel fades in: five layer blocks on Mac A, five on Mac B, arrow between. On "slices every layer," right panel appears with each layer block split half and half and a seam line drawing down the middle. | manim | split-compare | 15.5 |
| s06 | explain | But this line never fills, so decode never speeds up. Mistral Medium writes at the same speed on one Mac or two. Pipeline buys capacity. Tensor mode buys speed: the pair writes twenty-four point nine nine each second, only because the cable is fast. | Same speed on two. / 24.99 tokens/sec | On "the same on two," two equal-length bars pop up, labeled one Mac and two Macs, no digits. On "twenty-four point nine nine," a hard cut swaps to the giant 24.99 landing with a tick pulse. | hyperframes | giant-number | 12.5 |
| s07 | payoff_close | The recipe is one command: mlx.launch with a hostfile, a short JSON list of your machines. The model spreads itself across every Mac on the cables. The unit of local AI is no longer the machine, it is the desk. | mlx.launch + hostfile / The unit of local AI is the desk. | On "one command," a monospace command line rises. On "spreads itself," small shards fade out across two Mac icons; on the payoff line the desk text settles, then a wordmark settle for the final half second. | hyperframes | centered-stack | 14.0 |

## Judge score table

| Row | A | B | Reason |
|-----|---|---|--------|
| 1 Hook | 2 | 3 | A names the product and number fast but the felt tension arrives after five words; B lands the product and the status jab inside five words. |
| 2 Payoff timing | 3 | 2 | A's promised thing is concrete by second 4; B's substance lands around second 6-8 after an abstract claim. |
| 3 Specificity | 3 | 3 | Both spend one number per beat at the load-bearing moments; A held Mistral digit-free (minor: "two cables double the bandwidth" extrapolates the brief's plural). |
| 4 Voice | 3 | 0 | A clean second person, terms defined in-breath, one wry beat that lands; B broke hard constraints: "communication collectives" undefined, 24.99 spoken without its unit, "Yesterday Apple published" beyond the brief. |
| 5 Navigation | 3 | 2 | A's three labels legal, each naming an action, order load-bearing; B's "Here's what changed" generic and two beats swappable. |
| 6 Difference | 3 | 1 | A's shape, hook rhythm and landing overlap nothing in the last five; B reran the 2026-10-11 contrarian-plus-wrong-diagnosis combo. |
| 7 Repeat test | 3 | 3 | Both land the desk aphorism last; B carries "pipeline buys capacity, tensor buys speed" as a second. |
| 8 Teaching | 3 | 3 | A shows why pipelined decode never speeds up and enables the batching prediction; B's lockstep-plus-cable gives a causal model of interconnect-bound scaling. |
| Total | 23 | 17 | |

## Grafts

- One sentence from B s05 into A s05: "Tensor mode slices every layer, and both Macs
  compute each layer together, in sync." replaces A's "Tensor split: every layer, sliced
  across both Macs." Reason: B states the mechanism behind tensor speed that A only names;
  no numbers, person or structure moved. No hook graft: B leads row 1 by only one point,
  below the two-point bar.

## What the losing shape would have needed

B needed to clear the voice gates it broke: define collectives in plain language, speak the
unit with 24.99, and cut the fabricated "yesterday Apple published" framing; the three
hard-constraint breaks zeroed row 4. Structurally it needed a hook pattern other than
wrong-diagnosis and its first concrete beat inside four seconds, because rerunning the
2026-10-11 contrarian shape cost it the difference row outright.
