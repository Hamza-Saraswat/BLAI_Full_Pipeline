---
slug: 2026-09-19-fine-tune-on-amd-unsloth-docke
format: smooth-explainer
structure: myth-bust
style_pack: terminal
value_types: EQUIPS,TEACHES
promise: after this Short you can start fine-tuning on the AMD box you already own, tonight, with one Docker pull and no hand-built ROCm stack
target_duration_s: 90
brief: 2026-09-19-fine-tune-on-amd-unsloth-docke-brief.md
drafts: 2026-09-19-fine-tune-on-amd-unsloth-docke-drafts.md
---

# Fine-tune on AMD: the ROCm Docker image

## Decisions
- Two structures tried: how-to-three-moves (draft A, the brief's has_process shape) vs myth-bust (draft B, the CUDA belief broken by the VRAM floors). B won 19-18 on the judge rubric; A scored higher on navigation and difference, B on payoff timing and voice (A carried three over-cap sentences).
- Hook: candidate 4 "AMD boxes don't need a CUDA card anymore." (named-contradiction pattern, 7/7 score); rotation banned number-shock (2026-09-18) and wrong-diagnosis (2026-09-17), so the number hooks scored equal but were unusable.
- Graft from A: the number-free honest-catch sentence after Unsloth's seventy-percent claim.
- Number spend: three-gigabyte Qwen3.5 floor (spoken + on screen, s2), eight-gigabyte Gemma 4 floor (spoken only, s3), seventy-percent claim (spoken, attributed, s8). MI300X benchmark numbers deliberately unspent.
- Lexicon: added spoken forms for AMD, RDNA, TRL, PEFT, UI, SFT to skills/script-gates/tts_lexicon.json (self-test 150/150 after edit).
- Value lines: EQUIPS = s11 "You install Docker, you pull unsloth-rocm, you train." TEACHES = s7 "The method is QLoRA: load the model quantized, compressed to use less memory, and train small adapter weights on top."

## Hook candidates
1. Your Radeon fine-tunes tonight, straight out of Docker.
2. Three moves and your AMD card trains a model.
3. Skip the ROCm weekend. Pull the box instead.
4. AMD boxes don't need a CUDA card anymore. *
5. That old Radeon is a fine-tuning rig now.
6. The ROCm stack you dreaded is now one pull away.
7. Fine-tune Qwen3.5 in three gigabytes of VRAM.
8. No NVIDIA card? Fine-tune anyway.
9. Your last ROCm install died here. This one doesn't.
10. Docker just ate the hardest part of AMD fine-tuning.

## Script
| Scene | Role | Narration (spoken form) | On-screen text | Visual brief | Tool | Layout | Est s |
|-------|------|-------------------------|----------------|--------------|------|--------|-------|
| s1 | hook | AMD boxes don't need a CUDA card anymore. | AMD boxes don't need a CUDA card anymore. | Frame 1: matte-black terminal window with sharp corners centered in the safe area, amber prompt, and the full hook line in large monospace, already legible. At 0.3s a block cursor blinks at line end; on 'CUDA card' a thin amber rule rises in place under those two words. Background and window chrome stay static; nothing else moves. | hyperframes | centered-stack | 2.8 |
| s2 | explain | Every tutorial said it: fine-tuning needs a big NVIDIA card, and your Radeon is for games. Unsloth's floor says Qwen three point five fine-tunes in three gigabytes of VRAM, the memory on your card. | MYTH: big NVIDIA card required | Qwen3.5 fine-tunes in 3GB VRAM | Hard cut from hook to split screen. Upper panel: 'MYTH: big NVIDIA card required' types out on 'Every tutorial said it', then a strikethrough draws across it on 'Unsloth's floor says'. Lower panel: 'Qwen3.5 fine-tunes in' appears, and on the spoken 'three gigabytes of VRAM' the amber '3GB VRAM' scales in sharp, no fade. One text block animates at a time, panels static otherwise. | hyperframes | split-compare | 11.7 |
| s3 | explain | What is true now: Unsloth ships a Docker image, a ready-to-run package holding an app plus every dependency. The unsloth-rocm image carries the whole training stack. Gemma four fine-tunes in eight gigabytes of VRAM, a floor an aging Radeon clears. | docker pull unsloth/unsloth-rocm | Gemma 4: aging Radeons qualify | Single terminal window, hard cut in. On 'Docker image' the command 'docker pull unsloth/unsloth-rocm' types out with a blinking cursor. On 'whole training stack' a hard cut swaps the view to sharp-cornered layer bars filling top to bottom. On 'Gemma four' a small sharp badge 'Gemma 4' rises in place beside the top bar. The eight-gigabyte floor is never shown as text. Amber accents only. | hyperframes | centered-stack | 13.8 |
| s4 | explain | The image is the meal kit, the matched stack in one box. The manual route was grocery shopping. | IMAGE: matched stack in a box | MANUAL: grocery shopping | Diagram-flow, hard cut in. Left: a sharp box labeled IMAGE holding stacked layer bars, appearing on 'meal kit'. Right on 'grocery shopping': an empty shopping-list outline types in with three dimmed rows. One element animating at a time, amber accent only, hard cut out. | hyperframes | diagram-flow | 6.2 |
| s5 | explain | You hunted a PyTorch wheel that matched your ROCm version, AMD's open GPU compute platform. Then a pre-release bitsandbytes wheel for the four-bit fix. One pull replaces the trip. | PyTorch wheel + ROCm version | bitsandbytes wheel: pre-release | Split terminal, hard cut. Left pane on 'PyTorch wheel': 'match wheel to ROCm version' types at the prompt with the version tag rocm7.2 shown dimmed. Right pane on 'bitsandbytes wheel': 'pre-release, four-bit fix' rises in place. On 'One pull replaces the trip' both panes hard-cut to a single amber line 'docker pull unsloth/unsloth-rocm'. One text block animating at a time. | hyperframes | split-compare | 10.0 |
| s6 | explain | The run command passes AMD's kernel device nodes instead of NVIDIA's GPU flag. Your card reaches Docker through the kernel driver, not a container toolkit. A built-in smoke test runs a real training pass and fails loudly if the GPU is unusable. | docker run --device /dev/kfd --device /dev/dri | python /workspace/smoke_test_rocm.py | PASS, or it fails loudly | Terminal window, hard cut. On 'run command' the line 'docker run --device /dev/kfd --device /dev/dri' types out with a backslash continuation. On 'smoke test' a hard cut swaps to 'python /workspace/smoke_test_rocm.py'. On 'fails loudly' an amber status stamp 'PASS, or it fails loudly' snaps in at line end, no fade. Window chrome static throughout, one text block animating at a time. | hyperframes | centered-stack | 14.5 |
| s7 | explain | The method is QLoRA: load the model quantized, compressed to use less memory, and train small adapter weights on top. That is what cuts VRAM to the floor. | QLoRA: frozen quantized base | adapters: trained | Diagram-flow, hard cut in. On 'QLoRA' a wide sharp box labeled 'quantized base, frozen' fades in center. On 'small adapter weights' three small amber boxes rise in place on top of it, labeled 'adapters: trained'. On 'cuts VRAM to the floor' the base box's border thickens once. One element animating at a time, amber accent only, hard cut out. | hyperframes | diagram-flow | 9.7 |
| s8 | explain | Unsloth claims seventy percent less memory use with no accuracy loss. The honest catch: their own measured gain lands short of the headline claim. | vendor claim: no accuracy loss | measured gain: short of headline | Split terminal, hard cut. Left pane on 'Unsloth claims': the line 'vendor claim, no accuracy loss' types at the amber prompt. Right pane on 'The honest catch': the line 'measured gain: short of headline' rises in place, with a thin amber underline flickering once beneath 'short'. No digits shown anywhere; the percentages stay spoken only. One text block animating at a time, hard cut out. | hyperframes | split-compare | 8.3 |
| s9 | explain | It trains RDNA two, the Radeon architecture of recent generations, and newer. Older RDNA one cards get Vulkan inference only, and the Steam Deck's chip is refused. Multi-GPU training stays Linux-only. | TRAINS: RDNA2 and newer | RDNA1: Vulkan inference only | Steam Deck chip: refused | multi-GPU: Linux only | Grid of four sharp-cornered cells, hard cut in. Cell one lights amber on 'It trains RDNA two': 'TRAINS: RDNA2 and newer'. Cell two on 'Older RDNA one cards': 'RDNA1: Vulkan inference only'. Cell three on 'Steam Deck': 'Steam Deck chip: refused'. Cell four on 'Multi-GPU': 'multi-GPU: Linux only'. Cells swap by hard cuts, one at a time, grid frame static. | hyperframes | grid | 10.0 |
| s10 | explain | The myth still wins here: this is a training image. The web UI, JupyterLab, and the prebuilt inference servers stay CUDA-only for now, so some shopping remains. | TRAINING IMAGE ONLY | Studio UI + JupyterLab: CUDA for now | llama.cpp + vLLM: CUDA for now | Centered stack, hard cut. Header 'TRAINING IMAGE ONLY' types in on 'this is a training image'. On 'web UI, JupyterLab' a dimmed row appears: 'Studio UI + JupyterLab: CUDA for now'. On 'inference servers' a second dimmed row: 'llama.cpp + vLLM: CUDA for now'. On 'some shopping remains' a small amber asterisk blinks once beside the header. One text block animating at a time. | hyperframes | centered-stack | 9.3 |
| s11 | payoff_close | Your AMD box is a fine-tuning rig tonight. You install Docker, you pull unsloth-rocm, you train. | install Docker → pull unsloth-rocm → train | BUILD LOCAL AI | Timeline of three sharp nodes joined by an amber line. 'install Docker' lights on its spoken phrase, then 'pull unsloth-rocm', then 'train', each node brightening in sequence. Final 0.5s: nodes settle and the wordmark BUILD LOCAL AI fades to center inside the same terminal chrome as frame 1, so the last frame rhymes with the first. | hyperframes | timeline | 5.5 |

## Notes for review
Graft from draft A (judge row 1 allowed, reason logged in drafts.md): the number-free honest-catch sentence after Unsloth's seventy-percent claim. Numbers: three-gigabyte floor spoken and shown with Qwen three point five; eight-gigabyte floor spoken only; seventy-percent claim spoken with attribution, never on screen. Analogy: meal kit, limit stated ('the kit does not carry the web UI... some shopping remains'). Steam Deck chip refusal kept; RDNA1 Vulkan-only kept.
