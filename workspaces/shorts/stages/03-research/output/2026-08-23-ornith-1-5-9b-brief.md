# Ornith 1.5 9B, a dense nine-billion-parameter model whose four-bit build fits a mid-range gaming card: research brief

## Summary

A nine-billion-parameter model reports seventy point six on SWE-bench Verified, and its four-bit build is five and a half gigabytes, so the file fits a card you may already own. The scores are the lab's own.

## Thesis

A nine-billion-parameter model reports seventy point six on SWE-bench Verified, and its four-bit build is five and a half gigabytes, so the file fits a card you may already own. The scores are the lab's own.

## Explanation path

Open on the viewer's hardware, not on the model: an eight-gigabyte card and the standing assumption that nothing serious fits. Give the file size before the benchmark, because the size is the surprise and the benchmark is the reason to care. Then the score, once, with what it measures. Then the honest catch: the lab ran and published its own numbers, though with unusually strict controls. Close on what they can actually do tonight.

## Viewer situation

You have a graphics card with eight or twelve gigabytes and you keep being told nothing serious fits on it.

## Has process

false

## Objection

Benchmark numbers on a model card are self-reported by the people who trained the model.

## Claims

1. Ornith-1.5-9B is a 9B dense model the Ornith team describes as 'designed for efficient single-GPU deployment', built on Qwen3.5 and Gemma4 with additional pretraining and post-training. [primary, high confidence] -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF (accessed 2026-08-23)
2. The GGUF builds are Q4_K_M at 5.63 GB, Q5_K_M at 6.47 GB, Q6_K at 7.36 GB, Q8_0 at 9.53 GB and BF16 at 17.9 GB. [primary, high confidence] -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF (accessed 2026-08-23)
3. The card reports SWE-bench Verified 70.6, GPQA Diamond 86.4 and Terminal-Bench 2.1 Terminus-2 46.2, and the model is MIT licensed with a 262,144-token context window. [primary, high confidence] -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF (accessed 2026-08-23)
4. The GGUF build recorded 359,078 downloads in its first month and 168 likes. [primary, high confidence] -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF (accessed 2026-08-23)
5. Ornith AI shipped Ornith-1.5 on 2026-08-20 in three sizes, a 397B mixture of experts, a 35B mixture of experts and this 9B dense model. [primary, medium confidence] -- https://ornith.ai/ornith_1_5.html (accessed 2026-08-23)
6. Ornith reports the figures as averaged over five independent runs, evaluated through OpenHands for SWE-bench and Harbor/Terminus-2 for Terminal-Bench, with git history stripped from the repository and network access disabled during solving. [primary, medium confidence] -- https://ornith.ai/ornith_1_5.html (accessed 2026-08-23)
7. The self-improvement loop is a training-time procedure: the model proposes new tasks, generates task-specific scaffolds and produces solution rollouts used for reinforcement learning. [primary, medium confidence] -- https://ornith.ai/ornith_1_5.html (accessed 2026-08-23)

## Key numbers

- **SWE-bench Verified**: 70.6 -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF
- **Four-bit build size (Q4_K_M)**: 5.63 GB -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF
- **Parameters**: 9B -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF
- **Downloads in the first month**: 359,078 -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF
- **Context window**: 262,144 tokens -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF
- **GPQA Diamond**: 86.4 -- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF
- **Benchmark runs averaged**: 5 -- https://ornith.ai/ornith_1_5.html

## Analogy candidates

- **a hatchback that laps the track with the sports cars**: the 9B dense model is the hatchback, the frontier models are the sports cars, SWE-bench Verified is the track. Breaks when: it laps well on this track. Broad world knowledge still scales with size, and a 9B will not know what a 400B knows.

## Misconceptions

- **Myth**: A model that scores like a frontier model must need frontier hardware.  
  **Reality**: The four-bit build is 5.63 gigabytes. That fits a mid-range gaming card with room left for context.
- **Myth**: Self-improving means it keeps learning on your machine.  
  **Reality**: The self-improvement loop ran during training, where the model proposed tasks and generated its own scaffolds for reinforcement learning. What you download is a finished set of weights that does not change.

## Glossary

- **dense model**: a model where every parameter runs for every word, as opposed to a mixture of experts that wakes only a slice
- **GGUF**: the file format local runtimes read, one file holding the weights at a chosen precision
- **Q4_K_M**: a four-bit build, where each stored number keeps fewer bits so the file gets much smaller
- **SWE-bench Verified**: a test where a model has to fix real bugs in real open-source repositories, scored on whether the fix passes the project's own tests
- **context window**: how much text the model can hold in mind at once

## Unverified

- Every benchmark figure is self-reported by Ornith. No independent reproduction was found for the 9B.
- Terminal-Bench 2.1 is 46.2 on the model card and 47.0 in secondary coverage. Do not speak this number without picking one and saying which.
- The GGUF card says the model 'serves on a single 80GB GPU' in BF16 while giving the BF16 size as ~19 GB. The two do not agree; the 80GB line looks inherited from the larger family members.
- The creation date is not stated on the GGUF card. 2026-08-20 comes from secondary coverage of the family launch.
- No local run of this model was performed for this brief, so no first-hand tokens-per-second figure exists.

## Suggested outline

1. Your card has eight gigabytes and you have been told nothing serious fits. 2. This one is five and a half, and it fixes real bugs in real repositories at seventy point six on SWE-bench Verified. 3. The numbers are the lab's own, run five times with the git history stripped and the network off, which is stricter than most, and still their own.

## Sources

- https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF -- ornith-ai/Ornith-1.5-9B-GGUF model card
- https://ornith.ai/ornith_1_5.html -- Ornith-1.5: From Self-Scaffolding to Self-Improvement

## Notes

Format is classic, so between two and five spoken numbers. The file size and the benchmark are the two that carry the video; the download count is a third if a beat needs it. Do not spend the context window and the GPQA figure as well.
