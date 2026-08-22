# Style packs: selection and rotation

One brand, seven looks. The storyboard picks ONE pack per video and records it in `style_pack`; scene workers load `styles/<pack>.md` instead of guessing aesthetics. The pack list is the `style_pack` enum in `shared/schemas/storyboard.schema.json` (single source of truth): `signal`, `terminal`, `sketch`, `blueprint`, `axon`, `halftone`, `silicon`. `styles/README.md` holds the locked shared anchors. Paths are relative to `skills/render-shorts/`.

## Selection rules (applied at storyboard time)

1. Pick by topic fit (the table in each pack file). Summary:

| Pack | Topic fit |
|------|-----------|
| `signal` | the default: benchmarks, numbers, comparisons (X vs Y), takes on news, anything without a better specialist |
| `terminal` | CLI, how-to, setup, serving, Docker, Ollama, vLLM, llama.cpp; anything whose natural visual IS a terminal |
| `sketch` | intuition and analogy-heavy concepts, the napkin explanation |
| `blueprint` | architecture and "how it works" internals: KV cache, request flow, unified memory, image vs container vs cache |
| `axon` | system topology and data-flow stories: what happens inside the box, between machines, inside a MoE |
| `halftone` | hot takes, benchmark face-offs, myth-busting, "everyone says X" |
| `silicon` | hardware anatomy: GPU, VRAM, bandwidth, quantization, tokens per second, DGX Spark internals |

2. Never the same pack twice in a row. `styles/history.json` is the ledger (oldest first; the last entry is the previous video).
3. One pack per video. No mixing. A named series locks its pack.
4. Packs change look, never geometry: safe zones, caption band, canvas and caption style are identical in every pack. Amber `#FFB347` is the accent everywhere; backgrounds are always dark-family (the safe-zone linter's bright-pixel detection depends on dark margins).

## The rotation script

```bash
python3 scripts/style_rotation.py --pick --slug <slug> --storyboard <storyboard.json>   # prints the pack
python3 scripts/style_rotation.py --pick --slug <slug> --topic "DGX Spark vs Mac Studio" --json
python3 scripts/style_rotation.py --record <pack> --slug <slug>                          # on approval
```

- `--pick` excludes the previous entry's pack, scores the remaining six by keyword hits in the storyboard (topic, title, hook, narration, visual briefs) or `--topic`, breaks ties by least recent use, and falls back to `signal`. The writer may overrule the pick with a better topic-fit argument, but never into the previous pack.
- `--record` appends `{slug, pack, date}` and refuses a repeat of the last entry (`--force` exists for a deliberate series lock, and must be explained in the hub note). Record once, when the storyboard is approved, not at every re-script.
- The history is committed text; keep it in `styles/history.json` so cloud routines and the Spark read the same ledger.

## Anti-sameness beyond packs

- Every scene carries a `layout_archetype` (`centered-stack`, `split-compare`, `timeline`, `grid`, `giant-number`, `diagram-flow`); adjacent scenes may not repeat one.
- Scene rhythm: vary durations (do not make every scene about 8 s); stillness is contrast, use it after motion bursts.
- The hook scene opens on a finished composition in the pack's own voice (typed prompt, chalk word, drafted guide, iso slab, punch card, lit trace, or a kinetic headline), never on a generic title card.
