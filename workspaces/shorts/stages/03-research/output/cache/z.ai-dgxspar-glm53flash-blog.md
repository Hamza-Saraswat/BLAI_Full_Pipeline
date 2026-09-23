https://z.ai/blog/glm-5.3-flash
Accessed: 2026-09-23

# GLM-5.3-Flash: Frontier Intelligence, Flash Cost - Z.ai blog (2026-08-26, Research)

"We introduce GLM-5.3-Flash, the first natively multimodal model in the GLM-5 series. With 320B total parameters and just 18B active parameters, it outperforms GLM-5.2 across benchmarks and real-world workloads at one-tenth the price, while approaching Claude Opus 4.8 on coding and agentic benchmarks."

"Before release, we tested GLM-5.3-Flash anonymously as `ox-alpha` on OpenCode and OpenRouter to gather user feedback. It quickly became the most popular model of the week -- with all of this traffic served on Chinese AI chips."

# Competitive Performance at Flash Cost

"GLM-5.3-Flash pushes the Pareto frontier of the Artificial Analysis Intelligence Index v4.1.1, scoring 57 at just $0.045 per task (discounted) -- a level of intelligence previously only available at roughly 10x the cost."

"Across six coding and agentic benchmarks, GLM-5.3-Flash consistently outperforms GLM-5.2, often by a wide margin -- 63.4 vs. 46.2 on DeepSWE v1.1 and 48.8 vs. 26.2 on AutomationBench -- while approaching Claude Opus 4.8 overall."

# Architecture for Extreme Efficiency

"Compared with the GLM-4.5 series, GLM-5.3-Flash is specifically designed for ultra-low-cost inference. Despite a similar total parameter count (320B vs. 355B), it nearly halves both the activated parameter count (18B vs. 32B) and the number of layers (45 vs. 92)."

"To minimize attention costs in long-context scenarios, we use a hybrid architecture combining linear and sparse attention... we introduce IndexPool, which compresses four indexer key vectors into one through weighted pooling."

Base-model table: Activated Params 18B (GL-5.3-Flash-Base) vs 32B (GLM-4.5-Base), 40B (GLM-5-Base), 13B (DeepSeek-V4-Flash-Base); Total Params 320B vs 355B / 744B / 284B.
