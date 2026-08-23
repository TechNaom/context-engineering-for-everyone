# Chapter 8 Quality Audit: Retrieval Integration: From Ranked Results to Context

Session summary: this session built Chapter 8 in full, closing Module 4
(Chapters 7-8). Uses Chapters 1-7 as a lens, extends the running
fictional-org exclusion list (not restarting it), re-verifies Ollama and
every citation fresh this session, and ships Module 4's single L3
Independent project (the curriculum map's own literal L3 tier), closing
the module — the task Chapter 7's own session deliberately deferred
here.

## Honest self-critique

**What's strong:**

- The hook (Mossgate Regional Law Library Consortium/CiteLine) isolates
  a genuinely distinct failure mode from Chapter 7's own hook, on
  purpose: retrieval architecture itself — the embedding model, the
  similarity search, the ranking — is correct throughout, and the
  system still gives a confidently wrong answer, because nothing
  between the retriever and the model decided that a chunk cut off
  mid-clause is worse than no chunk at all, or that two adjacent ranked
  chunks were really one continuous passage. This is deliberately not
  Chapter 7's own contradiction-between-sources problem — it's a
  single-source integration problem, one level upstream of where
  Chapter 7's own recipe starts.
- The Retrieval Integration Recipe's six steps map directly onto the
  hook's own failure and are each independently testable: relevance
  floor, boundary-safe budget fit, provenance preservation, adjacent-
  chunk stitching, explicit empty/low-confidence handling, and an
  explicit handoff to Chapter 7's own Source Assembly Recipe rather than
  re-deriving it. The three-approach comparison table (unconditional
  top-k, relevance-floor-only, the full recipe) is grounded directly in
  what CiteLine's actual pipeline did and what each alternative would
  and wouldn't have caught.
- Both live captures this session are genuinely informative, not
  cherry-picked for a clean pass or fail: the first (stitched, correctly
  filtered bundle) produced a clean, correctly cited answer; the second
  (the qualifying clause truncated away, noise present) produced a
  response that avoided confidently misstating the rule but still
  fabricated plausible-sounding reasoning not grounded in anything
  retrieved — a more nuanced failure than a simple wrong answer, used
  honestly in the lesson as a second, distinct argument for why the
  recipe's boundary-safe fit and stitching steps matter even when a
  model doesn't fail as visibly as the hook's own story.
- Every number in the lesson's worked-math table and every exercise/
  practice/project `solution.py` was computed and cross-checked against
  its own dependent scoring code before publishing, not asserted — all
  three score a perfect total when run (see "Code tested before
  writing" below for the actual output).
- The chapter states explicitly, in its own text, both what it is not
  re-teaching (Chapters 1-7's own recipes, used only as a lens, and
  retrieval architecture/chunking/embeddings/ranking quality itself,
  `rag-for-everyone`'s subject) and the precise handoff boundary against
  Chapter 7 (this chapter produces the one well-formed source Chapter
  7's own Step 1 inventory assumes it already has) — the same
  boundary-setting discipline every prior chapter modeled.
- Two of five original citation candidates (a stale LangChain URL that
  308-redirects to a page with no splitter content, and an AWS Bedrock
  relevance-threshold page that returned no fetchable body text) were
  caught during live verification this session and swapped for
  citations that were actually confirmed live with real, quotable
  content (LangChain's current `docs.langchain.com` splitter-integrations
  page, and Google Cloud's Agent Search relevance-threshold
  documentation) rather than left pointing at dead or unverifiable URLs
  — disclosed honestly in the lesson's own sources section rather than
  silently substituted.

**Honest gaps:**

- As in every prior chapter, no exercise, practice, or project
  `solution.py` depends on a live model call — every relevance-floor,
  budget-fit, provenance, and stitching decision in the automated
  harnesses is deterministic, hand-computed data. This remains a
  disclosed, deliberate judgment call for the same reason Chapters 3-7
  gave: `scripts/local_check.sh` runs every `solution.py` under a
  20-second timeout, well inside this session's own measured Ollama load
  time (~54-70 seconds).
- This chapter's boundary-safe-fit exercises (Exercise 4, Scenario 4,
  and the project's own Part 1) use a simple greedy-by-score selection
  rule as the one correct answer. Real production retrieval integration
  sometimes has to choose between a slightly lower-scored chunk that
  completes a stitched group and a slightly higher-scored, unrelated
  chunk that doesn't — this chapter's own worked examples were
  deliberately constructed so the highest-scored chunks are also the
  ones that need stitching, avoiding that harder trade-off, the same
  category of simplification Chapter 7's own audit flagged for its
  clean, unambiguous authority ranking.
- The project's Part 2 resolution (keep all four sources, flag one
  claim as superseded rather than dropping any full source) is one
  reasonable design choice, not the only one a real system might make —
  a stricter design might drop the retrieved document's departure-clause
  content entirely once superseded, trading a smaller token footprint
  for less redundant, less potentially-confusing context. The rubric
  grades against the given design's own internal consistency, not
  against a claim that this is the uniquely correct real-world choice.
- This chapter's own live captures, while genuinely informative (see
  above), are both single-turn, single-model captures from one session
  — a reader should not conclude every model, retriever, or prompt
  phrasing produces the same "confident correct answer when well-formed,
  confident-but-ungrounded reasoning when a clause is missing" pattern;
  a future revision could add a second model or a repeated-trial capture
  to strengthen this claim beyond a single illustrative example, the
  same tightening Chapters 6 and 7's own audits flagged for their own
  captures.

## Module 4 project, shipped — closing the module

Per the one-project-per-module convention and the curriculum map's own
project ladder, Module 4's single project ships this session, at the
end of Chapter 8, as committed in Chapter 7's own audit. Unlike Module
3's own project (which fell in a genuine gap the ladder never assigned a
tier to), Module 4's project lands exactly on the ladder's own literal
**L3 Independent** tier (L1 after Ch. 2, L2 after Ch. 4, L3 after Ch. 8,
L4 the Ch. 13 capstone) — no honest-labeling workaround was needed here.
"Independent" is implemented as no scaffold: `project/starter.py` gives
the full spec and raw data (matching Chapter 6's own L2-adjacent
project's level of spec completeness) but, unlike Chapter 4's own L2
project, no partially-filled template or step-by-step hints beyond the
spec itself — every design decision in both Part 1 (retrieval
integration) and Part 2 (source assembly) is left to the learner. The
project (Quartzfield Regional Public Defender Consortium's BriefLine)
draws on both Chapter 7's Source Assembly Recipe and Chapter 8's own
Retrieval Integration Recipe together, in the correct sequence: Part 1's
own resolved, stitched, provenance-tagged output becomes Part 2's own
`retrieved_document` source, which then has to be reconciled with a
genuinely contradicting live-tool-output source — exactly the two
chapters' own labs stated as a pair in the curriculum map ("assemble
context from 3+ real sources for one request" and "take a retriever's
ranked output and produce well-formed context from it").

## The full, combined fictional-org exclusion list

Reproduced in full so the next session only needs this file, not every
prior audit. Chapters 1-6's 65 orgs plus Chapter 7's 10 orgs (75 total,
already checked with zero collision against `ai-engineering-for-
everyone`'s own compiled list): Airport, Alderbrook, Alderwood,
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
Milbrandt, Nordkeep, Calderleigh — plus, as full organization names used
directly by this repo through Chapter 6: Utilities Cooperative, Graytide
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
Records Office — plus Chapter 7's own 10: Hadleworth Metro Water
Authority, Corrinvale Independent Pharmacy Network, Juniper Ridge
Veterinary Partners, Quarrydale Auto Diagnostics Cooperative, Tamworth
Regional Housing Trust, Wexford Maritime Charter Group, Dovetail
Woodcraft Guild, Cinderfield Volunteer Fire Network, Barleycroft Grain &
Feed Cooperative, Yewmarsh Wildlife Sanctuary — and against
`ai-engineering-for-everyone`'s own full compiled exclusion list (its
`quality-audits/chapter-13-audit.md`, as reproduced since Chapter 6's
own audit): the same root-word list reproduced above (Airport through
Calderleigh) is shared verbatim between the two lists as previously
cross-checked; no new fetch of that repo was needed this session since
it is not present locally in this sandbox, consistent with how this
repo has referenced it since Chapter 1.

**11 new fictional orgs used this session**, every distinctive root word
(Moss, Cobalt, Harbor, Aspen, Beacon, Slate, Timber, Garnet, Poplar,
Otter, Quartz) checked for zero collision against both lists above via a
live grep across `quality-audits/`, `chapters/`, and this repo's own
tracked files before use, which returned zero matches for any of the 11
new roots below:

- **Mossgate Regional Law Library Consortium** (lesson hook; product:
  CiteLine)
- **Cobalt Ridge Claims Adjustment Bureau** (exercises; product:
  DossierLine)
- **Harborlight Maritime Archive Society, Aspenfield Community College
  Library, Beacon Crest Genealogy Society, Slatebrook Patent Research
  Group, Timberline Structural Engineering Archive, Garnet Valley
  Genetic Testing Registry, Poplar Crossing School District Archive,
  Otterbend Wildlife Research Station** (practice bank, 8 orgs)
- **Quartzfield Regional Public Defender Consortium** (Module 4
  project; product: BriefLine)

No collision found against either list's distinctive roots. Future
chapters should extend this combined list (Chapters 1-7's 75 orgs plus
this session's 11, for **86 total in this repo**, plus the full
`ai-engineering-for-everyone` list above), not restart it.

## Source verification, done honestly

All 5 sources cited in `lesson.html` were fetched and read live this
session via WebFetch/WebSearch, not assumed valid from any prior
chapter's own draft:

1. Anthropic, "Effective context engineering for AI agents" — re-fetched
   live and confirmed live; the exact "smallest possible set of
   high-signal tokens" quote was verified present, word for word, before
   citing it.
2. LangChain, text-splitter documentation — the historically-expected
   URL (`python.langchain.com/docs/how_to/recursive_text_splitter/`)
   308-redirects to a different page (`docs.langchain.com/oss/python/
   langchain/overview`) with no splitter content at all. This was caught
   during live verification, not assumed still valid, and the citation
   was swapped to the current working page
   (`docs.langchain.com/oss/python/integrations/splitters`), fetched
   live and confirmed to contain the actual quoted guidance
   ("for most use cases, start with the `RecursiveCharacterTextSplitter`").
   Disclosed honestly in the lesson's own sources list rather than
   left pointing at a dead redirect.
3. Google Cloud, "Filter searches by document-level relevance" (Agent
   Search documentation) — this replaced an originally-planned Amazon
   Bedrock Knowledge Bases relevance-threshold citation, which returned
   only a bare page title with no fetchable body text via WebFetch and
   could not be verified as making the specific claim needed. Rather
   than cite an unverified page, a WebSearch located this Google Cloud
   page, which was fetched live and confirmed to state the exact
   HIGH/MEDIUM/LOW/LOWEST relevance-threshold behavior cited.
4. Microsoft, "Chunk documents" (Azure AI Search documentation) —
   fetched live and confirmed live; the specific 512-token/25%-overlap
   recommendation and "smoother transitions between chunks" language
   quoted in the lesson were verified present in the actual fetched
   content, not recalled from a prior session.
5. Pinecone, "Chunking Strategies for LLM Applications" — fetched live
   and confirmed live. The original planned quote ("sentences might end
   up being split") was not actually present in the live-fetched
   content; the citation text was corrected to the claim the page
   actually makes ("if our chunks are too small or too large, it may
   lead to imprecise search results or missed opportunities to surface
   relevant content"), disclosed honestly in the lesson's own citation
   text rather than over-stated.

Two of five original citation candidates needed live-verification-driven
correction this session (see "What's strong" above) — a stricter
citation-discipline outcome than Chapter 7's own session, which found
all 5 of its citations clean with zero issues. This is reported here as
this session's own, less clean result, not a claim that verification
failures are rare — exactly the discipline `PROJECT_STATE.md` requires.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally and confirmed
the same installed model as all seven prior chapters
(`llama3.2:latest`). `/api/chat` was called twice this session and
succeeded on the first attempt both times:

1. The first call (the hook's own stitched, correctly-filtered
   Excerpt 1+2 legal-research prompt, a 200-second timeout) returned a
   real response in **54.1 seconds**, with about 19.6 seconds of that
   spent on the model's own cold load.
2. A second call minutes later (the truncated-clause, noise-present
   prompt, a 150-second timeout) returned in **69.9 seconds**, with its
   own reported load time only about 0.6 seconds — the model was already
   resident; the longer wall-clock time came from generation itself, not
   a reload.

Both results are reported honestly as this session's own data point,
consistent with Chapters 4-7's own two-consecutive-first-attempt-
successes pattern, but not a claim the intermittent hang documented in
Chapter 3 is permanently resolved. Future sessions should keep budgeting
for retries with generous (120s+) timeouts regardless. As in every prior
chapter, no graded `solution.py` in this chapter depends on a live call
— every relevance-floor, budget-fit, provenance, and stitching decision
in the automated harnesses is deterministic, hand-computed data, for the
same 20-second-`local_check.sh`-timeout reason documented since Chapter
3. Both live captures in `lesson.html` are real and unedited, used as
illustrative content this chapter's own argument depends on, not as
something any graded script requires to pass.

## Code tested before writing

`exercises/solution.py`, `practice/solution.py`, and `project/
solution.py` were each run for real this session and produce a perfect
score:

```
$ python3 exercises/solution.py   -> TOTAL: 21/21
$ python3 practice/solution.py    -> TOTAL: 8/8
$ python3 project/solution.py     -> PASS (all self-checks clean; 28/28 per RUBRIC.md)
```

`exercises/starter.py`, `practice/starter.py`, and `project/starter.py`
were each also run for real (with their TODOs still unfilled) to confirm
they fail cleanly with a readable score report and no traceback, since a
learner will run these files first:

```
$ python3 exercises/starter.py    -> TOTAL: 0/21 (clean, no traceback)
$ python3 practice/starter.py     -> TOTAL: 0/8 (clean, no traceback)
$ python3 project/starter.py      -> 8 issues found (clean, no traceback)
```

`bash scripts/local_check.sh` was run from the repo root at the end of
this session — see `PROJECT_STATE.md` and this session's own commit
message for the exact result recorded.
