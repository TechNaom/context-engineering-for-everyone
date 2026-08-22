"""
Chapter 1 Practice Bank: The Context Budget -- REFERENCE SOLUTION

See starter.py for the eight scenarios. This file fills in every TODO
with a correct reference answer and scores a perfect total when run:

    python3 solution.py
"""

LEDGER_LINES = {
    "L1": "System Instructions",
    "L2": "Grounding Context",
    "L3": "Conversation History",
    "L4": "Recalled Long-Term Memory",
    "L5": "Working Space",
}

# Scenario 1 -- Windermere Legal Services: eleven paragraphs of accumulated
# boilerplate in the system prompt, never pruned -- a System Instructions
# (L1) gap.
scenario_1_answer = "L1"

# Scenario 2 -- Pinecrest Veterinary Group: stale retrieved articles never
# evicted from the request -- a Grounding Context (L2) gap.
scenario_2_answer = "L2"

# Scenario 3 -- Solmark Payments: unsummarized transcript exceeds the
# window and the earliest turns are silently dropped -- Conversation
# History (L3).
scenario_3_answer = "L3"

# Scenario 4 -- Thistledown Air Cargo: no persistent memory layer, so a
# fact from an earlier session is never recalled in a later one --
# Recalled Long-Term Memory (L4).
scenario_4_answer = "L4"

# Scenario 5 (judgment) -- Ravenhollow University Registrar: sending the
# full transcript only during low-traffic hours still means every
# individual long conversation eventually exceeds the window regardless of
# time of day -- traffic volume and per-conversation budget overrun are
# unrelated. A real gap remains.
scenario_5_answer = "no"

# Scenario 6 (judgment, prioritization) -- Copperfield Home Appliances:
# within this chapter's ledger, the missing eviction policy on grounding
# context (a) is the higher-priority fix -- it's a real, growing budget
# risk affecting every long session. A cosmetic spelling inconsistency (b)
# has no budget or correctness impact.
scenario_6_answer = "a"

# Scenario 7 (production-gear) -- Marrowgate Public Library: a re-ranking/
# eviction step that drops stale retrieved articles (b) directly builds
# Grounding Context discipline; a bigger model, a faster database, and a
# UI redesign don't touch what's actually competing for budget.
scenario_7_answer = "b"

# Scenario 8 (production-gear) -- Fenwick Outdoor Adventures: no
# summarization on the full transcript (Conversation History, L3) and no
# re-fetch of persisted facts across turns (Recalled Long-Term Memory, L4)
# are the two most directly missing lines.
scenario_8_answers = ["L3", "L4"]


# ===========================================================================
# Scoring harness -- identical to starter.py.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Windermere Legal Services)", scenario_1_answer == "L1", 1))
    results.append(("Scenario 2 (Pinecrest Veterinary Group)", scenario_2_answer == "L2", 1))
    results.append(("Scenario 3 (Solmark Payments)", scenario_3_answer == "L3", 1))
    results.append(("Scenario 4 (Thistledown Air Cargo)", scenario_4_answer == "L4", 1))
    results.append(("Scenario 5 (Ravenhollow University Registrar, judgment)", scenario_5_answer.strip().lower() == "no", 1))
    results.append(("Scenario 6 (Copperfield Home Appliances, judgment)", scenario_6_answer.strip().lower() == "a", 1))
    results.append(("Scenario 7 (Marrowgate Public Library)", scenario_7_answer.strip().lower() == "b", 1))

    s8_key = {"L3", "L4"}
    s8_given = set(scenario_8_answers)
    results.append(("Scenario 8 (Fenwick Outdoor Adventures)", s8_given == s8_key, 1))

    return results


def main():
    print("Chapter 1 Practice Bank -- Score Report (reference solution)")
    print("=" * 60)
    results = score()
    total_correct = 0
    total_possible = 0
    for label, correct, possible in results:
        total_correct += int(correct) * possible
        total_possible += possible
        mark = "PASS" if correct else "FAIL"
        print(f"{label}: {mark}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every scenario correctly diagnosed.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
