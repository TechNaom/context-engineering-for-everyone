# Chapter 2 Project Rubric: Design Halveston Regional Health System's Post-Discharge Follow-Up Budget

This chapter's project is a design-and-validate task (see `README.md`
for why this shape is the right second project for Module 1). Grade
your own completed `starter.py` against the five criteria below, each
worth up to 4 points (20 points total).

## 1. Allocation correctness (0-4)

- **4:** `ALLOCATION` sums to exactly the real remaining budget (44,300
  tokens), every value is a positive integer, and every line's share
  falls in a plausible range (roughly 5%-80%) — the mechanical part of
  this criterion is fully checked by `starter.py` itself; full credit
  requires the self-check to pass with no allocation errors.
- **2:** The self-check reports a sum or range error that's off by a
  small, clearly accidental amount (a rounding slip), correctable in
  one line.
- **0:** `ALLOCATION` is missing, has the wrong keys, or is off by a
  large, unexplained amount from the real remaining budget.

## 2. Profile reasoning quality (0-4)

- **4:** `PROFILE_JUSTIFICATION` gives a real, specific reason for the
  chosen split tied to Post-Discharge Follow-Up's actual shape (a
  memory-heavy, moderately long, recurring conversation) — not a
  restatement of the percentages themselves, and not a default copy of
  one of the lesson's four archetypes without saying why it does or
  doesn't fit this request type as-is.
- **2:** A justification is present but generic ("this split seemed
  reasonable") without tying the reasoning to this request type's
  specific content shape.
- **0:** `PROFILE_JUSTIFICATION` is missing or under 40 characters.

## 3. Validation correctness (0-4)

- **4:** `VALIDATION` correctly classifies all three lines as
  "surplus" or "deficit" against the learner's own `ALLOCATION` and the
  given worst-case numbers — this is fully mechanically checked by
  `starter.py`; full credit requires the self-check to pass with no
  validation errors.
- **2:** One of three lines is misclassified.
- **0:** `VALIDATION` is missing, malformed, or most lines are
  misclassified.

## 4. Follow-up plan concreteness (0-4)

- **4:** `FOLLOW_UP_PLAN` names a real, specific technique for any line
  marked "deficit" (e.g. a named compression or eviction strategy) and
  correctly points to the later chapter that owns it — or, if there are
  no deficits, gives a real, specific reason the allocation has genuine
  headroom rather than just asserting it does.
- **2:** A plan is present but vague ("we'll optimize it later") or
  doesn't name a real technique.
- **0:** `FOLLOW_UP_PLAN` is missing or under 40 characters.

## 5. Completeness and self-check discipline (0-4)

- **4:** `python3 starter.py` passes the self-check with no errors, and
  the learner can explain in their own words which parts of this
  project's self-check are fully mechanical (the sum constraint, the
  surplus/deficit calls, both checked against the learner's *own*
  numbers) versus which parts are judgment-graded (whether the profile
  split and follow-up plan are actually well-reasoned, not just
  present).
- **2:** The self-check passes, but the learner cannot explain the
  difference between the mechanical and judgment-graded parts.
- **0:** The self-check does not pass.

## Passing bar

**16/20 (80%)** or higher, with no single criterion scoring 0, is a
passing allocation design for this chapter's own self-graded check.

## How this rubric was used to grade `solution.py`

Run `python3 solution.py`. It passes the self-check with no errors
(`ALLOCATION` sums to exactly 44,300 across three positive-integer,
in-range values; `VALIDATION`'s surplus/deficit calls are internally
consistent with `ALLOCATION` and `WORST_CASE_ACTUAL`). On the two
judgment criteria: `PROFILE_JUSTIFICATION` explains a deliberate
departure from the lesson's own `long_recurring` archetype (shifting
weight toward Line 4) tied to this specific request type's unusually
heavy recalled-memory need (criterion 2); `FOLLOW_UP_PLAN` names the
real deficit on Line 3, names a specific technique (summarizing older
follow-up sessions into a running note) rather than "just allocate
more" (which the fixed budget rules out), and correctly points to
Chapter 3 as the chapter that owns it (criterion 4) — a full 20/20
reference design.
