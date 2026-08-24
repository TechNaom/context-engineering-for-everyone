# Chapter 13 Quality Audit: Capstone: Designing a Context Engineering System

Session summary: this session built Chapter 13 in full — `lesson.html`,
exercises (`README.md`, `starter.py`, `solution.py`, `index.html`),
practice bank (`README.md`, `starter.py`, `solution.py`, `index.html`),
`quiz.html`, `interview-questions.md`/`.html`, and the L4 Architecture
Challenge capstone project (`project/README.md`,
`project/DESIGN_DOCUMENT_TEMPLATE.md`, `project/self_check.py`,
`project/solution.py`, `project/solution/SOLUTION_DESIGN_DOCUMENT.md`,
`project/RUBRIC.md`, `project/index.html`) — closing Module 6 and the
entire 13-chapter, 6-module course. It also runs a full course-completion
registration pass (`assets/chapters-data.js`, root `index.html`,
`docs/curriculum/index.html`, `README.md`), extends the running
fictional-org exclusion list, re-verifies all three sibling-course
boundaries fresh, and fetches and reads two new external sources live
this session.

## Honest self-critique

**What's strong:**

- The lesson does not teach a twelfth recipe — it composes all eleven
  from Chapters 1-12 against one realistic, fully worked incident (a
  highway closure forcing DispatchMind, Castellan Fleet Logistics'
  dispatch copilot, to replan a route, check HOS compliance, and decide
  whether to notify a customer), with every step's own real, executed
  Python output quoted verbatim — 10 pipeline steps plus 2 live Ollama
  captures, 12 real code/output blocks total.
- Composing all eleven recipes on one scenario, rather than showing each
  in isolation, surfaced two genuine findings neither the lesson author
  nor any single prior chapter's own recipe would have found alone: (1)
  Chapter 3's pin and Chapter 4's staleness check reach two different,
  both-correct freshness verdicts on the same underlying waiver fact,
  because they check different properties of it; (2) Chapter 12's own
  deterministic evaluation gate passed the final bundle at 100%
  completeness, yet a live LLM completeness check (Live Capture 2) found
  the required-fact list itself had a real gap — it checked for
  supporting reasoning about compliance, not the resolved `compliant`
  value stated as literal text. Both findings are disclosed as genuine
  discoveries, not engineered outcomes, and both extend Chapter 12's own
  precedent (a gate passing is a necessary floor, not a guarantee) one
  layer further at capstone scale.
- Live Capture 1 (a starvation/contamination probe on the Customer-Comms
  Agent's own isolated bundle) produced a real, disclosed imperfection —
  the model echoed the literal field name `[eta_delay_min]` instead of
  substituting 95 — while the isolation boundary itself held perfectly
  (zero HOS/waiver leakage). This is used directly to argue isolation
  correctness and generation quality are separable failure surfaces, a
  genuine finding from the capture, not asserted without evidence.
- The capstone project follows `ai-engineering-for-everyone` Chapter 13's
  own established L4 artifact-shape precedent exactly (see "L4
  artifact-shape decision" below): a business-problem-only README, a
  design-document template with real, mechanically-checkable arithmetic
  (a Context Budget Ledger per component that must actually fit its own
  hard limit, and an evaluation-gate spec with in-range thresholds), a
  `self_check.py` that verifies structure and arithmetic only, and a
  six-criteria, 30-point, 80%-passing-bar `RUBRIC.md` for the qualitative
  remainder — `solution.py` confirms the reference document scores a
  full structural pass.
- The two components chosen for the capstone problem (DispatchMind, the
  same real-time/multi-agent/user-facing system the lesson walks
  through in miniature, and ComplianceLedger, a newly-introduced
  asynchronous/single-agent/internal system at the same fictional
  company) are deliberately shaped to force genuinely different recipe
  depths across all eleven recipes, not just a relabeled repeat of the
  lesson's own scenario — mirrored directly from
  `ai-engineering-for-everyone`'s own CommuteNote/MaintainNote split,
  adapted to this course's own recipe stack instead of that course's
  own cost/latency/reliability/deployment/observability stack.

**Honest gaps:**

- As in every prior chapter, no graded `solution.py` in this chapter's
  own `exercises/`, `practice/`, or `project/` depends on a live model
  call — every ledger, classification, isolation-boundary, and
  evaluation-gate arithmetic check is deterministic, hand-computed data,
  for the same 20-second-timeout reason documented since Chapter 3. The
  two live Ollama captures embedded in the lesson are illustrative and
  disclosed, not something any graded script requires to pass.
- This chapter's own exercises (5 tasks) and practice bank (4 scenarios)
  are meaningfully shorter than a typical chapter's own eight-task/
  eight-scenario format, a deliberate scope decision (see "Exercises and
  practice bank scope decision" below) rather than an oversight — the
  bulk of this chapter's own graded work is the L4 capstone project, per
  this chapter's own heavier-project judgment call the task brief
  explicitly allowed.
- This chapter omits `ai-paired.html`, present in six of the eleven prior
  chapters (5, 7, 9, 10, 11, 12) but absent in five (1-4, 6, 8) — not
  every chapter has shipped one, and given this chapter's own heavier
  project component, an AI-pairing exercise on top of the exercises,
  practice bank, and capstone project was judged as diminishing rather
  than adding value. Flagged explicitly here rather than silently
  omitted.
- The capstone's own `self_check.py` checks Context Budget Ledger and
  evaluation-gate arithmetic mechanically, but — like every prior
  chapter's own automated harness — cannot check whether a learner's
  eleven-recipe qualitative reasoning (the actual bulk of the
  deliverable) is any good; that remains `RUBRIC.md`'s job and a human
  reader's, the same limitation `ai-engineering-for-everyone` Chapter
  13's own audit disclosed for its own composition-depths arithmetic.

## L4 artifact-shape decision

Following `ai-engineering-for-everyone` Chapter 13's own precedent
directly (re-read fresh this session at
`/home/dell/projects/ai-engineering-for-everyone/chapters/chapter-13-capstone-architecting-and-shipping-a-production-llm-system/project/`):
a business problem with no provided pipeline and no scaffold has no
fixture data for a `starter.py`/`solution.py` pair to grade in the way
every prior chapter's own exercises and practice bank do. The actual
deliverable — for both `ai-engineering-for-everyone`'s own capstone and
this one — is a written design document, closer in shape to a real
Architecture Decision Record (see the lesson's own Sources section,
citation 1) than a filled-in exercise file. This chapter's own
`self_check.py` therefore checks only what's genuinely mechanical: 21
required section headers present, and two Python-literal blocks per
component (a Context Budget Ledger that must actually fit its own
declared hard limit, with Line 5 reserved, and an evaluation-gate spec
with in-range thresholds) — reusing Chapter 1-2's own ledger-validation
logic and Chapter 12's own evaluation-gate shape directly rather than
inventing a new composition-depth formalism the way
`ai-engineering-for-everyone`'s own capstone did. This was a deliberate
choice: this chapter's own framing states directly, in the lesson's own
"What This Chapter Owns" section, that Chapter 13 introduces no twelfth
recipe — inventing a new mechanically-checkable formalism for the
project would have contradicted that framing, so the project's own
checkable arithmetic reuses exactly the two recipes (the ledger and the
evaluation gate) that were already mechanically checkable in earlier
chapters.

## Exercises and practice bank scope decision

The task brief for this chapter explicitly anticipated it "may
reasonably have a heavier project/capstone component than a regular
chapter's exercises/practice split." This session applied that
judgment: 5 exercise tasks (recipe-matching judgment, Context Budget
Ledger arithmetic, short-term memory classification, isolation-boundary
judgment, evaluation-gate arithmetic) and 4 practice scenarios (budget
worst-case validation, compression fidelity, source authority
resolution, tool-result curation), both roughly half the typical
eight-task/eight-scenario size used by Chapters 1-12, with the L4
capstone project carrying the chapter's own primary graded weight. Both
the exercises and practice bank use a second and third Castellan Fleet
Logistics scenario respectively (a cold-chain reefer-mechanical incident
for exercises, four independent fresh-load vignettes for practice),
deliberately distinct from the lesson's own I-80 closure hook and from
each other, following the same "second scenario, not the lesson's own"
discipline every prior chapter's own exercises/practice split has used.

## Re-verified sibling-course boundaries

All three re-checked directly against their own current curriculum maps
this session, not assumed unchanged from Chapter 12's own
re-confirmation, with a first fully direct check specifically for
architecture-level system-design overlap (this chapter's own subject
makes it directly relevant for the first time, the same way Chapter 12's
session gave `ai-engineering-for-everyone`'s Module 3 its first direct
evaluation-overlap check):

- `/home/dell/projects/ai-engineering-for-everyone/docs/curriculum/CURRICULUM_MAP.md`
  — its own Module 7-equivalent capstone (Chapter 13, "Architecting and
  Shipping a Production LLM System") owns the plain-prompt/RAG/
  fine-tune/agent architecture decision and the cost/latency/
  reliability/deployment/observability composition around it — assumed
  as a given input by this chapter, not re-taught. Its own forward
  cross-link list names a future `AI Architecture for Everyone`, not yet
  built, confirmed still unbuilt this session.
- `/home/dell/projects/mcp-for-everyone/docs/curriculum/CURRICULUM_MAP.md`
  — re-read fresh. Its own Module 7 capstone ("Enterprise MCP Platform
  Architecture," Chapter 13, L4 Architecture Challenge: "Secure,
  multi-tenant MCP platform") owns protocol-level, multi-tenant server
  design — not which content belongs in a given call's context.
- `/home/dell/projects/ai-coding-agents-for-everyone/docs/curriculum/CURRICULUM_MAP.md`
  — re-read fresh. Its own Module 6 capstone ("Design an Agent Workflow
  for a Real Team," Chapter 13, L4 Architecture Challenge: "Design an
  agentic CI workflow ... business problem only") owns one coding
  agent's own workflow design for one codebase, not cross-domain context
  composition.

No chapter in any of the three siblings' own final capstones overlaps
with "compose budget, memory, compression, assembly, retrieval,
tool/agent, and evaluation recipes into one context engineering system"
— this chapter's own, unclaimed territory, confirmed directly rather
than assumed from the course's own original positioning alone.

## New-org exclusion list

Read `quality-audits/chapter-12-audit.md`'s full running list (Chapters
1-11's combined 116 orgs plus Chapter 12's 10 new orgs — 126 total)
before naming a new fictional org for this chapter, and cross-checked
the single candidate root against a live grep of this repo's own
tracked files and `ai-engineering-for-everyone`'s own tracked files
(`/home/dell/projects/ai-engineering-for-everyone/quality-audits/chapter-13-audit.md`
and every other `quality-audits/*.md` in that repo, present locally as
in every prior session), including a targeted check for "Emberlyn" and
"Harrowgate" (`ai-engineering-for-everyone` Chapter 13's own project org
and this repo's own Chapter 1 org, respectively) before settling on the
final candidate.

**1 new fictional org used this session**, extending Chapters 1-12's
combined 126-org list to **127 total in this repo**:

- **Castellan Fleet Logistics** (lesson hook and capstone project; long-haul
  trucking company; products DispatchMind and, introduced fresh in the
  capstone project only, ComplianceLedger).

Confirming the task brief's own prediction: this chapter needed
meaningfully fewer new orgs than a typical chapter's usual 10, because
its own format is one integrated system design (the lesson's worked
example plus the capstone project, both set at the same fictional
company with two different components) rather than many short,
independent scenarios. The exercises and practice bank both reuse
Castellan Fleet Logistics with fresh load/case numbers — the same
"fresh case at an already-introduced organization" pattern
`ai-engineering-for-everyone`'s own module-assessment folders and this
repo's own Chapter 12 assessment groundwork both used — rather than
introducing additional new organizations for each. No collision found
against either exclusion list's distinctive roots.

Future work extending this repository beyond its original 13-chapter
scope (see `PROJECT_STATE.md`'s own updated "Next Recommended Task"
section) should extend this combined list (Chapters 1-12's 126 orgs plus
this session's 1, for **127 total in this repo**), not restart it.

## Source verification, done honestly

Two externally-fetched sources this session, both fetched and read live,
not recalled from training data or reused from a prior chapter's own
citation set:

1. Nygard, "Documenting Architecture Decisions" —
   `cognitect.com/blog/2011/11/15/documenting-architecture-decisions`.
   Fetched live and read this session for the first time in this
   repository. Grounds the capstone's own `DESIGN_DOCUMENT_TEMPLATE.md`
   structure directly: a short, structured document (context, decision,
   status, consequences) that preserves the motivation behind a
   decision, not only its outcome.
2. Anthropic, "Building Effective Agents" —
   `anthropic.com/engineering/building-effective-agents`. Fetched live
   and read this session for the first time in this repository. Grounds
   Section 6's own restraint argument ("add complexity only when it
   demonstrably improves outcomes") and the capstone rubric's own
   "mechanical copy" and treatment-depth criteria — DispatchMind's own
   three-sub-agent complexity is justified by real, independently-
   motivated needs, and ComplianceLedger's own single-agent design in
   the same business problem is the deliberate counter-example proving
   restraint matters as much as capability.

Both sources are new to this repository. Neither was reused from a
prior chapter's own citation set — this chapter's own subject (composing
recipes into a defended system, not any single recipe's own mechanics)
called for genuinely different grounding than any earlier chapter's own
citations provided.

## Ollama re-verification, done honestly

`curl http://localhost:11434/api/tags` responded normally at the start
of this session and confirmed the same installed model as every prior
chapter (`llama3.2:latest`). Two live `POST /api/chat` calls were made
this session, both embedded in the lesson as Live Captures 1 and 2. The
first (a starvation/contamination probe drafting a customer message from
the isolated Customer-Comms Agent bundle) ran 100.3 seconds cold; the
second (a literal-scan completeness check on the final DispatchMind
bundle) ran 47.5 seconds warm. Both were comfortably inside this
course's standing 120-second-plus timeout guidance, and neither required
a retry — a cleaner session than Chapter 12's own (whose first call
exceeded a 2-minute tool timeout before returning at all). Both captures
are quoted verbatim in the lesson including their own imperfections (the
unsubstituted `[eta_delay_min]` placeholder in Capture 1, and the
inferential "YES" on item 5 in Capture 2 despite an explicit
literal-scan-only instruction) rather than edited for a cleaner
narrative — the same disclosure discipline every chapter since Chapter 3
has held. No graded `solution.py` anywhere in this chapter's own
`exercises/`, `practice/`, or `project/` depends on a live call.

## Registration — full course-completion pass

Since this is the final chapter, this session ran a full
course-completion registration pass rather than the routine
per-chapter update:

- `assets/chapters-data.js` — added Chapter 13's entry (`path` to
  `lesson.html`) under Module 6, and updated the file's own top-of-file
  comment describing build status.
- Root `index.html` — `hero-stats` updated to "13 of 13 chapters live"
  and "6 of 6 modules complete"; the `hero-eyebrow` ("Free · in progress
  · open-source by default") flipped to remove the stale "in progress"
  language; the "All Chapters" section's own `section-kicker` ("Learning
  path, in progress") and intro paragraph updated to describe the course
  as complete; the intro paragraph's own closing sentences updated to
  describe Chapter 13 as live and the course as finished rather than
  "planned and scaffolded."
- `docs/curriculum/index.html` — Chapter 13's own chapter-card flipped
  from "Planned" to "Live" with a working link to `lesson.html`; Module
  6's own feature card flipped from "In Progress" to "Complete"; the
  page's own closing lede paragraph updated to describe Chapter 13 as
  live and the course as complete rather than "not yet built."
- `docs/curriculum/CURRICULUM_MAP.md` — re-checked for inline status
  language this session, as prior sessions also found none; still none
  present (the file is a pure content map, no "in progress"/"planned"
  markers of its own) — no edit needed, confirmed rather than assumed.
- `README.md` — the stale "Chapter 1 of 13 is live" status line (never
  updated across any of the prior twelve sessions) corrected to describe
  the full, complete course.

Grepped `index.html` and `docs/curriculum/index.html` for both "of 13"
and "In Progress" after editing to confirm no stale occurrence remained
anywhere in either file.

## Module 5's own "Assessment" line, resolved retroactively

`docs/curriculum/CURRICULUM_MAP.md`'s own Module 5 entry names an
"applied agentic-context design exercise" as its own Assessment line.
Chapter 9's own session (see `quality-audits/chapter-09-audit.md`)
resolved Module 5's **Labs** — folding both of Module 5's own labs (the
Chapter 9 tool-call miniature and the Chapter 10 multi-step/multi-agent
pipeline lab) into the Chapter 13 capstone — but no session through
Chapter 12's own left a matching resolution for Module 5's own
**Assessment** line specifically; grepping all three of
`quality-audits/chapter-09-audit.md`, `chapter-10-audit.md`, and
`chapter-11-audit.md` for "assessment" this session found zero
mentions. This session resolves it explicitly, rather than leaving it
open a fourth time: this chapter's own capstone project requires a real,
graded "Tool context and multi-agent/isolation plan" (Ch. 9-11) for both
components, applying exactly Module 5's own three recipes under real
constraints, self-checked and rubric-graded — satisfying Module 5's own
"applied agentic-context design exercise" assessment line the same way
Chapter 8's own L3 project was already confirmed (in
`quality-audits/chapter-07-audit.md`) to satisfy Module 4's own
assessment line. No separate `assessments/module-assessments/` artifact
for Module 5 is needed as a result. Recorded here so a future
maintenance pass doesn't need to re-derive this.

## Validation

`bash scripts/local_check.sh` run at the end of this session — see
`PROJECT_STATE.md` and the commit message for the exact recorded result.
