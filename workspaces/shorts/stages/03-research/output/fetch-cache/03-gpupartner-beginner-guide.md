# 03 -- gpupartner.com beginner guide (the HN front-page thread's target)

URL: https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth
Accessed: 2026-11-23 | Via: web_extract | Tier: docs (named author Jerry James, dated Nov 22, 2026; full-page cached at ~/.hermes/cache/web/www.gpupartner.com-a9f7ae49b5.md)

"A beginner's guide to Local AI with Inkling, Qwen, and Unsloth" -- "We have AI at home! Set up your own free personal ChatGPT on your PC with Unsloth and Inkling or Qwen."

## Verbatim numbers
- "Once you have the hardware sorted, it takes about 10-15 minutes (excluding download times)."
- "I'm using an RTX 5090 with 32GB VRAM for this setup."
- "As a rough guide, 8-12GB of VRAM handles smaller 9B-12B models, while 32GB comfortably runs 27B-35B models with plenty of room for long conversations."
- "The full-size Qwen model sits at around 56GB and won't really fit on a consumer graphics card unless you're running a Mac with unified memory."
- "a hilariously overpriced RTX 5090 (remember when $1,999 felt too high?) is unfortunately still not a terrible 'deal' these days"
- "On an RTX 5060 Ti 16GB, our calculator puts Qwen3.6-35B at about 47 tokens per second this way."
- Qwen3.8-27B memory at 128K context by precision: "16-bit 61.0 GB, 8-bit 36.7, 6-bit 30.4, 5-bit 27.6, 4-bit 24.9, 3-bit 21.9, 2-bit 18.9" with "A line marks a 32 GB card; 6-bit and below fit under it."
- "Thinking Machines Lab released it on November 17, 2026: 26.4B parameters, Apache 2.0, vision support and a 1M-token context. Unsloth's recommended file, UD-Q4_K_XL, is 17.6 GB. That is within 0.1 GB of the Qwen3.8-27B file in this guide, so it sits on a 32GB card the same way and leaves about 14GB for context."
- "Inkling 2 Mini is a mixture-of-experts model with 5.4B parameters active, so the 4-bit file also runs on a 16 GB card with the remainder in system RAM, a little slower."
- Inkling 2 Mini memory table: "2-bit 10-11 GB (12 GB card); 3-bit 13-15 GB (16 GB card); 4-bit (recommended) 17-18 GB (24 GB card); 8-bit (lossless) 24 GB (32 GB card)". "Those figures are Unsloth's."
- "Those figures are Unsloth's. They count RAM and VRAM together and cover the model alone, so a long context needs more."

## Explainer material (audience-appropriate)
- Quantization: "Quantization shrinks a model by compressing weights and moving to a lower precision. You basically trade some accuracy for a model that actually fits on your GPU and runs faster." Photo analogy: "The same photo stored at 8, 4 and 2 bits per pixel. A model's weights lose detail the same way going from Q8 to Q4 to Q2."
- "You'll find that certain types of workloads don't really care and give similar outputs, while others may be nearly unusable."
- Context window: "how much of the conversation the model can keep in mind at once"
- MoE: "Models marked MoE (mixture of experts) only run a few billion of their parameters for each token. They keep a decent speed on a smaller card with the rest held in system RAM, which is why a 35B model sits in the 16 GB row."
- Setup steps: "Install Unsloth Desktop, download a quantized AI model that fits your GPU's VRAM, set your context size, and turn on LAN access so everyone at home can use it."
- Why people switch: "OpenAI and Anthropic have displayed a pattern of dropping model quality in the 'latest' version and controlling exactly what you're allowed to run on their models. Add to this ballooning costs and privacy concerns..."
- Limits stated: "Not with this setup alone. Everything so far is limited to your local home network." and "the PC needs to stay on with Unsloth running for anyone to reach it."

## Conflict
- This guide says Inkling 2 Mini was "released on November 17, 2026"; the Thinking Machines model card says "Date of release: November 20, 2026". Record both; trust the model card (first-party) and note the guide may cite an earlier announce date.
