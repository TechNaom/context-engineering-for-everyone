# Chapter 13 Project Rubric: Castellan Fleet Logistics — Context Engineering System Design

Grade your own filled-in design document against the six criteria below,
each worth up to 5 points (30 points total). See `README.md` for the
full business problem.

## 1. Job-to-be-done and multi-step/agentic shape, both components (0-5)

- **5:** Both components have a real job-to-be-done sentence naming who's
  actually waiting on the answer and how quickly, and a correctly-reasoned
  multi-step/agentic assessment (DispatchMind: genuinely multi-agent,
  naming the real sub-agents and each one's own job; ComplianceLedger:
  multi-step but single-agent, with a real reason given for why no
  sub-agent delegation is needed).
- **3:** Both assessments reach the correct conclusion, but one reads as
  asserted rather than reasoned from the business problem's own facts.
- **0:** A component's multi-step/agentic shape is misjudged (e.g.
  treating ComplianceLedger as needing its own multi-agent isolation
  boundary it has no real use for, or treating DispatchMind as a single
  prompt call with no real sub-agent structure).

## 2. Context Budget Ledgers, both components (0-5)

- **5:** `self_check.py` passes cleanly on both components (all five
  ledger lines present, non-negative, Line 5 reserved, and the total at
  or under the declared `hard_limit`) AND the allocation itself is
  defensibly reasoned for each component's own real request shape (e.g.
  DispatchMind's Line 2 dominance justified by live, multi-source
  incident grounding; ComplianceLedger's larger Line 2 justified by raw
  full-route log volume, not just asserted as "more").
- **3:** `self_check.py` passes, but one or both ledgers' own allocation
  reasoning is generic rather than tied to the component's own actual
  request shape.
- **0:** `self_check.py` fails on one or both components (missing
  section, unparseable block, Line 5 not reserved, or a ledger that
  exceeds its own declared hard limit).

## 3. DispatchMind's five recipe-treatment plans (0-5)

- **5:** All five plans (short-term memory, long-term memory,
  compression/ordering, source assembly/retrieval, tool/multi-agent/
  isolation) name a real, specific mechanism from their own chapter — a
  real pinning rule tied to a concrete example, a real staleness check
  tied to a concrete stale-vs-fresh conflict, a real isolation boundary
  naming exactly what crosses it and what doesn't — not a generic
  restatement of "this needs good memory management" with no mechanism
  named.
- **3:** All five plans are present and correctly scoped to DispatchMind's
  real-time, multi-agent shape, but two or more read as generic rather
  than naming DispatchMind's own specific mechanism.
- **0:** One or more plans are missing, or the isolation plan fails to
  name an actual boundary (what specifically does and does not cross
  from the Compliance Agent to the Customer-Comms Agent).

## 4. ComplianceLedger's five recipe-treatment plans (0-5)

- **5:** All five plans are present and correctly reflect
  ComplianceLedger's own different shape — no live verbatim window
  needed and a real reason given (Section 2.4), no isolation boundary
  needed and a real reason given (single-agent, not multi-agent), and the
  evaluation gate's stricter thresholds (Section 2.9) defended with a
  real reason (regulatory-record consequence) rather than just asserted
  as "more strict."
- **3:** The five plans are correct and present, but one or more "this
  doesn't apply the way it does for DispatchMind" claims isn't backed by
  a specific reason.
- **0:** One or more plans are missing, or ComplianceLedger is designed
  as a mechanical copy of DispatchMind's own plans with no real
  adaptation to its own async, single-agent, regulatory-record shape.

## 5. Cross-component synthesis (0-5)

- **5:** Section 3.1 names the specific facts (not labels) driving the
  divergence across all eleven recipes; 3.2 proposes a real, concrete
  future change for each component and correctly identifies which
  specific recipe(s) it would force a re-application of; 3.3 names a
  real, specific shared-infrastructure risk (a genuinely shared
  mechanism between the two components, not a generic "communication is
  important" answer) and a real, concrete guard against it.
- **3:** All three subsections are present and reasonable, but one is
  generic rather than tied to a specific real fact or mechanism.
- **0:** One or more of the three subsections is missing or is a
  placeholder.

## 6. Overall document completeness and internal consistency (0-5)

- **5:** All 21 required sections are present (`self_check.py` confirms
  this mechanically); no section contradicts another (e.g. a component
  whose plan describes a live verbatim conversation window but whose
  Section 2.2 explicitly says no such window exists); every "this recipe
  applies lightly/not at all here" claim anywhere in the document is
  defended with a real fact, never left as an unexplained label.
- **3:** All sections present, but at least one internal inconsistency
  exists between a stated plan and a later section's own claim about it.
- **0:** One or more required sections are missing entirely.

## Passing bar

**24/30 (80%)** or higher, with no single criterion scoring 0, is a
passing response for this chapter's own self-graded check — the same 80%
bar every project since Chapter 5's has used.

## How this rubric was used to grade `solution/SOLUTION_DESIGN_DOCUMENT.md`

Run `python3 solution.py`. It passes the full structural self-check (21
required sections present, both components' ledger and evaluation-gate
arithmetic valid). On the six qualitative criteria: both job-to-be-done
and multi-step/agentic assessments are real and correctly reasoned from
the business problem's own stated facts (Criterion 1); both ledgers use
a defensible, component-specific allocation with working arithmetic
(Criterion 2); DispatchMind's five plans each name a real, specific
mechanism, including an explicit isolation boundary naming exactly what
crosses it (Criterion 3); ComplianceLedger's five plans correctly reflect
its own async, single-agent, regulatory-record shape with real reasons
given for each divergence from DispatchMind's own treatment (Criterion
4); the cross-component synthesis names real facts (not labels) for the
divergence, a real concrete future change for each component tied to a
specific recipe re-application, and a real shared-infrastructure risk
(the shared tool-result curator) with a concrete per-caller-configuration
guard (Criterion 5); and the full document is internally consistent with
no contradiction between any component's stated plans (Criterion 6) — a
full 30/30 reference response.

## Why this rubric, and not a scored `starter.py`

A rubric requiring an actual working DispatchMind or ComplianceLedger
pipeline would be testing implementation skill this course doesn't teach
at the capstone level, not the architect-level composition judgment
Module 6 is actually about. The six criteria above deliberately mirror
the shape every project since Chapter 1's has used (objectively-checkable
facts graded by a script, open-ended reasoning graded by a rubric against
a reference response) — the genuine difference here, consistent with the
L4 "Architecture Challenge" tier's own no-scaffold, business-problem-only
scope, is that the checkable facts are a written document's structure and
arithmetic rather than a filled-in Python script's function calls, and
the reference response is a design document rather than a `solution.py`
holding all the answers. 24/30 (no criterion at 0) is set at the same
proportional bar (80%) as every project before it for the same reason:
passing requires getting every objectively-checkable fact right and
showing real, mechanism-specific reasoning on most of the judgment calls,
not restating this chapter's own worked DispatchMind incident example
under new names.
