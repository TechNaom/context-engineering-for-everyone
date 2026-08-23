# Module 4 Project Rubric (L3 Independent): Quartzfield Regional Public Defender Consortium's BriefLine Retrieval Integration + Source Assembly Pipeline

This project is a two-part design-and-validate task (see `README.md`
for why this shape — and its literal L3 Independent tier — is the right
closing lab for Module 4). Grade your own completed `starter.py` against
the seven criteria below, each worth up to 4 points (28 points total).

## 1. Part 1 relevance-floor correctness (0-4)

- **4:** `PART1_SURVIVORS` contains exactly the chunk keys that clear
  `RELEVANCE_FLOOR` (0.55) — fully checked by `starter.py` itself; full
  credit requires `check_part1_floor()` to report no errors.
- **2:** Exactly one chunk is wrongly included or excluded.
- **0:** Two or more chunks are wrong, or `PART1_SURVIVORS` is not a
  valid set.

## 2. Part 1 boundary-safe budget fit (0-4)

- **4:** `PART1_KEPT_CHUNKS` and `PART1_TOTAL_TOKENS` correctly reflect
  a greedy, descending-score fit that never partially includes a chunk
  and never exceeds the 380-token budget — fully checked by
  `starter.py`; full credit requires `check_part1_fit()` to report no
  errors.
- **2:** The kept set is correct but the reported total token count is
  wrong, or vice versa.
- **0:** The kept set is wrong, or the budget is exceeded.

## 3. Part 1 stitching and provenance (0-4)

- **4:** `PART1_STITCHED_GROUPS` correctly identifies the base-range/
  departure-clause group as one stitched passage, and `PART1_PROVENANCE`
  gives a complete source document and section for every kept chunk —
  fully checked by `starter.py`; full credit requires both
  `check_part1_stitch()` and `check_part1_provenance()` to report no
  errors.
- **2:** Exactly one of the two checks fails.
- **0:** Both checks fail, or stitching/provenance is missing entirely.

## 4. Part 2 contradiction detection (0-4)

- **4:** `PART2_CONTRADICTION_DETECTED` is `True`, correctly identifying
  that `part1_retrieved_document` and `live_docket_status_check` make
  incompatible claims about the same fact — fully checked by
  `starter.py`; full credit requires `check_part2_contradiction()` to
  report no errors.
- **0:** `PART2_CONTRADICTION_DETECTED` is `False`, `None`, or otherwise
  incorrect.

## 5. Part 2 authority-based resolution (0-4)

- **4:** `PART2_WINNING_SOURCE` correctly identifies
  `live_docket_status_check` as the higher-authority source for the
  contested claim, per `AUTHORITY_RANK` — fully checked by `starter.py`;
  full credit requires `check_part2_resolution()` to report no errors.
- **0:** The wrong source is chosen, or the field is left unset.

## 6. Part 2 retained-set and budget correctness (0-4)

- **4:** `PART2_SOURCES_RETAINED` includes all four sources (no
  restated duplicate content exists between them, so nothing should be
  dropped outright — only the contested claim itself is resolved),
  `PART2_ASSEMBLED_TOTAL_TOKENS` correctly sums their token counts, and
  `PART2_WITHIN_BUDGET` correctly reflects whether that total fits the
  500-token window budget — fully checked by `starter.py`; full credit
  requires `check_part2_budget()` to report no errors.
- **2:** The retained set is correct but the token total or budget flag
  is wrong, or vice versa.
- **0:** The retained set incorrectly drops a source that should stay,
  or the assembled total exceeds budget.

## 7. Judgment-call and write-up quality (0-4)

- **4:** `PART1_JUSTIFICATION` gives a real, specific reason for the
  floor/fit/stitch choices tied to the actual chunk scores and token
  counts, AND `PART2_JUSTIFICATION` gives a real, specific reason for
  the contradiction resolution that names *why* authority ranking (not
  an arbitrary tiebreak) is the right mechanism here — not a
  restatement of the rule names.
- **2:** Both write-ups are present but generic, or one engages with the
  reasoning behind its choices and the other doesn't.
- **0:** Either write-up is missing or under 40 characters.

## Passing bar

**22/28 (about 80%)** or higher, with no single criterion scoring 0, is
a passing design for this project's own self-graded check.

## How this rubric was used to grade `solution.py`

Run `python3 solution.py`. It passes both self-checks with no errors:
Part 1 correctly identifies three chunks past the relevance floor, fits
the two highest-scored (290 of 380 tokens) without ever truncating a
chunk, stitches the base-range and departure-clause chunks into one
contiguous passage, and attaches complete provenance to both. Part 2
correctly detects the contradiction between the retrieved document and
the live docket-status check, resolves it in favor of the live tool
output (rank 3 over rank 1), keeps all four sources (475 of 500 tokens,
25 tokens of headroom), and both write-ups explain the specific
reasoning behind each choice — a full 28/28 reference design.
