# PROJECT_STATE.md — Context Engineering for Everyone

Last updated: 2026-08-23 (Session 2 — Chapter 2, "Designing Context
Window Budgets," complete. Module 1 is now fully built. Session 1
built Discovery, the curriculum map, the full repository scaffold, and
Chapter 1.)

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
      run at the end of Session 1; passed clean.
- [x] **Ollama re-checked fresh in Session 2**: `/api/tags` responded
      normally (`llama3.2:latest` still installed); `/api/chat` was
      retried with a considerably more patient 75-second timeout (versus
      Session 1's 20 seconds) and still did not return within it — the
      same persistent hang, now confirmed across two independent
      sessions in this sandbox. Disclosed directly in Chapter 2's
      `lesson.html`, not just here. Chapter 2 has no load-bearing
      dependency on a live model call (every worked-math number is
      direct, verified arithmetic against stated inputs).
- [x] **Chapter 2 built and live — "Designing Context Window Budgets,"
      completing Module 1**. Uses Chapter 1's five-line ledger as a
      lens, not a fresh mental model, per the Session 1 handoff. Hook:
      Vantry Health Network's TriageLine, a patient-messaging assistant
      whose team did real, correct context-budget work for its first
      request type (New Symptom Triage) — then broke a second request
      type (Chronic Care Check-In) by reusing that exact budget
      unchanged instead of re-deriving one for a fundamentally
      different content shape, under-provisioning Recalled Long-Term
      Memory and silently truncating a patient's just-changed
      medication (warfarin) out of context. Builds a five-step Budget
      Allocation Recipe (fix the hard limit; reserve Working Space
      first; fix System Instructions; split what's left by a
      request-type profile; validate against the worst realistic case)
      and a four-archetype request-type profile table (short lookup,
      long recurring, tool-heavy agentic, long-document review), with
      full worked token arithmetic for two request types on a
      32,000-token window and a second worked example on an
      8,000-token window. A real percentage-sum bug in two of the four
      profile rows (85% and 90% instead of 100%) was caught and fixed
      during this session's own build, disclosed in the quality audit.
      Grounded in 5 real, live-verified sources this session (Claude
      Docs "Context windows," OpenAI Models documentation, Claude Docs
      "Token counting," Google Gemini "Long context," and the OpenAI
      Cookbook's token-counting guide — 4 of 5 required following a
      live redirect this session, more than Chapter 1's 2 of 5, all
      disclosed honestly in both `lesson.html` and the quality audit).
      8 exercises (6 production-gear: budget subtraction, profile-split
      arithmetic, worst-case validation, reuse-safety judgment,
      from-scratch allocation design, a recipe completeness gate), 8
      practice scenarios (2 explicit judgment calls, 2 production-gear)
      across 8 fresh fictional orgs, 8 interview questions across all 4
      levels, and a real, gradeable **L1 Guided project** (Halveston
      Regional Health System/IntakeLine) designing a token budget for a
      brand-new "Post-Discharge Follow-Up" request type — more
      mechanically rigorous than Chapter 1's project, since the
      self-check verifies the learner's surplus/deficit calls are
      internally consistent with the learner's own allocation numbers,
      not just that fields are non-empty.
- [x] **Quality audit** (`quality-audits/chapter-02-audit.md`) — honest
      self-critique (including the profile-percentage bug caught this
      session, and a disclosed judgment call resolving a tension
      between the curriculum map's project ladder and Chapter 1's
      already-shipped L1 project), a fictional-org exclusion check
      extending Chapter 1's 11-org list with 11 new orgs (22 total in
      this repo), checked against `ai-engineering-for-everyone`'s full
      compiled list with zero collision found, and documentation of the
      four live redirects encountered and handled during citation
      verification.
- [x] **Step 5: Validation (Chapter 2)** — `scripts/local_check.sh` run
      at the end of this session; passed clean (folder structure,
      placeholder-text scan, Python syntax, every `solution.py` executed
      for real, JS syntax and chapter-path validation, secret scan).
- [x] **Registration updated in the same session**:
      `assets/chapters-data.js` (Chapter 2's `path` added), root
      `index.html` (hero-stats now "2 of 13 chapters live" / "1 of 6
      modules complete," and the "All Chapters" intro paragraph
      rewritten to describe both live chapters), and
      `docs/curriculum/index.html` (Chapter 2's chapter-card now
      "Live" with a working link, and its own lede paragraph updated).

## Pending / Not Started

- Chapters 3-13 (all remaining modules) — scaffolded with `.gitkeep`
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

- Ollama's `/api/chat` endpoint has now timed out across two
  independent sessions (Session 1: 20-second timeout; Session 2: a
  considerably more patient 75-second timeout, still no response) —
  consistent with every sibling course's reported sandbox behavior. A
  future session that needs a real captured transcript should retry
  with an even more generous timeout (120s+) and consider whether the
  model needs to be pulled or warmed differently in this sandbox,
  before concluding it's permanently unreachable — per
  `ai-engineering-for-everyone`'s own later-session finding that a
  sufficiently patient retry eventually succeeded after several
  sessions of hangs.
- The "Lost in the Middle" citation (Liu et al., 2023) is the original
  finding, not a more recent replication — flagged in the quality audit
  as something Chapter 6 (which owns this topic in depth) should
  re-verify against more current research before treating the finding
  as settled across all current model families.
- A real bug was caught and fixed during Chapter 2's own build: two of
  the four request-type profile rows in the lesson's allocation table
  (tool-heavy agentic, long-document review) originally had
  percentages summing to 85% and 90% instead of 100%, caught by
  cross-checking against the exercises that depend on the same numbers
  before publishing. No chapter's arithmetic should be trusted without
  this kind of cross-check against its own dependent exercises before
  it ships.

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
- Chapter 2 resolved a tension between the curriculum map's project
  ladder (one "L1 Guided" project "ships after Ch. 2") and the fact
  that Chapter 1 already shipped a complete, real L1 project in
  Session 1, by shipping a *second* L1-tier project for Chapter 2 (tied
  to Module 1's own two stated labs, one project per chapter). This is
  a judgment call, not a confirmed ecosystem convention — a future
  session should re-confirm before assuming Chapters 3 and 4 (Module
  2, which ships the "L2 Assisted" project after Chapter 4) follow the
  same one-project-per-chapter pattern, or whether Module 2's single L2
  project should instead ship once, at the end of Chapter 4 only.

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

**Chapter 3 — "Short-Term Conversational Memory," starting Module 2.**

Per `docs/curriculum/CURRICULUM_MAP.md`: Module 2 (Memory Systems),
Chapters 3-4. Module 2's outcomes: "design short-term memory that
stays in budget; design a long-term memory system with a real
retrieval-into-context policy." Chapter 3 specifically owns Line 3 of
the ledger (Conversation History) — managing turn-by-turn history
inside a bounded window (now a real, derived budget, thanks to Chapter
2) without silently truncating something load-bearing. Its lab, per
the module outcomes: "manage a long-running conversation's history
under a hard token limit." Chapter 4 (long-term/persistent memory, Line
4) is the next chapter after that — do not build both in one session,
per this ecosystem's one-chapter-at-a-time discipline.

What NOT to re-derive:
- The five-line Context Budget Ledger (Chapter 1) and the five-step
  Budget Allocation Recipe (Chapter 2) are already-built material —
  Chapter 3 should use Line 3's *allocated budget* (a real number, now
  that Chapter 2 exists) as its starting constraint, and build the
  actual eviction/compression policy that keeps conversation history
  inside it, rather than re-deriving what the budget should be from
  scratch. Chapter 1's hook (Brackwater/SignalDesk) already showed what
  a *missing* history policy costs; Chapter 3's job is to actually build
  one.
- The course's positioning relative to `rag-for-everyone`,
  `mcp-for-everyone`, and `ai-engineering-for-everyone` Chapter 3 is
  already established in `docs/discovery-notes.md` and Chapter 1's own
  "Why This Course Exists" section — Chapter 3 can reference it briefly
  but should not re-argue it from scratch.
- Read Chapter 2's own quality audit
  (`quality-audits/chapter-02-audit.md`) before starting, not just the
  curriculum map — per `AI_HANDOFF.md`'s own standing instruction, it
  may surface scope notes this file doesn't fully capture (e.g. the
  open L1/L2 project-ladder judgment call logged above, which could
  affect whether Chapter 4's project ships solo or per-chapter).

New-org exclusion list: read `quality-audits/chapter-02-audit.md`'s
full running list (Chapter 1's 11 orgs plus Chapter 2's 11 new orgs —
Vantry Health Network, Corravine Freight, Marrenkirk Insurance Group,
Duvane Utilities Cooperative, Graytide Hospitality Group, Oakspire Home
Care Network, Corundale Media Group, Pallisade Manufacturing, Redcliff
Credit Union, Thackery Regional Exchange, Halveston Regional Health
System — 22 total in this repo) plus `ai-engineering-for-everyone`'s
own full compiled list (see that repo's
`quality-audits/chapter-13-audit.md`) before naming any new fictional
org for Chapter 3, and extend — don't restart — the list in
`quality-audits/chapter-03-audit.md`.

Citation/Ollama re-verification discipline: do not assume Chapter 2's
five citations are still live — re-fetch and re-read anything reused,
and treat all-new sources as the default. Re-check Ollama's `/api/tags`
and `/api/chat` fresh at the start of the session, with an even more
patient timeout than Chapter 2's 75 seconds (see Known Issues above);
do not assume the hang will repeat or resolve without testing. Chapter
3 is the first chapter in this course likely to want a real runnable
compression/summarization example — if it builds one, this is also the
first chapter where a live Ollama response would be genuinely
load-bearing rather than illustrative, so the retry is worth extra
patience this time.

Registration-staleness check reminders: once Chapter 3's `lesson.html`
exists, update `assets/chapters-data.js` (add its `path`), the root
`index.html` (`hero-stats` counts and the "All Chapters" intro
paragraph), and `docs/curriculum/index.html` (its own chapter-card
status and lede paragraph) in the same session — these four locations
drifted stale in multiple sibling courses' own build histories when a
chapter shipped without updating all four at once.

Local validation, done at the end of every session:

```
$ bash scripts/local_check.sh
```

Passed clean at the end of this session (Chapter 2) — folder
structure, placeholder-text scan, Python syntax, every `solution.py`
executed for real, JS syntax and chapter-path validation, secret scan.
See this session's own commit message / `AI_HANDOFF.md` for the exact
result recorded.
