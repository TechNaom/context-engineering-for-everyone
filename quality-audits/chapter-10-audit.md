# Chapter 10 Quality Audit: Context Engineering for Multi-Agent Systems

Session summary: this session built Chapter 10 in full — `lesson.html`,
exercises (`index.html`, `README.md`, `starter.py`, `solution.py`,
`ai-paired.html`), practice bank (`index.html`, `README.md`,
`starter.py`, `solution.py`), `quiz.html`, and `interview-questions.md`/
`.html` — continuing Module 5 (Chapters 9-11). Uses Chapters 1-9 as a
lens, extends the running fictional-org exclusion list (not restarting
it), re-verifies Ollama and every citation fresh this session, and
directly re-confirms both sibling-course boundaries against their own
current curriculum maps rather than trusting the prior session's
one-line summaries — `mcp-for-everyone` (re-checked, unchanged from
Chapter 9's own finding) and, per `PROJECT_STATE.md`'s own explicit
instruction, `ai-coding-agents-for-everyone` (re-checked for the first
time this directly, not just re-asserted from Chapter 9's own session).

## Honest self-critique

**What's strong:**

- The hook (Heronbrook Regional Grantmaking Alliance/GrantPilot)
  isolates a genuinely distinct failure mode from Chapter 9's own:
  Chapter 9 lost one field to a character cutoff inside one tool result.
  This chapter's own hook loses an entire unit of work's own data to the
  same category of cutoff, but applied to an ever-growing, multi-step,
  multi-unit-of-work session history — a pipeline-scale version of the
  same underlying problem (an unscoped, growing thing competing for a
  fixed budget), with a new consequence Chapter 9 never had to name:
  cross-unit-of-work contamination, where a resolved finding from one
  completed case bleeds into a different case's own review.
- Every sub-agent in the hook's own story reasons correctly about
  whatever it's actually shown — the failure is entirely in what the
  orchestrator decided to hand each step, not in any individual agent's
  own logic. This distinction (correct per-agent reasoning is not the
  same as a well-scoped pipeline) is carried through the whole chapter,
  including the interview questions and the AI-paired critique.
- The Pipeline/Multi-Agent Context Recipe's six steps map directly onto
  the hook's own failure and are each independently testable: Step 1
  (scoped context contract) and Step 2 (curated hand-off) fix the
  per-step scoping gap; Step 3 (per-step ledger line) and Step 4
  (unit-of-work isolation) fix the budget-overflow and
  contamination-between-units failure the two live-capture pairs show
  concretely; Step 5 (sub-agent delegation) and Step 6 (downstream
  handoff) close the boundary against `ai-coding-agents-for-everyone`
  and Chapter 7 respectively.
- Four live Ollama captures this session are genuinely informative, not
  cherry-picked, and two negative results from early prompt iterations
  are disclosed honestly rather than hidden: the first two attempts at
  reproducing cross-applicant contamination (naming the current
  applicant explicitly in the question, against an otherwise-unscoped
  session log) produced correct answers both times, a real negative
  result showing the model can filter a well-labeled current case out of
  unscoped history. Reproducing GrantPilot's own actual failure required
  reproducing its own actual character-based budget cutoff, not just an
  unscoped-but-labeled history — this is reported explicitly in the
  lesson's own live-capture section and the Ollama disclosure, not
  smoothed over. The second live-capture pair (naive vs. evicted
  unit-of-work working context) is read honestly on both sides: the
  evicted capture avoided the naive capture's specific contamination
  failure (borrowing a completed case's own resolved finding) but still
  produced a minor, ungrounded elaboration of its own, disclosed directly
  in the lesson rather than presented as a clean win.
- This session's own re-confirmation of the `ai-coding-agents-for-everyone`
  boundary went beyond the one-line cross-link claim in
  `CURRICULUM_MAP.md`: this session independently read that repo's own
  `docs/curriculum/CURRICULUM_MAP.md` at
  `/home/dell/projects/ai-coding-agents-for-everyone/docs/curriculum/CURRICULUM_MAP.md`
  and confirmed its entire 13-chapter roadmap is scoped to building,
  prompting, reviewing, and securing one coding agent operating on one
  codebase (Modules 1-6), with no chapter anywhere addressing a
  multi-agent pipeline, an orchestrator delegating to sub-agents, or
  inter-step/inter-agent context scoping — the closest chapter (6,
  "Context Windows and Codebase-Scale Understanding") is about one
  agent's own budget against a large codebase, not multiple agents at
  all. This is the direct verification `PROJECT_STATE.md` explicitly
  flagged as needing more rigor than Chapter 9's own session gave it.
- Every number in the lesson's two worked-math tables and every
  exercise/practice `solution.py` was computed and cross-checked against
  its own dependent scoring code before publishing, not asserted — see
  "Code tested before writing" below.

**Honest gaps:**

- As in every prior chapter, no exercise or practice `solution.py`
  depends on a live model call — every context-scoping, curation,
  budget, and eviction decision in the automated harnesses is
  deterministic, hand-computed data. This remains a disclosed, deliberate
  judgment call for the same reason Chapters 3-9 gave:
  `scripts/local_check.sh` runs every `solution.py` under a 20-second
  timeout, well inside this session's own measured Ollama load times.
- This chapter's worked-math tables use round, hand-assigned per-step
  token figures (140-180 tokens of raw output per prior unit of work,
  chosen for narrative clarity) rather than the harder real-world problem
  of measuring an actual pipeline's own per-unit token cost empirically.
  Real production pipelines' own per-unit cost varies by case complexity
  in ways this chapter's own worked examples don't model — a
  simplification in the same spirit as Chapter 9's own audit flagged for
  its field-priority exercises' clean, unambiguous scoring.
- Unit-of-work isolation (Step 4, Exercise 5) is exercised only as an
  exact `household_id`/`applicant` match. Real production pipelines
  sometimes have fuzzier unit-of-work boundaries — a single case that
  spans multiple pipeline runs (a re-submitted application, a household
  whose placement is revisited after an initial match falls through)
  where "is this the same unit of work or a new one" is itself a design
  decision, not a clean identity check. This chapter's exercises don't
  exercise that harder judgment call, flagged here for a later chapter
  or revision the same way Chapter 9's own audit flagged fuzzier
  tool-result staleness rules as unexercised.
- This chapter's own four live captures are all single-turn,
  single-model captures from one session, the same disclosed limitation
  Chapters 6-9's own audits flagged for their own captures — a reader
  should not conclude every model or prompt phrasing reproduces the same
  contamination pattern; a future revision could add a second model or a
  repeated-trial capture to strengthen the claim.
- The evicted-context live capture (capture 4) produced a technically
  correct "pending further evaluation" eligibility answer but attached an
  ungrounded elaboration ("due to prior applicants' organizations being
  found ineligible") not present anywhere in the evicted context handed
  to it. This is disclosed directly in the lesson's own text as a
  reminder that eviction prevents a specific, identifiable failure mode
  (borrowing another unit of work's own resolved finding) rather than
  every way a model can produce an ungrounded sentence — not smoothed
  into a clean "eviction fixes everything" narrative.

## Module 5's project status, re-confirmed not shipping this chapter

Per `docs/curriculum/CURRICULUM_MAP.md`'s own "Projects" section, read
again fresh this session rather than assumed unchanged: the numbered
project ladder is still L1 (after Ch. 2), L2 (after Ch. 4), L3 (after
Ch. 8), L4 the Ch. 13 capstone, with no L-tier or module-level project
assigned anywhere in Module 5 (Chapters 9-11). Module 5's own two labs
("design the context payload for a tool call," "design a multi-step
pipeline's per-step context with isolation where it matters") still read
as inputs to the Chapter 13 capstone's own system design, not a project
due at the end of Chapter 10. This chapter's `lesson.html`,
`ai-paired.html`, `interview-questions.md`, and `interview-questions.html`
all state this explicitly.

## Boundary re-verification, done directly this session

**`ai-coding-agents-for-everyone`** — the boundary `PROJECT_STATE.md`
explicitly flagged as needing more direct verification than Chapter 9's
own session gave it. This session read
`/home/dell/projects/ai-coding-agents-for-everyone/docs/curriculum/CURRICULUM_MAP.md`
directly, not the cross-link summary alone. Findings: that course's 13
chapters (Modules 1-6) build, prompt, review, secure, and CI-integrate
**one** coding agent operating on **one** codebase — Module 1 (using
coding agents well), Module 2 (the agentic loop, internals of one
agent), Module 3 (building a minimal agent from scratch, then giving it
tools, then MCP-based tools), Module 4 (reviewing that one agent's own
generated diffs), Module 5 (sandboxing and CI-hardening that one agent),
Module 6 (a capstone designing one agentic CI workflow). No chapter in
its roadmap addresses a multi-agent pipeline, an orchestrator delegating
to sub-agents, or what context one step or agent should receive from
another — the closest chapter (6, "Context Windows and Codebase-Scale
Understanding") is scoped to one agent's own context budget against a
large codebase, not inter-agent or inter-step scoping. The
`CURRICULUM_MAP.md` claim ("builds on but does not duplicate...
`ai-coding-agents-for-everyone` (agent-loop depth for one application
category)") holds without adjustment, now independently verified rather
than asserted.

**`mcp-for-everyone`** — re-checked fresh this session at
`/home/dell/projects/mcp-for-everyone/docs/curriculum/CURRICULUM_MAP.md`
even though Chapter 9's own session already verified it directly, per
`PROJECT_STATE.md`'s own instruction not to assume a local file is
unchanged. Its Module 5 (Chapters 9-10) remains "Permissions, Scopes &
Sandboxing" and "Prompt Injection & Tool-Output Trust," unchanged from
Chapter 9's own finding. No chapter in its 13-chapter roadmap addresses
multi-step or multi-agent context scoping.

## The full, combined fictional-org exclusion list

Reproduced in full so the next session only needs this file, not every
prior audit. Chapters 1-8's 86 orgs plus Chapter 9's 10 new orgs
(Sagebrush Regional Field Services Cooperative, Kestrel Regional Grid
Operations Cooperative, Winslow County Emergency Medical Services,
Gullwick Harbor Pilotage Authority, Sparrowmere Independent News
Network, Hazelcombe Regional Blood Bank Network, Renfrew Municipal Snow
Removal Cooperative, Dunbar Ridge Avalanche Forecast Center, Corvale
Regional Air Ambulance Consortium, Whitmore County Livestock Health
Cooperative — 96 total before this session), reproduced verbatim from
`quality-audits/chapter-09-audit.md`: Airport, Alderbrook, Alderwood,
Amberglass, Applecross, Ashenvale, Ashford, Barrowfield, Basilwood,
Bellwood, Berkeley, Blackwood, Blythedale, Brackenfield, Brackwater,
Brindlewood, Capstone, Castlebridge, Cedarview, Cobblestone, Coldwater,
Copperfield, Copperlark, Coppervale, Cranmoor, Crowmarsh, Driftwood,
Duskwater, Elmsworth, Faircross, Fairhaven, Fairmont, Fallowfield,
Fenwick, Fernbrook, Foxhaven, Galewood, Gladstone, Grantham, Grovewell,
Halcombe, Harrowgate, Hartwell, Hollowmere, Hollowridge, Ironwood,
Ivywell, Kellbrook, Kestwick, Kettleford, Larchgate, Larchmoor,
Lindenmoor, Loxley, Marlowfield, Marlstone, Marrowgate, Millbrook,
Nettlebrook, Nettlewood, Northaven, Northfield, Oldfield, Ombervale,
Ondermoor, Openfield, Pellham, Pinehaven, Quillstone, Ravenhollow,
Ridgemont, Rosewick, Rutherglen, Saltmere, Silvergate, Sorrelfield,
Stanford, Sunderland, Talbridge, Thistlecombe, Thorncastle, Thornhollow,
Thornwell, Thrumley, Vaultridge, Vellcross, Vesperfield, Wickmoor,
Windale, Windmere, Woodmere, Wrenfield, Wrensdale, Yarrowfield,
Milbrandt, Nordkeep, Calderleigh, Moss(gate), Cobalt (Ridge),
Harbor(light), Aspen(field), Beacon (Crest), Slate(brook), Timber(line),
Garnet (Valley), Poplar (Crossing), Otter(bend), Quartz(field) — plus,
as full organization names used directly by this repo through Chapter 9:
Utilities Cooperative, Graytide Hospitality Group, Oakspire Home Care
Network, Corundale Media Group, Pallisade Manufacturing, Redcliff Credit
Union, Thackery Regional Exchange, Halveston Regional Health System,
Emberlynn Transit Cooperative, Quarrowstead Legal Aid Partners, Larkmoth
Outdoor Retail, Feldspar Municipal Water Utility, Pemberglen Veterinary
Partners, Sootmarsh Freight Cooperative, Glennoak Wealth Advisors,
Tarnwick Community College, Hushfield Telehealth Network, Vallowmere
Grocery Cooperative, Wrayland Behavioral Health Group, Nightbourne Senior
Living Network, Caldermere Home Health Alliance, Underholt Family
Medicine Network, Presswick Disability Services Cooperative, Dunmere
Memory Care Residences, Oxbridge Pediatric Home Care, Wetherby Insurance
Trust, Camberwell Independent Pharmacy Group, Penrose Estate Planning
Partners, Rushbrook K-12 Special Education Cooperative, Brightmoor Elder
Law Group, Brannigan Home Energy Services, Kirkholme Public Transit
Safety Board, Lynhaven Community Health Partners, Sablewood Legal Trust,
Coalridge Municipal Transit Authority, Pikestone Logistics Group,
Rowancraig Insurance Underwriters, Draymoor Agricultural Cooperative,
Osprey Ridge Wealth Management, Talmarsh Veterinary Alliance, Marchside
Regional Trauma Network, Calverton Public Defender's Office, Nunroth
Independent Bookstore Cooperative, Vesparro Marine Salvage, Holstead
Grain Exchange, Quenby Historical Archive Society, Farrowline Dairy
Cooperative, Delacroix Regional Airport Authority, Pennwhistle Community
Radio Network, Ostergaard Marine Insurance, Brackholt County Court
Records Office, Hadleworth Metro Water Authority, Corrinvale Independent
Pharmacy Network, Juniper Ridge Veterinary Partners, Quarrydale Auto
Diagnostics Cooperative, Tamworth Regional Housing Trust, Wexford
Maritime Charter Group, Dovetail Woodcraft Guild, Cinderfield Volunteer
Fire Network, Barleycroft Grain & Feed Cooperative, Yewmarsh Wildlife
Sanctuary, Mossgate Regional Law Library Consortium, Cobalt Ridge Claims
Adjustment Bureau, Harborlight Maritime Archive Society, Aspenfield
Community College Library, Beacon Crest Genealogy Society, Slatebrook
Patent Research Group, Timberline Structural Engineering Archive, Garnet
Valley Genetic Testing Registry, Poplar Crossing School District
Archive, Otterbend Wildlife Research Station, Quartzfield Regional
Public Defender Consortium.

This session also re-checked the exclusion list directly against
`ai-engineering-for-everyone`'s own compiled list, which is now present
locally in this sandbox (`/home/dell/projects/ai-engineering-for-everyone/quality-audits/chapter-13-audit.md`),
unlike Chapter 9's own session where that repo wasn't available locally.
A live grep of every candidate root word this session used against that
repo's full tracked file set returned zero matches, in addition to the
zero-collision check against this repo's own combined list above.

**10 new fictional orgs used this session**, every distinctive root word
checked for zero overlap against both lists above via a live grep across
this repo's own tracked files and `ai-engineering-for-everyone`'s own
tracked files before use:

- **Heronbrook Regional Grantmaking Alliance** (lesson hook; product:
  GrantPilot)
- **Prescott County Emergency Housing Placement Network** (exercises;
  product: PlacementLine)
- **Bramwell County Court Interpreter Scheduling Service, Solmere
  Regional Disaster Shelter Intake Network, Anchorfield Regional Small
  Business Loan Consortium, Hawkridge Regional Reforestation Grants
  Program, Havermill County Meals-on-Wheels Route Optimization Service,
  Ledgemont Regional Water Utility Leak Response Pipeline, Tessington
  Regional Scholarship Review Board, Cresswell Regional Building Permit
  Review Pipeline** (practice bank, 8 orgs)

No collision found against either list's distinctive roots. Future
chapters should extend this combined list (Chapters 1-9's 96 orgs plus
this session's 10, for **106 total in this repo**), not restart it.

## Source verification, done honestly

All 3 externally-fetched web sources cited in `lesson.html` (2 further
citations are explicitly disclosed local sibling-repo file reads, not
web fetches) were fetched and read live this session via `WebFetch`, and
independently re-confirmed live via `curl -L -o /dev/null -w
"%{http_code}"`:

1. Anthropic, "How we built our multi-agent research system" — fetched
   live and confirmed live this session (HTTP 200), grounding Step 2's
   curated-handoff rule and the general claim that multi-agent systems
   carry a real, disclosed token cost ("about 15x more tokens than
   chats").
2. Anthropic, "Effective context engineering for AI agents" — re-fetched
   live this session (HTTP 200); cited by Chapter 9's own session for a
   different passage (Step 2's tool-schema-budgeting rationale there),
   disclosed honestly here as re-fetched for this chapter's own Step 5
   sub-agent-delegation rule specifically.
3. Anthropic, "Building effective agents" — fetched live and confirmed
   live this session (HTTP 200), grounding this chapter's own choice of
   scenario shape (the "orchestrator-workers" workflow pattern
   GrantPilot's own architecture follows).
4. `mcp-for-everyone`, `docs/curriculum/CURRICULUM_MAP.md` (local
   repository file, re-read fresh this session, not a web fetch) —
   confirms the `mcp-for-everyone` boundary remains unchanged from
   Chapter 9's own finding.
5. `ai-coding-agents-for-everyone`, `docs/curriculum/CURRICULUM_MAP.md`
   (local repository file, read fresh this session, not a web fetch) —
   the direct verification `PROJECT_STATE.md` explicitly requested; see
   "Boundary re-verification" above for the full finding.

No citation needed correction or replacement this session — consistent
with Chapter 9's own clean session and Chapter 7's own clean session,
reported here as this session's own result, not an expectation either
way per `PROJECT_STATE.md`'s own re-verification discipline.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally this session
and confirmed the same installed model as all nine prior chapters
(`llama3.2:latest`). `POST /api/chat` was called six times this session,
all six succeeding on the first attempt with no hang or retry needed.
Two early prompt iterations (explicitly naming the current applicant
against an otherwise-unscoped session log) are disclosed honestly in the
lesson's own text as negative results, not hidden — the real failure
required reproducing GrantPilot's own actual character-based budget
cutoff, not just an unscoped-but-labeled history. The four calls
embedded in `lesson.html` as this chapter's own live captures returned
in 54.1s (naive, budget-truncated log), 26.4s (scoped, correct), 18.0s
(naive, unevicted between units of work), and 19.7s (Step 4, evicted),
all already warm this session with sub-second reported load times after
the session's first call. As in every prior chapter, no graded
`solution.py` depends on a live call — every context-scoping, curation,
budget, and eviction decision in the automated harnesses is
deterministic, hand-computed data, for the same 20-second-timeout reason
documented since Chapter 3. This session's own six first-attempt
successes are reported honestly as this session's own result, not a
claim the intermittent hang documented in Chapter 3 is permanently
resolved; future sessions should keep budgeting for retries with
generous (120s+) timeouts regardless.

## Code tested before writing

`exercises/solution.py` and `practice/solution.py` were each run for
real this session and produce a perfect score:

```
$ python3 exercises/solution.py   -> TOTAL: 25/25
$ python3 practice/solution.py    -> TOTAL: 8/8
```

`exercises/starter.py` and `practice/starter.py` were each also run for
real (with their TODOs still unfilled) to confirm they fail cleanly with
a readable score report and no traceback, since a learner will run these
files first:

```
$ python3 exercises/starter.py    -> TOTAL: 0/25 (clean, no traceback)
$ python3 practice/starter.py     -> TOTAL: 0/8 (clean, no traceback)
```

`full_pipeline.py`, `worked_math_check.py`, and `ledger_and_eviction.py`
(the three standalone scripts embedded as executed code in `lesson.html`)
were each run for real this session, and their printed output is
reproduced verbatim in the lesson, not hand-typed.

`bash scripts/local_check.sh` was run from the repo root at the end of
this session and passed clean (folder structure, placeholder-text scan,
Python syntax, every `solution.py` executed for real, JS syntax and
chapter-path validation, secret scan).

## Registration updated this session

`assets/chapters-data.js` (added Chapter 10's own `path`), root
`index.html` (`hero-stats` now reads "10 of 13 chapters live," "4 of 6
modules complete" left unchanged since Module 5 still needs Chapter 11,
and the "All Chapters" intro paragraph extended with Chapter 10's own
summary), and `docs/curriculum/index.html` (Chapter 10's own chapter-card
flipped to "Live" with a real `href`, and its own lede paragraph
extended) were all updated in this same session. `docs/curriculum/CURRICULUM_MAP.md`
was checked and confirmed not to track per-chapter completion status
inline (its own "Chapter Roadmap" table has no status column at all), so
no edit was needed there. Module 5's own feature card in
`docs/curriculum/index.html` was left reading "In Progress," as
instructed — Chapter 11 closes the module, not this chapter.
