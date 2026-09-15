---
slug: 2026-09-15-4x-dgx-sparks-the-rack-power-a
format: smooth-explainer
structure: worked-example
style_pack: silicon
value_types: TEACHES,REFRAMES
promise: After this you can decide whether a rack of Sparks buys you the model class you need, knowing it buys memory and not speed.
target_duration_s: 100
brief: 2026-09-15-4x-dgx-sparks-the-rack-power-a-brief.md
drafts: 2026-09-15-4x-dgx-sparks-the-rack-power-a-drafts.md
---

# 4x DGX Sparks: the rack, power and multi-node math

## Decisions

- Structures tried: worked-example (A) and number-first (B, later rewritten as myth-bust after the first B draft failed the sameness gate: number-first repeated 2026-09-12's ledger entry, and the price hook classified number-shock, which also repeats 2026-12). Worked-example won 19 to 16.
- Hook: "Your DGX Spark just hit its ceiling." (situation pattern, viewer_situation named inside three words; alternative "Four thousand seven hundred dollars a box. Four boxes." kept for the price angle in drafts).
- Graft from B: the sentence "Every word pulls some weights through it." into the catch scene (s05), reason: A named the road-width gap but never said why a thin cable taxes every token.
- Style pack silicon picked by rotation script (previous signal); music steady-build.

## Hook candidates

1. Your DGX Spark just hit its ceiling. *
2. Four thousand seven hundred dollars a box. Four boxes.
3. Five hundred twelve gigabytes. No GPU you can buy has that.
4. Four Sparks bought memory, not speed.
5. One box is a toy. Four are a rack.
6. You bought one hundred twenty-eight gigabytes. The biggest models laugh at it.
7. A team bought four DGX Sparks. Here is the math.
8. Why would anyone cable four Sparks in a ring?
9. The cable, not the box, decides your speed.
10. Your rack reads at human pace. That is the point.

## Script

| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s01 | hook | Your DGX Spark just hit its ceiling. The newest open models grew past what your box can hold. | Your Spark hit a ceiling | Frame 1 is the finished composition: dark desk, one amber-outlined box dead center, the caption already legible above it. Motion onset at 0.3 seconds: the box scales up one notch. On 'Your DGX Spark' a single small amber-outlined box fades in center-frame on a dark desk. On 'hit its ceiling' a flat amber line scales in just above the box and the box rises slightly to press against it. On 'grew past' a taller translucent block fades in above the line, looming over the box. | hyperframes | centered-stack | 5.5 |
| s02 | foreshadow | An open model called GLM five point two just landed. Its card lists seven hundred fifty-three billion parameters, the stored dials a model reads to write. No single graphics card you can buy holds them all. | 753B | On 'seven hundred fifty-three billion parameters' a giant amber '753B' scales up center-frame. On 'stored dials' small dial glyphs fade in, dotting the dark space around the number. On 'No single graphics card' a consumer GPU card outline fades in below the number, visibly dwarfed, then dims. | hyperframes | giant-number | 12.4 |
| s03 | explain | Your Spark carries one hundred twenty-eight gigabytes of unified memory, one pool the processor and the graphics chip share. That was roomy last year. This model is roomier. | 128 GB, one shared pool | Split frame. On 'one hundred twenty-eight gigabytes' the left pane fades in: your small box with a bar labeled '128 GB'. On 'one pool' the bar fills amber edge to edge, no divider, showing the single shared pool. On 'This model is roomier' the right pane rises in: an unlabeled dark block several times taller than the bar. | hyperframes | split-compare | 9.7 |
| s04 | explain | So you cable four Sparks together. Tensor parallelism, the trick that splits one model across boxes, pools their memory into one heap. Four boxes give five hundred twelve gigabytes of pooled memory, and the giant finally fits. | 512 GB | On 'cable four Sparks together' four small boxes fade in as a two by two grid, then thin amber cables fade in linking them. On 'pools their memory' four short bars scale up inside the boxes and merge into one tall shared bar. On 'five hundred twelve gigabytes' the merged bar is labeled '512 GB' in amber, and the translucent giant block from earlier settles onto it. | hyperframes | grid | 11.7 |
| s05 | explain | Here is the catch, straight from Petronella's measurements. Inside a box, memory feeds the chip over a wide road. The cable between boxes is about a tenth as wide. Every word pulls some weights through it. | Wide road in, thin road out | On 'wide road' the left pane fades in: a box interior with a thick amber band pulsing from memory block to chip. On 'a tenth as wide' the right pane fades in: two boxes joined by a hairline amber thread, the band shrunk to a tenth. On 'every word pulls some weights' small weight glyphs tick across the thin thread one at a time. | manim | split-compare | 10.5 |
| s06 | explain | Picture four movers with one piano. Together they lift it, but they keep stopping to call out the next step. | Four movers, one piano | On 'four movers' four small figures fade in along a horizontal line, the piano glyph centered beneath. On 'keep stopping' the figures pulse in sequence, each pausing at a doorway mark on the line before the next moves. | manim | timeline | 6.8 |
| s07 | explain | A benchmark team called Petronella ran four boxes on GLM five point three Flash, a smaller open model. On plain prose it decoded twenty-six point five tokens per second. A token is a chunk of a word, so that is reading pace. | 26.5 tok/s | On 'twenty-six point five tokens per second' a giant amber '26.5 tok/s' scales up center-frame. On 'reading pace' a line of answer text types on beneath the number at calm reading speed, keeping the number company. | hyperframes | giant-number | 11.5 |
| s08 | explain | The piano picture bends for sparse models like Qwen three point eight Flash Next, a kind that wakes only a few small specialists per word. There, more boxes really do pay. | Sparse models: boxes pay | On 'expert-mixture models' the piano from the earlier scene dissolves and four small specialist glyphs light up along a horizontal timeline, only two glowing at a time. On 'more boxes really do pay' a fourth node rises in at the end of the line and the glyphs brighten. | hyperframes | timeline | 7.5 |
| s09 | explain | Alex Ellis's team built this. They cabled four Sparks into a closed ring, with no network switch at all. They also patched the networking library that moves data between boxes, so neighbors relay. | A ring, no switch | On 'four Sparks' four nodes rise into a diamond formation on dark. On 'closed ring' amber arcs fade in joining each node to its two neighbors, closing the loop. On 'no network switch' a gray switch glyph fades in off to the side with an amber cross over it, then fades out. On 'neighbors relay' small amber packets fade from node to node around the ring. | manim | diagram-flow | 11.7 |
| s10 | explain | So what did four boxes buy? Not speed. The decode strolls at reading pace. They bought a model class your shelf could not hold yesterday. | Not a speed buy | On 'Not speed' the left pane fades in: a shallow amber arc gauge with the needle resting low. On 'model class' the right pane rises: the tall dark block from the earlier scenes now resting on a thin shelf line, fitting. On 'could not hold yesterday' the shelf line brightens from dim gray to amber. | hyperframes | split-compare | 9.0 |
| s11 | payoff_close | Four Sparks buy memory, not speed. The model that outgrew your one box now fits on four, and it answers at the pace you read. | Memory, not speed | Loop anchor: on 'your one box' the frame-one composition returns, same dark desk, same amber ceiling line, one small box beneath it. On 'now fits on four' three more identical boxes scale in beside the first, the ceiling line fades out, and the four boxes settle where the single box began. | hyperframes | centered-stack | 8.6 |

## Notes for review

- "about a tenth as wide" is the writer's rounding of 273 GB/s inside a unit vs 25 GB/s between units; the brief carries the verbatim numbers if you want them on screen instead.
- The Petronella 26.5 tok/s is measured on GLM-5.3-Flash NVFP4 prose, not on GLM-5.2; the script says "a smaller open model" to keep that honest.
- The piano analogy's limit (sparse/MoE models where four boxes beat two) is spoken in s08.
- Qwen three point eight Flash Next (s08) is the brief's four-to-eight-node sweet-spot example, named for specificity only.
