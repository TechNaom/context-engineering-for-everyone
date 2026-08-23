# Chapter 2 Quality Audit: Designing Context Window Budgets

Session date: 2026-08-23. This audit extends Chapter 1's running
fictional-org exclusion list (not restarting it) and re-verifies
Ollama and every citation fresh this session, per this repo's own
standing discipline.

## Honest self-critique

**What's strong:**

- The hook (Vantry Health Network/TriageLine) demonstrates a distinct
  failure mode from Chapter 1's Brackwater hook on purpose: a team that
  already did real, correct context-budget work for one request type,
  then broke a second request type by reusing that budget unchanged
  instead of re-deriving it. This is the precise gap Chapter 2 exists
  to close — proactive, per-request-type allocation — rather than a
  restatement of Chapter 1's "no budget at all" failure.
- Every number in the lesson's worked-math sections (the TriageLine
  vs. Chronic Care Check-In table, the second 8,000-token worked
  example, and every exercise/practice/project answer) is real,
  computed arithmetic, verified by running the actual Python this
  session, not asserted. `python3 exercises/solution.py`,
  `practice/solution.py`, and `project/solution.py` all score/pass
  perfectly.
- The project's self-check is more mechanically rigorous than Chapter
  1's: because the task asks for a token allocation *and* a
  surplus/deficit classification of that same allocation against given
  worst-case numbers, the self-check can verify the surplus/deficit
  calls are internally consistent with the learner's own numbers —
  not just that fields are non-empty. Only the profile-choice
  reasoning and the follow-up plan's specific wording remain
  judgment-graded, and this is disclosed explicitly in both
  `project/README.md` and `RUBRIC.md`.
- The lesson's request-type profile table was checked for a real bug
  during this session's own build: two of the four archetype rows
  (tool-heavy agentic, long-document review) originally had
  percentages that did not sum to 100% (85% and 90% respectively).
  This was caught before publishing by cross-checking the numbers
  against the exercises that depend on them, and corrected to 55/25/20
  and 65/20/15. Disclosed here directly as a real error caught and
  fixed this session, not silently corrected.

**Honest gaps:**

- Per the task brief, this chapter deviates from a literal reading of
  "project `README.md` + `solution.py` + `RUBRIC.md` + `ai-paired.html`"
  — no chapter in this repo (including the Chapter 1 reference chapter
  actually inspected this session) uses an `ai-paired.html` file; the
  real, load-bearing pattern this repo actually follows is
  `index.html` as the project's styled page. This chapter matches
  Chapter 1's *actual* file structure (`index.html`, not
  `ai-paired.html`) rather than the task brief's literal filename,
  since the explicit instruction was to match the reference chapter's
  real structure. Flagged here in case a future session's brief still
  names `ai-paired.html` — it does not exist anywhere in this repo's
  history and should not be assumed.
- The curriculum map's own project ladder lists one "L1 Guided"
  project tied to "ships after Ch. 2," while Chapter 1's own project
  (CaseNote) already shipped as a complete, real L1 Guided project in
  the prior session. This chapter resolves that tension by treating
  Module 1's own two stated labs — "diagnose a given system's
  context-budget gaps" (Chapter 1's project) and "design a budget
  allocation for a new request type" (this chapter's project) — as the
  intended one-project-per-chapter shape for Module 1, and ships a
  second, real L1-tier project (Halveston Regional Health System) newly
  built this session, still tagged "L1 Guided" since Module 2's L2
  Assisted tier does not begin until Chapter 4. This is a judgment call
  worth a human's review before Chapter 4 assumes the same resolution
  applies to L2.
- Like Chapter 1, no live model call was captured this session (see the
  Ollama disclosure below). Every worked-math number is direct,
  verified arithmetic against stated inputs, not sampled output.
- The request-type profile percentages in Section 4 of the lesson are
  presented as defensible starting points, explicitly labeled as such
  in the lesson text ("treat the percentages as a starting allocation
  to validate against real data for your own system, not a fixed
  law") — they are this course's own original synthesis for teaching
  purposes, not values taken from any external source, and are not
  claimed to be industry-standard.

## Fictional-org exclusion check, extending the running list

Checked against Chapter 1's own 11-org list (from
`quality-audits/chapter-01-audit.md`: Brackwater Home Internet, Cobalt
Home Security, Windermere Legal Services, Pinecrest Veterinary Group,
Solmark Payments, Thistledown Air Cargo, Ravenhollow University
Registrar, Copperfield Home Appliances, Marrowgate Public Library,
Fenwick Outdoor Adventures, Meridian Legal Aid Network) and against
`ai-engineering-for-everyone`'s own full compiled exclusion list (its
`quality-audits/chapter-13-audit.md`, itself compiling Chapters 1-13):
Airport, Alderbrook, Alderwood, Amberglass, Applecross, Ashenvale,
Ashford, Barrowfield, Basilwood, Bellwood, Berkeley, Blackwood,
Blythedale, Brackenfield, Brackwater, Brindlewood, Capstone,
Castlebridge, Cedarview, Cobblestone, Coldwater, Copperfield,
Copperlark, Coppervale, Cranmoor, Crowmarsh, Driftwood, Duskwater,
Elmsworth, Faircross, Fairhaven, Fairmont, Fallowfield, Fenwick,
Fernbrook, Foxhaven, Galewood, Gladstone, Grantham, Grovewell,
Halcombe, Harrowgate, Hartwell, Hollowmere, Hollowridge, Ironwood,
Ivywell, Kellbrook, Kestwick, Kettleford, Larchgate, Larchmoor,
Lindenmoor, Loxley, Marlowfield, Marlstone, Marrowgate, Millbrook,
Nettlebrook, Nettlewood, Northaven, Northfield, Oldfield, Ombervale,
Ondermoor, Openfield, Pellham, Pinehaven, Quillstone, Ravenhollow,
Ridgemont, Rosewick, Rutherglen, Saltmere, Silvergate, Sorrelfield,
Stanford, Sunderland, Talbridge, Thistlecombe, Thorncastle,
Thornhollow, Thornwell, Thrumley, Vaultridge, Vellcross, Vesperfield,
Wickmoor, Windale, Windermere, Windmere, Woodmere, Wrenfield,
Wrensdale, Yarrowfield (plus this course's own Cobalt, Pinecrest,
Solmark, Thistledown, Meridian, which are single-word/non-suffix names
already distinct from the pattern above).

**11 new fictional orgs used this session**, every distinctive root
word checked for zero overlap against both lists above before use:

- **Vantry Health Network** (lesson hook; product: TriageLine)
- **Corravine Freight** (exercises; product: DispatchLine)
- **Marrenkirk Insurance Group, Duvane Utilities Cooperative, Graytide
  Hospitality Group, Oakspire Home Care Network, Corundale Media Group,
  Pallisade Manufacturing, Redcliff Credit Union, Thackery Regional
  Exchange** (practice bank, 8 orgs)
- **Halveston Regional Health System** (project; product: IntakeLine)

No collision found against either list's distinctive roots. Future
chapters should extend this combined list (Chapter 1's 11 plus this
session's 11, for 22 total in this repo, plus the full
`ai-engineering-for-everyone` list above), not restart it.

## Source verification, done honestly

All 5 sources cited in `lesson.html` were fetched and read live this
session via WebFetch, not reused from Chapter 1's citation set without
re-verifying:

1. Anthropic / Claude Docs, "Context windows" — the historical
   `docs.claude.com/en/docs/build-with-claude/context-windows` URL
   302-redirected to `platform.claude.com/docs/en/build-with-claude/context-windows`
   this session; the redirect target was fetched and confirmed live,
   with the direct quote "to stay within context window limits, use
   the token counting API to estimate token usage before sending
   messages" and confirmation that the window "holds the conversation
   history plus the new output" generated.
2. OpenAI, Models documentation — the historical
   `platform.openai.com/docs/models` URL 301-redirected to
   `developers.openai.com/api/docs/models` this session; confirmed
   live, showing context-window size and maximum output tokens listed
   as distinct, per-model figures.
3. Anthropic / Claude Docs, "Token counting" — the historical
   `docs.claude.com/en/docs/build-with-claude/token-counting` URL
   302-redirected to `platform.claude.com/docs/en/build-with-claude/token-counting`
   this session; confirmed live, with the direct quote that counting
   tokens before sending lets a team "proactively manage rate limits
   and costs" and "optimize prompts to a specific length."
4. Google, Gemini API "Long context" — fetched successfully at its
   stable URL, `ai.google.dev/gemini-api/docs/long-context`; confirmed
   the direct quote "if you don't need tokens to be passed to the
   model, it is best to avoid passing them" and a named cost/performance
   tradeoff even at very large context sizes.
5. OpenAI Cookbook, "How to count tokens with tiktoken" — the
   historical `cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken`
   URL 308-redirected to
   `developers.openai.com/cookbook/examples/how_to_count_tokens_with_tiktoken`
   this session; confirmed live, with direct evidence that token counts
   determine "whether the string is too long for a text model to
   process" and "how much an OpenAI API call costs."

Four of five sources required following a live redirect this session
(more than Chapter 1's two of five) — all four disclosed directly in
`lesson.html`'s own Sources section, not just here, matching this
ecosystem's standing discipline of catching and disclosing exactly
this kind of drift rather than masking it. This is worth flagging for
future sessions: provider documentation URLs in this space appear to
churn frequently, and every session's own citation set should expect
to re-verify, not assume stability from one session to the next, even
within the same provider.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally and
confirmed the same installed model as Chapter 1
(`llama3.2:latest`). A `POST /api/chat` completion request was retried
with a considerably more patient timeout than Chapter 1's session used
(75 seconds, versus Chapter 1's 20-second attempt), per
`PROJECT_STATE.md`'s own instruction to retry more patiently before
concluding it's unreachable. The request still did not return within
that window. Disclosed directly in `lesson.html`'s own "A Note on This
Chapter's Live-Testing Limitation" section, not just here. This chapter
has no load-bearing dependency on a live model call — every
worked-math number is direct, verified arithmetic against stated
inputs, and every exercise/practice/project answer is graded the same
way. Chapters that build a runnable compression, memory-retrieval, or
context-evaluation harness (Chapters 5, 4, and 12) still need Ollama's
chat endpoint working for real, and should retry with an even more
patient timeout (and consider whether the model needs to be pulled or
warmed differently in this sandbox) before claiming any live output.

## Code tested before writing

`exercises/solution.py`, `practice/solution.py`, and `project/solution.py`
were each run for real this session and produce a perfect score:

```
$ python3 exercises/solution.py   -> TOTAL: 22/22
$ python3 practice/solution.py    -> TOTAL: 8/8
$ python3 project/solution.py     -> PASS (self-check, internally consistent)
```

`bash scripts/local_check.sh` was run from the repo root at the end of
this session and passed clean (folder structure, placeholder-text scan,
Python syntax, every `solution.py` executed for real, JS syntax and
chapter-path validation, secret scan) — see `PROJECT_STATE.md` for the
exact recorded result.

No code example in `lesson.html` claims to be a captured live-model
transcript; the TriageLine hook's request-building code and every
worked-math table are explicitly disclosed as directly computed, not
sampled, per the Ollama section above.
