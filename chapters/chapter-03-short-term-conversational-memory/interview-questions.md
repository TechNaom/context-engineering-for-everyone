# Chapter 3 Interview Questions: Short-Term Conversational Memory

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) What's the difference between an eviction mechanism and a memory policy, in your own words?

**Strong answer:** An eviction mechanism is the code that actually
removes something once a budget is exceeded — a sliding window that
drops the oldest turns is a real, working mechanism. A memory policy is
the set of rules that decides *what* gets removed and *what* survives,
based on more than just recency: a verbatim window for the newest
turns, a running summary for anything older, and explicit pins for
facts that must survive no matter when they occurred. A mechanism with
no policy behind it defaults to the simplest possible rule — keep
whatever's newest — which has no way to know a small early fact might
matter more than a large recent one.

**Red flag:** Treats "we have an eviction mechanism" as equivalent to
"we have a memory policy."

**Follow-up:** "What's the simplest possible memory policy, and when is
it actually sufficient?"

**What this proves:** Understands this chapter's central distinction —
the presence of a working mechanism says nothing about whether it's
governed by a real policy.

---

### 2. (Beginner) Why does a pinned-facts reserve need to be bounded, not unlimited?

**Strong answer:** If a pinned-facts list can grow without limit, it
just recreates the original budget problem under a new name — nothing
is actually prioritized if everything can be pinned. A real pinning
policy has to be selective: it reserves a deliberately small, fixed
slice of the Line 3 budget for facts that are genuinely load-bearing
(safety, eligibility, dosage changes), and anything that doesn't meet
that bar goes through the running summary instead, even if it's
somewhat important.

**Red flag:** Argues that pinning more facts is strictly safer with no
acknowledgment of the tradeoff against verbatim window size.

**Follow-up:** "What would you do if the number of facts that
genuinely deserve pinning started to exceed the reserve you sized for
it?"

**What this proves:** Understands that pinning is a budgeted, bounded
mechanism, not a way to opt out of the budget entirely.

---

### 3. (Intermediate) Walk through why RouteLine's incident happened even though Line 3's budget was correctly derived.

**Strong answer:** The team ran Chapter 2's own recipe correctly and
landed on a real, defensible 8,680-token Line 3 budget for Multi-Leg
Trip Planning. The gap wasn't the budget — it was the eviction
mechanism layered on top of it: a sliding window that keeps only the
most recent whole turns, dropping the oldest first once the total
exceeds budget. That mechanism has no concept of importance, only
recency, so it dropped turn 2's 90-token accessibility disclosure along
with the other early turns, purely because of when it happened, not
because of what it said.

**Red flag:** Blames the incident on "not enough budget," missing that
the budget itself was correct and the failure was one layer up.

**Follow-up:** "If the team had simply doubled the Line 3 budget
instead of building a real policy, would the incident have been
prevented, or just delayed?"

**What this proves:** Understands that a right-sized budget and a
sound eviction policy are two separate, both-necessary things.

---

### 4. (Intermediate) A teammate proposes summarizing every turn immediately, starting from turn 1, so the running summary is "always current." What's the problem?

**Strong answer:** Summarizing continuously from turn 1 wastes compute
and latency compressing turns that are still inside the verbatim window
and haven't aged out yet — there's no reason to compress something the
model is about to read in full anyway. It also risks compressing very
recent, still-nuanced turns too early, losing detail the model may
still need this turn. Compression should trigger once a real threshold
is reached (Step 3 of the recipe), not run continuously regardless of
whether anything has actually aged out of the verbatim window yet.

**Red flag:** Treats "more summarization, more often" as strictly safer
with no cost/latency tradeoff acknowledged.

**Follow-up:** "How would you decide where to set the compression
trigger threshold relative to the hard budget limit?"

**What this proves:** Understands the recipe's ordering isn't
arbitrary — each step has a real reason for firing when it does, not
just early or often.

---

### 5. (Senior) You're reviewing a new request type's short-term memory policy before it ships. What do you check beyond "does it fit inside the budget"?

**Strong answer:** Fitting the budget is necessary but not sufficient.
Check that the pin list was derived from real criteria (safety,
eligibility, dosage/deadline changes) rather than a convenience list
that happens to be short enough; check that the verbatim window size
was chosen deliberately, not defaulted to whatever's left over after
everything else; and validate the full package — pins plus summary
plus verbatim window — against the longest realistic conversation this
request type actually produces, not a typical-length demo
conversation. A policy that only survives an average-length
conversation hasn't actually been validated.

**Red flag:** Signs off purely because the arithmetic in the self-check
passes, with no scrutiny of how the pin criteria were derived.

**Follow-up:** "The team tells you they tested against 'a few
representative conversations.' What's your follow-up question?"

**What this proves:** Understands that a passing structural check is a
floor, matching the same discipline Chapter 2 established for
allocation, now applied to the policy layer above it.

---

### 6. (Senior) How do you decide whether a given request type needs the full hybrid policy (pins + summary + verbatim window) versus no policy at all?

**Strong answer:** Look at whether the request type's realistic
conversations can actually exceed Line 3's allocated budget, and
whether any single early fact in those conversations could plausibly
still matter later. A short, bounded request type (Chapter 2's
short-lookup archetype) or a session that's intentionally stateless
genuinely needs no policy — building one anyway is wasted complexity.
A long-running, recurring, or safety-relevant request type needs the
full hybrid policy, because both conditions (conversations that exceed
budget, and early facts that stay load-bearing) are realistically true
for it.

**Red flag:** Proposes building the hybrid policy for every request
type "to be safe," without engaging with the actual cost of unnecessary
complexity.

**Follow-up:** "What's the cheapest way to check whether a request
type's realistic conversations actually approach the budget, before
committing to build the full policy?"

**What this proves:** Can apply proportionate judgment rather than
reaching for the heaviest tool by default.

---

### 7. (Architect) Design a lightweight governance process so every long-running request type gets a real short-term memory policy, not just a correctly sized budget.

**Strong answer:** Require a short, standard artifact per request type
before launch, alongside Chapter 2's own allocation artifact: the
chosen verbatim window size and its justification, the compression
trigger threshold, the pin criteria used (not just the resulting list),
and evidence of worst-case validation against the longest realistic
conversation this request type produces. Pair it with an automated
check that flags any request type whose Line 3 budget was allocated
(exists in the Chapter 2-style artifact) but has no corresponding
memory-policy artifact on file — since that gap, a real budget with no
real policy, is exactly the state RouteLine shipped in. Make the
artifact proportionate: request types below a realistic conversation-
length threshold can explicitly declare "no policy needed" rather than
being forced through the full process.

**Red flag:** Proposes a process that only checks the budget artifact
exists, without a parallel check for the policy artifact.

**Follow-up:** "How would you catch a request type that had a policy
artifact on file, but whose pin criteria had quietly drifted out of
date as the request type's real content evolved?"

**What this proves:** Architect-level judgment — connects governance
for allocation (Chapter 2) and governance for the policy that operates
inside it (this chapter) as two halves of one real discipline, not
independent checklists.

---

### 8. (Architect) Leadership says: "we already have Chapter 2's budget allocation policy — isn't a short-term memory policy just the same discipline applied continuously?" How do you explain what's actually different?

**Strong answer:** Allocation (Chapter 2) answers a one-time question
per request type: given a hard window limit, how many tokens does each
ledger line get. A short-term memory policy (this chapter) answers a
different, ongoing question that only exists *because* Line 3 has a
real, finite allocation: once a real conversation's raw content
actually reaches that allocation, which specific turns and facts get
to keep occupying it. Allocation produces a number; a memory policy
produces a set of rules for what happens to real content once that
number is reached, live, for every long conversation this request type
ever runs. Without allocation, there is no fixed budget to design a
policy against; without a policy, a correct allocation collapses to
"keep whatever's newest" the moment a conversation actually gets long
— exactly what RouteLine's incident showed.

**Red flag:** Claims the two disciplines are interchangeable, or can't
name the concrete artifact allocation produces that a memory policy
depends on (the fixed Line 3 number itself).

**Follow-up:** "If your org could only fund building one of the two
disciplines fully this quarter, which would you prioritize, and for
which kinds of request types would that choice matter most?"

**What this proves:** Can articulate the precise relationship between
Chapters 2 and 3 to a non-specialist audience without collapsing them
into the same thing.

## Strategy Tips

- Ground every answer in RouteLine's actual mechanism (a correctly
  sized budget, a working but policy-free eviction mechanism) rather
  than a generic "always have a memory policy" answer.
- For senior/architect questions, always name a concrete artifact or
  check, not just a principle.
- If you're new to engineering interviews: reason out loud by naming
  which of the three concerns (recency, aged-out content, load-bearing
  facts) a given piece of conversation history falls into before
  proposing what happens to it — that's exactly the order this
  chapter's recipe uses.
