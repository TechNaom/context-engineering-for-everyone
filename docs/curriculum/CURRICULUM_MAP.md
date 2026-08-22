# Context Engineering for Everyone — Curriculum Map

LAST_REVIEWED: 2026-08-22

## Course Size

Focused emerging topic: 13 chapters, 4 projects (L1–L4), 1 capstone —
same sizing model as `mcp-for-everyone`, `ai-coding-agents-for-everyone`,
`ai-security-for-everyone`, and `ai-engineering-for-everyone`.

## Course Vision

Full reasoning and cross-course overlap check in `../discovery-notes.md`.
In short: this course teaches the engineering discipline of deciding
what actually goes into a model's context window at inference time, and
how it's organized once there — context budget management, memory
systems (short-term and long-term), context compression/curation,
multi-source context assembly, context engineering for agentic/
multi-step systems, and context evaluation. It is not retrieval
architecture (`rag-for-everyone`'s subject — RAG produces candidate
context; this course decides what makes it into the window), not
protocol-level tool integration (`mcp-for-everyone`'s subject), and not
the prompt template as a versioned software artifact
(`ai-engineering-for-everyone` Chapter 3's subject — this course assumes
the template is already managed and engineers the dynamic, per-request
content that fills it).

## Personas

- **`ai-engineering-for-everyone` graduate hitting a context wall** —
  ships production LLM features, treats prompts as versioned software,
  but the feature degrades as history/retrieved context grows and has
  no course teaching why.
- **RAG engineer whose retrieval metrics look fine but answers still
  degrade** — the problem is context assembly, not retrieval quality.
- **Agent/multi-step system builder debugging "it forgot" or "it got
  confused"** — the failure is a context-budget or context-isolation
  issue disguised as a model-quality issue.
- **Backend engineer building a long-running assistant/chat product** —
  needs memory and context-assembly design for long conversations
  without an unbounded, ever-growing prompt.

## Prerequisites

- Comfortable with Python (`python-for-everyone` level).
- Soft prerequisite, strongly recommended: `ai-engineering-for-everyone`
  — this course assumes the prompt template itself is already a managed,
  versioned artifact (that course's Chapter 3) and does not re-teach it
  or the rest of the LLM engineering stack from zero.
- Helpful, not required: `rag-for-everyone` (Chapter 8 assumes a ranked
  retrieval result as a given input) and `mcp-for-everyone` (Chapter 9
  assumes a tool call already happened by some protocol).

## Learning Outcomes

1. Explain the context budget mental model and use it to diagnose a
   real system's context-window misallocation.
2. Design a token budget across system instructions, history, retrieved
   context, and tool output for a given request type and hard limit.
3. Design short-term conversational memory that stays within budget
   under a long-running conversation without silently truncating
   load-bearing content.
4. Design a long-term/persistent memory system: what's stored, what's
   retrieved back into context for a given turn, and what stays dormant.
5. Compress and curate context without losing information the model
   needs, and defend against lost-in-the-middle degradation through
   context ordering.
6. Assemble context from multiple sources into one coherent window
   without the sources contradicting or crowding out each other.
7. Engineer context for tool-calling and multi-agent/multi-step
   systems, including deliberate context isolation between steps.
8. Evaluate assembled context quality before it reaches the model, and
   design and defend a complete context engineering system end to end
   (the capstone).

## Module Architecture

### Module 1 — The Context Budget Mental Model
**Purpose:** the core mental model (every token competes for a limited,
costed budget) and the practical skill of allocating it.
**Outcomes:** diagnose a real system's context-budget misallocation;
allocate a token budget across sources for a given request type.
**Chapters:** 1, 2
**Labs:** diagnose a given system's context-budget gaps; design a
budget allocation for a new request type
**Assessment:** concept + budget-allocation exercise

### Module 2 — Memory Systems
**Purpose:** what a system remembers within a conversation and across
sessions, and what gets retrieved back into context.
**Prerequisites:** Module 1
**Outcomes:** design short-term memory that stays in budget; design a
long-term memory system with a real retrieval-into-context policy.
**Chapters:** 3, 4
**Labs:** manage a long-running conversation's history under a hard
token limit; design a persistent memory store and retrieval policy
**Assessment:** memory-system design exam

### Module 3 — Context Compression and Curation
**Purpose:** making the most of a limited budget without losing
load-bearing content, and understanding why position matters.
**Prerequisites:** Module 2
**Outcomes:** compress/summarize context without losing what the model
needs; order context to avoid lost-in-the-middle degradation.
**Chapters:** 5, 6
**Labs:** build a summarization pipeline that preserves load-bearing
facts; reorder a context window to fix a lost-in-the-middle failure
**Assessment:** applied compression + ordering exercise

### Module 4 — Multi-Source Context Assembly
**Purpose:** combining retrieved documents, tool output, conversation
history, and system instructions into one coherent window.
**Prerequisites:** Module 3
**Outcomes:** assemble multi-source context without contradiction or
crowding; integrate a RAG pipeline's ranked results into context
correctly.
**Chapters:** 7, 8
**Labs:** assemble context from 3+ real sources for one request; take a
retriever's ranked output and produce well-formed context from it
**Assessment:** multi-source assembly + retrieval-integration review

### Module 5 — Context Engineering for Agentic Systems
**Purpose:** what context a step, tool call, or sub-agent actually
needs, and where deliberate isolation is the right design.
**Prerequisites:** Module 4
**Outcomes:** engineer context for a tool call; engineer context across
a multi-step/multi-agent pipeline with deliberate isolation.
**Chapters:** 9, 10, 11
**Labs:** design the context payload for a tool call; design a
multi-step pipeline's per-step context with isolation where it matters
**Assessment:** applied agentic-context design exercise

### Module 6 — Evaluation and Capstone
**Purpose:** measuring assembled context quality, and architect-level
synthesis.
**Prerequisites:** Module 5
**Outcomes:** evaluate context completeness/relevance/ordering before
it reaches the model; design and defend a complete context engineering
system.
**Chapters:** 12, 13
**Assessment:** context-evaluation exercise (Ch. 12) + capstone rubric
(Ch. 13, architecture challenge, Level 4)

## Chapter Roadmap

| # | Chapter | Module | Difficulty |
|---|---------|--------|------------|
| 1 | The Context Budget | 1 | Beginner |
| 2 | Designing Context Window Budgets | 1 | Intermediate |
| 3 | Short-Term Conversational Memory | 2 | Intermediate |
| 4 | Long-Term and Persistent Memory Systems | 2 | Intermediate |
| 5 | Context Compression and Summarization | 3 | Advanced |
| 6 | Avoiding Lost-in-the-Middle | 3 | Advanced |
| 7 | Multi-Source Context Assembly | 4 | Advanced |
| 8 | Retrieval Integration: From Ranked Results to Context | 4 | Advanced |
| 9 | Context Engineering for Tool Use | 5 | Advanced |
| 10 | Context Engineering for Multi-Agent Systems | 5 | Advanced |
| 11 | Context Isolation and Scoping | 5 | Advanced |
| 12 | Evaluating Context Quality | 6 | Advanced |
| 13 | Capstone: Designing a Context Engineering System | 6 | Architect |

## Projects

- **L1 Guided** — Diagnose a given system's context-budget gaps and
  design a fix plan (ships after Ch. 2).
- **L2 Assisted** — Design short-term and long-term memory for a
  provided long-running assistant, partial scaffold (ships after Ch. 4).
- **L3 Independent** — Build a compression/curation and multi-source
  assembly pipeline for a provided pipeline, no scaffold (ships after
  Ch. 8).
- **L4 Architecture Challenge** — Design and defend a complete context
  engineering system for a realistic multi-step/agentic system; business/
  system problem only (this is the capstone, Ch. 13).

## Cross-Course Links

- Builds on: `python-for-everyone` (baseline)
- Builds on, assumes, and does not re-teach:
  `ai-engineering-for-everyone` (the LLM engineering stack generally,
  and Chapter 3's "prompt as versioned software artifact" specifically)
- Builds on but does not duplicate: `rag-for-everyone` (retrieval
  architecture depth), `mcp-for-everyone` (tool/resource protocol
  depth), `ai-coding-agents-for-everyone` (agent-loop depth for one
  application category)
- Feeds: future `LLM Evaluation for Everyone`, `Observability for
  Everyone`, an expanded `Agentic AI for Everyone`, and `AI Architecture
  for Everyone` — this course is a deepening layer on top of
  `ai-engineering-for-everyone`'s shared engineering foundation.
