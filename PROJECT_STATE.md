# PROJECT_STATE.md — Context Engineering for Everyone

Last updated: 2026-08-23 (Session 8 — Chapter 8, "Retrieval Integration:
From Ranked Results to Context," complete, closing Module 4 in full and
shipping Module 4's single L3 Independent project, the curriculum map's
own literal L3 tier. Session 7 built Chapter 7, opening Module 4,
shipping no project of its own. Session 6 built Chapter 6, closing
Module 3 in full and shipping Module 3's single joint project. Session 5
built Chapter 5, opening Module 3. Session 4 built Chapter 4, closing
Module 2 in full. Session 3 built Chapter 3, opening Module 2. Session 2
built Chapter 2, completing Module 1. Session 1 built Discovery, the
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
- [x] **Ollama re-checked fresh in Session 6, two consecutive
      first-attempt successes**: `/api/tags` responded normally
      (`llama3.2:latest` still installed). `/api/chat` was called
      twice, both under a 200-second timeout: a first call (a
      positional-bias prompt placing a load-bearing fact in the middle
      of a short context) returned in **113.7 seconds**, almost
      entirely cold model-load time (~100s); a second, warm call a few
      minutes later returned in **5.1 seconds**. Reported honestly as
      this session's own result, consistent with Sessions 4 and 5's own
      consecutive successes, not treated as evidence the earlier
      intermittent-hang finding no longer applies. The first capture is
      used in Chapter 6's `lesson.html` as a live, unedited "Live-
      Captured Positional Example," notable for a genuinely nuanced
      partial result: the model correctly extracted a specific
      identifier (a forklift serial number) from a middle-positioned
      fact while explicitly reporting the fact's own substance as "isn't
      stated," when it plainly was — read honestly as a real instance of
      position affecting reliability even when nothing about the fact
      was missing, ambiguous, or compressed away. No graded
      `solution.py` in Chapter 6 depends on a live call, for the same
      20-second-`local_check.sh`-timeout reason every prior chapter
      documented.
- [x] **Chapter 6 built and live — "Avoiding Lost-in-the-Middle,"
      closing Module 3 in full**. Uses Chapters 1-5 as a lens, not
      fresh material: the token budget, pin/summary/window shape,
      long-term write/retrieval policy, and fidelity-checked compression
      pipeline are all given inputs, not re-derived. This chapter's own
      job is the positional question every prior chapter assumed out of
      scope: given a final, assembled set of already-correctly-included
      content, *where* it sits inside the window measurably changes
      whether the model actually uses it. Hook: Marchside Regional
      Trauma Network's VitalsLine, a pre-op review assistant that
      implemented every recipe through Chapter 5 correctly (a real
      budget, a real pin/summary/window shape, a real long-term recall
      policy, a real fidelity-checked compression pipeline) and still
      failed to surface a documented, present, unmodified lidocaine
      allergy fact, because nothing decided where it belonged once
      everything correct was already inside the window — a genuinely
      distinct failure from all five prior chapters' hooks (no budget;
      wrong-shaped budget; naive within-session eviction; no
      cross-session memory; an uncontrolled compression call). Builds a
      five-step Context Ordering Recipe (rank by load-bearing weight;
      reserve the anchor positions for the highest-weight content;
      reorder the middle deliberately; put the query near the end,
      closest to generation; test position directly with an explicit
      probe, re-run after any model/length change) and a three-approach
      comparison table (arrival order; naive "move everything to the
      top" — still leaves the query anchor uncovered; weight-ranked,
      both-anchors, position-tested placement). Full worked math for
      VitalsLine's 2,900-token hook window compared across all three
      approaches. **Re-verified the "Lost in the Middle" (Liu et al.,
      2023) citation this session, resolving the Known Issue flagged
      since Chapter 1**: fetched two additional, more recent sources
      live — Hsieh et al.'s 2024 "Found in the Middle" (identifies the
      mechanistic cause, an intrinsic U-shaped attention bias, and a
      partially corrective calibration method) and Chroma's 2025
      "Context Rot" report (an 18-frontier-model 2025 replication,
      including GPT-4.1/Claude 4/Gemini 2.5/Qwen3, confirming the effect
      persists on current models while surfacing a genuine nuance —
      models performed better on shuffled than structurally coherent
      long contexts). The lesson's own "Re-Verification" section states
      the honest conclusion directly: the core claim still holds on
      2025-era frontier models, but its exact shape is now understood to
      be model- and length-specific with a mechanistic, partially
      correctable cause, not a fixed universal curve. Grounded in these
      5 real, live-verified sources this session (Liu et al.'s original
      2023 paper, re-fetched and confirmed unchanged; Hsieh et al. 2024;
      Chroma's 2025 report, following a live redirect; Anthropic's
      Claude Platform Docs long-context-prompting guidance, following a
      live redirect after its dedicated URL was folded into a
      consolidated page; and LangChain's `LongContextReorder` API
      reference, cited after LangChain's own how-to guide for the same
      feature was found to be a genuine dead link this session,
      disclosed honestly rather than silently swapped). 8 exercises (6
      production-gear: position-percentile arithmetic, load-bearing
      weight classification, a positional probe, query-anchor
      classification, an arrival-order-vs-weight-ranked regression gate,
      a retest/escalation decision), 8 practice scenarios (4 judgment
      calls, 4 production-gear) across 8 fresh fictional orgs, and 8
      interview questions across all 4 levels. **Ships Module 3's single
      guided project this session**, drawing on both Chapter 5
      (compression fidelity) and Chapter 6 (context ordering) together
      per the curriculum map's own paired Module 3 labs — Brackholt
      County Court Records Office/ArchiveLine, a two-part design task
      whose self-check mechanically verifies both Part 1's compression
      candidate/strategy choices and Part 2's anchor/middle placement
      rules and budget fit. Disclosed honestly as sitting between the
      curriculum map's own L2 and L3 tiers, since the map's numbered
      project ladder does not itself assign a tier to Module 3 (full
      reasoning in `quality-audits/chapter-06-audit.md`).
- [x] **Quality audit** (`quality-audits/chapter-06-audit.md`) — honest
      self-critique (including the disclosed gap that this chapter's
      positional-probe exercises validate against clean hand-authored
      position/weight labels, not real natural-language model output,
      flagged for a later chapter), the full Lost-in-the-Middle
      re-verification writeup, the honest project-tier resolution (no
      numbered ladder tier applies to Module 3; this is the course's own
      one-project-per-module convention filling the L2/L3 gap), a
      fictional-org exclusion check extending Chapters 1-5's list with
      11 new orgs (65 total in this repo), checked against
      `ai-engineering-for-everyone`'s own full compiled list with zero
      collision found, and full documentation of the citation churn
      (two live redirects to relocated content, one genuine dead link
      requiring a different source page from the same provider)
      encountered during verification.
- [x] **Step 5: Validation (Chapter 6)** — `scripts/local_check.sh` run
      at the end of this session; passed clean (folder structure,
      placeholder-text scan, Python syntax, every `solution.py` executed
      for real, JS syntax and chapter-path validation, secret scan).
- [x] **Registration updated in the same session (Chapter 6)**:
      `assets/chapters-data.js` (Chapter 6's `path` added), root
      `index.html` (hero-stats now "6 of 13 chapters live" / "3 of 6
      modules complete," and the "All Chapters" intro paragraph rewritten
      to describe all six live chapters and Module 3's completion), and
      `docs/curriculum/index.html` (Chapter 6's chapter-card now "Live"
      with a working link, its own lede paragraph updated, and Module
      3's feature card marked "Complete").
- [x] **Ollama re-checked fresh in Session 7 (after a session-interrupting
      connection error), two consecutive first-attempt successes**:
      `/api/tags` responded normally (`llama3.2:latest` still
      installed). Before the interruption, `/api/chat` was called twice
      and captured the chapter's own substantive live example (a
      contradiction-resolution prompt using the hook's own two
      disagreeing sources): a first call returned in ~109 seconds
      (mostly cold load), a second warm call in ~5.1 seconds — used
      directly in `lesson.html`'s "A Live-Captured Contradiction
      Example" section. After resumption, this session re-confirmed
      Ollama's availability with two more calls (a supplementary
      connectivity check, not a new substantive capture): a first call
      (150-second timeout) returned in **64.8 seconds** (~60.9s cold
      load), a second warm call in **10.9 seconds**. Both rounds
      consistent with Chapters 4, 5, and 6's own consecutive successes,
      reported honestly as this session's own result, not evidence the
      earlier intermittent hang is permanently resolved.
- [x] **Chapter 7 built and live — "Multi-Source Context Assembly,"
      opening Module 4**. Uses Chapters 1-6 as a lens, not fresh
      material: the token budget, memory policies, the Compression
      Fidelity Recipe, and the Context Ordering Recipe are all given
      inputs, not re-derived. This chapter's own job is the question
      every prior chapter deferred: which sources belong in a window at
      all, and how do several different sources — retrieved documents,
      live tool output, conversation history, system instructions — get
      combined into one coherent window without silently contradicting
      or crowding each other out, before Chapter 6's own ordering recipe
      ever runs. Hook: Hadleworth Metro Water Authority's ConfluenceLine,
      a customer-service assistant that implemented every recipe through
      Chapter 6 correctly (a real budget, no eviction problem, nothing
      to recall, nothing needing compression, both facts sitting at
      reasonable positions with no lost-in-the-middle risk) and still
      gave a functionally wrong, hedged answer, because a retrieved
      knowledge-base article and a live advisory-status tool call — both
      individually correct — contradicted each other about the same
      fact, with nothing deciding which should govern. Builds a six-step
      Source Assembly Recipe (inventory every candidate source; assign
      each source type an authority rank per request type; detect
      overlapping and contradicting claims before assembly; resolve or
      explicitly surface each contradiction found; deduplicate restated
      content; hand the resolved set to Chapter 6's own ordering recipe)
      and a three-approach comparison table (naive concatenation; string-
      level deduplication only — never sufficient alone; the Source
      Assembly Recipe). Full worked math for Hadleworth's 610-token
      assembled turn compared across all three approaches (610 tokens
      naive/string-dedup vs. 470 tokens and one unambiguous claim under
      the recipe). A genuinely nuanced live-captured example: the model
      reasoned its way to the correct authority conclusion in the
      abstract (trust the live source) but gave a concrete recommendation
      that contradicted its own stated conclusion — used directly as the
      lesson's own argument for why resolution must be a deterministic
      pipeline step. Grounded in 5 real, live-verified sources this
      session, all fetched clean with no redirects or dead links (a
      different, less churny outcome than Chapters 3-6's own sessions):
      Anthropic's "Effective context engineering for AI agents" (Step 5's
      "informative, yet tight" citation), Wang et al.'s "Resolving
      Knowledge Conflicts in Large Language Models" (2023, Step 4's three
      desiderata), Xu et al.'s "Knowledge Conflicts for LLMs: A Survey"
      (EMNLP 2024, Step 3's "inter-context conflict" taxonomy),
      LangChain's `create_stuff_documents_chain` API reference (the
      "stuff" pattern, naive-concatenation row), and Microsoft's Azure AI
      Search RAG documentation ("multi-source data access" as a named RAG
      challenge). 8 exercises (6 production-gear: authority-rank conflict
      resolution, contradiction detection, deduplication arithmetic, a
      post-resolution budget check, a naive-vs-recipe regression gate, an
      escalation decision), 8 practice scenarios (4 judgment calls, 4
      production-gear) across 8 fresh fictional orgs, and 8 interview
      questions across all 4 levels. **No chapter project this session,
      by design** — per the one-project-per-module convention, Module
      4's single project is planned for the end of Chapter 8, once
      retrieval integration is also in place;
      `interview-questions.html` and `lesson.html` both say so
      explicitly. This session also resumed cleanly from a
      connection-error interruption partway through the build (after
      `lesson.html`, `quiz.html`, and part of `exercises/` were already
      on disk) — everything already on disk was verified correct before
      the session continued, rather than restarted from scratch.
- [x] **Quality audit** (`quality-audits/chapter-07-audit.md`) — honest
      self-critique (including the disclosed gap that this chapter's
      contradiction-detection exercises classify clean, hand-labeled
      claim pairs rather than detecting contradictions from real
      unlabeled natural-language text, flagged for a later chapter), an
      explicit confirmation that Chapter 7 ships no project and why
      (including the finding that Module 4's project lands cleanly on
      the curriculum map's own L3 Independent tier already assigned to
      Chapter 8, unlike Module 3's tier gap), a fictional-org exclusion
      check extending Chapters 1-6's list with 10 new orgs (75 total in
      this repo), checked against `ai-engineering-for-everyone`'s own
      full compiled list with zero collision found, and confirmation
      that all 5 citations were fetched clean this session with no
      redirects or dead links.
- [x] **Step 5: Validation (Chapter 7)** — `scripts/local_check.sh` run
      at the end of this session; passed clean (folder structure,
      placeholder-text scan, Python syntax, every `solution.py` executed
      for real, JS syntax and chapter-path validation, secret scan).
- [x] **Registration updated in the same session (Chapter 7)**:
      `assets/chapters-data.js` (Chapter 7's `path` added), root
      `index.html` (hero-stats now "7 of 13 chapters live" — "3 of 6
      modules complete" stays as-is, since Module 4 also needs Chapter
      8 — and the "All Chapters" intro paragraph rewritten to describe
      all seven live chapters and Module 4 opening), and
      `docs/curriculum/index.html` (Chapter 7's chapter-card now "Live"
      with a working link, its own lede paragraph updated, and Module
      4's feature card marked "In Progress").

- [x] **Ollama re-checked fresh in Session 8, two consecutive
      first-attempt successes**: `/api/tags` responded normally
      (`llama3.2:latest` still installed). `/api/chat` was called twice,
      both succeeding on the first attempt: a first call (the hook's own
      stitched, correctly-filtered legal-research prompt, a 200-second
      timeout) returned in **54.1 seconds** (~19.6s cold load); a second
      call (the truncated-clause, noise-present prompt, a 150-second
      timeout) returned in **69.9 seconds** (~0.6s load this time — the
      model was already resident, the longer wall-clock time came from
      generation itself). Reported honestly as this session's own
      result, consistent with Chapters 4-7's own consecutive successes,
      not evidence the earlier intermittent hang is permanently
      resolved.
- [x] **Chapter 8 built and live — "Retrieval Integration: From Ranked
      Results to Context," closing Module 4 in full**. Uses Chapters 1-7
      as a lens, not fresh material: the token budget, memory policies,
      the Compression Fidelity Recipe, the Context Ordering Recipe, and
      the Source Assembly Recipe are all given inputs, not re-derived.
      This chapter's own job is the handoff Chapter 7 deliberately left
      open: turning a retriever's own raw ranked, scored chunk list into
      one well-formed source before it ever reaches Chapter 7's own
      inventory step. Hook: Mossgate Regional Law Library Consortium's
      CiteLine, a legal-research assistant whose retriever ranked the
      one qualifying clause that actually decided a case-law question
      second out of five chunks — correctly — and still lost it, because
      the pipeline always took a fixed top-k of chunks and truncated the
      assembled text by raw character count wherever the budget ran out,
      cutting the clause off mid-sentence with no boundary awareness and
      no recognition that two of the surviving chunks were really one
      continuous paragraph. A genuinely distinct failure from Chapter 7's
      own hook (two individually-correct, fully-included sources
      contradicting each other) — this chapter's failure happens one
      level upstream, entirely within a single retriever's own output,
      before Chapter 7's multi-source problem is even in play. Builds a
      six-step Retrieval Integration Recipe (apply a relevance floor
      before selecting anything; fit surviving chunks to budget at a
      chunk boundary, never truncating mid-sentence; preserve each
      chunk's provenance; stitch adjacent same-document chunks back
      together; handle a low-confidence or empty result set explicitly;
      hand the resolved bundle to Chapter 7's own Source Assembly Recipe
      as one source) and a three-approach comparison table (unconditional
      top-k stuffing; relevance-floor filtering only — never sufficient
      alone; the Retrieval Integration Recipe). Full worked math for
      CiteLine's five ranked chunks compared across all three approaches
      (the naive pipeline's exact-budget block still lost the one clause
      that decided the answer; the recipe produced a single, complete,
      citable 340-token excerpt 160 tokens under budget). Two live-
      captured outcomes this session: a stitched, correctly-filtered
      bundle produced a clean, correctly-cited answer; the same question
      with the qualifying clause truncated away (noise present instead)
      produced a response that avoided confidently misstating the rule
      but still fabricated plausible-sounding reasoning never actually
      grounded in anything retrieved — used directly as a second, more
      nuanced argument for why the recipe's boundary-safe fit and
      stitching steps matter even when a model doesn't fail as visibly as
      the hook's own story. Grounded in 5 real, live-verified sources this
      session, with two of the five original citation candidates caught
      and corrected during live verification (a stale LangChain URL that
      308-redirects to a page with no splitter content, replaced with
      LangChain's current splitter-integrations page; an AWS Bedrock
      relevance-threshold page that returned no fetchable body text,
      replaced with Google Cloud's Agent Search relevance-threshold
      documentation) — a stricter citation-verification outcome than
      Chapter 7's own clean session, disclosed honestly rather than
      smoothed over. 8 exercises (6 production-gear: relevance-floor
      filtering, boundary-safe budget fit, provenance completeness,
      adjacent-chunk stitching, a naive-vs-recipe regression gate, an
      empty/low-confidence result decision), 8 practice scenarios (4
      judgment calls, 4 production-gear) across 8 fresh fictional orgs,
      and 8 interview questions across all 4 levels. **Ships Module 4's
      single project this session, closing the module** — Quartzfield
      Regional Public Defender Consortium's BriefLine, drawing on both
      Chapter 7 (source assembly) and Chapter 8 (retrieval integration)
      together, landing cleanly on the curriculum map's own literal **L3
      Independent** tier (no honest-labeling workaround needed, unlike
      Module 3's own tier gap) — implemented with no scaffold beyond the
      given spec and data, per the L3 tier's own definition.
- [x] **Quality audit** (`quality-audits/chapter-08-audit.md`) — honest
      self-critique (including the disclosed simplification that this
      chapter's boundary-safe-fit exercises deliberately avoid the harder
      trade-off between a lower-scored stitching-completion chunk and a
      higher-scored unrelated one, flagged for a later chapter), full
      confirmation that Module 4's project ships this session at its
      literal L3 Independent tier, a fictional-org exclusion check
      extending Chapters 1-7's list with 11 new orgs (86 total in this
      repo), checked against `ai-engineering-for-everyone`'s own full
      compiled list with zero collision found, and full documentation of
      the two citation corrections made during live verification this
      session.
- [x] **Step 5: Validation (Chapter 8)** — `scripts/local_check.sh` run
      at the end of this session; passed clean (folder structure,
      placeholder-text scan, Python syntax, every `solution.py` executed
      for real, JS syntax and chapter-path validation, secret scan).
- [x] **Registration updated in the same session (Chapter 8)**:
      `assets/chapters-data.js` (Chapter 8's `path` added), root
      `index.html` (hero-stats now "8 of 13 chapters live" / "4 of 6
      modules complete," and the "All Chapters" intro paragraph rewritten
      to describe all eight live chapters and Module 4's completion), and
      `docs/curriculum/index.html` (Chapter 8's chapter-card now "Live"
      with a working link, its own lede paragraph updated, and Module 4's
      feature card marked "Complete").

## Pending / Not Started

- Chapters 9-13 — scaffolded with `.gitkeep` only, no content. Per this
  ecosystem's standing discipline, they are built one chapter at a time
  in future sessions, each validated before the next begins — do not
  mass-build multiple chapters in one pass.
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
  timeouts by default. Session 7 (Chapter 7) also got two consecutive
  first-attempt successes before its own session-interrupting
  connection error (109s cold / 5.1s warm, used for the chapter's own
  substantive live capture), and two more consecutive first-attempt
  successes after resuming (64.8s cold / 10.9s warm, a supplementary
  connectivity re-check) — four consecutive successes total across the
  interruption, still reported as this session's own result, not
  evidence the intermittent-hang finding no longer holds. Session 8
  (Chapter 8) also got two consecutive first-attempt successes (54.1s
  cold with ~19.6s of that load time, 69.9s on a second call whose own
  reported load time was only ~0.6s) — again this session's own result,
  not evidence the pattern is resolved; future sessions should keep
  budgeting for retries with generous (120s+) timeouts regardless.
- **RESOLVED in Session 6 (Chapter 6).** The "Lost in the Middle"
  citation (Liu et al., 2023) was flagged since Chapter 1 as the
  original finding, not a more recent replication. Chapter 6's own
  session re-verified it live against two newer sources: Hsieh et al.
  2024 ("Found in the Middle," a mechanistic explanation and a partially
  corrective calibration method) and Chroma's 2025 "Context Rot" report
  (an 18-frontier-model replication confirming the effect persists on
  2025-era models). Honest conclusion, stated in `lesson.html`'s own
  "Re-Verification" section: the core claim still holds on current
  frontier models, but its exact shape is model- and length-specific
  with a mechanistic, partially correctable cause, not a fixed universal
  curve as the original single paper alone might suggest. Full detail in
  `quality-audits/chapter-06-audit.md`.
- Chapter 6's own positional-probe exercises (Exercise 5, Practice
  Scenario 4, and the project's Part 2 self-check) validate placement
  against clean, hand-authored position/weight labels, not the harder
  real-world problem of deriving load-bearing weight or measuring actual
  positional recall from real model output — flagged in
  `quality-audits/chapter-06-audit.md` as an open gap for a later
  chapter or revision, the same category of gap Chapter 5's own audit
  flagged for its fidelity-check exercises.
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

- **RESOLVED in Session 8 (Chapter 8).** Whether Chapter 8's retrieval-
  integration content would need its own small, runnable retriever stub
  or could use a hand-authored, clearly-labeled example ranked list:
  resolved in favor of hand-authored, clearly-labeled ranked-chunk data
  (scores, token counts, document/section provenance, sequence numbers)
  throughout the lesson, exercises, practice bank, and project — the
  same choice every prior chapter made for its own worked examples, and
  consistent with `local_check.sh`'s own 20-second timeout making a live
  retrieval call in any graded harness unreliable. `rag-for-everyone`
  was not consulted for structural patterns since no retriever-stub
  approach was ultimately needed.
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
  the section. **RESOLVED in Session 6 (Chapter 6).** Chapter 6 shipped
  Module 3's single project as committed, drawing on both Chapter 5
  (compression) and Chapter 6 (ordering) together. It also resolved a
  related, previously unstated question: the curriculum map's own
  numbered project ladder (L1 after Ch. 2, L2 after Ch. 4, L3 after Ch.
  8, L4 the capstone) does not assign any numbered tier to Module 3 at
  all — it jumps from L2 to L3 across Chapters 4-8. Module 3's project is
  therefore labeled "Module 3 Project," not a numbered tier, in every
  artifact — full reasoning in `quality-audits/chapter-06-audit.md`.
  Future modules whose own project falls between two ladder tiers (none
  currently expected, since Modules 4-6 each map cleanly to L3/L4) should
  follow this same honest-labeling precedent rather than inventing an
  unearned numbered tier.

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

**Chapter 9 — "Context Engineering for Tool Use," opening Module 5.**

Per `docs/curriculum/CURRICULUM_MAP.md`: Module 5 (Context Engineering
for Agentic Systems), Chapters 9-11, difficulty Advanced. Module 5's
purpose: "what context a step, tool call, or sub-agent actually needs,
and where deliberate isolation is the right design." Module 5's
outcomes: "engineer context for a tool call; engineer context across a
multi-step/multi-agent pipeline with deliberate isolation." Module 5's
labs: "design the context payload for a tool call; design a multi-step
pipeline's per-step context with isolation where it matters." Chapter 9
opens this module and, per `docs/discovery-notes.md`, is scoped
protocol-agnostic relative to `mcp-for-everyone` — this course engineers
what context a tool call needs (which tool definitions, which results,
how much history), not the wire protocol a tool call uses to happen at
all. Re-confirm that boundary still holds before writing, per the
now-resolved Open Decision above and `docs/discovery-notes.md` section
1.2 — do not assume it silently.

Read `quality-audits/chapter-08-audit.md` before starting, not just this
file or the curriculum map — per `AI_HANDOFF.md`'s own standing
instruction, it may surface scope notes this file doesn't fully capture.
Chapter 8's own session found real value in re-verifying every citation
live even when a URL "looks" like it should still work (two of five
originally planned citations needed correction this session) — carry
that same skepticism into Chapter 9's own citation work, not just a
mechanical re-fetch.

What NOT to re-derive:
- The five-line Context Budget Ledger (Chapter 1), the five-step Budget
  Allocation Recipe (Chapter 2), the six-step Short-Term Memory Policy
  Recipe (Chapter 3), the six-step Long-Term Memory Policy Recipe
  (Chapter 4), the six-step Compression Fidelity Recipe (Chapter 5), the
  five-step Context Ordering Recipe (Chapter 6), the six-step Source
  Assembly Recipe (Chapter 7), and the six-step Retrieval Integration
  Recipe (Chapter 8) are all already-built material. Chapter 9 should
  treat every one of them as a given input where relevant (a tool call's
  own context payload still has to respect Chapter 2's budget, may still
  need Chapter 5's compression if a tool result is large, and if more
  than one source feeds the same tool-call context, Chapter 7's own
  authority-ranking/contradiction discipline still applies) — but
  Chapter 9's own new job is deciding what belongs in a tool call's
  context payload in the first place: which tool definitions the model
  actually needs for this turn (not every registered tool by default),
  how much of a tool's own result belongs in context afterward versus
  being summarized or dropped, and how much prior tool-call history
  should persist into a later turn. This is a genuinely new question
  none of Chapters 1-8 asked, since they all assumed the content
  competing for context was conversational, retrieved, or instructional
  — not the mechanics of a tool call's own request/response shape.
- The course's positioning relative to `rag-for-everyone`,
  `mcp-for-everyone`, and `ai-engineering-for-everyone` Chapter 3 is
  already established in `docs/discovery-notes.md` and Chapter 1's own
  "Why This Course Exists" section — Chapter 9 can reference it briefly
  but should not re-argue it from scratch. Chapter 9's own boundary
  against `mcp-for-everyone` needs the most care of any chapter so far:
  this course assumes a tool call happens by whatever protocol a system
  uses (MCP or otherwise) and engineers only what context that call
  needs and produces — not the protocol mechanics of the call itself.
- **No chapter project is due at the end of Chapter 9** — per the
  curriculum map's own project ladder, Module 5's own project (the L4
  tier does not apply here; re-check the map's own module/project
  table before assuming a tier) ships once, per this course's confirmed
  one-project-per-module convention, likely at the end of Chapter 11
  once Module 5's own three chapters (9, 10, 11) are all built — verify
  this against `CURRICULUM_MAP.md`'s own "Projects" section before
  assuming Chapter 9 needs to ship one solo.

New-org exclusion list: read `quality-audits/chapter-08-audit.md`'s full
running list (Chapters 1-7's combined 75 orgs plus Chapter 8's 11 new
orgs — Mossgate Regional Law Library Consortium, Cobalt Ridge Claims
Adjustment Bureau, Harborlight Maritime Archive Society, Aspenfield
Community College Library, Beacon Crest Genealogy Society, Slatebrook
Patent Research Group, Timberline Structural Engineering Archive, Garnet
Valley Genetic Testing Registry, Poplar Crossing School District
Archive, Otterbend Wildlife Research Station, Quartzfield Regional
Public Defender Consortium — 86 total in this repo) plus
`ai-engineering-for-everyone`'s own full compiled list (see that repo's
`quality-audits/chapter-13-audit.md`, as reproduced in Chapter 8's own
audit) before naming any new fictional org for Chapter 9, and extend —
don't restart — the list in `quality-audits/chapter-09-audit.md`.

Citation/Ollama re-verification discipline: do not assume Chapter 8's
five citations are still live — re-fetch and re-read anything reused,
and treat all-new sources as the default. Chapter 8's own session found
two of five originally planned citations needed correction during live
verification (a stale redirect with no relevant content, and a page that
returned no fetchable body text) — a stricter outcome than Chapter 7's
own clean session, disclosed honestly as that session's own result;
do not assume Chapter 9's own session will be equally clean OR equally
churny. Re-check Ollama's `/api/tags` and `/api/chat` fresh at the start
of the session, even though Chapters 4-8 all got two consecutive
first-attempt successes — Chapter 3 already showed a successful warm
call can still be followed by a later timeout within the same session,
so treat the endpoint as intermittently slow/hanging by default, budget
for retries throughout the session, not just at the start, and keep
timeouts generous (120s+) throughout.

Registration-staleness check reminders: once Chapter 9's `lesson.html`
exists, update `assets/chapters-data.js` (add its `path`), the root
`index.html` (`hero-stats` counts — it should read "9 of 13 chapters
live"; "4 of 6 modules complete" stays as-is, since Module 5 also needs
Chapters 10-11 — and the "All Chapters" intro paragraph), and
`docs/curriculum/index.html` (its own chapter-card status, lede
paragraph, and Module 5's feature card changed from its current state to
"In Progress") in the same session — these four locations drifted stale
in multiple sibling courses' own build histories when a chapter shipped
without updating all four at once.

Local validation, done at the end of every session:

```
$ bash scripts/local_check.sh
```

Passed clean at the end of this session (Chapter 8) — folder
structure, placeholder-text scan, Python syntax, every `solution.py`
executed for real, JS syntax and chapter-path validation, secret scan.
See this session's own commit message / `AI_HANDOFF.md` for the exact
result recorded.
