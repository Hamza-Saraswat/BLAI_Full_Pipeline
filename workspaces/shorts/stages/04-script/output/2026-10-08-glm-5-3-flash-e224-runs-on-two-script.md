---
slug: 2026-10-08-glm-5-3-flash-e224-runs-on-two
format: classic
structure: worked-example
style_pack: silicon
value_types: TEACHES,PROVES
promise: after half a minute the viewer can decide -- cable a second Spark for the near-full-quality build, or stay on one box with the smaller three-bit file.
target_duration_s: 35
brief: 2026-10-08-glm-5-3-flash-e224-runs-on-two-brief.md
drafts: 2026-10-08-glm-5-3-flash-e224-runs-on-two-drafts.md
---

# GLM 5.3 Flash E224 runs on two DGX Sparks

## Decisions
- Structures tried: news-react-so-what (draft A) and worked-example (draft B); both cleared rotation (last two shipped: contrarian-take, myth-bust). Judge: B wins 19 to 18 on payoff timing, navigation and teaching; A stronger on voice and the repeat test.
- Hook: the situation pattern (candidate 2 of 10), because the classic band pays fastest on the viewer's own wall; draft A kept the tonight pattern (candidate 1) and the two patterns were forced apart to stop the writers converging (finding 12).
- Graft from A: the payoff line "Cable a second Spark for near-full quality, or stay at three-bit." replaces B's vaguer close; named by the judge, no surrounding beats touched.
- hook_pattern set explicitly (tonight for A, situation for B): the classifier reads only the frame-1 text, where digits fire number-shock (A) and "can't" fires named-contradiction (B), both clashing with the last two ledger entries; the spoken hooks carry the true patterns.
- Soft gates entity_spend (0.36) and top2 ("GLM-5") failed on form, not substance: narration says "GLM five point three Flash" in spoken form, which the entity matcher does not string-match; the model is named in the hook and on screen. Kept on purpose.
- repeated_phrase advisory: one shared 8-word shingle with 2026-09-30-best-local-coding-llm-what-act (1 of 400, min-hash sample); not reconstructable as a lift. Kept.
- Validator: 0 blockers, 0 advisories on the winner (FK grade 7.2 warning only; the classic band's dense register with named products). Eval: all nine gates pass, exit 0. Variety check: ok, no violations. Normalizer: 2 scenes adjusted (E two twenty-four; GLM spoken form).

## Hook candidates
1. GLM 5.3 Flash runs on two Sparks, as of tonight *
2. You download GLM 5.3 Flash. Then the wall *
3. 141 GiB. Two boxes to hold it
4. Everyone says one Spark can't run GLM Flash
5. One Spark or two for GLM Flash? The gigabytes decide
6. Your Spark isn't too slow for GLM Flash. It's too small
7. Two linked Sparks just served GLM Flash at 15.7 tok/s
8. 15.7 tok/s, from two desk boxes
9. Your one Spark met its match: GLM 5.3 Flash
10. One builder's two Sparks now serve GLM Flash whole

(both picks marked *; A took 1, B took 2; B's shape won and its hook ships)

## Script
| Scene | Role | Narration (spoken form) | On-screen text (digits ok, 8 words max) | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|------------------------------------------|--------------|------|--------|-------|
| s01 | hook | You download the trimmed GLM five point three Flash build. Then the wall: one hundred forty-one gigabytes of weights. | E224 build / 141 GB of weights | Frame 1: matte black silicon field with faint amber circuit traces, hook text "Your Spark can't hold it" at top, a dark DGX Spark outline centered low. Motion onset within 0.5 s: at 0.35 s a giant amber "141 GB" scales in center on "one hundred forty-one gigabytes". On "the wall" the number settles and a thin amber rule snaps under it. Hard cut out. | hyperframes | giant-number | 6.9 |
| s02 | explain | Your Spark holds one hundred twenty-eight gigabytes of memory. The E two twenty-four build prunes the mixture of experts, a model waking a slice per word. | Spark: 128 GB / E224 prunes the experts | Dark silicon grid of memory cells filling bottom-to-top: on "one hundred twenty-eight" the grid fills to a hard ceiling line and stalls; on "prunes" grayed expert slots fade out while amber kept slots stay lit, showing the slice that wakes per word. Change every ~3 s. | hyperframes | grid | 9.0 |
| s03 | explain | It keeps two hundred twenty-four experts a layer in NVIDIA's four-bit format, weights rounded smaller. | 224 experts kept per layer / NVFP4 4-bit weights | Centered stack on dark silicon: a column of tiny expert slots, amber-lit, most rows solid. On "two hundred twenty-four experts" the kept slots brighten in a stagger while grayed-out slots thin to hairlines. On "NVIDIA's four-bit format" each remaining slot compresses with a single tick, then the stack stills. Hard cut. | hyperframes | centered-stack | 5.2 |
| s04 | explain | The fix: a second cabled Spark and tensor parallelism, splitting every word across both boxes. The builder's runbook reports fifteen point seven tokens a second. | ConnectX-7 cable / Tensor parallelism 2 / vLLM 0.31.0: 15.7 tok/s | Two Spark silhouettes joined by an animated amber cable; on "tensor parallelism" a word splits into two halves flowing to both boxes and reassembling; on "fifteen point seven" a counter ticks to 15.7 tok/s beside the pair. | hyperframes | diagram-flow | 8.6 |
| s05 | explain | Or keep one Spark: Unsloth's three-bit file, one hundred twenty gigabytes of weights, lower quality. | Unsloth 3-bit GGUF / 120.37 GB on one Spark | Split compare: left the cabled pair glowing, right a single Spark holding a smaller amber block labeled 120.37 GB; on "lower quality" the right block's edges soften a step. | hyperframes | split-compare | 5.9 |
| s06 | payoff_close | Cable a second Spark for near-full quality, or stay at three-bit. | cable up, or stay 3-bit / Build Local AI | Wordmark settle: the two-box motif from frame 1 shrinks into the Build Local AI wordmark, amber accent; final 0.5 s settle, last frame rhymes with frame 1. | hyperframes | centered-stack | 3.1 |

## Notes for review
Numbers rounded for the ear: one hundred twenty gigabytes spoken for the 120.37 GB Unsloth three-bit file; fifteen point seven tokens a second is the builder's runbook figure on two linked Sparks, not our measurement. The hook says "the trimmed build" so one hundred forty-one gigabytes is attributed to E224, not the base model. The mixture-of-experts picture is carried by "a model waking a slice per word"; no extended analogy is used, so no limit clause was needed. The judge's graft replaced the original close with draft A's payoff line.
