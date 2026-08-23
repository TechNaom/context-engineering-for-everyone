# Chapter 3 Exercises: Short-Term Conversational Memory

These exercises use a fresh scenario, deliberately different from the
lesson's Emberlynn Transit Cooperative/RouteLine hook: **Quarrowstead
Legal Aid Partners**, a fictional legal aid organization. Its internal
caseworker assistant, **DocketLine**, holds long-running conversations
about an active case on a 20,000-token-context-window model. Chapter
2's recipe already ran for this request type: Line 3 (Conversation
History) was correctly allocated **6,000 tokens**. That number is a
given here, not something to re-derive — your job is the real
eviction/compression *policy* that keeps a growing conversation inside
it without silently dropping something load-bearing.

## How to run

```bash
python3 --version
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Match scenarios to short-term memory policies** — decide which of
   three DocketLine scenarios need a real eviction/compression policy at
   all, and which don't.
2. **Order the Short-Term Memory Policy Recipe** — put six policy steps
   in the correct sequence.
3. **(Production-gear) Running totals, first turn over budget** — real
   cumulative-token arithmetic across a growing conversation.
4. **(Production-gear) Verbatim window sizing** — compute how many
   recent turns can stay raw once pinned-fact and summary reserves are
   subtracted from the Line 3 budget.
5. **(Production-gear) Pin/no-pin classification** — decide which facts
   from a real case conversation are load-bearing enough to pin.
6. **(Production-gear) Compression trigger check** — find the turn where
   compression should start, ahead of the hard budget limit.
7. **(Production-gear) Build and validate the final memory package** —
   verify pinned facts + summary + verbatim turns fit inside budget.
8. **(Production-gear) Naive-vs-hybrid regression gate** — confirm a
   pinned fact that a naive FIFO policy would drop survives under the
   hybrid policy, the exact gap the lesson's hook fell into.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly
to see a score report. `solution.py` is the fully filled-in reference
and scores a perfect total when run.
