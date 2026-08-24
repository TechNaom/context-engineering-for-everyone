# Chapter 12 Interview Questions: Evaluating Context Quality

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) Ternfield's ClaimLens pipeline followed every one of Chapters 1-11's own recipes correctly. Why did it still produce a wrong determination?

**Strong answer:** Every per-step check those recipes define passed —
the budget fit, the source was fresh, nothing overflowed, nothing leaked
across an isolation boundary, and the decisive medical exam was
correctly retrieved into the bundle. What never happened is a check on
the *finished* bundle as a single artifact: whether the one fact this
specific case turns on was easy for the model to actually use, not just
technically present somewhere inside a much longer document. Correctness
at every step of assembly doesn't automatically compose into a good
finished result, because no per-step recipe was ever built to check the
result.

**Red flag:** Says the pipeline must have had a bug in one of Chapters
1-11's own recipes, or argues that following every recipe correctly
should have been sufficient — missing that this chapter's own checks are
a genuinely new, additional layer, not a re-run of any earlier chapter's
own check.

**Follow-up:** "If the exam result had been placed at the very start of
the bundle instead of buried in the middle of a long medical-records
block, would that alone have been enough to fix the case?"

**What this proves:** Understands that per-step correctness and
finished-bundle quality are two separate claims — this chapter's central
distinction.

---

### 2. (Beginner) What does "evaluating context quality" mean, in one sentence a non-technical stakeholder would understand?

**Strong answer:** Checking the actual information handed to the model
before it answers — does it contain everything the specific question
needs, is it cluttered with material that doesn't belong, and is the
most important fact placed somewhere the model is likely to notice it —
rather than assuming a system that was built correctly will always hand
the model a good set of information.

**Red flag:** Describes this as "testing whether the model's answer is
right," conflating it with output evaluation, or describes it as just
"making sure nothing broke," with no mention of completeness, noise, or
position specifically.

**Follow-up:** "Is checking whether the model's final answer was correct
the same thing as checking whether the context it was given was good?"

**What this proves:** Distinguishes evaluating the model's input from
evaluating the model's output, the chapter's own core boundary.

---

### 3. (Intermediate) A teammate says: "our RAG pipeline retrieved the right document and it's inside the token budget, so our context is good." How do you respond?

**Strong answer:** Retrieving the right document and fitting a budget
are both real and worth confirming, but neither one checks whether the
*specific fact* the current request needs is actually present and
easy for the model to use. Ternfield's own hook shows exactly this gap:
the right medical-records source was retrieved, and the bundle fit its
budget the entire time, and the determination was still wrong, because
nobody checked fact-level completeness, measured a real noise ratio, or
audited where the decisive fact actually landed.

**Red flag:** Treats "the right source was retrieved" or "it fits the
budget" as equivalent to "the context is complete and well-ordered," or
assumes a source-presence check is the same as a fact-presence check.

**Follow-up:** "If that same document were 3,000 tokens long and the
one sentence that answers the question were in the middle of it, would
your current checks catch that?"

**What this proves:** Understands the real gap between retrieval/budget
correctness and this chapter's own fact-level completeness, noise, and
positional checks.

---

### 4. (Intermediate) How is this chapter's subject different from what Chapters 1-11 already cover?

**Strong answer:** Chapters 1-11 are all about *producing* a context
bundle correctly, one concern at a time — budgeting it, keeping it
fresh, compressing it, ordering sources, assembling multiple sources,
retrieving and curating results, scoping a tool call, scoping a
pipeline, and isolating context where isolation is the right call. This
chapter is the first to ask whether the *finished* bundle, built by all
of that correctly, is actually good — checked as its own artifact
against fact-level completeness, a real noise ratio, and where the
load-bearing facts landed, combined into one gate run before the model
ever sees it.

**Red flag:** Says the chapters are "basically the same because they're
both about context," without naming the specific distinction (producing
context correctly vs. measuring the finished result).

**Follow-up:** "If a pipeline correctly implements every recipe through
Chapter 11, does that guarantee this chapter's own quality gate would
pass?"

**What this proves:** Can articulate that this chapter checks the
output of Chapters 1-11's own combined process, not a re-application of
any one of their recipes.

---

### 5. (Senior) You're reviewing a context-evaluation gate before it ships. What do you check beyond "does it report a pass/fail score"?

**Strong answer:** Whether completeness is scored against a specific,
per-case list of required facts rather than a proxy like source
presence (Step 1 and Step 2); whether the noise ratio measures content
that's genuinely irrelevant to this request rather than just staying
under budget (Step 3); whether the positional audit checks where every
required fact actually landed against real primacy/recency research
rather than assuming ordering was handled once at assembly time (Step
4); whether all three checks are combined into a single gate rather than
any one being treated as sufficient on its own (Step 5); and whether the
gate re-runs whenever the assembly pipeline itself changes rather than
being checked once at launch (Step 6). A gate that reports "source
present, budget fits" can look green while missing everything this
chapter actually checks.

**Red flag:** Treats "the gate returns a score" as sufficient evidence
the gate is measuring the right things, without asking what it actually
measures completeness, relevance, and ordering against.

**Follow-up:** "Walk me through what specific facts your own gate's own
completeness check requires for one real request type, and how you
decided that list."

**What this proves:** Reviews evaluation gates for what they actually
measure, not just whether they produce a score.

---

### 6. (Senior) A teammate proposes using an LLM to check context completeness by asking it "does this contain everything needed?" How do you respond?

**Strong answer:** That's real and automatable, but this chapter's own
live captures showed it fails in a specific, reproducible way: asking a
model to *reason* about a derived condition (e.g., "is this within the
last 30 days") produced a false negative on a fact that was plainly
present in the text, twice in a row, while phrasing the identical
underlying check as a literal scan-and-quote instruction worked
immediately. An open-ended "does this contain everything needed"
question is exactly the reasoning-style phrasing that failed — a
reliable LLM-based completeness check has to be scoped as narrowly as
the deterministic presence check it's standing in for, not asked to
judge sufficiency in the abstract.

**Red flag:** Assumes an LLM-based completeness check is reliable by
default, or dismisses LLM-assisted checking as never worth trying rather
than naming the specific phrasing distinction that made the difference.

**Follow-up:** "If your completeness checker needs to check for ten
different required facts, would you ask one open-ended question or ten
narrow ones?"

**What this proves:** Understands both the real potential and the real,
demonstrated failure mode of LLM-assisted context checking, not just an
optimistic or dismissive default.

---

### 7. (Architect) Design a lightweight governance process so every context-assembly pipeline in a production system actually gets evaluated before shipping, not just built correctly.

**Strong answer:** A short checklist attached to each pipeline's own
design review, distinct from an ordinary assembly or retrieval review:
(1) is there a per-request-type list of required facts, defined before
assembly, not inferred from source categories after the fact; (2) does
a completeness check run against that literal list; (3) is a real noise
ratio computed, measuring irrelevant content specifically, not just
confirming the bundle fits its budget; (4) is a positional audit run
against every required fact, flagging high-priority facts landing in a
degraded middle zone; (5) are all three checks combined into a single
pass/fail gate that blocks the call on any one failure, not just
reported as separate metrics; (6) is there a trigger to re-run the gate
whenever the assembly pipeline itself changes (a new source, a
retrieval-query change, a reordered template). Each item should be
checkable against the pipeline's own code, the same way this chapter's
own `context_evaluation_recipe.py` asserts completeness, noise, and
position directly rather than describing them only in a design doc.

**Red flag:** Proposes a checklist that only checks whether an
evaluation step exists at all, without requiring it to check fact-level
completeness, a real noise ratio, and position specifically — or one
that treats "reviewed once before launch" as sufficient without a
re-verification trigger.

**Follow-up:** "How would this checklist have caught Ternfield's own
ClaimLens failure before it shipped?"

**What this proves:** Designs governance that catches all three of this
chapter's own failure modes together, assertable against real code, not
a one-sided or metric-without-a-gate checklist.

---

### 8. (Architect) Leadership says: "we already have a golden-set evaluation harness grading our model's own final answers — do we still need to evaluate context separately?"

**Strong answer:** Yes, for a reason this chapter's own hook makes
concrete: a golden-set harness grades the model's own generated output
against a reference answer, after generation — useful, but it tells you
the system got a specific case wrong, not *why*, and specifically not
whether the cause was a bad context bundle the model reasoned correctly
from. Ternfield's own case would fail a golden-set check (wrong
determination) without ever revealing that the actual defect was a
completeness gap in the assembled context, not a reasoning failure in
the model. Evaluating context catches the defect before the call, at
the layer where it actually originated, and evaluating output catches a
different, later-stage set of problems (a poorly reasoned or poorly
phrased answer built from genuinely good context) — the two disciplines
are complementary, not substitutes for each other.

**Red flag:** Treats output evaluation as a superset of context
evaluation, or assumes that if the golden-set harness is passing overall,
the context feeding it must already be good.

**Follow-up:** "If a golden-set check flags a wrong answer, how would you
determine whether the cause was a context defect or a reasoning defect,
without a separate context-evaluation gate?"

**What this proves:** Distinguishes evaluating a system's input from
evaluating its output as two necessary, non-overlapping disciplines,
rather than treating one as a stand-in for the other.
