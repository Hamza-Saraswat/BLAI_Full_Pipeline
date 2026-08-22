# Reconcile: measured numbers versus the script

`shared/pipeline-overview.md` sets the rule: measured numbers in `capture.json` win over the numbers in the brief and the script. This file says how far they may differ before something changes, and what changes.

## Tolerances

| Quantity | Metric keys | Tolerance | Example |
|----------|-------------|-----------|---------|
| tokens per second | `tok_s`, `prompt_tok_s` | 10 % | script says 40, measured 37.5: keep; measured 35: rewrite |
| memory | `vram_gb`, `ollama_vram_gb`, `vram_total_gb` | 5 % | script says 85 GB, measured 88: keep; measured 91: rewrite |
| load time | `load_s` | 20 % | script says 30 s, measured 35: keep; measured 40: rewrite |
| anything else (TTFT, throughput totals) | `ttft_ms`, `total_tok_s`, `tpot_ms` | 10 % | |

Tolerance is relative to the number the script cites. Within tolerance the narration stays as written and only the on-screen digits change to the measured value, so the voice and the screen never disagree by more than the tolerance.

## Procedure (render stage, before the props are written)

1. Collect every number the spec cites: `stat-callout.data.value`, `chart.data.series`, `comparison-table` cells, `on_screen_text` lines with digits, and every `narration` sentence with a spelled-out number. Map each to a `capture.json` entry by the ids named in `<slug>-experiment.md` ("bench1.metrics.tok_s replaces the number in s07").
2. For each pair compute the relative difference. Within tolerance: write the measured value (one decimal for `tok_s`, whole GB for memory, one decimal for seconds) into `data` and `on_screen_text`; leave `narration` alone.
3. Outside tolerance: rewrite the narration sentence that cites it with the measured number written as words, following `brand-vault/voice-rules.md` Hard Constraint 4 (numbers as words, unit and referent in the same sentence, one new number per sentence) and the 20-word cap. Round spoken numbers to two significant figures ("forty-two tokens a second"), keep the on-screen digits exact ("41.7 tok/s"). Update the matching `on_screen_text` and `data` too.
4. Regenerate the narration audio for the changed scenes through `skills/elevenlabs-narration`, which recomputes `captions.json`; then render. A rewritten sentence without new audio is a desync.
5. Record every decision in `<slug>-capture.md` under "Reconcile": scene id, entry id, script value, measured value, difference, action (kept, digits updated, narration rewritten, blocked).

## When to block for a re-script

Set the hub note to `blocked` with `blocked_reason` and stop (the Telegram `rescript:` path takes it from there) when a measurement changes what the episode claims, not just a number:

- A comparison winner flips (`comparison-table` winner cell, "the Spark is faster than the Mac").
- A fit claim flips: the model does not load, `gpu_busy` on the main entry, memory over the box's total.
- The main number moves more than 2x either way (the thesis, the title and the thumbnail concepts all cite it).
- The entry the episode's main number comes from is `failed`, `timeout`, `no_metric` or `refused`.
- More than three narration sentences need rewriting: at that point the script is a draft again.

A re-script keeps the experiment plan and its ids; only the text moves.

## What never changes here

- The spec's scene order and types. A number that needs a new visual is a re-script.
- The capture itself. A surprising number is re-run (`--window any`, same id) only when the run was visibly broken (another process on the GPU, a pull still in progress); otherwise the surprise is the episode.
- The brief's cited sources. Vendor numbers stay attributed as vendor numbers; ours are labelled "measured on the Spark".
