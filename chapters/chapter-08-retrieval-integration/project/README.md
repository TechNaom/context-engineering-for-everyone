# Module 4 Project (L3 Independent): Build Quartzfield Regional Public Defender Consortium's BriefLine Retrieval Integration + Source Assembly Pipeline

This is Module 4's closing lab, drawing on **both** chapters this module
built — Chapter 7's Source Assembly Recipe and Chapter 8's own Retrieval
Integration Recipe — not just Chapter 8's material in isolation, per the
curriculum map's own Module 4 labs: "assemble context from 3+ real
sources for one request" and "take a retriever's ranked output and
produce well-formed context from it." Chapter 7's own session
deliberately deferred its project here (see
`quality-audits/chapter-07-audit.md`), and this project is where that
commitment is honored.

## A note on this project's tier

This is the curriculum map's own literal **L3 Independent** tier
project (its four-tier ladder: L1 after Ch. 2, L2 after Ch. 4, L3 after
Ch. 8, L4 the Ch. 13 capstone) — unlike Module 3's own project, which
fell in a gap the ladder never assigned, Module 4's project lands
exactly where the ladder says it should. "Independent" means **no
scaffold**: `starter.py` gives you the full spec and the raw data, but
no partially-filled template beyond that and no step-by-step hints —
you design both parts of the pipeline yourself, the way Chapter 4's own
L2 project gave a partial scaffold and this one deliberately does not.

## The task

Quartzfield Regional Public Defender Consortium's fictional pre-hearing
brief assistant, BriefLine, prepares a sentencing brief in two parts:

1. **Part 1 (Chapter 8's own skill):** a retriever returns five ranked,
   scored chunks from the sentencing-guideline and case-law corpus.
   Apply a relevance floor, fit the survivors to a 380-token budget at a
   chunk boundary (never partially including a chunk), identify which
   surviving chunks are consecutive passages of the same document and
   should be stitched together, and attach provenance to every kept
   chunk.
2. **Part 2 (Chapter 7's own skill):** Part 1's own resolved output
   becomes one inventoried source among four for the same request.
   Detect the genuine contradiction between two of those sources (the
   retrieved guideline commentary and a live docket-status check, both
   speaking to whether a sentencing departure exception currently
   applies), resolve it using the given authority ranking, and confirm
   the retained set fits the 500-token window budget.

## Why this project touches both chapters, not just this one

Module 4's own two labs are stated as a pair in the curriculum map, not
as two separate single-chapter tasks. A real production RAG pipeline
never stops at "the retriever returned good chunks" — those chunks still
have to become one well-formed source (Chapter 8) and then take their
place among whatever else is feeding the same request, including
sources that might actively disagree with them (Chapter 7). This
project tests whether you can hold both skills at once, in the correct
order: Chapter 8's integration discipline first, producing exactly the
kind of single, well-formed source Chapter 7's own Step 1 inventory is
entitled to assume it already has.

## How to run it

```bash
python3 starter.py
```

Most of this project's self-check IS fully mechanical: it verifies your
Part 1 floor/fit/stitch/provenance choices exactly as Chapter 8's own
recipe would, and separately verifies your Part 2 contradiction
detection, authority-based resolution, and budget fit exactly as
Chapter 7's own recipe would. Only the QUALITY of your two write-ups is
open-ended.

## How to check your work for real

1. Run the self-check above until it passes.
2. Compare your full reasoning against `solution.py` — not to match its
   exact wording, but to check whether your justification is comparably
   specific, especially about *why* the two conflicting sources
   disagree and *why* authority ranking (not a coin flip, not "keep
   both and let the model sort it out") is what resolves it.
3. Self-grade against `RUBRIC.md`.

## Files

- `starter.py` — the spec, both parts' data, and the self-check. No
  partial scaffold — per this project's own "no scaffold" L3 tier.
- `solution.py` — one complete, valid reference design.
- `RUBRIC.md` — the grading criteria.
- `index.html` — the styled project page (same content as this file,
  for browser reading).
