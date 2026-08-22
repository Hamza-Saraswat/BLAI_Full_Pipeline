# Allowlist

`allowlist.json` is the whole policy; this file explains it. `capture.py` checks every command in a plan before running any of them. A plan with one refused command runs nothing, so a typo at 03:00 cannot half-execute an experiment.

## How a command is judged

1. Deny patterns run first against the raw string. Any hit refuses the command and the message names the rule (`sudo`, `rm-rf`, `pipe-to-shell`, ...).
2. The string is split with shell quoting rules, then into segments at `|`, `||`, `&&`, `;`. Each segment's first token must be a family's `first_token`; after a pipe it may also be one of the `filters` (`head`, `tail`, `grep`, `jq`, `wc`, `sort`, `cut`, `tr`, `tee`, `cat`).
3. Family checks: `subcommands` (the second token), `arg_pattern` (the second token, used for the benchmark scripts), `url_pattern` (every URL in the command, used for curl), `image_patterns` and `deny_flags` (docker).
4. Redirections (`>`, `>>`, `2>`, `&>`, `tee`, `curl -o`) may only target `/dev/null` or a path inside the capture `--out` directory. `curl -O` is refused outright.
5. Inline environment assignments (`FOO=bar cmd`, `env FOO=bar cmd`) are refused; settings live in `build/.env`.

## Families

| Family | First token | Allowed | Why it is here |
|--------|-------------|---------|----------------|
| `ollama` | `ollama` | `run`, `list`, `ps`, `pull`, `show` | the runtime most viewers use; `run --verbose` prints the eval rate, `ps` proves GPU placement |
| `llama-server` | `llama-server` | any flags | llama.cpp's HTTP server for OpenAI-compatible benchmarks |
| `llama-cli` | `llama-cli` | any flags | one-shot generation with the timing block |
| `llama-bench` | `llama-bench` | any flags | the canonical pp/tg table |
| `vllm` | `vllm` | `serve`, `bench` | vLLM serving and its own benchmark |
| `python-benchmarks` | `python3` | only `skills/dgx-capture/benchmarks/<name>.py` | our two benchmark scripts; nothing else in Python |
| `nvidia-smi` | `nvidia-smi` | any flags | memory and utilization readings |
| `docker-run` | `docker` | `run` with images `nvcr.io/nvidia/*`, `vllm/vllm-openai`, `ollama/ollama`; no `--privileged`; no mounts of `/`, `/etc`, `/root`, `/home`, `/usr`, `/var`, `/boot` | NGC containers and the two runtime images |
| `huggingface-cli`, `hf` | `huggingface-cli`, `hf` | `download` | weights |
| `curl-local` | `curl` | URLs on `localhost`, `127.0.0.1` or `[::1]` only; `-o` only inside the capture dir | hitting a local inference endpoint |
| `lscpu`, `free`, `df`, `uname` | same | any flags | facts for the on-screen spec card |

GPU families (`gpu: true` in the JSON): ollama, llama.cpp, vllm, docker, the benchmark scripts. They get the free-memory check (`gpu_min_free_gb`, default 8 GB). A plan entry can force it either way with `"gpu": true|false`.

## Denied patterns

| Rule | Catches | Why |
|------|---------|-----|
| `sudo` | `sudo ...` anywhere in the string | nothing in a capture needs root |
| `rm-rf`, `rm` | `rm -rf`, `rm -fr`, `rm -r -f`, any `rm` | captures never delete |
| `pipe-to-shell` | `| sh`, `| bash`, `| python3`, `| sudo bash` | remote-execution pattern |
| `wget` | `wget` | downloads go through `hf`, `huggingface-cli`, `ollama pull` |
| `ssh` | `ssh`, `scp`, `sftp`, `rsync` | no remote hosts from a capture |
| `dd`, `mkfs` | raw device writes and filesystem creation | obvious |
| `backticks`, `command-substitution`, `process-substitution` | `` ` ``, `$(`, `<(`, `>(` | they hide the real command from the allowlist |
| `eval-exec` | `eval`, `exec`, `source`, `nohup`, `setsid`, `systemctl`, `reboot`, `shutdown`, `kill`, `pkill`, `killall` | process and system control are not captures |
| `chmod-chown` | `chmod`, `chown`, `mount`, `umount`, `apt`, `apt-get`, `pip`, `pip3`, `npm` | installs belong to `build/install.sh` |
| `redirect-outside-capture-dir` | `> /etc/x`, `>> ~/y`, `tee /tmp/z` | the capture dir is the only writable place |

## Adding a family

1. Add an object to `families` in `allowlist.json`: `name`, `first_token`, and the narrowest of `subcommands`, `arg_pattern`, `url_pattern`, `image_patterns`. Set `gpu: true` if it loads a model. Write the `why`.
2. Add a fake output for `--dry-run` under `fixtures/fake-outputs/` and map it in `fake_output()` in `scripts/capture.py`; add the metric regex to `extract_metrics()` if the tool prints a number the episode will cite.
3. Add a row to the table above and, if useful, an entry to `fixtures/plan-example.md`.
4. Run the dry run and the negative test:

```
python3 skills/dgx-capture/scripts/capture.py --plan skills/dgx-capture/fixtures/plan-example.md --out /tmp/cap-test --dry-run --window any
```

A family is never added for convenience alone: the question is what happens if a plan produced at 07:00 by a model with a bad brief contains the worst possible argument to it.
