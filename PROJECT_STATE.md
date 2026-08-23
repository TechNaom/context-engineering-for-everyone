# PROJECT_STATE.md — Context Engineering for Everyone

Last updated: 2026-08-23 (Session 3 — Chapter 3, "Short-Term
Conversational Memory," complete, opening Module 2. Session 2 built
Chapter 2, completing Module 1. Session 1 built Discovery, the
curriculum map, the full repository scaffold, and Chapter 1.)

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
- [x] **Registration updated in the same session (Chapter 2)**:
      `assets/chapters-data.js` (Chapter 2's `path` added), root
      `index.html` (hero-stats now "2 of 13 chapters live" / "1 of 6
      modules complete," and the "All Chapters" intro paragraph
      rewritten to describe both live chapters), and
      `docs/curriculum/index.html` (Chapter 2's chapter-card now
      "Live" with a working link, and its own lede paragraph updated).
- [x] **Ollama re-checked fresh in Session 3, with genuinely mixed
      results, disclosed honestly rather than rounded to a clean
      answer**: `/api/tags` responded normally (`llama3.2:latest`
      still installed). `/api/chat` was retried across four separate
      attempts this session: a 120-second attempt did not return; a
      180-second attempt succeeded (~153 seconds total, ~138 of which
      was model load time); an immediate warm follow-up call returned
      in ~11.5 seconds; a later call then timed out twice more (60s,
      150s) before succeeding on a third attempt at a 240-second
      timeout in 8.7 seconds flat. This session did not observe a
      simple "cold once, fast forever after" pattern — the endpoint
      hung intermittently even after a prior successful warm call.
      This is the first session in this course's history to capture
      real, live model output. The live, unedited transcript is used
      in Chapter 3's `lesson.html` as an illustrative "Live-Captured
      Compression Example," including honest disclosure that the model
      did not fully follow an explicit instruction in the prompt (asked
      to omit one fact, it included it anyway) — used directly as the
      lesson's own argument for why load-bearing facts are pinned via a
      separate, deterministic mechanism rather than trusted to a
      summarization call's instruction-following. No graded
      `solution.py` in Chapter 3 depends on a live call: this
      repository's own `scripts/local_check.sh` runs every
      `solution.py` under a 20-second timeout, far shorter than several
      of this session's own measured Ollama wait times, so wiring a
      live call into the graded harness would make the automated
      checks themselves unreliable. Disclosed in full in
      `lesson.html`'s own "A Note on This Chapter's Live-Testing"
      section and in `quality-audits/chapter-03-audit.md`.
- [x] **Chapter 3 built and live — "Short-Term Conversational Memory,"
      opening Module 2**. Uses Chapter 1's ledger and Chapter 2's
      allocation recipe as a lens, not fresh material: Line 3's
      already-allocated token budget is a given constraint, not
      re-derived. Hook: Emberlynn Transit Cooperative's RouteLine, a
      transit rider-support assistant that did Chapter 2's own recipe
      correctly for its "Multi-Leg Trip Planning" request type (a real,
      derived 8,680-token Line 3 budget on a 24,000-token window) but
      paired it with a naive FIFO sliding-window eviction mechanism
      that decides what survives purely by recency. A rider's 90-token
      accessibility disclosure (turn 2 of 16) gets evicted well before
      the model recommends a specific transfer point at turn 16,
      because the mechanism has no concept of importance, only recency
      — a genuinely distinct failure from Chapter 1's missing budget and
      Chapter 2's wrong-shaped budget. Builds a six-step Short-Term
      Memory Policy Recipe (start from the allocated budget; size a
      verbatim window; set a compression trigger ahead of the hard
      limit; compress, don't truncate, anything older; pin load-bearing
      facts explicitly, bounded; validate against the worst realistic
      long conversation) and a three-policy comparison table (no policy
      needed; naive FIFO — never sufficient alone; the hybrid policy:
      pinned facts + running summary + verbatim window). Full worked
      token arithmetic for the hook's 16-turn conversation under both
      the naive and hybrid policies. Grounded in 5 real, live-verified
      sources this session (Claude's "Context management on the Claude
      Developer Platform" blog post, Claude Docs "Context editing," the
      MemGPT arXiv paper, OpenAI's "Conversation state" guide, and
      Google Gemini's "Text generation" docs — 2 of 5 required following
      a live redirect, and 2 originally planned URLs were dropped for
      dead/off-topic redirects and replaced with working, on-topic
      sources found live this session, all disclosed honestly in both
      `lesson.html` and the quality audit). 8 exercises (6
      production-gear: running-total arithmetic, verbatim window sizing,
      pin/no-pin classification, compression trigger checks, package
      validation, a naive-vs-hybrid regression gate), 8 practice
      scenarios (4 explicit judgment calls, 4 production-gear) across 8
      fresh fictional orgs, 8 interview questions across all 4 levels,
      and a real, gradeable **L1 Guided project** (Wrayland Behavioral
      Health Group/SupportLine) designing a short-term memory policy
      for a "Recurring Counseling Check-In" request type — its
      self-check mechanically verifies required/forbidden pin
      categories and full-package budget fit against the learner's own
      numbers, leaving only the two administrative facts' pin status
      and both write-ups judgment-graded.
- [x] **Quality audit** (`quality-audits/chapter-03-audit.md`) — honest
      self-critique (including the deliberate choice not to wire a live
      Ollama call into any graded `solution.py`, and a re-flagged note
      that Chapter 4 should re-confirm the one-project-per-chapter
      judgment call before assuming its own project ships solo as
      Module 2's single L2 Assisted project), a fictional-org exclusion
      check extending Chapters 1-2's list with 11 new orgs (33 total in
      this repo), checked against `ai-engineering-for-everyone`'s full
      compiled list with zero collision found, and documentation of the
      two live redirects and two dropped/replaced source URLs
      encountered during citation verification.
- [x] **Step 5: Validation (Chapter 3)** — `scripts/local_check.sh` run
      at the end of this session; passed clean (folder structure,
      placeholder-text scan, Python syntax, every `solution.py` executed
      for real, JS syntax and chapter-path validation, secret scan).
- [x] **Registration updated in the same session (Chapter 3)**:
      `assets/chapters-data.js` (Chapter 3's `path` added), root
      `index.html` (hero-stats now "3 of 13 chapters live," and the
      "All Chapters" intro paragraph rewritten to describe all three
      live chapters and the Module 1 -> Module 2 transition), and
      `docs/curriculum/index.html` (Chapter 3's chapter-card now "Live"
      with a working link, and its own lede paragraph updated).

## Pending / Not Started

- Chapters 4-13 (the remainder of Module 2 onward) — scaffolded with
  `.gitkeep` only, no content. Per this ecosystem's standing
  discipline, they are built one chapter at a time in future sessions,
  each validated before the next begins — do not mass-build multiple
  chapters in one pass.
- No module written exams, module-assessments, or architecture
  challenges exist yet — `assessments/` is fully scaffolded but empty
  (`.gitkeep` in every subdirectory) until the modules they cover are
  built.
- No GitHub remote, no GitHub Pages, no push — by explicit instruction,
  this repo stays local-only until a human reviews the course's
  positioning.

## Known Issues

- Ollama's `/api/chat` endpoint timed out across Sessions 1-2 (20s,
  then 75s), but Session 3 finally got real responses — twice — after
  enough patience (a 180-second timeout on the first success, a
  240-second timeout on a later success), confirming
  `ai-engineering-for-everyone`'s own prior finding that this hang
  eventually resolves with a sufficiently patient retry. The important
  new finding for future sessions: it did NOT stay resolved within the
  same session — two later calls in Session 3 timed out again (60s,
  150s) even after a prior successful warm call, before a third,
  more patient attempt succeeded in under 9 seconds. Treat this
  endpoint as *intermittently* slow/hanging, not simply "cold once,
  fast forever after" — a future session needing a live call should
  budget for retries throughout the session, not just at the start,
  and should keep timeouts generous (120s+) even after an earlier call
  in the same session has already succeeded.
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
  to Module 1's own two stated labs, one project per chapter). Chapter
  3 continued this same one-project-per-chapter pattern into Module 2
  (a third L1 Guided project, not the curriculum map's "L2 Assisted"
  tier, which it ties specifically to Chapter 4). This is still a
  judgment call, not a confirmed ecosystem convention — Chapter 4's own
  session must finally resolve it: either ship Chapter 4's project as a
  fourth L1-tier project matching this pattern, or ship the curriculum
  map's literal "L2 Assisted" project once, solo, at the end of Chapter
  4, closing out Module 2. Whichever way Chapter 4 resolves this, it
  should update this note so Module 3 doesn't inherit the same open
  question a third time.

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

**Chapter 4 — "Long-Term and Persistent Memory Systems," completing Module 2.**

Per `docs/curriculum/CURRICULUM_MAP.md`: Module 2 (Memory Systems),
Chapters 3-4. Module 2's outcomes: "design short-term memory that
stays in budget; design a long-term memory system with a real
retrieval-into-context policy." Chapter 3 already delivered the first
outcome (short-term memory inside Line 3's budget). Chapter 4 owns Line
4 of the ledger (Recalled Long-Term Memory) and the second outcome
directly: what a system stores persistently across sessions (not just
within one conversation), and — the part that actually touches context
engineering rather than generic database design — the real *policy*
for what gets retrieved back into Line 4 for a given turn, and what
stays dormant. Its lab, per the module outcomes: "design a persistent
memory store and retrieval policy." Chapter 5 (Context Compression and
Summarization, opening Module 3) is the next chapter after that — do
not build both in one session, per this ecosystem's one-chapter-at-a-
time discipline.

What NOT to re-derive:
- The five-line Context Budget Ledger (Chapter 1), the five-step
  Budget Allocation Recipe (Chapter 2), and the six-step Short-Term
  Memory Policy Recipe (Chapter 3) are already-built material. Chapter
  4 should use Line 4's *allocated budget* (a real number, once
  Chapter 2's recipe has been run for whatever request type Chapter 4's
  hook uses) as a given constraint, the same way Chapter 3 treated
  Line 3's budget as given rather than re-derived. Chapter 4's own job
  is the boundary Chapter 3's own MemGPT citation already named: what
  crosses from "fast," in-conversation memory (Line 3, bounded by a
  single conversation) into genuinely persistent storage that outlives
  any one conversation, and what real policy governs pulling it back
  into Line 4 later. Do not re-explain short-term eviction/compression
  mechanics (pinning, verbatim windows, running summaries) — Chapter 4
  can reference them briefly as the *boundary* it starts from, not
  re-teach them.
- The course's positioning relative to `rag-for-everyone`,
  `mcp-for-everyone`, and `ai-engineering-for-everyone` Chapter 3 is
  already established in `docs/discovery-notes.md` and Chapter 1's own
  "Why This Course Exists" section — Chapter 4 can reference it briefly
  but should not re-argue it from scratch. Chapter 4 sits closest to
  `rag-for-everyone` of any chapter so far (persistent storage +
  retrieval sounds retrieval-adjacent) — state explicitly, the way
  Chapter 3 stated its own boundary with that course, what Chapter 4 is
  NOT doing: it does not design a retrieval *architecture* (ranking,
  embeddings, vector-store mechanics are that course's subject); it
  decides what a context-engineering system stores in the first place
  and what real policy pulls a stored memory back into Line 4 for a
  specific turn, assuming retrieval mechanics already exist by
  whatever means. This distinction needs to be as explicit in Chapter
  4's own lesson text as Chapter 1's "Why This Course Exists" section
  was for the whole course.
- Read Chapter 3's own quality audit
  (`quality-audits/chapter-03-audit.md`) before starting, not just the
  curriculum map — per `AI_HANDOFF.md`'s own standing instruction, it
  may surface scope notes this file doesn't fully capture. In
  particular: the open L1/L2 project-ladder judgment call (see "Open
  Decisions" above) must finally be resolved this session, one way or
  the other, and the resolution documented in Chapter 4's own audit and
  in this file — don't leave it open a third time.

New-org exclusion list: read `quality-audits/chapter-03-audit.md`'s
full running list (Chapters 1-2's combined 22 orgs plus Chapter 3's 11
new orgs — Emberlynn Transit Cooperative, Quarrowstead Legal Aid
Partners, Larkmoth Outdoor Retail, Feldspar Municipal Water Utility,
Pemberglen Veterinary Partners, Sootmarsh Freight Cooperative, Glennoak
Wealth Advisors, Tarnwick Community College, Hushfield Telehealth
Network, Vallowmere Grocery Cooperative, Wrayland Behavioral Health
Group — 33 total in this repo) plus `ai-engineering-for-everyone`'s own
full compiled list (see that repo's `quality-audits/chapter-13-audit.md`)
before naming any new fictional org for Chapter 4, and extend — don't
restart — the list in `quality-audits/chapter-04-audit.md`.

Citation/Ollama re-verification discipline: do not assume Chapter 3's
five citations are still live — re-fetch and re-read anything reused,
and treat all-new sources as the default (two of Chapter 3's five
already needed a live-redirect follow, and two originally planned URLs
were dead/off-topic and had to be replaced entirely — expect the same
kind of churn again, not stability by default). Re-check Ollama's
`/api/tags` and `/api/chat` fresh at the start of the session. Chapter
3's own session found the hang is *intermittent*, not a simple "cold
once, fast forever after" pattern — two later calls timed out again
even after an earlier call in the same session had already succeeded
warm. Budget for retries throughout the session, not just at the
start, keep timeouts generous (120s+) throughout, and disclose the
full honest sequence of attempts (not just the best result) the way
Chapter 3's own lesson and this file both did. Chapter 4 is a strong
candidate for another genuinely load-bearing live capture (e.g. a
retrieval-relevance judgment call, "should this stored memory be
recalled for this turn") if the session has room for it — but keep any
such example illustrative-only in the lesson text, not wired into a
graded `solution.py`, given `scripts/local_check.sh`'s 20-second
per-solution timeout and this sandbox's demonstrated latency variance.

Registration-staleness check reminders: once Chapter 4's `lesson.html`
exists, update `assets/chapters-data.js` (add its `path`), the root
`index.html` (`hero-stats` counts and the "All Chapters" intro
paragraph — note it should read "4 of 13 chapters live" and "2 of 6
modules complete" once Chapter 4 ships, since it completes Module 2),
and `docs/curriculum/index.html` (its own chapter-card status and lede
paragraph) in the same session — these four locations drifted stale in
multiple sibling courses' own build histories when a chapter shipped
without updating all four at once.

Local validation, done at the end of every session:

```
$ bash scripts/local_check.sh
```

Passed clean at the end of this session (Chapter 3) — folder
structure, placeholder-text scan, Python syntax, every `solution.py`
executed for real, JS syntax and chapter-path validation, secret scan.
See this session's own commit message / `AI_HANDOFF.md` for the exact
result recorded.
