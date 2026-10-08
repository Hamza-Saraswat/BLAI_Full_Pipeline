---
slug: 2026-10-08-glm-5-3-flash-e224-runs-on-two
stage: 04-script
generated_at: 2026-10-08
---

# Drafts and judgment: GLM 5.3 Flash E224 runs on two DGX Sparks

Two blind drafts on one brief, both classic band, both passing the validator (0 blockers), the nine eval gates (exit 0) and the variety check. Writers were Kimi K3 packets in private scratch dirs; neither saw the other. The judge (a third packet) saw both boards plus the brief.

## Draft A: news-react-so-what (hook pattern: tonight)

| Scene | Narration | On-screen |
|-------|-----------|-----------|
| s01 hook | GLM five point three Flash just shipped for two Sparks tonight. Your Spark needs a twin or a crushed file. | GLM 5.3 Flash / on 2 DGX Sparks / just shipped tonight |
| s02 explain | A community build prunes it to two hundred twenty-four experts per layer. Think layoffs, not pay cuts; real layoffs change answers. | E224 community build / 224 experts per layer / pruned, not crushed |
| s03 explain | NVIDIA's four-bit format, fewer digits per weight, brings the file to one hundred forty-one gigabytes of weights. A single Spark cannot hold it; a network cable links a pair. | NVFP4 weights / 141 GiB / ConnectX-7 links the pair |
| s04 explain | Your Spark has one hundred twenty-eight gigabytes of unified memory. The builder's own runbook clocks fifteen point seven tokens a second. | 128 GB unified memory / 15.7 tok/s / builder's vLLM runbook |
| s05 explain | The three-bit file, one hundred twenty gigabytes of weights, fits one box. | Unsloth 3-bit GGUF / 120.37 GB / fits one box |
| s06 payoff_close | Cable a second Spark for near-full quality, or stay at three-bit. | cable up, or stay 3-bit / Build Local AI |

## Draft B: worked-example (hook pattern: situation)

| Scene | Narration | On-screen |
|-------|-----------|-----------|
| s01 hook | You download the trimmed GLM five point three Flash build. Then the wall: one hundred forty-one gigabytes of weights. | E224 build / 141 GB of weights |
| s02 explain | Your Spark holds one hundred twenty-eight gigabytes of memory. The E two twenty-four build prunes the mixture of experts, a model waking a slice per word. | Spark: 128 GB / E224 prunes the experts |
| s03 explain | It keeps two hundred twenty-four experts a layer in NVIDIA's four-bit format, weights rounded smaller. | 224 experts kept per layer / NVFP4 4-bit weights |
| s04 explain | The fix: a second cabled Spark and tensor parallelism, splitting every word across both boxes. The builder's runbook reports fifteen point seven tokens a second. | ConnectX-7 cable / Tensor parallelism 2 / vLLM 0.31.0: 15.7 tok/s |
| s05 explain | Or keep one Spark: Unsloth's three-bit file, one hundred twenty gigabytes of weights, lower quality. | Unsloth 3-bit GGUF / 120.37 GB on one Spark |
| s06 payoff_close | Cable a second Spark for near-full quality, or stay at three-bit. (grafted from A after judgment; B originally closed "Two Sparks for the bigger build, or one box with the smaller file.") | cable up, or stay 3-bit / Build Local AI |

## Score table

| Row | A | B |
|-----|---|---|
| 1 Hook | 2 | 2 |
| 2 Payoff timing | 2 | 3 |
| 3 Specificity without cramming | 2 | 2 |
| 4 Voice | 3 | 2 |
| 5 Navigation | 2 | 3 |
| 6 Difference | 2 | 2 |
| 7 Repeat test | 3 | 2 |
| 8 Teaching | 2 | 3 |
| **Total** | **18** | **19** |

Winner: B. Reason: B's causal worked-example lands the promised wall (141 GB) by about second four, cannot be reordered without breaking, and teaches two concrete mechanisms (MoE slice-per-word, tensor parallelism splitting every word) that let the viewer predict unmentioned cases, edging out A's stronger voice and closer.

Graft taken from A: the payoff line "Cable a second Spark for near-full quality, or stay at three-bit." B's close was its weakest beat and vague on stakes; A's payoff names the action and carries the brief's promise wording, fits B's second-person imperative voice, adds no new numbers, and drops into the payoff_close scene without touching surrounding beats.

Drift flags the judge raised, both fixed before saving: B's hook originally conflated the base model with the E224 build (141 GiB belongs to the trimmed build; the hook now says "the trimmed GLM five point three Flash build"), and B's on-screen text named "UD-IQ3_XXS", a variant the brief never mentions (now "Unsloth 3-bit GGUF"). A's hook dated the ship event ("tonight") beyond the brief; noted, and the winning hook carries no such date.

What the losing shape would have needed: the news-react shape spent its fast payment restating the fork ("a twin or a crushed file") and then asserted "a single Spark cannot hold it" before stating the 128 GB capacity that proves it, so its middle beats could be reshuffled without breaking. It needed the capacity fact ahead of the verdict and one mechanism beat showing how two cabled boxes actually share the work, not just that a cable exists.
