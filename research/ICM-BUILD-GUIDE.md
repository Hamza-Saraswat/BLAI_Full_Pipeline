# ICM Build Guide

Interpretable Context Methodology (ICM): folder structure as agent architecture. A self-contained reference and build manual, compiled from the paper and the reference implementation so that a person or an agent can understand the method, build a workspace for any domain, and operate it, without opening the paper or cloning the repo.

| | |
|---|---|
| Paper | Jake Van Clief and David McDermott, "Interpretable Context Methodology: Folder Structure as Agent Architecture", arXiv:2603.16021v2 [cs.AI], 18 Mar 2026. https://arxiv.org/abs/2603.16021 |
| Reference implementation | https://github.com/RinDig/Interpretable-Context-Methodology (MIT). This guide reflects commit `02ba5d8` (2026-07-25): four workspaces, `_core/` conventions and templates, 15 commits, no releases. |
| Origin system | https://github.com/RinDig/Content-Agent-Routing-Promptbase, the production content system ICM was extracted from. It holds the only fully populated brand vault and worked output artifacts in the ecosystem. |
| License note | Sections 4 and 5 reproduce the repo's `_core/CONVENTIONS.md`, `_core/placeholder-syntax.md`, and `_core/templates/*` under the MIT license, with the corrections listed in Appendix C. Appendix A adapts a validator proposed in the repo's PR #14. |
| Compiled | 2026-08-22 |

House style: this guide follows ICM's own quality rules (plain English, tables for contracts, numbered steps, no em dashes, lowercase-with-hyphens names) so that it models what it teaches.

## Contents

- [0. How to Use This Document](#0-how-to-use-this-document)
- [1. What ICM Is](#1-what-icm-is)
- [2. Why It Works](#2-why-it-works)
- [3. The Architecture](#3-the-architecture)
- [4. The Conventions](#4-the-conventions)
- [5. Templates and Placeholder Syntax](#5-templates-and-placeholder-syntax)
- [6. How to Build a Workspace](#6-how-to-build-a-workspace)
- [7. Worked Patterns from the Shipped Workspaces](#7-worked-patterns-from-the-shipped-workspaces)
- [8. Running a Workspace](#8-running-a-workspace)
- [9. Pitfalls and Gaps to Design Around](#9-pitfalls-and-gaps-to-design-around)
- [Appendix A: Convention Validator](#appendix-a-convention-validator)
- [Appendix B: A Complete Minimal Workspace](#appendix-b-a-complete-minimal-workspace)
- [Appendix C: Known Upstream Defects and Fixes Applied](#appendix-c-known-upstream-defects-and-fixes-applied)
- [Appendix D: Glossary](#appendix-d-glossary)
- [Appendix E: Source Index](#appendix-e-source-index)
- [Appendix F: Optional Extensions](#appendix-f-optional-extensions)

## 0. How to Use This Document

This guide is a build-time reference, not run-time context. Once a workspace exists, its own `CLAUDE.md` and `CONTEXT.md` files are the only routing an agent should read while producing work. Loading this whole file into a stage's context window would violate the method it describes.

### 0.1 Reading paths

| You are | Read | Skip |
|---|---|---|
| A person who wants to understand ICM | 1, 2, 3, then 7 and 8 | 4, 5, Appendix A (reference material) |
| An agent asked to build a new ICM workspace | 0.2, 3, 4, 5, 6, Appendix B; validate with Appendix A | 1, 2 (background), 7 (consult when a pattern is needed) |
| An agent asked to operate an existing workspace | `cd` into the workspace and read its `CLAUDE.md`; use section 8 of this guide only | Everything else |
| A reviewer checking a workspace against the spec | 4, 9, Appendix A, Appendix C | 1, 2 |

### 0.2 Quick path for an agent told "build an ICM workspace for X"

1. Read section 3 to internalize the five layers and the stage contract shape.
2. Read section 4 once. It is the spec. Every rule has a reason; keep the reason in mind, not just the rule.
3. Copy the templates in section 5 into your working memory. They are the starting points for every file you will write.
4. Follow section 6 stage by stage: discovery, mapping, scaffolding, questionnaire, validation. Do not skip the checkpoints; they exist so the human steers before files multiply.
5. Use Appendix B as a worked example of what "done" looks like for a small workspace. Copy its shape, not its domain.
6. Run the validator in Appendix A on the finished workspace. Fix every failure before handing it over.
7. Hand over by telling the user to `cd` into the workspace, open Claude Code, and type `setup`.

### 0.3 What this guide is not

- Not a framework. There is nothing to install. The workspace is a folder of markdown files, empty `output/` folders, and optional local scripts.
- Not a substitute for the user's domain knowledge. The method structures context; the content of the reference files (voice rules, design systems, conventions) still has to come from the person who owns the workflow.
- Not a finished product. ICM is a protocol with one reference implementation and open questions (section 1.6). Where the paper and the repo disagree, this guide says so and picks the working form.

## 1. What ICM Is

### 1.1 The thesis

Multi-step AI workflows are usually orchestrated in code: a framework passes context between agents, manages memory, handles errors, and coordinates steps. ICM's observation is that for a large class of workflows this coordination layer does not need to exist. If the prompts and context for each step already live as files in a well-organized folder hierarchy, one agent reading the right files at the right moment does the work that a multi-agent framework would otherwise do. The folder structure tells the agent what to do at each step. Local scripts handle the mechanical work that does not need a model (fetching data, moving files, formatting output, calling an API). Every intermediate result is a plain file a human can open, read, and edit before the next step runs.

The paper's one-line summary of the design: "Stage sequencing is the folder numbering. Context scoping is the folder hierarchy. State management is the files on disk. Coordination between stages is one folder's output being another folder's input."

### 1.2 What a workspace is

A workspace is a folder. Inside it:

- Numbered stage folders (`01-research/`, `02-script/`, ...) encode execution order.
- Each stage has a `CONTEXT.md` contract (what it reads, what it does, what it writes), a `references/` folder of stable rules, and an `output/` folder where its artifact lands.
- Workspace-level folders hold context shared across stages: a brand or design configuration folder, `shared/`, and optionally `skills/`.
- A `CLAUDE.md` at the workspace root orients the agent; a `CONTEXT.md` routes tasks to stages; `setup/questionnaire.md` configures the workspace once.
- One agent executes every stage, reading different files at each one. The same model can delegate sub-tasks within a stage, and the folder structure determines what context those sub-agents receive.

A workspace can be copied, zipped, emailed, committed to Git, or synced through cloud storage. It carries its own prompts, context structure, and stage definitions. There is no server, no environment to replicate, no deployment step.

### 1.3 The control surface

The paper's comparison of control surfaces for sequential, human-reviewed workflows (Table 1). The first six rows are where ICM is simpler; the last four are where frameworks do more.

| Dimension | Framework approach | ICM approach |
|---|---|---|
| Change stage order | Edit orchestration code, redeploy | Rename or reorder folders |
| Modify a prompt | Edit agent configuration in code | Edit a markdown file |
| Add or remove a stage | Write a new agent class, update the orchestrator | Add or delete a folder |
| Inspect intermediate state | Add logging, build a dashboard | Open the folder, read the files |
| Hand off to another person | Document environment, dependencies, setup | Copy the folder |
| Who can make changes | Developer | Anyone with a text editor |
| Error recovery mid-pipeline | Built-in retry, fallback, exception handling | Manual re-run of the failed stage |
| Conditional branching | Programmatic routing based on agent output | Human decides between stages |
| Concurrent execution | Native parallel agent coordination | Sequential by design |
| External service integration | Programmatic API calls, auth management | Local scripts or MCP connections |

### 1.4 Where it fits and where it does not

ICM fits workflows that are all three of:

- **Sequential.** Step 2 follows step 1. The stages form a line, not a graph.
- **Reviewable.** A human should check each step's output, and the output is something a human can read.
- **Repeatable.** The same pipeline runs weekly or daily with different input.

Deployed examples: content production (script to animation, short-form video, narrated explainers), training material (slide decks from source documents), academic research workflows, policy analysis, reporting and digest systems.

ICM does not fit:

- **Real-time multi-agent collaboration**, where agents respond to each other in tight loops. File handoffs are too slow; this needs message passing (AutoGen and similar).
- **High-concurrency systems**, where many users hit the same pipeline at once. ICM is local-first; scaling it means building the infrastructure it was designed to avoid.
- **Automated branching mid-pipeline.** A human can choose stage 3a over 3b after reading stage 2's output. Automating that choice means scripting, which moves ICM toward being a framework.

The claim is not that ICM replaces frameworks. The claim is that for a large and common class of workflows, frameworks provide more complexity than the problem requires, and that complexity has real costs: opacity, fragility, developer dependency, and overhead that slows iteration.

### 1.5 How it relates to neighboring ideas

| Neighbor | Relationship |
|---|---|
| Agent frameworks (CrewAI, LangChain, AutoGen) | Solve the same coordination problem in application code. Right choice for dynamic collaboration, concurrency, or complex branching. ICM trades their flexibility for portability, inspectability, and editability of plain files. |
| Model Context Protocol (MCP) | A different layer. MCP standardizes how a model reaches external tools and data. ICM structures what context the model receives at each stage. They compose: an ICM stage may call MCP tools, and its folder determines which tool definitions are loaded, so tool descriptions are scoped per stage instead of all loaded up front. |
| Claude Code skills | Bundled domain knowledge (a `SKILL.md` index plus rule files and scripts). ICM workspaces copy relevant skills into `skills/` and point at them from stage contracts (Pattern 9). |
| Prompt chaining (Wu, Terry, and Cai, AI Chains) | ICM is prompt chaining implemented at the filesystem level: each step's output is the next step's input, and the links are files. |
| Context engineering (Karpathy; Martin's write, select, compress, isolate) | ICM is "select" and "isolate" done by construction. Each stage folder contains only what that stage needs, so compression is rarely necessary. |
| Multi-pass compilers, Make, Unix pipes | The lineage. Section 2.7 lists what each contributed. |

### 1.6 Status of the evidence

ICM has run in production across content creation, training material, research analysis, and policy workflows, and has been adopted outside the authors' organization (University of Edinburgh Neuropolitics Lab, ICR Research, Academy of International Affairs in Bonn). The reported practitioner observations come from an invite-only community of 52 members and are self-reported through conversation, not instrumented. There has been no controlled comparison between ICM's staged context loading and a monolithic prompt on the same task; the quality argument rests on the "lost in the middle" literature and practitioner judgment. All testing used one model family (Claude Opus 4.6 orchestrating, Sonnet 4.6 for sub-tasks). The protocol itself is model-agnostic by design: it specifies folders, file formats, and naming, not model features.

Treat ICM as a well-argued, production-tested design pattern with open empirical questions, not as a measured result.

## 2. Why It Works

This section gives the reasons behind the rules in sections 3 and 4. An agent that knows why a rule exists applies it correctly in cases the rule did not anticipate.

### 2.1 The five design principles

| Principle | What it means in practice | Borrowed from | What it buys you |
|---|---|---|---|
| One stage, one job | Each stage reads a defined input, transforms it, and writes a defined output. A stage that fetches does not filter; a stage that filters does not format. | McIlroy's Unix rule; Parnas's information hiding; compiler passes | Stages can be replaced, re-run, or edited independently. Failures are local. |
| Plain text as the interface | Stages communicate through markdown and JSON files. No binary formats, no databases, no proprietary serialization. | Kernighan and Pike: text streams as the universal interface | Any tool can participate. Any person can inspect or change any artifact. |
| Layered context loading | An agent loads only what the current stage needs, and reference material is kept structurally separate from working artifacts. | Liu et al. (lost in the middle); Jiang et al. (prompt compression), inverted into prevention | Smaller, focused context windows, which is where models perform best. |
| Every output is an edit surface | Each stage's output is a file the human can open, edit, and save before the next stage runs. The next stage reads whatever is there. | Horvitz's mixed-initiative principles; Shneiderman's direct manipulation | The human steers at natural breakpoints without touching prompts or code. |
| Configure the factory, not the product | The workspace is set up once (identity, voice, design, tools). Each run produces a new deliverable from the same configuration. | Continuous delivery: production pipelines should be repeatable | Setup happens once; per-run work is only the per-run input. |

### 2.2 Context scoping, with numbers

Models perform worse when relevant information is buried in long contexts, and every irrelevant token dilutes attention. Prompt compression can recover much of the loss after the fact; ICM's approach is to avoid loading irrelevant context in the first place.

Representative context window composition from the script-to-animation workspace (paper Figure 3):

| Stage | Layers 0-2 (structural) | Layer 3 (reference) | Layer 4 (working) | Total |
|---|---|---|---|---|
| Research | ~1.3-1.6k | scoped | scoped | ~4.9k tokens |
| Script | ~1.3-1.6k | scoped | scoped | ~5.5k tokens |
| Production | ~1.3-1.6k | scoped | scoped | ~5.6k tokens |
| Monolithic (everything loaded) | all stages' instructions | all reference files | all prior outputs | ~42k tokens, most of it irrelevant to the current task |

Rules of thumb from the paper: Layers 0-2 together cost roughly 1,300-1,600 tokens; Layer 3 adds 500-2,000 depending on how many conventions apply; Layer 4 adds the working material, rarely more than a few thousand tokens when the previous stage did its job of condensing. Total per stage: 2,000-8,000 tokens. A monolithic prompt for the same pipeline easily reaches 30,000-50,000.

The practical test for any Inputs table: if a file or section would not change what the agent writes at this stage, it should not be loaded.

### 2.3 The factory and the product

Two kinds of content reach the model during a stage, and they ask for different kinds of attention:

- **Reference material (Layer 3)** says "here are the rules, follow them." Voice guides, design systems, build conventions, domain knowledge. Configured once, stable across runs. The model should internalize it as constraints.
- **Working artifacts (Layer 4)** say "here is the input, transform it." The previous stage's output, user-provided source material, anything specific to this run. The model should process it as input.

Mixing the two in one undifferentiated prompt forces the model to sort them. Separating them in the folder structure (references in `references/`, the configuration folder, and `shared/`; working artifacts in `output/`) means the model receives already-organized context. Practitioners report that stages with a clean separation produce more consistent adherence to style and format guidelines; the paper marks this as an open empirical question, but the design cost of keeping the separation is near zero.

### 2.4 Observability and edit surfaces

Because every intermediate output is a plain file, an ICM pipeline is observable without any logging layer, dashboard, or tooling. You open the folder and read the files. Rudin's argument applies at the workflow level: build systems that are inherently interpretable instead of explaining opaque ones afterward. ICM never had an opaque state to explain.

The human-AI interaction guidelines this satisfies by construction:

| Guideline (Amershi et al.) | How ICM meets it |
|---|---|
| Make clear what the system can do | Stage contracts state inputs, process, and outputs in plain language |
| Support efficient correction | Every output is a markdown file: open, edit, save |
| Support efficient dismissal | Review gates at every stage boundary: decide not to proceed, re-run with different input, or abandon the run |

This structure also lines up with regulatory language about human oversight (the EU AI Act's staged review, audit trails, and defined intervention points). The paper does not claim compliance; it notes that the artifacts such oversight requires are produced as a side effect of how ICM stages communicate.

### 2.5 Where humans actually intervene

Across 33 practitioners using multi-stage workspaces, 30 reported a U-shaped pattern of edits: heavy at the first stage, light in the middle, heavy again at the last stage (reported frequencies roughly 92%, 30%, 78% for a three-stage pipeline). The two peaks are different kinds of work:

| Stage position | Kind of human work | Design response |
|---|---|---|
| First stage (direction-setting) | Creative judgment: narrowing from many possibilities to one angle | Put checkpoints here. Present options before drafting. Lock the value the piece will deliver before writing. |
| Middle stages (constrained execution) | Trust. The earlier output sets direction and the reference material constrains execution, so there is little room to go wrong | Keep these stages tightly scoped. Audits more than checkpoints. |
| Final stage (alignment) | Debugging: checking that the output faithfully represents decisions made upstream, tracing misalignments back through the pipeline | Put audits here that re-read the stage n-2 output and compare. Consider a `Verify` section (Appendix F). |

Two more patterns from the same community: non-technical users successfully changed stage behavior by editing `CONTEXT.md` files (tone instructions, constraints like "keep scripts under 90 seconds", reordering emphasis), and users with a working workspace copy the folder and adapt the prompts for a new format rather than building from scratch.

### 2.6 Edit the source, not the output

Editing a stage's output fixes this run. Editing the source that produced it (the stage contract, the voice guide, the previous stage's framing) fixes every future run. In compiler terms, editing output is patching the binary.

The tension is real for creative work: sometimes a line needs a human touch no rule would have produced, and that is the practitioner adding value. But some output edits are diagnostic. If you tighten the opening paragraph every time, the contract should say "keep the opening under three sentences." If the tone drifts formal every time, the voice guide needs a stronger example of the target register. Recurring edits point to fixable source-level problems. Section 8.6 turns this into a habit.

### 2.7 Lineage

| Source | What ICM took from it |
|---|---|
| Unix philosophy (McIlroy, 1978; Kernighan and Pike; Raymond's rules of modularity, transparency, composition) | Programs that do one thing; output of one is input of the next; text as the universal interface |
| Pipe-and-filter architecture (Shaw and Garlan) | Independent components connected by data streams; any component can be replaced or tested alone |
| Make (Feldman, 1979) | Files are both the artifacts of work and the coordination mechanism; no separate orchestration layer when the filesystem tracks what was produced |
| Multi-pass compilers | Each pass reads the previous pass's output and writes a well-defined intermediate representation; incremental recompilation re-runs only what changed |
| Parnas (information hiding); Dijkstra (separation of concerns) | Decompose by what each module hides; address one thing at a time |
| Literate programming (Knuth) | The instruction file is also the documentation; a new team member can read the `CONTEXT.md` files top to bottom and understand the pipeline without running it |
| Infrastructure as code; continuous delivery | The workspace definition is the system; Git-diffable, repeatable |
| Mixed-initiative interfaces (Horvitz); direct manipulation (Shneiderman); human-centered AI | Human control at natural breakpoints; visible, manipulable objects; high control and high automation reinforcing each other |
| Plan 9's "everything is a file" | All state, context, and instructions exist as files in one namespace |

### 2.8 What you give up

ICM chooses simplicity of implementation over feature completeness (Gabriel's "worse is better"). Concretely, you give up automatic retries, programmatic branching, parallel agent coordination, and managed external integrations. In exchange you get a system that anyone can read, edit, copy, and run, and that has no opaque state. If your workflow needs the things ICM gives up, use a framework. If it does not, the framework's complexity is pure cost.

## 3. The Architecture

This section is the structural core. Everything in sections 4 to 6 elaborates it.

### 3.1 The five layers

Agents read down the layers and stop as soon as they have what they need. No agent reads everything.

| Layer | File | Question it answers | Tokens | When loaded | How many |
|---|---|---|---|---|---|
| 0 | `CLAUDE.md` (workspace root) | "Where am I?" Folder map, triggers, routing table, what to load per task | ~800 | Always (Claude Code auto-loads it) | One per workspace |
| 1 | `CONTEXT.md` (workspace root) | "Where do I go?" Task type to stage folder; shared resources | ~300 | On entry to the workspace | One per workspace |
| 2 | `stages/NN-name/CONTEXT.md` | "What do I do?" The stage contract: inputs, process, checkpoints, audit, outputs | 200-500 | Per task | One per stage |
| 3 | Reference material: `references/`, the configuration folder (`brand-vault/`, `design-system/`), `shared/`, `skills/` | "What rules apply?" Voice rules, design systems, conventions, domain knowledge | 500-2,000 | Selectively, as named in the stage's Inputs table | Stable across runs |
| 4 | Working artifacts: `output/` folders, user-provided source material | "What am I working with?" Previous stage output, this run's input | Varies | Selectively, as named in the stage's Inputs table | Changes every run |

Layers 0-2 are structural: identity, routing, instruction. Layers 3-4 are content: the factory and the product. Layer 2 is the control point of the whole system, because its Inputs table decides exactly which Layer 3 and Layer 4 files the agent loads, and which sections of them.

### 3.2 The canonical folder tree

The repo's real layout (the paper's figure draws a `_config/` folder, but no workspace uses that name; the configuration folder is `brand-vault/` in the content workspaces and `design-system/` in the course workspace, and any domain-appropriate name is fine).

```
workspace-name/
├── CLAUDE.md                     Layer 0: where am I
├── CONTEXT.md                    Layer 1: where do I go
├── .gitignore                    ignores stages/*/output/*, .env, node_modules, *-ref/
├── setup/
│   └── questionnaire.md          one-time onboarding; populates {{PLACEHOLDERS}}
├── brand-vault/                  Layer 3: workspace-level configuration (name varies by domain)
│   ├── CONTEXT.md                routing within the collection: which sections to load when
│   ├── identity.md               who you are, who you write for
│   └── voice-rules.md            hard constraints, wrong/right pairs, pacing
├── shared/                       Layer 3: cross-stage files (platform specs, env template, pipeline overview)
├── skills/                       Layer 3: bundled domain knowledge (SKILL.md + rules/ + scripts/)
└── stages/
    ├── 01-research/
    │   ├── CONTEXT.md            Layer 2: stage contract
    │   ├── references/           Layer 3: rules for this stage only
    │   └── output/               Layer 4: this stage's artifact (.gitkeep when empty)
    ├── 02-script/
    │   ├── CONTEXT.md
    │   ├── references/
    │   └── output/
    └── 03-production/
        ├── CONTEXT.md
        ├── references/
        └── output/
```

What the structure encodes:

- **Numbering encodes execution order.** Reordering stages is renaming folders.
- **Folder boundaries enforce separation of concerns.** A stage's `references/` holds rules only that stage needs. Rules shared by several stages live in the configuration folder or `shared/`.
- **`output/` folders are the handoff points.** Stage 02 reads from `../01-research/output/`. A human can edit any file there before stage 02 runs.
- **The configuration folder and `shared/` persist across runs.** They are the factory. `output/` changes every run. It is the product.

### 3.3 Layer 3 versus Layer 4

| | Layer 3: reference | Layer 4: working |
|---|---|---|
| Changes between runs | No | Yes |
| Example files | `voice-rules.md`, `design-system.md`, `build-conventions.md` | `topic-brief.md`, `topic-script.md`, user-supplied PDFs |
| Model should | Internalize as constraints | Process as input |
| Configured during | Workspace setup (once) | Pipeline execution (each run) |
| Folder location | `references/`, the configuration folder, `shared/`, `skills/` | `output/` (and, if you adopt the convention in section 9, `input/`) |
| Analogy | The recipe | The ingredients |

Larger Layer 3 collections get their own `CONTEXT.md` routing file (for example `brand-vault/CONTEXT.md`) that tells agents which sections of which files to load for which purpose. This is the Layer 1 routing pattern applied recursively inside Layer 3.

### 3.4 The stage contract

Every stage `CONTEXT.md` has the same shape. Three sections are mandatory (Inputs, Process, Outputs); two are added when the stage does creative or build work (Checkpoints, Audit). The file ends with one sentence naming the human edit surface.

```markdown
# Stage 02: Script

Take the research brief and write a script ready for the spec stage.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../01-research/output/[topic-slug]-brief.md` | Full file | Source of claims |
| Brand vault | `../../brand-vault/voice-rules.md` | "Hard Constraints" through "What the Voice Is NOT" | Tone discipline |
| Reference | `references/script-structure.md` | Full file | Required structure |
| Shared | `../../shared/platform-specs.md` | Row for {{PRIMARY_PLATFORM}} | Duration budget |

## Process

1. Read the brief
2. Propose 3-5 angles, one sentence each, tagged with the value type each delivers
3. **[Checkpoint]** -- Present the angles; the human picks one
4. Write the full script in one pass following the voice rules and the chosen angle
5. Run the audit checks below. If any fail, revise before saving
6. Save to `output/[topic-slug]-script.md`

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | 3-5 angles with value tags | Which angle to pursue, combine, or redirect |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Voice constraints | Zero violations of the Hard Constraints in voice-rules.md |
| Word budget | Within +/-10% of the platform's target |
| Claims sourced | Every quantitative claim traces to the brief |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Script | `output/[topic-slug]-script.md` | Markdown with a metadata header and the script body |

The script in `output/` is the human edit surface. Rewrite lines, change the hook, adjust timing. Stage 03 reads whatever is in that file.
```

The paper's minimal form of the same contract, for comparison:

```markdown
## Inputs
- Layer 4 (working): ../01_research/output/
- Layer 3 (reference): ../../_config/voice.md
- Layer 3 (reference): references/structure.md

## Process
Write a script based on the research output.
Follow the structure in structure.md.
Match the tone described in voice.md.

## Outputs
- script_draft.md -> output/
```

Rules that make the contract work:

1. **Inputs rows name sections, not just files.** "Hard Constraints through What the Voice Is NOT" loads 40 lines instead of 150. Write "Full file" only when the whole file is needed.
2. **Every Inputs row has a Why.** If you cannot say why a file is loaded, it should not be.
3. **Process steps are concrete enough that two agents following them produce structurally similar output.** "Write the script" is too vague. "Write the full script in one pass, then audit against the voice hard constraints and the value brief" is right.
4. **Checkpoints sit between steps, never inside them.** The agent finishes a unit of work, presents, and waits.
5. **The audit runs after the process and before the save.** If any check fails, the agent revises. The audit line is always worded the same way so it cannot be misread: "Run the audit checks below. If any fail, revise before saving."
6. **The contract never contains reference content.** No definitions, rules, examples, or guidelines. Those live in `references/` and are pointed to. This keeps contracts at 25-80 lines and stops them going stale.
7. **The closing sentence names the edit surface.** It tells the human what to edit and tells the next stage to read whatever is there.

### 3.5 Handoffs and naming

- Stage N writes `stages/0N-name/output/[topic-slug]-[artifact-type].md`. Stage N+1's Inputs table says to read it. That is the entire handoff mechanism.
- Naming: `[topic-slug]-[artifact-type].md`, for example `hello-world-script.md`, `hello-world-spec.md`. The slug is set by the entry stage and carried forward by convention; a metadata header in each artifact (source file, stage, date) is the explicit provenance link.
- Multi-file outputs go in a subfolder: `output/[topic-slug]/` containing, for example, `index.tsx`, `beats/`, `assets/`.
- Every `output/` folder contains a `.gitkeep` so the folder exists when empty, and the repo's `.gitignore` excludes everything else in `output/` (per-run artifacts are not part of the workspace definition).
- "Most recent file" in an Inputs table means the newest artifact for the current topic. If several runs accumulate, the slug disambiguates; if that is not enough, clear `output/` folders before a new run.

### 3.6 Triggers

Triggers are bare keywords the user types in chat. There are no slash commands, hooks, or scripts behind them; the workspace `CLAUDE.md` declares them in a table, and the agent acts on them by reading the file the table points to.

| Keyword | What the agent does |
|---|---|
| `setup` | Reads `setup/questionnaire.md`, asks every question in one pass, replaces placeholders across the workspace, scans for any remaining `{{NAME}}` tokens, and presents derived voice rules for review (section 5.3). |
| `status` | Scans `stages/*/output/`. A stage is COMPLETE if its output folder has files other than `.gitkeep`, otherwise PENDING. Renders the pipeline. |

The `status` render, from the conventions (keep the third line; it is the most useful part):

```
Pipeline Status: [workspace-name]

  [01-stage-name]  ------>  [02-stage-name]  ------>  [03-stage-name]
     COMPLETE                  PENDING                  PENDING
  (artifact.md)              (empty)                  (empty)
```

Workspaces may define more triggers in their own `CLAUDE.md` (for example `research [topic]` to run the whole pipeline, or `resume` to continue from a progress file).

### 3.7 How the agent moves through the pipeline

There is no orchestrator, run manifest, or "next stage" pointer. Three filesystem facts do the job:

1. Zero-padded numbering gives the order.
2. The routing tables in `CLAUDE.md` and `CONTEXT.md` map what the user asks for ("write a script", "build the deck") to a stage contract. The agent routes on the request, not on a state machine.
3. `status` derives progress from what is on disk.

A run starts at the entry stage, which collects per-run details conversationally (topic, audience, scope) because those are never in the questionnaire. The agent reads the stage contract, loads exactly the Inputs rows, follows the Process, pauses at checkpoints, runs the audit, and writes to `output/`. The human reviews the output file. Then the next stage, or a re-run of the same stage with edits. A workspace can also allow entry at a later stage when the user already has that stage's input (section 7.5).

### 3.8 Claude Code mechanics

- Claude Code auto-loads `CLAUDE.md` from the directory it is launched in and from parent directories, and pulls in `CLAUDE.md` files from child folders when the agent works with files under them. Launch Claude Code from inside the workspace folder (`cd workspace-name`) so the workspace's `CLAUDE.md` is the one in force. The repo's root `CLAUDE.md` says exactly this: navigate into a workspace and its `CLAUDE.md` takes over.
- The orchestrating model can delegate sub-tasks within a stage to other agents. In the reference deployment the primary model used the stage's own `CONTEXT.md` and Layer 3 files to fill the sub-agents' prompts, so the folder structure is both the human's control surface and the model's delegation spec. Delegation is not required; none of the shipped workspaces mention it in their files.
- Tools: a stage may use MCP connections or local scripts. Describe the tool in the stage's `references/` (Pattern 7) and invoke it from a Process step with the exact command.
- Model choice: the protocol specifies files, not model features. Any model that can read files and follow a markdown contract can run a workspace. Output quality across models is untested.

### 3.9 Token budget check

Before finalizing a stage contract, estimate its context: about 1,500 tokens for Layers 0-2, plus roughly 1 token per 4 characters for each Inputs row (count only the named sections), plus the working artifact. If the total passes 8,000, the stage is loading too much: narrow the Section/Scope column, split a reference file so the relevant part can be loaded alone, or split the stage. If a reference file exceeds 200 lines, split it regardless.

## 4. The Conventions

This is the spec: the fifteen patterns from the repo's `_core/CONVENTIONS.md` (reproduced under MIT with the project's old name "MWP" replaced by "ICM"), plus naming rules, quality guardrails, and the definition of done. Every workspace follows every applicable pattern. Where a pattern does not apply (for example shared constants in a non-code workspace), the convention says so.

### 4.1 Architecture patterns

#### Pattern 1: Stage Contracts

Every stage `CONTEXT.md` follows the same three-section shape:

```markdown
## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| ... | ... | ... | ... |

## Process

1. Step one
2. Step two
3. Step three

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| ... | ... | ... |
```

This is the contract. It is simple enough that a non-technical user can read it and understand what is happening. It is structured enough that an agent can follow it reliably. Every stage follows this exact shape. No exceptions. Checkpoints and Audit sections (Patterns 11 and 12) are inserted between Process and Outputs when the stage needs them.

#### Pattern 2: Stage Handoffs via Output Folders

Every stage has an `output/` subfolder. The agent writes its artifact there. The next stage reads from the previous stage's `output/` folder.

- Stage N produces: `stages/0N-name/output/artifact-name.md`
- Stage N+1's `CONTEXT.md` says: read `../0N-name/output/artifact-name.md` as your input

This is the handoff. A human can open the output file, edit it, and the next stage picks up the edited version. No state management. No orchestration layer. Just files in predictable places.

File naming in output folders: `[topic-slug]-[stage-artifact].md`, for example `hello-world-script.md`, `hello-world-spec.md`.

#### Pattern 3: One-Way Cross-References

Every folder points outward to what it needs. No folder points back.

If stage 03 references stage 02's component registry, stage 02 does not reference anything in stage 03. If the brand vault is referenced by multiple stages, the brand vault does not reference any stage.

This prevents reference growth from going N-squared as the system scales. When adding a new reference, check: "Does the target file already reference my folder?" If yes, restructure.

#### Pattern 4: Selective Section Routing

Inputs tables do not just say "read voice-rules.md." They say "read the Voice Rules section of voice-rules.md."

This keeps token cost low. A 150-line file might have only 60 lines of actionable rules for a specific stage. The other 90 lines of strategic rationale stay unloaded.

```
| File | Section to Load | Why |
|------|----------------|-----|
| voice-rules.md | "Voice Rules" through "What the Voice Is NOT" | Tone guidance |
| identity.md | "One-Sentence Brand" and "Audience" sections | Audience context |
```

When a full file is needed, write "Full file" in the Section/Scope column.

#### Pattern 5: Canonical Sources

Every piece of information has one home. Other files point there. They do not duplicate it.

If you need to update a rule, you update it in one place. Every other file has a pointer. If you find the same information in two files, one of them should be replaced with a reference to the other.

Smell test: search the workspace for a specific phrase. If it appears in more than one file and both instances are meant to be authoritative, one needs to become a pointer.

#### Pattern 6: CONTEXT.md = Routing, Not Content

`CONTEXT.md` files answer three questions:

1. What is this folder?
2. What do I load?
3. What is the process?

They never contain the actual reference material. No definitions. No rules. No extended examples. No voice guidelines. This keeps them small (25-80 lines) and prevents them from going stale when the content they would otherwise duplicate gets updated.

If you find yourself writing more than a one-sentence description in a `CONTEXT.md`, that content belongs in a separate file that the `CONTEXT.md` points to.

#### Pattern 7: Tool Prerequisites

Some stages require external tools (Node.js, LibreOffice, ffmpeg, Python packages). Setup guides for these tools live in the `references/` folder of the stage that uses them, for example `stages/03-build/references/remotion-setup.md`.

Setup guides are written for someone who has never installed the tool: what it is (one sentence), installation steps, how to verify it works, and how the workspace uses it.

If a tool is needed by multiple stages, it can live in `shared/` instead. The `setup` onboarding process should check which tools are needed based on the user's answers and point them to the right setup guide.

When a workspace bundles skills (Pattern 9), many tools that would have needed separate prerequisites (scripts, libraries, utilities) come bundled inside the skill folder. Only tools that require system-level installation still need setup guides. If any stage runs Node or Python code, also ship the dependency manifest (`package.json`, `requirements.txt`) the code needs; the reference repo omits this in one workspace and the stage cannot run as written.

### 4.2 Onboarding

#### Pattern 8: Questionnaire Design

Onboarding questionnaires configure the production system, not a specific run. They follow these rules:

1. **Flat structure.** No category groupings. Just a numbered list of questions.
2. **All at once.** Every question appears in one pass. The user should be able to answer everything in a single message.
3. **System-level only.** Questions configure things that stay the same across runs: identity, brand, design, tool preferences, default workflow. Per-run details (project name, topic, audience, scope) are collected conversationally at the start of each pipeline run by the entry stage.
4. **Derive, do not ask.** If a field can be inferred from another answer, the agent fills it in. List derived fields under the question they depend on. Do not add a separate question.
5. **Sensible defaults.** Every question should have a default or example so the user can skip what they do not care about.
6. **Ask once, never again.** After setup, the user should never see these questions again. The answers are baked into the workspace files permanently.
7. **Examples over descriptions.** For voice and style questions, ask for concrete examples (sentences that sound right, sentences that sound wrong, specific error patterns) rather than abstract descriptions. Examples are pattern-matchable. Descriptions require interpretation and produce weaker constraints.

The questionnaire template in section 5.1.4 encodes these rules.

### 4.3 Bundled skills

#### Pattern 9: Bundled Skills

Workspaces can bundle Claude Code skills directly into a `skills/` folder. This gives agents domain-specific knowledge (APIs, best practices, code examples) without requiring the user to have the skills installed globally.

```
workspace/
├── skills/
│   ├── [skill-name]/          (copied from ~/.claude/skills/ or cloned from GitHub)
│   │   ├── SKILL.md           (skill entry point)
│   │   ├── rules/             (detailed rule files, if any)
│   │   └── scripts/           (utility scripts, if any)
│   └── [another-skill]/
│       └── SKILL.md
```

**Discovery.** During workspace building (discovery stage), the builder identifies relevant skills by scanning `~/.claude/skills/` and `~/.agents/skills/` for locally installed skills, searching GitHub for skill repos matching the workspace domain (for example "remotion skill", "pptx skill"), and presenting candidates to the user for selection.

**Bundling.** Selected skills are copied (local) or cloned (GitHub) into the workspace's `skills/` folder during scaffolding. This makes the workspace self-contained.

**Referencing.** Stage `CONTEXT.md` files reference skills in their Inputs table:

```
| Skill | `../../skills/[name]/SKILL.md` | Index, then load rules as needed | [What it provides] |
```

A stage may also point straight at one rule file or one section of a rule file when it does not need the whole skill.

Skills replace custom reference docs when an official skill covers the same ground. Keep workspace-specific files (design systems, brand config, build conventions) alongside skills, not inside them.

**Authored skills.** A workspace may also write its own skill (a `SKILL.md` with frontmatter `name`, `description`, and `metadata.tags`, plus `rules/` and `scripts/`) when no published skill covers the task. This is how the reference repo packages its local scripts (section 7.6).

**When not to bundle.** Do not bundle skills that are purely about Claude Code itself (skill creators, MCP builders). Only bundle skills that provide domain knowledge the workspace's agents need at runtime. Vendored skills are copied verbatim and are exempt from the style guardrails below.

### 4.4 Quality patterns

#### Pattern 10: Specs Are Contracts

Specification stages define what the output should achieve and when things happen. They do not prescribe how to implement. The build stage has creative freedom within the quality floor defined by the design system.

A spec contains:

- A beat map with approximate durations, narration, and mood
- A visual philosophy describing what a muted viewer should understand
- Key moments that must land, and why each matters
- Audio sync points mapping narration words to visual events
- Color flow with per-scene dominant color and mood

A spec does not contain: frame numbers, component names, pixel positions, spring configs, or prop definitions. These are implementation decisions that belong to the build stage. (The list is from a video workspace; the principle transfers to any spec-then-build pair: slides outline then deck generation, architecture then code.)

#### Pattern 11: Checkpoints

Creative stages should include at least one checkpoint where the agent pauses and the human steers. The agent completes a full unit of work, presents options or a draft, and the human redirects before the next unit begins. Checkpoints go between process steps, not within them.

Not every stage needs checkpoints. Linear stages (extract, render, validate) often run straight through. Creative stages (writing, design, ideation) benefit from at least one.

The Checkpoints section in a stage `CONTEXT.md` is a table:

```
| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| [step #] | [what to show] | [what to choose] |
```

#### Pattern 12: Stage Audits

Creative and build stages should include an Audit section: a checklist the agent runs after completing the process but before writing to `output/`. Audits catch quality issues before they propagate downstream. Each check should be specific enough that pass/fail is unambiguous.

Not every stage needs an audit. Data extraction or file conversion stages may not benefit. Creative and build stages almost always do.

```
| Check | Pass Condition |
|-------|---------------|
| [Check name] | [What "passing" looks like] |
```

If any check fails, the agent revises before saving to `output/`. Where a script can decide a check (line counts, schema validity, file exists, exit code 0), name the script in the pass condition and run it; agent judgment is for the checks a script cannot make.

#### Pattern 13: Value Validation

Content-producing stages should define what types of value their output can deliver. Before the main creative work begins (ideally at a checkpoint), the agent and human should agree on which value types this specific piece will hit. This prevents "interesting but does not do anything" output.

Value types are workspace-specific. A content workspace might use NOVEL, USABLE, QUESTION-GENERATING, INTERESTING. A course workspace might use TEACHES, PRACTICES, CHALLENGES. The framework is defined once in a reference file and used at every checkpoint.

#### Pattern 14: Docs Over Outputs

Reference docs (design system, build conventions, skill rules) are the authoritative source for how to build. Previous stage outputs in `output/` folders are artifacts, not templates. Agents should not read other outputs to learn patterns.

This prevents copying from older, lower-quality work and ensures docs remain the single source of truth for quality standards. Early outputs are the worst outputs. If future agents learn from them, quality never improves.

### 4.5 Code-producing workspaces

#### Pattern 15: Shared Constants

Workspaces that produce code should define a constants pattern. Configurable values (colors, fonts, timing, layout) live in shared files that all build outputs import from. The questionnaire populates these files once during onboarding. Change a value once, it updates everywhere.

This is Pattern 5 applied to code values. Without shared constants, the same hex code or font name is hardcoded in every output file. Changing the brand color means a find-and-replace across every file ever built.

For non-code workspaces (content writing, course design), this pattern does not apply. Shared values live in reference docs instead.

### 4.6 Naming conventions

- Folders and files: `lowercase-with-hyphens`
- Stage folders: zero-padded number prefix: `01-`, `02-`, `03-`
- Placeholders: `{{SCREAMING_SNAKE_CASE}}`
- Output artifacts: `[topic-slug]-[artifact-type].md`
- No spaces in file or folder names
- Fixed names the protocol itself mandates: `CLAUDE.md`, `CONTEXT.md`, `SKILL.md`, `README.md`, `LICENSE`

### 4.7 Quality guardrails

- `CONTEXT.md` files: under 80 lines (the shipped stage contracts run 45-56)
- Reference files: under 200 lines (if longer, split into multiple files so a stage can load the relevant part alone)
- Plain English. Avoid jargon. If a term needs explaining, it is too specialized.
- No em dashes anywhere in the workspace; write `--`
- Every folder that should persist but starts empty gets a `.gitkeep` file
- Every markdown file should be readable by someone who understands markdown and git basics but does not have a deep engineering background
- Every path in an Inputs table resolves from the folder containing the `CONTEXT.md`; no absolute paths

### 4.8 Definition of done

The reference repo's contribution checklist, which doubles as the acceptance test for any new workspace:

- [ ] Built by following the build procedure (section 6), not hand-assembled
- [ ] `setup` runs cleanly and every placeholder resolves
- [ ] At least one end-to-end run completed
- [ ] No stage outputs committed (output folders contain only `.gitkeep`)
- [ ] All `CONTEXT.md` files are under 80 lines
- [ ] All reference files are under 200 lines
- [ ] Creative stages have at least one checkpoint and an audit section
- [ ] No circular dependencies between stages
- [ ] The validator in Appendix A passes

What makes a good workspace: a repeatable workflow (something that will run many times, not a one-off task); clear stage boundaries (each stage produces a distinct artifact a human might want to review or edit before proceeding); system-level setup (the questionnaire configures the production system, not a specific run); and full adherence to the conventions above.

## 5. Templates and Placeholder Syntax

The four templates are the repo's `_core/templates/*`, reproduced verbatim (the HTML comments are authoring guidance for the agent and stay in the file until it is filled in). The placeholder rules are the repo's `_core/placeholder-syntax.md`. Section 5.3 describes the `setup` flow as the shipped workspaces actually run it.

### 5.1 The four templates

#### 5.1.1 Workspace CLAUDE.md template

````markdown
# [Workspace Name]

[One sentence: what this workspace does.]

## Folder Map

```
[workspace-name]/
├── CLAUDE.md          (you are here)
├── CONTEXT.md         (start here for task routing)
├── setup/             (onboarding questionnaire)
├── skills/            (bundled Claude skills for domain knowledge)
├── [context-folder]/  (shared context files)
├── stages/
│   ├── 01-[name]/     ([brief description])
│   ├── 02-[name]/     ([brief description])
│   └── 03-[name]/     ([brief description])
└── shared/            (cross-stage reference files)
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run onboarding questionnaire |
| `status` | Show pipeline completion for all stages |

## Routing

| Task | Go To |
|------|-------|
| [Task type 1] | `stages/01-[name]/CONTEXT.md` |
| [Task type 2] | `stages/02-[name]/CONTEXT.md` |
| [Task type 3] | `stages/03-[name]/CONTEXT.md` |

## What to Load

<!-- Map each task to its minimal file set. Loading more files dilutes quality.
     The context window is working memory, not storage. -->

| Task | Load These | Do NOT Load |
|------|-----------|-------------|
| [Task 1] | [minimal file list] | [what to skip and why] |
| [Task 2] | [minimal file list] | [what to skip and why] |

## Stage Handoffs

Each stage writes its output to its own `output/` folder. The next stage reads from there. If you edit an output file, the next stage picks up your edits.
````

#### 5.1.2 Workspace CONTEXT.md template

````markdown
# [Workspace Name]

[One sentence: what this workspace covers.]

## Task Routing

| Task Type | Go To | Description |
|-----------|-------|-------------|
| [Task 1] | `stages/01-[name]/CONTEXT.md` | [What this stage does] |
| [Task 2] | `stages/02-[name]/CONTEXT.md` | [What this stage does] |
| [Task 3] | `stages/03-[name]/CONTEXT.md` | [What this stage does] |

## Shared Resources

| Resource | Location | Contains |
|----------|----------|----------|
| [Context folder] | `[folder]/CONTEXT.md` | [What it routes to] |
| [Shared files] | `shared/` | [What cross-stage files live here] |
| [Skill name] | `skills/[name]/SKILL.md` | [What domain knowledge this skill provides] |
````

#### 5.1.3 Stage CONTEXT.md template

````markdown
# [Stage Name]

[One sentence: what this stage does.]

## Inputs

<!-- List every file the agent needs. Be specific about which sections. -->

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../0N-prev/output/artifact.md` | Full file | The artifact to work from |
| Reference | `references/example.md` | "Relevant Section" | What it provides |

## Process

<!-- Numbered steps. Each step is one concrete action. Be specific enough that
     two different agents following these steps would produce structurally similar
     outputs.

     Too vague: "Write the script"
     Good: "Write the full script in one pass, then audit against the voice
            hard constraints and value brief"

     Too vague: "Generate ideas"
     Good: "Propose 3-5 concept angles, each as a single sentence. Tag each
            with its value type and format." -->

1. Read the input artifact from the previous stage
2. [Step two]
3. [Step three]
4. Save to output/

## Checkpoints

<!-- Points where the agent pauses for human input before continuing.
     Not every stage needs checkpoints. Linear stages (extract, render, validate)
     often run straight through. Creative stages (writing, design, ideation)
     benefit from at least one.

     Format: after which process step, what the agent presents, what the human decides.
     Delete this section if the stage runs straight through. -->

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| [step #] | [what options/output to show] | [what direction to choose] |

## Audit

<!-- Quality checks before the output is considered done. The agent runs these
     after completing the process steps. If any check fails, revise before saving.

     Not every stage needs an audit. Data extraction or file conversion stages
     may not benefit. Creative and build stages almost always do.
     Delete this section if no audit applies. -->

| Check | Pass Condition |
|-------|---------------|
| [Check name] | [What "passing" looks like] |

## Outputs

<!-- What this stage produces and where it goes. -->

| Artifact | Location | Format |
|----------|----------|--------|
| [Name] | `output/[slug]-[type].md` | [Description of the format] |

<!-- Target: keep this file under 80 lines. -->
````

#### 5.1.4 Questionnaire template

````markdown
# Onboarding Questionnaire

<!-- Agent instructions: Read this file when the user types "setup". Ask ALL questions
     in a single conversational pass. The user should be able to answer everything in one
     message. Collect answers. Replace placeholders across the specified files. After all
     replacements, verify no {{PLACEHOLDER}} patterns remain in the workspace. -->

<!-- Questionnaire design rules:
     1. FLAT STRUCTURE: No category groupings. Just a numbered list of questions.
     2. ALL AT ONCE: Every question appears in one pass. The user answers in one message.
     3. SYSTEM-LEVEL ONLY: Questions configure the production system, not a specific run.
        Per-run details (project name, topic, audience) are collected conversationally
        at the start of each pipeline run by the entry stage.
     4. DERIVE, DON'T ASK: If a field can be derived from other answers, the agent fills
        it in without asking. List derived fields under the question they depend on.
     5. SENSIBLE DEFAULTS: Every question should have a default or example so the user
        can skip what they don't care about.
     6. ASK ONCE, NEVER AGAIN: After setup, the user should never be asked these questions
        again. The answers are baked into the workspace files permanently.
     7. EXAMPLES OVER DESCRIPTIONS: For voice/style questions, ask for concrete examples
        (sentences that sound right, sentences that sound wrong, specific error patterns)
        rather than abstract descriptions. Examples are pattern-matchable. Descriptions
        require interpretation and produce weaker constraints. -->

### Q1: [Question text]
- Placeholder: `{{PLACEHOLDER_NAME}}`
- Files: `path/to/file1.md`, `path/to/file2.md`
- Type: free text
- Default: [Default value if user wants to skip]

### Q2: [Question text]
- Placeholder: `{{PLACEHOLDER_NAME}}`
- Files: `path/to/file.md`
- Type: selection
- Options: Option A, Option B, Option C

### Q3: [Question about an optional feature -- yes/no]
- Type: yes/no
- If NO: Remove `stages/0N-name/` entirely
- If YES: Keep it

---

## After Onboarding

[Tell the user what was configured and where to start.]

After all replacements, scan the entire workspace for remaining `{{` patterns. If any remain, ask for the missing info.
````

### 5.2 Placeholder syntax

Workspaces ship with placeholder variables in their markdown files. The onboarding agent replaces these with real content when a user runs `setup`.

#### Basic syntax

Placeholders use double braces and SCREAMING_SNAKE_CASE:

```
{{BRAND_NAME}}
{{TARGET_AUDIENCE}}
{{PRIMARY_COLOR}}
```

These are literal strings in markdown files. They are not code variables. The onboarding agent finds them and replaces them with the user's answers through string substitution.

#### Replacement rules

1. The onboarding agent reads `setup/questionnaire.md` for the list of questions
2. Each question maps to one or more placeholders
3. Each question specifies which files contain its placeholder
4. The agent asks the questions conversationally, collecting answers
5. The agent replaces every instance of each placeholder with the corresponding answer (every instance: a placeholder may appear more than once in a file)
6. After all replacements, the agent scans the entire workspace for any remaining placeholder patterns
7. If any remain, the agent flags them and asks the user for the missing information
8. Onboarding is complete only when zero placeholders remain

#### Where placeholders can appear

Placeholders can appear in any markdown file within a workspace: configuration files (`voice-rules.md`, `identity.md`), reference files (`hook-system.md`, `design-system.md`), shared files (`platform-specs.md`), bundled skill files the workspace authored, and stage `CONTEXT.md` files (only in Inputs table values, not in routing structure).

Placeholders should not appear in `CLAUDE.md` files (these need to work before onboarding runs), in top-level `CONTEXT.md` routing tables (same reason), or in the questionnaire itself (the questions are the source, not the target).

#### Conditional sections

Conditional sections wrap content that gets removed if the user indicates it is not needed:

```markdown
{{?SECTION_NAME}}

## Section Heading

Content that may or may not be relevant...

{{/SECTION_NAME}}
```

**Rule: conditional blocks can only wrap entire sections.** A section means a heading and all content below it, up to the next heading of the same or higher level.

Valid:

```markdown
{{?VIDEO_PRODUCTION}}

## Video Production Settings

Resolution, frame rate, and export format for your video pipeline.

- Resolution: 1920x1080
- Frame rate: 30fps
- Export format: MP4

{{/VIDEO_PRODUCTION}}
```

Invalid (do not do this):

```markdown
- Item one
{{?OPTIONAL_ITEM}}
- Item two (optional)
{{/OPTIONAL_ITEM}}
- Item three
```

Invalid (do not do this):

```markdown
The brand voice is {{?FORMAL}}formal and authoritative{{/FORMAL}}
{{?CASUAL}}casual and conversational{{/CASUAL}}.
```

Why this rule exists: removing inline content leaves orphaned list markers, broken sentences, or malformed markdown. Wrapping complete sections means removal always produces clean markdown.

Conditional blocks also remove whole stages: a yes/no question can delete `stages/0N-name/` and the `{{?STAGE_NAME}}` block that routes to it in the workspace `CONTEXT.md`. That block sits outside the routing table, which is why a top-level `CONTEXT.md` may contain a conditional even though its tables may not contain placeholders.

#### Naming

Use descriptive names: `{{BRAND_NAME}}` not `{{BN}}`. Group related placeholders with common prefixes: `{{VOICE_DESCRIPTION}}`, `{{VOICE_ADJECTIVES}}`; `{{PRIMARY_COLOR}}`, `{{SECONDARY_COLOR}}`, `{{ACCENT_COLOR}}`; `{{CONTENT_PILLAR_1}}`, `{{CONTENT_PILLAR_2}}`. Conditional section names describe what they wrap: `{{?BUILD_STAGE}}`, `{{?PILLAR_4}}`.

#### Questionnaire mapping

`setup/questionnaire.md` is the bridge between questions and placeholders. Each question entry specifies the question text, the placeholder(s) it populates, the file(s) where those placeholders appear, the input type (free text, selection, yes/no, structured), an optional default or example, optional follow-up questions for vague answers, optional derived fields, and optional conditional logic (if the answer is X, remove section Y).

#### Correction: what to scan for

The repo's completion check is "scan for remaining `{{` patterns." That check trips on any code example containing double braces, for example JSX `style={{ opacity }}` in a build-conventions file, and it misses placeholders written in a different syntax. Scan instead for the exact token shapes the protocol defines:

- Unresolved values: the regex `\{\{[A-Z][A-Z0-9_]*\}\}`
- Unresolved conditionals: `\{\{\?[A-Z][A-Z0-9_]*\}\}` and `\{\{/[A-Z][A-Z0-9_]*\}\}`
- Wrong-syntax placeholders that `setup` would never touch: `\[[A-Z]+(_[A-Z]+)+\]` (bracket style such as `[BODY_FONT]`)

The validator in Appendix A runs all three.

### 5.3 The setup flow as shipped

How the three shipped questionnaires actually run, which is the behavior to replicate in a new workspace:

1. **Instruction block at the top.** Three sentences: read this file when the user types `setup`; ask all questions in a single pass so the user can answer in one message; these configure the production system, not a specific run, and per-run details are collected at the start of each run. Workspaces that use paid APIs add a fourth: never write a real API key or voice id into any committed file; those go in `.env`.
2. **Per-question schema.** Every question is an `### Qn:` heading followed by a fixed bullet set: `Placeholder(s)`, `Files`, `Type`, and optionally `Example`, `Default`, `Options`, `Note`, and a list of derived fields ("Agent derives from Q2-Q5: ..."). No prose between questions.
3. **Mixed placeholder and default rows.** In the target files, user-supplied rows sit next to shipped defaults (hard constraints 1-3 are placeholders, 4-6 are defaults; wrong/right pairs 1-2 are placeholders, 3-4 are exemplars). The user's answers land beside worked examples, which anchors quality even for a lazy setup.
4. **Pass 1: replace.** Collect all answers, replace direct placeholders across the listed files, apply conditional logic (delete optional stages and their `{{?...}}` blocks; strip unused pillar sections).
5. **Pass 2: voice review.** Present the populated voice rules (Hard Constraints, the Wrong/Right table, Pacing, What the Voice Is NOT) and ask the user to edit anything that does not match how they actually sound. This is the only point where the agent's inference is human-verified before being baked in permanently; one-shot derivation produces worse rules.
6. **Derive the rest.** Pacing description and anti-patterns from the voice answers; positioning and content mission from brand, audience, and mission; per-pillar details from pillar names plus audience; generic descriptions for any value type the user did not mention, so the framework stays complete.
7. **Sweep.** Scan every `.md` file with the patterns in 5.2 and resolve anything left.
8. **Close.** Tell the user what was configured ("your production system is configured with [brand]'s voice, [palette], and [platform]") and how to start a run ("give me a topic"). If the workspace needs secrets, remind the user to populate `.env` from the template in `shared/`.

## 6. How to Build a Workspace

This is the repo's `workspace-builder` (a workspace whose output is a workspace) rewritten as a procedure an agent can follow without the builder present. Five stages, each with a checkpoint where the human steers and an audit the agent runs before moving on. The builder enforces the conventions so that the workspaces it produces follow them; keep that discipline when running it by hand.

### 6.0 Before you start

- **Input:** the user's description of a repeatable, sequential workflow, plus answers to four framing questions (ask them in one message): what domain is this for; describe the end-to-end workflow in one sentence; who will use it and how comfortable are they with AI tools; roughly how many stages, and are any skippable.
- **Where the workspace goes:** a new folder named `lowercase-with-hyphens` for the domain (for example `article-pipeline/`). If several workspaces will live side by side, put them under `workspaces/` with a root `CLAUDE.md` that lists and routes to each one (the repo's root `CLAUDE.md` is the model: folder map, routing table, triggers).
- **Working files:** the discovery and mapping stages produce two planning documents, `workflow-map.md` and `stage-contracts.md`. Keep them in a `_design/` folder next to the workspace (or in the builder's own `output/` folders if you are using the upstream builder). They are useful documentation afterward and can be deleted once the workspace is validated.
- **What you need from this guide:** section 3 (shape), section 4 (rules), section 5 (templates), Appendix B (a finished example).

### 6.1 Stage 1: Discovery

Understand the domain workflow through conversation with the user.

Inputs: the user's description; this guide's conventions (section 4); the example in Appendix B.

Process:

1. Ask the user to describe the workflow end to end. What do they start with? What do they end with?
2. Identify the distinct stages. Where does one task end and another begin? Look for natural handoff points where a human would want to review or edit before continuing. A stage boundary is where the artifact changes kind (brief to script, script to spec, spec to build).
3. For each stage, ask: what goes in (files, user input, previous stage output); what comes out (the artifact this stage produces); what does the agent need to know (reference material, rules, constraints).
4. Identify shared context: information used across several stages (brand voice, design system, audience, platform specs). This becomes the configuration folder and `shared/`.
5. Identify user-specific details: what varies from one user to another (brand name, colors, audience, platform, voice). These become placeholders.
6. Identify optional stages some users might skip. These become conditional sections and yes/no questions.
7. Identify tool prerequisites. For each stage: does it need an external tool (Node.js, Python packages, LibreOffice, ffmpeg, a paid API)? Note which stage, required or optional, and what it does. Each becomes a setup guide; each paid API becomes an `.env` variable.
8. Discover relevant skills: scan `~/.claude/skills/` and `~/.agents/skills/` for installed skills that match the domain; search GitHub for skill repos ("[domain] claude skill"); present candidates with one-line descriptions; let the user pick. Skills can replace custom reference docs and prerequisites when they cover the same ground.
9. **[Checkpoint]** -- Present the draft workflow map. Ask: are all stages captured? Any missing inputs or outputs? Any stages to combine or split?
10. Run the audit below. If any check fails, revise before saving.
11. Write `workflow-map.md`.

| After Step | Agent Presents | Human Decides |
|---|---|---|
| 8 | Draft workflow map: all stages with inputs and outputs, shared context, variables, tools, skills | Whether the stage breakdown, handoff points, and shared context are correct |

| Check | Pass Condition |
|---|---|
| Stage clarity | Every stage has a single responsibility and a named output artifact |
| Input/output chain | Every stage's inputs are either user-provided or produced by a prior stage |
| Shared context identified | Cross-stage resources (brand, design, audience) are listed separately from stage-specific references |
| Variable coverage | Every user-specific detail is captured as a named placeholder |

Output: `workflow-map.md` with these sections: Overview (one sentence, target user); Stages (for each: name, input, output artifact, reference material needed, creative or linear, optional?); Shared Context; User-Specific Variables (name, where it will be used); Optional Stages; Tool Prerequisites (tool, stage, required/optional, purpose); Selected Skills (name, source, what it provides).

### 6.2 Stage 2: Mapping

Turn the workflow map into formal stage contracts and verify the dependency graph.

Inputs: `workflow-map.md`; Patterns 1 and 3 in section 4.

Process:

1. Read the workflow map.
2. For each stage, write the formal Inputs / Process / Outputs contract in the stage-contract shape (section 3.4). Name sections in the Section/Scope column wherever a whole file is not needed.
3. Map cross-references: which stages read from which other stages and which shared files.
4. Identify canonical sources: where does each piece of information live? One home per fact.
5. Check for circular references: draw the dependency graph and verify it flows one way only.
6. Verify every stage's output is consumed by at least one downstream stage, or is the final deliverable.
7. **[Checkpoint]** -- Present the dependency diagram and the contracts. Ask: does the flow make sense? Any missing connections?
8. Run the audit below. If any check fails, revise before saving.
9. Write `stage-contracts.md` with the contracts and an ASCII dependency diagram.

| After Step | Agent Presents | Human Decides |
|---|---|---|
| 6 | Dependency diagram and draft contracts for all stages | Whether the dependency flow and contract definitions are correct |

| Check | Pass Condition |
|---|---|
| No circular references | Dependency graph flows in one direction only |
| Output consumption | Every stage's output is read by at least one downstream stage or is the final deliverable |
| Contract completeness | Every stage has Inputs, Process, and Outputs sections with no empty fields |
| Canonical sources | No piece of information is defined as authoritative in more than one stage |

### 6.3 Stage 3: Scaffolding

Generate the complete folder structure, `CONTEXT.md` files, and placeholder reference files.

Inputs: `stage-contracts.md`; the Tool Prerequisites and Selected Skills sections of `workflow-map.md`; the four templates (section 5.1); the placeholder syntax (section 5.2).

Process:

1. Read the stage contracts.
2. Create the folder structure: root `CLAUDE.md`, `CONTEXT.md`, `.gitignore`, `setup/`; the configuration folder (`brand-vault/` or a domain equivalent) with its own `CONTEXT.md`; `stages/` with one numbered subfolder per stage, each containing `CONTEXT.md`, `references/`, and `output/`; `shared/`; `skills/` if any skills were selected.
3. Populate each stage `CONTEXT.md` from the stage template, filled with the contract's inputs, process, and outputs. For each stage decide: does it benefit from a checkpoint (creative stages: yes, at least one; linear stages: usually no)? Does it need an audit (creative and build stages: yes; extraction and conversion stages: optional)? Delete the sections the stage does not need. End the file with the sentence naming the human edit surface.
4. Create the workspace `CLAUDE.md` from its template: folder map, triggers, routing table, and a What to Load table that maps each task to its minimal file set and names what not to load.
5. Create the workspace `CONTEXT.md` from its template: task routing table and shared resources. Wrap the routing entry for any optional stage in a `{{?STAGE_NAME}}` block outside the table.
6. Create placeholder reference files for each stage, with `{{PLACEHOLDERS}}` for user-specific content and shipped defaults beside them.
7. For content-producing workspaces, create a value framework reference file (Pattern 13).
8. For code-producing workspaces, create a shared constants file or pattern (Pattern 15).
9. Create the configuration folder files. If the workspace produces voice or style content, structure the voice rules as Hard Constraints, Sentence Rules (wrong/right pairs), Pacing, and What the Voice Is NOT, not as a single description placeholder.
10. If skills were selected: copy local skills (`~/.claude/skills/`, `~/.agents/skills/`) or clone GitHub skills into `skills/[name]/`; remove any custom reference file the skill replaces; update the Inputs tables to point at `../../skills/[name]/SKILL.md` (or a specific rule file) instead.
11. If any tool requires system-level installation, write a setup guide in the consuming stage's `references/` (what it is, install steps, verification command, how the workspace uses it). Ship dependency manifests for any code the stages run. If any stage calls a paid API, add `shared/env-template.md` (section 7.6) and make the first Process step of that stage "confirm `.env` exists and is ignored by Git".
12. Add a `.gitkeep` to every `output/` folder.
13. Run the audit below. If any check fails, fix before moving on.
14. The workspace now exists on disk. Nothing else is written until the questionnaire is designed.

| Check | Pass Condition |
|---|---|
| Folder structure | Every stage has `CONTEXT.md`, `output/`, and `references/` |
| Contract fidelity | Every stage `CONTEXT.md` matches the contracts from stage 2 |
| Placeholder syntax | All placeholders use `{{SCREAMING_SNAKE_CASE}}`; no bracket-style `[NAME]` placeholders |
| .gitkeep coverage | Every `output/` directory contains a `.gitkeep` |
| CONTEXT.md size | No `CONTEXT.md` exceeds 80 lines |
| Naming conventions | All folders and files use lowercase-with-hyphens |
| Paths resolve | Every path in every Inputs table resolves from the folder that contains the `CONTEXT.md` |

### 6.4 Stage 4: Questionnaire Design

Build the onboarding questionnaire that hydrates the placeholders.

Inputs: the User-Specific Variables section of `workflow-map.md`; every file in the scaffolded workspace that contains a placeholder; the questionnaire template (section 5.1.4); the placeholder syntax (section 5.2).

Process:

1. Read the workflow map's user-specific variables.
2. Scan every markdown file in the workspace for `{{[A-Z][A-Z0-9_]*}}` and `{{?...}}` tokens. Build the complete list with the files each appears in.
3. Split the variables into two buckets. **System-level:** things that stay the same across runs (identity, brand, design, tools, workflow preferences). These become setup questions. **Per-run:** things that change each run (project name, topic, audience, scope). These do not become setup questions; the entry stage's `CONTEXT.md` collects them conversationally at the start of each run, and a placeholder-free per-run template in `shared/` can define their shape (section 7.5).
4. For each system-level placeholder, write a question: text a non-technical person understands; the placeholder(s) it populates; the files where they appear; the input type (free text, selection, yes/no, structured); a sensible default or example.
5. For voice and style questions, ask for concrete examples, not descriptions: "give me 2-3 sentences that sound exactly like your brand" and "2-3 sentences your brand would never say" produce pattern-matchable rules; "describe your voice" produces an abstraction.
6. If a field can be derived from another answer, list it as a derived field under the source question. The agent fills derived fields without asking.
7. Write all questions as one flat numbered list. No category groupings. The user answers everything in one message.
8. Add conditional logic for optional stages: yes/no questions whose NO answer removes a folder and its `{{?SECTION}}` block.
9. If the workspace has voice or style rules with derived fields, add the two-pass process: after populating the rules from answers, the agent presents them for review before finalizing.
10. Verify every system-level placeholder has a question.
11. Verify per-run placeholders are handled by stage `CONTEXT.md` files, not the questionnaire.
12. Run the audit below. If any check fails, revise before saving.
13. Write `setup/questionnaire.md`.

| Check | Pass Condition |
|---|---|
| Placeholder coverage | Every system-level placeholder in the workspace has a corresponding question, and every question's placeholders exist in the files it lists |
| Per-run separation | No per-run variables appear in the questionnaire |
| Flat structure | All questions are in a single numbered list with no category groupings |
| Defaults present | Every question has a sensible default or example |

### 6.5 Stage 5: Validation

Verify the workspace against the conventions and fix what fails before it ships.

Inputs: the whole scaffolded workspace; `setup/questionnaire.md`; section 4; section 5.2; the validator in Appendix A.

Run each check, record pass or fail, fix, and re-run the failed checks:

1. **Cross-reference integrity.** Every path in every Inputs table points to a real file, resolved from the `CONTEXT.md` that contains it. List broken references.
2. **No circular dependencies.** Trace the reference graph; confirm it is a directed acyclic graph.
3. **Placeholder coverage.** Every placeholder in the workspace has a question; every question maps to at least one file that contains its placeholder. List orphans in both directions.
4. **Conditional section validity.** Every `{{?SECTION}}...{{/SECTION}}` block wraps a complete section and is balanced.
5. **Stage handoff chain.** Stage N's output location matches what stage N+1's Inputs table references. List the chain; flag gaps.
6. **CONTEXT.md purity.** No `CONTEXT.md` contains reference content (definitions, extended rules, examples, guidelines). Only: title, one-sentence description, Inputs, Process, Checkpoints (optional), Audit (optional), Outputs, and the closing edit-surface sentence.
7. **Checkpoints in creative stages.** Stages doing creative work have at least one checkpoint, and the checkpoint table's step numbers match the Process list.
8. **Audits in creative and build stages.** Present, with unambiguous pass conditions, placed after the process and before the save.
9. **Contract purity in spec stages.** Spec outputs define what and when, not how. No component names, frame numbers, prop definitions, or implementation details in spec reference files.
10. **Line counts.** No `CONTEXT.md` over 80 lines; no reference file over 200.
11. **Naming.** Lowercase-with-hyphens everywhere; zero-padded stage prefixes; `.gitkeep` in every empty `output/`.
12. **Tool prerequisites.** Every tool named in the workflow map has a setup guide with install steps and a verification command; optional tools have a yes/no question so their stages can be removed; paid APIs have an `.env` template and an ignore rule.
13. **Quality scan.** No em dashes; no unexplained jargon; markdown renders.
14. **Mechanical check.** Run `python3 validate.py <workspace>` (Appendix A). All rules pass.

Write `validation-report.md` (pass/fail per check, issues found, fixes applied) next to the other planning documents.

### 6.6 Handover

Tell the user three things: where the workspace is; how to start (`cd` into it, open Claude Code, type `setup`, answer in one message, review the derived voice rules); and how to run it (give the agent a topic, walk through the stages, edit any output before the next stage). If the workspace sits beside others under `workspaces/`, add it to the root `CLAUDE.md` folder map and routing table now; a workspace absent from the routing tables is invisible to an agent.

### 6.7 What becomes a placeholder

The rule of thumb from the reference workspace: if it varies from one user to another, it is a placeholder; if it is part of the framework's structure, it is hardcoded.

| Placeholders (ask once) | Hardcoded (ship as-is) |
|---|---|
| Brand or project name; mission; positioning | File structure; section headings; the stage-contract shape |
| Voice: right examples, wrong examples, hard constraints, adjectives, pacing | Process steps; checkpoint and audit tables |
| Audience: who, what they care about, what they already know | Audit checks and their pass conditions |
| Content pillars and their angles; value-type descriptions | Reference-file structure, recipes, anti-pattern tables |
| Platform and target duration or length | Hardcoded platform tables (all platforms), pointed to by the active-platform placeholder |
| Colors, fonts, lockup assets, URLs | Design-system rules and checklists |
| Tool preferences (model sizes, voice settings, defaults); optional-stage yes/no | Setup guides; skill files (except a few labeled settings) |

### 6.8 Recommended .gitignore

```
# Stage outputs (per-run artifacts, not part of the workspace definition)
**/stages/*/output/*
!**/stages/*/output/.gitkeep

# Per-run source material, if you adopt an input/ folder (section 9)
**/stages/*/input/*
!**/stages/*/input/.gitkeep

# Secrets
.env
.env.local
.env.*.local

# Dependencies and caches
node_modules/
__pycache__/
*.pyc

# Cloned reference repos (local only)
*-ref/

# Editor and OS files
.DS_Store
Thumbs.db
*.swp
.vscode/settings.json
.claude/
```

If you want an audit trail of runs (the paper's suggestion), remove the two `output/` lines and commit text outputs after each run; keep binary outputs ignored by extension.

### 6.9 Using the upstream builder instead

If the repo is cloned, `cd workspaces/workspace-builder`, type `setup`, and walk its five stages; it is the same procedure as above with outputs written to its own `stages/*/output/` folders. Before using it, fix its `_core` references: the builder's `CLAUDE.md`, `references/conventions-reference.md`, and stage contracts write them as `/_core/...`, which resolves to the filesystem root. The correct forms are `../../_core/` from the builder root, `../../../_core/` from its `references/`, and `../../../../_core/` from a stage folder (repo PR #10). Its quick-reference also omits Pattern 8; use section 4 of this guide as the conventions source.

## 7. Worked Patterns from the Shipped Workspaces

The repo ships three production workspaces. They are the best evidence of how the conventions look when applied, and several of their best ideas are not in the conventions file at all. Each pattern below is shown as it appears on disk, then "copy this when".

| Workspace | Stages | Domain | Best source for |
|---|---|---|---|
| `script-to-animation` | 3: script, spec, build | Content idea to Remotion animation code | Checkpoints and audits in a creative stage; brand vault; value framework; spec-as-contract; design system; bundled third-party skills |
| `course-deck-production` | 5: extraction, curriculum, outline, generation, qa-delivery | Source documents to PowerPoint decks | Multi-entry pipelines; travelling per-run metadata; QA checklists; section-scoped loading of a vendored skill |
| `voice-driven-animation` | 5: research, script, voice, animate, render | Narrated explainer video where the recorded audio is the timeline | Authored skills with scripts; secrets handling; source-of-truth table; loop-back routing; dry-run gates before paid API calls |

### 7.1 The workspace CLAUDE.md as shipped

About 75 lines: folder map, triggers, routing, a What to Load table, stage handoffs. Two things worth copying that the template only hints at.

**The Do NOT Load column.** Naming exclusions is what actually keeps the window clean:

```
| Task | Load These | Do NOT Load |
|------|-----------|-------------|
| Write a script | `brand-vault/voice-rules.md`, `brand-vault/identity.md`, `stages/01-script/references/*`, `shared/platform-specs.md` | `skills/remotion-best-practices/`, `stages/02-spec/references/`, `stages/03-build/references/` |
| Build Remotion code | `stages/02-spec/output/`, `stages/03-build/references/*`, `skills/remotion-best-practices/SKILL.md`, `stages/02-spec/references/design-system.md` | `brand-vault/`, `stages/01-script/`, `stages/02-spec/references/spec-format.md` |
```

Keep this table in sync with the stage Inputs tables; in the repo they drift (section 9).

**A When to Use section.** The voice-driven workspace opens with "When to Use This Workspace": the deliverable it is for, what it is not for, and which sibling workspace to use instead. Copy this when more than one workspace exists.

### 7.2 The configuration folder

`brand-vault/` is a Layer 3 collection with its own router. Its `CONTEXT.md` is twelve lines:

```
| File | Key Sections | Load When |
|------|-------------|-----------|
| `voice-rules.md` | "Hard Constraints", "Sentence Rules", "Pacing", "What the Voice Is NOT" | Writing any content (scripts, captions, narration) |
| `voice-rules.md` | "Strategic Rationale" | Understanding why voice choices were made (rarely needed) |
| `identity.md` | "One-Sentence Brand", "Audience" | Understanding who you are writing for |
| `identity.md` | "Positioning", "Content Mission" | Evaluating whether a script serves the brand |
```

Rows are file-plus-section pairs, and one row exists specifically to mark a section as skippable. Write a section you intend not to load (the rationale) so the router has something to exclude.

`voice-rules.md` (about 70 lines) uses three rule formats on purpose, because each is pattern-matchable in a different way:

1. **Hard Constraints:** a numbered list of errors. "These are errors. If the output contains any of these, rewrite." Items 1-3 are placeholders from the questionnaire; items 4-6 are shipped defaults.
2. **Sentence Rules:** a `| Wrong | Right |` table with verbatim pairs. Rows 1-2 are placeholders; rows 3-4 are exemplars such as "They invested significant time in infrastructure development" versus "They spent six months building a custom pipeline."
3. **Pacing** and **What the Voice Is NOT:** named anti-patterns with Bad/Good pairs ("Not antithetical: the 'not X, but Y' pattern. AI defaults to this constantly. One per script is fine.").

`identity.md` holds who: one-sentence brand, audience (who, what they care about, what they already know), positioning, content mission, and one enforcement line: "If a finished script does not clearly serve this mission, it needs reworking before it moves to the spec stage."

`shared/platform-specs.md` holds the container: an "Active Platform" pointer section driven by `{{PRIMARY_PLATFORM}}` and `{{TARGET_DURATION}}`, followed by hardcoded tables for every platform (resolution, fps, duration, safe zones, minimum text size). The data stays complete after onboarding narrows the pointer.

Copy this when: any workspace with a voice, a brand, or a house style. Name the folder for the domain (`design-system/` for decks; `research-preferences/` for a research pipeline).

### 7.3 Stage contracts as written

The script stage of `script-to-animation` is the fullest example. Its Process:

```
1. Identify which content pillar this topic falls under
2. Propose 3-5 concept angles, each as a single sentence a viewer could repeat to a friend. For each angle, tag which value types it naturally hits and which format it leans toward
3. **[Checkpoint 1]** -- Present angles to the human for selection
4. Take the selected angle and propose a value brief: the concept, which value slots this piece will fill (minimum 2) with specifics for each, the format, the hook in one sentence, and the close in one sentence
5. **[Checkpoint 2]** -- Present value brief to the human for confirmation
6. Write the full script in one pass following voice rules, audience constraints, and the value brief
7. Run the audit checks below. If any fail, revise before saving
8. Add the metadata header (pillar, hook type, template, value slots, duration, platform)
9. Save to output/
```

Its audit:

```
| Check | Pass Condition |
|-------|---------------|
| Voice constraints | Zero violations of hard constraints from voice-rules.md |
| Value delivery | Script delivers on the value slots locked in the value brief |
| Hook timing | The belief gap or tension lands within 2-3 seconds |
| Close quality | Last line is something someone could say to a friend |
| Retention beats | No gap longer than 5 seconds without a tagged beat |
| Share test | Someone who learned this 5 minutes ago would feel confident sharing it |
```

What to copy:

- **Two checkpoints in the direction-setting stage** (angles, then a value brief), none in the spec and build stages, whose control surface is the output file itself. This matches the U-shaped intervention data.
- **Checkpoints declared twice:** inline in the Process list as `**[Checkpoint]** --` with the literal questions to ask, and in the table. The inline marker is what the agent trips over while executing; the table is what a human scans. "After Step" names the last work step (the checkpoint is itself step N+1).
- **Fixed ordering:** work steps, checkpoint, audit, save. The audit sentence is identical in every stage.
- **Falsifiable pass conditions** with numbers where possible: "within 2-3 seconds", "no gap longer than 5 seconds", "zero violations", "at most one", "within +/-10%", "exit code 0".
- **The closing sentence:** "The finished script in `output/` is the human edit surface. Open it, rewrite lines, adjust the hook, change timing notes. Stage 02 reads whatever is in that file."
- **Linear stages run straight through.** Rendering and QA stages in the repo have no checkpoints; the QA stage externalizes its audit into a `qa-checklist.md` reference with a fix-and-reverify loop ("repeat until clean") and a final human approval step.

### 7.4 Reference-file shapes

Each reference file in the repo has a small fixed micro-schema. Reuse the schema; replace the content.

| File (workspace) | Shape | Copy this when |
|---|---|---|
| `hook-system.md` (script-to-animation) | Four patterns, each: Template / Example / Best for / Avoid when / Key rule; ends with "Choosing a Hook" | A library of openers, framings, or moves the agent picks from |
| `script-templates.md` | Four structures, each a numbered list with per-step durations, Best for, Key rule; owns the output's metadata header schema | Structural templates for an artifact type |
| `value-framework.md` | Four value types, each a hardcoded definition paragraph plus a placeholder line for the brand's flavor; a How to Use section that names the process steps where it applies | Any content workspace (Pattern 13) |
| `content-pillars.md` | One section per pillar: angle, topics, audience fit, default template; pillars 4-5 wrapped in `{{?PILLAR_4}}` and `{{?PILLAR_5}}`; header says agents load only the relevant pillar | Recurring themes with per-theme guidance |
| `design-system.md` | Four faces in one file: values tables (colors, typography, motion, spacing), rules under each table, recipes, an anti-patterns table (`Error | Why It Fails`), and a production checklist that the build audit points at | Any quality floor for a build stage |
| `spec-format.md` | Header fields, required sections, what a spec does not contain, a side-by-side good/bad example (creative intent versus component names and props), five rules | Any spec-then-build pair (Pattern 10) |
| `component-registry.md` | Named components with props; lives in the spec stage, referenced one-way from the build stage; ends with a protocol for adding components | A vocabulary shared by two stages (one home, one pointer) |
| `build-conventions.md` | Code-first: folder layout, naming, two canonical code skeletons, timing conventions, which skill rule files to always load, a pre-run checklist | Any code-producing stage |
| `remotion-setup.md` | Prerequisites, create, install, verify, how the stage output plugs in, troubleshooting (symptom to fix) | Any external tool (Pattern 7) |
| `slide-patterns.md` (course-deck) | Twelve slide types, each: When / Layout / Content / Note, where Note carries forward-compatibility hints for the next stage | A menu of output types the next stage must recognize |
| `qa-checklist.md` | Checkboxes grouped Critical / Warning / Design compliance, each `**Name:** symptom (likely cause)` | Any inspection stage; naming the probable cause turns a checklist into a repair manual |
| `extraction-rules.md` | Chunk types table with examples, a tagging template, grouping rules, what to skip, target counts | Any stage that turns raw material into structured chunks |

Two details worth keeping: a format-boundary reminder at the top of a constants file ("use without `#` in PptxGenJS code, with `#` in CSS") prevents a whole class of silent bugs; and an HTML comment at the top of the build stage, `<!-- Do not read other output/ files to learn patterns. -->`, is invisible when rendered and loud in the context window.

### 7.5 Multi-entry pipelines and travelling metadata

`course-deck-production` lets a user enter at stage 1, 2, or 3 depending on what they already have. Three mechanisms:

1. **Every stage's first Process step is conditional:** "If this is the entry stage (no Stage 0N output exists), collect course metadata from the user and write it to `output/[course-slug]-meta.md`. Otherwise, copy the metadata forward from the previous stage's output."
2. **A placeholder-free per-run template** in `shared/course-meta.md` defines the shape of that metadata (name, description, audience, session count, duration, source material) with the warning "Do NOT put placeholders here -- this is per-course data, not system config." This is how the per-run versus system-level split from Pattern 8 is made concrete.
3. **The metadata travels:** each stage re-emits `[slug]-meta.md` into its own `output/`, so every Inputs table reaches back exactly one hop and Pattern 3 holds as the pipeline grows. A `{{DEFAULT_START_STAGE}}` placeholder from the questionnaire records where this user usually begins.

Copy this when users will sometimes arrive with a later stage's input already in hand.

### 7.6 Scripts and authored skills

`voice-driven-animation` is the reference for "local scripts handle the mechanical work." It authors three skills instead of vendoring them:

```
skills/
├── elevenlabs-narration/   SKILL.md + rules/{paste-block,tone-tags}.md + scripts/generate-audio.py
├── whisper-beat-finder/    SKILL.md + rules/{cpu-fallback,phrase-matching}.md + scripts/{transcribe,find-beats}.py
└── remotion-scene-anatomy/ SKILL.md + rules/{timing-ts,beat-local-time,gap-fill-sequence,end-card-pattern}.md
```

`SKILL.md` opens with frontmatter (`name`, `description`, `metadata.tags` as a comma-separated string), then When to Use, What You Need Before Calling, How It Works (numbered), settings (placeholders that `setup` fills), a Rules list with one-line glosses linking each rule file, and After the Call. Stage contracts point at the whole skill, at one rule file, or at one section of a rule file:

```
| Skill | `../../skills/elevenlabs-narration/SKILL.md` | Full file | How to call ElevenLabs |
| Skill | `../../skills/elevenlabs-narration/rules/tone-tags.md` | Tag vocabulary | What `[brackets]` tags the API honors |
| External | `../../../script-to-animation/skills/remotion-best-practices/SKILL.md` | When deeper API help is needed | Reuse the upstream skill rather than re-bundling |
```

The `External` row avoids duplicating a 130 KB skill, at the cost of portability: copy the workspace out of the repo and the row dangles. Prefer bundling unless the skill is very large and the workspaces always travel together.

The division of labour in the voice stage:

| Work | Who |
|---|---|
| Find and extract the narration text from the script file | Script (string parse) |
| Call the TTS API, save the master and a runtime copy | Script |
| Transcribe with word timestamps | Script (local, no API) |
| Match anchor phrases to times and build the beat table | Script |
| Choose the anchor phrases; interpret a NOT FOUND; decide when to regenerate | Agent and human |

Script conventions worth copying: standard library first; guarded imports that print the `pip install` line; a `--dry-run` flag that runs before any paid call and works with no credentials; output to stdout so the shell does the filing (`find-beats.py transcript.json > beat-timings.md`); credentials only through `.env` loaded with `python-dotenv`; a warning before expensive calls ("over 5000 chars; the API may truncate"); the workspace root computed from the script's own location with a comment saying to adjust it if the file moves.

Three more files from this workspace are reusable as-is:

- **`shared/env-template.md`:** a fenced block of `KEY=` lines with empty values for the two secrets and populated defaults for tuning variables; "how to get the values"; the `.gitignore` lines to confirm; a table of which stage reads which variable; and "what never goes into `.env`" (per-run creative content). Secrets never appear in any committed file; the questionnaire collects a human-readable label (`{{ELEVEN_VOICE_LABEL}}`) and leaves the id in `.env`.
- **`shared/pipeline-overview.md`:** the five-stage diagram plus a "Source of Truth at Each Stage" table (stage, which artifact wins, why) and the regeneration rule: if the audio is regenerated, every downstream timing is recomputed from the new transcript. Write this table whenever an upstream artifact can be regenerated mid-run.
- **`## When to Loop Back`** in the final stage: a symptom-to-stage table ("beat lands off-cue: stage 04; audio sounds wrong: stage 03; script reads wrong: stage 02, then 03, then 04; claim unsupported: stage 01"). This is the workspace's error-recovery routing, which ICM otherwise leaves to the human.

The voice stage also shows a checkpoint used as a cost gate: after the dry run, "Approve or fix the script before spending API credits."

### 7.7 Questionnaires as shipped

The three questionnaires have 5, 14, and 16 questions. All follow the per-question schema in section 5.3. Differences worth knowing:

- The course-deck questionnaire offers four named palette presets with hex values plus Custom, and a selection for the default entry stage.
- The content questionnaires ask for right and wrong example sentences before asking for adjectives, and label the adjectives "supplementary."
- The voice-driven questionnaire adds structured questions for API voice settings (label, model, stability, similarity, speed, format), a Whisper model selection with the CPU-safe option as default, lockup asset path and URL for an end card, and single-video versus series.
- All three end with a two-pass close and a `{{` sweep; the voice-driven one also reminds the user to populate `.env`.

### 7.8 Where to crib from

| You need | Copy from |
|---|---|
| A creative stage with checkpoints, a value brief, and a six-row audit | `script-to-animation/stages/01-script/CONTEXT.md` |
| A spec stage and a build stage with creative freedom inside a quality floor | `script-to-animation/stages/02-spec/` and `03-build/` |
| A voice guide, identity file, and collection router | `script-to-animation/brand-vault/` |
| A pipeline users can enter at different stages | `course-deck-production/stages/*/CONTEXT.md` step 1 and `shared/course-meta.md` |
| Section-scoped loading of a large vendored skill | `course-deck-production/stages/05-qa-delivery/CONTEXT.md` |
| Skills with scripts, secrets handling, source-of-truth table, loop-back routing | `voice-driven-animation/` |
| Filled-in brand vault and real output artifacts to learn what good looks like | The origin repo `Content-Agent-Routing-Promptbase` (brand story, voice and tone, five content pillars, topic bank, platform playbooks, and dozens of finished scripts and specs) |

## 8. Running a Workspace

Operating an ICM workspace is reading files, editing files, and typing a few words. This section is the operator's manual; the workspace's own `CLAUDE.md` is the only routing an agent needs at run time.

### 8.1 Setup, once

1. `cd` into the workspace folder and open Claude Code there.
2. Type `setup`. Answer every question in one message; skip anything you do not care about and the defaults apply.
3. Review the derived voice rules when the agent presents them. Edit anything that does not sound like you. This is the one moment the agent's inference is checked before it is baked in.
4. If the workspace uses a paid API, create `.env` from `shared/env-template.md` and confirm it is ignored by Git. Never paste a key into any other file.
5. Type `status`. Every stage should read PENDING. Scan the workspace for `{{` once yourself; zero should remain.

### 8.2 A run, step by step

1. Start at the entry stage by asking for its task in the words the routing table uses ("write a script about X", "extract content from these files"). The entry stage asks for the per-run details (topic, audience, scope) that the questionnaire deliberately did not.
2. The agent reads the stage contract, loads exactly the rows in its Inputs table, and follows the Process. At each checkpoint it stops and presents; you choose. It runs the audit before saving and writes to `output/`.
3. Open the output file. This is the review gate (8.3).
4. Ask for the next stage. It reads whatever is in the previous `output/`, edits included.
5. Repeat to the final stage. `status` at any time shows what exists on disk.

### 8.3 The review gate: three choices

At every stage boundary you can:

| Choice | When | How |
|---|---|---|
| Accept | The output is right | Ask for the next stage |
| Edit the output | The output needs a one-off human touch (a better line, a trimmed section, a reordered beat) | Edit the file in place and save; the next stage picks it up |
| Fix the source and re-run | The output is wrong in a way that will recur (tone, structure, a missing constraint, a bad framing inherited from the previous stage) | Edit the stage contract, the reference file, or the previous stage's output; then re-run this stage (8.4) |

Where people actually intervene: heavily at the first stage (choosing direction), lightly in the middle, heavily at the last stage (checking alignment with earlier decisions). Expect that shape and budget review time accordingly.

### 8.4 Re-running a stage

ICM supports incremental recompilation by default. A stage's output may be stale when any file in its Inputs table has changed: the previous stage's output, a reference file, the configuration folder, or the contract itself. Nothing tracks this automatically; the Inputs table is the dependency list, so read it.

- To re-run one stage: ask for its task again. It overwrites (or adds beside) its previous output; if you want a clean slate, delete the old file first.
- To re-run from the middle: edit the upstream output you want to change, then run each downstream stage in order.
- To start a new run: clear the `output/` folders (or rely on distinct slugs if you keep several runs side by side).
- If the workspace has a source-of-truth table (section 7.6), regenerating an upstream artifact means every downstream timing or reference derived from it is recomputed, not patched by hand.

### 8.5 Sub-agents inside a stage

A stage's orchestrating agent may delegate: parallel research questions, one worker per scene, one per session deck. Give each sub-agent the same files the contract names (the stage `CONTEXT.md`, the specific reference sections, its slice of the working artifact) and nothing else. The stage folder is the delegation spec; a sub-agent that is handed the whole workspace is back to the monolithic prompt the method exists to avoid. Keep delegation inside a stage; handoffs between stages stay files.

### 8.6 Edit the source, not the output

Output edits fix one run. Source edits fix every future run. Keep a short log of what you changed at each gate, and after the same kind of edit shows up three runs in a row, move it upstream:

| You keep editing | Fix at the source |
|---|---|
| The opening (shortening, sharpening) | Add a constraint to the stage contract: "keep the opening under three sentences" |
| Tone (too formal, too hedged, too hypey) | Add a wrong/right pair or a hard constraint to the voice rules with the exact phrasing you removed |
| Structure (reordering sections, cutting a section) | Change the structural template in `references/`, or the Process step that produced the order |
| Facts or framing inherited from upstream | Fix the upstream output or the upstream stage's contract; do not patch downstream |
| Length | Put the budget in the audit with a number ("within +/-10% of N words") |
| A check the agent keeps missing | Add an audit row with an unambiguous pass condition; if a script can decide it, name the script |

### 8.7 Git practice

- Commit the workspace definition (contracts, references, configuration, questionnaire) with ordinary commit messages. Every prompt change is a diff.
- The repo's default ignores everything in `output/` except `.gitkeep`: outputs are per-run products, not part of the definition. This keeps the workspace small and keeps agents from reading old outputs as templates (Pattern 14).
- The alternative, suggested by the paper, is to commit outputs after each run as an audit trail of the pipeline's behavior over time. If you do this, commit text artifacts and ignore binaries by extension, tag or branch per run, and keep Pattern 14 in force by contract (agents read references, never `output/` files from other runs).
- Never commit `.env`. Check the ignore rules before the first run that uses a key.

### 8.8 Duplicating a workspace for a new format

Practitioners copy a working workspace rather than building a new one: copy the folder, rename it, edit the stage prompts for the new format (a long-form essay instead of a short video), delete or add a stage, and keep the configuration folder if the brand is the same. Register the copy in the root routing tables if several workspaces live together. Re-run `setup` only if the new format needs different system-level answers.

### 8.9 Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Output ignores the voice or design rules | The rules were not loaded (missing Inputs row), or they are descriptions rather than examples | Add the row with the exact section; rewrite rules as wrong/right pairs and hard constraints |
| Output is generic or drifts off the chosen angle | No checkpoint locked the direction before drafting | Add an angles checkpoint and a value brief to the first stage |
| A downstream stage contradicts an upstream decision | No alignment check | Add an audit row that re-reads the stage n-2 output and compares; or a `Verify` section (Appendix F) |
| The agent loaded far more than the contract names | What to Load table and Inputs table disagree, or Section/Scope says "Full file" everywhere | Reconcile the tables; name sections |
| The agent read old outputs to learn patterns | Pattern 14 not stated in the contract | Add the HTML comment at the top of the build stage and a Do NOT Load entry for other `output/` folders |
| A script step fails | Path or argument drift between the contract, the reference, and the script | Make the contract the canonical command; put the exact invocation in one place and point to it |
| `status` shows COMPLETE for a stage you did not run | Leftover files in `output/` | Clear `output/` before a new run |
| `setup` left `{{` tokens behind | Orphan placeholder with no question, or a code example with double braces | Run the validator (Appendix A); scan with the exact token regex |

## 9. Pitfalls and Gaps to Design Around

Lessons from auditing the reference repo against its own spec. Each one is a rule to apply when building, with the defect that motivated it.

1. **Every path resolves from the file that contains it.** The upstream builder writes `/_core/...`, which is the filesystem root, so its scaffolding stage cannot reach the templates it scaffolds from. A build-conventions file writes `require('../../skills/pptx/scripts/html2pptx.js')` from a file four levels deep; Node resolves `require` against the requiring file, so the stage fails on first run. Write relative paths from the file's own folder and resolve every one before shipping.
2. **Keep the What to Load table and the Inputs tables in agreement.** In `script-to-animation`, `CLAUDE.md` loads `stages/02-spec/references/*` for the spec task, which includes the component registry that the spec stage's own audit forbids using. One of the two tables is always wrong when they differ; treat the Inputs table as canonical and regenerate the What to Load table from it.
3. **One placeholder syntax.** `[INSTRUCTOR_NAME]`, `[SESSION_TITLE]`, and `[BODY_FONT]` in a build-conventions file are never replaced by `setup`, which only knows `{{NAME}}`, and `[BODY_FONT]` duplicates `{{BODY_FONT}}` elsewhere. Use `{{SCREAMING_SNAKE_CASE}}` only, and let the validator flag bracket style.
4. **Placeholder coverage runs both ways.** `{{VOICE_ADJECTIVES}}` is declared by a question but exists in no file (the answer only feeds derivations); `{{PROJECT_SHAPE}}` likewise; `{{CONTENT_PILLAR_1}}` through `{{CONTENT_PILLAR_5}}` are declared for a research reference file that never mentions them; `{{TARGET_DURATION}}` is declared for a contract that does not contain it. The final `{{` sweep cannot catch a placeholder that is missing from its target. Check declared-versus-present in both directions (Appendix A does).
5. **Scan for token shapes, not for `{{`.** JSX `style={{ opacity }}` in a code example trips the naive completion check every time. Use the regexes in section 5.2.
6. **Register every workspace in every routing table.** The repo's fourth workspace is absent from the README table and both root `CLAUDE.md` tables; Layers 0 and 1 are how an agent discovers what exists, so an unlisted workspace is unreachable.
7. **Give user-provided source material a home on disk.** The repo has no `input/` folder anywhere; PDFs and notes enter through chat attachments and leave no trace except a one-line description in a metadata file. That breaks the observability and portability claims for one input class. Add a gitignored `input/` folder at the workspace root (or in the entry stage), with an Inputs row pointing at it, and record file names in the per-run metadata.
8. **Ship tool prerequisites and manifests.** The course-deck workspace invokes Node, `pptxgenjs`, `sharp`, Python, LibreOffice, and poppler with no setup guide and no `package.json`. Pattern 7 applies to every stage that runs code; the manifest is part of the workspace.
9. **Vendored dead weight is a portability cost.** One bundled skill brings about 900 KB of XML schemas and four scripts nothing routes to; the workspace is forty times larger than its own content. Prune what the stages do not reference, or document why it stays.
10. **Cross-workspace `External` rows break portability.** Reusing `../../../script-to-animation/skills/...` saves 130 KB and makes the workspace dependent on a sibling. Bundle unless the workspaces always travel together, and say so in the workspace `CLAUDE.md`.
11. **Contract, reference, and script must agree.** In the voice workspace the contract says `output/audio.mp3`, the reference says `audio/video1.mp3`, and the script hardcodes `audio/{video}.mp3` with keys `video1`/`video2` while the contract passes `{topic-slug}`. Put the exact command in one place (the contract) and make the script read its paths from arguments.
12. **Silent drops need an audit row.** The beat-finder script drops any beat it cannot match and continues; only an audit row ("every beat resolves to a numeric start time") catches it. Whenever a script can lose data quietly, write the audit row that would notice.
13. **Keep the `status` render complete.** Two workspaces compress the three-line render to two, dropping the artifact filenames, which is the most useful line. Copy the form in section 3.6.
14. **If you declare shared constants, ship the file.** Pattern 15 is described, and one build audit requires "reference shared constants, not hardcoded values", but no constants file exists and the build conventions tell the agent to improvise one. Create `constants.*` during scaffolding with the questionnaire's values.
15. **Decide checkpoints and audits per stage, deliberately.** The conventions exempt "extract" and "validate" stages, yet the extraction stage in one workspace has both and the QA stage has neither section (its audit lives in a reference checklist). Either is defensible; the rule is to decide by whether the model makes creative decisions in the stage and to make the choice visible in the contract.
16. **One name for the project.** The conventions file still says MWP, the root `CLAUDE.md` draws a `model-workspace-protocol/` root, the README cites "Model Workspace Protocol" next to a dead `link-to-paper` link, and the README draws a `_config/` folder no workspace has. Naming drift in routing files costs agents real confusion; rename everywhere or nowhere.
17. **One statement of Git policy.** The voice workspace's env template says stage outputs "are committed normally" while the repo's ignore file excludes them. Put the policy in the workspace `CLAUDE.md` and make the ignore file match it.
18. **Genericize templates fully.** Placeholder files in the repo still carry a real company URL, a prior tagline, and a specific font in the neighborhood of the placeholders. When templating from a working system, scrub every brand-specific value, not just the ones you remembered to parameterize.
19. **A stage whose input is a live project is a break in the chain; say so.** The animate-to-render handoff in the voice workspace is not a file but a Remotion project registered in `Root.tsx`, gated by "a passing studio preview". That is acceptable, but the Inputs table must state it and the gate must be explicit, or observability quietly ends at that boundary.
20. **Keep skill indexes complete.** A bundled `SKILL.md` lists 29 rule files while 33 exist, so four are unreachable through progressive disclosure; the workspace also repeats a wrong count ("35 rule files") in three places. An index an agent cannot trust is worse than none; regenerate it from the folder.

## Appendix A: Convention Validator

ICM's thesis is that the filesystem is the orchestration layer. The trade-off is that a code framework throws on a bad import path, whereas here a wrong path degrades silently: the agent guesses, or loads nothing, and the pipeline still appears to run. The reference repo has no mechanical enforcement of its own conventions. This validator, adapted from a script proposed in the repo's PR #14 (by Avicennasis, standard library only, each rule mutation-tested upstream), checks a workspace or a whole repo against section 4 and section 5.2.

Save it as `validate.py` (in the workspace, in a `bin/` folder beside several workspaces, or anywhere on your path) and run:

```bash
python3 validate.py path/to/workspace
```

Add `--strict` to include vendored `skills/` content in the style rules. Run it on a clean workspace: files left in `output/` fail the "output folders contain only .gitkeep" rule by design. Exit code 0 means every rule passed.

Run against the upstream repo at `02ba5d8` it reports 12 of 18 rules passing; the six failures are defects 1, 2, 4, 7, 9 with 21, and 15 in Appendix C. Run against the workspace in Appendix B it passes 18 of 18.

| Rule | Catches |
|---|---|
| CONTEXT.md under 80 lines; reference files under 200 | Guardrail violations |
| No em dashes | Style guardrail |
| Empty persistent folders carry .gitkeep | Folders Git would drop |
| No spaces; lowercase-with-hyphens; zero-padded stage prefixes | Naming violations |
| Stage CONTEXT.md has Inputs, Process, Outputs in order | Pattern 1 |
| Inputs rows carry a Section/Scope value | Pattern 4 |
| Stage cross-references are one-way | Pattern 3 (a cycle between two stages) |
| Output folders contain only .gitkeep | Committed run artifacts |
| Inputs-table paths resolve | Broken references (the highest-value rule) |
| Every workspace is registered in README and root CLAUDE.md | An unrouted workspace (repo layout only) |
| Markdown links have real targets | `(link-to-paper)` and friends |
| Directories described in the README exist | Documented-but-absent folders such as `_config/` |
| Placeholders match the questionnaire both ways | Orphan placeholders and orphan questions; numbered families such as `{{PILLAR_2_ANGLE}}` and `{{PILLAR_N_ANGLE}}` are compared as one (added) |
| No bracket-style placeholders | `[BODY_FONT]` style that `setup` never replaces (added) |
| Conditional sections are balanced | An unclosed `{{?SECTION}}`; only markers alone on a line count, so prose mentions are ignored (added) |

```python
#!/usr/bin/env python3
"""Check an ICM workspace (or a repo of workspaces) against the ICM conventions.

Adapted from bin/validate.py proposed in RinDig/Interpretable-Context-Methodology
PR #14 (Avicennasis, MIT). Changes from upstream: runs on a single workspace
folder as well as a repo with workspaces/; three added rules (placeholder
coverage between the questionnaire and the files, with numbered families such as
PILLAR_2_ANGLE and PILLAR_N_ANGLE compared as one; no bracket-style placeholders;
balanced conditional sections, counting only markers that stand alone on a line);
a few more protocol-mandated names exempted from
the lowercase rule; folders whose name starts with "_" (such as _core and
_design) are treated as documentation and skipped by the placeholder rules.

Sources of truth: ICM-BUILD-GUIDE.md section 4 (patterns, naming, guardrails)
and section 5.2 (placeholder syntax).

Usage:
  python3 validate.py [workspace_or_repo_root] [--strict]

By default, style rules (line counts, em dashes, file naming) skip bundled
skills/ content, which is copied verbatim from upstream per Pattern 9.
--strict checks everything.

Exits 0 if all rules pass, 1 otherwise.
"""

import collections
import os
import re
import sys

EM_DASH = chr(0x2014)  # by codepoint: the rule forbids the literal
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", ".claude"}
# Filenames the spec itself mandates in non-lowercase form, plus dotfiles.
NAME_EXEMPT = {"CLAUDE.md", "CONTEXT.md", "CONVENTIONS.md", "README.md", "SKILL.md",
               "ICM-BUILD-GUIDE.md", "LICENSE", "LICENSE.txt", "LICENSE.md",
               "_core", "_design", ".gitkeep", ".gitignore", ".gitattributes",
               ".github", ".env", ".env.local", ".env.example"}
LOWER_RE = re.compile(r"^[a-z0-9]+([-._][a-z0-9]+)*$")
STAGE_RE = re.compile(r"^\d{2}-[a-z0-9]+(-[a-z0-9]+)*$")
# A path ref containing any of these is resolved at run time, not check time.
RUNTIME_MARKERS = ("{{", "[", "*")
PLACEHOLDER_LINKS = re.compile(
    r"\]\(\s*(link-to-\S*|TODO|TBD|url|example\.com\S*|#?)\s*\)", re.I)
VALUE_PH = re.compile(r"\{\{([A-Z][A-Z0-9_]*)\}\}")
# Real conditional markers stand alone on a line; prose mentions are ignored.
COND_OPEN = re.compile(r"^\s*\{\{\?([A-Z][A-Z0-9_]*)\}\}\s*$", re.M)
COND_CLOSE = re.compile(r"^\s*\{\{/([A-Z][A-Z0-9_]*)\}\}\s*$", re.M)
BRACKET_PH = re.compile(r"\[[A-Z]+(?:_[A-Z]+)+\]")
# Generic tokens used when writing ABOUT placeholders, not as placeholders.
META_TOKENS = {"PLACEHOLDER", "PLACEHOLDERS", "PLACEHOLDER_NAME", "SCREAMING_SNAKE_CASE",
               "NAME", "SECTION", "SECTION_NAME", "VARIABLES", "VARIABLE"}

results = []


def rule(name, violations, note=""):
    results.append((name, list(violations), note))


def posix(rel):
    return "/" + rel.replace(os.sep, "/") + "/"


def is_vendored(rel):
    return "/skills/" in posix(rel)


def is_doc(rel):
    """Top-level folders starting with "_" hold conventions and planning docs."""
    return rel.replace(os.sep, "/").split("/")[0].startswith("_")


def in_output(rel):
    return "/output/" in posix(rel)


def family(name):
    """{{PILLAR_2_ANGLE}} and {{PILLAR_N_ANGLE}} are one family: digits become N."""
    return re.sub(r"_\d+(?=_|$)", "_N", name)


def walk_files(root, ext=None, skip_vendored=False):
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            p = os.path.join(dp, f)
            r = os.path.relpath(p, root)
            if skip_vendored and is_vendored(r):
                continue
            if ext and not f.endswith(ext):
                continue
            yield r, p


def walk_dirs(root, skip_vendored=False):
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for d in dn:
            p = os.path.join(dp, d)
            r = os.path.relpath(p, root)
            if skip_vendored and is_vendored(r):
                continue
            yield r, p


def read(p):
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def sections(text):
    return [ln[3:].strip() for ln in text.splitlines() if ln.startswith("## ")]


def inputs_rows(text):
    """Yield cell-lists for each data row of the '## Inputs' table."""
    inside = False
    for ln in text.splitlines():
        if ln.startswith("## "):
            inside = ln.strip() == "## Inputs"
            continue
        if not inside or not ln.startswith("|"):
            continue
        if re.fullmatch(r"\|[-: |]+\|", ln.strip()):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if cells and cells[0] in ("Source", "File"):
            continue
        yield cells


def is_stage_context(rel):
    return os.path.basename(rel) == "CONTEXT.md" and "/stages/" in posix(rel)


def main(root, strict):
    root = os.path.abspath(root)
    V = not strict  # skip vendored skills/ for style rules unless --strict

    # -- Quality Guardrails -------------------------------------------------
    rule("CONTEXT.md under 80 lines",
         ["%s (%d)" % (r, len(read(p).splitlines()))
          for r, p in walk_files(root, ".md") if os.path.basename(r) == "CONTEXT.md"
          and len(read(p).splitlines()) > 80])

    L3 = ("references", "shared", "brand-vault", "design-system", "skills")
    rule("Reference files under 200 lines",
         ["%s (%d)" % (r, len(read(p).splitlines()))
          for r, p in walk_files(root, ".md", skip_vendored=V)
          if any("/%s/" % d in posix(r) for d in L3)
          and len(read(p).splitlines()) > 200])

    rule("No em dashes (U+2014)",
         ["%s (%d)" % (r, read(p).count(EM_DASH))
          for r, p in walk_files(root, (".md", ".txt", ".py", ".js", ".tsx"), skip_vendored=V)
          if EM_DASH in read(p)])

    rule("Empty persistent folders carry .gitkeep",
         [r for r, p in walk_dirs(root) if not os.listdir(p)])

    # -- Naming Conventions -------------------------------------------------
    rule("No spaces in file or folder names",
         sorted({r for r, _ in walk_files(root) if " " in r}
                | {r for r, _ in walk_dirs(root) if " " in r}))

    rule("Names are lowercase-with-hyphens",
         sorted({r for r, _ in list(walk_files(root, skip_vendored=V))
                 + list(walk_dirs(root, skip_vendored=V))
                 if os.path.basename(r) not in NAME_EXEMPT
                 and not LOWER_RE.match(os.path.basename(r))}))

    rule("Stage folders use a zero-padded numeric prefix",
         [r for r, _ in walk_dirs(root)
          if re.search(r"(^|/)stages/[^/]+$", r.replace(os.sep, "/"))
          and not STAGE_RE.match(os.path.basename(r))])

    # -- Pattern 1: stage contracts ----------------------------------------
    bad = []
    for r, p in walk_files(root, ".md"):
        if not is_stage_context(r):
            continue
        s = sections(read(p))
        try:
            if not s.index("Inputs") < s.index("Process") < s.index("Outputs"):
                bad.append("%s: out of order %s" % (r, s))
        except ValueError:
            bad.append("%s: missing Inputs/Process/Outputs, has %s" % (r, s))
    rule("Stage CONTEXT.md has Inputs, Process, Outputs in order", bad)

    # -- Pattern 4: every Inputs row names a section scope ------------------
    rule("Inputs rows carry a Section/Scope value",
         ["%s: %s" % (r, cells[:2])
          for r, p in walk_files(root, ".md") if is_stage_context(r)
          for cells in inputs_rows(read(p)) if len(cells) < 4 or not cells[2]])

    # -- Pattern 3: one-way cross-references --------------------------------
    # Works for both layouts: <root>/stages/NN-x and <root>/workspaces/<ws>/stages/NN-x
    edges = collections.defaultdict(set)
    for r, p in walk_files(root, ".md"):
        m = re.search(r"(?:(workspaces/[^/]+)/)?stages/(\d{2}-[a-z0-9-]+)/", posix(r))
        if not m:
            continue
        ws, src = (m.group(1) or "."), m.group(2)
        for tgt in set(re.findall(r"\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*", read(p))):
            if tgt != src and os.path.isdir(os.path.join(root, ws, "stages", tgt)):
                edges[(ws, src)].add(tgt)
    rule("Stage cross-references are one-way",
         sorted({"%s: %s <-> %s" % (ws, *sorted([s, t]))
                 for (ws, s), ts in edges.items() for t in ts
                 if s in edges.get((ws, t), ())}))

    # -- Pattern 2 / definition of done: no committed stage outputs ---------
    rule("Output folders contain only .gitkeep",
         ["%s: %s" % (r, sorted(set(os.listdir(p)) - {".gitkeep"}))
          for r, p in walk_dirs(root) if os.path.basename(r) == "output"
          and set(os.listdir(p)) - {".gitkeep"}])

    # -- Inputs-table paths actually resolve --------------------------------
    # The filesystem is the orchestration layer, so a wrong path here is an
    # uncaught bug. Per-run outputs are gitignored by design and are skipped.
    bad = []
    for r, p in walk_files(root, ".md"):
        if not is_stage_context(r):
            continue
        base = os.path.dirname(p)
        for cells in inputs_rows(read(p)):
            for ref in re.findall(r"`([^`]+)`", cells[1] if len(cells) > 1 else ""):
                ref = ref.strip()
                if not ref or ref.startswith("http"):
                    continue
                if not ("/" in ref or ref.endswith(".md")):
                    continue
                if any(m in ref for m in RUNTIME_MARKERS):
                    continue
                if re.search(r"/(output|input)/", ref):   # gitignored per-run artifact
                    continue
                if not os.path.exists(os.path.normpath(os.path.join(base, ref))):
                    bad.append("%s -> %s" % (r, ref))
    rule("Inputs-table paths resolve", bad)

    # -- Every workspace is registered in both routing tables (repo layout) --
    ws_dir = os.path.join(root, "workspaces")
    bad = []
    if os.path.isdir(ws_dir):
        readme = read(os.path.join(root, "README.md")) if os.path.exists(
            os.path.join(root, "README.md")) else ""
        claude = read(os.path.join(root, "CLAUDE.md")) if os.path.exists(
            os.path.join(root, "CLAUDE.md")) else ""
        for w in sorted(os.listdir(ws_dir)):
            if not os.path.isdir(os.path.join(ws_dir, w)):
                continue
            missing = [n for n, t in (("README.md", readme), ("CLAUDE.md", claude))
                       if w not in t]
            if missing:
                bad.append("%s: absent from %s" % (w, ", ".join(missing)))
    rule("Every workspace is registered in README and root CLAUDE.md", bad)

    # -- No placeholder link targets ----------------------------------------
    rule("Markdown links have real targets",
         ["%s: %s" % (r, m.group(0))
          for r, p in walk_files(root, ".md", skip_vendored=V)
          for m in PLACEHOLDER_LINKS.finditer(read(p))])

    # -- Folders named in the README exist ----------------------------------
    bad = []
    readme_path = os.path.join(root, "README.md")
    if os.path.exists(readme_path):
        real = {os.path.basename(r) for r, _ in walk_dirs(root)}
        for name in sorted(set(re.findall(r"^\s{2,}([a-z_][a-z0-9_-]*)/\s+#",
                                          read(readme_path), re.M))):
            if name not in real:
                bad.append("README describes %s/ but no such directory exists" % name)
    rule("Directories described in the README exist", bad)

    # -- Placeholders: questionnaire <-> files, per workspace (added) -------
    bad = []
    for r, q in walk_files(root, ".md"):
        if is_doc(r) or r.replace(os.sep, "/").split("/")[-2:] != ["setup", "questionnaire.md"]:
            continue
        ws_root = os.path.dirname(os.path.dirname(q))
        label = os.path.relpath(ws_root, root)
        declared = {family(n) for n in VALUE_PH.findall(read(q))} - META_TOKENS
        used = collections.defaultdict(set)
        for r2, p2 in walk_files(ws_root, ".md"):
            if p2 == q or in_output(r2):
                continue
            for name in VALUE_PH.findall(read(p2)):
                if name not in META_TOKENS:
                    used[family(name)].add(r2)
        for name in sorted(set(used) - declared):
            bad.append("%s: {{%s}} in %s has no question"
                       % (label, name, ", ".join(sorted(used[name])[:3])))
        for name in sorted(declared - set(used)):
            bad.append("%s: question declares {{%s}} but no file contains it" % (label, name))
    rule("Placeholders match the questionnaire both ways", bad)

    # -- No bracket-style placeholders (added) ------------------------------
    rule("No bracket-style placeholders (use {{NAME}})",
         ["%s: %s" % (r, ", ".join(sorted(set(BRACKET_PH.findall(read(p))))[:4]))
          for r, p in walk_files(root, ".md", skip_vendored=V)
          if not is_doc(r) and not in_output(r) and BRACKET_PH.search(read(p))])

    # -- Conditional sections balanced (added) ------------------------------
    bad = []
    for r, p in walk_files(root, ".md"):
        if is_doc(r) or in_output(r):
            continue
        t = read(p)
        opens = collections.Counter(COND_OPEN.findall(t))
        closes = collections.Counter(COND_CLOSE.findall(t))
        for name in sorted(set(opens) | set(closes)):
            if opens[name] != closes[name]:
                bad.append("%s: {{?%s}} x%d vs {{/%s}} x%d"
                           % (r, name, opens[name], name, closes[name]))
    rule("Conditional sections are balanced", bad)

    # -- report -------------------------------------------------------------
    failed = 0
    for name, bad, note in results:
        if bad:
            failed += 1
            print("FAIL  %-52s %d" % (name, len(bad)))
            for b in bad[:6]:
                print("        - %s" % b)
            if len(bad) > 6:
                print("        ... and %d more" % (len(bad) - 6))
        else:
            print("PASS  %s" % name)
    print("\n%d/%d rules passed%s" % (len(results) - failed, len(results),
                                      "" if strict else "  (skills/ skipped; --strict to include)"))
    return 1 if failed else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    sys.exit(main(args[0] if args else ".", "--strict" in sys.argv))
```

What it cannot check: whether a Process step is concrete enough, whether an audit's pass condition is unambiguous, whether a contract contains reference content, or whether the spec stage leaks implementation detail. Those stay in the validation stage's checklist (section 6.5) for the agent and the human.

## Appendix B: A Complete Minimal Workspace

The repo ships no filled-in example in one place: its workspaces are spread over dozens of files and their `output/` folders are empty by rule. This appendix is one small, complete, convention-compliant workspace in a neutral domain: a topic becomes a sourced research brief, the brief becomes an article draft, the draft becomes a publish package (titles, summary, social posts). Three stages, one optional. Copy its shape, not its domain.

Every file is preceded by an HTML comment naming its path. The script below materializes the workspace from this guide, which is also how the guide was tested:

```python
# materialize.py: python3 materialize.py ICM-BUILD-GUIDE.md target-dir
import re, sys, pathlib
guide, target = sys.argv[1], pathlib.Path(sys.argv[2])
lines = open(guide, encoding="utf-8").read().splitlines()
i = 0
while i < len(lines):
    m = re.match(r"<!-- file: (\S+) -->", lines[i])
    if m:
        j = i + 1
        while not lines[j].startswith("```"):
            j += 1
        fence = re.match(r"`+", lines[j]).group(0)
        k = j + 1
        while lines[k].strip() != fence:
            k += 1
        out = target / m.group(1)
        out.parent.mkdir(parents=True, exist_ok=True)
        body = "\n".join(lines[j + 1:k])
        out.write_text(body + ("\n" if body else ""), encoding="utf-8")
        i = k
    i += 1
```

Then `python3 validate.py target-dir/article-pipeline` (Appendix A) passes every rule, and `cd target-dir/article-pipeline` followed by `setup` in Claude Code configures it.

### B.1 Layout

```
article-pipeline/
├── CLAUDE.md
├── CONTEXT.md
├── .gitignore
├── setup/
│   └── questionnaire.md
├── brand-vault/
│   ├── CONTEXT.md
│   ├── identity.md
│   └── voice-rules.md
├── shared/
│   └── platform-specs.md
└── stages/
    ├── 01-research/   CONTEXT.md, references/source-rules.md, output/.gitkeep
    ├── 02-draft/      CONTEXT.md, references/article-structure.md, references/value-framework.md, output/.gitkeep
    └── 03-package/    CONTEXT.md, references/package-format.md, output/.gitkeep
```

### B.2 Layer 0 and Layer 1

<!-- file: article-pipeline/CLAUDE.md -->
````markdown
# Article Pipeline

Turn a topic into a sourced research brief, an article draft in your voice, and a publish package, one stage at a time.

## Folder Map

```
article-pipeline/
├── CLAUDE.md              (you are here)
├── CONTEXT.md             (start here for task routing)
├── setup/questionnaire.md (run with "setup")
├── brand-vault/           (identity and voice rules, with its own CONTEXT.md)
├── shared/platform-specs.md (word budgets per publication type)
└── stages/
    ├── 01-research/       (topic -> sourced brief)
    ├── 02-draft/          (brief -> article draft)
    └── 03-package/        (draft -> titles, summary, social posts)
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run the onboarding questionnaire: brand, audience, voice, platform |
| `status` | Show pipeline completion for all stages |

### How `status` works

Scan `stages/*/output/`. A stage is COMPLETE if its output folder contains files other than `.gitkeep`, otherwise PENDING. Render:

```
Pipeline Status: article-pipeline

  [01-research]  ------>  [02-draft]  ------>  [03-package]
     STATUS                 STATUS               STATUS
  (files...)             (files...)           (files...)
```

## Routing

| Task | Go To |
|------|-------|
| Research a topic | `stages/01-research/CONTEXT.md` |
| Write the article | `stages/02-draft/CONTEXT.md` |
| Package for publishing | `stages/03-package/CONTEXT.md` |
| Configure this workspace | `setup/questionnaire.md` |

## What to Load

| Task | Load These | Do NOT Load |
|------|-----------|-------------|
| Research a topic | `brand-vault/identity.md` ("Audience"), `stages/01-research/references/*` | `brand-vault/voice-rules.md`, `stages/02-draft/`, `stages/03-package/` |
| Write the article | `stages/01-research/output/`, `brand-vault/voice-rules.md` ("Hard Constraints" through "What the Voice Is NOT"), `brand-vault/identity.md`, `stages/02-draft/references/*`, `shared/platform-specs.md` | `stages/01-research/references/`, `stages/03-package/` |
| Package for publishing | `stages/02-draft/output/`, `stages/03-package/references/*` | `brand-vault/`, `stages/01-research/`, `stages/02-draft/references/` |

## Stage Handoffs

Each stage writes to its own `output/`. The next stage reads from there. If you edit an output file between stages, the next stage picks up your edits. That is the primary way to steer the pipeline.

Git policy: `output/` contents are per-run products and are ignored; commit the workspace definition only.
````

<!-- file: article-pipeline/CONTEXT.md -->
```markdown
# Article Pipeline Workspace

Take a topic through research, drafting, and packaging.

## Task Routing

| Task Type | Go To | Description |
|-----------|-------|-------------|
| Research a topic | `stages/01-research/CONTEXT.md` | Produces a sourced brief with citations |
| Write the article | `stages/02-draft/CONTEXT.md` | Produces a full draft in the brand voice |
| Package for publishing | `stages/03-package/CONTEXT.md` | Produces titles, a summary, and social posts |

{{?PACKAGE_STAGE}}

### Package Stage

The package stage (03-package) writes titles, a summary, and social posts for the finished draft. If you publish without that step, this stage can be removed during onboarding.

{{/PACKAGE_STAGE}}

## Shared Resources

| Resource | Location | Contains |
|----------|----------|----------|
| Brand context | `brand-vault/CONTEXT.md` | Routes to identity and voice rules |
| Platform specs | `shared/platform-specs.md` | Word budgets and format per publication type |
```

<!-- file: article-pipeline/.gitignore -->
```
**/stages/*/output/*
!**/stages/*/output/.gitkeep
.env
.env.local
.DS_Store
*-ref/
```

### B.3 The configuration folder

<!-- file: article-pipeline/brand-vault/CONTEXT.md -->
```markdown
# Brand Vault

Identity and voice rules for this workspace. Stages load specific sections as their Inputs tables direct.

| File | Key Sections | Load When |
|------|-------------|-----------|
| `voice-rules.md` | "Hard Constraints", "Sentence Rules", "Pacing", "What the Voice Is NOT" | Writing any prose |
| `voice-rules.md` | "Strategic Rationale" | Understanding why the voice is what it is (rarely needed) |
| `identity.md` | "One-Sentence Brand", "Audience" | Knowing who you are writing for |
| `identity.md` | "Content Mission" | Judging whether a draft serves the brand |
```

<!-- file: article-pipeline/brand-vault/identity.md -->
```markdown
# Identity: {{BRAND_NAME}}

## One-Sentence Brand

{{BRAND_MISSION}}

## Audience

- **Who:** {{TARGET_AUDIENCE}}
- **What they care about:** {{AUDIENCE_CARES_ABOUT}}
- **What they already know:** {{AUDIENCE_KNOWLEDGE_LEVEL}}
- **What they do not need:** explanations of things they already understand. If the audience can finish your sentence, cut it.

## Content Mission

Every article should leave the reader able to do or decide something they could not before. If a finished draft does not clearly serve this mission, it needs reworking before it moves to packaging.
```

<!-- file: article-pipeline/brand-vault/voice-rules.md -->
```markdown
# Voice Rules: {{BRAND_NAME}}

## Hard Constraints

These are errors. If a draft contains any of these, rewrite before saving.

1. {{VOICE_HARD_CONSTRAINT_1}}
2. {{VOICE_HARD_CONSTRAINT_2}}
3. {{VOICE_HARD_CONSTRAINT_3}}
4. No em dashes. Use a comma, a period, or `--`.
5. No hype words: revolutionary, game-changing, seamless, unlock.
6. No claim without a source in the brief.

## Sentence Rules

| Wrong | Right |
|-------|-------|
| {{VOICE_WRONG_EXAMPLE_1}} | {{VOICE_RIGHT_EXAMPLE_1}} |
| {{VOICE_WRONG_EXAMPLE_2}} | {{VOICE_RIGHT_EXAMPLE_2}} |
| "They invested significant time in infrastructure development." | "They spent six months building a custom pipeline." |
| "It is important to note that costs may vary." | "Costs vary. Here is why." |

## Pacing

{{VOICE_PACING_DESCRIPTION}}

## What the Voice Is NOT

- **Not antithetical.** "Not X, but Y" once per article at most.
- **Not rhetorical.** Questions the reader cannot answer are filler. Bad: "But what does this mean for the future?" Fine: "So what do you actually change on Monday?"

## Strategic Rationale

Concrete sentences are checkable; abstract ones are not. The wrong/right pairs above exist so the agent can pattern-match instead of interpret. Agents writing prose load the sections above this one and skip this section.
```

<!-- file: article-pipeline/shared/platform-specs.md -->
```markdown
# Platform Specs

## Active Platform

This workspace is configured for **{{PRIMARY_PLATFORM}}** with a target length of **{{TARGET_WORD_COUNT}}** words. The tables below stay complete so the platform can be changed by editing the line above.

## Publication Types

| Type | Length | Format notes |
|------|--------|--------------|
| Blog post | 800-1500 words | H2 sections, one idea per section, no H4 |
| Newsletter issue | 400-800 words | Short paragraphs, one link per section |
| Long-form essay | 1500-3000 words | Sections may nest one level; a summary up top |
```

### B.4 Stage 01: Research

<!-- file: article-pipeline/stages/01-research/CONTEXT.md -->
```markdown
# Stage 01: Research

Take a topic and produce a sourced brief. The brief is a plan; the cited sources are the authority.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | (conversation) | Topic, angle hints, any source pointers | The starting point for this run |
| Brand vault | `../../brand-vault/identity.md` | "Audience" | Know what the reader already knows; do not restate it |
| Reference | `references/source-rules.md` | Full file | What counts as a source, how to cite it, the brief format |

## Process

1. Restate the topic in one sentence and name the slug that will prefix every artifact in this run
2. Identify 3-7 primary sources (papers, official documentation, company reports, named people quoted in reputable outlets). Skip listicles and unattributed blogs.
3. Pull the specific claims you intend to use. Each claim gets a source link; numbers and direct arguments get a verbatim quote.
4. Note conflicts. If two reputable sources disagree, the brief says so.
5. Draft the brief in the format from source-rules.md: summary, claims with citations, angle, open questions
6. Run the audit checks below. If any fail, revise before saving
7. Save to `output/[topic-slug]-brief.md`

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | Restated topic and slug | Confirm or redirect before sources are gathered |
| 5 | Draft brief with claims and citations | Approve, request more sources, or change the angle |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Source quality | Every claim has a primary or reputable secondary source; no "studies show" without a citation |
| Number accuracy | Every quantitative claim is a quote or a computed value from a named source |
| Audience fit | The brief assumes only what the Audience section says readers already know |
| Conflict surfacing | Disagreements between sources appear in the brief, not buried |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Research brief | `output/[topic-slug]-brief.md` | Markdown: Summary, Claims, Angle, Open Questions, Sources |

The brief in `output/` is the human edit surface. Cut claims, add sources, change the angle. The draft stage reads whatever is in that file.
```

<!-- file: article-pipeline/stages/01-research/references/source-rules.md -->
````markdown
# Source Rules

## What Counts as a Source

| Tier | Examples | Use for |
|------|----------|---------|
| Primary | Peer-reviewed papers, official documentation, primary data, first-party announcements | Any number or direct claim |
| Reputable secondary | Named journalists at established outlets, named experts quoted on the record | Context and interpretation |
| Not a source | Top-N listicles, unattributed blogs, AI-generated summaries, forum posts | Leads only; verify elsewhere |

## Citation Format

Inline, numbered, with the list at the end:

```
The median run took 6.2 minutes [3].

## Sources
[3] Author or Organization, "Title", Outlet, date, URL (accessed YYYY-MM-DD)
```

Quote numbers verbatim in the claim list so the writer never rounds twice.

## Brief Format

```
# [Topic]: research brief

## Summary
One paragraph: what this is, why the reader cares, the one surprising thing.

## Claims
- [claim] [n]  (verbatim quote if a number or a direct argument)

## Angle
The takeaway in one sentence, and what the reader will be able to do with it.

## Open Questions
Anything the human should decide or verify before drafting.

## Sources
```
````

<!-- file: article-pipeline/stages/01-research/output/.gitkeep -->
```
```

### B.5 Stage 02: Draft

<!-- file: article-pipeline/stages/02-draft/CONTEXT.md -->
```markdown
# Stage 02: Draft

Take the brief and write the full article in the brand voice.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../01-research/output/[topic-slug]-brief.md` | Full file | Claims, citations, angle |
| Brand vault | `../../brand-vault/voice-rules.md` | "Hard Constraints" through "What the Voice Is NOT" | Tone discipline |
| Brand vault | `../../brand-vault/identity.md` | "One-Sentence Brand" and "Audience" | Who is being addressed |
| Reference | `references/article-structure.md` | Full file | Required structure and metadata header |
| Reference | `references/value-framework.md` | Full file | Value types to lock before drafting |
| Shared | `../../shared/platform-specs.md` | Row for {{PRIMARY_PLATFORM}} | Word budget and format |

## Process

1. Read the brief
2. Propose three angles, one sentence each, tagged with the value types each would deliver
3. **[Checkpoint]** -- Present the angles; the human picks one or redirects
4. Outline the article: hook, promise, sections (one idea each), close
5. Write the full draft in one pass, following the voice rules, the outline, and the word budget
6. Run the audit checks below. If any fail, revise before saving
7. Add the metadata header from article-structure.md
8. Save to `output/[topic-slug]-draft.md`

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | Three angles with value tags | Which angle to pursue, combine, or redirect |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Voice constraints | Zero violations of the Hard Constraints in voice-rules.md |
| Value delivery | The draft delivers the value types locked at the checkpoint |
| Word budget | Within +/-10% of the target in platform-specs.md |
| Claims sourced | Every quantitative claim traces to a numbered source in the brief |
| Structure | Hook, promise, one-idea sections, and close are all present |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Article draft | `output/[topic-slug]-draft.md` | Markdown with metadata header and body |

The draft in `output/` is the human edit surface. Rewrite lines, cut sections, sharpen the close. The package stage reads whatever is in that file.
```

<!-- file: article-pipeline/stages/02-draft/references/article-structure.md -->
````markdown
# Article Structure

## Metadata Header

Every draft starts with:

```
---
title-working: [working title]
source-brief: [topic-slug]-brief.md
value-types: [from value-framework.md]
target-words: [from platform-specs.md]
---
```

## Structure

1. **Hook** (1-2 sentences): the specific thing, not the category. A number, a named case, a concrete scene.
2. **Promise** (1 sentence): what the reader will be able to do or decide by the end.
3. **Sections** (3-5): one idea each, H2 headings, each ending on something usable.
4. **Close** (2-3 sentences): the promise delivered, said plainly. No summary of the summary, no question to the reader.

## Rules

- One concept per section. If a section explains two things, split it.
- Numbers appear as comparisons ("twice as fast as"), never bare.
- Every technical term gets a plain definition in the same sentence.
- The last line is something a reader could repeat to a colleague.
- {{BRAND_NAME}} articles never open with a definition or a dictionary quote.
````

<!-- file: article-pipeline/stages/02-draft/references/value-framework.md -->
```markdown
# Value Framework

A piece that tries to deliver every kind of value delivers none. Lock two before drafting.

## Value Types

### TEACHES
The reader understands something they did not before, well enough to explain it.

### EQUIPS
The reader can do something in the next week: a technique, a checklist, a decision rule.

### REFRAMES
The reader sees a familiar thing differently, and the new frame changes a decision.

## How to Use

At the angles checkpoint (Process step 2 of the draft stage), tag each angle with the types it naturally delivers. The chosen angle's types are locked and checked in the audit.
```

<!-- file: article-pipeline/stages/02-draft/output/.gitkeep -->
```
```

### B.6 Stage 03: Package

<!-- file: article-pipeline/stages/03-package/CONTEXT.md -->
```markdown
# Stage 03: Package

Take the finished draft and produce everything needed to publish it: title options, a summary, and social posts.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../02-draft/output/[topic-slug]-draft.md` | Full file | The article to package |
| Reference | `references/package-format.md` | Full file | Package layout, title rules, per-platform limits |

## Process

1. Read the draft
2. Write five title options following the title rules, and mark the one you recommend
3. **[Checkpoint]** -- Present the titles; the human picks one
4. Write the summary and one post per social platform within the limits in package-format.md
5. Run the audit checks below. If any fail, revise before saving
6. Save to `output/[topic-slug]-package.md`

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | Five titles with a recommendation | Which title to use, or a direction for new ones |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Title length | Chosen title is 70 characters or fewer and contains the article's key term |
| No new claims | Every fact in the summary and posts appears in the draft |
| Limits | Every post is within its platform's character limit |
| Voice | Posts read like the draft, not like an advertisement |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Publish package | `output/[topic-slug]-package.md` | Markdown: Title, Summary, Posts, Call to Action |

The package in `output/` is the human edit surface and the last stop. Edit it, then publish from it.
```

<!-- file: article-pipeline/stages/03-package/references/package-format.md -->
````markdown
# Package Format

## Layout

```
# Package: [title]

## Title
[chosen title]   (alternatives listed below it)

## Summary
2-3 sentences: what the article says and who should read it.

## Posts
### [platform]
[post text]

## Call to Action
{{CALL_TO_ACTION}}
```

## Title Rules

- 70 characters or fewer; key term in the first half
- Say the specific thing, not the category ("Why the 6-minute research cap works", not "Thoughts on research")
- Never restate the hook sentence verbatim

## Social Platforms

Write one post for each of: {{SOCIAL_PLATFORMS}}.

| Platform | Limit | Notes |
|----------|-------|-------|
| LinkedIn | 1,300 characters visible before the fold; 3,000 max | First line carries the hook; no hashtags in the body |
| X | 280 characters | One idea; no link in the first line |
| Newsletter blurb | 80 words | Summary plus a reason to click |
````

<!-- file: article-pipeline/stages/03-package/output/.gitkeep -->
```
```

### B.7 The questionnaire

<!-- file: article-pipeline/setup/questionnaire.md -->
```markdown
# Onboarding Questionnaire: Article Pipeline

Read this file when the user types "setup". Ask ALL questions below in a single conversational pass. The user should be able to answer everything in one message. These configure the production system, not a specific article. Topics are provided at the start of each run.

### Q1: What is your brand, publication, or project name?
- Placeholder: `{{BRAND_NAME}}`
- Files: `brand-vault/identity.md`, `brand-vault/voice-rules.md`, `stages/02-draft/references/article-structure.md`
- Type: free text

### Q2: What does it do, in one sentence?
- Placeholder: `{{BRAND_MISSION}}`
- Files: `brand-vault/identity.md`
- Type: free text
- Example: "Practical guides for engineers running AI on their own hardware."

### Q3: Who is your reader, what do they care about, and what do they already know?
- Placeholders: `{{TARGET_AUDIENCE}}`, `{{AUDIENCE_CARES_ABOUT}}`, `{{AUDIENCE_KNOWLEDGE_LEVEL}}`
- Files: `brand-vault/identity.md`
- Type: free text

### Q4: Give me two sentences that sound exactly like you.
- Placeholders: `{{VOICE_RIGHT_EXAMPLE_1}}`, `{{VOICE_RIGHT_EXAMPLE_2}}`
- Files: `brand-vault/voice-rules.md`
- Type: free text

### Q5: Give me two sentences you would never write.
- Placeholders: `{{VOICE_WRONG_EXAMPLE_1}}`, `{{VOICE_WRONG_EXAMPLE_2}}`
- Files: `brand-vault/voice-rules.md`
- Type: free text
- Note: pair each with the Q4 sentence it contrasts with; the agent fills the Wrong/Right table in that order

### Q6: List things that are always errors in your writing (phrases, habits, structures).
- Placeholders: `{{VOICE_HARD_CONSTRAINT_1}}`, `{{VOICE_HARD_CONSTRAINT_2}}`, `{{VOICE_HARD_CONSTRAINT_3}}`
- Files: `brand-vault/voice-rules.md`
- Type: free text
- Note: if fewer than three are given, the agent derives the rest from Q4 and Q5
- Derived from Q4-Q6 (not asked): `{{VOICE_PACING_DESCRIPTION}}` in `brand-vault/voice-rules.md`, two sentences on rhythm and paragraph length

### Q7: Where does this publish, and how long should a piece be?
- Placeholders: `{{PRIMARY_PLATFORM}}`, `{{TARGET_WORD_COUNT}}`
- Files: `shared/platform-specs.md`, `stages/02-draft/CONTEXT.md`
- Type: selection for platform (Blog post, Newsletter issue, Long-form essay); number for words
- Default: Blog post, 1200

### Q8: Do you want a packaging stage (titles, summary, social posts)?
- Type: yes/no
- If NO: remove `stages/03-package/` and the `{{?PACKAGE_STAGE}}` ... `{{/PACKAGE_STAGE}}` block in `CONTEXT.md`, and drop the package row from the routing tables in `CLAUDE.md`
- If YES, two more answers:
  - Placeholder: `{{SOCIAL_PLATFORMS}}` in `stages/03-package/references/package-format.md` (default: LinkedIn, X)
  - Placeholder: `{{CALL_TO_ACTION}}` in `stages/03-package/references/package-format.md` (example: "Subscribe at example.org/newsletter")

---

## After Onboarding (Two-Pass Process)

**Pass 1:** Replace every placeholder above across the listed files. Apply Q8.

**Pass 2 (Voice Review):** Show the populated Hard Constraints, Sentence Rules table, and Pacing from `brand-vault/voice-rules.md` and say: "Here are the voice rules I derived from your examples. Edit anything that does not match how you actually write." Apply the edits.

Then scan every `.md` file for `{{[A-Z][A-Z0-9_]*}}` and `{{?` tokens. Resolve any that remain.

Tell the user: "You are set up. To start an article, give me a topic and we will begin at Stage 01."
```

### B.8 What this example shows

- Every stage contract is under 55 lines and contains no reference content; everything reusable sits in `references/` or `brand-vault/`.
- Layer 3 and Layer 4 are separated by folder: `brand-vault/`, `shared/`, `references/` are the factory; `output/` is the product.
- Inputs rows name sections; the What to Load table in `CLAUDE.md` names exclusions and agrees with the Inputs tables.
- The creative stages have checkpoints placed where direction is set (angles, titles) and audits with falsifiable pass conditions; the research stage has an early scope checkpoint.
- Placeholders sit beside shipped defaults; one derived field is declared under the question it depends on; the optional stage is a conditional block that wraps a whole section; every placeholder has a question and every question has a target.
- The closing sentence of each contract names the edit surface and tells the next stage to read what is there.

## Appendix C: Known Upstream Defects and Fixes Applied

Found by checking the repo at `02ba5d8` against its own conventions, and in its open pull requests. Listed so that anyone cloning the repo knows what to correct, and so that the differences between this guide and the repo are explicit.

| # | Where | Defect | What this guide does |
|---|---|---|---|
| 1 | `workspaces/workspace-builder/**` (29 references in 6 files) | `_core` paths written as `/_core/...`, which is the filesystem root; the scaffolding and validation stages cannot reach the templates or conventions (PR #10) | Section 6 carries the templates inline and states the correct relative forms (6.9) |
| 2 | Root `CLAUDE.md`, `README.md` | `voice-driven-animation` missing from the folder map, the routing table, and the workspace table (PR #11) | Section 7 treats it as a first-class reference; pitfall 6 makes registration a rule; the validator checks it |
| 3 | `_core/CONVENTIONS.md`, root `CLAUDE.md`, README Origin section | Still named "MWP" / "Model Workspace Protocol"; root `CLAUDE.md` title misspelled "Interpreted-Context-Methdology"; folder map root `model-workspace-protocol/` (PR #12) | All text uses ICM |
| 4 | `README.md` | Describes a `_config/` folder no workspace has; the real configuration folders are `brand-vault/` and `design-system/` (PR #13) | Section 3.2 uses the real names and notes the paper's figure |
| 5 | `workspaces/workspace-builder/references/conventions-reference.md` | Skips Pattern 8, the pattern the questionnaire stage needs most (PR #13) | Section 4 is complete |
| 6 | `.gitignore` | No `__pycache__/` or `*.pyc` rule despite 15 bundled Python scripts (PR #13) | Section 6.8 includes them |
| 7 | `README.md` Origin section | Paper citation links to `link-to-paper`, a 404, under the old project name; the working arXiv link is 249 lines earlier (issue #4, PRs #5, #9) | The header of this guide carries the arXiv link |
| 8 | Repo root | No validator, CI, or `.github/` (PR #14 proposes one; 11 of its 15 rules pass on `main`, the four failures being defects 1, 2, 4, and 7) | Appendix A adapts and extends the validator |
| 9 | `script-to-animation/setup/questionnaire.md` | `{{VOICE_ADJECTIVES}}` declared for `voice-rules.md` but present in no file; `{{TARGET_DURATION}}` declared for a contract that does not contain it; `build-conventions.md` listed as a color/font target but contains no placeholders | Pitfall 4; validator rule "placeholders match the questionnaire both ways" |
| 10 | `script-to-animation/stages/03-build/references/build-conventions.md` | JSX `style={{ opacity }}` trips the `{{` completion sweep | Section 5.2 correction; validator uses exact token shapes |
| 11 | `script-to-animation/CLAUDE.md` | What to Load row for the spec task globs in `component-registry.md`, which the spec audit forbids; the build row omits it although the build stage loads it | Pitfall 2 |
| 12 | `script-to-animation/CLAUDE.md`, `CONTEXT.md`, builder example summary | "35 rule files" (33 exist); the skill's own index lists 29 | Pitfall 20 |
| 13 | `script-to-animation` | Pattern 15 required by the build audit but no constants file shipped | Pitfall 14; scaffolding step 8 |
| 14 | `course-deck-production/stages/04-generation/references/build-conventions.md` | `require('../../skills/pptx/scripts/html2pptx.js')` from a file four levels deep; needs `../../../../`; no `package.json`; no setup guide for Node, `pptxgenjs`, `sharp`, LibreOffice, poppler | Pitfalls 1 and 8 |
| 15 | Same file | Bracket-style `[INSTRUCTOR_NAME]`, `[SESSION_TITLE]`, `[BODY_FONT]` that `setup` never replaces; `[BODY_FONT]` duplicates `{{BODY_FONT}}` | Pitfall 3; validator rule |
| 16 | `course-deck-production/setup/questionnaire.md` vs `design-system/typography.md` | Font list of 7 versus 9 | Pattern 5 reminder in section 7.2 |
| 17 | `course-deck-production/CLAUDE.md`, `voice-driven-animation/CLAUDE.md` | `status` render drops the artifact filename line | Section 3.6 keeps it; pitfall 13 |
| 18 | `course-deck-production/skills/pptx/` | About 900 KB of OOXML schemas and four scripts nothing routes to | Pitfall 9 |
| 19 | All workspaces | No `input/` folder for user-provided source material; it enters via chat and is not on disk | Pitfall 7; section 6.8 ignore rule |
| 20 | `voice-driven-animation/stages/03-voice/CONTEXT.md` vs `references/audio-pipeline.md` vs `scripts/generate-audio.py` | Output paths and script arguments disagree three ways (`output/audio.mp3`, `audio/video1.mp3`, `{topic-slug}` versus `video1`) | Pitfall 11 |
| 21 | `voice-driven-animation/setup/questionnaire.md` | `{{PROJECT_SHAPE}}`, `{{VOICE_ADJECTIVES}}`, and `{{CONTENT_PILLAR_1}}` through `{{CONTENT_PILLAR_5}}` declared but absent from every file (the validator in Appendix A reports all four orphan families across the repo) | Pitfall 4 |
| 22 | `voice-driven-animation/shared/env-template.md` | Says stage outputs "are committed normally"; the ignore file excludes them | Pitfall 17 |
| 23 | `voice-driven-animation/stages/04-animate/CONTEXT.md` | `External` row depends on a sibling workspace's skill; the workspace is not standalone | Pitfall 10 |
| 24 | `voice-driven-animation` reference files | A real company URL, a prior tagline, and a hardcoded font sit beside placeholders | Pitfall 18 |
| 25 | `voice-driven-animation/skills/whisper-beat-finder/scripts/find-beats.py` | Drops unmatched beats silently; the `BEATS` list is hardcoded in the script | Pitfall 12 |
| 26 | `_core/placeholder-syntax.md` | Says placeholders must not appear in top-level `CONTEXT.md` routing tables, while `script-to-animation/CONTEXT.md` carries `{{?BUILD_STAGE}}` outside the table | Section 5.2 states the distinction explicitly |

## Appendix D: Glossary

| Term | Meaning |
|---|---|
| Workspace | A folder that is a complete ICM pipeline: routing files, numbered stages, configuration, shared files, optional skills, a questionnaire |
| Stage | One numbered folder that does one job: reads defined inputs, transforms, writes a defined output |
| Stage contract | The stage's `CONTEXT.md`: Inputs, Process, Checkpoints, Audit, Outputs |
| Layer 0 / 1 / 2 | `CLAUDE.md` (where am I), workspace `CONTEXT.md` (where do I go), stage `CONTEXT.md` (what do I do) |
| Layer 3 | Reference material: stable rules and knowledge configured once (references, configuration folder, shared, skills). The factory. |
| Layer 4 | Working artifacts: previous outputs and per-run source material. The product. |
| Configuration folder | The workspace-level Layer 3 folder for identity and style: `brand-vault/`, `design-system/`, or a domain name |
| Handoff | Stage N's `output/` being stage N+1's input |
| Edit surface | Any output file the human can change before the next stage reads it |
| Checkpoint | A pause between process steps where the agent presents and the human decides |
| Audit | A checklist the agent runs after the process and before saving; unambiguous pass conditions |
| Value validation | Agreeing, before drafting, which kinds of value a piece will deliver |
| Spec as contract | A specification stage defines what and when, never how |
| Docs over outputs | Agents learn patterns from reference docs, never from earlier outputs |
| Shared constants | One file of configurable values that all generated code imports |
| Selective section routing | Inputs rows that name the sections to load, not just the file |
| Canonical source | The one home of a fact; every other file points there |
| One-way reference | If A points to B, B never points to A |
| Placeholder | `{{SCREAMING_SNAKE_CASE}}` token replaced by `setup` |
| Conditional section | `{{?NAME}}...{{/NAME}}` wrapping a whole section that `setup` may remove |
| Questionnaire | `setup/questionnaire.md`: flat, all-at-once, system-level questions that populate placeholders |
| Trigger | A bare keyword (`setup`, `status`, custom) the workspace `CLAUDE.md` declares |
| Skill | A bundled folder of domain knowledge: `SKILL.md` index, `rules/`, `scripts/` |
| Source of truth table | A per-stage statement of which artifact wins if two disagree, and what is recomputed when one is regenerated |
| Loop-back table | Symptom-to-stage routing in the final stage for error recovery |
| Incremental recompilation | Re-running only the stages whose Inputs changed |
| Edit-source principle | Recurring output edits point to a fix in the contract or reference file |
| Review gate | The human decision at each stage boundary: accept, edit the output, or fix the source and re-run |

## Appendix E: Source Index

### Paper sections to guide sections

| Paper | Guide |
|---|---|
| 1 Introduction; Table 1 | 1.1, 1.3 |
| 2.1 Composability and the Unix tradition | 2.7 |
| 2.2 Context engineering and agentic AI | 1.5, 2.2 |
| 2.3 Human oversight and observability | 2.4 |
| 3.1 Design principles | 2.1 |
| 3.2 Architecture; Figures 1-3; Table 2 | 3.1, 3.2, 3.3, 2.2 |
| 3.3 Stage contracts and handoffs; Figure 4 | 3.4, 3.5 |
| 3.4 Portability and reproducibility | 1.2, 8.7 |
| 4.1 Model and environment | 3.8, 1.6 |
| 4.2-4.4 Script-to-animation, course deck, workspace builder | 7, 6 |
| 4.5 Early practitioner experience; Figure 5 | 2.5, 8.3, 8.8 |
| 4.6 Threats to validity | 1.6 |
| 5.1-5.2 Where this works and does not | 1.4 |
| 5.3 Observability as a side effect | 2.4 |
| 5.4 Implications for intelligent system design | 2.3 |
| 6.1 Multi-pass incremental compilation | 8.4 |
| 6.2 Toward semantic debugging | Appendix F |
| 6.3 Source integrity and the edit-source principle | 2.6, 8.6 |

### Repo files (commit `02ba5d8`)

| Path | Role | Guide |
|---|---|---|
| `README.md` | Overview, getting started, conventions summary, contribution checklist | 1, 4.8 |
| `CLAUDE.md` | Root routing across workspaces | 6.0, 6.6 |
| `.gitignore` | Output and secrets ignore rules | 6.8 |
| `_core/CONVENTIONS.md` | The fifteen patterns, triggers, naming, guardrails | 4 |
| `_core/placeholder-syntax.md` | Placeholder and conditional rules | 5.2 |
| `_core/templates/workspace-claude-template.md` | Layer 0 template | 5.1.1 |
| `_core/templates/workspace-context-template.md` | Layer 1 template | 5.1.2 |
| `_core/templates/stage-context-template.md` | Layer 2 template | 5.1.3 |
| `_core/templates/questionnaire-template.md` | Questionnaire template and design rules | 5.1.4 |
| `workspaces/workspace-builder/` | Five-stage builder: discovery, mapping, scaffolding, questionnaire design, validation | 6 |
| `workspaces/workspace-builder/references/examples/script-to-animation-summary.md` | Condensed summary of a finished workspace, including the placeholder rule of thumb | 6.7, 7 |
| `workspaces/script-to-animation/` | 3 stages; brand vault; value framework; spec as contract; bundled Remotion and frontend-design skills | 7.1-7.4 |
| `workspaces/course-deck-production/` | 5 stages; design system; multi-entry; travelling metadata; bundled pptx skill | 7.4, 7.5 |
| `workspaces/voice-driven-animation/` | 5 stages; authored skills with scripts; env template; source-of-truth table; loop-back table | 7.6 |

### Pull requests and issues consulted

| Ref | Subject |
|---|---|
| PR #2 (closed, unmerged) | A research-pipeline workspace with two-layer quality gates, a `resume` trigger, and a progress file |
| Issue #4, PR #5, PR #9 | Dead paper link in the README |
| PR #6 (merged 2026-06-01) | Added `voice-driven-animation` |
| PR #10 | Absolute `/_core/` paths in the builder |
| PR #11 | Register `voice-driven-animation` in the routing tables |
| PR #12 | Complete the MWP to ICM rename |
| PR #13 | `_config/` does not exist; Pattern 8 missing from the builder's quick reference; `__pycache__` ignore |
| PR #14 | Convention validator and CI workflow |

### Origin repo

`RinDig/Content-Agent-Routing-Promptbase` (last pushed 2026-02-11, eleven days before the ICM repo was created). Four layers with the same token budgets; ICM split its Layer 3 into reference and working layers and added numbered stages. It contains what the ICM repo does not: a fully populated brand vault (brand story, voice and tone, five content pillars, author profile), a topic bank, platform playbooks and funnel documents, a production rhythm and analytics tracker, a real Remotion project with per-composition constants files, and dozens of finished scripts and animation specs. Consult it to see what filled-in Layer 3 material and good outputs look like.

## Appendix F: Optional Extensions

None of these are in the protocol. They come from the paper's future-work section, from an unmerged community workspace, and from the gaps in section 9. Adopt them one at a time, and write each one down in the workspace `CLAUDE.md` so the next reader knows the workspace deviates from the base conventions.

1. **An `input/` folder for per-run source material.** A gitignored `input/` at the workspace root (or inside the entry stage), an Inputs row pointing at it, and a line in the per-run metadata listing the files. Closes the observability gap in pitfall 7.
2. **Machine-checked audit rows.** Where a script can decide a check (schema validity, line or word counts, a file exists, a render exit code, duration within tolerance), write the script's invocation in the pass condition and have the agent run it. The agent's judgment is reserved for checks a script cannot make. This is the paper's "local scripts handle the mechanical work" applied to quality gates.
3. **A `Verify` section.** Alongside Inputs, Process, and Outputs, a table of cross-stage consistency checks: which earlier outputs to re-read and what criteria to compare against. The paper's motivating case is an audit that re-reads the stage 2 script against the stage 3 animation spec and flags frame-count, density, and pacing mismatches. It targets the final-stage alignment work in the U-shaped pattern.

   ```
   ## Verify

   | Compare | Against | Criteria |
   |---------|---------|----------|
   | Every beat in this spec | `../01-script/output/[slug]-script.md` | Narration text identical; no beat added or dropped; durations sum to the script's target |
   ```

4. **Two-layer quality gates.** From the unmerged research-pipeline workspace: a `QUALITY-GATES.md` that defines, at each stage boundary, structural checks a script can verify (file exists, format correct) and semantic checks the agent verifies (aligned with the goal, complete), each with a pass condition and an on-fail action, and marks which gates require a human.
5. **A `resume` trigger and a progress file.** A `PROGRESS.md` the agent updates at each checkpoint, and a `resume` keyword that reads it and continues from the last one. Useful for long runs that span sessions; `status` already covers the stage-level view.
6. **Output provenance markers.** Lightweight identifiers in stage outputs (section tags or comment annotations) that point back to the contract step or reference section that produced them, so a wrong phrase in stage 3 can be traced to its source without reading everything. The paper's analogy is debug symbols.
7. **Breakpoints in markdown.** A marker in a `CONTEXT.md` that means "after the agent processes this instruction, show me what it produced before continuing." Turns a single-pass stage into verifiable sub-steps for complex contracts.
8. **Edit tracking toward source improvement.** Keep a log of output edits per stage across runs (section 8.6). When the same kind of edit recurs, propose a contract amendment, a reference update, or a new constraint. The paper frames this as the step that turns a workspace from a tool into a system that improves with use; it depends on provenance (item 6) to trace the edit back.
9. **A workspace summary document.** For each workspace, a condensed summary in the shape of the builder's example (overview, stage summary with checkpoints and audits, shared context, bundled skills, reference-file strategy, placeholder strategy, conditional sections, onboarding). It is the fastest way for a new person, or a builder agent, to understand a workspace without reading every file.
10. **A root `CLAUDE.md` for a family of workspaces.** When several workspaces live together, the root file is a folder map plus a routing table plus the two triggers, and nothing else. Register every workspace in it; the validator checks this when a `workspaces/` folder exists.
