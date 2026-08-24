# Context Engineering for Everyone

Free, interactive course on the engineering discipline of deciding what
actually goes into a model's context window at inference time, and how
it's organized once there: context window budget management, memory
systems (short-term and long-term), context compression and curation
(avoiding "lost in the middle" degradation), multi-source context
assembly, context engineering for agentic and multi-step systems, and
context evaluation — closing with a capstone that designs a complete
context engineering system.

🔗 **Repo:** <https://github.com/TechNaom/context-engineering-for-everyone>
🔗 **Live UI:** <https://technaom.github.io/context-engineering-for-everyone/>
*(GitHub Pages not yet enabled)*

This course follows the same philosophy as the rest of the TechNaom
"for Everyone" ecosystem:

- Plain-language first, without hiding the real engineering.
- One chapter at a time, validated before scaling.
- No signup required to *read or run* the course. Hands-on chapters
  that need a real model run against a local, open-source model via
  [Ollama](https://ollama.com) by default — no API key, no account, no
  per-run cost — with a documented option to point the same code at a
  hosted provider instead.
- Browser-first learning pages.
- Every practice is tied to a real context-engineering failure mode it
  prevents, never taught as abstract "best practice."
- Hands-on code tested for real before being written into a lesson.
- Interview-ready explanations.
- Strong architecture and trade-off thinking.

All examples, scenarios, exercises, projects, and thought-process
journals in this course are original.

## What this is

`Context Engineering for Everyone` sits in a specific, deliberately
narrow gap in the TechNaom ecosystem: `rag-for-everyone` teaches
retrieval architecture (producing candidate context), `mcp-for-everyone`
teaches protocol-level tool integration, and `ai-engineering-for-everyone`
Chapter 3 teaches the prompt *template* as a versioned software
artifact. None of them teach what actually earns a place in the context
window at inference time, in what order, or how multiple sources get
combined without contradicting each other — that gap is this course's
entire subject. Full reasoning and a verified cross-course overlap check
live in [`docs/discovery-notes.md`](docs/discovery-notes.md).

## Model/API versions

Hands-on chapters that need a real model use the plain **`openai`**
Python package (`pip install openai`) pointed, by default, at
**Ollama**'s local OpenAI-compatible endpoint — zero cost, zero API
key. A documented option points the exact same code at a hosted
provider (OpenAI, Anthropic, Gemini — all expose OpenAI-compatible
endpoints). See `docs/course-architecture.md` for the full policy,
including this session's live Ollama reachability check.

## Who this is for

- **`ai-engineering-for-everyone` graduates** hitting a "context wall"
  — production LLM features that degrade as history or retrieved
  context grows.
- **RAG engineers** whose retrieval metrics look fine but final answers
  still degrade — the problem is context assembly, not retrieval
  quality.
- **Agent/multi-step system builders** debugging "it forgot" or "it got
  confused" failures that are actually context-budget or
  context-isolation issues.
- **Backend engineers** building long-running assistant/chat products
  that need real memory design, not an unbounded, ever-growing prompt.

## Learning path

See [`docs/curriculum/CURRICULUM_MAP.md`](docs/curriculum/CURRICULUM_MAP.md)
for the full module/chapter roadmap, learning outcomes, and project
ladder.

## Repository structure

```text
context-engineering-for-everyone/
  chapters/            per-chapter lessons, quizzes, labs, interview prep
  docs/curriculum/      curriculum map (source of truth) + styled roadmap
  docs/discovery-notes.md   positioning/scope decisions and reasoning
  docs/course-architecture.md
  templates/            reusable chapter/quiz/lab/project templates
  assessments/          quizzes, written exams, interview questions
  quality-audits/       per-chapter quality gate checklists
  assets/                shared site styling, sidebar, progress, quiz engine
  PROJECT_STATE.md       current build status (read this first)
  AI_HANDOFF.md          for any AI coding assistant picking this up cold
```

## Current status

**All 13 chapters are live — the course is complete.** All 6 modules
(The Context Budget Mental Model; Memory Systems; Context Compression
and Curation; Multi-Source Context Assembly; Context Engineering for
Agentic Systems; Evaluation and Capstone) are built in full, closing
with Chapter 13's Level 4 Architecture Challenge capstone. See
`PROJECT_STATE.md` for full build history and any open follow-up work.

## Projects

Four project levels, from guided to architecture-challenge — see the
curriculum map's Projects section. Chapter 1 ships the course's first,
real L1 Guided project.

## Capstone

Design and defend a complete context engineering system for a
realistic multi-step/agentic system — a full budget allocation, memory
design, compression/curation plan, multi-source assembly plan, context-
isolation plan, and evaluation plan — matching the same rigor as
`ai-engineering-for-everyone`'s own capstone.

## Contributing

Solo-maintained; not open to external PRs. See `CONTRIBUTING.md` if
you're forking this for your own use.

## License

Code is licensed under [MIT](LICENSE). Educational content (lessons,
diagrams, exercises, interview questions) is licensed under
[CC BY 4.0](LICENSE-CONTENT).
