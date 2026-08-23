# PROJECT_STATE.md — Context Engineering for Everyone

Last updated: 2026-08-23 (Session 5 — Chapter 5, "Context Compression
and Summarization," complete, opening Module 3. Session 4 built Chapter
4, closing Module 2 in full. Session 3 built Chapter 3, opening Module
2. Session 2 built Chapter 2, completing Module 1. Session 1 built
Discovery, the curriculum map, the full repository scaffold, and
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
- [x] **Chapter 4 built and live — "Long-Term and Persistent Memory
      Systems," closing Module 2 in full**. Uses Chapter 1's ledger,
      Chapter 2's allocation recipe, and Chapter 3's short-term policy
      as a lens, not fresh material: Line 4's already-allocated token
      budget is a given constraint, the same way Chapter 3 treated Line
      3's budget as given. Hook: Nightbourne Senior Living Network's
      HearthLine, a family-facing senior-living assistant that got
      Chapters 1-3 completely right — a real, correctly derived Line 4
      budget (1,200 tokens) and a correct Chapter 3 hybrid short-term
      policy inside every session — and still lost a family's
      fall-risk disclosure three weeks later, because nothing decided
      what should survive a session boundary at all; Line 3 was
      correctly cleared per Chapter 3's own recipe, and no persistent
      store existed to have caught the fact first. A genuinely distinct
      failure from all three prior chapters' hooks (no budget; wrong-
      shaped budget; correct budget, naive within-session eviction).
      Builds a six-step Long-Term Memory Policy Recipe (decide write
      criteria; decide the storage shape; decide the retrieval scope;
      handle staleness explicitly; bound Line 4's own budget; validate
      against the longest realistic relationship) and a three-approach
      comparison table (no persistent memory needed; naive append-only
      log — never sufficient; the curated store: write criteria +
      storage shape + scoped, staleness-aware retrieval). Introduces
      staleness handling (active/superseded/expired record status) as
      the one recipe step with no Chapter 3 analog — short-term memory
      only ever asked whether a fact was recent; long-term memory has
      to ask whether it's still true. Full worked math for HearthLine's
      hook across "no memory," "naive append," and "curated" approaches.
      Grounded in 5 real, live-verified sources this session (Claude's
      "Context management" blog post — the same URL Chapter 3 cited,
      re-verified live and cited here for a different passage, disclosed
      explicitly; LangGraph's memory-concepts docs; a Letta blog post on
      memory blocks; Google Cloud's Vertex AI Memory Bank docs, following
      a live redirect; and AWS's Bedrock Agents memory docs, disclosed
      honestly as describing a product now in "Classic/maintenance
      mode" — no OpenAI source made this chapter's final five, disclosed
      as a real change from every prior chapter, not an oversight; two
      candidate Anthropic/OpenAI URLs 404'd and two more OpenAI URLs
      403'd during verification). 8 exercises (6 production-gear:
      uncurated-growth arithmetic, retrieval budget sizing, write/no-
      write classification, staleness resolution, package validation, a
      naive-append-vs-curated regression gate), 8 practice scenarios (4
      judgment calls, 4 production-gear) across 8 fresh fictional orgs,
      8 interview questions across all 4 levels, and a real, gradeable
      **L2 Assisted project** (Brightmoor Elder Law Group/CaseLine) that
      finally resolves the L1/L2 project-ladder question Chapters 2-3
      left open — see "Open Decisions" below — by shipping the
      curriculum map's own literal L2 tier once, solo, closing the
      module; its self-check mechanically verifies both a short-term
      package (Chapter 3's own skill, reused) and a long-term retrieval
      package (this chapter's skill, including staleness exclusion)
      against the learner's own numbers at once.
- [x] **Quality audit** (`quality-audits/chapter-04-audit.md`) — honest
      self-critique (including the disclosed gap that no artifact in
      this chapter exercises staleness *detection*, only the policy
      once staleness is already labeled, flagged for a later chapter),
      a fictional-org exclusion check extending Chapters 1-3's list with
      11 new orgs (44 total in this repo), checked against
      `ai-engineering-for-everyone`'s own full compiled list with zero
      collision found, the L1/L2 project-ladder decision finally
      resolved and documented (see "Open Decisions" below), and full
      documentation of the citation churn (one redirect, one dropped/
      replaced source URL, two additional 404s, two 403s) encountered
      during verification.
- [x] **Step 5: Validation (Chapter 4)** — `scripts/local_check.sh` run
      at the end of this session; passed clean (folder structure,
      placeholder-text scan, Python syntax, every `solution.py` executed
      for real, JS syntax and chapter-path validation, secret scan).
- [x] **Registration updated in the same session (Chapter 4)**:
      `assets/chapters-data.js` (Chapter 4's `path` added), root
      `index.html` (hero-stats now "4 of 13 chapters live" / "2 of 6
      modules complete," and the "All Chapters" intro paragraph
      rewritten to describe all four live chapters and Module 2's
      completion), and `docs/curriculum/index.html` (Chapter 4's
      chapter-card now "Live" with a working link, and its own lede
      paragraph updated to describe Module 2's completion).
- [x] **Ollama re-checked fresh in Session 4, with two consecutive
      first-attempt successes, disclosed honestly as one session's data
      point, not a claim the earlier intermittent-hang finding no
      longer holds**: `/api/tags` responded normally
      (`llama3.2:latest` still installed). `/api/chat` was called
      twice: a first call (150-second timeout) returned in ~74.4
      seconds, mostly cold model-load time; a second, warm call
      (90-second timeout) returned in ~21.8 seconds. Unlike Chapter 3,
      neither call needed a retry this session — reported honestly as
      what happened, not generalized into "the hang is fixed," since
      Chapter 3 already showed a successful warm call can still be
      followed by a later timeout within the same session. The first
      capture is used in Chapter 4's `lesson.html` as a live,
      unedited "Live-Captured Write-Extraction Example," notable for
      correctly following an exclusion instruction Chapter 3's own
      capture did not follow — used honestly as one data point in
      either direction, not proof instruction-following is now
      reliable; the lesson explicitly argues this is exactly why this
      chapter's write criteria and staleness handling are deterministic,
      rule-based decisions, never delegated to a summarization call's
      judgment. No graded `solution.py` in Chapter 4 depends on a live
      call, for the same 20-second-`local_check.sh`-timeout reason
      Chapter 3 documented.
- [x] **Ollama re-checked fresh in Session 5, two consecutive
      first-attempt successes**: `/api/tags` responded normally
      (`llama3.2:latest` still installed). `/api/chat` was called
      twice, both under a 200-second timeout: a first call (a
      compression prompt with an explicit exclusion instruction)
      returned in **64 seconds**, mostly cold model-load time; a second,
      warm call a few minutes later returned in **8 seconds**. Reported
      honestly as this session's own result, following the same two
      consecutive first-attempt successes Session 4 got — not treated as
      evidence the earlier intermittent-hang finding no longer applies,
      since Session 3 already showed a warm success can still be
      followed by a later timeout within one session. The first capture
      is used in Chapter 5's `lesson.html` as a live, unedited
      "Live-Captured Compression Example," notable for a genuinely
      partial result: the model correctly omitted a literal PIN value it
      was told to exclude, but still described the excluded fact's shape
      ("a 4-digit account number") — read honestly as a small, real
      instance of the "decontextualization" fidelity-loss pattern named
      in this chapter's own fifth citation, neither a clean pass nor a
      clean failure. No graded `solution.py` in Chapter 5 depends on a
      live call, for the same 20-second-`local_check.sh`-timeout reason
      every prior chapter documented.
- [x] **Chapter 5 built and live — "Context Compression and
      Summarization," opening Module 3**. Uses Chapters 1-4 as a lens,
      not fresh material: the token budget, the compression trigger, the
      pin/summary/window shape, and the long-term write/retrieval
      policy are all given inputs, not re-derived. This chapter's own
      job is the one thing Chapter 3's own recipe named but deliberately
      left unengineered — the actual mechanics a compression call uses
      to decide what survives when content no longer fits its budget.
      Hook: Brannigan Home Energy Services' GridLine, a meter-
      troubleshooting assistant that implemented every recipe through
      Chapter 4 correctly (a real budget, a real trigger, a real
      pin/summary/window shape, a real long-term policy) and still lost
      a load-bearing detail — a cross-turn correlation between meter
      resets and furnace timing, real but never individually pin-worthy
      or write-worthy — because its compression step was a single
      "summarize as concisely as possible" call with no pre-extraction
      and no post-hoc check. A genuinely distinct failure from all four
      prior chapters' hooks (no budget; wrong-shaped budget; correct
      budget, naive within-session eviction; correct short-term policy,
      no cross-session memory at all). Builds a six-step Compression
      Fidelity Recipe (identify what's already exempt; extract
      load-bearing candidates before compressing; choose a strategy
      matched to content type; bound the target explicitly; run the
      compression; validate fidelity before shipping) and a
      three-approach comparison table (no compression needed; naive
      summarization — never sufficient alone; the fidelity-checked
      pipeline: pre-extraction + bounded, strategy-matched compression +
      post-hoc validation). Full worked math for GridLine's 2,400-token
      hook segment compressed to the same 480-token target under both
      naive and fidelity-checked approaches, showing the fix was never
      "compress less" but compressing on purpose. Grounded in 5 real,
      live-verified sources this session (Anthropic's "Effective context
      engineering for AI agents," OpenAI's Cookbook "Summarizing long
      documents" following a live redirect, LangChain's "Short-term
      memory" docs, Google's Gemini "Long context" docs, and an arXiv
      preprint on information fidelity in LLM-compressed financial
      analysis — the first non-vendor-documentation academic source
      since Chapter 1's Liu et al. citation, disclosed honestly as a
      preprint rather than a peer-reviewed or long-established source).
      8 exercises (6 production-gear: compression ratio arithmetic,
      load-bearing candidate classification, a fidelity check,
      extractive-vs-abstractive strategy selection, a naive-vs-
      fidelity-checked regression gate, an escalation decision), 8
      practice scenarios (4 judgment calls, 4 production-gear) across 8
      fresh fictional orgs, and 8 interview questions across all 4
      levels. **No chapter project this session, by design** — per the
      now-confirmed one-project-per-module convention (see "Open
      Decisions" below), Module 3's single project ships once, solo, at
      the end of Chapter 6; `interview-questions.html` says so
      explicitly rather than silently omitting the section a reader
      would expect after four straight chapters that each had one.
- [x] **Quality audit** (`quality-audits/chapter-05-audit.md`) — honest
      self-critique (including the disclosed gap that this chapter's
      fidelity-check exercises test clean string-token matching, not the
      harder real-world problem of detecting a paraphrased or
      partially-present candidate, flagged for a later chapter), an
      explicit confirmation (not a silent omission) that Chapter 5 ships
      no project this session and why, a fictional-org exclusion check
      extending Chapters 1-4's list with 10 new orgs (54 total in this
      repo), checked against `ai-engineering-for-everyone`'s own full
      compiled list with zero collision found (verified with a live
      grep across this repo and that repo's own audit file, not just
      visual inspection), and full documentation of the citation churn
      (one live redirect, one candidate page set aside for a more
      directly relevant one) encountered during verification.
- [x] **Step 5: Validation (Chapter 5)** — `scripts/local_check.sh` run
      at the end of this session; passed clean (folder structure,
      placeholder-text scan, Python syntax, every `solution.py` executed
      for real, JS syntax and chapter-path validation, secret scan).
- [x] **Registration updated in the same session (Chapter 5)**:
      `assets/chapters-data.js` (Chapter 5's `path` added), root
      `index.html` (hero-stats now "5 of 13 chapters live" — "2 of 6
      modules complete" stays as-is, since Module 3 also needs Chapter
      6 — and the "All Chapters" intro paragraph rewritten to describe
      all five live chapters and Module 3 opening), and
      `docs/curriculum/index.html` (Chapter 5's chapter-card now "Live"
      with a working link, and its own lede paragraph updated to
      describe Module 3 opening and the deferred Chapter 6 project).

## Pending / Not Started

- Chapter 6 and Chapters 7-13 — scaffolded with `.gitkeep` only, no
  content. Per this ecosystem's standing discipline, they are built one
  chapter at a time in future sessions, each validated before the next
  begins — do not mass-build multiple chapters in one pass. Chapter 6
  also owns Module 3's single project (per the one-project-per-module
  convention), so it is not a drop-in-content-only session the way
  Chapters 2, 3, and 5 were.
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
  in the same session has already succeeded. Session 4 (Chapter 4) got
  two consecutive first-attempt successes (74.4s cold, 21.8s warm) with
  no retries needed — reported honestly as that session's own result,
  not as evidence the intermittent-hang finding above no longer holds;
  future sessions should still budget for retries and generous
  timeouts by default.
- The "Lost in the Middle" citation (Liu et al., 2023) is the original
  finding, not a more recent replication — flagged in the quality audit
  as something Chapter 6 (which owns this topic in depth) should
  re-verify against more current research before treating the finding
  as settled across all current model families.
- Chapter 5's own fifth citation (`arxiv.org/abs/2606.29251`, "When
  Summaries Distort Decisions: Information Fidelity in LLM-Compressed
  Financial Analysis") is an arXiv preprint, not a peer-reviewed or
  long-established source — flagged in `quality-audits/chapter-05-audit.md`
  for a future revision to re-check whether it has since been published,
  revised, or superseded.
- Chapter 5's own fidelity-check exercises (Exercise 5, Practice
  Scenario 4) test candidate-presence matching against clean,
  hand-authored string tokens, not the harder real-world problem of
  detecting a paraphrased or partially-present candidate inside natural
  language — flagged in `quality-audits/chapter-05-audit.md` as an open
  gap for a later chapter or revision, the same way Chapter 4's audit
  flagged staleness *detection* (vs. staleness *policy*) as unexercised.
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
- **RESOLVED in Session 4 (Chapter 4).** Chapters 2 and 3 each shipped
  a second, module-internal L1-tier project rather than the curriculum
  map's literal "L2 Assisted" tier, logging this as open both times.
  Session 4 finally resolved it: **Chapter 4 shipped the curriculum
  map's literal L2 Assisted project once, solo, closing Module 2**
  ("Design short-term and long-term memory for a provided long-running
  assistant, partial scaffold"), rather than a fourth L1-tier project.
  Reasoning (full detail in `quality-audits/chapter-04-audit.md`):
  continuing the one-L1-per-chapter pattern a third time would mean
  Module 2 never produced the L2-tier artifact the curriculum map
  calls for, silently drifting the whole project ladder one tier behind
  its own stated schedule. **Confirmed convention going forward: one
  project per module, at the project ladder's own stated tier, not one
  project per chapter.** Module 3 (Chapters 5-6) should plan for a
  single L2/L3-tier-appropriate project shipping once, at the end of
  Chapter 6 — not a project at the end of each of Chapters 5 and 6
  individually. This question should not resurface as "open."
  **Session 5 (Chapter 5) applied this convention as intended**: Chapter
  5 shipped no project of its own, confirmed explicitly in both
  `lesson.html`/`interview-questions.html` and
  `quality-audits/chapter-05-audit.md`, rather than silently omitting
  the section. Chapter 6 must ship Module 3's single project — this is
  now a firm commitment, not a default to re-litigate.

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

**Chapter 6 — "Avoiding Lost-in-the-Middle," closing Module 3 — and
shipping Module 3's single project.**

Per `docs/curriculum/CURRICULUM_MAP.md`: Module 3 (Context Compression
and Curation), Chapters 5-6. Module 3's outcomes: "compress/summarize
context without losing load-bearing content; order context to avoid
lost-in-the-middle degradation." Chapter 5 (this session) owned the
first outcome — the real compression *mechanics* (a six-step
Compression Fidelity Recipe) that decide what survives when content no
longer fits its budget. Chapter 6 owns the second outcome: given that
content has survived compression intact (Chapter 5's own subject),
*where* it gets placed inside the final assembled context window
measurably changes how reliably the model actually uses it — the "lost
in the middle" effect Chapter 1's own hook first named in passing.
Chapter 6's own lab, per the module outcomes: "reorder a context window
to fix a lost-in-the-middle failure." Per the now-confirmed
one-project-per-module convention (see "Open Decisions" above, applied
as intended in Chapter 5's own session), **Chapter 6 must also ship
Module 3's single project** — this is a firm commitment carried forward
from Chapter 5's session, not a default to re-litigate. Read Chapter
5's own quality audit before scoping Chapter 6's project shape against
the module's stated lab and outcomes, per `AI_HANDOFF.md`'s standing
instruction not to assume Chapter 6's scope from the curriculum map
alone.

What NOT to re-derive:
- The five-line Context Budget Ledger (Chapter 1), the five-step
  Budget Allocation Recipe (Chapter 2), the six-step Short-Term Memory
  Policy Recipe (Chapter 3), the six-step Long-Term Memory Policy
  Recipe (Chapter 4), and the six-step Compression Fidelity Recipe
  (Chapter 5) are already-built material. Chapter 6 should re-read
  Chapter 5's own "Context Engineering Builder Thought Process" section
  (it explicitly named ordering/positioning as deferred to Chapter 6)
  before scoping its own content, so it neither re-teaches what Chapter
  5 already covered (deciding what content survives compression) nor
  leaves a gap between the two. Chapter 6's own new job is the
  positional question every prior chapter assumed as out of scope: given
  a final, assembled set of content (already correctly budgeted per
  Chapters 1-2, already correctly evicted/compressed per Chapters 3-5,
  already correctly retrieved per Chapter 4), where in the window does
  each piece go, and how does that placement change whether the model
  actually attends to it. Do not re-explain budgeting, pinning,
  write/retrieval criteria, or compression mechanics — Chapter 6 can
  reference them briefly as the *inputs* its own ordering step receives,
  not re-teach them.
- The course's positioning relative to `rag-for-everyone`,
  `mcp-for-everyone`, and `ai-engineering-for-everyone` Chapter 3 is
  already established in `docs/discovery-notes.md` and Chapter 1's own
  "Why This Course Exists" section — Chapter 6 can reference it briefly
  but should not re-argue it from scratch.
- Read Chapter 5's own quality audit
  (`quality-audits/chapter-05-audit.md`) before starting, not just the
  curriculum map — per `AI_HANDOFF.md`'s own standing instruction, it
  may surface scope notes this file doesn't fully capture.
- **Re-verify the "Lost in the Middle" citation (Liu et al., 2023)
  against more current research before treating the finding as settled
  across all current model families** — flagged in the Known Issues
  section above across multiple prior chapters as something Chapter 6
  specifically, not any earlier chapter, owns resolving, since this is
  the chapter where that finding moves from a supporting citation to
  the chapter's own central subject.

New-org exclusion list: read `quality-audits/chapter-05-audit.md`'s
full running list (Chapters 1-4's combined 44 orgs plus Chapter 5's 10
new orgs — Brannigan Home Energy Services, Kirkholme Public Transit
Safety Board, Lynhaven Community Health Partners, Sablewood Legal
Trust, Coalridge Municipal Transit Authority, Pikestone Logistics
Group, Rowancraig Insurance Underwriters, Draymoor Agricultural
Cooperative, Osprey Ridge Wealth Management, Talmarsh Veterinary
Alliance — 54 total in this repo) plus `ai-engineering-for-everyone`'s
own full compiled list (see that repo's
`quality-audits/chapter-13-audit.md`) before naming any new fictional
org for Chapter 6, and extend — don't restart — the list in
`quality-audits/chapter-06-audit.md`.

Citation/Ollama re-verification discipline: do not assume Chapter 5's
five citations are still live — re-fetch and re-read anything reused,
and treat all-new sources as the default (Chapter 5's own session
needed to follow one live redirect and set aside one initially
attempted candidate page in favor of a more directly relevant one —
expect similar churn, not stability by default). Re-check Ollama's
`/api/tags` and `/api/chat` fresh at the start of the session, even
though Chapters 4 and 5 both got two consecutive first-attempt
successes — Chapter 3 already showed a successful warm call can still
be followed by a later timeout within the same session, so treat the
endpoint as intermittently slow/hanging by default, budget for retries
throughout the session, not just at the start, and keep timeouts
generous (120s+) throughout.

Registration-staleness check reminders: once Chapter 6's `lesson.html`
exists, update `assets/chapters-data.js` (add its `path`), the root
`index.html` (`hero-stats` counts and the "All Chapters" intro
paragraph — it should read "6 of 13 chapters live" AND "3 of 6 modules
complete" once Chapter 6 ships, since it closes Module 3), and
`docs/curriculum/index.html` (its own chapter-card status and lede
paragraph) in the same session — these four locations drifted stale in
multiple sibling courses' own build histories when a chapter shipped
without updating all four at once.

Local validation, done at the end of every session:

```
$ bash scripts/local_check.sh
```

Passed clean at the end of this session (Chapter 5) — folder
structure, placeholder-text scan, Python syntax, every `solution.py`
executed for real, JS syntax and chapter-path validation, secret scan.
See this session's own commit message / `AI_HANDOFF.md` for the exact
result recorded.
