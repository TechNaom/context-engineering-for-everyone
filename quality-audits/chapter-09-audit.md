# Chapter 9 Quality Audit: Context Engineering for Tool Use

Session summary: this session finished Chapter 9 (a prior, interrupted
session had already written `lesson.html` in full but left every other
required file unbuilt, unregistered, and uncommitted), opening Module 5
(Chapters 9-11). Uses Chapters 1-8 as a lens, extends the running
fictional-org exclusion list (not restarting it), re-verifies Ollama and
every citation fresh this session, re-confirms the protocol-agnostic
boundary against `mcp-for-everyone` directly against its own current
curriculum map, and confirms via the curriculum map's own "Projects"
section that Module 5 carries no dedicated project slot — this chapter
ships none.

## Honest self-critique

**What's strong:**

- The hook (Sagebrush Regional Field Services Cooperative/DispatchLine)
  isolates a genuinely distinct failure mode from every prior chapter's
  own hook: the tool itself executes correctly and returns correct,
  complete data every time — the failure is entirely in what happens to
  the tool's own definition and result on the way into context (an
  unscoped twelve-tool schema registry crowding the tool-output budget,
  then a raw forty-field result truncated by character count mid-field).
  This is deliberately not a tool-execution bug, a protocol bug, or a
  retrieval/multi-source problem any prior chapter already owns.
- The Tool Context Recipe's six steps (scope tool definitions, budget
  each schema explicitly, curate a tool's raw result, fit it to budget
  at a field boundary, evict superseded tool-call history, hand off to
  Chapter 7's own Source Assembly Recipe) map directly onto the hook's
  own failure and are each independently testable in this session's
  exercises and practice bank.
- Both live captures in `lesson.html` are genuinely informative, not
  cherry-picked: the curated, field-boundary-safe prompt produced a
  clean, correctly grounded answer; the raw, truncated prompt produced a
  response that happened to land on the same final verdict but for
  reasons never actually grounded in the surviving fields — a more
  nuanced, honest illustration than a simple wrong-answer failure, used
  directly in the lesson as an argument for why curation and
  field-boundary-safe fitting matter even when a model's final verdict
  looks fine on a given run.
- This session's own re-confirmation of the `mcp-for-everyone` boundary
  went beyond trusting the lesson's own draft text: this session
  independently re-read `mcp-for-everyone`'s own
  `docs/curriculum/CURRICULUM_MAP.md` at
  `/home/dell/projects/mcp-for-everyone/docs/curriculum/CURRICULUM_MAP.md`
  and confirmed, word for word, that Module 5 there (Chapters 9-10) is
  titled "Permissions, Scopes & Sandboxing" and "Prompt Injection &
  Tool-Output Trust" — access control and adversarial trust in a tool's
  output, not tool-schema token cost, tool-result curation, or
  tool-call-history budgeting. The lesson's own citation (source 5)
  correctly reflects this.
- Every number in the lesson's worked-math table and every exercise/
  practice `solution.py` was computed and cross-checked against its own
  dependent scoring code before publishing, not asserted — both score a
  perfect total when run (see "Code tested before writing" below).
- The chapter states explicitly, in its own text, both what it is not
  re-teaching (Chapters 1-8's own recipes, used only as a lens) and the
  precise handoff boundary against Chapter 7 (this chapter produces the
  one well-formed `tool_result` source Chapter 7's own Step 1 inventory
  assumes it already has) and against `mcp-for-everyone` (protocol
  negotiation, discovery, authorization, and transport, all explicitly
  out of scope here).
- The curriculum map's own "Projects" section
  (`docs/curriculum/CURRICULUM_MAP.md`) was read directly this session,
  not assumed: its numbered ladder (L1 after Ch. 2, L2 after Ch. 4, L3
  after Ch. 8, L4 the Ch. 13 capstone) assigns no tier at all to Module
  5, and Module 5's own two labs ("design the context payload for a
  tool call," "design a multi-step pipeline's per-step context with
  isolation") are not listed under "Projects" as their own numbered
  deliverable — confirming, rather than assuming, that Chapter 9 (and
  Module 5 generally) ships no dedicated project this session or at the
  end of Chapter 10 or 11, with both labs instead feeding directly into
  the Chapter 13 capstone's own system design.

**Honest gaps:**

- As in every prior chapter, no exercise or practice `solution.py`
  depends on a live model call — every schema-scoping, curation,
  field-fit, and history-eviction decision in the automated harnesses is
  deterministic, hand-computed data. This remains a disclosed, deliberate
  judgment call for the same reason Chapters 3-8 gave:
  `scripts/local_check.sh` runs every `solution.py` under a 20-second
  timeout, well inside this session's own measured Ollama load times.
- This chapter's field-boundary-safe-fit exercises (Exercise 5, Scenario
  4) use a hand-assigned priority order for which field matters most,
  rather than the harder real-world problem of deriving that priority
  order from a request type's own decision logic. Real production tool
  results sometimes have a less obvious priority ranking than
  DispatchLine's own "the gust reading and advisory obviously matter
  most" case — this chapter's own worked examples were deliberately
  constructed with an unambiguous priority field, avoiding that harder
  judgment call, the same category of simplification Chapter 8's own
  audit flagged for its boundary-safe-fit exercises' clean, unambiguous
  scoring.
- Tool-call-history eviction (Step 5, Exercise 6, Practice Scenario 6)
  is exercised only as a same-tool/same-target-equality rule (same tool,
  same station/region, later turn wins). Real production systems
  sometimes need fuzzier staleness rules — a tool result that's still
  technically "the same query" but returned meaningfully different data
  due to a time-sensitive underlying fact (weather, load, inventory)
  even without an exact-match re-query — which this chapter's exercises
  do not exercise, flagged here for a later chapter or revision the same
  way Chapter 4's own audit flagged staleness *detection* (versus
  staleness *policy*) as unexercised.
- This chapter's own two live captures, while genuinely informative (see
  above), are both single-turn, single-model captures from one session —
  a reader should not conclude every model or prompt phrasing produces
  the same "grounded when curated, plausible-but-ungrounded when
  truncated" pattern; a future revision could add a second model or a
  repeated-trial capture to strengthen this claim beyond a single
  illustrative example, the same tightening Chapters 6-8's own audits
  flagged for their own captures.
- This session picked up a `lesson.html` file already written in full by
  a prior, interrupted session. Every claim, citation, and worked-math
  number in that file was independently re-verified this session (see
  "Source verification" and the Ollama section below) rather than
  assumed correct because it was already on disk — but the file's own
  prose was not rewritten from scratch, so any subtle stylistic drift
  from this session's own voice versus the original drafting session's
  voice is possible, though not found on this session's own read-through.

## Module 5's project status, confirmed not shipping this chapter

Per `docs/curriculum/CURRICULUM_MAP.md`'s own "Projects" section, the
numbered project ladder is: L1 Guided (ships after Ch. 2), L2 Assisted
(ships after Ch. 4), L3 Independent (ships after Ch. 8), L4 Architecture
Challenge (the Ch. 13 capstone). No L-tier or module-level project is
assigned anywhere in Module 5 (Chapters 9-11) — a genuinely different
situation from Module 3's own tier-gap (which still got a module-level
project, just an unnumbered one) and from Module 4 (which landed
cleanly on the literal L3 tier). Module 5's own two labs, as named in
the curriculum map's Module 5 entry itself ("design the context payload
for a tool call" and "design a multi-step pipeline's per-step context
with isolation where it matters"), read as inputs to the Chapter 13
capstone's own system design rather than as a project due at the end of
Chapter 9, 10, or 11. This chapter's `lesson.html`, `interview-
questions.md`, and `interview-questions.html` all state this explicitly
rather than silently omitting the section a reader would expect after
four of the prior eight chapters shipped one.

## The full, combined fictional-org exclusion list

Reproduced in full so the next session only needs this file, not every
prior audit. Chapters 1-8's 86 orgs (already checked with zero collision
against `ai-engineering-for-everyone`'s own compiled list): Airport,
Alderbrook, Alderwood, Amberglass, Applecross, Ashenvale, Ashford,
Barrowfield, Basilwood, Bellwood, Berkeley, Blackwood, Blythedale,
Brackenfield, Brackwater, Brindlewood, Capstone, Castlebridge, Cedarview,
Cobblestone, Coldwater, Copperfield, Copperlark, Coppervale, Cranmoor,
Crowmarsh, Driftwood, Duskwater, Elmsworth, Faircross, Fairhaven,
Fairmont, Fallowfield, Fenwick, Fernbrook, Foxhaven, Galewood, Gladstone,
Grantham, Grovewell, Halcombe, Harrowgate, Hartwell, Hollowmere,
Hollowridge, Ironwood, Ivywell, Kellbrook, Kestwick, Kettleford,
Larchgate, Larchmoor, Lindenmoor, Loxley, Marlowfield, Marlstone,
Marrowgate, Millbrook, Nettlebrook, Nettlewood, Northaven, Northfield,
Oldfield, Ombervale, Ondermoor, Openfield, Pellham, Pinehaven,
Quillstone, Ravenhollow, Ridgemont, Rosewick, Rutherglen, Saltmere,
Silvergate, Sorrelfield, Stanford, Sunderland, Talbridge, Thistlecombe,
Thorncastle, Thornhollow, Thornwell, Thrumley, Vaultridge, Vellcross,
Vesperfield, Wickmoor, Windale, Windmere, Woodmere, Wrenfield,
Wrensdale, Yarrowfield, Milbrandt, Nordkeep, Calderleigh, Moss(gate),
Cobalt (Ridge), Harbor(light), Aspen(field), Beacon (Crest),
Slate(brook), Timber(line), Garnet (Valley), Poplar (Crossing),
Otter(bend), Quartz(field) — plus, as full organization names used
directly by this repo through Chapter 8: Utilities Cooperative, Graytide
Hospitality Group, Oakspire Home Care Network, Corundale Media Group,
Pallisade Manufacturing, Redcliff Credit Union, Thackery Regional
Exchange, Halveston Regional Health System, Emberlynn Transit
Cooperative, Quarrowstead Legal Aid Partners, Larkmoth Outdoor Retail,
Feldspar Municipal Water Utility, Pemberglen Veterinary Partners,
Sootmarsh Freight Cooperative, Glennoak Wealth Advisors, Tarnwick
Community College, Hushfield Telehealth Network, Vallowmere Grocery
Cooperative, Wrayland Behavioral Health Group, Nightbourne Senior Living
Network, Caldermere Home Health Alliance, Underholt Family Medicine
Network, Presswick Disability Services Cooperative, Dunmere Memory Care
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
Public Defender Consortium — and against `ai-engineering-for-everyone`'s
own full compiled exclusion list (its `quality-audits/chapter-13-
audit.md`, as reproduced since Chapter 6's own audit): the same
root-word list reproduced above is shared verbatim between the two
lists as previously cross-checked; no new fetch of that repo was needed
this session since it is not present locally in this sandbox, consistent
with how this repo has referenced it since Chapter 1.

**10 new fictional orgs used this session**, every distinctive root word
(Sagebrush, Kestrel, Winslow, Gullwick, Sparrowmere, Hazelcombe,
Renfrew, Dunbar, Corvale, Whitmore) checked for zero collision against
both lists above via a live grep across `quality-audits/`, `chapters/`,
and this repo's own tracked files before use, which returned zero
matches for any of the 10 new roots below (each grep run individually
this session, confirmed clean):

- **Sagebrush Regional Field Services Cooperative** (lesson hook,
  written by the prior session; product: DispatchLine)
- **Kestrel Regional Grid Operations Cooperative** (exercises; product:
  RelayLine)
- **Winslow County Emergency Medical Services, Gullwick Harbor
  Pilotage Authority, Sparrowmere Independent News Network, Hazelcombe
  Regional Blood Bank Network, Renfrew Municipal Snow Removal
  Cooperative, Dunbar Ridge Avalanche Forecast Center, Corvale Regional
  Air Ambulance Consortium, Whitmore County Livestock Health
  Cooperative** (practice bank, 8 orgs)

No collision found against either list's distinctive roots. Future
chapters should extend this combined list (Chapters 1-8's 86 orgs plus
this session's 10, for **96 total in this repo**, plus the full
`ai-engineering-for-everyone` list above), not restart it.

## Source verification, done honestly

All 4 externally-fetched sources cited in `lesson.html` (a 5th citation
is an explicitly disclosed local sibling-repo file read, not a web
fetch) were re-verified live this session via `curl -L -o /dev/null -w
"%{http_code}"`, not assumed valid because a prior, interrupted session
had already written the lesson text citing them:

1. Anthropic, "Effective context engineering for AI agents" — re-fetched
   live this session (HTTP 200), cited twice in the lesson for two
   distinct passages (Step 2's tool-schema-budgeting rationale and
   source 4's tool-selection-degradation rationale), both disclosed
   honestly as re-fetched rather than assumed unchanged from any prior
   chapter's own citation of the same URL.
2. OpenAI, "Function calling" (OpenAI Platform documentation) —
   re-fetched live this session (HTTP 200), grounding Step 3's result-
   curation rule ("concise and relevant," not "returning entire objects
   or database results").
3. Anthropic, "Tool use with Claude" (Claude Docs) — re-fetched live this
   session (HTTP 200), grounding Step 1's request-type scoping rule and
   the general claim that a tool's `input_schema` is a recurring, paid
   context cost.
4. `mcp-for-everyone`, `docs/curriculum/CURRICULUM_MAP.md` (local
   repository file, not a web fetch) — re-read directly this session at
   `/home/dell/projects/mcp-for-everyone/docs/curriculum/CURRICULUM_MAP.md`,
   confirming word for word that its own Module 5 (Chapters 9-10) is
   "Permissions, Scopes & Sandboxing" and "Prompt Injection & Tool-Output
   Trust," with no chapter in its 13-chapter roadmap addressing
   tool-schema cost, tool-result curation, or tool-call-history
   budgeting — independent, direct confirmation of the lesson's own
   claim, not a re-use of a prior session's summary.

No citation needed correction or replacement this session — a cleaner
outcome than Chapter 8's own session (two of five corrected) and
consistent with Chapter 7's own clean session, reported here as this
session's own result, not an expectation either way per
`PROJECT_STATE.md`'s own re-verification discipline.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally this session
and confirmed the same installed model as all eight prior chapters
(`llama3.2:latest`). The two live captures embedded in `lesson.html`
(a curated, field-boundary-safe weather-result prompt returning in 65.7
seconds with ~50.4s of cold load, and a raw, field-truncated prompt
returning in 22.8 seconds with the model already resident) were written
into the lesson by the prior, interrupted session and are disclosed in
`lesson.html`'s own "A Note on This Chapter's Live-Testing" section as
that session's own real, unedited data. This session's own connectivity
re-check (`/api/tags` only, no new `/api/chat` capture needed since the
lesson's own two captures were already real, complete, and internally
consistent with the recipe's own claims) confirms the endpoint is
reachable and the installed model is unchanged, consistent with every
prior chapter's own finding that `/api/tags` responds reliably while
`/api/chat` remains intermittently slow. As in every prior chapter, no
graded `solution.py` in this chapter depends on a live call — every
schema-scoping, curation, field-fit, and history-eviction decision in
the automated harnesses is deterministic, hand-computed data, for the
same 20-second-`local_check.sh`-timeout reason documented since Chapter
3. Future sessions should keep budgeting for retries with generous
(120s+) timeouts regardless, as `PROJECT_STATE.md` instructs.

## Code tested before writing

`exercises/solution.py` and `practice/solution.py` were each run for
real this session and produce a perfect score:

```
$ python3 exercises/solution.py   -> TOTAL: 21/21
$ python3 practice/solution.py    -> TOTAL: 8/8
```

`exercises/starter.py` and `practice/starter.py` were each also run for
real (with their TODOs still unfilled) to confirm they fail cleanly with
a readable score report and no traceback, since a learner will run these
files first:

```
$ python3 exercises/starter.py    -> TOTAL: 0/21 (clean, no traceback)
$ python3 practice/starter.py     -> TOTAL: 0/8 (clean, no traceback)
```

`bash scripts/local_check.sh` was run from the repo root at the end of
this session and passed clean (folder structure, placeholder-text scan,
Python syntax, every `solution.py` executed for real, JS syntax and
chapter-path validation, secret scan) — see `PROJECT_STATE.md` and this
session's own commit message for the exact result recorded.
