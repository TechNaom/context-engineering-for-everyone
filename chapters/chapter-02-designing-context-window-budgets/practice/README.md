# Chapter 2 Practice Bank: Designing Context Window Budgets

Eight short, independent scenarios, each its own fictional system —
none of them Vantry Health Network/TriageLine or Corravine Freight/
DispatchLine again. Each scenario is a few sentences and one judgment
or arithmetic question about *allocating* a budget, not diagnosing one
already broken. The point isn't depth on one system (that's what the
exercises did) — it's speed and accuracy across many different
systems, the way a real pre-launch budget review actually feels.

## How to run

```bash
python3 starter.py
```

Fill in each `# TODO`, re-run, and watch your score climb.

## The eight scenarios

1. **Marrenkirk Insurance Group** — matching a new, document-dominated
   claim-review request type to the right archetype profile.
2. **Duvane Utilities Cooperative** — a team that never reserved a
   Working Space allowance at all.
3. **Graytide Hospitality Group** — a team that split Lines 2/3/4 before
   subtracting Line 1, not after.
4. **Oakspire Home Care Network** — a team that validated only against
   average-case conversations, never the worst realistic case.
5. **Corundale Media Group (judgment)** — does a much bigger context
   window make per-request-type allocation unnecessary?
6. **Pallisade Manufacturing (judgment)** — is a matching archetype
   profile alone enough to safely copy one request type's exact token
   budget onto another?
7. **Redcliff Credit Union (production-gear)** — real arithmetic: derive
   a Grounding Context token allocation from a window, reservations, and
   a named profile.
8. **Thackery Regional Exchange (production-gear)** — identify which
   single ledger line is genuinely under-provisioned given real
   allocated-vs-actual numbers.

## Checking your work

`score()` in both `starter.py` and `solution.py` grades your answers
automatically. `solution.py` scores a perfect 8/8.
