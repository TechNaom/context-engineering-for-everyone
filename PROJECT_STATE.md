# PROJECT_STATE.md — Context Engineering for Everyone

Last updated: 2026-08-22 (Initial build session — Discovery, curriculum
map, full repository scaffold, and Chapter 1, "The Context Budget,"
complete. This is the course's first-ever session; nothing prior to
this exists to summarize.)

## Course Objective

Teach the engineering discipline of deciding what actually goes into a
model's context window at inference time, and how it's organized once
there: context window budget management, memory systems (short-term
and long-term), context compression and curation (avoiding "lost in
the middle" degradation), multi-source context assembly, context
engineering for agentic and multi-step systems, and context evaluation
— following the TechNaom master course-building philosophy (layered
depth, story-first, production-grade, interview-ready, original content
only).

## Architecture Decisions

- **Course size: 13 chapters** (focused-topic sizing, matching every
  other course in the ecosystem).
- **Positioning**: a deliberately narrow, verified gap between
  `rag-for-everyone` (retrieval architecture — produces candidate
  context), `mcp-for-everyone` (protocol-level tool integration), and
  `ai-engineering-for-everyone` Chapter 3 (the prompt template as a
  versioned software artifact). This course assumes the template is
  already managed and engineers the dynamic, per-request content that
  fills it. Full reasoning and a verified cross-course overlap check
  (including a full read of `ai-engineering-for-everyone` Chapter 3's
  own lesson content) in `docs/discovery-notes.md`.
- **Repo structure mirrors `ai-engineering-for-everyone`** (the most
  recently completed, most refined reference at the time of this
  course's build): static site, `chapters/chapter-XX-slug/`,
  `docs/curriculum/`, `templates/`, `assessments/`, `quality-audits/`.
  Shared front-end assets and templates copied and rebranded
  (`CEFE_MODULES`/`CEFEProgress`/`cefe-progress`), `.gitkeep` added to
  every not-yet-built chapter directory from day one (the bootstrap bug
  found in prior sibling courses — empty dirs aren't tracked by git —
  is avoided from the start here).
- **Chapter file pattern**: the rich per-chapter structure (README.md
  in exercises/practice/project, `interview-questions.md`+`.html`,
  project `RUBRIC.md`) from Chapter 1 onward — the ecosystem's current
  default, not a later exception.
- **Model/API policy**: inherits `ai-engineering-for-everyone`'s
  resolved policy directly — `openai` Python package pointed at
  Ollama's local OpenAI-compatible endpoint by default, zero cost/API
  key, documented hosted-provider-swap option. See
  `docs/course-architecture.md`.

## Completed

- [x] **Step 1: Discovery** — course vision, 4 personas, prerequisites,
      learning outcomes, 6-module/13-chapter structure, project ladder
      (L1-L4), capstone shape, differentiators, and an explicit,
      verified cross-course overlap check against `rag-for-everyone`,
      `mcp-for-everyone`, and `ai-engineering-for-everyone` (including a
      full read of that course's Chapter 3 lesson content, the closest
      single-chapter overlap risk). Full reasoning in
      `docs/discovery-notes.md`.
- [x] **Step 2: Curriculum map** (`docs/curriculum/CURRICULUM_MAP.md`).
- [x] **Step 3: Repository architecture scaffolded** — 13 chapter
      directories (Chapter 1 fully built; Chapters 2-13 with `.gitkeep`
      from the start), `templates/` (rebranded from
      `ai-engineering-for-everyone`), shared `assets/` rebranded
      (`CEFE_MODULES`, `CEFEProgress`, `cefe-progress`), CI
      (`.github/workflows/ci.yml`, `scripts/local_check.sh`) copied
      from `ai-engineering-for-everyone` and adapted, README, this
      file, AI_HANDOFF.md, CHANGELOG.md, CONTRIBUTING.md,
      LICENSE/LICENSE-CONTENT.
- [x] Homepage (`index.html`) and roadmap (`docs/curriculum/index.html`)
      built as part of the initial scaffold, showing Chapter 1 live and
      Chapters 2-13 as planned — not deferred.
- [x] **Ollama checked fresh this session**: `/api/tags` responded
      normally (`llama3.2:latest` installed); `/api/chat` did not
      return within a 20-second timeout on the attempt made — the same
      persistent hang every sibling TechNaom course has independently
      reported in this sandbox environment. Disclosed directly in
      `lesson.html`, not just here. Chapter 1 has no load-bearing
      dependency on a live model call (illustrative hook code and
      directly-computed exercise arithmetic); later chapters that build
      a runnable compression, memory-retrieval, or context-evaluation
      harness (Chapters 5, 4, and 12) will need to re-check this before
      claiming any live output.
- [x] **Chapter 1 built and live — reference chapter**: "The Context
      Budget." Hook: Brackwater Home Internet's SignalDesk, a customer
      support chat assistant where unbounded, unsummarized conversation
      history — combined with a naive end-of-pipeline truncation —
      silently dropped a load-bearing early fact (a customer's
      incompatible gateway hardware) that had already become less
      reliably used due to its buried mid-transcript position (the
      "lost in the middle" effect), producing a wrong recommendation
      with no attacker and no model bug involved. Builds the five-line
      Context Budget Ledger (System Instructions, Grounding Context,
      Conversation History, Recalled Long-Term Memory, Working Space)
      as the course's core mental model, walks it against the hook end
      to end in a full diagnosis table, and states the course's
      positioning explicitly relative to every sibling course by name.
      Grounded in 5 real, live-verified sources (Anthropic's "Effective
      context engineering for AI agents," Liu et al.'s "Lost in the
      Middle" arXiv paper, OpenAI's Prompt Engineering guide, Anthropic/
      Claude's context-management blog post, and LangChain's "Memory
      for agents" post — two of five required following a live
      redirect this session, disclosed honestly in both `lesson.html`
      and the quality audit). 8 exercises (5 production-gear: fix
      evaluation, budget arithmetic, eviction-policy selection,
      lost-in-the-middle ordering, context-health monitor design), 8
      practice scenarios (2 explicit judgment calls, 2 production-gear)
      across 8 fresh fictional orgs, 8 interview questions across all 4
      levels, and a real, gradeable **L1 Guided project** (not a
      preview) — diagnosing a third fictional system (Meridian Legal
      Aid Network/CaseNote) end to end, with a structural self-check
      harness and a 5-criterion/20-point `RUBRIC.md`. Honest Ollama
      live-testing disclosure stated directly in the lesson text
      itself.
- [x] **Quality audit** (`quality-audits/chapter-01-audit.md`) — honest
      self-critique, names real gaps (structural-only project grading
      by necessity, no live-captured model output this session), a
      fictional-org exclusion check (11 new orgs, checked against
      `ai-engineering-for-everyone`'s full compiled list with zero
      collision found), and documents the two live redirects
      encountered and handled during citation verification.
- [x] **Step 5: Validation (Chapter 1)** — `scripts/local_check.sh`
      run; see "Next Recommended Task" below for the exact result at
      the end of this session.

## Pending / Not Started

- Chapters 2-13 (all remaining modules) — scaffolded with `.gitkeep`
  only, no content. Per this ecosystem's standing discipline, they are
  built one chapter at a time in future sessions, each validated before
  the next begins — do not mass-build multiple chapters in one pass.
- No module written exams, module-assessments, or architecture
  challenges exist yet — `assessments/` is fully scaffolded but empty
  (`.gitkeep` in every subdirectory) until the modules they cover are
  built.
- No GitHub remote, no GitHub Pages, no push — by explicit instruction,
  this repo stays local-only until a human reviews the course's
  positioning.

## Known Issues

- Ollama's `/api/chat` endpoint timed out in this session's single
  attempt (20-second timeout) — consistent with every sibling course's
  reported sandbox behavior, but only one attempt was made this
  session (Chapter 1 had no load-bearing need to retry). Future
  chapters that need a real captured transcript should retry with a
  more generous timeout before concluding it's unreachable, per
  `ai-engineering-for-everyone`'s own later-session finding that a
  sufficiently patient retry eventually succeeded after several
  sessions of hangs.
- The "Lost in the Middle" citation (Liu et al., 2023) is the original
  finding, not a more recent replication — flagged in the quality audit
  as something Chapter 6 (which owns this topic in depth) should
  re-verify against more current research before treating the finding
  as settled across all current model families.

## Open Decisions

- Whether Chapter 8's retrieval-integration content will need its own
  small, runnable retriever stub (to produce a realistic "ranked
  results" input) or whether it's acceptable to use a hand-authored,
  clearly-labeled example ranked list — deferred to that chapter's own
  session; note in its planning that `rag-for-everyone` should be
  checked first for any reusable structural pattern (not content).
- Exact scope of Chapter 9 ("Context Engineering for Tool Use")
  relative to any future revision of `mcp-for-everyone` — currently
  scoped as protocol-agnostic per `docs/discovery-notes.md` section
  1.2; re-confirm this still holds if `mcp-for-everyone` gains new
  context-shaping content in the interim.

## Design Standards

Same as the rest of the ecosystem, per `docs/course-architecture.md`:
8 exercises per chapter (5+ production-gear), 8 practice scenarios, 8
interview questions across all 4 levels, a tested project, every code
example run for real before being written into a lesson, every
external citation fetched and read live each session (not assumed
still valid from a prior session), honest Ollama disclosure every
session, and a running fictional-org exclusion list maintained and
extended (not restarted) in each chapter's own quality audit.

## Next Recommended Task

**Chapter 2 — "Designing Context Window Budgets," completing Module 1.**

What NOT to re-derive:
- The five-line Context Budget Ledger (System Instructions, Grounding
  Context, Conversation History, Recalled Long-Term Memory, Working
  Space) and the course's core mental model are Chapter 1's material —
  Chapter 2 should use them as a lens (the way `ai-engineering-for-everyone`
  Chapter 2 used Chapter 1's six-layer stack as a lens) rather than
  re-teaching them. Chapter 2's own job, per the curriculum map, is the
  practical skill of *allocating* a budget across all five lines for a
  given request type and hard context-window limit — before a single
  request is sent, not diagnosed after the fact the way Chapter 1's
  project did.
- The course's positioning relative to `rag-for-everyone`,
  `mcp-for-everyone`, and `ai-engineering-for-everyone` Chapter 3 is
  already established in `docs/discovery-notes.md` and Chapter 1's own
  "Why This Course Exists" section — Chapter 2 can reference it briefly
  but should not re-argue it from scratch.

New-org exclusion list: read `quality-audits/chapter-01-audit.md`'s
full 11-org list (Brackwater Home Internet, Cobalt Home Security,
Windermere Legal Services, Pinecrest Veterinary Group, Solmark
Payments, Thistledown Air Cargo, Ravenhollow University Registrar,
Copperfield Home Appliances, Marrowgate Public Library, Fenwick Outdoor
Adventures, Meridian Legal Aid Network) plus
`ai-engineering-for-everyone`'s own full compiled list (see that
repo's `quality-audits/chapter-13-audit.md`) before naming any new
fictional org for Chapter 2, and extend — don't restart — the list in
`quality-audits/chapter-02-audit.md`.

Citation/Ollama re-verification discipline: do not assume Chapter 1's
five citations are still live — re-fetch and re-read anything reused,
and treat all-new sources as the default. Re-check Ollama's `/api/tags`
and `/api/chat` fresh at the start of the session; do not assume this
session's timeout will repeat or resolve without testing.

Registration-staleness check reminders: once Chapter 2's `lesson.html`
exists, update `assets/chapters-data.js` (add its `path`), the root
`index.html` (`hero-stats` counts and the "All Chapters" intro
paragraph), and `docs/curriculum/index.html` (its own chapter-card
status and lede paragraph) in the same session — these four locations
drifted stale in multiple sibling courses' own build histories when a
chapter shipped without updating all four at once.

Local validation, done at the end of this initial session:

```
$ bash scripts/local_check.sh
```

See the end of this session's own commit message / AI_HANDOFF.md for
the exact pass/fail result recorded.
