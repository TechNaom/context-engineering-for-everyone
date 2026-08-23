# Chapter 3 Quality Audit: Short-Term Conversational Memory

Session date: 2026-08-23. This audit extends Chapters 1-2's running
fictional-org exclusion list (not restarting it) and re-verifies Ollama
and every citation fresh this session, per this repo's own standing
discipline.

## Honest self-critique

**What's strong:**

- The hook (Emberlynn Transit Cooperative/RouteLine) demonstrates a
  genuinely distinct failure mode from both prior chapters on purpose:
  Chapter 1's SignalDesk had no budget at all; Chapter 2's TriageLine
  had a budget sized for the wrong request-type shape; RouteLine has a
  *correctly derived* Line 3 budget (8,680 tokens, via Chapter 2's own
  recipe) and a working eviction mechanism — the gap is a missing
  *policy* layer that decides what survives eviction by anything other
  than recency. This is precisely the gap Chapter 3 exists to close.
- Every number in the lesson's worked-math table (RouteLine's 16-turn
  conversation, the naive-FIFO suffix-sum calculation, the hybrid
  policy's 8,310-token package) is real, computed arithmetic, verified
  by hand and cross-checked against the exercises' own
  `_cumulative()`/suffix-sum logic before publishing — not asserted.
  `python3 exercises/solution.py`, `practice/solution.py`, and
  `project/solution.py` all score/pass perfectly when run.
- This is the first chapter in this course to actually capture live
  model output. Ollama's `/api/chat` endpoint responded successfully
  twice this session after multiple timeouts (see the Ollama section
  below), and the resulting live, unedited transcript is used directly
  in the lesson's "A Live-Captured Compression Example" section. The
  transcript's own imperfection (the model did not follow an explicit
  instruction to omit a specific fact) was disclosed honestly and
  turned into the lesson's own argument for why pinning is implemented
  as a separate, deterministic mechanism rather than trusted to a
  summarization call's instruction-following — a real finding used
  honestly, not smoothed over or discarded because it was inconvenient
  for a clean example.
- The project's self-check follows Chapter 2's mechanical-plus-judgment
  shape: required/forbidden pin categories and the budget-fit
  constraint are fully mechanically checked against the learner's own
  numbers; only the two administrative facts' pin status and the
  quality of both write-ups are judgment-graded, and this is disclosed
  explicitly in both `project/README.md` and `RUBRIC.md`.

**Honest gaps:**

- No exercise, practice, or project `solution.py` in this chapter
  depends on a live model call — every summarization/compression step
  in the automated harnesses is deterministic, hand-computed data (a
  fixed `SUMMARY_TOKENS` reserve, not an actual LLM call). This is a
  disclosed, deliberate judgment call: `scripts/local_check.sh` runs
  every `solution.py` under a 20-second timeout, and this session's own
  measured Ollama latencies ranged from 8.7 seconds (warm) to over two
  minutes (cold) with intermittent hangs even after a successful warm
  call — see the Ollama section below. Wiring a live call into the
  graded harness under those conditions would make the automated
  checks themselves flaky, which this repository's own standing
  discipline (every check should pass cleanly and repeatably) weighs
  against. The live capture is real and used in the lesson as
  illustrative content, clearly labeled as such, not as a load-bearing
  dependency of any graded script — flagged here as a boundary a future
  chapter (Chapter 5, which owns compression/summarization in full
  depth) should reconsider, especially if a documented hosted-provider
  swap removes the latency variance entirely.
- The project's conversation data (16 turns, 6 candidate facts) is
  hand-authored to produce a clean, feasible reference solution (a
  12-turn verbatim window, 245 pinned tokens, and a 7,225-token total
  package against the 7,500-token budget) rather than sampled from a
  real system's logs, the same necessary limitation Chapters 1-2's
  hand-authored scenario data already carried and disclosed.
- Chapter 3 continues Module 1's one-project-per-chapter pattern (a
  second real L1 Guided project, per Chapter 2's own logged judgment
  call in `quality-audits/chapter-02-audit.md` and
  `PROJECT_STATE.md`'s "Open Decisions") rather than waiting for
  Module 2's "L2 Assisted" tier, which the curriculum map ties to
  Chapter 4 specifically. This continues to be a judgment call, not a
  confirmed ecosystem convention — Chapter 4's own session should
  re-confirm whether its project ships as this module's single L2
  Assisted project (as the curriculum map's project ladder literally
  states) or as a second L1-tier project matching this chapter's own
  choice, before assuming either default.
- The MemGPT paper (source 3) is cited for its virtual-context-
  management framing, not its specific benchmark results — appropriate
  for this chapter's conceptual point about tiered memory, but Chapter
  4 (which owns long-term/persistent memory in depth) should not assume
  this citation covers retrieval-quality claims it doesn't make.

## Fictional-org exclusion check, extending the running list

Checked against Chapters 1-2's own combined 22-org list (from
`quality-audits/chapter-02-audit.md`: Brackwater Home Internet, Cobalt
Home Security, Windermere Legal Services, Pinecrest Veterinary Group,
Solmark Payments, Thistledown Air Cargo, Ravenhollow University
Registrar, Copperfield Home Appliances, Marrowgate Public Library,
Fenwick Outdoor Adventures, Meridian Legal Aid Network, Vantry Health
Network, Corravine Freight, Marrenkirk Insurance Group, Duvane
Utilities Cooperative, Graytide Hospitality Group, Oakspire Home Care
Network, Corundale Media Group, Pallisade Manufacturing, Redcliff
Credit Union, Thackery Regional Exchange, Halveston Regional Health
System) and against `ai-engineering-for-everyone`'s own full compiled
exclusion list (its `quality-audits/chapter-13-audit.md`): Airport,
Alderbrook, Alderwood, Amberglass, Applecross, Ashenvale, Ashford,
Barrowfield, Basilwood, Bellwood, Berkeley, Blackwood, Blythedale,
Brackenfield, Brackwater, Brindlewood, Capstone, Castlebridge,
Cedarview, Cobblestone, Coldwater, Copperfield, Copperlark, Coppervale,
Cranmoor, Crowmarsh, Driftwood, Duskwater, Elmsworth, Faircross,
Fairhaven, Fairmont, Fallowfield, Fenwick, Fernbrook, Foxhaven,
Galewood, Gladstone, Grantham, Grovewell, Halcombe, Harrowgate,
Hartwell, Hollowmere, Hollowridge, Ironwood, Ivywell, Kellbrook,
Kestwick, Kettleford, Larchgate, Larchmoor, Lindenmoor, Loxley,
Marlowfield, Marlstone, Marrowgate, Millbrook, Nettlebrook, Nettlewood,
Northaven, Northfield, Oldfield, Ombervale, Ondermoor, Openfield,
Pellham, Pinehaven, Quillstone, Ravenhollow, Ridgemont, Rosewick,
Rutherglen, Saltmere, Silvergate, Sorrelfield, Stanford, Sunderland,
Talbridge, Thistlecombe, Thorncastle, Thornhollow, Thornwell, Thrumley,
Vaultridge, Vellcross, Vesperfield, Wickmoor, Windale, Windmere,
Woodmere, Wrenfield, Wrensdale, Yarrowfield (plus this course's own
Cobalt, Pinecrest, Solmark, Thistledown, Meridian, Vantry, Corravine,
Marrenkirk, Duvane, Graytide, Oakspire, Corundale, Pallisade, Redcliff,
Thackery, Halveston, already distinct from the pattern above).

**11 new fictional orgs used this session**, every distinctive root
word checked for zero overlap against both lists above before use:

- **Emberlynn Transit Cooperative** (lesson hook; product: RouteLine)
- **Quarrowstead Legal Aid Partners** (exercises; product: DocketLine)
- **Larkmoth Outdoor Retail, Feldspar Municipal Water Utility,
  Pemberglen Veterinary Partners, Sootmarsh Freight Cooperative,
  Glennoak Wealth Advisors, Tarnwick Community College, Hushfield
  Telehealth Network, Vallowmere Grocery Cooperative** (practice bank,
  8 orgs)
- **Wrayland Behavioral Health Group** (project; product: SupportLine)

No collision found against either list's distinctive roots (checked
prefix-by-prefix, not just whole-word, against every root in both
lists above). Future chapters should extend this combined list
(Chapters 1-2's 22 orgs plus this session's 11, for 33 total in this
repo, plus the full `ai-engineering-for-everyone` list above), not
restart it.

## Source verification, done honestly

All 5 sources cited in `lesson.html` were fetched and read live this
session via WebFetch, not reused from Chapters 1-2's own citation sets
without re-verifying:

1. Claude (Anthropic), *"Context management on the Claude Developer
   Platform"* — the historical `anthropic.com/news/context-management`
   URL 308-redirected to `claude.com/blog/context-management` this
   session; the redirect target was fetched and confirmed live, with
   direct quotes on automatic clearing of "stale tool calls and
   results" and a memory tool that lets a system "save critical
   information to memory ... and bring that learning across successive
   agentic sessions."
2. Claude Docs, *"Context editing"* — fetched successfully at
   `platform.claude.com/docs/en/build-with-claude/context-editing`
   (also attempted at an older `claude.com/docs/...` path first, which
   404'd; the working `platform.claude.com` path was used instead,
   consistent with Chapter 2's own finding that this provider's
   documentation URLs churn between sessions). Confirmed live, with a
   real, shipped `trigger`/`keep`/`exclude_tools` configuration this
   chapter's own recipe steps are directly grounded in.
3. Packer et al., *"MemGPT: Towards LLMs as Operating Systems"* (arXiv)
   — fetched successfully at `arxiv.org/abs/2310.08560`; confirmed the
   "virtual context management" framing and its explicit analogy to
   "hierarchical memory systems in traditional operating systems."
4. OpenAI, *"Conversation state"* guide — the historical
   `platform.openai.com/docs/guides/conversation-state` URL
   301-redirected to
   `developers.openai.com/api/docs/guides/conversation-state` this
   session; confirmed live, with direct evidence that context-window
   and output-token limits both grow more pressing "as conversations
   extend."
5. Google, *Gemini API, "Text generation"* — fetched successfully at
   `ai.google.dev/gemini-api/docs/text-generation` (the previously
   planned `ai.google.dev/gemini-api/docs/chat` URL 404'd this session
   and was not used); confirmed live, with direct evidence that a
   caller can operate in "stateless mode" and must "maintain the
   conversation history" as a client-side array — direct support for
   this chapter's premise that conversation-history management is
   frequently the application's own responsibility, not a provider
   safety net.

Two of five sources required following a live redirect this session,
and two source URLs originally planned (`python.langchain.com/docs/
how_to/trim_messages`, redirected to a generic overview page with no
relevant content, and `ai.google.dev/gemini-api/docs/chat`, 404) were
dropped in favor of working, on-topic replacements found live during
this same session, rather than cited from a stale or dead URL. All of
this is disclosed directly in `lesson.html`'s own Sources section for
the two sources that did redirect, not just here.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally and
confirmed the same installed model as Chapters 1-2 (`llama3.2:latest`).
Unlike both prior chapters, `/api/chat` was tested repeatedly this
session with escalating patience, per `PROJECT_STATE.md`'s own
instruction to retry with an even more patient timeout than Chapter
2's 75 seconds before concluding it's unreachable — and the results
were genuinely mixed, disclosed honestly rather than rounded up to a
clean "it works now":

1. A 120-second attempt (a plain "Say OK" prompt) did not return.
2. A 180-second attempt on the same prompt succeeded, returning a real
   response after ~153 seconds, ~138 of which was model load time.
3. An immediate follow-up call, with the model already warm, returned
   in ~11.5 seconds.
4. A later call (the RouteLine compression example used in the lesson)
   then timed out twice more, at 60 and 150 seconds, before succeeding
   on a third attempt at a 240-second timeout — in 8.7 seconds flat.

This session did not observe a simple "cold once, fast forever after"
pattern; the endpoint hung intermittently even after a prior successful
warm call, suggesting some other periodic latency or contention source
in this sandbox, not just first-load cost. This is nonetheless the
first session in this course's history to capture real, live model
output — disclosed directly in `lesson.html`'s own "A Note on This
Chapter's Live-Testing" section with the full sequence above, not
smoothed into a single number. Per the honest-disclosure discipline
this course maintains, the live capture is also disclosed as including
a real model imperfection (an instruction was not fully followed), used
as a genuine finding rather than discarded for not being a clean
example. No graded `solution.py` in this chapter depends on a live
call, for the latency-variance reasons detailed in the self-critique
section above.

## Code tested before writing

`exercises/solution.py`, `practice/solution.py`, and `project/solution.py`
were each run for real this session and produce a perfect score/pass:

```
$ python3 exercises/solution.py   -> TOTAL: 21/21
$ python3 practice/solution.py    -> TOTAL: 8/8
$ python3 project/solution.py     -> PASS (self-check, internally consistent)
```

`project/starter.py` was also run for real (with its TODOs still
unfilled) to confirm it fails cleanly with a readable issue list and no
traceback, since a learner will run this file first.

`bash scripts/local_check.sh` was run from the repo root at the end of
this session and passed clean (folder structure, placeholder-text scan,
Python syntax, every `solution.py` executed for real, JS syntax and
chapter-path validation, secret scan).
