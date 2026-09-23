https://docs.z.ai/guides/vlm/glm-5.3-flash
Accessed: 2026-09-23

# GLM-5.3-Flash/FlashX - Overview - Z.AI Developer Document

## Model Overview

**GLM-5.3-Flash/GLM-5.3-FlashX** is the first native multimodal model in the GLM-5 series, delivering stronger intelligence than GLM-5.2 at an exceptionally low cost.

- **Highly Efficient Hybrid Architecture**

"GLM-5.3-Flash has 320B total parameters with 18B activated. As the first open-source frontier model to combine sparse and linear attention, it significantly cuts computation and serving costs while preserving long-context quality -- reducing attention computation and KV cache by 3.01x and 4.44x versus GLM-5.3."

- **Native Multimodal Visual Coding**: Visual capabilities are built into the coding loop: the model observes interfaces, rendered results, and interaction feedback to continuously test and improve its work.

**GLM-5.3-FlashX** is now live, delivering inference speeds of **200 tokens/s** for faster responses and a smoother experience.

## Input Modality: Video / Image / Text / File
## Output Modality: Text
## Context Length: 1M
## Maximum Output Tokens: 128K

## How to Use

- **Model Code**: glm-5.3-flash / glm-5.3-flashx
- **Parameter Settings**: Text parameters are consistent with GLM-5.3, with support for a 1M-token context window.
- **Recommended Settings**: temperature: 1, top_p: 0.95, and reasoning_effort: max. thinking.type only supports enabled.

## Capabilities

- Thinking Mode: thinking.type only supports enabled; thinking cannot be disabled.
- Function Calling, Context Caching, Structured Output, Visual Understanding.
