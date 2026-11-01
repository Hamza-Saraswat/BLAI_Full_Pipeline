fetched: 2026-11-01
via: web_extract
url: https://tech.ifeng.com/c/8xg9tbvWnnf
title: DeepSeek提出Super-agent架构设计：Router与Worker双层架构_凤凰网 (IT之家 report via ifeng, Oct 31 2026)

This is a direct Chinese-language report of the DeepSeek Harness team's design essay 《Super-agent 设计探索：迈向更自主的 Agent 系统》 ("Exploring Super-agent Design: Towards a More Autonomous Agent System"), published by the official DeepSeek Harness team on Oct 31, 2026.

KEY FACTS (Chinese verbatim + English gloss):
- "一个人通常只能同时跟进 3 至 5 个活跃 Session" -- a person can usually actively follow only 3 to 5 active sessions at once.
- "Super-agent 的任务完成时间 p50 和 p95 分别为 12.4 分钟和 15.7 分钟；中性提示下的单 Session 方案 p95 为 29.5 分钟。" -- Super-agent task completion p50 12.4 minutes, p95 15.7 minutes; neutral-prompt single Session p95 29.5 minutes.
- "实验每次包含约 300 条消息，其中约 20 条为工作请求，每种方案重复运行 5 次" -- each run about 300 messages, about 20 work requests, each scheme run 5 times.
- Caveat in DeepSeek's own words: "这些实验基于合成负载和简化环境，主要评估系统调度与协作能力，并不衡量单个任务的实际执行能力。" -- the experiments use synthetic load and a simplified environment, mainly evaluating system scheduling and coordination ability, and do not measure the actual execution ability of individual tasks.
- Router load test: "Trigger 到达速率从每分钟约 1 条提升至约 40 条时，平均批处理大小从 1.0 增至 2.8，单次请求耗时从 2.5 秒增至 3.9 秒，而单个决定分摊的推理时间从 6.4 秒降至 1.6 秒。"
- Architecture: 双层架构 Router 层 + Worker 层; Router handles human interaction, global context, dispatch; Workers execute in isolated concurrent sessions and report back to Router, which alone talks to the user.
- Four traits of a Super-agent: 连续 (continuous), 高效 (efficient), 主动 (proactive), 持久 (persistent).
- Cloud/local split design (essay, future direction): "计算与持久化状态放在云端，执行环境则可以保留在用户本地设备" with BYOM (Bring Your Own Machine) -- compute and persistent state in the cloud, execution environment on the user's local device, a lightweight daemon.
- "基于上述思路和 DeepSeek Harness 构建的内部 Super-agent 实例已经持续运行" -- an internal Super-agent instance built on DeepSeek Harness has been running continuously (issue reproduction/fix, code review response, Harness iteration).
- The prototype: "提供了名为 dsh-superagent-prototype 的原型实现，但明确指出，该插件用于验证技术路线，并非 DeepSeek 正式产品。" -- the dsh-superagent-prototype is provided to validate the technical route, explicitly NOT an official DeepSeek product.
- Open problems named: Router scaling, months-scale long-term memory, human collaboration outside sessions, A2A between agent instances, security/privacy (prompt injection, on-device credential leaks, cross-device permission risks after a cloud agent touches local devices).
