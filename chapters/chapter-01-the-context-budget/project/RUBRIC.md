# Chapter 1 Project Rubric: Diagnose CaseNote's Ledger Gaps

This chapter's project is a diagnosis-and-prioritization task (see
`README.md` for why this shape, not a build task, is the right first
project). Grade your own completed `starter.py` against the five
criteria below, each worth up to 4 points (20 points total).

## 1. Line mapping accuracy (0-4)

- **4:** All five facts are mapped to five distinct ledger lines, and
  each mapping is defensible on the fact's actual content (not just a
  plausible-sounding guess) — e.g., fact 4 (immigration status lost
  between sessions) maps to Recalled Long-Term Memory, not Conversation
  History.
- **2:** Most (3-4) facts are mapped to the correct line, or all five
  are mapped but one or two collide onto the same line when the
  scenario clearly describes five distinct gaps.
- **0:** Most mappings are incorrect, or fewer than three facts are
  mapped to a valid line ID at all.

## 2. Evidence quality (0-4)

- **4:** Each fact's `evidence` restates the specific mechanism from
  the scenario in the learner's own words (not copy-pasted verbatim
  from `starter.py`'s docstring), showing the evidence was actually
  understood, not just located.
- **2:** Evidence is present for all five facts but is copy-pasted
  verbatim or is too generic to show real understanding of the
  specific mechanism.
- **0:** Evidence is missing or is a placeholder for most facts.

## 3. Fix concreteness (0-4)

- **4:** Every fix is a specific, actionable engineering change (names
  a real technique: prompt-section splitting, a retrieval eviction
  step, transcript summarization, a persistent memory store with an
  explicit recall policy, a reserved output-token allowance) — never a
  vague "be more careful" or "trim it down."
- **2:** Fixes are present for all five facts but some are vague or
  restate the problem rather than proposing a real change.
- **0:** Most fixes are missing, vague, or not actually engineering
  changes.

## 4. Prioritization reasoning (0-4)

- **4:** `PRIORITIZED_ORDER` uses all five lines exactly once, and
  `JUSTIFICATION` gives a real, specific reason for the ordering —
  referencing which gaps compound as a conversation grows or carry real
  harm (a lost sensitive fact) versus which are bounded, fixed costs,
  the same reasoning the lesson's "two mechanisms compounded" point
  makes.
- **2:** The order is well-formed, but the justification is generic
  ("these are all important, roughly in this order") without real
  reasoning about growth or harm.
- **0:** `PRIORITIZED_ORDER` is missing, malformed, or the
  justification is missing or under 40 characters.

## 5. Completeness and self-check discipline (0-4)

- **4:** `python3 starter.py` passes the structural self-check with no
  errors, and the learner can explain in their own words why the
  self-check only verifies structure (completeness, distinct lines,
  non-trivial field lengths) and not the specific wisdom of any one
  fix — i.e., understands the difference between "well-formed" and
  "correct," and checked the latter by hand against `solution.py`.
- **2:** The self-check passes, but the learner cannot explain what it
  does and doesn't verify.
- **0:** The self-check does not pass.

## Passing bar

**16/20 (80%)** or higher, with no single criterion scoring 0, is a
passing diagnosis for this chapter's own self-graded check.

## How this rubric was used to grade `solution.py`

Run `python3 solution.py`. It passes the structural self-check with no
errors (all five facts mapped to five distinct lines, every evidence
and fix field well above the minimum length, `PRIORITIZED_ORDER` a
valid permutation of all five line IDs, `JUSTIFICATION` well above 40
characters). On the four judgment criteria: line mappings are each
directly traceable to the specific mechanism in the corresponding fact
(criterion 1); evidence restates the mechanism rather than quoting the
scenario verbatim (criterion 2); every fix names a specific, real
technique — prompt-section splitting, retrieval eviction, transcript
summarization with a recency window, a persistent memory store with an
explicit per-session recall policy, a reserved output-token allowance
(criterion 3); and the prioritization justification explicitly reasons
about which gaps compound as a conversation grows or carry real client
harm (Conversation History and Recalled Long-Term Memory first) versus
which are bounded, fixed costs (System Instructions last) (criterion
4) — a full 20/20 reference diagnosis.
