# Chapter 6 Interview Questions: Avoiding Lost-in-the-Middle

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) VitalsLine had a correct budget, correct pinning, a correct long-term recall policy, and a correct fidelity-checked compression pipeline. Why did it still miss a load-bearing allergy fact?

**Strong answer:** Chapters 1-5 all answer questions about *presence* —
is the fact in the budget, was it evicted, was it persisted and
recalled, did it survive compression intact. None of them decide
*where* a correctly-included fact ends up in the final assembled
window. VitalsLine's allergy fact was present, unmodified, and within
budget — it simply landed near the 40th percentile of the window with
nothing deciding that was a bad position for safety-critical content.

**Red flag:** Blames the budget, the recall policy, or the compression
step, rather than identifying that nothing in the pipeline ever made a
positional decision.

**Follow-up:** "If the team just added more pinning to protect the
allergy fact, would that have fixed the actual problem?"

**What this proves:** Understands the precise boundary between what
Chapters 1-5 already engineer (what's in the window) and what this
chapter engineers (where it sits once it's there).

---

### 2. (Beginner) What does "lost in the middle" actually mean, in one sentence a non-technical stakeholder would understand?

**Strong answer:** A model's ability to reliably use information from a
long context isn't the same everywhere in that context — it's most
reliable for information near the beginning or the end, and measurably
less reliable for information sitting in the middle, even when nothing
about that information is missing, shortened, or ambiguous.

**Red flag:** Describes it as a truncation or token-limit problem
(that's Chapters 2-3's subject) rather than a positional-reliability
problem within content that's already fully present.

**Follow-up:** "Is this the same thing as the context window being too
small?"

**What this proves:** Can articulate this chapter's central distinction
— presence versus reliable use — without conflating it with earlier
chapters' subjects.

---

### 3. (Intermediate) A teammate says: "we already re-verified this back in 2023 with Liu et al. — it's a solved, well-known finding, no need to re-check it." How do you respond?

**Strong answer:** The core claim still holds, but treating a single
2023 paper as permanently settled skips real, newer information. A 2024
paper ("Found in the Middle") identified the mechanistic cause — an
intrinsic U-shaped attention bias — and showed it's partially
correctable, not just present. A 2025 report (Chroma's "Context Rot")
confirmed the effect persists on today's frontier models, not just
2023-era ones, but also found a genuine nuance the original paper didn't
isolate: models performed better on shuffled than structurally coherent
long contexts in that study. Treating any single paper, however
well-established, as the final word skips real refinements that change
how you'd actually engineer around the problem.

**Red flag:** Either dismisses the original finding as outdated without
engaging with what's actually changed, or defends it as unchanged
without being able to name what the newer research actually adds.

**Follow-up:** "What would make you re-check this finding again in the
future?"

**What this proves:** Applies the same "re-verify, don't assume a
citation is still good" discipline this course applies to its own
citations, specifically to the finding this chapter is built on.

---

### 4. (Intermediate) How is this chapter's subject different from what Chapter 7 (Multi-Source Context Assembly) will teach?

**Strong answer:** This chapter assumes the set of content going into
the window is already decided — every source has already been selected,
and this chapter only asks where inside the window each piece should
sit. Chapter 7 answers an earlier question: which sources belong at
all, and how do several different sources (retrieved documents, tool
output, conversation history, system instructions) get combined into
one window without contradicting or crowding each other out. A system
could nail Chapter 7's assembly perfectly and still get this chapter's
ordering wrong, or vice versa — they're sequential, complementary
decisions, not the same decision under two names.

**Red flag:** Conflates "which sources are included" with "where
included content sits," or can't articulate which chapter owns which
question.

**Follow-up:** "If your retriever returns three perfectly relevant
documents, does this chapter's recipe tell you which three to pick?"

**What this proves:** Can hold the boundary between adjacent chapters
explicitly, the discipline every prior chapter's own lesson modeled.

---

### 5. (Senior) You're reviewing a new context-assembly pipeline before it ships. What do you check beyond "is every load-bearing fact somewhere in the window"?

**Strong answer:** Presence is necessary but not sufficient. Check that
content is explicitly ranked by load-bearing weight, not just
concatenated in arrival order. Check that both anchor positions (start,
and the position nearest generation) are reserved for the
highest-weight content and the active query, respectively — not
crowded out by an undifferentiated front-loaded block. And specifically
check for an explicit positional probe: has anyone actually tested that
a known load-bearing fact, placed at a middle position, is still
reliably retrieved by the live system — not just assumed from a
research paper, however credible?

**Red flag:** Signs off purely because every fact is technically
somewhere in the window, with no scrutiny of whether placement was ever
a deliberate decision or a positional probe was ever run.

**Follow-up:** "Show me the actual positional-probe result for this
pipeline's highest-stakes fact. When was it last run, and against which
model?"

**What this proves:** Understands presence is a floor, and that an
explicit, re-run positional probe is the one piece of this chapter's
recipe a naive "just concatenate everything" pipeline has no equivalent
of at all.

---

### 6. (Senior) How do you decide how much engineering investment a given window's ordering deserves?

**Strong answer:** Look at what's actually at stake if content in the
middle gets missed — a clinical decision, a legal filing, a financial
recommendation, versus a casual FAQ answer with no real cost to a
partial miss. High-stakes windows justify the full recipe: explicit
weight ranking, reserved anchors, deliberate middle reordering, and a
tested positional probe re-run per model. Low-stakes windows may
reasonably accept arrival order's risk, the same proportionate-judgment
discipline Chapter 5 required for its own fidelity-checked-pipeline-
versus-naive-summarization decision, applied here to ordering
investment instead of compression investment.

**Red flag:** Proposes the full recipe for every window "to be safe"
with no engagement with the actual engineering cost, or the reverse —
accepts arrival order for a window a real decision clearly depends on.

**Follow-up:** "Your team says every window needs a positional probe,
no exceptions. What's the cost of that policy, and is it justified for
an internal FAQ bot?"

**What this proves:** Applies proportionate judgment consistently
across chapters, not treating this chapter's recipe as free.

---

### 7. (Architect) Design a lightweight governance process so every context-assembly pipeline in a production system actually gets a positional review, not just a token-budget review.

**Strong answer:** Require a standard artifact per assembly pipeline:
the explicit weight-ranking logic (what counts as high load-bearing
weight for this window type, and why), which content is assigned to
each anchor and why, and evidence a positional probe was run against a
deliberately middle-placed, known load-bearing fact and passed — not
just that the pipeline compiles and fits its token budget. Pair it with
an automated regression check that re-runs the positional probe on
every model swap or meaningful context-length change, since this
chapter's own re-verified research shows the effect's exact shape is
model- and length-specific. Track positional-probe failure rates as a
first-class production metric, the same way Chapter 5's own architect
question required tracking fidelity-check failures.

**Red flag:** A process that only checks token budget and content
presence, with no requirement that positional placement was ever tested
against a known-bad arrangement.

**Follow-up:** "A model provider silently updates their model behind
the same API version string. How would your process catch that this
invalidates your last positional probe?"

**What this proves:** Architect-level judgment — treats positional
reliability as something that needs continuous verification tied to
the specific model in production, not a one-time check against a
research paper.

---

### 8. (Architect) Leadership says: "our new model has a much larger context window and, per this course's own Chapter 5 citation, seems to handle long documents better overall — do we still need explicit ordering logic?"

**Strong answer:** A larger, more capable context window changes the
calculus but doesn't eliminate the need. This chapter's own
re-verification found the effect persists on today's frontier models —
Chroma's 2025 study tested 18 current models, including large-context
frontier systems, and still found non-uniform reliability by position.
A bigger or more capable window may shrink the effect's magnitude for
that specific model, but "seems to handle it better" is not the same as
"has been tested and confirmed to handle it reliably for our specific
load-bearing content" — that claim needs this chapter's own positional
probe, re-run against the new model, not an assumption carried over
from the old one or from general capability claims.

**Red flag:** Treats a larger or more capable context window as
sufficient proof the ordering problem no longer applies, with no
engagement with this chapter's own re-verified 2025 evidence that it
persists on frontier models.

**Follow-up:** "What's the smallest, cheapest test you'd run before
trusting that claim for a safety-critical window?"

**What this proves:** Can reason about model capability improvements as
a reason to re-test, not a reason to skip testing — the same discipline
this chapter's own re-verification section modeled for a three-year-old
research citation.

## Strategy Tips

- Ground every answer in VitalsLine's actual failure (every recipe
  through Chapter 5 correct, one un-engineered positional decision)
  rather than a generic "keep important things near the top" answer.
- For senior/architect questions, always name the positional-probe step
  specifically — it's the one piece of this chapter's recipe a naive
  "just concatenate everything" pipeline has no equivalent of at all.
- If you're new to engineering interviews: reason out loud by naming
  which of this chapter's two failure-prone moments (deciding weight
  and anchor placement, versus testing that placement actually worked)
  a given scenario is testing, before proposing a fix.
