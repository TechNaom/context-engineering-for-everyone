# Chapter 12 Quality Audit: Evaluating Context Quality

Session summary: this session built Chapter 12 in full — `lesson.html`,
exercises (`index.html`, `README.md`, `starter.py`, `solution.py`,
`ai-paired.html`), practice bank (`index.html`, `README.md`,
`starter.py`, `solution.py`), `quiz.html`, and `interview-questions.md`/
`.html` — opening Module 6 (Chapters 12-13). It also builds the Module 6
assessment groundwork the curriculum map's own "Assessment" line
requires (`assessments/module-assessments/module-6-context-evaluation-exercise/`),
extends the running fictional-org exclusion list, re-verifies all three
sibling-course boundaries fresh, and fetches and reads three new external
sources live this session.

## Honest self-critique

**What's strong:**

- The hook (Ternfield Regional Disability Benefits Review Office/
  ClaimLens) isolates a genuinely distinct failure mode from every prior
  chapter's own hook: it is the first chapter whose failure is not
  attributable to any single Chapter 1-11 recipe running incorrectly.
  Every per-step check those recipes define passes — correct budget,
  fresh source, no contradiction, correct retrieval, no isolation leak —
  and the bundle still produces a wrong outcome, because no chapter
  before this one was ever built to check the *finished* bundle as a
  single artifact. This is the deliberate structural point
  `PROJECT_STATE.md` asked this chapter to make, not a variation on any
  earlier chapter's own bug category.
- The Context Evaluation Recipe's six steps map directly onto three
  independently-grounded metrics from established practice, not concepts
  invented for this course: Step 2's completeness score mirrors RAGAS's
  own "context recall" definition, Step 3's noise ratio mirrors RAGAS's
  own "context precision" definition, and Step 4's positional audit
  applies the re-verified Lost-in-the-Middle finding (already
  established in Chapter 6) as a checkable evaluation criterion for the
  first time rather than only a design principle applied once at
  assembly time.
- Both live-capture attempts at the chapter's own two central failure
  modes are disclosed with full honesty, including a genuine, informative
  negative result: four separate attempts to reproduce a pure
  *positional* burial failure on llama3.2 all failed — the model
  correctly used the most recent, decisive fact every time regardless of
  where in the prompt it sat, at the context lengths these prompts
  actually reached. Rather than force a reproduction or quietly drop the
  positional axis, the chapter reports this directly and pivots its own
  live evidence to the more central completeness axis (which reproduced
  reliably on the first attempt), while keeping the positional check
  itself grounded in the peer-reviewed literature rather than this
  session's own live captures.
- The LLM-as-completeness-checker section (Live Captures 3-4) surfaces a
  second, independently valuable finding, not a clean success story: a
  reasoning-style question ("is this within the last 30 days") produced
  a false negative on a plainly-present fact twice in a row, while an
  identical underlying check phrased as a literal scan-and-quote
  instruction worked immediately. This directly reinforces Step 2's own
  design choice (a literal presence check, not an inferential one) with
  real evidence rather than asserting it as a design principle alone.
- The worked-math table makes the same point Chapter 11's own worked
  math made, one layer up: the before-fixes bundle sits comfortably
  inside its own token budget the entire time it fails the gate — none
  of this chapter's three failure modes (incompleteness, noise, buried
  position) are budget problems, a distinction this chapter states
  explicitly rather than leaving implicit.
- The Module 6 assessment groundwork lands in
  `assessments/module-assessments/module-6-context-evaluation-exercise/`,
  matching `ai-engineering-for-everyone`'s own directory convention
  (`README.md`, `RUBRIC.md`, `starter.py`, `solution.py`) rather than
  folding it into `chapters/chapter-12.../exercises/` or `practice/` — a
  deliberate choice discussed below.

**Honest gaps:**

- As in every prior chapter, no exercise, practice, or module-assessment
  `solution.py` depends on a live model call — every completeness,
  noise-ratio, and positional decision in the automated harnesses is
  deterministic, hand-computed data, for the same reason
  `local_check.sh` runs every `solution.py` under a 20-second timeout.
- This chapter's own completeness and noise-ratio checks (Step 2,
  Step 3, and every exercise/practice/module-assessment task built on
  them) are exercised as clean structural checks on hand-labeled `found`/
  `position`/`noise_tokens` data — real production systems face a harder
  problem this chapter doesn't fully solve: deciding, automatically and
  at scale, *whether* a given span of retrieved text actually satisfies
  a required fact (not just whether a hand-labeled flag says so), and
  *which* tokens in a real document count as "noise" versus legitimately
  relevant supporting material. The LLM-as-completeness-checker section
  gestures at one automatable answer and honestly reports its own
  brittleness (a reasoning-phrased question produced a false negative
  twice), but does not resolve the harder underlying problem of
  automatically labeling positions and noise spans in unstructured real
  text — flagged here the same way Chapter 9's own audit flagged fuzzier
  tool-result staleness rules, Chapter 10's flagged fuzzier unit-of-work
  boundaries, and Chapter 11's flagged fuzzier contamination detection as
  open problems each chapter's own automated harness simplifies away.
- The positional-audit bucket boundaries (front/middle/back, drawn at a
  fixed 15%/70%/15% split in this chapter's own code) are a reasonable,
  literature-consistent simplification, not a claim that Lost-in-the-Middle
  degradation follows a precise, universal threshold at any particular
  percentage — the underlying research describes a continuous U-shaped
  degradation curve, not a hard three-bucket step function, and this
  chapter's own live-testing session (four failed reproduction attempts)
  is itself evidence that the risk is probabilistic and context-length-
  dependent rather than deterministic at any fixed position.

## Module 6 assessment groundwork decision

`docs/curriculum/CURRICULUM_MAP.md`'s own Module 6 "Assessment" line
reads "context-evaluation exercise (Ch. 12) + capstone rubric (Ch. 13,
architecture challenge, Level 4)" — explicitly two separate deliverables,
one attributed to each chapter, unlike `ai-engineering-for-everyone`'s
own Module 4/Module 5 assessments, which were each a single combined
review spanning two chapters, built once at the *later* chapter's own
session. Because Module 6's own two pieces are attributed to different
chapters rather than combined into one review, this session built only
Chapter 12's own half now
(`assessments/module-assessments/module-6-context-evaluation-exercise/`)
rather than waiting for Chapter 13 or inventing a combined-review
structure the curriculum map doesn't actually describe. This groundwork
deliberately does not live inside `chapters/chapter-12.../exercises/` or
`practice/`, both of which already exist in full and cover this
chapter's own eight-task and eight-scenario formats respectively — the
module-assessments directory is reserved, per
`ai-engineering-for-everyone`'s own established convention, for a single
integrated exercise with its own `RUBRIC.md`, distinct in format and
purpose from either of Chapter 12's own per-chapter deliverables. Chapter
13's own capstone rubric, covering the L4 architecture challenge, is
expected to land in `assessments/architecture-challenges/` — currently
empty in this repository — when that chapter ships.

## Re-verified sibling-course boundaries

All three re-checked directly against their own current curriculum maps
this session, not assumed unchanged from Chapter 11's own
re-confirmation:

- `/home/dell/projects/ai-engineering-for-everyone/docs/curriculum/CURRICULUM_MAP.md`
  — given a first fully direct check this session specifically for
  LLM-output-evaluation overlap (Chapter 11's own session did not need
  to check this boundary; Chapter 12's own subject makes it directly
  relevant for the first time). Its own Module 3 ("Evaluation-Driven
  Development") outcomes read "build a golden-set evaluation harness;
  use LLM-as-judge and human-in-the-loop review appropriately; wire
  evaluation into a [pipeline]" — squarely about grading a model's own
  generated output against a golden set, never about grading the context
  handed to the model before it generates anything. This chapter's own
  "What This Chapter Owns" section states this boundary directly and
  cites the exact outcome language.
- `/home/dell/projects/mcp-for-everyone/docs/curriculum/CURRICULUM_MAP.md`
  — re-read fresh. Its own Module 5 (Chapters 9-10, permissions/prompt-
  injection trust) and Module 6 (Chapters 11-12, production server
  concerns: tracing, versioning, spec-compatibility) remain unchanged;
  no chapter scores an assembled context bundle's own completeness,
  relevance, or ordering.
- `/home/dell/projects/ai-coding-agents-for-everyone/docs/curriculum/CURRICULUM_MAP.md`
  — re-read fresh. Its 13-chapter roadmap remains scoped entirely to one
  coding agent operating on one codebase (Modules 1-6); no chapter
  evaluates an assembled context bundle as its own artifact.

## New-org exclusion list

Read `quality-audits/chapter-11-audit.md`'s full running list (Chapters
1-10's combined 106 orgs plus Chapter 11's 10 new orgs — 116 total)
before naming any new fictional org for this chapter, and cross-checked
every candidate root word via a live grep against this repo's own
tracked files and `ai-engineering-for-everyone`'s own tracked files at
`/home/dell/projects/ai-engineering-for-everyone/quality-audits/chapter-13-audit.md`,
present locally as it was for Chapters 10 and 11's own sessions. One
candidate root ("Corrigan") was caught by this cross-check —
`ai-engineering-for-everyone`'s own Chapter 10 project uses "Corrigan" —
and replaced with "Bexmoor" before use, confirmed clean by the same
live-grep discipline.

**10 new fictional orgs used this session**, extending Chapters 1-11's
combined 116-org list to **126 total in this repo**:

- **Ternfield Regional Disability Benefits Review Office** (lesson hook;
  product: ClaimLens)
- **Merrivale County Emergency Housing Placement Network** (exercises;
  product: PlacementGuard)
- **Ossbrook Regional Grain Futures Clearinghouse, Colton Regional Home
  Inspection Licensing Board, Bramfield Regional Wildfire Evacuation
  Coordination Center, Grendale Regional Court Interpreter Certification
  Board, Delmoore Regional Pension Fund Audit Office, Sennwick Regional
  Livestock Export Health Certification Bureau, Bexmoor Regional
  Building Code Variance Board, Warrenfield Regional Small Business
  Disaster Loan Review Panel** (practice bank, 8 orgs)

The Module 6 assessment groundwork
(`assessments/module-assessments/module-6-context-evaluation-exercise/`)
deliberately reuses Ternfield Regional Disability Benefits Review
Office/ClaimLens (the lesson's own organization, a fresh case number
rather than a new organization), the same "fresh case at an
already-introduced organization" pattern
`ai-engineering-for-everyone`'s own module-assessment folders use — no
11th new organization was introduced for it.

No collision found against either list's distinctive roots, after the
one caught-and-replaced exception above. Future chapters should extend
this combined list (Chapters 1-11's 116 orgs plus this session's 10, for
**126 total in this repo**), not restart it.

## Source verification, done honestly

Three externally-fetched sources this session, all fetched and read live,
not recalled from training data or reused from a prior chapter's own
citation set without re-verifying:

1. Liu et al., "Lost in the Middle: How Language Models Use Long
   Contexts" (arXiv:2307.03172) — re-fetched live this session and
   confirmed still live and unchanged since Chapter 6's own citation.
   Reused for a different purpose than Chapter 6's own citation of it:
   here it grounds Step 4's positional audit as a checkable evaluation
   criterion, not the assembly-time ordering principle Chapter 6 applies
   it as.
2. RAGAS documentation, "Context Precision" — fetched live and read this
   session for the first time in this repository. Grounds Step 3's noise-
   ratio check directly.
3. RAGAS documentation, "Context Recall" — fetched live and read this
   session for the first time in this repository. Grounds Step 1 and
   Step 2's fact-level completeness check directly.

Both RAGAS citations are new to this repository and independently
corroborate this chapter's own three-part framing (completeness,
relevance/noise, ordering) against an established, real-world RAG
evaluation framework, rather than this chapter inventing its own
taxonomy from first principles.

## Ollama re-verification, done honestly

`curl http://localhost:11434/api/tags` responded normally at the start
of this session and confirmed the same installed model as every prior
chapter (`llama3.2:latest`). Ten live `POST /api/chat` calls were made
this session. The very first call exceeded a 2-minute tool timeout
before returning — a slow cold start, consistent with this course's
standing guidance, though on the harsher end of what recent chapters
have reported (Chapter 11's own session saw 66.7s; this session's first
call ran long enough to be killed by a 120-second Bash tool timeout
before it returned at all, and the retry succeeded normally). Every
subsequent call returned within roughly 5-65 seconds. Four separate
attempts at reproducing a pure positional "lost in the middle" failure
all failed to reproduce it, a genuine negative result disclosed fully in
the lesson's own text and its own "Note on This Chapter's Live-Testing"
section rather than hidden or silently dropped from the chapter's own
argument. The chapter's own live evidence instead centers on the
completeness axis (which reproduced correctly on the first attempt in
both directions) and the LLM-completeness-checker technique (which
surfaced its own genuine, reproducible failure mode — a false negative
under reasoning-style phrasing, corrected under literal-scan phrasing).
No graded `solution.py` anywhere in this chapter's own exercises,
practice bank, or the Module 6 assessment groundwork depends on a live
call.

## Validation

`bash scripts/local_check.sh` run at the end of this session — see
`PROJECT_STATE.md` and the commit message for the recorded result.
