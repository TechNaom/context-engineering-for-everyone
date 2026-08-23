# Chapter 5 Quality Audit — Context Compression and Summarization

Session date: 2026-08-23. This audit extends Chapters 1-4's running
fictional-org exclusion list (not restarting it), re-verifies Ollama
and every citation fresh this session, and confirms the
one-project-per-module convention holds for Chapter 5 (no chapter
project this time; Module 3's single project ships at the end of
Chapter 6).

## Honest self-critique

**What's strong:**

- The hook (Brannigan Home Energy Services/GridLine) demonstrates a
  genuinely distinct failure mode from all four prior chapters on
  purpose: SignalDesk (Ch. 1) had no budget; TriageLine (Ch. 2) had a
  budget shaped for the wrong request type; RouteLine (Ch. 3) had a
  correct budget and a naive within-session eviction mechanism;
  HearthLine (Ch. 4) got Chapters 1-3 right and lost a fact at a
  session boundary nothing was watching. GridLine got Chapters 1-4
  completely right — a real budget, a real Chapter 3 trigger and
  pin/summary/window shape, a real Chapter 4 write/retrieval policy —
  and still lost a load-bearing detail *inside the compression call
  itself*, because Chapter 3's own recipe named "compress, don't
  truncate" as a step without specifying the compression call's actual
  decision procedure. This is precisely the gap this chapter exists to
  close, and the lesson states the boundary against `rag-for-everyone`
  explicitly (chunking source documents ahead of retrieval vs.
  compressing content already inside a request's context), the same
  discipline every prior chapter's own lesson modeled.
- The failure case is deliberately chosen to be distinct from both
  Chapter 3's pinning and Chapter 4's write criteria: the dropped
  detail (a cross-turn correlation between meter resets and furnace
  timing) is real and load-bearing but was never individually
  pin-worthy (not a single discrete safety fact) or write-worthy (no
  cross-session value). This closes a gap the lesson itself names —
  content that matters collectively across turns within one session but
  has no existing mechanism protecting it — rather than re-describing
  Chapter 3's or Chapter 4's own subject with new vocabulary.
- Every number in the lesson's worked-math table and every exercise/
  practice number was computed and cross-checked against its own
  dependent scoring code before publishing, not asserted —
  `python3 exercises/solution.py` and `practice/solution.py` both
  score/pass perfectly when run (see "Code tested before writing"
  below for the actual output).
- Two live Ollama captures were made this session (see below), and one
  is used directly in the lesson as illustrative content that makes the
  chapter's own argument: the model excluded a literal PIN value it was
  told to exclude, but still described the excluded fact's shape ("a
  4-digit account number"). This is used honestly as a real, concrete
  instance of the "decontextualization" pattern named in this chapter's
  own fifth citation, not dismissed as an unrelated quirk, and it
  directly motivates why Step 6's fidelity check has to be built
  against an explicit candidate list (including what must NOT leak, not
  only what must be kept) rather than trusting a single prompt
  instruction.

**Honest gaps:**

- As in every prior chapter, no exercise or practice `solution.py`
  depends on a live model call — every candidate-extraction and
  fidelity-check decision in the automated harnesses is deterministic,
  hand-computed data. This remains a disclosed, deliberate judgment
  call for the same reason Chapters 3 and 4 gave:
  `scripts/local_check.sh` runs every `solution.py` under a
  20-second timeout, well inside some of this course's own previously
  observed Ollama wait times (Chapter 3's session saw waits as long as
  180-240 seconds).
- The exercise and practice fidelity-check tasks (Exercise 5, Practice
  Scenario 4) use hand-authored candidate and summary-content sets with
  clean, unambiguous string tokens (`"route_38"`, `"maintenance_bay_12"`)
  rather than deriving "does this candidate appear in this summary"
  from real natural-language text, which is a genuinely harder matching
  problem (paraphrase, partial mentions, synonyms) than exact set
  membership. This chapter's own recipe (Step 6) names fidelity
  validation as a real step, but no artifact in this chapter actually
  exercises the harder natural-language matching problem, only the
  policy problem once candidate presence is already reducible to clean
  tokens. Flagged for a later chapter or revision, the same way Chapter
  4's audit flagged staleness *detection* (vs. staleness *policy*) as
  an open gap.
- This chapter's own live capture (the PIN example) is a genuinely
  small, low-stakes illustration of decontextualization — a strong
  pedagogical example precisely because it's easy to verify by eye, but
  a reader should not conclude every real fidelity failure will be this
  easy to spot; the lesson says this directly but the point is worth
  restating here for anyone auditing the chapter's own rigor.
- Two of this session's five citations required following a live
  redirect (the OpenAI Cookbook URL) and one required moving past a
  Google Cloud caching-focused page to the more directly relevant
  `ai.google.dev/gemini-api/docs/long-context` page instead — disclosed
  in full below, consistent with every prior chapter's own finding that
  documentation URLs churn and must be re-verified per session, not
  assumed stable from a prior chapter's citation set (this chapter cites
  none of Chapters 1-4's own five URLs, a clean break rather than a
  reused-URL pattern).

## No chapter project this session — confirmed, not an oversight

Per the now-confirmed one-project-per-module convention (established in
`quality-audits/chapter-04-audit.md` and restated in
`PROJECT_STATE.md`'s "Open Decisions" and `AI_HANDOFF.md`'s "What NOT to
change"), Module 3 (Chapters 5-6) ships a single project once, at the
end of Chapter 6, not a project at the end of each chapter. This
session's own read of `PROJECT_STATE.md`'s "Next Recommended Task" and
`docs/curriculum/CURRICULUM_MAP.md`'s Module 3 entry confirms this
directly: the curriculum map lists two labs under Module 3 as a whole
("build a summarization pipeline that preserves load-bearing facts;
reorder a context window to fix a lost-in-the-middle failure"), not one
lab per chapter, and its own project ladder ties the next tier to a
later chapter rather than Chapter 5 specifically. Chapter 5 therefore
has no `project/` directory and its own `interview-questions.html` says
so explicitly in a closing note, rather than silently omitting the
section a reader would otherwise expect after four straight chapters
that each had one. What replaces a project this chapter: the same
worked-math table (GridLine's dropped correlation across three
approaches) and the eight production-gear exercises/practice scenarios
that exercise the full Compression Fidelity Recipe mechanically, just
without a single larger scored artifact tying them together — Chapter 6
is where that larger artifact ships, and it needs to be built to cover
both chapters' material (compression mechanics from this chapter,
lost-in-the-middle ordering from its own), not just its own chapter's
content in isolation.

## Fictional-org exclusion check, extending the running list

Checked against Chapters 1-4's own combined 44-org list (from
`quality-audits/chapter-04-audit.md`): Brackwater Home Internet, Cobalt
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
Cooperative, Brightmoor Elder Law Group — and against
`ai-engineering-for-everyone`'s own full compiled exclusion list (its
`quality-audits/chapter-13-audit.md`): Airport, Alderbrook, Alderwood,
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

**10 new fictional orgs used this session**, every distinctive root
word checked for zero overlap against both lists above before use (also
verified with a live grep across `quality-audits/`, `chapters/`, and
`ai-engineering-for-everyone`'s own audit file, which returned zero
matches for any of the 10 new roots below):

- **Brannigan Home Energy Services** (lesson hook; product: GridLine)
- **Kirkholme Public Transit Safety Board** (exercises; product: TransitLine)
- **Lynhaven Community Health Partners, Sablewood Legal Trust,
  Coalridge Municipal Transit Authority, Pikestone Logistics Group,
  Rowancraig Insurance Underwriters, Draymoor Agricultural
  Cooperative, Osprey Ridge Wealth Management, Talmarsh Veterinary
  Alliance** (practice bank, 8 orgs)

No collision found against either list's distinctive roots. Future
chapters should extend this combined list (Chapters 1-4's 44 orgs plus
this session's 10, for **54 total in this repo**, plus the full
`ai-engineering-for-everyone` list above), not restart it.

## Source verification, done honestly

All 5 sources cited in `lesson.html` were fetched and read live this
session via WebFetch, not reused from any prior chapter's own citation
set:

1. Anthropic, *"Effective context engineering for AI agents"* —
   `anthropic.com/engineering/effective-context-engineering-for-ai-agents`.
   Fetched successfully and confirmed live. Its "Compaction" section
   states that an agent "preserves architectural decisions, unresolved
   bugs, and implementation details" while "discarding redundant tool
   outputs or messages" — direct grounding for this chapter's Step 1
   (exempt/preserve categories) and the general selective-compression
   principle. This URL is a different one than any of Chapters 1-4 cited
   (Chapter 1 cited the same underlying source but under its older
   `claude.com/blog` path in a prior session; this session's own fetch
   used the current `anthropic.com/engineering/...` URL directly, not
   assumed carried over).
2. OpenAI, *"Summarizing long documents"* (Cookbook) — the originally
   attempted `cookbook.openai.com/examples/summarizing_long_documents`
   URL 308-redirected to
   `developers.openai.com/cookbook/examples/summarizing_long_documents`
   this session; the redirect target was fetched and confirmed live.
   Documents a chunk-based approach where "by controlling the number of
   text chunks and their sizes, we can ultimately control the level of
   detail in the output," with an explicit `detail` parameter and an
   optional recursive mode — direct support for this chapter's Step 4
   (an explicit, tunable compression target).
3. LangChain, *"Short-term memory"* —
   `docs.langchain.com/oss/python/langchain/short-term-memory`. Fetched
   successfully and confirmed live. States that "the problem with
   trimming or removing messages... is that you may lose information
   from culling of the message queue," motivating "a more sophisticated
   approach of summarizing the message history using a chat model" —
   direct grounding for treating summarization as strictly different
   from truncation.
4. Google, *"Long context"* (Gemini API docs) —
   `ai.google.dev/gemini-api/docs/long-context`. Fetched successfully
   and confirmed live. An initial search also surfaced a Google Cloud
   context-caching page as a candidate; it was set aside in favor of
   this page because it speaks more directly to compression itself
   ("the more limited context windows common in many other models often
   require strategies like arbitrarily dropping old messages,
   summarizing content... or filtering prompts to save tokens") rather
   than primarily to caching economics — used honestly in this
   chapter's own architect-level interview question to argue that a
   large context window changes, but doesn't eliminate, the case for
   compression.
5. Anonymous authors (arXiv preprint), *"When Summaries Distort
   Decisions: Information Fidelity in LLM-Compressed Financial
   Analysis"* — `arxiv.org/abs/2606.29251`. Fetched successfully and
   confirmed live. States "compression loses fidelity when it changes
   the decision induced by the source," and names
   "decontextualization" — "salient evidence is retained but separated
   from the caveats and contextual qualifiers needed for correct
   interpretation" — as a specific failure pattern. Disclosed honestly:
   this is a preprint (arXiv, not a peer-reviewed venue or vendor
   documentation), the first non-vendor-documentation, non-established-
   paper citation this course has used since Chapter 1's Liu et al.
   "Lost in the Middle" citation; it was selected because its central
   finding (fidelity loss can hide behind fluent, individually-accurate
   output) is directly and concretely on this chapter's own topic, not
   because it carries the same institutional weight as a
   multiply-cited, multi-year-old paper like Liu et al. A future
   revision of this chapter should re-check whether this preprint has
   been published, revised, or superseded, the same forward-looking
   check already flagged for the Liu et al. citation in
   `PROJECT_STATE.md`'s Known Issues.

No source from Chapters 1-4's own five-citation sets was reused this
session, even for a different passage (the pattern Chapter 4 used once
for the Claude "Context management" blog post) — a clean break, not a
gap, since fresh, directly-relevant ground was available on this
chapter's own topic.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally and confirmed
the same installed model as all four prior chapters
(`llama3.2:latest`). `/api/chat` was tested twice this session and
succeeded on the first attempt both times — consistent with Chapter 4's
session, not Chapter 3's, but reported honestly as this session's own
result, not a claim the earlier intermittent hang is resolved:

1. A first call (a compression prompt with an explicit exclusion
   instruction, 200-second timeout) returned a real response in
   **64 seconds**, most of which was the model's own cold load time in
   this sandbox.
2. A second, unrelated call a few minutes later (model already warm,
   200-second timeout) returned in **8 seconds**.

Future sessions should keep budgeting for retries with generous
(120s+) timeouts regardless, exactly as `PROJECT_STATE.md` instructs —
Chapter 3's own session already demonstrated that a successful warm
call can still be followed by a later timeout within the same session,
so two consecutive successes here (following two consecutive successes
in Chapter 4's own session) are additional data points, not a reason to
relax the standing discipline. As in every prior chapter, no graded
`solution.py` in this chapter depends on a live call, for the same
20-second-`local_check.sh`-timeout reason. The live capture (the first
call above) is used in `lesson.html`'s "A Live-Captured Compression
Example" section, disclosed as illustrative, and is notable for a
nuanced partial result: the literal excluded value (a PIN) never
appears, but the response still describes the excluded fact's shape ("a
4-digit account number") — read honestly in the lesson as a small, real
instance of the decontextualization pattern named in this chapter's
fifth citation, not as either a full pass or a full failure of
instruction-following.

## Code tested before writing

`exercises/solution.py` and `practice/solution.py` were each run for
real this session and produce a perfect score:

```
$ python3 exercises/solution.py   -> TOTAL: 26/26
$ python3 practice/solution.py    -> TOTAL: 8/8
```

`exercises/starter.py` and `practice/starter.py` were each also run for
real (with their TODOs still unfilled) to confirm they fail cleanly
with a readable score report and no traceback, since a learner will run
these files first:

```
$ python3 exercises/starter.py    -> TOTAL: 0/26 (clean, no traceback)
$ python3 practice/starter.py     -> TOTAL: 0/8 (clean, no traceback)
```

`bash scripts/local_check.sh` was run from the repo root at the end of
this session and passed clean (folder structure, placeholder-text scan,
Python syntax, every `solution.py` executed for real, JS syntax and
chapter-path validation, secret scan).
