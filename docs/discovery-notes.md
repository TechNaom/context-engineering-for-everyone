# Discovery Notes — Context Engineering for Everyone

LAST_REVIEWED: 2026-08-22
Status: Discovery complete for this session. This document is a
documented, reasoned decision, not a confirmed-by-human one — flag any
disagreement and redirect before Chapters 2-13 are built.

## 1. Course vision — what "Context Engineering" means here, and why it's
   a distinct discipline from every existing TechNaom course

The TechNaom ecosystem already has three courses that sit close to this
one's subject matter: `rag-for-everyone` (retrieval architecture),
`mcp-for-everyone` (tool/resource protocol), and `ai-engineering-for-everyone`
(production engineering discipline, including Chapter 3's "prompt as a
versioned software artifact"). If "Context Engineering for Everyone"
just re-taught chunking-and-embeddings, tool-protocol negotiation, or
prompt versioning under a new name, it would be redundant scaffolding,
not a new course. The discovery task here is to find the real,
non-overlapping territory — and to verify it directly against each
neighbor's actual content, not just assume a plausible-sounding
positioning paragraph holds.

**What this course actually owns:** the engineering discipline of
deciding what goes *into* the model's context window at inference time,
and how that content is organized once it's there. Concretely:

- **Context window budget management** — a context window is a fixed,
  finite resource. Every token spent on system instructions, history,
  retrieved documents, or tool output is a token not available for
  something else, and (per Chapter 1's own core mental model) usually a
  token that costs real money and adds real latency too. Deciding what
  earns a place in that budget under a hard limit — and what gets
  dropped, compressed, or deferred — is an engineering decision this
  course teaches as a repeatable method, not a vibe.
- **Memory systems** — what a system remembers within one conversation
  (short-term) versus across sessions (long-term/persistent), how that
  memory is stored, and — the actual context engineering question — what
  gets *retrieved back into context* for a given turn versus what stays
  discarded or dormant.
- **Context curation and compression** — summarizing, truncating, or
  re-ranking prior turns and retrieved material intelligently instead of
  blindly appending everything, and understanding "lost in the middle"
  degradation (documented directly by Liu et al.'s "Lost in the Middle"
  research, verified live this session — see Chapter 1's Sources) as a
  real, measurable failure mode that context *position*, not just
  context *content*, causes.
- **Multi-source context assembly** — combining retrieved documents,
  tool outputs, conversation history, and system instructions into one
  coherent context window without the pieces contradicting, crowding
  out, or silently overriding each other.
- **Context engineering for multi-agent and multi-step systems** — what
  context a given step, tool call, or sub-agent actually needs, versus
  inheriting the entire accumulated context indiscriminately, and how
  isolating context between steps is a deliberate design choice, not an
  oversight.
- **Context evaluation** — is the assembled context actually complete,
  relevant, and well-ordered, checked before it ever reaches the model,
  not inferred after the fact from a bad final answer.

### 1.1 Checked directly against `rag-for-everyone`

`rag-for-everyone` owns retrieval-augmented generation as an
*architecture pattern*: chunking strategy, embedding models, vector
store selection and indexing, retrieval quality (recall/precision,
re-ranking), and — per `ai-engineering-for-everyone`'s own cross-course
notes — some context-injection/prompt-injection-safety material
specific to RAG pipelines. RAG's job, in this ecosystem's own division
of labor, is to *produce candidate context* — a ranked list of chunks a
retriever believes are relevant to a query. What RAG's curriculum does
not own, by its own scope: what happens to those candidate chunks once
they're headed for the context window — how many of them actually fit
the request's token budget, in what order they should appear (RAG's own
similarity ranking is not automatically the right *context position*
ranking, per the lost-in-the-middle finding above), how they get
combined with unrelated context sources (conversation history, tool
output, system instructions) that RAG's own pipeline has no visibility
into, and whether the *assembled* context — not just the *retrieved*
set — is actually good. This course's Chapter 8 ("Retrieval
Integration: From Ranked Results to Context") is explicit about this
handoff: it starts from a RAG pipeline's ranked output as a given input
and teaches what happens next, deliberately not re-teaching chunking,
embeddings, or retrieval quality — those remain `rag-for-everyone`'s
material, cross-linked, not duplicated.

### 1.2 Checked directly against `mcp-for-everyone`

`mcp-for-everyone` owns the Model Context Protocol specifically: how an
MCP client and server negotiate tools, resources, and prompts, the
protocol-level message shapes, and (per its Module 5) permission
scoping and sandboxing for tool-calling. Its subject is the *protocol
mechanics of the negotiation* — what messages are exchanged, how a
server advertises capabilities, how a client discovers and invokes
them. What it does not own: once a tool result comes back — regardless
of whether it arrived over MCP, a plain function call, or any other
integration mechanism — what actually gets included in the model's next
context window, how much of a large tool result gets kept versus
summarized, and how that tool output is weighed against everything else
competing for the same token budget. This course's Chapter 9 ("Context
Engineering for Tool Use") is deliberately protocol-agnostic: it
assumes a tool call already happened (by whatever protocol) and teaches
the budget/curation decision about its result, explicitly deferring
protocol-level negotiation mechanics to `mcp-for-everyone`.

### 1.3 Checked directly against `ai-engineering-for-everyone`, especially
   its Chapter 3

This is the closest, highest-risk overlap, and the one this session
verified most carefully — `ai-engineering-for-everyone/chapters/
chapter-03-prompt-engineering-as-software/lesson.html` was read in full
this session before writing this section. Chapter 3 teaches: treating a
prompt as a **versioned software artifact** (a new, named, diffable
revision for every change, not a live string mutated in place),
**structured composition** of a prompt template out of named, separately
owned pieces (a base template, category blocks, a disclaimer block,
composed via XML-tag structure), **separating prompt content from
application code** (so a wording change doesn't require a code deploy),
a **human-scale before/after check** run by one engineer before a
change ships (explicitly distinguished, in that chapter's own text,
from `ai-engineering-for-everyone` Module 3's automated evaluation
harness), **diff review** for prompt changes with a weakened-guardrail
checklist, and a six-step **change-management workflow**. Its own
"Builder Thought Process" section states directly what it is *not*:
"Chapter 4 goes deep on the shape of a model's output... That contract
lives inside the same versioned, composed prompt artifact this chapter
just built" — i.e., Chapter 3's scope is the *template itself* as a
managed software artifact, its version history, its authorship, and its
release process.

None of that is this course's subject, and this course assumes it as a
given, not a gap to fill. Concretely: `ai-engineering-for-everyone`
Chapter 3's own composed template (`BASE_TEMPLATE` with
`{tone_instruction}`, `{category_block}`, `{disclaimer_block}`,
`{ticket_text}` placeholders) is a *static, versioned artifact checked
into source control* — the same template object serves every request
until a human deliberately ships a new version. This course's subject
starts exactly where that stops: `{ticket_text}` in that example is
literally this course's territory — the dynamic, per-request content
that fills a template slot, decided fresh (or freshly retrieved,
freshly compressed, freshly assembled from multiple sources) on every
single inference call, not versioned by a human and reviewed in a pull
request. A context engineering failure — a token budget blown by
unbounded history, a critical fact buried in the middle of a long
context and silently ignored, a tool result crowding out an earlier
instruction — can happen on the *exact same, unchanged, already-
reviewed prompt template* from one request to the next, purely because
the *content* poured into it that request was engineered (or wasn't).
This course explicitly assumes the prompt template itself is already
managed per Chapter 3's discipline, and does not re-teach prompt
versioning, template composition-as-a-static-artifact, diff review, or
release workflow for the template — those remain
`ai-engineering-for-everyone` Chapter 3's material, cross-linked in
Chapter 1's positioning section, not duplicated.

**Positioning statement:** *Context Engineering for Everyone* teaches
the discipline of engineering what actually goes into a model's context
window at inference time, as a system: budget management under a token
limit, memory (short-term and long-term, what's retrieved back into
context and what isn't), compression and curation (summarizing/
truncating/ordering intelligently, avoiding lost-in-the-middle
degradation), multi-source assembly (retrieved documents, tool output,
conversation history, and system instructions combined into one
coherent window), context engineering for agentic/multi-step systems
(what each step or sub-agent actually needs versus inheriting
everything), and context evaluation (is the assembled context actually
good). It is explicitly **not** retrieval architecture (`rag-for-everyone`'s
subject — RAG produces candidate context; this course decides what
makes it into the window and how it's organized once there), **not**
protocol-level tool integration (`mcp-for-everyone`'s subject), and
**not** the prompt template as a versioned software artifact
(`ai-engineering-for-everyone` Chapter 3's subject — this course assumes
the template is already managed and focuses on the dynamic, per-request
content that fills it).

## 2. Personas

- **`ai-engineering-for-everyone` graduate hitting a context wall** —
  already treats prompts as versioned software (Chapter 3) and has
  shipped a production LLM feature, but the feature degrades as
  conversation history or retrieved context grows, and nothing in that
  course's curriculum diagnoses *why*, because that's this course's
  subject, not that one's.
- **RAG engineer whose retrieval metrics look fine but answers still
  degrade** — has built a working retrieval pipeline (`rag-for-everyone`
  level), recall and precision look reasonable, but the final answer is
  still wrong or ignores retrieved facts — the actual problem is in
  *context assembly*, not retrieval quality, and this persona has no
  existing course teaching them to look there.
- **Agent/multi-step system builder debugging "it forgot" or "it got
  confused"** — has built a multi-step or multi-agent pipeline (using
  `mcp-for-everyone`-style tool integration or a custom orchestration
  layer) and is hitting failures that look like model quality issues but
  are actually context-budget or context-isolation issues — a step
  inherited irrelevant history, or a sub-agent never received a fact it
  needed.
- **Backend engineer building a long-running assistant/chat product** —
  comfortable with software engineering discipline, now needs to design
  memory (what persists across sessions) and a context-assembly pipeline
  for a product where conversations run long and users expect the system
  to "remember," without an unbounded, ever-growing prompt.

## 3. Prerequisites

- `python-for-everyone` level Python (or equivalent) — every hands-on
  chapter uses Python.
- `ai-engineering-for-everyone` (soft prerequisite, strongly
  recommended) — this course assumes the prompt template itself is
  already a managed artifact per that course's Chapter 3, and does not
  re-teach prompt versioning, template composition, or the LLM
  engineering stack's other five layers (evaluation, cost/latency,
  reliability, deployment, observability) from zero. Learners without
  that background can still follow this course, but will see references
  to that vocabulary treated as already understood.
- Helpful, not required: exposure to `rag-for-everyone` (this course's
  Chapter 8 assumes a ranked retrieval result as a given input rather
  than building a retriever from scratch) and `mcp-for-everyone` (this
  course's Chapter 9 assumes a tool call already happened by some
  protocol, without re-teaching that protocol).

## 4. Learning outcomes

By the end, a learner can:

1. Explain the context budget mental model (every token in the window
   competes for a limited, costed budget) and use it to diagnose why a
   real system's context window is misallocated.
2. Design a token budget across system instructions, conversation
   history, retrieved context, and tool output for a given request type
   and hard context-window limit.
3. Design short-term conversational memory that stays within budget
   under a long-running conversation without silently truncating
   load-bearing content.
4. Design a long-term/persistent memory system: what gets stored, what
   gets retrieved back into context for a given turn, and what stays
   dormant.
5. Compress and curate context (summarization, truncation, re-ranking)
   without losing information the model actually needs, and explain and
   defend against lost-in-the-middle degradation through context
   ordering.
6. Assemble context from multiple sources (retrieved documents, tool
   output, conversation history, system instructions) into one coherent
   window without the sources contradicting or crowding out each other.
7. Engineer context for tool-calling and multi-agent/multi-step systems:
   deciding what a given step or sub-agent needs in its own context,
   including deliberate context isolation between steps.
8. Evaluate assembled context quality (completeness, relevance,
   ordering) before it reaches the model, and design and defend a
   complete context engineering system end to end (the capstone).

## 5. Course size

13 chapters — the ecosystem's established sizing for a focused,
emerging-topic course (matching `mcp-for-everyone`,
`ai-coding-agents-for-everyone`, `ai-security-for-everyone`, and
`ai-engineering-for-everyone`). This course's scope, per the overlap
check above, is real and non-duplicative; 13 is a deliberate consistency
choice with the rest of the ecosystem, not padding and not a squeeze.

## 6. Modules and chapters (see CURRICULUM_MAP.md for full detail)

1. **Module 1 — The Context Budget Mental Model** (Ch. 1-2): the core
   mental model (every token competes for a limited, costed budget), and
   the practical skill of allocating that budget across sources.
2. **Module 2 — Memory Systems** (Ch. 3-4): short-term conversational
   memory within a bounded window; long-term/persistent memory and what
   gets retrieved back into context.
3. **Module 3 — Context Compression and Curation** (Ch. 5-6):
   summarization/truncation without losing load-bearing content;
   lost-in-the-middle and context ordering.
4. **Module 4 — Multi-Source Context Assembly** (Ch. 7-8): combining
   multiple context sources into one coherent window; the specific
   retrieval-to-context handoff with RAG.
5. **Module 5 — Context Engineering for Agentic Systems** (Ch. 9-11):
   context for tool use; context for multi-agent/multi-step systems;
   deliberate context isolation and scoping.
6. **Module 6 — Evaluation and Capstone** (Ch. 12-13): evaluating
   assembled context quality; the capstone, designing a complete context
   engineering system.

Chapter 1 ("The Context Budget") is the strong, standalone reference
chapter — it sets the course's unifying mental model (a context budget:
every token in the window costs something and competes for a limited
budget, so context engineering is fundamentally the discipline of
deciding what earns a place in that budget and what doesn't), the same
role Chapter 1 plays in every sibling course (the six-layer stack in
`ai-engineering-for-everyone`, an equivalent unifying frame in each
other course).

## 7. Capstone

Chapter 13 requires the learner to take a realistic, given system (a
long-running assistant or multi-step/agentic pipeline with a real,
finite context window limit, real growth in conversation history, real
retrieved and tool-sourced content competing for space) and produce a
complete context engineering design: a token budget allocation across
all real context sources, a memory design (what's short-term, what's
persistent, what's retrieved back in and when), a compression/curation
plan defending against lost-in-the-middle, a multi-source assembly plan
resolving any source conflicts, a context-isolation plan for any
multi-step/multi-agent portion of the system, and an evaluation plan for
the assembled context's quality. This matches
`ai-engineering-for-everyone`'s L4 capstone rigor (business/system brief
only, no planted single right answer, trade-offs documented and
defended) applied to context engineering's own synthesis rather than
production engineering's.

## 8. Differentiators

- **Owns the dynamic content, not the static template**: the one
  sentence that most precisely separates this course from
  `ai-engineering-for-everyone` Chapter 3 — that chapter versions the
  template; this course engineers what fills it, fresh, every request.
- **Treats the context window as a finite, costed resource from Chapter
  1 onward**: not "more context is better," but "every token here is a
  token not available for something else" — the budget framing this
  course's core mental model is built around.
- **Position, not just presence**: this course teaches that *where*
  something sits in the context window changes whether the model
  actually uses it (lost-in-the-middle), a finding no sibling course
  teaches as a first-class subject.
- **Multi-source assembly as its own discipline**: no existing course
  teaches how to combine retrieved documents, tool output, conversation
  history, and system instructions into one non-contradictory context —
  each sibling course only produces one of those sources.
- **Agentic context, not agent architecture**: teaches what context a
  step or sub-agent needs (and should be denied), a genuinely different
  question from `ai-coding-agents-for-everyone`'s or
  `mcp-for-everyone`'s agent-loop/protocol depth.

## 9. Cross-course links

- **Builds on**: `python-for-everyone` (baseline Python).
- **Builds on, assumes, and does not re-teach**: `ai-engineering-for-everyone`
  (the LLM engineering stack generally, and Chapter 3's "prompt as
  versioned software artifact" specifically — this course assumes the
  template is already managed and focuses on the dynamic content that
  fills it).
- **Builds on but does not duplicate**: `rag-for-everyone` (retrieval
  architecture — this course's Chapter 8 starts from a ranked retrieval
  result as a given input and teaches what happens next, not how to
  build the retriever), `mcp-for-everyone` (tool/resource protocol
  negotiation — this course's Chapter 9 assumes a tool call already
  happened by some protocol and teaches the context decision about its
  result, not the protocol itself), `ai-coding-agents-for-everyone` (one
  application category's agent-loop depth — this course's Module 5
  teaches the context decision inside any multi-step/agentic system,
  architecture-agnostic).
- **Feeds forward** (per the priority build order): a future `LLM
  Evaluation for Everyone` (this course's Chapter 12 introduces context
  evaluation specifically; a full evaluation course goes further),
  `Observability for Everyone` (this course's context-quality monitors
  are a narrower slice of what a full observability course would
  cover), an expanded `Agentic AI for Everyone` (this course's Module 5
  stops at the context decision per step; a future course goes deep on
  full agent architecture), and `AI Architecture for Everyone` (this
  course's capstone is one component of a fuller system-architecture
  discipline). This course is a deepening layer on top of
  `ai-engineering-for-everyone`'s shared engineering foundation, the
  same relationship `ai-engineering-for-everyone`'s own discovery notes
  anticipated when they named "Context Engineering for Everyone" as a
  course that "deepens what this course's Chapter 2 and Module 2 only
  introduce at the 'structure your prompt and context' level."

## 10. Cross-course overlap check (explicit, verified this session)

Checked this session by reading each neighbor's own curriculum
map/README, and — for the two highest-risk neighbors — the actual
lesson content, not just the summary:

- `rag-for-everyone`: deep on chunking, embeddings, vector stores, and
  retrieval quality (recall/precision, re-ranking) as an architecture
  pattern; RAG-specific context-injection safety material. No content
  found on token-budget allocation across multiple context sources, no
  content found on lost-in-the-middle context ordering, no content
  found on combining retrieved context with unrelated sources
  (conversation history, tool output) into one assembled window.
- `mcp-for-everyone`: deep on the MCP protocol's message shapes,
  client/server capability negotiation, and tool permission/sandboxing.
  No content found on what actually gets included in context from a
  tool result once it's returned, no content found on token-budget
  trade-offs for tool output.
- `ai-engineering-for-everyone` Chapter 3 (read in full this session,
  not just its summary): deep on prompt template versioning, structured
  composition of *static, checked-in* template pieces, prompt/code
  separation, a human-scale before/after check for a template change,
  diff review, and a change-management workflow for the template
  itself. No content found on token-budget allocation, memory-retrieval
  decisions, context compression, lost-in-the-middle, or multi-source
  assembly of the *dynamic, per-request* content that fills the
  template — the chapter's own text explicitly scopes itself to the
  template as a versioned artifact and treats what fills its variable
  slots (`{ticket_text}` and equivalents) as out of scope.
- `ai-engineering-for-everyone` more broadly (curriculum map and other
  chapter summaries): Module 3 (evaluation-driven development) evaluates
  *model output* quality against a golden set; no content found
  evaluating *context* quality (completeness, relevance, ordering)
  independent of the final answer, which is this course's Chapter 12's
  distinct subject.
- `ai-coding-agents-for-everyone`: deep on agent loops and coding-agent
  safety for one application category; no general content found on
  context-budget or context-isolation decisions across agent steps.

No existing course teaches context-window budget management, memory
retrieval decisions, context compression/curation, lost-in-the-middle
mitigation, multi-source context assembly, or context evaluation as a
dedicated subject. This course's scope is confirmed non-duplicative.
