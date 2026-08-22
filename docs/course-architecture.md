# Context Engineering for Everyone — Course Architecture

## Reference Pattern

Structural reference: `TechNaom/ai-engineering-for-everyone` (the most
recently completed, most refined pattern in the ecosystem as of this
course's build). Reuse:

- Root `index.html` GitHub Pages entry point + `docs/curriculum/index.html`
  styled roadmap.
- Shared `assets/` (style.css, sidebar.js, progress.js, quiz-engine.js,
  home.js, chapters-data.js) — copied and rebranded
  (`CEFE_MODULES`, `CEFEProgress`, `cefe-progress`), structure only.
- `chapters/chapter-XX-slug/` per-chapter folders using the rich
  per-chapter file pattern, the ecosystem's going-forward default:
  `lesson.html`, `quiz.html`, `interview-questions.html` + `.md`,
  `exercises/{index.html,starter.py,solution.py,README.md}`,
  `practice/{index.html,starter.py,solution.py,README.md}`,
  `project/{index.html,starter.py,solution.py,README.md}` (+
  `RUBRIC.md` where a chapter ships a real, non-preview project).
- `templates/`, `assessments/` (including
  `templates/written-exam.template.html` rendered as styled HTML),
  `quality-audits/`.
- `PROJECT_STATE.md`, `AI_HANDOFF.md` from day one.
- **CI**: `.github/workflows/ci.yml` and `scripts/local_check.sh`
  copied from `ai-engineering-for-everyone` and adapted — includes the
  `# CI: LONG_RUNNING_SERVER` / `# CI: NEEDS_LIVE_SERVER=` marker
  convention, `practice/solution.py` coverage, and `.gitkeep` in every
  empty directory from the start (avoiding the bootstrap bug found and
  fixed in prior sibling courses).

Do not reuse any sibling course's lesson content, examples, or project
stories. All examples and interview answers are original to this
course.

## Production Depth Standard

Same bar as the rest of the ecosystem: 8 exercises per chapter (5+
production-gear), 8 practice scenarios, 8 interview questions across
all 4 levels, a tested project. Every code example is run before being
written into a lesson.

## Model/API Policy

Inherits `ai-engineering-for-everyone`'s resolved policy directly, not
re-litigated: **fully local, open-source by default** via the plain
`openai` Python package pointed at **Ollama**'s local
OpenAI-compatible endpoint (`base_url="http://localhost:11434/v1"`),
zero API key, zero cost. A documented, one-parameter "use a hosted
provider instead" option (OpenAI, Anthropic, Gemini all expose
OpenAI-compatible endpoints) is included for learners who want
production-grade context-window sizes and behavior closer to what
they'll see in a real deployment.

Ollama status is checked fresh at the start of any chapter whose
examples depend on a live model call, and any live-testing limitation
is honestly disclosed in the lesson text itself, not just the quality
audit — same discipline as every sibling course.

## Context-Engineering-Specific Framing (non-negotiable)

This course teaches the discipline of engineering what fills the
context window, not a bigger prompting or RAG tutorial. Every chapter
must connect its topic back to a real failure mode caused by
mismanaged context (a budget overrun, a silently truncated fact, a
lost-in-the-middle miss, a contradiction between two assembled
sources, a sub-agent that inherited context it shouldn't have had, or
one it needed and didn't get) — never present a technique as abstract
"best practice." Every hands-on artifact (a budget allocator, a memory
store, a compression pipeline, a context assembler, a context-quality
evaluator) must be real, runnable code, not pseudocode.

Every chapter explicitly states, in its own text, what it is *not*
re-teaching from `rag-for-everyone`, `mcp-for-everyone`, or
`ai-engineering-for-everyone` Chapter 3, wherever its subject sits near
theirs — the same discipline `ai-engineering-for-everyone`'s Chapter 3
used relative to its own Module 3.

## Conversational Clarity Standard

Same as the rest of the ecosystem: explain like a helpful senior
engineer beside the learner, story-first, real trade-offs unpacked
patiently.

## Builder Thought-Process Layer

Every chapter includes a visible reasoning section (problem framing,
options considered, chosen approach, validation, observed failure,
decision) — same pattern as the rest of the ecosystem, adapted to
context engineering decisions (what's actually competing for this
budget, what does this technique really save versus what it costs to
compute, what's the residual risk after the fix — e.g., a compressed
summary that drops a fact nobody noticed was load-bearing until it
mattered).
