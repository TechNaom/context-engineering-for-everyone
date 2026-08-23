# AI_HANDOFF.md — Context Engineering for Everyone

Read this before touching anything in this repo. It's written so any AI
coding assistant can pick this up cold, with zero prior context, and
not redesign decisions that were already made.

## What this repository is

An open-source, free-to-read (and free-to-*run*) technical course
teaching the engineering discipline of deciding what actually goes
into a model's context window at inference time, and how it's
organized once there — context budget management, memory systems,
context compression and curation, multi-source context assembly,
context engineering for agentic and multi-step systems, and context
evaluation — part of the **TechNaom "for Everyone"** course ecosystem.
Follows the same detailed master course-building prompt as every
sibling course.

## Design philosophy (non-negotiable)

Same as the rest of the ecosystem: layered depth for 4 personas,
story-first, no shallow tutorials, 13 chapters, don't pad; all content
original.

**Context-engineering-specific addition (non-negotiable)**: every
practice taught must be tied to a real, concrete context-management
failure mode it prevents — never presented as abstract "best
practice." Every hands-on artifact must be real, runnable code, tested
before it's written into a lesson.

## Current state (as of 2026-08-23)

**Read `PROJECT_STATE.md` for the authoritative, up-to-date status.**
Short version: this is the course's **third session**. Session 1 built
Discovery, the curriculum map, the full repository scaffold, and
Chapter 1 ("The Context Budget"). Session 2 built Chapter 2
("Designing Context Window Budgets"), completing Module 1 in full.
Session 3 built Chapter 3 ("Short-Term Conversational Memory"), opening
Module 2. Chapters 4-13 exist only as `.gitkeep`'d directories, not yet
built.

- Directory skeleton (`.gitkeep` in every not-yet-built chapter
  directory from the start — the bootstrap bug found in prior sibling
  courses, where an empty dir's `.gitkeep` gets missed and CI's
  structure-check catches it on the first real run, is avoided here by
  starting with it in place), `docs/curriculum/CURRICULUM_MAP.md`,
  `docs/discovery-notes.md`, `docs/course-architecture.md`, `README.md`,
  this file, `PROJECT_STATE.md`, `LICENSE`/`LICENSE-CONTENT`,
  `CONTRIBUTING.md`, `CHANGELOG.md`.
- `templates/` and shared `assets/` copied from
  `ai-engineering-for-everyone` and rebranded (`window.CEFE_MODULES`,
  `window.CEFEProgress`, `cefe-progress` localStorage key) — structure
  only, no content reused.
- **CI (`.github/workflows/ci.yml`) and `scripts/local_check.sh`**
  copied from `ai-engineering-for-everyone` and adapted.
- **Homepage (`index.html`) and roadmap
  (`docs/curriculum/index.html`) built from day one**, showing Chapter
  1 live and Chapters 2-13 as planned.
- **NOT pushed to GitHub. No remote added.** Local `git commit` only,
  per the task's explicit instruction — this is a brand-new course
  whose positioning hasn't been reviewed by a human yet.
- **Chapter 1 ("The Context Budget") is built and live** — the
  reference chapter. See `quality-audits/chapter-01-audit.md`.
- **Chapter 2 ("Designing Context Window Budgets") is built and
  live**, completing Module 1. See
  `quality-audits/chapter-02-audit.md`. Uses Chapter 1's ledger as a
  lens; its own job is proactive, per-request-type budget allocation
  before a request is sent, contrasted with Chapter 1's after-the-fact
  diagnosis.
- **Chapter 3 ("Short-Term Conversational Memory") is built and
  live**, opening Module 2. See `quality-audits/chapter-03-audit.md`.
  Uses Chapter 2's allocation recipe as a lens: Line 3's already-
  allocated budget is a given constraint, and this chapter's own job is
  the real eviction/compression policy (verbatim window + running
  summary + bounded, explicit pinning) that keeps a long-running
  conversation inside that budget without silently dropping something
  load-bearing. This is also the first session in this course's history
  to capture real, live Ollama output (after several timeouts) —
  disclosed in full, including an honest, unedited transcript where the
  model didn't fully follow its own prompt instructions, used directly
  as the lesson's own argument for why pinning is a deterministic
  mechanism, not something delegated to a summarization call.

## Naming conventions

- Chapter folders: `chapters/chapter-NN-kebab-slug/`, matching the rest
  of the ecosystem.
- Repo name: `context-engineering-for-everyone`, intended GitHub org
  `TechNaom`, public, `main` branch — **not yet created on GitHub**.

## What NOT to change

- Don't restructure the repo layout without checking
  `docs/course-architecture.md` — mirrors `ai-engineering-for-everyone`
  deliberately.
- Don't assume a specific model's behavior without testing it against
  the real, installed model first — same test-before-write discipline
  as every sibling course. Ollama's `/api/chat` endpoint hung across
  Sessions 1-2 (20s, then 75s timeouts), but Session 3 finally got real
  responses — twice — with enough patience (180s and 240s timeouts).
  The important finding for future sessions: it did NOT stay resolved
  within Session 3 itself — two later calls timed out again (60s, 150s)
  even after an earlier call in the same session had already succeeded
  warm, before a third attempt succeeded in under 9 seconds. Treat this
  endpoint as *intermittently* slow/hanging, not "cold once, fast
  forever after." `/api/tags` has responded normally in all three
  sessions with `llama3.2:latest` installed. Re-check and disclose
  honestly every session, budgeting for retries throughout the session
  (not just at the start), with generous timeouts (120s+) even after an
  earlier call has already succeeded.
- Every code example — every budget calculator, memory store,
  compression pipeline, context assembler, evaluator — must be run for
  real before being written into a lesson. A claimed number that wasn't
  actually measured is the exact "it looked good in the demo" failure
  mode this course exists to teach people out of.
- **Re-verify every external citation live before trusting a prior
  session's fetch, not just on first use.** This session's own
  citation verification found two of five sources had moved to a new
  URL since their historically-known location (a 301/308 redirect in
  both cases) — both were followed, the redirect targets were fetched
  and confirmed live, and the lesson cites the working URLs. Don't
  assume a citation is still good just because it was good in a prior
  session, or even earlier in the same session.
- Don't copy lesson content, examples, or project stories from any
  sibling TechNaom repo — structure/templates only.
- **Do not mass-build multiple chapters in one pass** — one chapter at a
  time, validated before scaling, is this course's own standing
  discipline, inherited from every sibling TechNaom course. Session 1
  built Discovery, the scaffold, and Chapter 1 only; Session 2 built
  Chapter 2 only, completing Module 1; Session 3 built Chapter 3 only,
  opening Module 2 — matching exactly how `ai-engineering-for-everyone`
  itself progressed.
- **Check every fictional org against the running exclusion list before
  naming a new one** — see `quality-audits/chapter-03-audit.md` for the
  full, current list (33 orgs across Chapters 1-3 so far, checked
  against `ai-engineering-for-everyone`'s own full compiled list with
  zero collision found) and extend it (don't restart it) for every new
  chapter. Each new chapter's audit should reproduce the full list plus
  its own new orgs, so the next session only ever needs to read the
  latest one.
- **State explicitly, in each new chapter's own lesson text, what it is
  NOT re-teaching** from `rag-for-everyone`, `mcp-for-everyone`, or
  `ai-engineering-for-everyone` Chapter 3 wherever its subject sits
  close to theirs — this is the discipline that keeps this course from
  drifting into duplicating a sibling course over many sessions, and
  Chapter 1 modeled it directly in its "Why This Course Exists"
  section.

## Current task: Chapter 4 — "Long-Term and Persistent Memory Systems"

Completes Module 2 (Memory Systems). See `PROJECT_STATE.md`'s "Next
Recommended Task" section for the full handoff detail: what not to
re-derive from Chapters 1-3 (including Chapter 3's own short-term
eviction/compression mechanics — Chapter 4 starts from the boundary
between short-term and persistent memory, it doesn't re-teach pinning
or running summaries), the explicit boundary to state against
`rag-for-everyone` (Chapter 4 decides what's stored and what real
policy pulls it back into Line 4 for a given turn; it does not design
retrieval architecture itself), the new-org exclusion list to check
first (33 orgs across Chapters 1-3 so far), citation/Ollama
re-verification discipline (the hang is intermittent, not "cold once,
fast forever after" — budget for retries throughout the session), the
still-open L1/L2 project-ladder judgment call that must finally be
resolved this session (see `PROJECT_STATE.md`'s "Open Decisions"), and
the four registration-staleness locations to update in the same
session once `lesson.html` exists (`assets/chapters-data.js`, root
`index.html`'s hero-stats and intro paragraph — note it should read "4
of 13 chapters live" / "2 of 6 modules complete" once Chapter 4 ships,
`docs/curriculum/index.html`'s chapter-card status and lede paragraph).

## Next task after that

Chapter 5 ("Context Compression and Summarization"), opening Module 3
— not yet planned in detail beyond the curriculum map's own module
outcomes; a future session should read Chapter 4's own quality audit
before starting, not assume its scope from the curriculum map alone.
Chapter 5 is where this course's own compression/summarization mechanics
finally get full depth (Chapter 3 deliberately built only the minimum
needed to keep short-term memory in budget, and said so directly in its
own lesson text) — re-read Chapter 3's "Why This Chapter" section before
scoping Chapter 5, so it doesn't either re-teach what Chapter 3 already
covered or leave a gap between the two.

## Important architectural decisions (see PROJECT_STATE.md for full detail)

1. Model/API policy inherited directly from `ai-engineering-for-everyone`:
   `openai` package pointed at Ollama's local endpoint by default,
   zero cost/key, documented hosted-provider-swap option.
2. 13 chapters, focused-topic sizing.
3. Static site, no backend, mirrors `ai-engineering-for-everyone`
   exactly.
4. Deliberately narrow, verified positioning — does NOT duplicate
   `rag-for-everyone`'s retrieval architecture, `mcp-for-everyone`'s
   protocol mechanics, or `ai-engineering-for-everyone` Chapter 3's
   prompt-template versioning; assumes all three and engineers the
   dynamic, per-request content that fills an already-managed template.
5. Positioned as a deepening layer on top of `ai-engineering-for-everyone`'s
   shared engineering foundation — see `docs/discovery-notes.md` section
   9 for the full forward cross-link list (future `LLM Evaluation for
   Everyone`, `Observability for Everyone`, an expanded `Agentic AI for
   Everyone`, `AI Architecture for Everyone`).
