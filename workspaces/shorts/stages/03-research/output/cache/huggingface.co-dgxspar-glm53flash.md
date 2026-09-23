https://huggingface.co/zai-org/GLM-5.3-Flash
Accessed: 2026-09-23

# zai-org/GLM-5.3-Flash - Hugging Face (rendered model card)

"We introduce GLM-5.3-Flash, the first natively multimodal model in the GLM-5 series. With 320B total parameters and just 18B active parameters, it outperforms GLM-5.2 across benchmarks and real-world workloads at one-tenth the price, while approaching Claude Opus 4.8 on coding and agentic benchmarks."

"GLM-5.3-Flash starts from a newly trained base model... For the first time in the GLM series, we introduce a hybrid architecture combining sparse and linear attention, sharply reducing long-context serving costs while preserving precise long-context capabilities. The model also adopts Manifold-Constrained Hyper-Connections (mHC)."

Serve locally with: SGLang (cookbook), vLLM (recipes), Transformers, KTransformers, Unsloth.

Notes: "GLM-5.3-Flash supports controlling the thinking budget through the `reasoning_effort` parameter, which accepts three levels: `low`, `high`, and `max`."

Model metadata: "Model size 321B params", Tensor type BF16 / F8_E4M3 / F32. Downloads last month: 3,772,365.

Technical report: arXiv 2602.15763 (GLM-5: from Vibe Coding to Agentic Engineering).

Evaluation results: DeepSWE 63.4 *, ExtractBench Mean 80.75 *, Terminal-Bench 2.1: 84.3.

License: not stated in the fetched card text.
