# Module 6 Assessment, Part 1 Rubric: Context-Evaluation Exercise

Grade your own completed `starter.py` against the five criteria below,
each worth up to 4 points (20 points total). See `README.md` for the
full scenario.

## 1. Completeness score accuracy (0-4)

- **4:** `part1_completeness` is correctly `0.75` (3/4) — three of Case
  TF-9102's own four required facts are present
  (`current_lifting_restriction`, `diagnosis_code`,
  `referring_physician_name`), and `updated_medication_list` is
  correctly identified as missing.
- **0:** `part1_completeness` is missing or incorrect.

## 2. Noise ratio accuracy (0-4)

- **4:** `part2_noise_ratio` is correctly `0.11` (330/3000) — the
  unrelated applicant's own notes pulled into `prior_case_notes` by a
  stale join, correctly identified as over the 0.10 threshold.
- **0:** `part2_noise_ratio` is missing or incorrect.

## 3. Positional audit accuracy (0-4)

- **4:** `part3_position_audit` correctly buckets all four facts:
  `current_lifting_restriction` as `"middle"` (position 1600, between
  the 450-token front cutoff and the 2550-token back cutoff),
  `diagnosis_code` as `"front"` (position 200), `referring_physician_name`
  as `"back"` (position 2800), and `updated_medication_list` as
  `"missing"`.
- **2:** Three of the four buckets are correct.
- **0:** Two or fewer buckets are correct, or the audit is missing.

## 4. Combined gate decision accuracy (0-4)

- **4:** `part4_gate_decision` is correctly `False` — the bundle fails
  the gate because completeness is under 1.0, independent of whatever
  the noise ratio or positional audit alone would have concluded.
- **0:** `part4_gate_decision` is missing or incorrect.

## 5. Justification quality: names all three problems, not just one (0-4)

- **4:** The justification explicitly names and cites real numbers for
  all three independent problems: incomplete required-fact coverage
  (0.75, missing `updated_medication_list`), an over-threshold noise
  ratio (0.11 against a 0.10 ceiling), and a critical fact buried in the
  middle bucket (`current_lifting_restriction` at position 1600) —
  and states or implies that fixing only one of the three would still
  leave the bundle failing the gate on the others.
- **2:** The justification correctly names one or two of the three
  problems with real numbers, but misses at least one entirely, or
  states the gate fails without explaining why on all applicable axes.
- **0:** The justification is a placeholder, or asserts the bundle is
  fine, or names problems without citing the actual computed numbers.

## Passing bar

**16/20 (80%)** or higher, with no single criterion scoring 0, is a
passing response for this assessment's own self-graded check.

## How this rubric was used to grade `solution.py`

Run `python3 solution.py`. It passes the structural self-check with no
errors (5/5 — completeness correctly `0.75`, noise ratio correctly
`0.11`, all four positional buckets correct, gate decision correctly
`False`, and a descriptive justification present). On the five judgment
criteria: completeness, noise ratio, and positional audit are all
computed correctly (criteria 1-3); the gate decision correctly reflects
that a single failing axis (completeness) is sufficient to fail the
whole gate (criterion 4); and the justification explicitly names and
cites real numbers for all three independent problems, including that
fixing only one would leave the other two unresolved (criterion 5) — a
full 20/20 reference response.

## Why this rubric, and not a broader "build a full evaluation platform" bar

Same reasoning as `quality-audits/chapter-12-audit.md`'s "Module 6
assessment groundwork" section: this rubric tests applying Chapter 12's
own already-taught completeness, noise-ratio, and positional-audit
functions together against one case with all three problems present at
once, not a re-teaching of the chapter's own content a second time, and
not an infrastructure-engineering exercise this course was never
designed to grade. 16/20 (no criterion at 0) mirrors
`ai-engineering-for-everyone`'s own Module 4 and Module 5 assessment
passing bars exactly, for the same reason: passing requires getting
every objectively-checkable computation right and demonstrating real
synthesis across all three checks on the one genuinely open-ended task
(the justification), not reciting the lesson's own content back
verbatim.
