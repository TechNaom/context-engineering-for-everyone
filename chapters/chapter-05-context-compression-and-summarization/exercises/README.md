# Chapter 5 Exercises: Context Compression and Summarization

These exercises use a fresh scenario, deliberately different from the
lesson's Brannigan Home Energy Services/GridLine hook: **Kirkholme
Public Transit Safety Board**, a fictional transit safety oversight
agency. Its incident-intake assistant, **TransitLine**, handles
"Vehicle Incident Report" conversations that can run long, since a
real report often accumulates several details across many turns before
a mechanical or safety pattern emerges. Chapter 3's recipe already
fired for this request type: a compression trigger correctly kicks in
once a segment of the conversation exceeds the verbatim window, and the
resulting running summary has a fixed **480-token target**. That target
is a given here, not something to re-derive — your job is the real
compression *mechanics* that decide what survives inside it: what gets
extracted as a candidate before compressing, which strategy compresses
it, and whether the result actually preserves what was flagged.

## How to run

```bash
python3 --version
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Match scenarios to compression approaches** — decide which of
   three TransitLine scenarios need no compression at all, which show
   the naive-summarization anti-pattern, and which need the full
   fidelity-checked pipeline.
2. **Order the Compression Fidelity Recipe** — put six recipe steps in
   the correct sequence.
3. **(Production-gear) Compression ratio arithmetic** — compute how
   many tokens must be cut, and the resulting retention percentage, to
   hit the 480-token target from a raw 2,400-token segment.
4. **(Production-gear) Load-bearing candidate classification** —
   decide which of six incident-report details must be flagged as a
   candidate to preserve before compressing.
5. **(Production-gear) Fidelity check** — given a candidate list and a
   produced summary's actual contents, find which candidates are
   missing and whether the compression passes its own validation gate.
6. **(Production-gear) Extractive vs. abstractive strategy selection**
   — classify six content types by which compression strategy actually
   fits them.
7. **(Production-gear) Naive-vs-fidelity-checked regression gate** —
   confirm a load-bearing detail a naive "shrink as much as possible"
   pass would drop is correctly preserved and would be correctly
   flagged if it weren't.
8. **(Production-gear) Escalation decision** — for three fidelity-check
   outcomes, decide whether it's safe to ship the compressed result or
   whether the pipeline must retry or escalate.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly
to see a score report. `solution.py` is the fully filled-in reference
and scores a perfect total when run.
