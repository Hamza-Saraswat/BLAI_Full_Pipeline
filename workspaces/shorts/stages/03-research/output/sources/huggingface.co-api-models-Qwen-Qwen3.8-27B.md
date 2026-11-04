# URL: https://huggingface.co/api/models/Qwen/Qwen3.8-27B

HF model repo API metadata (JSON), fetched 2026-11-04:

{"_id":"6a72f2e302294c7d32dd278e","id":"Qwen/Qwen3.8-27B","private":false,"pipeline_tag":"image-text-to-text","library_name":"transformers","tags":["transformers","safetensors","qwen3_5","image-text-to-text","conversational","license:apache-2.0","eval-results","endpoints_compatible","deploy:azure","deploy:sagemaker","region:us"],"downloads":8014877,"likes":19094,"modelId":"Qwen/Qwen3.8-27B","author":"Qwen","sha":"1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0","lastModified":"2026-08-14T15:00:01.000Z","gated":false,"disabled":false,"model-index":null,"config":{"architectures":["Qwen3_5ForConditionalGeneration"],"model_type":"qwen3_5","tokenizer_config":{"bos_token":null,"eos_token":"<|im_end|>","unk_token":null,"pad_token":"<|endoftext|>","chat_template":"{%- set image_count = namespace(value=0) %}\n{%- set video_count = namespace(value=0) %}\n[... long chat template omitted; includes enable_thinking default true, reasoning_effort default xhigh, supported xhigh/medium/low ...]"}},[... "createdAt":"2026-08-05T08:22:59.000Z","safetensors":{"parameters":{"BF16":27781427952},"total":27781427952},"inference":"warm","usedStorage":55618036073}

Key fields extracted verbatim:
- "id": "Qwen/Qwen3.8-27B"
- "author": "Qwen"
- "tags" include "license:apache-2.0"
- "architectures": ["Qwen3_5ForConditionalGeneration"], "model_type": "qwen3_5"
- "pipeline_tag": "image-text-to-text"
- "createdAt": "2026-08-05T08:22:59.000Z"
- "lastModified": "2026-08-14T15:00:01.000Z"
- "safetensors": {"parameters": {"BF16": 27781427952}, "total": 27781427952}
- "downloads": 8014877
- "likes": 19094
- "usedStorage": 55618036073 (bytes)
- eos_token "<|im_end|>", pad_token "<|endoftext|>"
- chat template: enable_thinking default true; reasoning_effort default 'xhigh'; supported types xhigh (default), medium, low
