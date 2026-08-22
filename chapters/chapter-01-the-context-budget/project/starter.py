"""
Chapter 1 Project (L1 Guided): Diagnose CaseNote's Ledger Gaps

This is the course's first project -- a real, gradeable L1 Guided
project, not a preview. See README.md and RUBRIC.md for full context
and grading criteria.

THE SYSTEM
----------
Meridian Legal Aid Network is a fictional nonprofit legal-aid
organization. Its intake coordinators use CaseNote, an LLM-powered
assistant that helps gather a client's situation during an initial
intake conversation and drafts a structured case summary for a staff
attorney to review. It has been running for three months. Here is what
the team knows about how it actually operates today:

  1. CaseNote's system prompt has grown into an 1,800-word document
     combining role instructions, tone guidance, twelve categories of
     legal-topic routing rules, and unrelated formatting notes, all sent
     on every single request regardless of what the intake conversation
     is actually about.

  2. CaseNote retrieves legal-aid eligibility articles from a knowledge
     base as a conversation touches different topics. Nothing ever
     removes an earlier-retrieved article from the request once the
     topic moves on -- a session that starts on eviction defense and
     later shifts to child custody still carries all the original
     eviction articles in every later request.

  3. Intake conversations often run 25-50 turns as a coordinator
     gathers a client's full situation. CaseNote sends the complete raw
     transcript every turn with no summarization, and once a request
     exceeds the model's context window, the earliest turns are
     silently cut with no policy behind which ones go.

  4. A client's stated immigration status -- a fact that changes which
     legal-aid programs apply, and is often given once, early, in an
     intake session -- is never stored anywhere outside that session's
     own transcript. If the client returns for a follow-up conversation
     weeks later, CaseNote has no way to recall it, and the client has
     to restate sensitive information from scratch.

  5. CaseNote's context-budget check only accounts for what it's about
     to send the model. It does not reserve room for the model's own
     response, so on longer intake summaries the response is sometimes
     cut off mid-sentence -- right when it's explaining next steps to
     the client.

YOUR TASK
---------
For each of the five numbered facts above, in DIAGNOSIS below: identify
the single ledger line it maps to, write the evidence in your own
words, and write ONE concrete engineering fix (not "be more careful").
Then set PRIORITIZED_ORDER to the order you'd tackle the five fixes in
(a list of the five line IDs, most urgent first), and write
JUSTIFICATION explaining your prioritization in 2-4 sentences.

Fill in every TODO, then run:

    python3 starter.py

to see a structural self-check (this project is open-ended, so the
check verifies your diagnosis is complete and well-formed, not that it
matches one exact wording -- compare your reasoning against
solution.py for a full reference diagnosis).
"""

LEDGER_LINES = {
    "L1": "System Instructions",
    "L2": "Grounding Context",
    "L3": "Conversation History",
    "L4": "Recalled Long-Term Memory",
    "L5": "Working Space",
}

# TODO: for each fact (1-5 above), fill in "line" (one of the IDs above),
# "evidence" (a sentence in your own words), and "fix" (one concrete
# engineering change, at least 15 characters).
DIAGNOSIS = {
    "fact_1_system_prompt": {
        "line": "",      # TODO
        "evidence": "",  # TODO
        "fix": "",       # TODO
    },
    "fact_2_grounding": {
        "line": "",      # TODO
        "evidence": "",  # TODO
        "fix": "",       # TODO
    },
    "fact_3_history": {
        "line": "",      # TODO
        "evidence": "",  # TODO
        "fix": "",       # TODO
    },
    "fact_4_memory": {
        "line": "",      # TODO
        "evidence": "",  # TODO
        "fix": "",       # TODO
    },
    "fact_5_output": {
        "line": "",      # TODO
        "evidence": "",  # TODO
        "fix": "",       # TODO
    },
}

# TODO: order the five line IDs (e.g. ["L2", "L6", ...]) from most to
# least urgent to fix, in your judgment.
PRIORITIZED_ORDER = []

# TODO: 2-4 sentences justifying your prioritization above.
JUSTIFICATION = ""


# ===========================================================================
# Structural self-check -- do not need to edit anything below this line.
# This project is open-ended (there is more than one defensible fix per
# gap), so this check verifies completeness and internal consistency, not
# an exact match. Compare your full reasoning against solution.py.
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
    print("Chapter 1 Project -- Structural Self-Check")
    print("=" * 60)

    diag_errors = check_diagnosis()
    pri_errors = check_priority()
    all_errors = diag_errors + pri_errors

    if not all_errors:
        print("PASS -- diagnosis is complete, well-formed, and covers all 5 lines.")
        print("Now compare your reasoning (not just structure) against solution.py,")
        print("and check your work against RUBRIC.md before considering this project done.")
    else:
        print(f"{len(all_errors)} issue(s) found:")
        for e in all_errors:
            print(f"  - {e}")
        print("\nFix the issues above and re-run this file.")


if __name__ == "__main__":
    main()
