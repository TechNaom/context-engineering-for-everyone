# Chapter 1 Practice Bank: The Context Budget

Eight short, independent scenarios, each its own fictional system — none
of them Brackwater Home Internet/SignalDesk or Cobalt Home
Security/GuardLine again. Each scenario is a few sentences and one
judgment question. The point isn't depth on one system (that's what the
exercises did) — it's speed and accuracy across many different systems,
the way a real context-engineering review actually feels.

## How to run

```bash
python3 starter.py
```

Fill in each `# TODO`, re-run, and watch your score climb.

## The eight scenarios

1. **Windermere Legal Services** — a system prompt bloated with a year
   of accumulated, unpruned boilerplate.
2. **Pinecrest Veterinary Group** — stale retrieved articles never
   evicted from the request.
3. **Solmark Payments** — an unsummarized transcript exceeds the window
   and the earliest turns are silently dropped.
4. **Thistledown Air Cargo** — no persistent memory layer; a fact from
   an earlier session is never recalled later.
5. **Ravenhollow University Registrar (judgment)** — does sending the
   full transcript only during low-traffic hours actually fix an
   unbounded-history problem?
6. **Copperfield Home Appliances (judgment)** — prioritize between two
   real but unequal gaps, only one fixable before launch.
7. **Marrowgate Public Library (production-gear)** — pick the one
   investment that actually builds Grounding Context discipline.
8. **Fenwick Outdoor Adventures (production-gear)** — name both ledger
   lines most directly missing from a "the model just remembers"
   shipping process.

## Checking your work

`score()` in both `starter.py` and `solution.py` grades your answers
automatically. `solution.py` scores a perfect 8/8.
