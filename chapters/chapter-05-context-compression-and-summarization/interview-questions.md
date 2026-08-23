# Chapter 5 Interview Questions: Context Compression and Summarization

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) GridLine had a correct budget, a correct compression trigger, and a correct pin/summary/window shape. Why did it still lose a load-bearing detail?

**Strong answer:** Chapter 3's recipe decided *when* to compress and
*what shape* the result should take, but never specified *how* the
compression call itself decides what to keep. GridLine's actual
compression step was a single "summarize as concisely as possible"
prompt with no pre-extraction of important details and no check
afterward on what survived. The detail that got lost — a cross-turn
correlation between meter resets and furnace timing — wasn't
individually pin-worthy or write-worthy, so nothing else in the
pipeline was watching for it either.

**Red flag:** Blames the budget, the trigger, or Chapter 3's recipe
itself, rather than identifying the compression call's own lack of a
fidelity check.

**Follow-up:** "If GridLine's team just told the model 'don't lose
anything important' in the summarization prompt, would that have fixed
it?"

**What this proves:** Understands the precise boundary between what
Chapter 3 already engineered (trigger, shape) and what this chapter
engineers (the compression call's own decision procedure).

---

### 2. (Beginner) What's the difference between a fact that's "pin-worthy" and a detail that's "load-bearing but not pin-worthy"?

**Strong answer:** A pin-worthy fact (Chapter 3) is a single, discrete
fact important enough to protect explicitly and individually — a
safety disclosure, for example. A load-bearing-but-not-pin-worthy
detail is something that only matters in combination with other
details, or only becomes clear across several turns — like GridLine's
furnace-timing correlation, which no single turn revealed on its own.
Compression is exactly where this second category is at risk, because
nothing else in the pipeline is individually protecting it.

**Red flag:** Treats the two categories as the same thing, or claims
pinning alone is sufficient to protect everything that matters in a
long conversation.

**Follow-up:** "Give an example of a detail that would never get
pinned under Chapter 3's own criteria but that a compression step
still needs to preserve."

**What this proves:** Understands why this chapter's own subject
exists as a distinct concern from Chapter 3's pinning mechanics.

---

### 3. (Intermediate) A teammate says: "let's just tell the model 'don't lose anything important' in the compression prompt." What's wrong with relying on that alone?

**Strong answer:** An instruction inside the prompt is a request, not a
guarantee — the chapter's own live capture showed a model that
correctly excluded a literal PIN value while still leaking that a PIN
existed and its format, a real example of partial instruction-
following. Relying on instruction text alone gives no independent way
to verify the result, and it gives the compression call no explicit
definition of what "important" means for this specific content.
Deciding what's load-bearing has to happen deterministically, before
compression, as its own extraction step — and checking it has to
happen deterministically, after compression, as its own validation
step — not be delegated entirely to the compression call's own
judgment.

**Red flag:** Treats a well-worded prompt as sufficient protection with
no separate extraction or validation step.

**Follow-up:** "Your fidelity check just found a missing candidate.
Walk me through exactly what happens next in your pipeline."

**What this proves:** Understands that this chapter's recipe is
deterministic scaffolding around a probabilistic call, not trust placed
in the call itself — the same discipline Chapters 3 and 4 already
established for pinning and write criteria.

---

### 4. (Intermediate) How is this chapter's subject different from what `rag-for-everyone` teaches about chunking documents?

**Strong answer:** `rag-for-everyone` chunks source documents ahead of
time, before retrieval, to make them searchable and rankable. This
chapter compresses content that is already inside a request's context —
a conversation history, a tool result, a retrieved excerpt already
pulled in — because it no longer fits the budget available for it. A
retrieval system can chunk and rank a document perfectly and still hand
a context assembler an excerpt that later needs compressing to fit a
specific request's budget; that second step, regardless of how the
content arrived, is this chapter's own subject.

**Red flag:** Conflates chunking-for-retrieval with compressing-
already-in-context content, or can't name which course owns which step.

**Follow-up:** "If your retriever returns a perfectly ranked 3,000-token
excerpt but your request only has 500 tokens of budget left for it,
whose problem is that?"

**What this proves:** Can hold the boundary between adjacent courses
explicitly, the same discipline every prior chapter's own lesson
modeled.

---

### 5. (Senior) You're reviewing a new compression step before it ships. What do you check beyond "does the output fit the token target"?

**Strong answer:** Fitting the target is necessary but not sufficient.
Check that a real extraction pass runs before compression and produces
an explicit, reviewable candidate list — not an implicit assumption
that the model will figure out what matters. Check that the compression
strategy is actually matched to content type (extractive for anything
where exact wording matters, abstractive only where paraphrase is
genuinely safe). And specifically check the fidelity-validation step:
what happens when a candidate is missing, and confirm the pipeline
fails closed (retry, widen, or escalate) rather than shipping a
possibly-lossy result silently.

**Red flag:** Signs off purely because the output length is correct,
with no scrutiny of whether anything checks the output's actual
content.

**Follow-up:** "Show me the exact code path that runs when your
fidelity check finds a missing candidate. What happens if that path
never fires?"

**What this proves:** Understands that hitting a token target is a
floor, and that the validation step is the one piece of this chapter's
recipe a naive pipeline has no equivalent of at all.

---

### 6. (Senior) How do you decide whether a piece of content needs the full fidelity-checked pipeline versus naive summarization is acceptable?

**Strong answer:** Look at whether anything downstream — a diagnosis, a
recommendation, a compliance decision, a financial instruction —
actually depends on specific details surviving the compression intact.
If the compressed output only ever informs a human's casual sense of
"what happened so far" with no consequential decision riding on any
specific detail, naive summarization's risk may be genuinely
acceptable. The moment a real decision depends on the compressed
result, the fidelity-checked pipeline is required, because naive
summarization has no way to guarantee — or even detect — that it
preserved what mattered.

**Red flag:** Proposes the full fidelity-checked pipeline for
everything "to be safe" with no engagement with the actual cost of
building and maintaining an extraction/validation step for low-stakes
content, or the reverse — accepts naive summarization for content a
real decision clearly depends on.

**Follow-up:** "Your team says every compression step should use the
full pipeline, no exceptions. What's the cost of that decision, and is
it justified for a casual FAQ chatbot's own summary?"

**What this proves:** Applies proportionate judgment, the same
discipline Chapter 3 required for its own pin-vs-no-pin and hybrid-vs-
nothing decisions, applied here to the extraction/validation
investment itself.

---

### 7. (Architect) Design a lightweight governance process so every compression step in a production system actually has a fidelity check, not just a token-length check.

**Strong answer:** Require a standard artifact per compression step: the
explicit candidate-extraction logic (what counts as load-bearing for
this content type, and why), the chosen strategy (extractive or
abstractive) and its justification, the explicit target, and evidence
the fidelity-validation gate was tested against at least one scenario
where a candidate was deliberately dropped, confirming the gate
actually catches it rather than silently passing. Pair it with an
automated check that flags any compression call in the codebase with no
corresponding candidate-extraction step on file — the exact gap
GridLine shipped with. Track fidelity-check failure rates in production
as a first-class metric, the way error rates are tracked elsewhere, not
treated as a "should never happen" edge case with no monitoring.

**Red flag:** A process that only checks a token-length limit exists,
with no requirement that the validation gate itself was ever tested
against a known-bad input.

**Follow-up:** "How would you catch a fidelity check that exists in the
code but has quietly stopped actually failing anything, even when it
should?"

**What this proves:** Architect-level judgment — treats the validation
gate itself as something that needs its own test coverage, not just
trusted once written, and connects this to the same "silently rotting
safeguard" risk Chapter 4's own architect question raised for staleness
handling.

---

### 8. (Architect) Leadership says: "our model has a huge context window now — do we even need compression anymore?" How do you respond?

**Strong answer:** A larger context window changes the calculus but
doesn't eliminate it. Real documentation for large-context models
themselves acknowledges this tradeoff directly, noting smaller-context
models "often require strategies like arbitrarily dropping old
messages, summarizing content... or filtering prompts to save tokens,"
while very large context windows sometimes invite "providing all
relevant information upfront" instead. But cost, latency, and this
course's own recurring "lost in the middle" concern (Chapter 6's own
subject) don't disappear just because a window is technically large
enough to hold everything — a huge window that's mostly filled with
uncompressed, unprioritized history can still degrade the reliability
of what the model actually attends to, even if nothing gets literally
truncated. The right answer is that a bigger window raises the bar for
when compression is worth the engineering cost, not that it removes the
need for this chapter's discipline entirely.

**Red flag:** Claims a large context window makes compression obsolete
across the board, with no engagement with cost, latency, or attention-
reliability tradeoffs.

**Follow-up:** "If cost and latency were both zero, would you still
ever choose to compress something before sending it to the model?"

**What this proves:** Can reason about compression as an engineering
tradeoff with multiple real dimensions (cost, latency, fidelity,
attention reliability), not a binary "needed" or "not needed" driven by
window size alone.

## Strategy Tips

- Ground every answer in GridLine's actual failure (every recipe
  through Chapter 4 correct, one uncontrolled compression call) rather
  than a generic "always preserve important information" answer.
- For senior/architect questions, always name the fidelity-validation
  gate specifically — it's the one piece of this chapter's recipe a
  naive pipeline has no equivalent of at all, and interviewers will
  notice if you skip straight to "use a better prompt."
- If you're new to engineering interviews: reason out loud by naming
  which of this chapter's two failure-prone steps (extraction before
  compressing, validation after) a given scenario is actually testing,
  before proposing a fix.
