fetched: 2026-11-01
via: web_extract
url: https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart
title: Use the Web UI | DeepSeek Harness

KEY FACTS (verbatim):
- "Start the Web UI through the root README; the command prints its URL. The `dsh` process uses its invoking directory as the default filesystem location, but a fresh Web UI has no selected workspace until you add one."
- "Open Settings -> Models, enter a DeepSeek API key, and save it. The model route becomes usable immediately without restarting the server."
- "The model configuration guide covers other providers and custom OpenAI-compatible endpoints."
- "Click Choose workspace, add the project directory where you started `dsh`, and select it."
- "The agent can read and edit workspace files, run commands, delegate work, and maintain a plan. The Web UI asks before operations that require approval under the active permission policy."

url2: https://deepseek-harness.github.io/deepseek-harness/en/guide/providers
title2: Configure models | DeepSeek Harness

KEY FACTS (verbatim):
- "Switch the card to Custom model API for a relay, a company gateway, a self-hosted server, or any provider absent from the installed catalog. Supply a lowercase Provider ID, base URL, API protocol, credential, and at least one model."
- "The API protocol must be the one your gateway speaks, and the picker offers three: OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages, stored in the active profile's `cordis.patch.yml` as `openai-completions`, `openai-responses`, and `anthropic-messages`."
- "Under Model catalog, choose Fetch available models to ask the endpoint which models it serves."
- "Model discovery calls the OpenAI-compatible `GET /models` endpoint; enter models manually for endpoints that do not provide it."
- "Model changes take effect on the next request without restarting the server."
- Built-in third-party provider ids: "the list shows provider ids such as `anthropic`, `openai`, `moonshotai` for Kimi, or `zai` for GLM"
- Keys stored in `$DSH_HOME/.credentials.yaml`; settings retain only a credential reference. Keys are write-only / redacted.
- Config file: `$DSH_HOME/profiles/<profile>/cordis.patch.yml`; for `dsh web` the profile is `web`.
- Troubleshooting names OpenAI-compat quirks: `compat.supportsDeveloperRole: false`, `compat.maxTokensField: max_tokens` for gateways whose request shape differs from OpenAI's.
- IMPLICATION for local: a self-hosted OpenAI-compatible server (llama.cpp / Ollama / vLLM / LM Studio style) is a supported first-class case via Custom model API.
