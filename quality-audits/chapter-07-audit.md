# Chapter 7 Quality Audit — Multi-Source Context Assembly

Session date: 2026-08-23. This audit extends Chapters 1-6's running
fictional-org exclusion list (not restarting it), re-verifies Ollama and
every citation fresh this session, and confirms this chapter ships no
project of its own, opening Module 4.

Note on session continuity: this chapter's build was interrupted by a
connection error partway through (after `lesson.html`, `quiz.html`, and
`exercises/README.md`/`solution.py`/`starter.py` were already on disk,
mid-way through `exercises/index.html`). This session resumed from that
exact state, verified everything already on disk was correct and
complete before continuing, and finished every remaining artifact
(`exercises/index.html`, the full `practice/` bank, `interview-
questions.md`/`.html`, this audit, registration updates, and
validation) rather than restarting from scratch.

## Honest self-critique

**What's strong:**

- The hook (Hadleworth Metro Water Authority/ConfluenceLine) demonstrates
  a genuinely distinct failure mode from all six prior chapters on
  purpose: every recipe through Chapter 6 is implemented correctly — a
  real budget (Ch. 2), no eviction problem (Ch. 3), nothing to recall
  (Ch. 4), nothing needing compression (Ch. 5), both facts sitting at
  reasonable positions with no lost-in-the-middle risk (Ch. 6) — and the
  system still gives a functionally wrong, hedged answer, because two
  individually correct sources contradicted each other and nothing ever
  decided which should govern. This required deliberately designing a
  scenario where every prior chapter's own recipe succeeds completely
  and the problem only appears once more than one source is combined.
- The Source Assembly Recipe's six steps map directly onto the hook's
  own failure and are each independently testable: inventory, authority
  ranking, contradiction detection, resolution, deduplication, and an
  explicit handoff to Chapter 6's own ordering recipe rather than
  re-deriving it. The three-approach comparison table (naive
  concatenation, string-dedup-only, the full recipe) is grounded
  directly in what ConfluenceLine's actual pipeline did and what each
  alternative would and wouldn't have caught.
- The live-captured example is a genuinely nuanced result, not cherry-
  picked for a clean pass or fail: the model correctly reasoned its way
  to the right authority conclusion in the abstract (trust the live
  status endpoint over the static document) and then gave a concrete
  recommendation that contradicted its own stated conclusion. This is
  used honestly as the lesson's own direct argument for why Step 4's
  resolution has to be a deterministic pipeline decision, not delegated
  to a model's own in-context reasoning, however sound that reasoning
  looks in isolation.
- Every number in the lesson's worked-math table and every exercise/
  practice `solution.py` was computed and cross-checked against its own
  dependent scoring code before publishing, not asserted — both
  `exercises/solution.py` and `practice/solution.py` score a perfect
  total when run (see "Code tested before writing" below for the actual
  output).
- The chapter states explicitly, in its own text, both what it is not
  re-teaching (Chapters 1-6's own recipes, used only as a lens) and what
  it is deliberately deferring to Chapter 8 (retrieval architecture and
  ranking quality itself, `rag-for-everyone`'s subject) — the same
  boundary-setting discipline every prior chapter modeled.

**Honest gaps:**

- As in every prior chapter, no exercise or practice `solution.py`
  depends on a live model call — every authority-rank, contradiction-
  detection, and deduplication decision in the automated harnesses is
  deterministic, hand-computed data. This remains a disclosed, deliberate
  judgment call for the same reason Chapters 3-6 gave:
  `scripts/local_check.sh` runs every `solution.py` under a 20-second
  timeout, well inside this session's own measured Ollama load time
  (~65 seconds cold).
- This chapter's contradiction-detection exercises (Exercise 4, Practice
  Scenario 4) classify clean, hand-labeled claim pairs as contradiction/
  restatement/unrelated, not the harder real-world problem of detecting
  a contradiction or restatement from two pieces of actual natural-
  language source text with no pre-existing label — the same category of
  gap Chapters 5 and 6's own audits flagged for fidelity-checking and
  positional-probing, respectively. A live contradiction-detection
  probe against real model output, scored automatically, is a harder
  problem than this chapter's own artifacts exercise, flagged here for a
  later chapter or revision.
- The lesson's worked-math table (Hadleworth's contradicting advisory)
  uses a single, cleanly-separable authority ranking (live tool output
  strictly outranks a static document for a time-sensitive status claim)
  chosen because it makes the arithmetic and the resolution unambiguous
  for teaching purposes. Real production authority rankings are
  frequently harder — two sources of genuinely comparable authority for
  a given request type, or a ranking that varies by sub-claim within one
  document — and this chapter's own Exercise 8/Practice Scenario 8
  escalation-decision task is the only artifact that directly exercises
  the "no clear winner" case; a future revision could add a second
  worked-math example built around a genuine authority tie to make that
  harder case as concrete as the clean-ranking case already is.
- This chapter's own live capture, while genuinely nuanced (see above),
  is still a single-turn, single-model capture from one session — a
  reader should not conclude every model, every session, or every
  prompt phrasing produces the same "correct reasoning, inconsistent
  action" pattern; the lesson's own closing paragraph on the capture
  states this is "a precise, concrete illustration," not a claim of
  universal model behavior, but a future revision could state that
  scope limitation more explicitly right next to the capture itself,
  the same tightening Chapter 6's own audit flagged for its own capture.

## Chapter 7 ships no project — confirmed, not a silent omission

Per this course's now-confirmed one-project-per-module convention
(established in Chapter 4's session, applied in Chapter 5's session by
deferring to Chapter 6, and honored there), Module 4 (Chapters 7-8)
should ship a single project once, not one per chapter. `lesson.html`'s
own closing "A note on this chapter's project" section and
`interview-questions.md`/`.html`'s matching closing section both state
this explicitly, rather than silently omitting the project section a
reader would expect after Chapters 4 and 6 each shipped one.

`docs/curriculum/CURRICULUM_MAP.md`'s own Module 4 entry lists two labs
covering both chapters together ("assemble context from 3+ real sources
for one request" and "take a retriever's ranked output and produce
well-formed context from it") and a single "multi-source assembly +
retrieval-integration review" assessment — the map itself describes one
combined deliverable spanning both chapters, not a per-chapter project,
consistent with treating Module 4's project as a single artifact shipped
once. Per the project ladder's own numbered tiers (L1 after Ch. 2, L2
after Ch. 4, L3 after Ch. 8, L4 the Ch. 13 capstone), Module 4's project
lands cleanly on the L3 Independent tier already assigned to Chapter 8 —
unlike Module 3's own gap between L2 and L3 (Chapter 6's own audit
resolved that as an unassigned-tier "Module 3 Project"), Module 4 has an
explicit numbered tier waiting for it at Chapter 8, so no honest-
labeling workaround is needed here. **Chapter 7 carries no project.
Chapter 8, closing Module 4, will ship the L3 Independent project,
drawing on both Chapter 7 (source assembly) and Chapter 8 (retrieval
integration) together** — a future session building Chapter 8 should
plan for this explicitly rather than treating Chapter 8's own project as
a Chapter-8-only task wearing a Module 4 label, the same discipline
Chapter 6's session applied to Module 3.

## Fictional-org exclusion check, extending the running list

Checked against Chapters 1-6's own combined 65-org list (from
`quality-audits/chapter-06-audit.md`): Brackwater Home Internet, Cobalt
Home Security, Windermere Legal Services, Pinecrest Veterinary Group,
Solmark Payments, Thistledown Air Cargo, Ravenhollow University
Registrar, Copperfield Home Appliances, Marrowgate Public Library,
Fenwick Outdoor Adventures, Meridian Legal Aid Network, Vantry Health
Network, Corravine Freight, Marrenkirk Insurance Group, Duvane
Utilities Cooperative, Graytide Hospitality Group, Oakspire Home Care
Network, Corundale Media Group, Pallisade Manufacturing, Redcliff
Credit Union, Thackery Regional Exchange, Halveston Regional Health
System, Emberlynn Transit Cooperative, Quarrowstead Legal Aid Partners,
Larkmoth Outdoor Retail, Feldspar Municipal Water Utility, Pemberglen
Veterinary Partners, Sootmarsh Freight Cooperative, Glennoak Wealth
Advisors, Tarnwick Community College, Hushfield Telehealth Network,
Vallowmere Grocery Cooperative, Wrayland Behavioral Health Group,
Nightbourne Senior Living Network, Caldermere Home Health Alliance,
Underholt Family Medicine Network, Presswick Disability Services
Cooperative, Dunmere Memory Care Residences, Oxbridge Pediatric Home
Care, Wetherby Insurance Trust, Camberwell Independent Pharmacy Group,
Penrose Estate Planning Partners, Rushbrook K-12 Special Education
Cooperative, Brightmoor Elder Law Group, Brannigan Home Energy
Services, Kirkholme Public Transit Safety Board, Lynhaven Community
Health Partners, Sablewood Legal Trust, Coalridge Municipal Transit
Authority, Pikestone Logistics Group, Rowancraig Insurance
Underwriters, Draymoor Agricultural Cooperative, Osprey Ridge Wealth
Management, Talmarsh Veterinary Alliance, Marchside Regional Trauma
Network, Calverton Public Defender's Office, Nunroth Independent
Bookstore Cooperative, Vesparro Marine Salvage, Holstead Grain
Exchange, Quenby Historical Archive Society, Farrowline Dairy
Cooperative, Delacroix Regional Airport Authority, Pennwhistle
Community Radio Network, Ostergaard Marine Insurance, Brackholt County
Court Records Office — and against `ai-engineering-for-everyone`'s own
full compiled exclusion list (its `quality-audits/chapter-13-audit.md`,
as reproduced in Chapter 6's own audit): Airport, Alderbrook, Alderwood,
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
Milbrandt, Nordkeep, Calderleigh.

**10 new fictional orgs used this session**, every distinctive root word
checked for zero collision against both lists above via a live grep
across `quality-audits/`, `chapters/`, and this repo's own tracked files
(the `ai-engineering-for-everyone` repo itself is not present locally in
this sandbox, so its own compiled list is checked as reproduced text
above, consistent with how this repo has referenced it since Chapter 1)
before use, which returned zero matches for any of the 10 new roots
below:

- **Hadleworth Metro Water Authority** (lesson hook; product:
  ConfluenceLine)
- **Corrinvale Independent Pharmacy Network** (exercises; product:
  ScriptLine)
- **Juniper Ridge Veterinary Partners, Quarrydale Auto Diagnostics
  Cooperative, Tamworth Regional Housing Trust, Wexford Maritime
  Charter Group, Dovetail Woodcraft Guild, Cinderfield Volunteer Fire
  Network, Barleycroft Grain & Feed Cooperative, Yewmarsh Wildlife
  Sanctuary** (practice bank, 8 orgs)

No collision found against either list's distinctive roots. Future
chapters should extend this combined list (Chapters 1-6's 65 orgs plus
this session's 10, for **75 total in this repo**, plus the full
`ai-engineering-for-everyone` list above), not restart it.

## Source verification, done honestly

All 5 sources cited in `lesson.html` were fetched and read live this
session via WebFetch, not assumed valid from the interrupted prior
session's own draft — every citation was re-verified fresh after the
resumption, since the connection error that interrupted this chapter's
build meant no source had actually been re-confirmed live within this
session before now:

1. Anthropic, *"Effective context engineering for AI agents"* —
   `anthropic.com/engineering/effective-context-engineering-for-ai-agents`.
   Fetched live and confirmed live this session. The exact quoted
   guidance ("keep your context informative, yet tight" across every
   component of context) was confirmed present verbatim in the fetched
   page content.
2. Wang, Feng, Wang, Shi, Balachandran, He, and Tsvetkov, *"Resolving
   Knowledge Conflicts in Large Language Models"* (2023) —
   `arxiv.org/abs/2310.00935`. Fetched live and confirmed live this
   session. Confirmed the paper establishes exactly the three
   desiderata this chapter's Step 4 cites (identify, pinpoint, provide
   distinct viewpoints) and finds LLMs reliably do the first but
   struggle with the second and third unprompted.
3. Xu, Qi, Guo, Wang, Wang, Zhang, and Xu, *"Knowledge Conflicts for
   LLMs: A Survey"* (EMNLP 2024) — `aclanthology.org/2024.emnlp-main.486/`.
   Fetched live and confirmed live this session. Confirmed the paper's
   own taxonomy of three categories (context-memory, inter-context,
   intra-memory conflict), directly supporting this chapter's Step 3
   citation of "inter-context conflict."
4. LangChain, `create_stuff_documents_chain` API reference
   (`langchain-classic`) —
   `reference.langchain.com/python/langchain-classic/chains/combine_documents/stuff/create_stuff_documents_chain`.
   Fetched live and confirmed live this session. Confirmed the function
   formats documents with an optional template and joins them with a
   string separator into one context block — the "stuff" pattern this
   chapter's naive-concatenation comparison-table row cites directly.
5. Microsoft, *"RAG and Generative AI"* (Azure AI Search documentation,
   Microsoft Learn) —
   `learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview`.
   Fetched live and confirmed live this session. The exact quoted text
   ("enterprise content spans SharePoint, databases, blob storage, and
   other platforms. Creating a unified search corpus without disrupting
   data operations is essential," under a "Multi-source data access"
   challenge heading) was confirmed present verbatim in the fetched page
   content, unchanged from the version originally cited before the
   session interruption.

All 5 sources fetched clean this session with no redirects and no dead
links encountered — a genuinely different, less churny outcome than
Chapters 3-6's own sessions, each of which needed to follow at least one
live redirect or replace at least one dead link. Disclosed honestly as
this session's own result, not evidence that documentation URLs have
generally stabilized — future sessions should keep re-verifying rather
than assuming this chapter's own clean result generalizes.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally and confirmed
the same installed model as all six prior chapters (`llama3.2:latest`).
`/api/chat` was tested twice this session (after resumption, to confirm
the endpoint was still reachable following the connection error that
interrupted the earlier part of this build) and succeeded on the first
attempt both times:

1. A first call (a 150-second timeout) returned a real response in
   **64.8 seconds**, almost entirely the model's own cold load time
   (about 60.9 seconds of the total, per the response's own
   `load_duration` field).
2. A second, warm call moments later (a 90-second timeout) returned in
   **10.9 seconds**.

This reconfirms Ollama's availability in this sandbox after the session
interruption; it is a supplementary connectivity check, not a new
substantive capture. `lesson.html`'s own "A Note on This Chapter's
Live-Testing" section documents the chapter's actual, substantive live
capture (the two `/api/chat` calls made before the interruption,
including the on-topic contradiction-resolution prompt used as the
"Live-Captured Contradiction Example" in the lesson body itself,
109 seconds cold / 5.1 seconds warm) — that disclosure is accurate and
unchanged, and this session's supplementary reconfirmation is consistent
with it: two consecutive first-attempt successes, cold-load-dominated
timing, no hang encountered. Future sessions should keep budgeting for
retries with generous (120s+) timeouts regardless, per
`PROJECT_STATE.md`'s standing discipline — Chapter 3's own session
already showed a successful warm call can still be followed by a later
timeout within the same session. As in every prior chapter, no graded
`solution.py` in this chapter depends on a live call, for the same
20-second-`local_check.sh`-timeout reason every prior chapter documented.

## Code tested before writing

`exercises/solution.py` and `practice/solution.py` were each run for
real this session and produce a perfect score:

```
$ python3 exercises/solution.py   -> TOTAL: 28/28
$ python3 practice/solution.py    -> TOTAL: 8/8
```

`exercises/starter.py` and `practice/starter.py` were each also run for
real (with their TODOs still unfilled) to confirm they fail cleanly with
a readable score report and no traceback, since a learner will run these
files first:

```
$ python3 exercises/starter.py    -> TOTAL: 0/28 (clean, no traceback)
$ python3 practice/starter.py     -> TOTAL: 0/8 (clean, no traceback)
```

`bash scripts/local_check.sh` was run from the repo root at the end of
this session — see `PROJECT_STATE.md` and the session's own commit
message for the exact result recorded.
