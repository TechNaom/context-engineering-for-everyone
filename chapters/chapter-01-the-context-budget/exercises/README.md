# Chapter 1 Exercises: The Context Budget

These exercises use a second scenario, deliberately different from the
lesson's Brackwater Home Internet/SignalDesk hook: **Cobalt Home
Security**, a fictional home-security company. Its customer chat
assistant, **GuardLine**, walks customers through alarm troubleshooting,
pulls relevant knowledge-base articles, and can call a tool to check a
customer's account and equipment record. GuardLine calls a hosted model
API for every turn, at real per-token cost, inside a real, fixed
context-window limit. Applying the five-line ledger to a fresh scenario
is the point — recalling the lesson's answers by heart won't get you
through these.

## How to run

You'll need Python 3 installed. Check with:

```bash
python3 --version
```

Then run the starter file:

```bash
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Map failures to ledger lines** — assign the correct ledger-line ID
   to five GuardLine failure descriptions.
2. **Ledger line dependency reasoning** — decide whether one line's
   failure makes another line's problem more likely.
3. **(Production-gear) Evaluate which fixes address Conversation
   History** — given four candidate fixes, decide which ones actually
   address the Conversation History line versus a different line
   entirely.
4. **(Production-gear) Context budget arithmetic** — compute a real
   token budget for conversation history and the maximum number of full
   turns it can hold before compression must kick in.
5. **(Production-gear) Memory eviction policy selection** — pick the
   right first eviction policy for a conversation history nearing its
   budget.
6. **(Production-gear) Lost-in-the-middle ordering decision** — pick
   where a critical fact should sit in assembled context to counter the
   position effect.
7. **(Production-gear) Context-health monitor design** — name a
   concrete monitor (metric plus threshold) that would have caught a
   growing budget risk before it caused an incident.
8. **(Production-gear) Full-ledger completeness check** — confirm all
   five ledger lines were at least considered while working through
   this chapter's exercises, the same completeness gate a real team
   runs before a context-engineered feature ships.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly
to see a score report. `solution.py` is the fully filled-in reference
and scores a perfect total when run. Your own wording for the
open-ended tasks (Exercise 4's numbers must match; Exercise 7's monitor
just needs a real metric and threshold, not exact wording) is checked
for substance, not an exact string match.
