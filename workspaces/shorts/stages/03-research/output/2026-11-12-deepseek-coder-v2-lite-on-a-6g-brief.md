---
slug: 2026-11-12-deepseek-coder-v2-lite-on-a-6g
stage: 03-research
topic: "DeepSeek-Coder-V2-Lite on a 6GB GPU: 65 tok/s"
depth: standard
generated_at: 2026-11-12T12:50:00Z
sources: 11
hub: "[[videos/2026-11-12-deepseek-coder-v2-lite-on-a-6g]]"
---

# Research brief: DeepSeek-Coder-V2-Lite on a 6GB GPU: 65 tok/s

## Summary
The pitch in one line: expert pruning, not overclocking, is what puts a 16B-parameter coding model on a 6GB card. The arresting number is the gap rather than the speed: a card that crawls at 4.5 - 10.0 tokens per second on an offloaded official quant reaches 65.6 - 76.3 Tokens/Second once a 4.50 GB container holds every layer in VRAM. The strongest concrete case is a single RTX 4050 laptop GPU showing 4,850MiB of 6,141MiB used with zero layers offloaded to the CPU. What is unverified: the speed is one author's self-reported single-machine run, the pruned container was never re-scored on HumanEval or MBPP, and no other 6GB card was tested. The source conflict: the model card headline says the container is 4.50 GB while the repo's actual file is 4.83 GB.

## Thesis
A community rebuild squeezes the 16B-parameter DeepSeek-Coder-V2-Lite into a 4.50 GB file that fits entirely in 6GB of VRAM and generates at 65.6 - 76.3 Tokens/Second, turning an old gaming card into a local coding box.

## Explanation path
Start with what the viewer's card actually has: 6GB of VRAM, with the desktop already eating a slice of it. Establish that this model is a mixture of experts before any speed number lands: 16B parameters stored, 2.4B consulted per token, and the catch that memory follows the stored number, not the active one. Show the wall: official quantized files run 8.57 GB to 16.0 GB, so pieces get offloaded to the CPU over PCIe and generation drops to 4.5 - 10.0 tokens per second, which is why the viewer wrote the card off. Then the move: quantization alone cannot get under 6GB at usable quality, so the MAPLE rebuild additionally drops the 10 least-used experts per layer, producing a container the card can hold entirely, at which point the same class of card generates at 65.6 - 76.3 Tokens/Second. Prove the model was worth saving with the paper's 81.1% HumanEval Python tie with Llama3-Instruct 70B, then hand over the tonight path: download the GGUF, point an Ollama Modelfile at it, ollama create, and wire it into Continue as the autocomplete model. Close on the honest catch: one self-reported run on one RTX 4050 laptop, and the pruned container has never been re-benchmarked.

## Claims
1. **DeepSeek-Coder-V2-Lite is a Mixture-of-Experts model with 16B total parameters, 2.4B active parameters per token, and a 128k context length.**
   - Source: deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct, https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct
   - Tier: primary | Confidence: high | Accessed: 2026-11-12 | Via: web_extract
   - Quote: "We release the DeepSeek-Coder-V2 with 16B and 236B parameters based on the DeepSeekMoE framework, which has actived parameters of only 2.4B and 21B , including base and instruct models, to the public." and "| DeepSeek-Coder-V2-Lite-Instruct | 16B | 2.4B | 128k |"
2. **The Lite-Instruct model scores 81.1% on HumanEval Python, tying Llama3-Instruct 70B (81.1%), and 68.8% on MBPP+, for a 65.6% multi-language average.**
   - Source: DeepSeek-Coder-V2 paper (HTML v1), Table 3, https://arxiv.org/html/2406.11931v1
   - Tier: primary | Confidence: high | Accessed: 2026-11-12 | Via: web_extract
   - Quote: "DS-Coder-V2-Lite-Instruct16B2.4B81.1%76.6%75.8%76.6%80.5%77.6%74.5%43.0%" and "Llama3-Instruct70B70B81.1%67.7%64.0%69.6%69.8%70.2%65.8%36.1%" and "DS-Coder-V2-Lite-Instruct16B2.4B64.6%47.8%67.3%45.5%62.2%41.6%68.8%65.6%"
3. **Standard GGUF quants of this model do not fit 6GB: the recommended Q4_K_M file is 10.36GB, and even the smallest bartowski file, IQ2_XS at 5.96GB, is labeled very low quality.**
   - Source: Llamacpp imatrix Quantizations of DeepSeek-Coder-V2-Lite-Instruct, https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF
   - Tier: primary | Confidence: high | Accessed: 2026-11-12 | Via: web_extract
   - Quote: "DeepSeek-Coder-V2-Lite-Instruct-Q4_K_M.gguf | Q4_K_M | 10.36GB | Good quality, uses about 4.83 bits per weight, _recommended_." and "DeepSeek-Coder-V2-Lite-Instruct-IQ2_XS.gguf | IQ2_XS | 5.96GB | Very low quality, uses SOTA techniques to be usable."
4. **The MAPLE Sub-5GB rebuild reports a 4.50 GB container running 100% in-VRAM on an RTX 4050 6GB Laptop GPU with 0 layers offloaded to the CPU, generating at 65.6 - 76.3 Tokens/Second.**
   - Source: DeepSeek-Coder-V2-Lite-Instruct MAPLE (Sub-5GB GGUF), https://huggingface.co/AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF
   - Tier: benchmark | Confidence: medium | Accessed: 2026-11-12 | Via: web_extract
   - Quote: "Hardware Residency: 100% In-VRAM on NVIDIA GeForce RTX 4050 6GB Laptop GPU (0 Layers Offloaded to CPU)" and "Inference Speed: 65.6 - 76.3 Tokens/Second (Generation) | 236 - 370 Tokens/Second (Prompt Processing)"
5. **The same page measures the offloaded alternative: splitting the model's 27 MoE layers across PCIe Gen 4 x8 throttles generation to 4.5 - 10.0 tokens per second.**
   - Source: DeepSeek-Coder-V2-Lite-Instruct MAPLE (Sub-5GB GGUF), https://huggingface.co/AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF
   - Tier: benchmark | Confidence: medium | Accessed: 2026-11-12 | Via: web_extract
   - Quote: "Splitting 27 MoE layers across PCIe Gen 4 x8 throttles generation throughput down to 4.5 - 10.0 tokens per second."
6. **The actual file in the MAPLE repo, DeepSeek-Coder-V2-Lite-MAPLE-Sub5GB.gguf, is 4.83 GB, not the 4.50 GB the model card headline states, though still under the 5GB target.**
   - Source: Files in AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF, https://huggingface.co/AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF/tree/main
   - Tier: primary | Confidence: high | Accessed: 2026-11-12 | Via: web_extract
   - Quote: "DeepSeek-Coder-V2-Lite-MAPLE-Sub5GB.gguf 4.83 GB"
7. **Ollama's official library ships deepseek-coder-v2 with the 16b model at 8.9GB and a 160K context window, runnable with one command.**
   - Source: deepseek-coder-v2, Ollama model library, https://ollama.com/library/deepseek-coder-v2
   - Tier: docs | Confidence: high | Accessed: 2026-11-12 | Via: web_extract
   - Quote: "ollama run deepseek-coder-v2" and "deepseek-coder-v2:latest 8.9GB · 160K context window · Text"
8. **Ollama can import any GGUF directly: a Modelfile with the line FROM ./ollama-model.gguf, then ollama create with that Modelfile.**
   - Source: Modelfile Reference, Ollama Docs, https://docs.ollama.com/modelfile
   - Tier: docs | Confidence: high | Accessed: 2026-11-12 | Via: web_extract
   - Quote: "FROM ./ollama-model.gguf" and "ollama create choose-a-model-name -f <location of the file e.g. ./Modelfile>"
9. **Continue's autocomplete can run on a local Ollama model: add it to the config with the autocomplete role.**
   - Source: Continue Autocomplete Setup and Configuration Guide, https://docs.continue.dev/customize/deep-dives/autocomplete
   - Tier: docs | Confidence: high | Accessed: 2026-11-12 | Via: web_extract
   - Quote: "If you'd like to run your autocomplete model locally, we recommend using Ollama." and "roles: - autocomplete"
10. **The code is MIT licensed and the model weights carry the DeepSeek Model License, which supports commercial use.**
    - Source: deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct, https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct
    - Tier: primary | Confidence: high | Accessed: 2026-11-12 | Via: web_extract
    - Quote: "The use of DeepSeek-Coder-V2 Base/Instruct models is subject to the Model License. DeepSeek-Coder-V2 series (including Base and Instruct) supports commercial use."

## Key numbers
| # | Label | Value (verbatim, with unit) | Source | Quote |
|---|-------|-----------------------------|--------|-------|
| 1 | total parameters | 16B | https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct | "actived parameters of only 2.4B" |
| 2 | active parameters per token | 2.4B | https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct | "actived parameters of only 2.4B and 21B" |
| 3 | context length | 128k | https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct | "16B, 2.4B, 128k" |
| 4 | MAPLE container size (card claim) | 4.50 GB | https://huggingface.co/AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF | "Container Size: 4.50 GB (Strictly Sub-5GB Target)" |
| 5 | MAPLE GGUF actual file size | 4.83 GB | https://huggingface.co/AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF/tree/main | "DeepSeek-Coder-V2-Lite-MAPLE-Sub5GB.gguf 4.83 GB" |
| 6 | generation speed, RTX 4050 6GB, 100% in-VRAM | 65.6 - 76.3 Tokens/Second | https://huggingface.co/AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF | "65.6 - 76.3 Tokens/Second (Generation)" |
| 7 | generation speed, official quants, hybrid CPU offload | 4.5 - 10.0 tokens per second | https://huggingface.co/AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF | "throttles generation throughput down to 4.5 - 10.0 tokens per second" |
| 8 | HumanEval Python, DS-Coder-V2-Lite-Instruct | 81.1% | https://arxiv.org/html/2406.11931v1 | "DS-Coder-V2-Lite-Instruct16B2.4B81.1%" |

## Analogy candidates
- **Workshop on call**: A workshop with 64 specialists on payroll; only 6 (plus 2 all-rounders) touch any given job, but all 64 must be present to be callable. Mapping: stored parameters are the payroll (VRAM), active parameters are who actually touches the job; MAPLE retires the 10 least-called specialists so the payroll fits the building. Breaks when: a retired specialist was the only one who knew a rare task, which is exactly the accuracy cost nobody re-measured.
- **Compressed moving truck**: Quantization is packing everything into a smaller truck by using rougher boxes; expert pruning is leaving the least-used furniture behind entirely. Mapping: both shrink the load (file size) so it fits one truck (6GB VRAM) instead of shuttling back and forth (PCIe offload). Breaks when: the rougher boxes or the left-behind furniture turn out to be things you needed, and quality drops in ways the packing list cannot show.

## Misconceptions
- Myth: A model with 16B parameters needs a 16GB+ card. Reality: all 16B do sit in memory, but a 4.50 GB pruned container holds the whole model on a 6GB card with 0 layers offloaded (claims 3, 4, 6).
- Myth: Only 2.4B active parameters means it cannot really code. Reality: the paper puts Lite-Instruct at 81.1% on HumanEval Python, tied with Llama3-Instruct 70B at 81.1% (claim 2).
- Myth: Offloading a few layers to the CPU is a small tax. Reality: the measured cost is a fall from 65.6 - 76.3 Tokens/Second in-VRAM to 4.5 - 10.0 tokens per second across PCIe (claims 4, 5).

## Glossary
- **mixture of experts**: A model design that stores many specialist sub-networks and routes each token through only a few of them.
- **active parameters**: The portion of a model's weights actually consulted to produce one token.
- **quantization**: Storing model weights at lower numeric precision to shrink the file, trading some quality for size.
- **GGUF**: The single-file format that llama.cpp-based tools such as Ollama and LM Studio load local models from.
- **tokens per second**: How many chunks of text a model generates each second; the number that decides whether local feels usable.
- **KV cache**: The working memory a model keeps of everything it has read so far, which grows as context grows.

## Unverified
- The 65.6 - 76.3 Tokens/Second figure is one author's self-reported run on one RTX 4050 laptop GPU and no independent benchmark has reproduced it.
- No HumanEval or MBPP score exists for the pruned MAPLE container, so the accuracy cost of dropping 10 of 64 routed experts per layer is unknown.
- Generation speed on other 6GB-class cards (GTX 1060 6GB, RTX 2060 6GB, RTX 3050 6GB) has not been measured in any page fetched for this brief.
- Tab-autocomplete latency for this container, the time to first token on a single completion, has not been measured anywhere fetched.

## Suggested outline
1. An old 6GB card runs a 16B-parameter coding model at 65.6 - 76.3 Tokens/Second, and the trick is what got deleted, not overclocking.
2. Meet the model: 16B parameters stored, only 2.4B awake per token, 128k context, free for commercial use.
3. Why your card chokes: every expert lives in VRAM, official quants run 8.57 GB to 16.0 GB, the spill crosses PCIe and generation collapses to 4.5 - 10.0 tokens per second.
4. The fix: quantization alone cannot get there, so the rebuild also retires the 10 least-used experts per layer and the whole model plus its KV cache stays on the GPU.
5. Proof the model was worth saving: 81.1% on HumanEval Python, level with Llama3-Instruct 70B.
6. Do it tonight: download the GGUF, write a one-line Modelfile, ollama create, ollama run, then give Continue the autocomplete role.
7. The honest catch: one self-reported laptop run, the pruned model was never re-scored, and your card may differ.

## Viewer situation
Your PC has an aging 6GB graphics card you already decided is too small for real AI, so coding help means a browser tab to a cloud chat bot.

## Has process
`true`
- Download DeepSeek-Coder-V2-Lite-MAPLE-Sub5GB.gguf (4.83 GB) from the Hugging Face repo.
- Install Ollama and save a one-line Modelfile whose FROM line points at the downloaded .gguf file.
- Run ollama create to build the local model from that Modelfile.
- Run ollama run to chat with the model and watch VRAM usage to confirm it stays on the GPU.
- Install the Continue extension in VS Code and add the model to its config with the autocomplete role.

## Objection
One author's self-reported run on one laptop GPU is not a promise about your card, and dropping 10 experts per layer plausibly costs coding accuracy that nobody re-measured.

## Sources
| # | URL | Title | Tier | Fetched via | Accessed |
|---|-----|-------|------|-------------|----------|
| 1 | https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct | deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct | primary | web_extract | 2026-11-12 |
| 2 | https://arxiv.org/abs/2406.11931 | DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence (arXiv:2406.11931) | primary | web_extract | 2026-11-12 |
| 3 | https://arxiv.org/html/2406.11931v1 | DeepSeek-Coder-V2 paper, HTML v1, Table 3 | primary | web_extract | 2026-11-12 |
| 4 | https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF | Llamacpp imatrix Quantizations of DeepSeek-Coder-V2-Lite-Instruct | primary | web_extract | 2026-11-12 |
| 5 | https://huggingface.co/AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF | DeepSeek-Coder-V2-Lite-Instruct MAPLE (Sub-5GB GGUF) | benchmark | web_extract | 2026-11-12 |
| 6 | https://huggingface.co/AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF/tree/main | Files in AmSach/DeepSeek-Coder-V2-Lite-Instruct-MAPLE-Sub5GB-GGUF | primary | web_extract | 2026-11-12 |
| 7 | https://raw.githubusercontent.com/AmSach/maple/master/README.md | MAPLE: Manifold-Activated Pruning of Latent Experts (README) | primary | web_extract | 2026-11-12 |
| 8 | https://ollama.com/library/deepseek-coder-v2 | deepseek-coder-v2, Ollama model library | docs | web_extract | 2026-11-12 |
| 9 | https://docs.ollama.com/modelfile | Modelfile Reference, Ollama Docs | docs | web_extract | 2026-11-12 |
| 10 | https://docs.continue.dev/customize/deep-dives/autocomplete | Continue Autocomplete Setup and Configuration Guide | docs | web_extract | 2026-11-12 |
| 11 | https://news.ycombinator.com/item?id=50463281 | Show HN: DeepSeek-Coder-V2-Lite Under 5GB: 65 TPS 100% In-VRAM on 6GB GPU | community | web_extract | 2026-11-12 |

## Notes
Source conflict on size: the MAPLE model card headline says the container is 4.50 GB but the repo file tree lists DeepSeek-Coder-V2-Lite-MAPLE-Sub5GB.gguf at 4.83 GB; trust the file tree, since it reflects the artifact actually downloaded, and both values stay under the 5GB target and under the roughly 5,340 MB of usable VRAM the card claims after the desktop takes its share. All speed numbers (65.6 - 76.3 Tokens/Second in-VRAM, 4.5 - 10.0 tokens per second offloaded) come from the MAPLE author's own measurements on a single RTX 4050 6GB Laptop GPU with method and nvidia-smi output shown; treat them as one benchmark, not a guarantee, which is why confidence is medium and the reproduction gap is listed under Unverified. The paper was submitted 17 Jun 2024 (arXiv abstract page, fetched this run), matching the Ollama library page showing the model updated about 2 years ago. The ggml-org GGUF repo URL 404'd this session, so bartowski's repo serves as the official-quant size reference.
