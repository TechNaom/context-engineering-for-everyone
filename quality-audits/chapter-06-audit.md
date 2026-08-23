# Chapter 6 Quality Audit — Avoiding Lost-in-the-Middle

Session date: 2026-08-23. This audit extends Chapters 1-5's running
fictional-org exclusion list (not restarting it), re-verifies Ollama
and every citation fresh this session, documents this chapter's
required re-verification of the "Lost in the Middle" (Liu et al., 2023)
citation against newer research, and ships Module 3's single guided
project, closing Module 3.

## Honest self-critique

**What's strong:**

- The hook (Marchside Regional Trauma Network/VitalsLine) demonstrates a
  genuinely distinct failure mode from all five prior chapters on
  purpose: every recipe through Chapter 5 is implemented correctly —
  budget (Ch. 2), pin/summary/window shape (Ch. 3), long-term recall
  policy (Ch. 4), fidelity-checked compression (Ch. 5) — and a
  present, unmodified, correctly-compressed safety fact still fails to
  surface, because nothing decided where it belonged in the final
  assembled window. This is precisely the gap this chapter exists to
  close, and it required deliberately choosing a failure that is NOT a
  presence failure (every prior chapter's own subject) but a pure
  positional one, which meant designing a scenario where compression
  succeeds completely and the problem only appears afterward.
- The chapter's central task — re-verifying the "Lost in the Middle"
  citation Chapter 1 first used and every session since flagged in
  `PROJECT_STATE.md`'s Known Issues as needing this chapter's own
  re-check — was done for real this session, not asserted. Two
  additional sources were fetched live and read in full: Hsieh et al.'s
  2024 "Found in the Middle" (a mechanistic explanation and a partially
  corrective calibration method) and Chroma's 2025 "Context Rot" report
  (an 18-frontier-model 2025 replication). The lesson's own
  "Re-Verification" section states the honest conclusion directly: the
  core claim still holds on today's models, but its exact shape is now
  understood to be model- and length-specific with a real structural-
  coherence interaction the original paper didn't isolate — a genuine
  update, not a rubber-stamp of a three-year-old finding.
- The live-captured example (a forklift safety fact placed in the
  middle of a short context, captured this session) shows a real,
  nuanced partial result: the model correctly extracted a specific
  identifier from the middle-positioned fact while explicitly claiming
  the fact's own substance "isn't stated," when it plainly was. This is
  used honestly as a concrete instance of position affecting
  reliability even when nothing about the fact was missing, ambiguous,
  or compressed away — directly reinforcing why Step 5's positional
  probe has to check answer content, not just whether an ID or token
  appears.
- Every number in the lesson's worked-math table and every exercise/
  practice/project number was computed and cross-checked against its
  own dependent scoring code before publishing, not asserted —
  `python3 exercises/solution.py`, `practice/solution.py`, and
  `project/solution.py` all score/pass perfectly when run (see "Code
  tested before writing" below for the actual output).
- **Module 3's single guided project ships this session, as a firm,
  now-honored commitment** (Chapter 5's session explicitly deferred it
  here). The project deliberately draws on both Chapter 5 (compression
  fidelity, Part 1) and Chapter 6 (context ordering, Part 2) together,
  per the curriculum map's own paired Module 3 labs — not a
  Chapter-6-only task wearing a "Module 3" label. See "Project tier"
  below for the honest reasoning behind the project's tier, since the
  curriculum map's own numbered ladder doesn't assign one to Module 3.

**Honest gaps:**

- As in every prior chapter, no exercise, practice, or project
  `solution.py` depends on a live model call — every weight-ranking,
  anchor-assignment, and positional-probe decision in the automated
  harnesses is deterministic, hand-computed data. This remains a
  disclosed, deliberate judgment call for the same reason Chapters 3-5
  gave: `scripts/local_check.sh` runs every `solution.py` under a
  20-second timeout, well inside some of this course's own previously
  observed Ollama wait times.
- This chapter's positional-probe exercises (Exercise 5, Practice
  Scenario 4, and the project's Part 2 self-check) validate placement
  against clean, hand-authored position/weight labels rather than
  deriving "is this content actually load-bearing" or "did the model
  actually use this correctly" from a real natural-language answer —
  the same category of gap Chapter 5's own audit flagged for its
  fidelity-check exercises (clean tokens vs. real natural-language
  matching). A live positional probe against real model output, scored
  automatically, is a harder problem than this chapter's own artifacts
  exercise, flagged here for a later chapter or revision, consistent
  with the standing practice of flagging rather than silently omitting
  known gaps.
- The lesson's worked-math table (Marchside's buried allergy note) uses
  illustrative token counts and percentile bands calibrated to the
  general shape of the cited research (a middle band roughly 20-80% of
  window length being least reliable), not a claim that this exact
  numeric band is itself a peer-reviewed, universally applicable
  threshold — the lesson does not state it as one, but a reader
  skimming only the worked-math table without the surrounding
  Re-Verification section could mistake it for a precise, universal
  constant rather than an illustrative simplification of research that
  itself shows the effect is model- and length-specific. Flagged here
  explicitly so a future revision considers adding an inline caveat
  directly inside the worked-math table itself, not only in the
  preceding prose.
- This chapter's own live capture is a small, low-stakes illustration
  (a fictional forklift safety detail), chosen because it's easy to
  verify by eye — the same category of honest limitation Chapter 5's
  audit flagged for its own PIN-exclusion capture. A reader should not
  conclude every real positional failure will be this legible; the
  lesson states this indirectly through its broader Re-Verification
  section but does not restate it directly next to the live capture
  itself, worth tightening in a future revision.

## Module 3 project tier — an honest resolution, not a default

`docs/curriculum/CURRICULUM_MAP.md`'s own Projects section defines four
numbered tiers tied to specific chapters: L1 Guided (ships after Ch. 2),
L2 Assisted (ships after Ch. 4), L3 Independent (ships after Ch. 8), L4
Architecture Challenge (the Ch. 13 capstone). This ladder does not
assign a numbered tier to Module 3 at all — it jumps directly from L2
(Ch. 4) to L3 (Ch. 8), meaning no chapter of this course's own numbered
project-ladder is scheduled to ship between Chapters 4 and 8. This
chapter's own project therefore cannot honestly be labeled "L3" (that
label is the curriculum map's own explicit commitment to Chapter 8, and
mislabeling this chapter's project L3 would create a genuine conflict
two chapters later) or any other numbered tier the map doesn't itself
assign here.

What this chapter's project actually is: an application of this
course's own separate "one project per module" convention (established
in Chapter 4's session, applied again in Chapter 5's session by
deferring to this chapter, and honored here) filling the gap the
numbered ladder leaves between L2 and L3. It is titled "Module 3
Project," not "L3," in every artifact (`README.md`, `RUBRIC.md`,
`index.html`, `interview-questions.html`'s closing note, and the
lesson's own closing callout), and its scaffold level is disclosed
explicitly as sitting between L2's partial scaffold and L3's
no-scaffold: a full spec is given (like L2), but the learner designs
both halves (Chapter 5's compression skill and Chapter 6's own ordering
skill) together with no part solved for them, closer to L3's
independence than L2's. This is the honest resolution of the task's own
instruction to "confirm the project's level (L1/L2/etc.) for Module 3"
against the curriculum map — the correct finding is that no numbered
tier applies, and inventing one would misrepresent the map rather than
follow it.

## Fictional-org exclusion check, extending the running list

Checked against Chapters 1-5's own combined 54-org list (from
`quality-audits/chapter-05-audit.md`): Brackwater Home Internet, Cobalt
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
Management, Talmarsh Veterinary Alliance — and against
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

**11 new fictional orgs used this session**, every distinctive root
word checked for zero collision against both lists above via a live
grep across `quality-audits/`, `chapters/`, and
`ai-engineering-for-everyone`'s own audit file before use, which
returned zero matches for any of the 11 new roots below:

- **Marchside Regional Trauma Network** (lesson hook; product: VitalsLine)
- **Calverton Public Defender's Office** (exercises; product: DocketLine)
- **Nunroth Independent Bookstore Cooperative, Vesparro Marine Salvage,
  Holstead Grain Exchange, Quenby Historical Archive Society, Farrowline
  Dairy Cooperative, Delacroix Regional Airport Authority, Pennwhistle
  Community Radio Network, Ostergaard Marine Insurance** (practice
  bank, 8 orgs)
- **Brackholt County Court Records Office** (Module 3 project; product:
  ArchiveLine)

No collision found against either list's distinctive roots. Future
chapters should extend this combined list (Chapters 1-5's 54 orgs plus
this session's 11, for **65 total in this repo**, plus the full
`ai-engineering-for-everyone` list above), not restart it.

## The Lost-in-the-Middle re-verification, in full

This is the task Chapter 1 flagged as needing to happen here, and it
was done for real this session, fetching all three positional-effect
sources live rather than reusing any prior chapter's own citation:

1. **Liu et al., 2023, "Lost in the Middle" (`arxiv.org/abs/2307.03172`,
   also published at TACL)** — re-fetched live this session and
   confirmed still live, unchanged since Chapter 1's own original
   citation. This is the finding being re-verified, not new evidence.
2. **Hsieh et al., 2024, "Found in the Middle"
   (`arxiv.org/abs/2406.16008`)** — fetched live and confirmed live.
   Provides a mechanistic explanation (an intrinsic U-shaped attention
   bias toward the start and end of input, independent of content
   relevance) and a partially corrective calibration method improving
   retrieval-augmented results "by up to 15 percentage points." This
   upgrades the original finding from "observed" to "understood and
   partially addressable."
3. **Hong, Troynikov, and Huber, 2025, "Context Rot" (Chroma Research,
   `trychroma.com/research/context-rot`, reached via a 301 redirect
   from the historical `research.trychroma.com/context-rot` URL, both
   disclosed in the lesson's own Sources section)** — fetched live and
   confirmed live. Tested 18 current frontier models (GPT-4.1, the
   Claude 4 family, Gemini 2.5, Qwen3) and found the effect persists on
   2025-era frontier models, not only 2023-era ones, with non-uniform
   accuracy drops of 30-50% before documented context limits. Also
   surfaced a genuine nuance disclosed honestly in the lesson rather
   than smoothed over: models performed better on shuffled than
   structurally coherent long contexts in this specific study,
   something the original 2023 paper's simpler setup didn't isolate.

**The honest, re-verified conclusion this chapter's lesson states
directly:** the core claim (position measurably affects reliability,
especially content away from the start/end) still holds across current
frontier model families as of 2025 — this is not a stale, three-year-old
finding being treated as permanently settled. What has genuinely changed
since Chapter 1's original citation is the picture's precision: a
mechanistic, partially correctable cause is now understood (not an
unfixable transformer property), the exact shape and magnitude are
model- and context-length-specific rather than one universal curve, and
document structure/coherence measurably interacts with the effect in
ways the original paper didn't test for. This is disclosed in full in
the lesson's own "Is 'Lost in the Middle' Still True? A Re-Verification"
section, not summarized away, and `PROJECT_STATE.md`'s Known Issues
entry for this citation (open since Chapter 1) is resolved by this
session, not merely restated.

## Source verification, done honestly

All 5 sources cited in `lesson.html` were fetched and read live this
session via WebFetch/WebSearch, not reused from any prior chapter's own
citation set — including Chapter 1's own original Liu et al. citation,
deliberately re-fetched here specifically because this is the chapter
where it becomes the central subject:

1. Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, and Liang, *"Lost
   in the Middle: How Language Models Use Long Contexts"* —
   `arxiv.org/abs/2307.03172`. Re-fetched and confirmed live this
   session, unchanged from Chapter 1's own citation. The original,
   peer-reviewed foundational finding this entire chapter re-verifies.
2. Hsieh et al., *"Found in the Middle: Calibrating Positional
   Attention Bias Improves Long Context Utilization"* (2024) —
   `arxiv.org/abs/2406.16008`. Fetched and confirmed live this session.
   This chapter's required 2024/2025 re-verification source.
3. Hong, Troynikov, and Huber, *"Context Rot: How Increasing Input
   Tokens Impacts LLM Performance"* (Chroma Research, 2025) —
   `trychroma.com/research/context-rot`. This session's fetch of the
   historical `research.trychroma.com/context-rot` URL 301-redirected
   here; the redirect target was fetched and confirmed live. This
   chapter's second required re-verification source.
4. Anthropic, *"Prompting best practices"* (Claude Platform Docs, "Long
   context prompting" section) —
   `platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices`.
   This session's fetch of the historical
   `docs.claude.com/en/docs/build-with-claude/prompt-engineering/long-context-tips`
   URL 302-redirected here; notably, the dedicated long-context-tips
   page no longer exists as its own URL — its content has been folded
   into this consolidated prompting-best-practices page. The redirect
   target was fetched and confirmed live, and the exact quoted guidance
   ("place your long documents and inputs near the top... queries at
   the end can improve response quality by up to 30 percent") was
   confirmed present in the fetched page content.
5. LangChain, `LongContextReorder` API reference (`langchain-community`)
   — `reference.langchain.com/python/langchain-community/document_transformers/long_context_reorder/LongContextReorder`.
   Disclosed honestly: this session's first attempt to cite LangChain's
   own how-to guide for this exact feature (historically at
   `python.langchain.com/docs/how_to/long_context_reorder/`, and its
   `v0.2` archived equivalent) found both URLs now 308-redirect to a
   generic package overview page with no equivalent replacement content
   — a genuine dead link, not a relocation, unlike this chapter's other
   two redirects above. The API reference page was fetched instead as a
   working alternative and confirmed to still document the same
   behavior and cite Liu et al.'s own paper as its motivation.

Two of five sources required following a live redirect where the
content moved but stayed reachable (Chroma, Anthropic); one source's
originally intended URL was a genuine dead end requiring a different,
still-live page from the same provider entirely (LangChain) — all
three disclosed in full above and in the lesson's own Sources section,
consistent with every prior chapter's own finding that documentation
URLs churn and must be re-verified per session, never assumed stable
from a prior session's own fetch, let alone a prior chapter's.

## Ollama check, done fresh this session

`curl http://localhost:11434/api/tags` responded normally and confirmed
the same installed model as all five prior chapters
(`llama3.2:latest`). `/api/chat` was tested twice this session and
succeeded on the first attempt both times — consistent with Chapters 4
and 5's own sessions, not Chapter 3's, but reported honestly as this
session's own result, not a claim the earlier intermittent hang is
resolved:

1. A first call (a positional-bias prompt with a fact placed in the
   middle of a short context, 200-second timeout) returned a real
   response in **113.7 seconds**, almost entirely the model's own cold
   load time in this sandbox (about 100 seconds of the total, per the
   response's own `load_duration` field).
2. A second, unrelated call a few minutes later (model already warm,
   200-second timeout) returned in **5.1 seconds**.

Future sessions should keep budgeting for retries with generous
(120s+) timeouts regardless, exactly as `PROJECT_STATE.md` instructs —
Chapter 3's own session already demonstrated that a successful warm
call can still be followed by a later timeout within the same session,
so three consecutive session-level successes here (following Chapters 4
and 5's own consecutive successes) are additional data points, not a
reason to relax the standing discipline. As in every prior chapter, no
graded `solution.py` in this chapter depends on a live call, for the
same 20-second-`local_check.sh`-timeout reason. The live capture (the
first call above) is used in `lesson.html`'s "A Live-Captured
Positional Example" section, disclosed as illustrative, and is notable
for a nuanced partial result: the model correctly extracted a specific
identifier (a forklift serial number) from a middle-positioned fact
while explicitly reporting the fact's own substance as "isn't stated,"
when it plainly was — read honestly in the lesson as a real instance of
position affecting reliability even when nothing about the fact was
missing, ambiguous, or compressed away, not dismissed as an unrelated
quirk.

## Code tested before writing

`exercises/solution.py`, `practice/solution.py`, and
`project/solution.py` were each run for real this session and produce a
perfect score:

```
$ python3 exercises/solution.py   -> TOTAL: 26/26
$ python3 practice/solution.py    -> TOTAL: 8/8
$ python3 project/solution.py     -> PASS (all six self-check functions report no errors)
```

`exercises/starter.py`, `practice/starter.py`, and `project/starter.py`
were each also run for real (with their TODOs still unfilled) to
confirm they fail cleanly with a readable score report and no
traceback, since a learner will run these files first:

```
$ python3 exercises/starter.py    -> TOTAL: 0/26 (clean, no traceback)
$ python3 practice/starter.py     -> TOTAL: 0/8 (clean, no traceback)
$ python3 project/starter.py      -> 8 issue(s) found (clean, no traceback)
```

`bash scripts/local_check.sh` was run from the repo root at the end of
this session and passed clean (folder structure, placeholder-text scan,
Python syntax, every `solution.py` executed for real, JS syntax and
chapter-path validation, secret scan).
