# Chapter 1 Quality Audit: The Context Budget

Session date: 2026-08-22. This is the first quality audit in this repo
(brand-new course, first build session), so it establishes the running
fictional-org exclusion list rather than extending one.

## Honest self-critique

**What's strong:**
- The hook (Brackwater Home Internet/SignalDesk) demonstrates a
  genuinely distinct context-engineering failure — not a prompt bug, not
  a retrieval bug, not a security issue — combining two real,
  independently documented mechanisms (a position/attention effect, and
  a naive truncation policy) rather than a single simplistic cause.
- The core mental model (the Context Budget) and its five-line ledger
  give a concrete, checkable framework, directly analogous in role to
  `ai-engineering-for-everyone`'s own six-layer stack, without copying
  its content or structure.
- Positioning against all three closest neighbors (`rag-for-everyone`,
  `mcp-for-everyone`, `ai-engineering-for-everyone` Chapter 3) is stated
  explicitly by name, both in `docs/discovery-notes.md` and in the
  lesson text itself ("Why This Course Exists"), matching the standing
  ecosystem discipline.
- All 8 exercises, 8 practice scenarios, and the L1 project's
  `solution.py` were run for real this session and score a perfect
  total — not assumed correct.

**Honest gaps:**
- This chapter's project, like `ai-engineering-for-everyone`'s Chapter
  1 project, is graded by a structural self-check (completeness,
  distinct lines used, non-trivial field lengths), not automated
  semantic grading of fix quality — the same necessary limitation every
  sibling course's diagnosis-style L1 project has, disclosed here rather
  than implied to be more rigorous than it is.
- No live model call was captured this session (see the Ollama
  disclosure below) — the hook's request-building code and the
  Exercise 4 budget arithmetic are illustrative and computed directly
  from stated numbers, not sampled from a running model. This chapter
  has no load-bearing dependency on a live call (same posture as
  `ai-engineering-for-everyone` Chapter 1), but later chapters that
  build a runnable compression or memory harness will need Ollama's
  chat endpoint working for real, and will disclose honestly if it
  isn't.
- The "Lost in the Middle" citation (source 2) is the original 2023
  research finding, not a 2025/2026 update — it remains the most
  directly citable, peer-reviewed source for the position effect and
  was verified live and readable this session; a later chapter (Chapter
  6, which owns this topic in full depth) should re-check for more
  recent replications or refinements before treating the finding as
  settled across all current model families.

## Fictional-org exclusion check

This is the first chapter built in this repo, so this list starts fresh
here rather than extending a prior chapter's. It was also checked this
session against `ai-engineering-for-everyone`'s own running exclusion
list (its `quality-audits/chapter-13-audit.md`, which itself compiles
Chapters 1-13 plus `ai-security-for-everyone`'s own list) — zero
distinctive-root overlap found.

**11 fictional orgs used this session:**

- **Brackwater Home Internet** (lesson hook; product: SignalDesk)
- **Cobalt Home Security** (exercises; product: GuardLine)
- **Windermere Legal Services, Pinecrest Veterinary Group, Solmark
  Payments, Thistledown Air Cargo, Ravenhollow University Registrar,
  Copperfield Home Appliances, Marrowgate Public Library, Fenwick
  Outdoor Adventures** (practice bank, 8 orgs)
- **Meridian Legal Aid Network** (project; product: CaseNote)

Every distinctive root word above (Brackwater, Cobalt, Windermere,
Pinecrest, Solmark, Thistledown, Ravenhollow, Copperfield, Marrowgate,
Fenwick, Meridian) was checked for zero overlap against
`ai-engineering-for-everyone`'s full compiled list (Northfield,
Thornwell, Larkspur, Gladstone, Sable Ridge, Cascadeworks, Harrowgate,
Kettleford, Verdigris, Pikeman, Hartwell, Thorncastle, Galewood,
Foxhaven, Wrensdale, Calderleigh, Marlowfield, Sorrelfield, Nettlebrook,
Amberglass, Hollowmere, Thistlecombe, Faircross, Ombervale, Larchgate,
Milbrandt, Copperlark, Vesperfield, Thrumley, Kestwick, Pellucid,
Nordkeep, Ashenvale, Emberlyn, Alderwood, ClearDesk, BillBuddy, and
more per that repo's own full audit trail). No collision found. Future
chapters in this repo should extend this list, not restart it — the
same discipline `ai-engineering-for-everyone` used across its own 13
chapters.

## Source verification, done honestly

All 5 sources cited in `lesson.html` were fetched and read live this
session via WebFetch, not recalled from training data:

1. Anthropic, "Effective context engineering for AI agents" — fetched
   successfully; confirmed direct quotes on context as a finite
   resource, "context rot," and the attention-budget mechanism.
2. Liu et al., "Lost in the Middle" (arXiv 2307.03172) — fetched
   successfully; confirmed the U-shaped performance finding directly
   from the abstract.
3. OpenAI, Prompt Engineering guide — the historical
   `platform.openai.com/docs/guides/prompt-engineering` URL 301-
   redirected to `developers.openai.com/api/docs/guides/prompt-
   engineering` this session; the redirect target was fetched and
   confirmed live, and the lesson's citation links directly to the
   working, current URL rather than the stale one.
4. Anthropic/Claude, context management blog post — the historical
   `anthropic.com/news/context-management` URL 308-redirected to
   `claude.com/blog/context-management` this session; same handling as
   source 3, cited at the working URL.
5. LangChain, "Memory for agents" — the historical
   `blog.langchain.com/memory-for-agents/` URL 301-redirected to
   `www.langchain.com/blog/memory-for-agents` this session; same
   handling, cited at the working URL.

Two of five sources required following a live redirect this session —
both disclosed directly in `lesson.html`'s own Sources section (not
just here), matching this ecosystem's standing discipline of catching
and disclosing exactly this kind of drift rather than masking it.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally and confirmed
one installed model (`llama3.2:latest`). A `POST /api/chat` completion
request did not return within a 20-second timeout. This matches every
sibling TechNaom course's independently reported sandbox behavior.
Disclosed directly in `lesson.html`'s own "A Note on This Chapter's
Live-Testing Limitation" section, not just here. This chapter has no
load-bearing dependency on a live model call — the hook's illustrative
request-building code and the exercises' budget arithmetic are computed
directly, not sampled. Chapters that build a runnable compression,
memory-retrieval, or context-evaluation harness (Chapters 5, 4, and 12
respectively) will need to re-check this before claiming any live
output, and will disclose the result honestly whatever it is.

## Code tested before writing

`exercises/solution.py` and `practice/solution.py` and `project/
solution.py` were each run for real this session and produce a
perfect score:

```
$ python3 exercises/solution.py   -> TOTAL: 23/23
$ python3 practice/solution.py    -> TOTAL: 8/8
$ python3 project/solution.py     -> PASS (structural self-check)
```

No code example in `lesson.html` claims to be a captured live-model
transcript; the request-building illustration is explicitly disclosed
as illustrative, not captured, per the Ollama section above.
