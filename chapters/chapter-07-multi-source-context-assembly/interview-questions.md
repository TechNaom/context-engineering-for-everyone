# Chapter 7 Interview Questions: Multi-Source Context Assembly

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) ConfluenceLine had a correct budget, correct memory handling, nothing needing compression, and no positional risk. Why did it still give a wrong answer?

**Strong answer:** Chapters 1-6 all answer questions about a single
already-decided set of content: how much fits, what's kept, what
survives compression, where it sits. None of them ask whether two
different sources feeding the same request might be making incompatible
claims about the same fact. ConfluenceLine's retrieved document and its
live tool output were each individually correct and correctly included
— the failure was that nothing ever decided which one should govern
when they disagreed, or even flagged that they disagreed at all.

**Red flag:** Blames the budget, the retrieval step, or the model's own
reasoning, rather than identifying that no source-assembly decision was
ever made.

**Follow-up:** "If the team had just retrieved a fresher document, would
that have fixed the actual problem?"

**What this proves:** Understands that correct retrieval per source is
not the same as a coherent combination of sources — this chapter's
central distinction.

---

### 2. (Beginner) What does "multi-source context assembly" mean, in one sentence a non-technical stakeholder would understand?

**Strong answer:** When a request pulls information from more than one
place at once — a retrieved document, a live tool call, the
conversation, the system's own instructions — someone has to decide
which pieces belong, which one wins if two disagree, and how to avoid
saying the same thing twice, before any of it reaches the model.

**Red flag:** Describes it as simply "combining data" with no mention of
authority, contradiction, or deduplication.

**Follow-up:** "Is this the same thing as retrieval — picking which
documents to fetch in the first place?"

**What this proves:** Can distinguish source combination (this chapter)
from source production/retrieval (Chapter 8 and `rag-for-everyone`'s own
subject).

---

### 3. (Intermediate) A teammate says: "we already deduplicate identical strings across our sources, so we're covered." How do you respond?

**Strong answer:** String-level deduplication is a useful, cheap first
pass, and worth doing regardless — but it only catches exact or
near-exact duplicate text. It catches nothing when two sources disagree
about the same fact using different wording, which is exactly
ConfluenceLine's own failure: "advisory in effect" and "advisory lifted
yesterday" share no duplicate substring to strip, so string-dedup alone
would leave the contradiction fully present while the team believed
they'd addressed redundancy.

**Red flag:** Treats string-dedup as sufficient, or conflates
"deduplicated" with "contradiction-free."

**Follow-up:** "What would it take to catch two sources disagreeing in
different words, not just repeating the same words?"

**What this proves:** Understands the real gap between string-level
deduplication and semantic contradiction detection — the two are not
the same mechanism.

---

### 4. (Intermediate) How is this chapter's subject different from what Chapter 6 (Avoiding Lost-in-the-Middle) already taught?

**Strong answer:** Chapter 6 assumed the window's own content was
already decided and asked only where each already-included, already-
correct piece should sit. This chapter answers an earlier question:
which sources belong in the window at all, and how do several different
sources get combined into one coherent set — deciding authority,
resolving contradictions, deduplicating restatements — before Chapter
6's own ordering recipe ever runs on the result. A system could nail
this chapter's assembly perfectly and still get Chapter 6's ordering
wrong, or vice versa.

**Red flag:** Conflates "which sources are included and how they're
resolved" with "where included content sits," or can't say which
chapter's recipe runs first.

**Follow-up:** "If two sources contradict each other and you order the
window perfectly, have you actually fixed anything?"

**What this proves:** Can hold the sequential, complementary boundary
between Chapters 6 and 7 explicitly.

---

### 5. (Senior) You're reviewing a new multi-source assembly pipeline before it ships. What do you check beyond "every source individually returns correct data"?

**Strong answer:** Individual correctness is necessary but not
sufficient. Check that every candidate source is explicitly inventoried
and typed, not silently merged. Check that an authority ranking exists
per request type, decided in advance, not improvised per conflict.
Check that overlap and contradiction detection actually runs before
assembly, not left to the model to notice once everything is already in
the window. And check that resolution is deterministic — using the
ranking, or explicitly surfacing a disagreement authority doesn't
settle — rather than hoping the model reasons its way to the right
answer at generation time.

**Red flag:** Signs off purely because every individual source's own
data is accurate, with no scrutiny of how sources combine.

**Follow-up:** "Show me the authority ranking for this request type.
Who decided it, and when was it last reviewed?"

**What this proves:** Understands that per-source correctness is a
floor, and that assembly needs its own explicit, testable rules.

---

### 6. (Senior) How do you decide how much engineering investment a given request type's source assembly deserves?

**Strong answer:** Look at how many sources can plausibly speak to the
same fact, and what's at stake if a contradiction goes unresolved — a
safety advisory, a medication conflict, a financial figure, versus a
low-stakes FAQ answer with a single source and no real overlap risk.
Multi-source, high-stakes request types justify the full Source Assembly
Recipe: inventory, authority ranking, contradiction detection,
resolution, deduplication. A single-source or low-stakes request type
may reasonably skip most of it — the same proportionate-judgment
discipline every prior chapter's own comparison table required, applied
here to assembly investment instead.

**Red flag:** Proposes the full recipe for every request "to be safe"
with no engagement with actual overlap risk, or the reverse — skips
authority ranking for a request type where two sources clearly can
disagree about something that matters.

**Follow-up:** "Your team wants authority ranking for every request
type, no exceptions. What's the cost of that policy for a single-source
lookup?"

**What this proves:** Applies proportionate judgment consistently,
rather than treating this chapter's recipe as free or universally
required.

---

### 7. (Architect) Design a lightweight governance process so every multi-source pipeline in a production system actually gets contradiction review, not just a data-freshness review.

**Strong answer:** Require a standard artifact per request type that
pulls from more than one source: the source inventory (what each source
is, its type), the authority ranking and the reasoning behind it,
evidence that contradiction detection actually ran (not just that
individual sources passed their own health checks), and the resolution
or escalation outcome for every conflict found. Pair it with a
regression suite of known load-bearing contradictions (like
ConfluenceLine's own advisory conflict) that must resolve correctly
before a pipeline change ships, and track unresolved-contradiction and
tie/escalation rates as first-class production metrics, the same way
Chapter 6's own architect question required tracking positional-probe
failures.

**Red flag:** A process that only checks whether each source itself is
fresh and correct, with no requirement that combinations of sources were
ever tested against a known contradiction.

**Follow-up:** "A new source type gets added to the pipeline next
quarter. How does your process catch that its authority rank was never
assigned?"

**What this proves:** Architect-level judgment — treats multi-source
coherence as something that needs continuous verification as sources
change, not a one-time design decision.

---

### 8. (Architect) Leadership says: "our new model is much better at reasoning through conflicting information in its context — do we still need explicit authority ranking and conflict resolution?"

**Strong answer:** A more capable model changes the calculus but doesn't
eliminate the need. This chapter's own live-captured example shows
exactly the risk: the model reasoned its way to the correct authority
conclusion in the abstract (trust the live source over the static
document) and then gave a concrete recommendation that contradicted its
own stated reasoning. A model being generally better at reasoning about
conflicts is not the same as "tested and confirmed to reliably act on
that reasoning for our specific request type" — that claim needs an
explicit regression test against known contradictions, re-run per model,
not an assumption carried over from a general capability claim.

**Red flag:** Treats general model reasoning improvements as sufficient
replacement for a deterministic resolution step, with no engagement with
the specific failure mode (correct reasoning, inconsistent action) this
chapter's own live capture demonstrated.

**Follow-up:** "What's the smallest, cheapest test you'd run before
trusting that claim for a safety-critical request type?"

**What this proves:** Can reason about model capability improvements as
a reason to keep testing, not a reason to remove a deterministic
safeguard — the same discipline this chapter's own live capture
demonstrated concretely.

## Strategy Tips

- Ground every answer in ConfluenceLine's actual failure (every recipe
  through Chapter 6 correct, two individually correct sources
  contradicting each other with nothing deciding which should govern)
  rather than a generic "just combine your data sources" answer.
- For senior/architect questions, always name the explicit,
  deterministic resolution step specifically — it's the one piece of
  this chapter's recipe a naive "just concatenate everything" pipeline,
  or even a capable model's own unprompted reasoning, has no reliable
  equivalent of.
- If you're new to engineering interviews: reason out loud by naming
  which of this chapter's two failure-prone moments (deciding authority
  and detecting a conflict, versus actually resolving or surfacing it
  once found) a given scenario is testing, before proposing a fix.

## A note on this chapter's project

Chapter 7 does not ship its own guided project. Per this course's
one-project-per-module convention, Module 4's single project is planned
for the end of Chapter 8, once retrieval integration is also in place —
see `quality-audits/chapter-07-audit.md` for the full reasoning.
