"""
Chapter 1 Project (L1 Guided): Diagnose CaseNote's Ledger Gaps -- REFERENCE SOLUTION

See starter.py for the full system description and task instructions.
This is ONE valid, complete diagnosis -- not the only correct wording,
since this project is intentionally open-ended. Use it to check your
reasoning's completeness and rigor, not to match text exactly.
"""

LEDGER_LINES = {
    "L1": "System Instructions",
    "L2": "Grounding Context",
    "L3": "Conversation History",
    "L4": "Recalled Long-Term Memory",
    "L5": "Working Space",
}

DIAGNOSIS = {
    "fact_1_system_prompt": {
        "line": "L1",
        "evidence": (
            "The system prompt has grown to 1,800 words of mixed role "
            "instructions, tone guidance, topic routing rules, and "
            "formatting notes, all sent in full on every request "
            "regardless of the conversation's actual topic."
        ),
        "fix": (
            "Audit the system prompt and split it into a small, always-"
            "sent core plus topic-specific routing blocks only included "
            "when that topic is actually active in the conversation."
        ),
    },
    "fact_2_grounding": {
        "line": "L2",
        "evidence": (
            "Retrieved eligibility articles are never evicted once the "
            "conversation moves to a new topic, so articles about a "
            "topic already resolved keep competing for space in every "
            "later request."
        ),
        "fix": (
            "Add a re-ranking/eviction step that drops retrieved "
            "articles once the conversation's current sub-topic no "
            "longer matches what they were retrieved for."
        ),
    },
    "fact_3_history": {
        "line": "L3",
        "evidence": (
            "The full raw transcript of a 25-50 turn intake conversation "
            "is sent every turn with no summarization, and once it "
            "exceeds the context window, the earliest turns are dropped "
            "with no policy behind the cut."
        ),
        "fix": (
            "Summarize turns older than the most recent N into a "
            "compact running summary, and keep only the most recent N "
            "turns verbatim, instead of a blind end-of-window cut."
        ),
    },
    "fact_4_memory": {
        "line": "L4",
        "evidence": (
            "A client's immigration status, stated once in an earlier "
            "session, is never stored outside that session's own "
            "transcript, so a later follow-up conversation has no way "
            "to recall it."
        ),
        "fix": (
            "Add a persistent memory store for case-critical facts "
            "(immigration status, prior program eligibility) that is "
            "explicitly re-fetched at the start of every new session for "
            "a returning client, independent of any transcript."
        ),
    },
    "fact_5_output": {
        "line": "L5",
        "evidence": (
            "The budget check only accounts for input content sent to "
            "the model, with no reserved room for its own response, so "
            "longer case summaries sometimes get cut off mid-sentence."
        ),
        "fix": (
            "Reserve a fixed output-token allowance as part of the "
            "budget calculation before deciding how much input content "
            "fits, so the real, tighter input budget is visible up "
            "front instead of causing a surprise truncation."
        ),
    },
}

# Prioritization reasoning: Conversation History (L3) first, because an
# unbounded transcript is the fastest-growing, most immediate risk in a
# 25-50 turn intake conversation and directly causes case-critical facts to
# disappear mid-session. Recalled Long-Term Memory (L4) second, because it
# is the direct fix for sensitive information (immigration status) being
# lost between sessions entirely -- a real client-harm risk, not just an
# inconvenience. Grounding Context (L2) third, a real and growing but
# slower-building risk than L3. Working Space (L5) fourth, since mid-
# sentence truncation is visible and annoying but not as harmful as a lost
# fact. System Instructions (L1) last -- real waste, but it is a fixed,
# bounded cost per request rather than a risk that compounds as a
# conversation grows.
PRIORITIZED_ORDER = ["L3", "L4", "L2", "L5", "L1"]

JUSTIFICATION = (
    "Conversation History comes first because an unbounded transcript is "
    "the fastest-growing risk in a long intake conversation and directly "
    "causes case-critical facts to disappear mid-session. Recalled "
    "Long-Term Memory comes second because losing sensitive client "
    "information between sessions is a real harm, not just an "
    "inconvenience. Grounding Context and Working Space follow as real "
    "but slower-building or less harmful gaps, and System Instructions is "
    "prioritized last because it is a fixed, bounded cost per request "
    "rather than a risk that compounds as a conversation grows."
)


# ===========================================================================
# Structural self-check -- identical to starter.py.
# ===========================================================================

def check_diagnosis():
    errors = []
    expected_facts = {
        "fact_1_system_prompt", "fact_2_grounding",
        "fact_3_history", "fact_4_memory", "fact_5_output",
    }
    given_facts = set(DIAGNOSIS.keys())
    if given_facts != expected_facts:
        errors.append(f"DIAGNOSIS must have exactly these keys: {sorted(expected_facts)}")

    lines_used = []
    for fact, entry in DIAGNOSIS.items():
        line = entry.get("line", "")
        evidence = entry.get("evidence", "")
        fix = entry.get("fix", "")
        if line not in LEDGER_LINES:
            errors.append(f"{fact}: 'line' must be one of {list(LEDGER_LINES)}, got {line!r}")
        else:
            lines_used.append(line)
        if len(evidence.strip()) < 10:
            errors.append(f"{fact}: 'evidence' is missing or too short")
        if len(fix.strip()) < 15:
            errors.append(f"{fact}: 'fix' is missing or too short (needs a real, concrete change)")

    if len(set(lines_used)) != 5:
        errors.append(
            f"Expected all 5 distinct ledger lines to be used across the 5 facts, "
            f"got {len(set(lines_used))} distinct lines -- each fact maps to a "
            f"DIFFERENT line in this scenario."
        )

    return errors


def check_priority():
    errors = []
    expected = set(LEDGER_LINES.keys())
    given = set(PRIORITIZED_ORDER)
    if given != expected or len(PRIORITIZED_ORDER) != 5:
        errors.append(
            f"PRIORITIZED_ORDER must contain each of {sorted(expected)} exactly once, "
            f"got {PRIORITIZED_ORDER}"
        )
    if len(JUSTIFICATION.strip()) < 40:
        errors.append("JUSTIFICATION should be a real 2-4 sentence explanation (40+ characters)")
    return errors


def main():
    print("Chapter 1 Project -- Structural Self-Check (reference solution)")
    print("=" * 60)

    diag_errors = check_diagnosis()
    pri_errors = check_priority()
    all_errors = diag_errors + pri_errors

    if not all_errors:
        print("PASS -- diagnosis is complete, well-formed, and covers all 5 lines.")
    else:
        print(f"{len(all_errors)} issue(s) found:")
        for e in all_errors:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
