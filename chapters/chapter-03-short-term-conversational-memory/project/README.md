# Chapter 3 Project (L1 Guided): Design Wrayland Behavioral Health Group's Recurring Counseling Check-In Short-Term Memory Policy

This is Module 2's first lab (per the curriculum map: "manage a
long-running conversation's history under a hard token limit"). It
continues Module 1's one-project-per-chapter pattern (see
`quality-audits/chapter-02-audit.md`'s own note on this open decision)
rather than waiting for Module 2's "L2 Assisted" tier, which the
curriculum map ties to Chapter 4 instead.

## The task

Wrayland Behavioral Health Group's patient-messaging assistant,
SupportLine, already has a correctly allocated Line 3 (Conversation
History) budget for its "Recurring Counseling Check-In" request type —
Chapter 2's own recipe already ran for this request type. `starter.py`
gives you the real spec: a fixed 7,500-token Line 3 budget, a fixed
1,200-token running-summary size, 16 real turns with their token
counts, and 6 candidate facts disclosed across the conversation, each
tagged with a category. Your job:

1. **Pin** — choose which facts to explicitly pin, obeying the
   required/forbidden categories and making your own judgment call on
   the two administrative facts.
2. **Size the verbatim window** — choose how many of the most recent
   turns stay raw, such that pinned tokens + the fixed summary + your
   verbatim turns fit inside the 7,500-token budget.
3. **Justify and plan** — defend your choices, and explain what covers
   any turn that falls outside your verbatim window and isn't
   independently pinned.

This mirrors exactly what the lesson's own hook (Emberlynn Transit
Cooperative's RouteLine) got wrong — a right-sized budget with no real
policy for what happens when a long conversation exceeds it.

## Why this project, not another diagnosis or allocation task

Chapter 1's project tested diagnosis; Chapter 2's project tested
allocation. This chapter's own skill is different again: given a
budget that's already correctly sized, can you design the actual
eviction/compression policy that keeps a real, long-running
conversation inside it without silently dropping something
load-bearing — the exact policy layer Chapter 1 and Chapter 2 both
assumed would eventually get built, and this chapter finally builds.

## How to run it

```bash
python3 starter.py
```

Most of this project's self-check IS fully mechanical: it verifies
your pin choices obey the required/forbidden categories, and that your
full package (pins + summary + verbatim window) fits the given budget.
Only the quality of your `POLICY_JUSTIFICATION` and `FOLLOW_UP_PLAN`
reasoning is open-ended and self-graded.

## How to check your work for real

1. Run the self-check above until it passes.
2. Compare your full reasoning against `solution.py` — not to match its
   exact pin/window choices for the two administrative facts, but to
   check whether your justification is comparably specific.
3. Self-grade against `RUBRIC.md`.

## Files

- `starter.py` — the spec, your policy template, and the self-check.
- `solution.py` — one complete, valid reference policy.
- `RUBRIC.md` — the grading criteria.
- `index.html` — the styled project page (same content as this file,
  for browser reading).
