# Stage Contracts (ICM mapping output)

The formal contracts live in `workspaces/*/stages/*/CONTEXT.md`. This file records the dependency graph and the canonical sources checked during mapping.

## Dependency graph (Shorts)

```
input/ + sources --> 01-radar --> 02-ideas --> 03-research --> 04-script --> 05-package
                                    |              |               |              |
                                 hub note (videos/[slug].md) updated by every stage
                                                                   |
                                 06-voice <-- 04-script (storyboard)  |
                                 07-render <-- 04-script, 06-voice    |
                                 08-publish <-- 05-package, 07-render (final.mp4), hub status approved
published/ <-- 08-publish ; read by 01-radar and 05-package (dedupe only)
```

## Dependency graph (long-form)

```
input/ + sources --> 01-radar --> 02-ideas --> 03-research --> 04-outline --> 05-script --> 06-spec --> 07-package
                                                   |                            |           |
                                  08-capture <-- 03 (experiment), 05 (narration)            |
                                  09-voice   <-- 05 (narration, as reconciled)              |
                                  10-render  <-- 06 (spec), 08 (captures), 09 (voice)       |
                                  11-publish <-- 07 (package), 10 (render), hub status approved
```

Every arrow points from an earlier stage to a later one. No stage file mentions a later stage by number (validated by `tools/validate.py`, rule "Stage cross-references are one-way").

## Canonical sources

| Fact | Home | Pointers |
|------|------|----------|
| Voice rules | `brand-vault/voice-rules.md` | every script and package contract |
| Length bands | `skills/script-gates/formats.json` | script contracts, platform specs |
| Posting rules | `shared/playbook/*.md` | package contracts |
| Status machine | `shared/pipeline-overview.md` | workspace CLAUDE.md files, build agent |
| Hub note shape | `shared/hub-note-template.md`, `shared/schemas/hub-note.schema.json` | `tools/new-run.py`, `tools/check_outputs.py` |
| Publish manifest | `shared/schemas/publish-manifest.schema.json` | package references, `publish.py` |
| Scene types | `skills/render-longform/rules/scene-library.md` | spec contract and reference |
| Secrets | `shared/env-template.md` | `build/.env.example`, cloud environment |

## Output consumption

Every stage output is read by a later stage or is the final deliverable (`published/[slug].md` and the scheduled video). Radar JSON is also read by the next seven radar runs for dedupe.
