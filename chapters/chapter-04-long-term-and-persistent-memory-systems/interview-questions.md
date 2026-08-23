# Chapter 4 Interview Questions: Long-Term and Persistent Memory Systems

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) Why did HearthLine lose the fall-risk fact even though its short-term memory policy was built correctly?

**Strong answer:** Chapter 3's short-term memory policy is scoped to a
single session on purpose — it protects a pinned fact for the life of
one conversation, then correctly clears Line 3 when that session ends.
HearthLine had no persistent store at all, so nothing wrote the
fall-risk disclosure anywhere before Line 3 was cleared. The short-term
policy did exactly what it was designed to do, twice; the gap is a
separate layer nobody built — a decision about what should survive a
session boundary in the first place.

**Red flag:** Blames the short-term memory policy itself, or claims a
bigger Line 3 budget would have prevented this.

**Follow-up:** "If HearthLine's team had simply never cleared Line 3 at
session end, would that have fixed the problem?"

**What this proves:** Understands the precise boundary between Chapter
3's subject and this chapter's — a correct short-term policy is not a
substitute for a long-term one.

---

### 2. (Beginner) What's the difference between "recent" and "still true," and why does long-term memory care about the second one specifically?

**Strong answer:** Short-term memory (Chapter 3) only ever needed to
ask whether a fact was recent enough to still be in the verbatim
window or worth pinning — within one conversation, most facts don't
actually change out from under you. Long-term memory spans real time —
weeks, months — during which a stored fact can become false: a
medication dosage changes, an insurance tier changes, an address
changes. A long-term memory policy has to actively track whether a
stored fact is still true (via status: active, superseded, expired),
not just assume anything written down stays valid forever.

**Red flag:** Treats "old" and "stale" as the same concept, or can't
name a concrete example of a fact that goes stale without becoming
"old" in a recency sense.

**Follow-up:** "How would your system find out that a previously
stored fact has become false, if the user doesn't explicitly say so?"

**What this proves:** Understands this chapter's central new idea —
staleness is a truth question, not a recency question.

---

### 3. (Intermediate) A teammate proposes: "let's just write every fact ever disclosed to the persistent store, so we never miss anything." What's wrong with that?

**Strong answer:** An unbounded write policy is the naive append-only
log this chapter explicitly rejects. It fails two ways: first, it
eventually exceeds Line 4's retrieval budget as the relationship grows,
forcing either an overflow or a recency-based truncation that has the
same blind spot as Chapter 3's naive FIFO. Second, and more
specifically to long-term memory, it retrieves superseded and outdated
facts alongside their replacements with nothing to resolve the
contradiction — writing everything doesn't just cost more tokens, it
actively produces wrong answers when old and new facts disagree.

**Red flag:** Argues that writing more is strictly safer, with no
engagement with the staleness/contradiction problem specifically.

**Follow-up:** "Your store now has an old address and a new address for
the same client, both 'written.' Walk me through what your retrieval
policy needs to do."

**What this proves:** Can name the two distinct failure modes of
unbounded writing (budget growth, staleness contradiction), not just
one.

---

### 4. (Intermediate) How is this chapter's subject different from what `rag-for-everyone` teaches, given both involve "storing something and retrieving it later"?

**Strong answer:** `rag-for-everyone` owns retrieval architecture —
how candidate documents get ranked, embedded, and searched. This
chapter assumes that architecture already exists by whatever means and
owns two different decisions: what a context-engineering system writes
to persistent storage in the first place (the write criteria), and
what real policy decides which of it gets pulled back into Line 4 for
a specific turn (the retrieval scope and staleness rule). A system
could have an excellent retriever and still fail this chapter's own
subject, if nothing worth retrieving was ever written, or if what's
retrievable includes contradictory, stale facts the retriever has no
way to know are outdated.

**Red flag:** Conflates the two courses, or can't name a concrete
failure mode a great retriever wouldn't fix.

**Follow-up:** "If your retriever's precision and recall metrics both
look great, what could still be wrong with your long-term memory
system?"

**What this proves:** Can hold the boundary between adjacent courses
the way this chapter's own lesson states it explicitly, not just
gesture at "they're different."

---

### 5. (Senior) You're reviewing a new request type's long-term memory design before it ships. What do you check beyond "does retrieval fit inside the budget"?

**Strong answer:** Fitting the budget is necessary but not sufficient.
Check that the write criteria are a real, bounded set of categories
tied to what could plausibly matter in a future session — not a
convenience list. Check that every write produces a structured record
with a status field, not a raw transcript append. Check that the
retrieval policy is genuinely scoped (by subject and relevant category)
rather than "everything for this user." And specifically check the
staleness mechanism: what actually happens when a new fact contradicts
an old one, and confirm the old record becomes unretrievable, not just
lower-priority.

**Red flag:** Signs off purely because the token arithmetic passes,
with no scrutiny of the staleness mechanism.

**Follow-up:** "Show me the exact code path that marks an old record
superseded when a new one arrives. What happens if that path is
skipped?"

**What this proves:** Understands that budget-fit is a floor, and that
staleness handling is the one piece of this chapter's recipe with no
Chapter 3 analog, worth extra scrutiny.

---

### 6. (Senior) How do you decide whether a given request type needs the full curated long-term memory approach versus none at all?

**Strong answer:** Look at whether the request type involves a real
recurring relationship — the same user, resident, case, or client
across multiple sessions separated by real time — and whether a fact
disclosed in one session could plausibly still matter, or plausibly
change, in a later one. A genuinely one-off interaction needs no
persistent memory at all; building one anyway is wasted complexity and
an unnecessary staleness-management burden. A real recurring
relationship where facts can go stale needs the full curated approach,
because both conditions this chapter cares about (cross-session
relevance, and the possibility of contradiction over time) are
realistically true for it.

**Red flag:** Proposes building persistent memory for every request
type "to be safe" without engaging with the cost of staleness upkeep.

**Follow-up:** "What's the cheapest way to check whether a request
type's relationships are actually long enough and change enough to
justify this?"

**What this proves:** Applies proportionate judgment, matching the same
discipline Chapter 3 required for its own hybrid-vs-nothing decision,
now one layer up.

---

### 7. (Architect) Design a lightweight governance process so every long-running request type gets a real long-term memory policy, not just a correctly allocated Line 4 budget.

**Strong answer:** Require a standard artifact per request type,
alongside Chapter 2's allocation artifact and Chapter 3's short-term
policy artifact: the write criteria (the bounded category list and its
justification), the storage record schema, the retrieval scope logic,
and evidence that a staleness mechanism exists and was tested against
a scenario with at least one superseded fact. Pair it with an automated
check that flags any request type with a Line 4 allocation on file but
no corresponding long-term policy artifact — exactly the gap
HearthLine shipped with. Require the worst-case validation (Step 6) to
include at least one scenario where a stored fact was updated, not just
scenarios where facts only accumulate.

**Red flag:** A process that only checks the budget artifact exists,
with no check for staleness-scenario test coverage specifically.

**Follow-up:** "How would you catch a request type whose staleness
mechanism existed on paper but had quietly stopped firing in
production?"

**What this proves:** Architect-level judgment — connects governance
across all three memory-related artifacts (allocation, short-term,
long-term) as layers of one discipline, and specifically protects
against staleness handling silently rotting, which is easy to miss
because nothing crashes when it fails.

---

### 8. (Architect) Leadership says: "we already solved memory in Chapter 3 — isn't long-term memory just short-term memory with a bigger, cross-session budget?" How do you explain what's actually different?

**Strong answer:** Chapter 3's short-term memory answers a question
scoped to one conversation: given a fixed Line 3 budget, which turns
and pinned facts survive as that one conversation grows. It has no
concept of a fact becoming false — only of a fact becoming old within a
bounded window. Long-term memory answers a structurally different
question: given a relationship that spans real time and multiple
separate sessions, what's worth persisting at all, and does what's
persisted still describe reality by the time it's retrieved. A bigger
budget doesn't solve staleness — you can have unlimited Line 4 tokens
and still retrieve a contradictory, outdated fact if nothing tracks
whether a record is still active. The two systems solve genuinely
different problems that happen to share a superficial shape (both keep
some facts and drop others).

**Red flag:** Claims the two are the same discipline at different
scales, or can't name staleness as the concrete capability short-term
memory never needed.

**Follow-up:** "If your org could only build one of the two fully this
quarter, which request types would suffer most from having only the
other one?"

**What this proves:** Can articulate the precise, non-superficial
difference between Chapters 3 and 4 to a non-specialist audience.

## Strategy Tips

- Ground every answer in HearthLine's actual failure (correct
  short-term policy, zero persistent memory, a fact lost at a session
  boundary) rather than a generic "always persist important facts"
  answer.
- For senior/architect questions, always name the staleness mechanism
  specifically — it's the one piece of this chapter's recipe with no
  direct Chapter 3 analog, and interviewers will notice if you skip it.
- If you're new to engineering interviews: reason out loud by naming
  which of this chapter's three concerns (write-worthiness, retrieval
  scope, staleness) a given fact falls into before proposing what
  happens to it — the same ordering the recipe itself uses.
