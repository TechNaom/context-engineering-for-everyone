# Chapter 4 Project Rubric: Brightmoor Elder Law Group's CaseLine Short-Term AND Long-Term Memory

This chapter's project is a two-part design-and-validate task (see
`README.md` for why this shape — and the L2 Assisted tier — is the
right closing lab for Module 2). Grade your own completed `starter.py`
against the six criteria below, each worth up to 4 points (24 points
total).

## 1. Short-term required-pin correctness (0-4)

- **4:** `PINNED_FACT_IDS` includes every `legal_critical` fact from
  `CURRENT_SESSION_FACTS` and excludes the `small_talk` fact — fully
  checked by `starter.py` itself; full credit requires
  `check_short_term_pins()` to report no errors.
- **2:** Exactly one required or forbidden fact is misclassified.
- **0:** Two or more are misclassified, or `PINNED_FACT_IDS` is missing
  or empty.

## 2. Short-term budget correctness (0-4)

- **4:** `VERBATIM_WINDOW_TURNS` is a valid integer in range, and the
  full Line 3 package (pins + fixed summary + verbatim window) fits
  inside the 3,800-token budget — fully checked by `starter.py`; full
  credit requires `check_short_term_budget()` to report no errors.
- **2:** A small, clearly accidental overage (one turn's worth of
  tokens).
- **0:** Missing, out of range, or a large unexplained overage.

## 3. Long-term required-retrieval and staleness correctness (0-4)

- **4:** `RETRIEVED_LONG_TERM_FACT_IDS` includes every active
  `legal_critical` record, excludes the `small_talk` record regardless
  of status, and excludes every non-active (superseded/expired) record
  regardless of category — fully checked by `starter.py`; full credit
  requires `check_long_term_retrieval()` to report no errors.
- **2:** Exactly one required/forbidden/staleness rule is violated.
- **0:** Two or more rules are violated, or a superseded/expired record
  is retrieved.

## 4. Long-term budget correctness (0-4)

- **4:** The retrieved long-term package fits inside the 250-token
  Line 4 budget — fully checked by `starter.py`; full credit requires
  `check_long_term_budget()` to report no errors.
- **2:** A small, clearly accidental overage.
- **0:** Missing or a large unexplained overage.

## 5. Judgment-call and write-up quality (0-4)

- **4:** `SHORT_TERM_JUSTIFICATION` gives a real, specific reason for
  the administrative pin call, and `LONG_TERM_RETRIEVAL_JUSTIFICATION`
  gives a real, specific reason for the administrative retrieval call
  AND correctly explains *why* the superseded/expired records must be
  excluded (not just restates that they are) — not a restatement of
  category labels.
- **2:** Both write-ups are present but generic, or one engages with
  the staleness reasoning and the other doesn't.
- **0:** Either write-up is missing or under 40 characters.

## 6. Completeness and boundary understanding (0-4)

- **4:** `python3 starter.py` passes with no errors, and the learner
  can explain in their own words which parts of each check are fully
  mechanical versus judgment-graded, AND can explain the specific
  boundary between Part 1 (Line 3, this session, Chapter 3's skill) and
  Part 2 (Line 4, across sessions, this chapter's own skill) — not just
  that both exist.
- **2:** The self-check passes, but the learner cannot clearly
  articulate the Line 3 / Line 4 boundary.
- **0:** The self-check does not pass.

## Passing bar

**19/24 (about 80%)** or higher, with no single criterion scoring 0, is
a passing design for this chapter's own self-graded check.

## How this rubric was used to grade `solution.py`

Run `python3 solution.py`. It passes both self-checks with no errors:
Part 1 pins all three `legal_critical` facts, uses a 7-turn verbatim
window, and totals 3,400 of 3,800 Line 3 tokens. Part 2 retrieves both
active eligible records (the required `legal_critical` language
preference and the judgment-call administrative contact preference),
excludes both superseded records, the expired record, and the
small_talk record, and totals 85 of 250 Line 4 tokens.
`SHORT_TERM_JUSTIFICATION` explains the administrative pin call
(criterion 5); `LONG_TERM_RETRIEVAL_JUSTIFICATION` explains the
administrative retrieval call and explicitly explains why each
excluded record is excluded, not just that it is (criterion 5) — a full
24/24 reference design.
