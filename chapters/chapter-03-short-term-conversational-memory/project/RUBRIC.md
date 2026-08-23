# Chapter 3 Project Rubric: Design Wrayland Behavioral Health Group's Recurring Counseling Check-In Short-Term Memory Policy

This chapter's project is a design-and-validate task (see `README.md`
for why this shape is the right first project for Module 2). Grade
your own completed `starter.py` against the five criteria below, each
worth up to 4 points (20 points total).

## 1. Required-pin correctness (0-4)

- **4:** `PINNED_FACT_IDS` includes every `safety_critical` and
  `clinical_change` fact and excludes every `small_talk` fact — the
  mechanical part of this criterion is fully checked by `starter.py`
  itself; full credit requires `check_pins()` to report no errors.
- **2:** Exactly one required or forbidden fact is misclassified.
- **0:** Two or more required/forbidden facts are misclassified, or
  `PINNED_FACT_IDS` is missing or empty.

## 2. Administrative-fact judgment quality (0-4)

- **4:** `POLICY_JUSTIFICATION` gives a real, specific reason for how
  the two `administrative` facts were handled (pinned or not) tied to
  this request type's actual shape — not a restatement of the
  category labels themselves.
- **2:** A justification is present but generic ("this seemed
  reasonable") without engaging with the administrative facts
  specifically.
- **0:** `POLICY_JUSTIFICATION` is missing or under 40 characters.

## 3. Budget correctness (0-4)

- **4:** `VERBATIM_WINDOW_TURNS` is a valid integer in range, and the
  full package (pinned-fact tokens + the fixed 1,200-token summary +
  the chosen verbatim window's tokens) fits inside the 7,500-token
  Line 3 budget — this is fully mechanically checked by `starter.py`;
  full credit requires `check_budget()` to report no errors.
- **2:** The self-check reports a budget overage that's a small,
  clearly accidental amount (off by one turn's worth of tokens).
- **0:** `VERBATIM_WINDOW_TURNS` is missing, out of range, or the
  package is over budget by a large, unexplained amount.

## 4. Follow-up plan concreteness (0-4)

- **4:** `FOLLOW_UP_PLAN` correctly names what covers any turn that
  falls outside the chosen verbatim window and isn't independently
  pinned (the running summary), and gives a real, specific reason this
  is an acceptable tradeoff for this request type — not just asserting
  it is.
- **2:** A plan is present but vague ("the summary handles it") without
  engaging with why that's acceptable here specifically.
- **0:** `FOLLOW_UP_PLAN` is missing or under 40 characters.

## 5. Completeness and self-check discipline (0-4)

- **4:** `python3 starter.py` passes the self-check with no errors, and
  the learner can explain in their own words which parts of this
  project's self-check are fully mechanical (required/forbidden pin
  categories, the budget-fit constraint) versus which parts are
  judgment-graded (the administrative-fact calls, the quality of both
  write-ups).
- **2:** The self-check passes, but the learner cannot explain the
  difference between the mechanical and judgment-graded parts.
- **0:** The self-check does not pass.

## Passing bar

**16/20 (80%)** or higher, with no single criterion scoring 0, is a
passing short-term memory policy design for this chapter's own
self-graded check.

## How this rubric was used to grade `solution.py`

Run `python3 solution.py`. It passes the self-check with no errors
(all three required facts pinned, the one forbidden fact excluded, a
12-turn verbatim window that brings the package to 7,225 of 7,500
tokens). On the two judgment criteria: `POLICY_JUSTIFICATION` explains
why both administrative facts were deliberately left unpinned
(recoverable elsewhere, not worth the reserve) and why the verbatim
window was sized to the maximum the budget allows (criterion 2);
`FOLLOW_UP_PLAN` correctly names the running summary as what covers
the four oldest, unpinned turns and explains why that's acceptable
given the one safety-relevant fact from that period is independently
pinned (criterion 4) — a full 20/20 reference design.
