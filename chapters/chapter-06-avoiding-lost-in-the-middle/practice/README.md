# Chapter 6 Practice Bank: Avoiding Lost-in-the-Middle

Eight short, independent scenarios, each its own fictional system —
none of them Marchside Regional Trauma Network/VitalsLine or Calverton
Public Defender's Office/DocketLine again. Each scenario is a few
sentences and one judgment or arithmetic question about *where already-
included, already-fidelity-checked content should sit in the assembled
window*, not deciding what belongs in the window at all (that's Chapters
2-5's job) or how several sources combine (that's Chapter 7's job). The
point is speed and accuracy across many different systems, the way a
real context-assembly review actually feels.

## How to run

```bash
python3 starter.py
```

Fill in each `# TODO`, re-run, and watch your score climb.

## The eight scenarios

1. **Nunroth Independent Bookstore Cooperative (judgment)** — does
   moving every fact to the front of the window alone guarantee the
   model uses it, or does the query still need its own anchor?
2. **Vesparro Marine Salvage (production-gear)** — position-percentile
   arithmetic for a fact inside a 4,000-token window.
3. **Holstead Grain Exchange (judgment)** — is a passed Chapter 5
   fidelity check alone sufficient proof of reliable positional use?
4. **Quenby Historical Archive Society (production-gear)** — find
   which anchor-required facts are missing from a produced window's
   actual placements, and whether the probe passes.
5. **Farrowline Dairy Cooperative (judgment)** — does the effect's
   exact shape stay identical across every model and context length,
   or does it need re-testing?
6. **Delacroix Regional Airport Authority (production-gear)** — a
   query-anchor classification call on a specific content type.
7. **Pennwhistle Community Radio Network (production-gear)** — an
   arrival-order-vs-weight-ranked regression check on a specific
   detail.
8. **Ostergaard Marine Insurance (judgment)** — if a positional probe
   fails once, is it safe to just re-run the exact same arrival-order
   pipeline again unchanged?

## Checking your work

`score()` in both `starter.py` and `solution.py` grades your answers
automatically. `solution.py` scores a perfect 8/8.
