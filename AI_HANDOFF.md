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
Short version: this is the course's **ninth session**. Session 1 built
Discovery, the curriculum map, the full repository scaffold, and
Chapter 1 ("The Context Budget"). Session 2 built Chapter 2
("Designing Context Window Budgets"), completing Module 1 in full.
Session 3 built Chapter 3 ("Short-Term Conversational Memory"), opening
Module 2. Session 4 built Chapter 4 ("Long-Term and Persistent Memory
Systems"), closing Module 2 in full. Session 5 built Chapter 5
("Context Compression and Summarization"), opening Module 3. Session 6
built Chapter 6 ("Avoiding Lost-in-the-Middle"), closing Module 3 in
full and shipping Module 3's single joint project. Session 7 built
Chapter 7 ("Multi-Source Context Assembly"), opening Module 4, shipping
no project of its own. Session 8 built Chapter 8 ("Retrieval
Integration: From Ranked Results to Context"), closing Module 4 in full
and shipping Module 4's single project — the curriculum map's own
literal L3 Independent tier. Session 9 built Chapter 9 ("Context
Engineering for Tool Use"), opening Module 5, shipping no project of its
own per the curriculum map's own project ladder. Session 10 built
Chapter 10 ("Context Engineering for Multi-Agent Systems"), continuing
Module 5, also shipping no project of its own. Chapters 11-13 exist
only as `.gitkeep`'d directories, not yet built.

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
- **Chapter 4 ("Long-Term and Persistent Memory Systems") is built and
  live**, closing Module 2 in full. See
  `quality-audits/chapter-04-audit.md`. Uses Chapter 3's short-term
  policy as a lens: Line 3's own eviction/compression mechanics are a
  given, not re-derived, and this chapter's own job is what a system
  writes to durable storage once a session ends, and the real policy
  that decides what gets retrieved back into Line 4 for a given turn —
  including the one genuinely new mechanic short-term memory never
  needed: staleness handling (a stored fact can become false, not just
  old). This chapter also finally resolved the L1/L2 project-ladder
  question Chapters 2-3 left open twice, shipping the curriculum map's
  literal L2 Assisted project once, solo, closing the module — see
  "Open Decisions" in `PROJECT_STATE.md` for the confirmed convention
  going forward (one project per module, at the ladder's own stated
  tier).
- **Chapter 5 ("Context Compression and Summarization") is built and
  live**, opening Module 3. See `quality-audits/chapter-05-audit.md`.
  Uses Chapters 1-4 as a lens: the token budget, the compression
  trigger, the pin/summary/window shape, and the long-term write/
  retrieval policy are all given inputs, not re-derived. This chapter's
  own job is the one thing Chapter 3's own recipe named ("compress,
  don't truncate") but deliberately left unengineered — the real
  mechanics a compression call uses to decide what survives when
  content no longer fits its budget: a six-step Compression Fidelity
  Recipe (identify what's already exempt, extract load-bearing
  candidates before compressing, choose a strategy matched to content
  type, bound the target explicitly, run the compression, validate
  fidelity before shipping). **Chapter 5 ships no project of its own —
  by design, not by omission.** Per the now-confirmed
  one-project-per-module convention, Module 3's single project ships
  once, solo, at the end of Chapter 6; `interview-questions.html` says
  so explicitly.
- **Chapter 6 ("Avoiding Lost-in-the-Middle") is built and live**,
  closing Module 3 in full. See `quality-audits/chapter-06-audit.md`.
  Uses Chapters 1-5 as a lens: the budget, pin/summary/window shape,
  long-term recall policy, and fidelity-checked compression pipeline
  are all given inputs, not re-derived. This chapter's own job is the
  positional question every prior chapter assumed out of scope: given a
  final, assembled set of already-correctly-included content, *where*
  it sits inside the window measurably changes whether the model
  actually uses it — a five-step Context Ordering Recipe (rank by
  load-bearing weight, reserve the anchor positions for the
  highest-weight content, reorder the middle deliberately, put the
  query near the end closest to generation, test position directly with
  an explicit probe). **This session also re-verified the "Lost in the
  Middle" (Liu et al., 2023) citation** flagged since Chapter 1 —
  fetched two newer sources live (Hsieh et al. 2024's "Found in the
  Middle," Chroma's 2025 "Context Rot" report) and stated an honest
  conclusion in the lesson itself: the core claim still holds on
  current frontier models, but its exact shape is model- and
  length-specific with a mechanistic, partially correctable cause, not
  a fixed universal curve. **Ships Module 3's single guided project**
  this session (Brackholt County Court Records Office/ArchiveLine),
  drawing on both Chapter 5 (compression) and Chapter 6 (ordering)
  together — disclosed honestly as sitting between the curriculum map's
  own L2 and L3 tiers, since the map's numbered ladder doesn't itself
  assign a tier to Module 3 (full reasoning in the quality audit).
- **Chapter 7 ("Multi-Source Context Assembly") is built and live**,
  opening Module 4. See `quality-audits/chapter-07-audit.md`. Uses
  Chapters 1-6 as a lens: the budget, memory policies, the Compression
  Fidelity Recipe, and the Context Ordering Recipe are all given inputs,
  not re-derived. This chapter's own job is the question every prior
  chapter deferred: which sources belong in a window at all, and how do
  several different sources — retrieved documents, live tool output,
  conversation history, system instructions — get combined into one
  coherent window without contradicting or crowding each other out,
  before Chapter 6's own ordering recipe ever runs — a six-step Source
  Assembly Recipe (inventory every candidate source, assign each source
  type an authority rank per request type, detect overlapping and
  contradicting claims before assembly, resolve or explicitly surface
  each contradiction found, deduplicate restated content, hand the
  resolved set to Chapter 6's own ordering recipe). **This session's own
  build was interrupted partway through by a connection error** (after
  `lesson.html`, `quiz.html`, and part of `exercises/` were already on
  disk) and resumed cleanly — everything already on disk was verified
  correct before continuing, not restarted from scratch, and this is
  documented explicitly in `quality-audits/chapter-07-audit.md`. **This
  chapter ships no project of its own — by design.** Per the
  one-project-per-module convention, Module 4's single project is
  planned for the end of Chapter 8, once retrieval integration is also
  in place; unlike Module 3's own tier gap, Module 4's project lands
  cleanly on the curriculum map's own L3 Independent tier already
  assigned to Chapter 8 (full reasoning in the quality audit).
- **Chapter 8 ("Retrieval Integration: From Ranked Results to Context")
  is built and live**, closing Module 4 in full. See
  `quality-audits/chapter-08-audit.md`. Uses Chapters 1-7 as a lens: the
  budget, memory policies, the Compression Fidelity Recipe, the Context
  Ordering Recipe, and the Source Assembly Recipe are all given inputs,
  not re-derived. This chapter's own job is the handoff Chapter 7
  deliberately left open: turning a retriever's own raw ranked, scored
  chunk list into one well-formed source before it ever reaches Chapter
  7's own inventory step — a six-step Retrieval Integration Recipe
  (apply a relevance floor before selecting anything, fit surviving
  chunks to budget at a chunk boundary rather than truncating
  mid-sentence, preserve each chunk's provenance, stitch adjacent
  same-document chunks back together, handle a low-confidence or empty
  result set explicitly, hand the resolved bundle to Chapter 7's own
  Source Assembly Recipe as one source). **This session shipped Module
  4's single project**, closing the module — Quartzfield Regional Public
  Defender Consortium's BriefLine, drawing on both Chapter 7 (source
  assembly) and Chapter 8 (retrieval integration) together, landing on
  the curriculum map's own literal L3 Independent tier with no scaffold
  beyond the given spec, unlike Module 3's own tier-gap workaround. This
  session also caught and corrected two of five originally planned
  citations during live verification (a stale LangChain redirect with no
  relevant content, and an AWS Bedrock page that returned no fetchable
  body text) rather than leaving them uncorrected — a stricter citation
  outcome than Chapter 7's own clean session, disclosed honestly.
- **Chapter 9 ("Context Engineering for Tool Use") is built and live**,
  opening Module 5. See `quality-audits/chapter-09-audit.md`. Uses
  Chapters 1-8 as a lens: the budget, memory policies, the Compression
  Fidelity Recipe, the Context Ordering Recipe, the Source Assembly
  Recipe, and the Retrieval Integration Recipe are all given inputs, not
  re-derived. This chapter's own job is the first genuinely new content
  shape the course has engineered: a tool's own definition, a token cost
  paid on every call whether or not the tool executes, and a tool's own
  result, structured rather than prose, with its own truncation-safety
  and staleness rules — a six-step Tool Context Recipe (scope tool
  definitions to the request type, budget each included schema
  explicitly, curate a tool's raw result before it enters context, fit
  the curated result to budget at a field boundary rather than
  truncating mid-object, budget and evict tool-call history across a
  multi-step loop, hand the resolved typed result to Chapter 7's own
  Source Assembly Recipe). **This session picked up a `lesson.html`
  already written in full by a prior, interrupted session** — every
  claim, citation, and worked-math number in it was independently
  re-verified this session (all 4 external citations re-fetched live
  with zero corrections needed, and the `mcp-for-everyone` boundary
  re-confirmed directly against that repo's own current curriculum map)
  before this session built everything else the chapter still needed:
  `exercises/`, `practice/`, `interview-questions.md`/`.html`,
  `quiz.html`, the quality audit, all four registration locations, and
  the commit itself. **This session also finally resolved a
  previously-open Module 5 project-ladder question**: `docs/curriculum/
  CURRICULUM_MAP.md`'s own "Projects" section assigns no numbered tier
  to Module 5 at all, so Chapters 9, 10, and 11 each ship no project of
  their own — Module 5's own two labs fold directly into the Chapter 13
  capstone's own system design instead, confirmed explicitly rather than
  assumed.

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
  forever after." `/api/tags` has responded normally in all seven
  sessions with `llama3.2:latest` installed. Session 4 got two
  consecutive first-attempt successes (74.4s cold, 21.8s warm), with no
  retries needed. Session 5 also got two consecutive first-attempt
  successes (64s cold, 8s warm). Session 6 also got two consecutive
  first-attempt successes (113.7s cold, 5.1s warm). Session 7 got two
  consecutive first-attempt successes before its own session-interrupting
  connection error (109s cold, 5.1s warm — the pair used for the
  chapter's own substantive live capture), then two more consecutive
  first-attempt successes after resuming (64.8s cold, 10.9s warm — a
  supplementary connectivity re-check) — reported honestly as each
  session's own result, not evidence the intermittent pattern is
  resolved. Session 8 also got two consecutive first-attempt successes
  (54.1s cold with ~19.6s of that as load time, 69.9s on a second call
  whose own reported load time was only ~0.6s). Session 9 picked up a
  `lesson.html` already written by a prior, interrupted session,
  including its own two real `/api/chat` captures (65.7s cold, 22.8s
  warm) — re-verified as internally consistent rather than re-run; this
  session's own fresh check confirmed `/api/tags` still responds
  normally with the same installed model. Re-check and disclose honestly
  every session, budgeting for retries throughout the session (not just
  at the start), with generous timeouts (120s+) even after an earlier
  call has already succeeded.
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
  opening Module 2; Session 4 built Chapter 4 only, closing Module 2;
  Session 5 built Chapter 5 only, opening Module 3; Session 6 built
  Chapter 6 only, closing Module 3 in full; Session 7 built Chapter 7
  only, opening Module 4; Session 8 built Chapter 8 only, closing Module
  4 in full; Session 9 built Chapter 9 only, opening Module 5 —
  matching exactly how `ai-engineering-for-everyone` itself progressed.
  (Session 7's own build was interrupted partway through by a connection
  error and resumed within the same logical session, verifying
  everything already on disk before continuing — this is not an
  exception to the one-chapter-at-a-time discipline, just a resumed
  single chapter. Session 9's own build similarly picked up a
  `lesson.html` a *prior*, separately-interrupted session had already
  written in full before this session began — also not an exception,
  since verifying everything already on disk before continuing is
  exactly the same discipline Session 7 applied.)
- **Check every fictional org against the running exclusion list before
  naming a new one** — see `quality-audits/chapter-09-audit.md` for the
  full, current list (96 orgs across Chapters 1-9 so far, checked
  against `ai-engineering-for-everyone`'s own full compiled list with
  zero collision found) and extend it (don't restart it) for every new
  chapter. Each new chapter's audit should reproduce the full list plus
  its own new orgs, so the next session only ever needs to read the
  latest one.
- **One project per module, at the project ladder's own stated tier
  where the ladder assigns one — otherwise labeled honestly as a
  module-level project with no numbered tier.** Chapters 2-3 each
  shipped a second, module-internal L1-tier project, logging the tension
  with the curriculum map's own ladder as open both times; Chapter 4's
  session finally resolved it by shipping the curriculum map's literal
  "L2 Assisted" project once, solo, closing Module 2, and confirmed this
  as the convention going forward. Chapter 5's session applied this
  convention as intended — no project this chapter, confirmed explicitly
  rather than silently omitted. Chapter 6's session shipped Module 3's
  single project as committed, and also found the curriculum map's own
  numbered ladder does not assign any tier to Module 3 at all (it jumps
  from L2 after Ch. 4 to L3 after Ch. 8) — resolved by labeling it
  "Module 3 Project," not an invented numbered tier; see
  `quality-audits/chapter-06-audit.md` for the full reasoning, and apply
  the same honest-labeling approach if a future module's project ever
  falls in a similar gap. Chapter 7's session shipped no project of its
  own, confirmed explicitly (not silently omitted), and found Module 4's
  own project lands cleanly on the curriculum map's own **L3
  Independent** tier already assigned to Chapter 8 by the numbered
  ladder — unlike Module 3's gap, no honest-labeling workaround is
  needed here. **Chapter 8's session shipped this L3 project**,
  Quartzfield Regional Public Defender Consortium's BriefLine, drawing
  on both Chapter 7 (source assembly) and Chapter 8 (retrieval
  integration) together, closing Module 4, implemented with no scaffold
  beyond the given spec and data per the L3 tier's own definition. See
  `quality-audits/chapter-08-audit.md` for the full reasoning.
  **RESOLVED in Chapter 9's own session: Module 5 (Chapters 9-11) ships
  no project at all.** `CURRICULUM_MAP.md`'s own "Projects" section was
  read directly and its numbered ladder (L1 after Ch. 2, L2 after Ch. 4,
  L3 after Ch. 8, L4 the Ch. 13 capstone) assigns no tier to Module 5 —
  a different situation from Module 3's own tier-gap (which still got an
  honestly-labeled module-level project). Module 5's own two labs fold
  directly into the Chapter 13 capstone's own system design instead; see
  `quality-audits/chapter-09-audit.md` for the full reasoning. Chapters
  10 and 11 should not ship a project either, absent a future revision of
  the curriculum map.
- **State explicitly, in each new chapter's own lesson text, what it is
  NOT re-teaching** from `rag-for-everyone`, `mcp-for-everyone`, or
  `ai-engineering-for-everyone` Chapter 3 wherever its subject sits
  close to theirs — this is the discipline that keeps this course from
  drifting into duplicating a sibling course over many sessions, and
  Chapter 1 modeled it directly in its "Why This Course Exists"
  section.

## Current task: Chapter 11 — "Context Isolation and Scoping"

Closes Module 5 (Context Engineering for Agentic Systems), Chapters
9-11 — Chapter 10 is now complete. See `PROJECT_STATE.md`'s "Next
Recommended Task" section for the full handoff detail: what not to
re-derive from Chapters 1-10 (the budget ledger, memory policies, the
Compression Fidelity Recipe, the Context Ordering Recipe, the Source
Assembly Recipe, the Retrieval Integration Recipe, the Tool Context
Recipe, and the Pipeline/Multi-Agent Context Recipe are all given
inputs, not re-taught fresh) — Chapter 11's own new job is the
deliberate flip side of Chapter 10's own recipe: Chapter 10 treated
every case of a step or sub-agent not getting some piece of context as
either a bug (an unscoped budget overflow) or an oversight (a stale
finding never evicted between units of work). Chapter 11 asks when
withholding context between steps or agents is the *correct* design
choice on purpose — not a scoping bug Chapter 10's own recipe would flag
— and where that kind of intentional isolation itself breaks down or
gets misapplied (a sub-agent withheld information it genuinely needed,
or an isolation boundary drawn for one good reason quietly becoming an
excuse to under-inform every downstream step by default). Re-confirm
both the `mcp-for-everyone` boundary (re-confirmed unchanged again in
Chapter 10's own session) and the `ai-coding-agents-for-everyone`
boundary (given its first fully direct verification in Chapter 10's own
session, per `PROJECT_STATE.md`'s prior explicit instruction) fresh this
session rather than assuming either is now permanently settled — the
same direct-verification discipline every chapter since Chapter 9 has
applied. Also check: the new-org exclusion list (106 orgs across
Chapters 1-10 so far, in `quality-audits/chapter-10-audit.md`, which
also now includes a live-grep cross-check against
`ai-engineering-for-everyone`'s own compiled list, present locally in
this sandbox for the first time as of Chapter 10's own session),
citation/Ollama re-verification discipline (Chapter 10's own session
found all 3 citations clean with zero corrections needed; the Ollama
hang remains intermittent regardless — budget for retries throughout the
session, even though Chapter 10's own session got six consecutive
first-attempt successes), **no chapter project is due at the end of
Chapter 11** (Chapter 9's own session already resolved this for all of
Module 5, re-confirmed again in Chapter 10's own session — re-verify the
curriculum map still says so, but do not treat it as newly open), and
the registration-staleness locations to update in the same session once
Chapter 11's `lesson.html` exists (`assets/chapters-data.js`, root
`index.html`'s hero-stats — it should read "11 of 13 chapters live" AND
"5 of 6 modules complete" this time, since Chapter 11 is the one that
closes Module 5 — plus the intro paragraph, and
`docs/curriculum/index.html`'s chapter-card status and lede paragraph
AND Module 5's own feature card, which should finally flip from "In
Progress" to "Complete").

## Next task after that

Chapter 12 ("Evaluating Context Quality"), opening Module 6 (Evaluation
and Capstone) — not yet planned in detail beyond the curriculum map's
own module outcomes; a future session should read Chapter 11's own
quality audit before starting, not assume its scope from the curriculum
map alone. Module 6's own two chapters (12 and 13) map cleanly onto the
curriculum map's own project ladder differently from Module 5: Chapter
12 is expected to ship an applied context-evaluation exercise per the
map's own "Assessment" line for Module 6, and Chapter 13 is the Level 4
capstone itself — re-verify both against the curriculum map before
assuming either, the same way every resolved-but-re-checked convention
in this course works.

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
