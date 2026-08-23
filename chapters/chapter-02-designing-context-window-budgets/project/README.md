# Chapter 2 Project (L1 Guided): Design Halveston Regional Health System's Post-Discharge Follow-Up Budget

This is Module 1's second project — completing the module's two labs
(per the curriculum map: "diagnose a given system's context-budget
gaps" in Chapter 1, "design a budget allocation for a new request
type" here). Chapter 1's project asked you to diagnose an existing
system's gaps after the fact. This one asks you to do this chapter's
own job: **design a real token budget for a brand-new request type
before it ships.**

## The task

Halveston Regional Health System's patient-messaging assistant,
IntakeLine, is shipping a new request type: "Post-Discharge
Follow-Up," a recurring, memory-heavy, moderately long conversation
type. `starter.py` gives you the real spec — a fixed context window, a
fixed reserved-output allowance, a fixed system-instructions cost, and
a worst-case content audit's real token needs per line. Your job:

1. **Allocate** — split the real remaining budget across Grounding
   Context (L2), Conversation History (L3), and Recalled Long-Term
   Memory (L4), and defend your split against this request type's
   actual shape.
2. **Validate** — compare your own allocation against the worst-case
   numbers given, and correctly classify each line as surplus or
   deficit.
3. **Plan the follow-up** — for any line you find in deficit, name a
   real technique (not "allocate more," since the budget is fixed) and
   the later chapter that owns it.

This mirrors exactly what Chapter 2's own lesson did for Vantry Health
Network's TriageLine — you're now doing it yourself, on a fresh
system, without the lesson doing the arithmetic for you first.

## Why this project, not another diagnosis task

Chapter 1's project tested whether you could look at an existing
system and correctly name what's missing. This chapter's own skill is
different and earlier in the lifecycle: given a request type that
doesn't exist yet, can you derive a real, defensible token budget for
it before a single request goes out the door, and know honestly
whether that budget will hold up against the worst realistic case —
the exact step Vantry's team skipped when Chronic Care Check-In
reused New Symptom Triage's budget unchanged.

## How to run it

```bash
python3 starter.py
```

Unlike Chapter 1's project, most of this one's self-check IS fully
mechanical: it verifies your `ALLOCATION` sums to exactly the real
remaining budget, and that your `VALIDATION` surplus/deficit calls are
internally consistent with your own numbers — not just well-formed.
Only the quality of your `PROFILE_JUSTIFICATION` and `FOLLOW_UP_PLAN`
reasoning is open-ended and self-graded.

## How to check your work for real

1. Run the self-check above until it passes.
2. Compare your full reasoning against `solution.py` — not to match its
   exact split, but to check whether your profile justification is
   comparably specific and your follow-up plan names a real technique.
3. Self-grade against `RUBRIC.md`.

## Files

- `starter.py` — the spec, your allocation template, and the self-check.
- `solution.py` — one complete, valid reference allocation.
- `RUBRIC.md` — the grading criteria.
- `index.html` — the styled project page (same content as this file,
  for browser reading).
