# URL: https://ollama.com/library/qwen3.8:27b
qwen3.8:27b — Ollama

5.7M Downloads · Updated 4 days ago

## Qwen3.8 delivers substantial gains across coding, professional work, research, and long-horizon agentic tasks.

Tags: vision, tools, thinking, 27b

`ollama run qwen3.8:27b`

curl http://localhost:11434/api/chat -d '{"model": "qwen3.8:27b", "messages": [{"role": "user", "content": "Hello!"}]}'

## Details (llamacpp variant)

- Updated 1 month ago — 47951e4a6661 · 18GB
- config json: "bos_token_id": 248044, "do_sample": true, "eos_token_id": [248046, 248044]
- quantization json: "producer": {"name": "modelopt", "version": "0.0.0"}, "quantization": {"quant_algo": "MIXED_PRE..."
- 1199 tensors — 18GB
- architectures json: "architectures": ["Qwen3_5ForConditionalGeneration"], "image_token_id": 248056
- license: Apache License Version 2.0
- params: {"min_p": 0, "presence_penalty": 0, "repeat_penalty": 1, "temperature": 1, "top_k": 20, "top_p": 0.95}

## Tags / model blobs (mlx and llamacpp listed)

llamacpp tag (aaee06c39dcf · 18GB):
- model: arch qwen35 · parameters 27.3B · quantization Q4_K_M · 17GB
- projector: arch clip · parameters 461M · quantization BF16 · 931MB
- license: Apache License Version 2.0
- params: {"draft_num_predict": 4, "min_p": 0, "presence_penalty": 0, "repeat_penalty": 1, ...}

## Readme highlights

Qwen3.8-27B features the following enhancements:
- **Core Capabilities**: Comprehensive improvements across coding, professional work, research, and long-horizon agentic tasks.
- **Agent Execution**: Stronger autonomous planning and better handling of environment feedback, leading to more reliable end-to-end task completion.
- **Downstream Compatibility**: Broader support for popular harnesses and development tools, making it easier to integrate into your existing stack.
- **Flexible Thinking Control**: Thinking mode is on by default and can be disabled per request; reasoning depth can be tuned with `reasoning_effort`, and reasoning context from historical messages is retained via `preserve_thinking`.
- **Vision-Language Understanding**: Native support for image and video understanding, from STEM diagrams and documents to hour-scale videos.

Benchmark charts (images): text performance, VL performance.
