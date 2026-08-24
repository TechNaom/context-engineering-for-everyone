/*
  Single source of truth for the Context Engineering for Everyone chapter
  roster. Mirrors the ai-engineering-for-everyone pattern: sidebar.js and
  home.js render navigation from this file. A chapter is "live" iff it has
  a `path` -- omit `path` for chapters that don't exist yet, do not set a
  placeholder path, or sidebar/home will link to a 404. The same rule
  applies to a module's `examPath`: set it to null until that module's
  written exam actually exists in assessments/written-exams/.

  Chapters 1-2 (Module 1, complete), Chapters 3-4 (Module 2, complete),
  Chapters 5-6 (Module 3, complete), Chapters 7-8 (Module 4, complete),
  and Chapters 9-11 (Module 5, complete) are live as of this build --
  see PROJECT_STATE.md for status. Chapter 12 (Module 6, opening) is now
  live too. Chapter 13 is planned, `.gitkeep`'d, not yet built.
*/

window.CEFE_MODULES = [
  {
    title: "Module 1 — The Context Budget Mental Model",
    summary: "What the context window actually is, and the budget discipline that governs everything else in this course.",
    examPath: null,
    chapters: [
      {
        id: "chapter-01",
        num: 1,
        title: "The Context Budget",
        description: "Every token in the window costs something and competes for a limited budget -- the mental model the rest of this course deepens.",
        path: "chapters/chapter-01-the-context-budget/lesson.html"
      },
      {
        id: "chapter-02",
        num: 2,
        title: "Designing Context Window Budgets",
        description: "Allocating a fixed token budget across system instructions, history, retrieved context, and tool output -- on purpose, not by accident.",
        path: "chapters/chapter-02-designing-context-window-budgets/lesson.html"
      }
    ]
  },
  {
    title: "Module 2 — Memory Systems",
    summary: "What a system remembers between turns, and between sessions.",
    examPath: null,
    chapters: [
      {
        id: "chapter-03",
        num: 3,
        title: "Short-Term Conversational Memory",
        description: "Managing the turn-by-turn conversation history inside a bounded window without silently truncating something load-bearing.",
        path: "chapters/chapter-03-short-term-conversational-memory/lesson.html"
      },
      {
        id: "chapter-04",
        num: 4,
        title: "Long-Term and Persistent Memory Systems",
        description: "What a system should remember across sessions, how it's stored, and the real decision of what to retrieve back into context later.",
        path: "chapters/chapter-04-long-term-and-persistent-memory-systems/lesson.html"
      }
    ]
  },
  {
    title: "Module 3 — Context Compression and Curation",
    summary: "Making the most of a limited budget: what to compress, and where in the window it goes.",
    examPath: null,
    chapters: [
      {
        id: "chapter-05",
        num: 5,
        title: "Context Compression and Summarization",
        description: "Summarizing or truncating prior turns intelligently instead of blindly -- and knowing what compression actually loses.",
        path: "chapters/chapter-05-context-compression-and-summarization/lesson.html"
      },
      {
        id: "chapter-06",
        num: 6,
        title: "Avoiding Lost-in-the-Middle",
        description: "Why position inside the context window changes how well a model uses information, and how to curate and order context around it.",
        path: "chapters/chapter-06-avoiding-lost-in-the-middle/lesson.html"
      }
    ]
  },
  {
    title: "Module 4 — Multi-Source Context Assembly",
    summary: "Combining retrieved documents, tool outputs, conversation history, and system instructions into one coherent context.",
    examPath: null,
    chapters: [
      {
        id: "chapter-07",
        num: 7,
        title: "Multi-Source Context Assembly",
        description: "Composing several context sources into one window without the pieces contradicting or crowding out each other.",
        path: "chapters/chapter-07-multi-source-context-assembly/lesson.html"
      },
      {
        id: "chapter-08",
        num: 8,
        title: "Retrieval Integration: From Ranked Results to Context",
        description: "Turning a retriever's ranked results into well-formed context -- the handoff point with RAG, not a re-run of retrieval architecture.",
        path: "chapters/chapter-08-retrieval-integration/lesson.html"
      }
    ]
  },
  {
    title: "Module 5 — Context Engineering for Agentic Systems",
    summary: "What context a step, a tool call, or a sub-agent actually needs -- not everything, by default.",
    examPath: null,
    chapters: [
      {
        id: "chapter-09",
        num: 9,
        title: "Context Engineering for Tool Use",
        description: "Deciding what tool definitions, results, and history a model needs in context for a tool call -- distinct from the protocol MCP defines.",
        path: "chapters/chapter-09-tool-use-context/lesson.html"
      },
      {
        id: "chapter-10",
        num: 10,
        title: "Context Engineering for Multi-Agent Systems",
        description: "What context each step or sub-agent needs versus inheriting everything indiscriminately, across a multi-step pipeline.",
        path: "chapters/chapter-10-multi-agent-context/lesson.html"
      },
      {
        id: "chapter-11",
        num: 11,
        title: "Context Isolation and Scoping",
        description: "Deliberately withholding context between agents or steps as a design choice, not an oversight -- and where that isolation breaks down, closing Module 5.",
        path: "chapters/chapter-11-context-isolation-and-scoping/lesson.html"
      }
    ]
  },
  {
    title: "Module 6 — Evaluation and Capstone",
    summary: "Is the assembled context actually good, and can you defend a complete context engineering system end to end.",
    examPath: null,
    chapters: [
      {
        id: "chapter-12",
        num: 12,
        title: "Evaluating Context Quality",
        description: "Measuring whether assembled context is complete, relevant, and well-ordered -- before it ever reaches the model, opening Module 6.",
        path: "chapters/chapter-12-evaluating-context-quality/lesson.html"
      },
      {
        id: "chapter-13",
        num: 13,
        title: "Capstone: Designing a Context Engineering System",
        description: "A Level 4 architecture challenge composing budget, memory, compression, assembly, and evaluation into one real system."
      }
    ]
  }
];
