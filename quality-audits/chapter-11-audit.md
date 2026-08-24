# Chapter 11 Quality Audit: Context Isolation and Scoping

Session summary: this session built Chapter 11 in full — `lesson.html`,
exercises (`index.html`, `README.md`, `starter.py`, `solution.py`,
`ai-paired.html`), practice bank (`index.html`, `README.md`,
`starter.py`, `solution.py`), `quiz.html`, and `interview-questions.md`/
`.html` — closing Module 5 (Chapters 9-11) in full. Uses Chapters 1-10 as
a lens, extends the running fictional-org exclusion list, re-verifies
Ollama and every citation fresh this session, and directly re-confirms
both sibling-course boundaries against their own current curriculum maps
rather than trusting Chapter 10's own one-line summaries.

## Honest self-critique

**What's strong:**

- The hook (Vesteroak Regional Appeals Review Board/AppealLine) isolates
  a genuinely distinct failure mode from every prior chapter's own hook:
  Chapter 9 lost a field to a character cutoff inside one tool result.
  Chapter 10 lost an entire unit of work's own data to the same category
  of cutoff at pipeline scale. This chapter's own hook is not a scoping
  bug at all — the isolation boundary that caused the wrong outcome was
  drawn for exactly the right reason (preventing anchoring on a prior
  agent's own conclusion) and still produced a wrong appeal, because it
  swept away a shared, objective fact that was never a threat to the
  reason it existed. This is the deliberate flip side `PROJECT_STATE.md`
  asked this chapter to build, not a re-run of Chapter 10's own
  contamination story.
- The Context Isolation Recipe's six steps are each independently
  testable against the hook's own scenario and map onto a genuinely new
  skill Chapter 10 never taught: Step 1 (name the isolation goal) and
  Step 2 (draw the boundary around opinion, not the whole step) are the
  distinction the hook's own failure turns on; Step 6's own two-probe
  discipline (contamination vs. starvation) is the concrete tool that
  would have caught Vesteroak's own bug before it shipped, and the
  worked math shows explicitly that a contamination probe alone would
  have reported the buggy approach as clean.
- Six live Ollama captures this session are genuinely informative, and
  two negative results (one correct-despite-exposure answer, one outright
  refusal) are disclosed honestly rather than hidden, the same standard
  every prior chapter has held. The four embedded captures show all four
  cells of this chapter's own 2x2 space: no isolation (anchoring
  reproduced), correct isolation (correct, independent judgment),
  isolation drawn too broadly (the stale-threshold bug reproduced), and
  the recipe's own curated hand-off (correct outcome restored) — each
  capture reused the identical underlying facts ($34,200 income, $36,000
  current threshold, $31,500 stale threshold) so only the isolation
  treatment varies between them, not the scenario.
- The worked-math table makes a point none of Chapters 9 or 10 needed to
  make: the buggy approach (isolation drawn too broadly) uses *fewer*
  tokens than its own budget, with 80 tokens of headroom to spare, and
  still produces the wrong decision — a deliberate contrast with Chapter
  9's and Chapter 10's own overflow-centered worked-math tables, making
  explicit that this chapter's own failure mode is not a budget problem
  at all.
- Both live-capture responses that reached the correct final conclusion
  (captures 2 and 4) are read honestly rather than smoothed into a clean
  win: capture 4's own stated reasoning contains an inverted comparison
  ("$34,200 exceeds the minimum required income threshold of $36,000")
  even though its final recommendation is correct, disclosed directly in
  the lesson's own text rather than hidden, the same caution Chapter 10's
  own audit applied to its own evicted-context capture.

**Honest gaps:**

- As in every prior chapter, no exercise or practice `solution.py`
  depends on a live model call — every isolation-goal, boundary,
  hand-off, and probe decision in the automated harnesses is
  deterministic, hand-computed data, for the same reason `local_check.sh`
  runs every `solution.py` under a 20-second timeout.
- This chapter's contamination and starvation probes (Step 6, Exercise 6
  and Exercise 7, Practice Scenario 6) are exercised as clean
  structural/presence checks on a Python dict — real production systems
  often can't check contamination this cleanly, since a model's own
  generated text can leak an opinion's substance in a paraphrase without
  ever including a literally-named field the way this chapter's own
  `contamination_probe()` checks for. This chapter's exercises don't
  exercise that harder, fuzzier detection problem, flagged here the same
  way Chapter 9's own audit flagged fuzzier tool-result staleness rules
  and Chapter 10's own audit flagged fuzzier unit-of-work boundaries as
  unexercised.
- This chapter's own four live captures are all single-turn,
  single-model captures from one session, the same disclosed limitation
  every prior chapter's own audit has flagged for its own captures — a
  reader should not conclude every model or prompt phrasing reproduces
  the same anchoring or starvation pattern shown here.
- The security-motivated isolation goal (Step 1's "reduced blast radius"
  rationale, grounded in this session's own Sophos citation) is
  discussed in the lesson's own text and interview question 8, but this
  chapter's hook, worked math, and live captures all center on the
  anchoring-prevention goal specifically, not the blast-radius-reduction
  goal — a deliberate scope choice to keep one scenario coherent through
  the whole chapter rather than splitting the hook across two unrelated
  isolation goals, disclosed here rather than left implicit. A future
  revision could add a second, security-specific worked example.
- Live capture 3's own first attempt was refused outright by the model
  rather than answered (disclosed honestly in the lesson's own Ollama
  note), which cost one call and one rephrasing cycle this session;
  future sessions attempting a similarly loaded framing should budget for
  this possibility, not just for slow or hung calls.

## Module 5's status, now complete

Per `docs/curriculum/CURRICULUM_MAP.md`'s own "Projects" section, read
again fresh this session rather than assumed unchanged: the numbered
project ladder is still L1 (after Ch. 2), L2 (after Ch. 4), L3 (after
Ch. 8), L4 the Ch. 13 capstone, with no L-tier or module-level project
assigned anywhere in Module 5 (Chapters 9-11) — unchanged from Chapter
9's and Chapter 10's own re-confirmations. Module 5's own two labs
("design the context payload for a tool call," "design a multi-step
pipeline's per-step context with isolation where it matters") still read
as inputs to the Chapter 13 capstone's own system design. This chapter's
`lesson.html`, `ai-paired.html`, `interview-questions.md`, and
`interview-questions.html` all state this explicitly. Module 5 itself is
now complete across Chapters 9-11 — its own curriculum-map outcome
("engineer context for a tool call; engineer context across a
multi-step/multi-agent pipeline with deliberate isolation") is fully
delivered: Chapter 9 (the tool call), Chapter 10 (the pipeline), Chapter
11 (deliberate isolation specifically).

## Boundary re-verification, done directly this session

**`mcp-for-everyone`** — re-checked fresh this session at
`/home/dell/projects/mcp-for-everyone/docs/curriculum/CURRICULUM_MAP.md`.
Its Module 5 (Chapters 9-10) remains "Permissions, Scopes & Sandboxing"
and "Prompt Injection & Tool-Output Trust," unchanged from Chapter 9's
and Chapter 10's own findings — real security-adjacent territory, scoped
to a single server's own permission boundary and a single tool result's
own trustworthiness, not to a deliberate isolation boundary between two
agents or pipeline steps.

**`ai-coding-agents-for-everyone`** — re-checked fresh this session at
`/home/dell/projects/ai-coding-agents-for-everyone/docs/curriculum/CURRICULUM_MAP.md`.
Its 13-chapter roadmap remains scoped entirely to building, prompting,
reviewing, sandboxing, and CI-hardening one coding agent operating on one
codebase (Modules 1-6), unchanged from Chapter 10's own first fully
direct verification. No chapter addresses a second agent, an
orchestrator, or a deliberate isolation boundary between two steps.

## The full, combined fictional-org exclusion list

Reproduced in full so the next session only needs this file, not every
prior audit. Chapters 1-9's 96 orgs plus Chapter 10's 10 new orgs
(Heronbrook Regional Grantmaking Alliance, Prescott County Emergency
Housing Placement Network, Bramwell County Court Interpreter Scheduling
Service, Solmere Regional Disaster Shelter Intake Network, Anchorfield
Regional Small Business Loan Consortium, Hawkridge Regional
Reforestation Grants Program, Havermill County Meals-on-Wheels Route
Optimization Service, Ledgemont Regional Water Utility Leak Response
Pipeline, Tessington Regional Scholarship Review Board, Cresswell
Regional Building Permit Review Pipeline — 106 total before this
session), reproduced verbatim from `quality-audits/chapter-10-audit.md`:
Airport, Alderbrook, Alderwood, Amberglass, Applecross, Ashenvale,
Ashford, Barrowfield, Basilwood, Bellwood, Berkeley, Blackwood,
Blythedale, Brackenfield, Brackwater, Brindlewood, Capstone, Castlebridge,
Cedarview, Cobblestone, Coldwater, Copperfield, Copperlark, Coppervale,
Cranmoor, Crowmarsh, Driftwood, Duskwater, Elmsworth, Faircross,
Fairhaven, Fairmont, Fallowfield, Fenwick, Fernbrook, Foxhaven, Galewood,
Gladstone, Grantham, Grovewell, Halcombe, Harrowgate, Hartwell,
Hollowmere, Hollowridge, Ironwood, Ivywell, Kellbrook, Kestwick,
Kettleford, Larchgate, Larchmoor, Lindenmoor, Loxley, Marlowfield,
Marlstone, Marrowgate, Millbrook, Nettlebrook, Nettlewood, Northaven,
Northfield, Oldfield, Ombervale, Ondermoor, Openfield, Pellham,
Pinehaven, Quillstone, Ravenhollow, Ridgemont, Rosewick, Rutherglen,
Saltmere, Silvergate, Sorrelfield, Stanford, Sunderland, Talbridge,
Thistlecombe, Thorncastle, Thornhollow, Thornwell, Thrumley, Vaultridge,
Vellcross, Vesperfield, Wickmoor, Windale, Windmere, Woodmere, Wrenfield,
Wrensdale, Yarrowfield, Milbrandt, Nordkeep, Calderleigh, Moss(gate),
Cobalt (Ridge), Harbor(light), Aspen(field), Beacon (Crest), Slate(brook),
Timber(line), Garnet (Valley), Poplar (Crossing), Otter(bend),
Quartz(field) — plus, as full organization names used directly by this
repo through Chapter 10: Utilities Cooperative, Graytide Hospitality
Group, Oakspire Home Care Network, Corundale Media Group, Pallisade
Manufacturing, Redcliff Credit Union, Thackery Regional Exchange,
Halveston Regional Health System, Emberlynn Transit Cooperative,
Quarrowstead Legal Aid Partners, Larkmoth Outdoor Retail, Feldspar
Municipal Water Utility, Pemberglen Veterinary Partners, Sootmarsh
Freight Cooperative, Glennoak Wealth Advisors, Tarnwick Community
College, Hushfield Telehealth Network, Vallowmere Grocery Cooperative,
Wrayland Behavioral Health Group, Nightbourne Senior Living Network,
Caldermere Home Health Alliance, Underholt Family Medicine Network,
Presswick Disability Services Cooperative, Dunmere Memory Care
Residences, Oxbridge Pediatric Home Care, Wetherby Insurance Trust,
Camberwell Independent Pharmacy Group, Penrose Estate Planning Partners,
Rushbrook K-12 Special Education Cooperative, Brightmoor Elder Law
Group, Brannigan Home Energy Services, Kirkholme Public Transit Safety
Board, Lynhaven Community Health Partners, Sablewood Legal Trust,
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
Public Defender Consortium, Sagebrush Regional Field Services
Cooperative, Kestrel Regional Grid Operations Cooperative, Winslow
County Emergency Medical Services, Gullwick Harbor Pilotage Authority,
Sparrowmere Independent News Network, Hazelcombe Regional Blood Bank
Network, Renfrew Municipal Snow Removal Cooperative, Dunbar Ridge
Avalanche Forecast Center, Corvale Regional Air Ambulance Consortium,
Whitmore County Livestock Health Cooperative.

This session cross-checked every candidate root word for this chapter's
own new orgs via a live grep against this repo's own tracked files, not
just the reproduced list above. `ai-engineering-for-everyone`'s own
compiled list was checked for availability again this session at
`/home/dell/projects/ai-engineering-for-everyone/quality-audits/chapter-13-audit.md`
and remains present locally, as it was for Chapter 10's own session; a
live grep of every candidate root word this session used against that
repo's full tracked file set also returned zero matches.

**10 new fictional orgs used this session**, every distinctive root word
checked for zero overlap against both lists above via a live grep across
this repo's own tracked files and `ai-engineering-for-everyone`'s own
tracked files before use:

- **Vesteroak Regional Appeals Review Board** (lesson hook; product:
  AppealLine)
- **Calloway County Child Welfare Case Review Network** (exercises;
  product: CaseShield)
- **Brightfen Regional Utility Outage Response Cooperative, Norwick
  Regional Medical Second-Opinion Network, Marrenfield Regional Crop
  Insurance Claims Bureau, Coalport Regional Ferry Safety Inspection
  Authority, Sallowbrook Regional Land Trust Conservation Board, Vantree
  Regional Air Quality Monitoring Network, Kesterly Regional Public
  Records Redaction Service, Wolvercote Regional Peer Review Grant
  Panel** (practice bank, 8 orgs)

No collision found against either list's distinctive roots. Future
chapters should extend this combined list (Chapters 1-10's 106 orgs plus
this session's 10, for **116 total in this repo**), not restart it.

## Source verification, done honestly

All 3 externally-fetched web sources cited in `lesson.html` (2 further
citations are explicitly disclosed local sibling-repo file reads, not
web fetches) were fetched and read live this session via `WebFetch`:

1. Anthropic, "How we built our multi-agent research system" — re-fetched
   live this session for a different passage than Chapter 10's own
   citation of it (Chapter 10 cited its curated-hand-off claim and its
   15x-token-cost figure; this chapter cites its "separate context
   windows" statement and its documented coordination cost of isolation
   — subagents "duplicate work" without clear task boundaries), grounding
   Step 3 and the honest disclosure that isolation carries real
   coordination costs alongside its real benefits.
2. Lance Martin, "Context Engineering for Agents" (blog) — a genuinely
   new citation this session, not reused from any prior chapter. Names
   "isolate" directly as a first-class context engineering strategy
   distinct from write/select/compress, grounding this chapter's own
   framing of isolation as a deliberate design decision rather than
   ordinary curation.
3. Sophos, "Inside the lethal trifecta: Blast radius reduction in AI
   agent deployments" — a genuinely new citation this session, fetched
   live and read for its own direct statements on sandboxing limiting
   collateral damage and credentials never entering LLM context,
   grounding Step 1's security-motivated isolation goal.
4. `mcp-for-everyone`, `docs/curriculum/CURRICULUM_MAP.md` (local
   repository file, re-read fresh this session, not a web fetch).
5. `ai-coding-agents-for-everyone`, `docs/curriculum/CURRICULUM_MAP.md`
   (local repository file, re-read fresh this session, not a web fetch).

No citation needed correction or replacement this session — consistent
with every prior chapter's own clean sessions (Chapters 3, 7, 9, and 10),
reported here as this session's own result, not an expectation either
way.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally this session
and confirmed the same installed model as all ten prior chapters
(`llama3.2:latest`). The session's first `POST /api/chat` call took 66.7s
wall time (63.4s of that reported as model-load time, a cold start),
consistent with this course's own standing guidance to budget for a slow
first call regardless of how many consecutive prior chapters got
first-attempt successes. `POST /api/chat` was called seven times this
session in total. One early prompt iteration (Live Capture 1's own first
attempt, presenting the prior agent's conclusion as a plain fact rather
than a recommendation) produced a correct, unaffected answer — a
genuinely informative negative result, disclosed honestly in the lesson's
own text, showing the model doesn't anchor on every prior conclusion
shown to it unconditionally. One further attempt (an early phrasing of
Live Capture 3) was refused outright by the model rather than answered,
also disclosed honestly; a rephrased, less loaded version of the same
request produced a substantive answer on the next call. The four calls
embedded in `lesson.html` as this chapter's own live captures returned in
25.8s (no isolation, anchoring reproduced), 18.2s (isolated, correct),
20.3s (isolation drawn too broadly, stale threshold reproduced), and
25.4s (Step 4 curated hand-off, correct), all warm after the session's
own first cold call. As in every prior chapter, no graded `solution.py`
depends on a live call — every isolation-goal, boundary, hand-off, and
probe decision in the automated harnesses is deterministic, hand-computed
data, for the same 20-second-timeout reason documented since Chapter 3.
This session's own mix of one slow cold start, one refusal, and five
otherwise first-attempt successes is reported honestly as this session's
own result, not a claim about how the endpoint will behave next time;
future sessions should keep budgeting for retries with generous (120s+)
timeouts and occasional outright content refusals regardless.

## Code tested before writing

`exercises/solution.py` and `practice/solution.py` were each run for
real this session and produce a perfect score:

```
$ python3 exercises/solution.py   -> TOTAL: 20/20
$ python3 practice/solution.py    -> TOTAL: 8/8
```

`exercises/starter.py` and `practice/starter.py` were each also run for
real (with their TODOs still unfilled) to confirm they fail cleanly with
a readable score report and no traceback, since a learner will run these
files first:

```
$ python3 exercises/starter.py    -> TOTAL: 0/20 (clean, no traceback)
$ python3 practice/starter.py     -> TOTAL: 0/8 (clean, no traceback)
```

`context_isolation_recipe.py`, `worked_math_check.py`, and
`isolation_probes.py` (the three standalone scripts embedded as executed
code in `lesson.html`) were each run for real this session, and their
printed output is reproduced verbatim in the lesson, not hand-typed.

`bash scripts/local_check.sh` was run from the repo root at the end of
this session and passed clean (folder structure, placeholder-text scan,
Python syntax, every `solution.py` executed for real, JS syntax and
chapter-path validation, secret scan).

## Registration updated this session

`assets/chapters-data.js` (added Chapter 11's own `path`), root
`index.html` (`hero-stats` now reads "11 of 13 chapters live" and "5 of 6
modules complete" — the first module-count change since Chapter 8 closed
Module 4 — plus the "All Chapters" intro paragraph extended with Chapter
11's own summary and Module 5's own closing note), and
`docs/curriculum/index.html` (Chapter 11's own chapter-card flipped to
"Live" with a real `href`, its own lede paragraph extended, AND Module
5's own feature card flipped from "In Progress" to "Complete," the first
module-status flip since Chapter 8 closed Module 4) were all updated in
this same session. `docs/curriculum/CURRICULUM_MAP.md` was checked and
confirmed not to track per-chapter or per-module completion status
inline (its own "Chapter Roadmap" table has no status column at all,
unchanged from Chapter 10's own finding), so no edit was needed there.
