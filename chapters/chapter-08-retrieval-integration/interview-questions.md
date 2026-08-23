# Chapter 8 Interview Questions: Retrieval Integration

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) CiteLine's retriever ranked the right qualifying clause second out of five chunks. Why did the assistant still miss it?

**Strong answer:** The retriever did its job correctly — relevance
ranking and scoring is not this chapter's problem. The failure was
downstream: the pipeline always took a fixed top-k of chunks and then
truncated the assembled text by raw character count wherever the budget
happened to run out, with no awareness that it was cutting through the
middle of the one chunk that actually decided the answer. Correct
ranking within a retriever's own output is not the same as a
well-formed context block built from that output.

**Red flag:** Blames the retriever, the embedding model, or the ranking
algorithm, rather than the integration step that mishandled correctly-
ranked output.

**Follow-up:** "If the team had retrained the retriever to rank the
clause first instead of second, would that have fixed the actual
problem?"

**What this proves:** Understands that correct retrieval ranking is not
the same as a well-formed context source — this chapter's central
distinction.

---

### 2. (Beginner) What does "retrieval integration" mean, in one sentence a non-technical stakeholder would understand?

**Strong answer:** A retriever hands back a ranked list of scored text
fragments, not a finished answer — someone has to decide which
fragments are actually relevant enough to keep, make sure none of them
get cut off mid-sentence to fit a budget, keep track of where each piece
came from, and stitch back together fragments that were really one
continuous passage before any of it reaches the model.

**Red flag:** Describes it as simply "formatting the search results,"
with no mention of relevance filtering, boundaries, or provenance.

**Follow-up:** "Is this the same thing as building the search index or
choosing the embedding model?"

**What this proves:** Can distinguish the integration handoff (this
chapter) from retrieval architecture itself (`rag-for-everyone`'s own
subject).

---

### 3. (Intermediate) A teammate says: "we already filter out chunks below a relevance score, so our retrieval pipeline is solid." How do you respond?

**Strong answer:** A relevance floor is a real, worthwhile improvement
over unconditional top-k stuffing, and worth keeping — but it doesn't
address budget-fit truncation or chunk stitching. CiteLine's own second
live capture showed exactly this gap: even with the three genuinely
irrelevant chunks correctly excluded, nothing about a relevance floor
prevents a tight budget from truncating a surviving, relevant chunk
mid-clause, or leaves two adjacent passages of the same document
correctly separate when they should be merged into one.

**Red flag:** Treats relevance filtering as sufficient on its own, or
conflates "irrelevant chunks excluded" with "well-formed context."

**Follow-up:** "What happens in your pipeline right now if two
surviving, relevant chunks are the same paragraph split by the chunker?"

**What this proves:** Understands the real gap between relevance
filtering and the rest of the integration recipe — the two solve
different problems.

---

### 4. (Intermediate) How is this chapter's subject different from what Chapter 7 (Multi-Source Context Assembly) already taught?

**Strong answer:** Chapter 7 assumed every candidate source — including
a retrieved document — was already well-formed by the time it reached
its own inventory step, and asked how several such sources combine
without contradicting each other. This chapter answers an earlier
question specific to one of those sources: given a retriever's raw
ranked, scored chunk list, how does it become the single well-formed
source Chapter 7's Step 1 is entitled to assume it already has? A
pipeline could nail this chapter's integration perfectly on a
single-source request and never even reach Chapter 7's multi-source
problem, or vice versa on a request with only one, already-clean source.

**Red flag:** Conflates "shaping one retriever's own output" with
"combining several sources," or can't say which chapter's recipe runs
first on a retrieved document specifically.

**Follow-up:** "If two well-formed retrieved sources from two different
retrievers still disagree with each other, which chapter's recipe
handles that?"

**What this proves:** Can hold the sequential, complementary boundary
between this chapter and Chapter 7 explicitly — this chapter's output
feeds Chapter 7's input for exactly one source type.

---

### 5. (Senior) You're reviewing a new RAG pipeline before it ships. What do you check beyond "the retriever returns the right documents, ranked correctly"?

**Strong answer:** Correct ranking is necessary but not sufficient.
Check that a relevance floor is applied on purpose, not just "whatever
top-k happens to be configured." Check that the budget fit stops at
chunk boundaries, never truncating a surviving chunk mid-sentence. Check
that provenance (source document, section, score) survives into the
final context block, not just raw text. Check that consecutive chunks
from the same document get recognized and stitched rather than left as
disconnected fragments. And check that an empty or low-confidence result
is surfaced honestly as its own outcome, not silently backfilled with
the best available but still-irrelevant chunk.

**Red flag:** Signs off purely because retrieval precision/recall
metrics look good, with no scrutiny of what happens between retrieval
and the model actually receiving the text.

**Follow-up:** "Walk me through what your pipeline does today when
every retrieved chunk for a query scores below your relevance floor."

**What this proves:** Understands that retrieval quality is a floor, and
integration needs its own explicit, testable rules downstream of it.

---

### 6. (Senior) How do you decide how much engineering investment a given request type's retrieval integration deserves?

**Strong answer:** Look at how tight the token budget typically is
relative to chunk sizes (tighter budgets mean truncation risk is real,
not theoretical), how often the corpus contains adjacent, split passages
for this request type's typical documents, and what's at stake if a
load-bearing clause gets silently dropped — a legal qualifying limit, a
medical contraindication, a safety exclusion, versus a low-stakes FAQ
lookup where a single short, self-contained chunk is the normal case.
High-stakes, budget-constrained request types justify the full Retrieval
Integration Recipe; a single-chunk, low-stakes lookup may reasonably
need only the relevance floor.

**Red flag:** Proposes full boundary-safe fitting and stitching for
every request "to be safe" with no engagement with actual truncation
risk, or the reverse — skips it for a request type where a real,
observed truncation already happened.

**Follow-up:** "Your highest-traffic request type has generous budget
headroom relative to typical chunk sizes. Does it still need the full
recipe?"

**What this proves:** Applies proportionate judgment consistently,
rather than treating this chapter's recipe as free or universally
required — the same discipline every prior chapter's own comparison
table required.

---

### 7. (Architect) Design a lightweight governance process so every RAG pipeline in a production system actually gets integration review, not just a retrieval-quality review.

**Strong answer:** Require a standard artifact per request type that
uses retrieval: the configured relevance floor and the reasoning behind
it, evidence that budget fitting is boundary-safe (a test that verifies
no chunk is ever partially included), a provenance-completeness check
(every surviving chunk carries a source, section, and score), and a
documented behavior for the empty/low-confidence case. Pair it with a
regression suite built from known load-bearing multi-chunk passages
(like CiteLine's own qualifying-clause pair) that must survive
integration intact before a pipeline change ships, and track
truncation-detected and empty-result rates as first-class production
metrics, the same way Chapter 7's own architect answer required tracking
contradiction and escalation rates.

**Red flag:** A process that only tracks retrieval precision/recall,
with no requirement that integration behavior — truncation, stitching,
provenance, empty-result handling — was ever tested directly.

**Follow-up:** "A new document type gets added to the corpus next
quarter, with a different typical passage length. How does your process
catch that the existing relevance floor and budget assumptions might no
longer fit it?"

**What this proves:** Architect-level judgment — treats retrieval
integration as something that needs continuous verification as the
corpus and request types evolve, not a one-time pipeline setting.

---

### 8. (Architect) Leadership says: "our new retriever has a much larger context window and better reranking — do we still need explicit relevance floors, boundary-safe fitting, and stitching?"

**Strong answer:** A better retriever and a larger window change the
calculus but don't eliminate the need. A larger window reduces how often
budget-fit truncation actually triggers, but doesn't eliminate the
question of what happens when a request type's retrieved content still
exceeds it, and better reranking improves which chunks are top-ranked
but says nothing about whether two of them are still mechanically split
fragments of the same underlying passage. This chapter's own hook and
live captures show the risk is not "retrieval is bad," it's that
correctly-produced, correctly-ranked chunks can still combine into a
poorly-formed context block — a claim about a bigger window or a better
reranker needs its own regression evidence against known multi-chunk,
load-bearing passages for the *new* system, not an assumption that a
generically better retriever solves an integration-layer problem it was
never designed to solve.

**Red flag:** Treats retriever/window upgrades as a sufficient
replacement for explicit integration steps, with no engagement with the
specific failure mode (correctly retrieved, incorrectly integrated) this
chapter's own hook and live captures demonstrated.

**Follow-up:** "What's the smallest, cheapest test you'd run against the
new retriever before removing your boundary-safe budget fit for a
high-stakes request type?"

**What this proves:** Can reason about retrieval capability improvements
as a reason to keep testing the integration layer specifically, not a
reason to remove it — the same discipline this chapter's own live
captures demonstrated concretely.

## Strategy Tips

- Ground every answer in CiteLine's actual failure (a correctly ranked,
  correctly scored retriever output, still mishandled between retrieval
  and the model by a boundary-blind cutoff) rather than a generic
  "retrieval quality matters" answer.
- For senior/architect questions, always name the specific integration
  mechanism at risk — relevance floor, boundary-safe fit, provenance,
  stitching, or empty-result handling — rather than treating "better
  retrieval" as a universal fix for problems that happen after
  retrieval.
- If you're new to engineering interviews: reason out loud by naming
  which of this chapter's own failure-prone moments (deciding what's
  relevant enough to keep, cutting safely within budget, or recognizing
  that two chunks are really one passage) a given scenario is testing,
  before proposing a fix.

## A note on this chapter's project

This chapter ships Module 4's single L3 Independent project, drawing on
both Chapter 7's Source Assembly Recipe and this chapter's own Retrieval
Integration Recipe together, closing Module 4 — see
`chapters/chapter-08-retrieval-integration/project/README.md`.
