#!/usr/bin/env python3
"""Scoring for the trend radar: signal normalization, recency decay, product extraction,
the why-now rubric, and lane or series assignment.

rules/scoring.md is the readable twin of this module. Change the two together.
"""
from __future__ import annotations

import math
import re

HALF_LIFE_HOURS = 48.0
DECAY_FLOOR = 0.05
PRODUCT_BONUS = 0.15
BASE_SCALE = 0.85                 # leaves room for the bonus: only a named product can reach 100
CROSS_SOURCE_BOOST = 5            # score points per extra source that carried the same item
SOURCE_WEIGHT = {"reddit": 1.0, "hn": 1.0, "hf": 0.9, "github": 1.0, "youtube": 0.9, "firecrawl": 0.8}
BONUS_KINDS = {"hardware", "model", "runtime", "format", "cloud"}   # vendors earn no bonus

# (canonical name, kind, pattern). Matched case-insensitively against title + summary.
PRODUCTS = [
    ("DGX Spark", "hardware", r"dgx[ -]?spark"),
    ("DGX Station", "hardware", r"dgx[ -]?station"),
    ("GB10", "hardware", r"\bgb10\b"),
    ("Grace Blackwell", "hardware", r"grace[ -]blackwell"),
    ("Blackwell", "hardware", r"\bblackwell\b"),
    ("RTX 5090", "hardware", r"\b(?:rtx[ -]?)?5090\b"),
    ("RTX 5080", "hardware", r"\b(?:rtx[ -]?)?5080\b"),
    ("RTX 5070", "hardware", r"\b(?:rtx[ -]?)?5070(?: ?ti)?\b"),
    ("RTX 4090", "hardware", r"\b(?:rtx[ -]?)?4090\b"),
    ("RTX 4080", "hardware", r"\b(?:rtx[ -]?)?4080\b"),
    ("RTX 3090", "hardware", r"\b(?:rtx[ -]?)?3090\b"),
    ("RTX 3060", "hardware", r"\b(?:rtx[ -]?)?3060\b"),
    ("RTX PRO 6000", "hardware", r"rtx[ -]?pro[ -]?6000"),
    ("H100", "hardware", r"\bh100\b"),
    ("H200", "hardware", r"\bh200\b"),
    ("B200", "hardware", r"\bb200\b"),
    ("B300", "hardware", r"\bb300\b"),
    ("Jetson", "hardware", r"\bjetson\b"),
    ("Apple M4", "hardware", r"\b(?:apple )?m4(?: (?:pro|max|ultra))?\b"),
    ("Apple M5", "hardware", r"\b(?:apple )?m5(?: (?:pro|max|ultra))?\b"),
    ("Mac Studio", "hardware", r"mac[ -]?studio"),
    ("Mac mini", "hardware", r"mac[ -]?mini"),
    ("MacBook", "hardware", r"\bmacbook\b"),
    ("Strix Halo", "hardware", r"strix[ -]?halo"),
    ("Ryzen AI", "hardware", r"ryzen[ -]?ai"),
    ("Radeon", "hardware", r"\bradeon\b"),
    ("Intel Arc", "hardware", r"intel[ -]?arc\b"),
    ("Raspberry Pi", "hardware", r"raspberry[ -]?pi"),
    ("Qwen", "model", r"\bqwen"),
    ("DeepSeek", "model", r"deep[ -]?seek"),
    ("Llama", "model", r"\bllama\b(?!\.cpp|-server|-cli|-bench|-swift)"),
    ("Mistral", "model", r"\bmistral\b"),
    ("Mixtral", "model", r"\bmixtral\b"),
    ("Gemma", "model", r"\bgemma\b"),
    ("GLM", "model", r"\bglm[ -]?\d"),
    ("Nemotron", "model", r"\bnemotron\b"),
    ("Phi", "model", r"\bphi[ -]?\d"),
    ("Kimi", "model", r"\bkimi\b"),
    ("MiniMax", "model", r"\bminimax\b"),
    ("gpt-oss", "model", r"\bgpt[ -]?oss\b"),
    ("Grok", "model", r"\bgrok\b"),
    ("Whisper", "model", r"\bwhisper\b(?!\.cpp)"),
    ("Kokoro", "model", r"\bkokoro\b"),
    ("FLUX", "model", r"\bflux[ .-]?(?:\d|dev|schnell|kontext)"),
    ("Stable Diffusion", "model", r"stable[ -]diffusion"),
    ("Wan", "model", r"\bwan[ -]?\d"),
    ("Hunyuan", "model", r"\bhunyuan"),
    ("SmolLM", "model", r"\bsmollm"),
    ("Granite", "model", r"\bgranite\b"),
    ("OLMo", "model", r"\bolmo\b"),
    ("ChatGPT", "cloud", r"chat[ -]?gpt"),
    ("GPT-5", "cloud", r"\bgpt[ -]?5(?:\.\d)?\b"),
    ("Claude", "cloud", r"\bclaude\b"),
    ("Gemini", "cloud", r"\bgemini\b"),
    ("Copilot", "cloud", r"\bcopilot\b"),
    ("llama.cpp", "runtime", r"llama\.cpp"),
    ("vLLM", "runtime", r"\bvllm\b"),
    ("Ollama", "runtime", r"\bollama\b"),
    ("LM Studio", "runtime", r"lm[ -]?studio"),
    ("SGLang", "runtime", r"\bsglang\b"),
    ("Unsloth", "runtime", r"\bunsloth\b"),
    ("TensorRT", "runtime", r"tensorrt(?:[ -]?llm)?"),
    ("CUDA", "runtime", r"\bcuda\b"),
    ("MLX", "runtime", r"\bmlx\b"),
    ("MLC", "runtime", r"\bmlc(?:[ -]?llm)?\b"),
    ("exo", "runtime", r"\bexo\b"),
    ("Open WebUI", "runtime", r"open[ -]?webui"),
    ("ComfyUI", "runtime", r"comfy[ -]?ui"),
    ("whisper.cpp", "runtime", r"whisper\.cpp"),
    ("ExLlama", "runtime", r"\bexllama"),
    ("LocalAI", "runtime", r"\blocalai\b"),
    ("Docker Model Runner", "runtime", r"docker model runner"),
    ("GGUF", "format", r"\bgguf\b"),
    ("NVFP4", "format", r"\bnvfp4\b"),
    ("MXFP4", "format", r"\bmxfp4\b"),
    ("FP8", "format", r"\bfp8\b"),
    ("FP4", "format", r"\bfp4\b"),
    ("AWQ", "format", r"\bawq\b"),
    ("GPTQ", "format", r"\bgptq\b"),
    ("NVIDIA", "vendor", r"\bnvidia\b"),
    ("AMD", "vendor", r"\bamd\b"),
    ("Intel", "vendor", r"\bintel\b"),
    ("Apple", "vendor", r"\bapple\b"),
    ("Meta", "vendor", r"\bmeta\b"),
    ("Google", "vendor", r"\bgoogle\b"),
    ("Microsoft", "vendor", r"\bmicrosoft\b"),
    ("OpenAI", "vendor", r"\bopenai\b"),
    ("Anthropic", "vendor", r"\banthropic\b"),
    ("Hugging Face", "vendor", r"hugging[ -]?face"),
    ("Alibaba", "vendor", r"\balibaba\b"),
    ("Moonshot", "vendor", r"\bmoonshot\b"),
    ("Zhipu", "vendor", r"\bzhipu\b|\bz\.ai\b"),
    ("xAI", "vendor", r"\bxai\b"),
]
_PRODUCT_RES = [(name, kind, re.compile(pattern, re.I)) for name, kind, pattern in PRODUCTS]

# Why-now rubric: the first matching kind wins, in this order (text sources only; GitHub
# releases and new Hugging Face models are "Shipped" by construction).
WHY_NOW = [
    ("Broke", r"\b(broke|broken|breaks?(?![ -]even)|breaking|bug|regression|crash(?:es|ed)?|fail(?:s|ed|ure)?|"
              r"not working|security|cve-\d|vulnerab|outage|revert|pin to|workaround|oom\b)"),
    ("Shipped", r"\b(releas\w*|launch\w*|announc\w*|introduc\w*|unveil\w*|ships?|shipped|is out|"
                r"are out|now available|open[ -]?weights?|weights (?:are )?(?:out|released|up|on)|"
                r"drops?\b|dropped|new model|day[ -]0|ga\b|show hn)"),
    ("Measured", r"\b(benchmark\w*|tok(?:ens)?/s|tokens per second|throughput|latency|faster|slower|"
                 r"speedup|\d+(?:\.\d+)?x\b|\d+ ?%|measured|tested|testing|compared|comparison|"
                 r"vs\.?|versus|side by side|results|numbers|ran the same)"),
    ("Changed", r"\b(updat\w*|upgrad\w*|chang\w*|deprecat\w*|pric\w*|cheaper|"
                r"now (?:supports?|runs?|works?|fine[ -]?tunes?|trains?|fits?|ships?)|"
                r"support for|adds?|added|enables?|firmware|driver|migrat\w*|default|new version|"
                r"patch|policy|regulation|obligations|act\b|shortage)"),
]
_WHY_NOW_RES = [(kind, re.compile(pattern, re.I)) for kind, pattern in WHY_NOW]

LANE_ORDER = ["news-react", "myth-bust", "comparison", "how-to", "explainer", "enterprise-privacy"]
SERIES_ORDER = ["local-ai-for-dummies", "my-dgx-spark-projects", "benchmarks",
                "inference-engineering-at-home", "dgx-spark-specific", "beyond-llms"]

LANE_RULES = [
    ("comparison", r"\bvs\.?\b|versus|compared to|comparison|head[ -]to[ -]head|side by side|"
                   r"which (?:one|is better)|better than|killer\?|worth it over|instead of|ahead of|"
                   r"\bbeats\b|outperforms"),
    ("how-to", r"\bhow to\b|\bguide\b|tutorial|step[ -]by[ -]step|\binstall|\bsetup\b|set up|"
               r"getting started|in \d+ minutes|walkthrough|here'?s the stack|the stack\b"),
    ("enterprise-privacy", r"privacy|private data|gdpr|hipaa|complian|on[ -]prem|air[ -]?gapp|"
                           r"enterprise|law firm|clinic|hospital|sovereign|eu ai act|data leak|"
                           r"leak(?:ed|s)? (?:data|prompts)|self[ -]hosted|regulat|obligations"),
    ("myth-bust", r"\bmyth|actually|don'?t need|do not need|you don'?t|overrated|is not free|"
                  r"not as (?:fast|good|cheap)|the truth|really (?:need|faster|cheaper)|"
                  r"still (?:run|worth)|\bwrong\b|debunk|surprising|\bno, |the math\b|finally cheaper"),
    ("explainer", r"explained|explain|what is|what are|why (?:does|do|is|are|your|local)|how does|"
                  r"how do\b|why \w+ matters|understanding|deep dive|plain (?:english|explanation)|"
                  r"in \d+ seconds"),
]
_LANE_RES = [(lane, re.compile(pattern, re.I)) for lane, pattern in LANE_RULES]

BEYOND_LLM_TAGS = {"text-to-speech", "automatic-speech-recognition", "text-to-image",
                   "text-to-video", "image-to-text"}
SERIES_RULES = [
    ("beyond-llms", r"text[ -]to[ -]speech|\btts\b|speech|whisper|\bvoice\b|\basr\b|transcri|"
                    r"image generation|text[ -]to[ -]image|text[ -]to[ -]video|video model|"
                    r"diffusion|\bflux\b|\bwan[ -]?\d|kokoro|comfyui|image[ -]to[ -]text|\bocr\b"),
    ("dgx-spark-specific", r"firmware|driver|connectx|two (?:dgx )?sparks|dual[ -]spark|"
                           r"2 dgx sparks|\bgb10\b|spark os|playbook|nvidia container|nccl|"
                           r"200 ?gbe|cuda graphs? on gb10|sm_121"),
    ("my-dgx-spark-projects", r"fine[ -]?tun|finetun|\blora\b|unsloth|\bagent|\brag\b|i built|"
                              r"built a|project|home ?lab|here'?s the stack"),
    ("benchmarks", r"benchmark|tok(?:ens)?/s|tokens per second|throughput|latency|\bvs\.?\b|"
                   r"versus|faster|slower|\d+(?:\.\d+)?x\b|measured|side by side|compared|"
                   r"ran the same|results"),
    ("inference-engineering-at-home", r"quantiz|\bgguf\b|\bawq\b|\bfp8\b|\bfp4\b|nvfp4|kv cache|"
                                      r"batch|context (?:length|window)|speculative|flash attention|"
                                      r"kernel|cuda graph|offload|serving|vllm|llama\.cpp|sglang|"
                                      r"tensorrt|ollama|lm studio|exllama|\bmlx\b|\bexo\b"),
    ("local-ai-for-dummies", r"explained|what is|what are|beginner|for dummies|basics|\bintro|"
                             r"plain|why (?:does|do|is|are|your|local)|understanding|how does|"
                             r"cheaper than|the math"),
]
_SERIES_RES = [(series, re.compile(pattern, re.I)) for series, pattern in SERIES_RULES]


def log_norm(value, full: float) -> float:
    """0..1 on a log scale; reaches 1.0 at `full` and stays there."""
    value = max(0.0, float(value or 0))
    return min(1.0, math.log10(1 + value) / math.log10(1 + full))


def signal(raw: dict) -> tuple[float, dict]:
    """Per-source engagement normalized to 0..1, plus the parts that made it."""
    source = raw.get("source")
    if source == "reddit":
        parts = {"upvotes": log_norm(raw.get("score"), 1000), "comments": log_norm(raw.get("num_comments"), 300)}
        value = 0.7 * parts["upvotes"] + 0.3 * parts["comments"]
    elif source == "hn":
        parts = {"points": log_norm(raw.get("points"), 300), "comments": log_norm(raw.get("num_comments"), 150)}
        value = 0.7 * parts["points"] + 0.3 * parts["comments"]
    elif source == "hf":
        parts = {"trending": log_norm(raw.get("trendingScore"), 2000), "likes": log_norm(raw.get("likes"), 1000),
                 "downloads": log_norm(raw.get("downloads"), 1000000)}
        value = 0.5 * parts["trending"] + 0.5 * max(parts["likes"], parts["downloads"])
    elif source == "github":
        parts = {"release": 0.4 if raw.get("prerelease") else 0.6,
                 "notes": 0.1 if len(raw.get("body") or "") >= 300 else 0.0}
        value = parts["release"] + parts["notes"]
    elif source == "youtube":
        parts = {"views_per_hour": log_norm(raw.get("views_per_hour"), 2000), "views": log_norm(raw.get("views"), 500000)}
        value = 0.6 * parts["views_per_hour"] + 0.4 * parts["views"]
    else:                                   # firecrawl and anything new: flat prior
        parts = {"news": 0.5}
        value = 0.5
    return round(min(1.0, value), 3), {k: round(v, 3) for k, v in parts.items()}


def decay(age_hours, window_hours: int) -> float:
    """Half-life HALF_LIFE_HOURS with a floor; unknown dates sit at the window's midpoint."""
    age = float(window_hours) / 2.0 if age_hours is None else float(age_hours)
    return round(max(DECAY_FLOOR, 0.5 ** (age / HALF_LIFE_HOURS)), 4)


def products(text: str) -> tuple[list[str], set]:
    """Canonical product names in order of first appearance, plus the set of their kinds."""
    found = []
    for name, kind, regex in _PRODUCT_RES:
        match = regex.search(text or "")
        if match:
            found.append((match.start(), name, kind))
    found.sort()
    names, kinds = [], set()
    for _, name, kind in found:
        if name not in names:
            names.append(name)
            kinds.add(kind)
    return names, kinds


def product_bonus(kinds: set) -> float:
    return PRODUCT_BONUS if kinds & BONUS_KINDS else 0.0


def why_now_kind(raw: dict, text: str) -> str:
    if raw.get("source") in ("github", "hf"):
        if raw.get("source") == "github" and _WHY_NOW_RES[0][1].search(raw.get("body") or ""):
            return "Shipped with a known break"
        return "Shipped"
    for kind, regex in _WHY_NOW_RES:
        if regex.search(text or ""):
            return kind
    return "Discussed"


def compact(number) -> str:
    number = float(number or 0)
    if number >= 1000000:
        return "%.1fM" % (number / 1000000)
    if number >= 1000:
        return "%.1fk" % (number / 1000)
    return "%d" % number


def age_text(age_hours) -> str:
    if age_hours is None:
        return "date unknown (this week)"
    if age_hours < 48:
        return "%d h ago" % round(age_hours)
    return "%.0f d ago" % (age_hours / 24.0)


def why_now_text(kind: str, raw: dict, age_hours) -> str:
    source = raw.get("source")
    if source == "reddit":
        evidence = "r/%s thread, %s upvotes, %s comments" % (raw.get("subreddit"), compact(raw.get("score")), compact(raw.get("num_comments")))
    elif source == "hn":
        evidence = "%s points, %s comments on HN" % (compact(raw.get("points")), compact(raw.get("num_comments")))
    elif source == "hf":
        evidence = "new on Hugging Face (%s), %s likes, %s downloads, trending score %s" % (
            raw.get("pipeline_tag"), compact(raw.get("likes")), compact(raw.get("downloads")), compact(raw.get("trendingScore")))
    elif source == "github":
        evidence = "%s %s released%s" % (raw.get("repo"), raw.get("tag"), " (pre-release)" if raw.get("prerelease") else "")
    elif source == "youtube":
        evidence = "%s views, %s/h on %s" % (compact(raw.get("views")), compact(raw.get("views_per_hour")), raw.get("channel"))
    else:
        evidence = "in this week's web news for %r" % (raw.get("query") or "news")
    return "%s: %s, %s" % (kind, evidence, age_text(age_hours))


def lane(title: str, summary: str, kinds: set, product_names: list[str]) -> str:
    """Shorts lane. A comparison is declared in the title; the other lanes may read the summary."""
    text = (title or "") + " " + (summary or "")
    hits = {name for name, regex in _LANE_RES if regex.search(text)}
    versus = _LANE_RES[0][1].search(title or "") is not None
    named = [p for p in product_names if p not in ("CUDA", "NVIDIA", "AMD", "Intel", "Apple", "Meta", "Google")]
    if versus and len(named) >= 2:
        return "comparison"
    for candidate in ("enterprise-privacy", "how-to", "myth-bust", "explainer"):
        if candidate in hits:
            return candidate
    if versus:
        return "comparison"
    return "news-react"


def series(text: str, kinds: set, pipeline_tag: str | None, product_names: list[str]) -> str:
    """Long-form series. Non-text models go to beyond-llms before any keyword rule fires."""
    if pipeline_tag in BEYOND_LLM_TAGS:
        return "beyond-llms"
    hits = [name for name, regex in _SERIES_RES if regex.search(text or "")]
    if "dgx-spark-specific" in hits and "DGX Spark" in product_names:
        return "dgx-spark-specific"
    for candidate in ("beyond-llms", "my-dgx-spark-projects", "benchmarks",
                      "inference-engineering-at-home", "local-ai-for-dummies", "dgx-spark-specific"):
        if candidate in hits:
            return candidate
    if "model" in kinds:
        return "benchmarks"
    if "runtime" in kinds or "format" in kinds:
        return "inference-engineering-at-home"
    return "local-ai-for-dummies"

# --- relevance ------------------------------------------------------------
# A radar item must be about running AI on your own hardware. Hacker News ranks by
# points, so without this gate a marathon medal story and a crypto disappearance
# scored 38 and 49 on the 2026-08-23 live run purely on discussion volume.
# An item passes when it names a known product OR carries a topic term.
TOPIC_TERMS = [
    r"\bl\.?l\.?m\b", r"\bslm\b", r"local ai", r"local model", r"on-?device", r"self-?host",
    r"\bgpu\b", r"\bvram\b", r"\bnpu\b", r"\btpu\b", r"unified memory", r"memory bandwidth",
    r"quantiz", r"\bgguf\b", r"\bfp(?:8|4|16)\b", r"\bint(?:4|8)\b", r"\bkv[ -]?cache\b",
    r"\btoken(?:s|/s| per second)\b", r"context window", r"fine[- ]?tun", r"\blora\b",
    r"open[- ]weights?", r"open[- ]source model", r"inference", r"\bprompt\b", r"embedding",
    r"transformer", r"mixture of experts", r"\bmoe\b", r"diffusion", r"text[- ]to[- ]speech",
    r"speech[- ]to[- ]text", r"\bagent(?:s|ic)?\b", r"\brag\b", r"vector (?:db|database|store)",
    r"\bmodel weights?\b", r"\bcheckpoint\b", r"\bbenchmark\b", r"\bai\b",
]
_TOPIC_RES = [re.compile(rx, re.I) for rx in TOPIC_TERMS]


def relevance(text: str, product_names) -> tuple[bool, str]:
    """True when the item is about local AI. Returns (ok, reason)."""
    if product_names:
        return True, "product:" + product_names[0]
    for rx in _TOPIC_RES:
        m = rx.search(text or "")
        if m:
            return True, "topic:" + m.group(0).lower()
    return False, "no product and no topic term"
