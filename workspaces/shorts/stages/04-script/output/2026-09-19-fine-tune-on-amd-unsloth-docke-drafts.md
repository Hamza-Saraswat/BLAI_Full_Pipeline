---
slug: 2026-09-19-fine-tune-on-amd-unsloth-docke
stage: 04-script
generated: 2026-09-19
---

# Drafts and judge: 2026-09-19-fine-tune-on-amd-unsloth-docke

Both drafts are smooth-explainer, terminal pack, blind-written by separate Kimi K3 calls; both passed every machine gate before judging (validator, eval, variety).

## Draft Draft A (how-to-three-moves, hook: tonight pattern)

- **s1 (hook, centered-stack, 8.6s)** Your Radeon fine-tunes tonight, straight out of Docker. Every tutorial you tried skipped your AMD card, and your last ROCm install died on version tags.
  - on screen: Your Radeon fine-tunes tonight. | straight out of Docker.
- **s2 (explain, diagram-flow, 13.1s)** Unsloth shipped a Docker image, a ready-to-run package holding the whole training stack, built for AMD. PyTorch comes matched to ROCm seven point two, AMD's answer to CUDA, with the fixed bitsandbytes, TRL, and PEFT in one box.
  - on screen: unsloth/unsloth-rocm | PyTorch + ROCm 7.2 | bitsandbytes | TRL | PEFT
- **s3 (explain, grid, 8.3s)** The Docker image is a meal kit. Skip an ingredient the kit does not carry, like the web UI, and you are shopping again.
  - on screen: meal kit: matched stack | web UI: empty slot
- **s4 (explain, centered-stack, 9.3s)** Install Docker Engine on your Linux host. One command from the docs downloads the installer and runs it. If Docker is already there, this step is done.
  - on screen: curl -fsSL https://get.docker.com \ | -o get-docker.sh && sh get-docker.sh
- **s5 (explain, split-compare, 15.5s)** Run the container with the AMD device nodes. Your card reaches Docker through slash dev slash kfd, the kernel node that exposes the compute driver, so you pass device flags instead of gpus all. Mount your Hugging Face cache so downloads survive deleting the container.
  - on screen: --device /dev/kfd --device /dev/dri | -v hf-cache:/root/.cache/huggingface
- **s6 (explain, timeline, 13.8s)** The image carries a built-in smoke test, a real QLoRA run on small adapter weights, that fails loudly if your GPU cannot train. The base model stays frozen. Run it first. A broken setup screams before you waste an evening.
  - on screen: python /workspace/smoke_test_rocm.py | PASS or loud FAIL
- **s7 (explain, grid, 7.6s)** Train your model inside the container. Load it with Unsloth's FastModel, wrap it in adapters with get_peft_model, then fit it with SFTTrainer.
  - on screen: FastModel | get_peft_model | SFTTrainer | trainer.train()
- **s8 (explain, split-compare, 12.1s)** bitsandbytes, the library handling the quantized load, is what cuts memory. Gemma four fits in eight gigabytes of VRAM. This is a training image, so the web UI and inference extras stay CUDA-only for now.
  - on screen: memory: 8GB floor, spoken | web UI + inference: CUDA for now
- **s9 (payoff_close, giant-number, 14.1s)** Three gigabytes of VRAM, and Qwen three point five trains on the Radeon you already own. The honest catch: their own measured gain lands short of the headline claim, and some chips still force rebuilds. Still, the ROCm weekend is over.
  - on screen: 3GB VRAM | Qwen3.5
- Title: Fine-tune on AMD with Unsloth Docker

## Draft Draft B (myth-bust, hook: named-contradiction pattern)

- **s1 (hook, centered-stack, 2.8s)** AMD boxes don't need a CUDA card anymore.
  - on screen: AMD boxes don't need a CUDA card anymore.
- **s2 (explain, split-compare, 11.7s)** Every tutorial said it: fine-tuning needs a big NVIDIA card, and your Radeon is for games. Unsloth's floor says Qwen three point five fine-tunes in three gigabytes of VRAM, the memory on your card.
  - on screen: MYTH: big NVIDIA card required | Qwen3.5 fine-tunes in 3GB VRAM
- **s3 (explain, centered-stack, 13.8s)** What is true now: Unsloth ships a Docker image, a ready-to-run package holding an app plus every dependency. The unsloth-rocm image carries the whole training stack. Gemma four fine-tunes in eight gigabytes of VRAM, a floor an aging Radeon clears.
  - on screen: docker pull unsloth/unsloth-rocm | Gemma 4: aging Radeons qualify
- **s4 (explain, diagram-flow, 6.2s)** The image is the meal kit, the matched stack in one box. The manual route was grocery shopping.
  - on screen: IMAGE: matched stack in a box | MANUAL: grocery shopping
- **s5 (explain, split-compare, 10.0s)** You hunted a PyTorch wheel that matched your ROCm version, AMD's open GPU compute platform. Then a pre-release bitsandbytes wheel for the four-bit fix. One pull replaces the trip.
  - on screen: PyTorch wheel + ROCm version | bitsandbytes wheel: pre-release
- **s6 (explain, centered-stack, 14.5s)** The run command passes AMD's kernel device nodes instead of NVIDIA's GPU flag. Your card reaches Docker through the kernel driver, not a container toolkit. A built-in smoke test runs a real training pass and fails loudly if the GPU is unusable.
  - on screen: docker run --device /dev/kfd --device /dev/dri | python /workspace/smoke_test_rocm.py | PASS, or it fails loudly
- **s7 (explain, diagram-flow, 9.7s)** The method is QLoRA: load the model quantized, compressed to use less memory, and train small adapter weights on top. That is what cuts VRAM to the floor.
  - on screen: QLoRA: frozen quantized base | adapters: trained
- **s8 (explain, split-compare, 8.3s)** Unsloth claims seventy percent less memory use with no accuracy loss. The honest catch: their own measured gain lands short of the headline claim.
  - on screen: vendor claim: no accuracy loss | measured gain: short of headline
- **s9 (explain, grid, 10.0s)** It trains RDNA two, the Radeon architecture of recent generations, and newer. Older RDNA one cards get Vulkan inference only, and the Steam Deck's chip is refused. Multi-GPU training stays Linux-only.
  - on screen: TRAINS: RDNA2 and newer | RDNA1: Vulkan inference only | Steam Deck chip: refused | multi-GPU: Linux only
- **s10 (explain, centered-stack, 9.3s)** The myth still wins here: this is a training image. The web UI, JupyterLab, and the prebuilt inference servers stay CUDA-only for now, so some shopping remains.
  - on screen: TRAINING IMAGE ONLY | Studio UI + JupyterLab: CUDA for now | llama.cpp + vLLM: CUDA for now
- **s11 (payoff_close, timeline, 5.5s)** Your AMD box is a fine-tuning rig tonight. You install Docker, you pull unsloth-rocm, you train.
  - on screen: install Docker → pull unsloth-rocm → train | BUILD LOCAL AI
- Title: Fine-tune on AMD: the ROCm Docker image

## Judge scores (0-3 per row, max 24)

| Row | A | B | Why |
|-----|---|---|-----|
| 1 | 3 | 3 | Both name a product and a felt tension inside five words: Radeon/Docker for the burned AMD owner, CUDA card for the NVIDIA-taxed viewer. |
| 2 | 1 | 2 | A's hook runs 8.6s and the concrete image lands at ~9s; B's Qwen/3GB fact lands ~5s after the break, which is where the fairness note starts the clock. |
| 3 | 3 | 3 | Both spend their three numbers where they land hardest (3GB, 8GB, 70%) and every beat carries a specific; A's five-name pile in s2 is the only cram pressure. |
| 4 | 0 | 3 | A breaks hard constraint 9 three times (s2: 22 words, s5: 26 words, s6: 23 words) and leaves QLoRA and SFTTrainer undefined (constraint 3); B is within cap, every term defined, wry beats land on things. |
| 5 | 3 | 2 | A's install-run-test-train spine cannot be reordered and each beat opens by naming the new action; B has two strong named turns but its middle beats (s5-s8) could swap without breaking. |
| 6 | 3 | 1 | How-to with a tonight-promise hook is absent from the whole ledger; B repeats the 09-16 script's exact structure and hook pattern (myth-bust, named-contradiction). |
| 7 | 3 | 2 | A's repeatable line 'the ROCm weekend is over' is the last thing heard; B's most repeatable line is its hook, and the video ends on 'you train' instead. |
| 8 | 2 | 3 | B's QLoRA mechanism plus the /dev/kfd kernel-path explanation let a viewer predict unmentioned cases (full fine-tune won't fit, other AMD images need the same flags); A shows the mechanism but scattered and with QLoRA undefined. |
| **Total** | **18** | **19** | |

Winner: **B (myth-bust)**, 19-18.

## Grafts
- Sentence from A into B's claim/catch scene (now s8): "The honest catch: their own measured gain lands short of the headline claim." -- B quoted Unsloth's seventy-percent claim but omitted the measured shortfall the brief flags; the sentence is number-free, so B's three-number budget survives.

## What the losing shape would have needed
A had the stronger spine and the fresher shape, but three narration sentences run past the twenty-word hard cap and QLoRA plus the s7 API names go undefined, which zeroes the voice row. It also needed the concrete delivery inside the first eight seconds: a one-sentence hook naming the unsloth-rocm image would have paid the promise before second 8 instead of after it.

## Gate log
- Draft A: validator blockers 0; eval failures number_spend (round 1: bare "Step one/two/three" ordinals substring-matched the s/step benchmark rows; fixed by dropping the ordinals), then scene_specificity (fixed with glossary-grounded rewrites); final eval exit 0.
- Draft B: validator blockers 0 throughout; eval exit 0 every round; fixes were advisory-level only (hook_text length, number referent, long scenes, runaway sentence).
- variety_check: ok for both drafts against the 15-entry ledger (no structure/hook/closing/duration/opener clashes).
