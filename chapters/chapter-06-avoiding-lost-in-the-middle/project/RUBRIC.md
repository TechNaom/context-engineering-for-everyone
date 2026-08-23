# Module 3 Project Rubric: Brackholt County Court Records Office's ArchiveLine Compression + Ordering Pipeline

This project is a two-part design-and-validate task (see `README.md`
for why this shape — and the between-L2-and-L3 tier — is the right
closing lab for Module 3). Grade your own completed `starter.py`
against the six criteria below, each worth up to 4 points (24 points
total).

## 1. Part 1 candidate-presence correctness (0-4)

- **4:** `PRODUCED_SUMMARY_CONTENT` includes all three flagged
  candidates from `CANDIDATE_DETAILS` and contains no unknown keys —
  fully checked by `starter.py` itself; full credit requires
  `check_part1_candidates()` to report no errors.
- **2:** Exactly one candidate is missing.
- **0:** Two or more candidates are missing, or `PRODUCED_SUMMARY_CONTENT`
  is not a valid set.

## 2. Part 1 strategy correctness (0-4)

- **4:** `STRATEGY_CHOICES` assigns a valid strategy to every candidate,
  and correctly chooses `extractive` for all three (each candidate is a
  specific, structured fact where exact wording matters) — fully
  checked by `starter.py`; full credit requires `check_part1_strategy()`
  to report no errors.
- **2:** Exactly one candidate has the wrong strategy.
- **0:** Two or more candidates have the wrong strategy, or an entry is
  missing or invalid.

## 3. Part 2 anchor-assignment correctness (0-4)

- **4:** The query block sits at `end_anchor_query_position`, and both
  high-weight blocks (the pinned safety note and Part 1's own compressed
  summary) sit at `start_anchor_region` — fully checked by `starter.py`;
  full credit requires `check_part2_anchor_assignment()` to report no
  errors.
- **2:** Exactly one anchor rule is violated.
- **0:** Two or more anchor rules are violated, or `BLOCK_POSITIONS` is
  missing entries.

## 4. Part 2 middle-placement correctness and budget fit (0-4)

- **4:** Every low-weight block is placed in `middle`, not occupying
  either anchor position, and the assembled window's total token count
  fits inside the 3,200-token budget — fully checked by `starter.py`;
  full credit requires `check_part2_middle_placement()` and
  `check_window_budget()` to both report no errors.
- **2:** Exactly one low-weight block wrongly occupies an anchor
  position.
- **0:** Two or more low-weight blocks wrongly occupy an anchor
  position, or the window exceeds its budget.

## 5. Judgment-call and write-up quality (0-4)

- **4:** `PART1_JUSTIFICATION` gives a real, specific reason for the
  extractive-strategy choice tied to each candidate's own content, and
  `PART2_JUSTIFICATION` gives a real, specific reason for the anchor
  assignments AND correctly explains *why* the low-weight blocks are
  safely left in the middle (not just that they are) — not a
  restatement of weight labels.
- **2:** Both write-ups are present but generic, or one engages with the
  reasoning behind its placements and the other doesn't.
- **0:** Either write-up is missing or under 40 characters.

## 6. Completeness and boundary understanding (0-4)

- **4:** `python3 starter.py` passes with no errors, and the learner can
  explain in their own words which parts of each check are fully
  mechanical versus judgment-graded, AND can explain the specific
  boundary between Part 1 (Chapter 5's compression-fidelity skill) and
  Part 2 (this chapter's own context-ordering skill) — not just that
  both exist, but why a compressed block still needs its own positional
  decision afterward.
- **2:** The self-check passes, but the learner cannot clearly articulate
  the Part 1 / Part 2 boundary.
- **0:** The self-check does not pass.

## Passing bar

**19/24 (about 80%)** or higher, with no single criterion scoring 0, is
a passing design for this project's own self-graded check.

## How this rubric was used to grade `solution.py`

Run `python3 solution.py`. It passes both self-checks with no errors:
Part 1 preserves all three candidates with extractive strategy chosen
for each, defended by content-specific reasoning. Part 2 places both
high-weight blocks (the pinned safety note and the compressed summary)
at the start anchor region, the query at the end anchor position, and
all three low-weight blocks in the middle, totaling 2,850 of 3,200
window tokens. `PART1_JUSTIFICATION` explains why exact wording matters
for each candidate; `PART2_JUSTIFICATION` explains both the anchor
assignments and explicitly why the low-weight blocks are safely left in
the middle, not just that they are — a full 24/24 reference design.
