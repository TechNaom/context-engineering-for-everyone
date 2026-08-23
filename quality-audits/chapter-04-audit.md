# Chapter 4 Quality Audit: Long-Term and Persistent Memory Systems

Session date: 2026-08-23. This audit extends Chapters 1-3's running
fictional-org exclusion list (not restarting it), re-verifies Ollama and
every citation fresh this session, and finally resolves the open
L1/L2 project-ladder judgment call flagged open across Chapters 2 and 3.

## Honest self-critique

**What's strong:**

- The hook (Nightbourne Senior Living Network/HearthLine) demonstrates
  a genuinely distinct failure mode from all three prior chapters on
  purpose: SignalDesk (Ch. 1) had no budget; TriageLine (Ch. 2) had a
  budget shaped for the wrong request type; RouteLine (Ch. 3) had a
  correct budget and a naive within-session eviction mechanism.
  HearthLine got Chapters 1-3 completely right — a real Line 4 budget,
  a correct Chapter 3 short-term policy inside each session — and still
  lost a safety-relevant fact, because nothing decided what should
  survive a session boundary at all. This is precisely the gap Chapter
  4 exists to close, and it is stated as explicitly as Chapter 1's "Why
  This Course Exists" section stated the whole course's boundary
  against `rag-for-everyone` specifically, since persistent storage +
  retrieval is the closest this course has come to that neighbor's
  territory.
- Every number in the lesson's worked-math table and every exercise/
  practice/project number was computed and cross-checked against its
  own dependent scoring code before publishing, not asserted —
  `python3 exercises/solution.py`, `practice/solution.py`, and
  `project/solution.py` all score/pass perfectly when run (see the
  "Code tested before writing" section below for the actual output).
- This chapter introduces a genuinely new mechanic with no Chapter 3
  analog — staleness handling (active/superseded/expired record
  status) — and builds it into every artifact: Exercise 6 (staleness
  resolution), Exercise 8 (naive-append-vs-curated regression gate),
  and the project's own `PERSISTENT_STORE` (two deliberately superseded
  records and one expired record the learner must correctly exclude
  from retrieval regardless of category). This is the one piece of the
  recipe this chapter had to invent rather than adapt from Chapter 3,
  and it is exercised mechanically, not just described in prose.
- Two live Ollama captures were made this session (see below), and one
  is used directly in the lesson as illustrative content that makes the
  chapter's own argument: unlike Chapter 3's capture (which failed to
  follow an exclusion instruction), this session's capture correctly
  followed one — and the lesson is honest that a single success is not
  evidence that instruction-following is now reliable, using both
  chapters' captures together as the actual argument for why write
  criteria and staleness handling are deterministic, rule-based
  decisions in this chapter's own recipe, never delegated to a
  summarization call's judgment.

**Honest gaps:**

- As in Chapter 3, no exercise, practice, or project `solution.py`
  depends on a live model call — every write/retrieval/staleness
  decision in the automated harnesses is deterministic, hand-computed
  data. This remains a disclosed, deliberate judgment call for the same
  reason Chapter 3 gave: `scripts/local_check.sh` runs every
  `solution.py` under a 20-second timeout, and this session's own
  Ollama latencies (21.8s-74.4s) would already be tight against that
  limit even on a good day, let alone a repeat of Chapter 3's
  120-240-second range.
- The persistent store's superseded/expired records in the project
  (`PERSISTENT_STORE`) are hand-authored with clean, unambiguous status
  labels (`status: "superseded"`) rather than derived
  from a system that had to infer staleness from raw disclosed content
  itself.
  Real systems more often face the harder problem of *detecting* that a
  new fact contradicts an old one before either can be marked — this
  chapter's own recipe (Step 4) names that as a real step, but no
  artifact in this chapter actually exercises the *detection* problem,
  only the *policy* problem once staleness is already known. Flagged
  for Chapter 5 or a later revision to consider, if compression/
  extraction work ever needs to build a real staleness-detection
  mechanism rather than assume labeled status.
- Chapter 4's citation set reuses one URL from Chapter 3 (the Claude
  "Context management" blog post) for a different passage than Chapter
  3 quoted from the same page. This was a deliberate choice once the
  page was re-fetched and re-verified live this session (not assumed
  still valid) and confirmed to contain a second, chapter-4-relevant
  passage (the memory-tool section) distinct from Chapter 3's own
  citation of the same page's context-editing section — disclosed
  explicitly in `lesson.html`'s own Sources section, not left implicit.
  A future chapter citing this same page a third time should find fresh
  ground rather than repeat the pattern.
- One of the five sources (AWS Bedrock Agents memory documentation)
  describes a product now in "Classic / maintenance mode," no longer
  open to new customers — disclosed explicitly in both `lesson.html`
  and here rather than silently cited as if current-generation. The
  documented mechanics (session-scoped memory, configurable retention
  duration, automatic summarization) are still real and on-topic, but a
  future revision of this chapter should check whether AWS's successor
  product (Bedrock AgentCore) publishes comparable memory documentation
  that would be a stronger citation.

## The L1/L2 project-ladder decision, finally resolved

Chapters 2 and 3 each shipped a second, module-internal L1 Guided
project rather than the curriculum map's literal "L2 Assisted" tier,
logging this as an open decision both times (see
`quality-audits/chapter-02-audit.md` and
`quality-audits/chapter-03-audit.md`, and `PROJECT_STATE.md`'s "Open
Decisions"). This session resolves it: **Chapter 4 ships the curriculum
map's literal L2 Assisted project once, solo, closing Module 2** —
"Design short-term and long-term memory for a provided long-running
assistant, partial scaffold," exactly as the curriculum map's own
project ladder states.

Reasoning: the curriculum map explicitly ties the L2 tier to "ships
after Ch. 4," the same way it ties L1 to "ships after Ch. 2" and L3 to
"ships after Ch. 8." Chapters 2 and 3 each had a legitimate reason to
add a second L1 project (Module 1 and Module 2's own two labs, one
project per chapter, per the curriculum map's own "Labs" field listing
two labs per module) — but continuing that pattern a third time would
mean Module 2 never actually produces the L2-tier artifact the
curriculum map calls for, silently drifting the whole project ladder
one tier behind its own stated schedule going into Module 3. Chapter
4's own project is also the first one in this course that genuinely
needs to touch two ledger lines at once (Line 3 for the still-open
session, Line 4 for what crosses in from prior sessions) — a "partial
scaffold, Assisted" shape fits that naturally, since it requires
holding two constraints simultaneously rather than the fully guided,
single-constraint shape Chapters 1-3's L1 projects each used. Module 3
onward should treat this as the confirmed convention: **one project per
module, at the project-ladder's own stated tier, not one project per
chapter** — Module 3 (Chapters 5-6) should plan for one L2/L3-tier-
appropriate project shipping once, at the end of Chapter 6, not a
project at the end of each of Chapters 5 and 6 individually. This
closes the question `PROJECT_STATE.md` has carried open since Chapter
2; the next session should not need to re-litigate it.

## Fictional-org exclusion check, extending the running list

Checked against Chapters 1-3's own combined 33-org list (from
`quality-audits/chapter-03-audit.md`: Brackwater Home Internet, Cobalt
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
Vallowmere Grocery Cooperative, Wrayland Behavioral Health Group) and
against `ai-engineering-for-everyone`'s own full compiled exclusion
list (its `quality-audits/chapter-13-audit.md`): Airport, Alderbrook,
Alderwood, Amberglass, Applecross, Ashenvale, Ashford, Barrowfield,
Basilwood, Bellwood, Berkeley, Blackwood, Blythedale, Brackenfield,
Brackwater, Brindlewood, Capstone, Castlebridge, Cedarview, Cobblestone,
Coldwater, Copperfield, Copperlark, Coppervale, Cranmoor, Crowmarsh,
Driftwood, Duskwater, Elmsworth, Faircross, Fairhaven, Fairmont,
Fallowfield, Fenwick, Fernbrook, Foxhaven, Galewood, Gladstone,
Grantham, Grovewell, Halcombe, Harrowgate, Hartwell, Hollowmere,
Hollowridge, Ironwood, Ivywell, Kellbrook, Kestwick, Kettleford,
Larchgate, Larchmoor, Lindenmoor, Loxley, Marlowfield, Marlstone,
Marrowgate, Millbrook, Nettlebrook, Nettlewood, Northaven, Northfield,
Oldfield, Ombervale, Ondermoor, Openfield, Pellham, Pinehaven,
Quillstone, Ravenhollow, Ridgemont, Rosewick, Rutherglen, Saltmere,
Silvergate, Sorrelfield, Stanford, Sunderland, Talbridge, Thistlecombe,
Thorncastle, Thornhollow, Thornwell, Thrumley, Vaultridge, Vellcross,
Vesperfield, Wickmoor, Windale, Windmere, Woodmere, Wrenfield,
Wrensdale, Yarrowfield.

**11 new fictional orgs used this session**, every distinctive root
word checked for zero overlap against both lists above before use:

- **Nightbourne Senior Living Network** (lesson hook; product: HearthLine)
- **Caldermere Home Health Alliance** (exercises; product: CareLine)
- **Underholt Family Medicine Network, Presswick Disability Services
  Cooperative, Dunmere Memory Care Residences, Oxbridge Pediatric Home
  Care, Wetherby Insurance Trust, Camberwell Independent Pharmacy
  Group, Penrose Estate Planning Partners, Rushbrook K-12 Special
  Education Cooperative** (practice bank, 8 orgs)
- **Brightmoor Elder Law Group** (project; product: CaseLine)

No collision found against either list's distinctive roots (checked
prefix-by-prefix, not just whole-word, against every root in both
lists above). Future chapters should extend this combined list
(Chapters 1-3's 33 orgs plus this session's 11, for **44 total in this
repo**, plus the full `ai-engineering-for-everyone` list above), not
restart it.

## Source verification, done honestly

All 5 sources cited in `lesson.html` were fetched and read live this
session via WebFetch, not reused from prior chapters' own citation sets
without re-verifying:

1. Claude (Anthropic), *"Context management on the Claude Developer
   Platform"* — `claude.com/blog/context-management`. Same URL Chapter
   3 cited, re-fetched and re-read live this session rather than
   assumed still valid, and cited here for a different passage: its
   memory-tool section, which states the tool lets Claude "create,
   read, update, and delete files in a dedicated memory directory
   stored in your infrastructure that persists across conversations,"
   letting agents "build up knowledge bases over time" and "maintain
   project state across sessions."
2. LangChain, *"Memory" (LangGraph concepts)* —
   `docs.langchain.com/oss/python/langgraph/memory`. An initial fetch
   attempt at `langchain-ai.github.io/langgraph/concepts/memory/`
   returned only a client-side redirect shell with no readable content;
   this working, current-generation URL was found and fetched
   successfully instead. Confirmed live, with direct quotes on the
   short-term/long-term boundary ("thread-scoped" vs. "shared across
   conversational threads... recalled at any time and in any thread"),
   the semantic/episodic/procedural memory-type taxonomy, hot-path vs.
   background write timing, and an explicit note that "most LLMs still
   perform poorly over long contexts," motivating deliberate forgetting.
3. Letta, *"Memory Blocks"* (blog) — `letta.com/blog/memory-blocks`.
   Fetched successfully; confirmed live with direct evidence that
   memory blocks are "individually persisted in the DB" and, "unlike
   ephemeral memory in many LLM frameworks," maintain state between
   interactions, and that a request's context window is "compiled"
   from existing DB state — direct grounding for treating retrieval as
   a deliberate compile-in step, not a standing presence in context.
4. Google Cloud, Vertex AI Agent Engine, *"Memory Bank"* — the
   originally attempted `cloud.google.com/vertex-ai/...` URL
   301-redirected to `docs.cloud.google.com/vertex-ai/...` this
   session; the redirect target was fetched and confirmed live, with
   direct evidence of long-term fact storage across sessions, a
   "fetch" mechanism for later reintegration, and "memory revisions"
   tracking how a memory changes over time — direct support for this
   chapter's staleness-tracking and scoped-retrieval framing.
5. Amazon Web Services, *"Retain conversational context across multiple
   sessions using memory"* (Bedrock Agents documentation) —
   `docs.aws.amazon.com/bedrock/latest/userguide/agents-memory.html`.
   Fetched successfully and confirmed live, but disclosed honestly as
   describing a product AWS's own page labels "Amazon Bedrock Agents
   (now Amazon Bedrock Agents Classic)," "no longer open to new
   customers," with a successor product (Bedrock AgentCore) referenced
   in its place. Cited anyway because the documented mechanics are
   real and directly on-topic: a configurable memory retention duration
   "between 1 and 365 days" after which session summaries are deleted
   is a concrete, shipped example of Step 4's staleness handling
   implemented as explicit expiration.

Two of five sources required following a live redirect or replacing an
initially attempted URL this session (the LangChain docs URL and the
Google Cloud docs URL), consistent with every prior chapter's own
finding that provider/framework documentation URLs churn between
sessions and must be re-verified, never assumed stable. Two candidate
sources were attempted and dropped before landing on the final five: an
Anthropic memory-tool-specific docs page
(`platform.claude.com/docs/en/build-with-claude/tool-use/memory-tool`)
404'd, and an OpenAI memory guide
(`developers.openai.com/api/docs/guides/memory`) also 404'd; both
`openai.com/index/memory-and-new-controls-for-chatgpt/` and
`help.openai.com/en/articles/8590148-memory-faq` returned HTTP 403 and
were not used. No OpenAI source made it into this chapter's final
five — a real, disclosed change from every prior chapter (which each
included at least one OpenAI citation) — because no live, readable
OpenAI documentation specifically on persistent/long-term memory could
be reached this session, not because one wasn't sought.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally and confirmed
the same installed model as all three prior chapters
(`llama3.2:latest`). `/api/chat` was tested twice this session, and —
unlike Chapter 3's own session, which needed several retries with
escalating timeouts before its first success — both calls succeeded on
the first attempt:

1. A first call (a compression/write-extraction prompt, 150-second
   timeout) returned a real response in **74.4 seconds**, most of which
   was the model's own cold load time in this sandbox.
2. A second, unrelated call a few minutes later (model already warm,
   90-second timeout) returned in **21.8 seconds**.

This is reported honestly as what happened this session, not rounded
into a claim that the earlier intermittent-hang finding no longer
applies — Chapter 3's own session already demonstrated that a
successful warm call can still be followed by a later timeout within
the same session, so two consecutive successes here are one additional
data point, not a reason to relax the standing discipline of budgeting
for retries with generous (120s+) timeouts in future sessions. As in
Chapter 3, no graded `solution.py` in this chapter depends on a live
call, for the same 20-second-`local_check.sh`-timeout reason. The live
capture (the first call above) is used in `lesson.html`'s "A
Live-Captured Write-Extraction Example" section, disclosed as
illustrative, and is notable for correctly following an explicit
exclusion instruction (unlike Chapter 3's own capture, which did not)
— reported honestly as one data point in either direction, not
generalized into a claim that instruction-following is now reliable.

## Code tested before writing

`exercises/solution.py`, `practice/solution.py`, and `project/solution.py`
were each run for real this session and produce a perfect score/pass:

```
$ python3 exercises/solution.py   -> TOTAL: 23/23
$ python3 practice/solution.py    -> TOTAL: 8/8
$ python3 project/solution.py     -> PASS (both self-checks, internally consistent)
```

`exercises/starter.py`, `practice/starter.py`, and `project/starter.py`
were each also run for real (with their TODOs still unfilled) to
confirm they fail cleanly with a readable score/issue report and no
traceback, since a learner will run these files first.

`bash scripts/local_check.sh` was run from the repo root at the end of
this session and passed clean (folder structure, placeholder-text scan,
Python syntax, every `solution.py` executed for real, JS syntax and
chapter-path validation, secret scan).
