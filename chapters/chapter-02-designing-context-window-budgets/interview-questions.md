# Chapter 2 Interview Questions: Designing Context Window Budgets

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) What's the difference between diagnosing a context-budget problem and allocating a context budget, in your own words?

**Strong answer:** Diagnosis looks at a system that's already running
and asks which of the five ledger lines is responsible for an observed
failure — it happens after the fact, usually after something has
already gone wrong. Allocation happens before a single request is
sent: given a request type and a model's hard context-window limit,
decide on purpose how many tokens each of the five lines gets, so
there's a real budget to diagnose against later if something does go
wrong.

**Red flag:** Treats the two as interchangeable, or can't explain why a
team would need both.

**Follow-up:** "Which one does a team need first, on a brand-new
feature that hasn't shipped yet?"

**What this proves:** Understands this chapter's actual relationship to
Chapter 1 — a lens applied earlier in the lifecycle, not a repeat of
the same skill.

---

### 2. (Beginner) Why does this chapter's recipe reserve Working Space (Line 5) before doing anything else with the budget?

**Strong answer:** Every token the model generates in its response also
counts against the same fixed context window the input competes for —
it isn't a separate, free allowance. Reserving Line 5 first means every
later number (System Instructions, then the split across Grounding
Context, Conversation History, and Recalled Long-Term Memory) is
computed against the *real* remaining budget, not an optimistic number
that ignores the cost of the model's own output.

**Red flag:** Treats Working Space as an afterthought, or assumes
"budget" only concerns input content.

**Follow-up:** "What actually happens if a team forgets to reserve
output space and a long response is generated near the window's limit?"

**What this proves:** Understands that a context window is a shared
resource between input and output, not two separate pools.

---

### 3. (Intermediate) Walk through why TriageLine's Chronic Care Check-In incident happened even though the team had already done real context-budget work.

**Strong answer:** The team correctly derived a budget for New Symptom
Triage — real reserved output, real system-instructions line, real
profile-driven split. The gap was treating that derived budget as a
property of the whole system rather than a property of the specific
request type it was derived for. Chronic Care Check-In had a
fundamentally different content shape (longer conversations, a fuller
medication and lab record), but reused Triage's percentages unchanged,
which under-provisioned Recalled Long-Term Memory and forced an
emergency truncation with no real policy behind which content got cut.

**Red flag:** Blames the incident on "not having a budget," missing
that a budget existed and was simply misapplied.

**Follow-up:** "What would you check before reusing one request type's
budget for another, even on the identical model and window?"

**What this proves:** Understands allocation as a per-request-type
artifact, the chapter's central distinction.

---

### 4. (Intermediate) A teammate proposes splitting a request type's remaining budget evenly across Grounding Context, Conversation History, and Recalled Long-Term Memory — one-third each, every time, to keep things simple. What's the problem?

**Strong answer:** An even split ignores the fact that different
request types have genuinely different content shapes. A short,
single-turn lookup barely needs conversation history but leans heavily
on grounding; a long-document review is dominated by one grounding
source and barely touches history or memory. Splitting evenly wastes
budget on lines a request type doesn't need while starving the line
that actually matters most for that request type — a subtler version of
exactly the mismatch that broke Chronic Care Check-In.

**Red flag:** Defends an even split as "fair" without engaging with
actual content-shape differences between request types.

**Follow-up:** "Name one request-type archetype where an even split
would be badly wrong, and explain why."

**What this proves:** Understands that a real allocation has to be
derived from a request type's actual profile, not a default rule of
thumb applied everywhere.

---

### 5. (Senior) You're asked to sign off on a new request type's budget allocation before it ships. What do you actually check, beyond "does the math add up"?

**Strong answer:** The arithmetic passing is necessary but not
sufficient. Check that the profile percentages are actually derived
from this request type's real content shape, not copied from a
convenient existing request type; check that Working Space was
reserved based on this request type's real expected response length,
not a generic default; and — most importantly — validate the
allocation against the worst realistic case in real data (the longest
conversations, the fullest memory records), not the median case a demo
happens to use. A budget that only survives the typical case is not
validated, it's untested.

**Red flag:** Signs off purely on the numbers summing correctly, with
no mention of profile derivation or worst-case validation.

**Follow-up:** "The team tells you they tested against 'a few
representative conversations.' What's your follow-up question?"

**What this proves:** Understands that a passing self-check on
arithmetic is a floor, not a substitute for real validation discipline.

---

### 6. (Senior) A product team wants to add a fifth request type to an assistant that already has four budgeted request types on the same model. How do you decide whether the new request type needs its own allocation or can reuse an existing one?

**Strong answer:** Compare the new request type's actual content shape
— expected conversation length, grounding volume, and recalled-memory
volume — against each existing request type's profile, not just
against which one "feels similar." If an existing request type's
profile and Line 1/Line 5 costs are a genuine match (not just the same
model and window), reuse is defensible; if any dimension differs
meaningfully, a full re-derivation is required, because a matching
window size says nothing about whether the underlying content shape
matches — the same trap that broke Chronic Care Check-In even though it
shared TriageLine's exact window.

**Red flag:** Treats "same model, same window" as sufficient grounds
for reuse.

**Follow-up:** "What's the cheapest way to check whether two request
types actually share a content shape, before doing a full re-derivation?"

**What this proves:** Can generalize the chapter's central lesson to a
new, unscripted scenario rather than reciting the hook's specific facts.

---

### 7. (Architect) Design a lightweight governance process so every new request type on a shared, multi-request-type assistant gets a real budget allocation before it ships, without slowing every team down to a crawl.

**Strong answer:** Require a short, standard artifact per request type
before launch: the hard window limit and model used, the reserved
Working Space and System Instructions costs, the chosen profile
percentages with a one-paragraph justification tied to real content
data (not a copied default), and evidence of worst-case validation
(the specific longest-conversation and fullest-memory-record test
cases used). Make the artifact small enough to write in minutes for a
simple request type, but require an actual re-derivation — not a
checkbox — whenever a new request type's content shape genuinely
differs from an existing one on the same assistant. Pair it with an
automated check that flags when two request types share an identical
numeric allocation despite differing profiles, since that pattern is
exactly the silent-reuse failure this chapter's hook shows.

**Red flag:** Proposes a heavyweight review board with no concrete
artifact, or a process so light it wouldn't have caught Chronic Care
Check-In's actual mistake.

**Follow-up:** "How would this process differ for a request type
that's a minor variant of an existing one versus a genuinely new
shape?"

**What this proves:** Architect-level judgment — turns a per-request-
type discipline into a proportionate, enforceable organizational
process.

---

### 8. (Architect) A leadership team asks: "we already have a documented context-budget policy from Chapter 1's diagnostic work — isn't allocation the same skill applied earlier?" How do you explain what's actually different?

**Strong answer:** A diagnostic policy (Chapter 1's subject) is built to
recognize failure patterns after they occur — it's reactive by design,
even when it's well documented. Allocation (this chapter's subject) is
a design discipline applied per request type, before any request ships,
producing a concrete artifact (a real token split across five lines,
validated against a worst case) that a later diagnosis can actually be
checked against. Without allocation, diagnosis has nothing to compare
a failing system to except "it feels wrong" — with a real allocation on
record, a diagnosis can say precisely which line's real numbers were
violated, and by how much. The two are complementary halves of the same
discipline, not the same skill run at different times: one produces the
budget, the other checks reality against it.

**Red flag:** Claims the two skills are interchangeable, or can't
explain what artifact allocation produces that diagnosis depends on.

**Follow-up:** "If your org could only build one of the two disciplines
this quarter, which would you pick first, and why?"

**What this proves:** Can articulate the precise relationship between
Chapters 1 and 2 to a non-specialist audience without collapsing them
into the same thing.

## Strategy Tips

- Ground every answer in the TriageLine incident's actual mechanism
  (a budget correctly derived for one request type, silently reused for
  a differently shaped one) rather than a generic "always have a
  budget" answer.
- For senior/architect questions, always name a concrete artifact or
  check, not just a principle — interviewers probe for what you'd
  actually build or require.
- If you're new to engineering interviews: it's fine to reason out loud
  by naming the request type's real content shape first ("how long do
  these conversations actually run, how much grounding does this pull,
  how much memory does it need recalled") before touching a single
  percentage — that's exactly the order this chapter's recipe uses.
