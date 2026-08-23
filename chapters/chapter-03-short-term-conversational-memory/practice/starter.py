"""
Chapter 3 Practice Bank: Short-Term Conversational Memory

See README.md for the eight scenarios. Fill in each TODO, then run:

    python3 starter.py

to see a score report.
"""

# Scenario 1 (judgment) -- Larkmoth Outdoor Retail: a team's Conversation
# History (Line 3) budget was correctly allocated per Chapter 2's recipe,
# but a customer's early return-window request still gets "forgotten" in
# a long support conversation. A teammate proposes: "let's just raise
# Line 3's token budget." Does that actually fix the problem by itself?
# TODO: "yes" or "no"
scenario_1_answer = ""

# Scenario 2 (production-gear) -- Feldspar Municipal Water Utility: Line
# 3's budget is 5,000 tokens. Reserve 400 tokens for pinned facts and
# 1,200 tokens for a running summary. Average turn size is 450 tokens.
# TODO: how many recent turns can stay verbatim (integer division)?
FELDSPAR_LINE3_BUDGET = 5_000
FELDSPAR_PINNED_RESERVE = 400
FELDSPAR_SUMMARY_RESERVE = 1_200
FELDSPAR_AVG_TOKENS_PER_TURN = 450
scenario_2_answer = None  # TODO: int

# Scenario 3 (judgment) -- Pemberglen Veterinary Partners: a team decides
# to let its pinned-facts list grow without any size limit, reasoning
# that "important facts should never be at risk of eviction." Is an
# unlimited pinned-facts reserve a sound design?
# TODO: "yes" or "no"
scenario_3_answer = ""

# Scenario 4 (production-gear) -- Sootmarsh Freight Cooperative: the
# compression trigger threshold is 6,000 tokens. Given the cumulative
# token totals below (one entry per turn, in order), which turn (1-
# indexed) first reaches or exceeds the trigger?
SOOTMARSH_TRIGGER_THRESHOLD = 6_000
SOOTMARSH_CUMULATIVE = [500, 1_200, 2_000, 3_100, 4_400, 5_800, 7_000, 8_200]
scenario_4_answer = None  # TODO: int (1-indexed turn number)

# Scenario 5 (judgment) -- Glennoak Wealth Advisors: an engineer proposes
# summarizing every single turn immediately, starting from turn 1, so
# the running summary is "always up to date." Is running compression
# continuously from turn 1 a good idea?
# TODO: "yes" or "no"
scenario_5_answer = ""

# Scenario 6 (production-gear) -- Tarnwick Community College: a student
# tells the assistant they are currently unhoused, which is directly
# relevant to a priority financial-aid review. Should this fact be
# pinned?
# TODO: True or False
scenario_6_answer = None

# Scenario 7 (production-gear) -- Hushfield Telehealth Network: pinned
# facts = 350 tokens, running summary = 1,100 tokens, verbatim turns =
# 3,000 tokens, Line 3 budget = 5,000 tokens. Does the total package
# "fit" inside budget, or is it a "deficit"?
HUSHFIELD_PINNED_TOKENS = 350
HUSHFIELD_SUMMARY_TOKENS = 1_100
HUSHFIELD_VERBATIM_TOKENS = 3_000
HUSHFIELD_LINE3_BUDGET = 5_000
scenario_7_answer = ""  # TODO: "fits" or "deficit"

# Scenario 8 (judgment) -- Vallowmere Grocery Cooperative: a team adds a
# real compression policy (verbatim window + pinned facts + running
# summary) to a request type that previously had none. Does adding a
# compression policy remove the need to still validate the resulting
# package against the worst realistic case?
# TODO: "yes" or "no"
scenario_8_answer = ""


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Larkmoth Outdoor Retail, judgment)", scenario_1_answer.strip().lower() == "no", 1))

    expected_2 = (FELDSPAR_LINE3_BUDGET - FELDSPAR_PINNED_RESERVE - FELDSPAR_SUMMARY_RESERVE) // FELDSPAR_AVG_TOKENS_PER_TURN
    results.append(("Scenario 2 (Feldspar Municipal Water Utility)", scenario_2_answer == expected_2, 1))

    results.append(("Scenario 3 (Pemberglen Veterinary Partners, judgment)", scenario_3_answer.strip().lower() == "no", 1))

    expected_4 = next(i + 1 for i, total in enumerate(SOOTMARSH_CUMULATIVE) if total >= SOOTMARSH_TRIGGER_THRESHOLD)
    results.append(("Scenario 4 (Sootmarsh Freight Cooperative)", scenario_4_answer == expected_4, 1))

    results.append(("Scenario 5 (Glennoak Wealth Advisors, judgment)", scenario_5_answer.strip().lower() == "no", 1))

    results.append(("Scenario 6 (Tarnwick Community College)", scenario_6_answer is True, 1))

    _hushfield_total = HUSHFIELD_PINNED_TOKENS + HUSHFIELD_SUMMARY_TOKENS + HUSHFIELD_VERBATIM_TOKENS
    expected_7 = "fits" if _hushfield_total <= HUSHFIELD_LINE3_BUDGET else "deficit"
    results.append(("Scenario 7 (Hushfield Telehealth Network)", scenario_7_answer.strip().lower() == expected_7, 1))

    results.append(("Scenario 8 (Vallowmere Grocery Cooperative, judgment)", scenario_8_answer.strip().lower() == "no", 1))

    return results


def main():
    print("Chapter 3 Practice Bank -- Score Report")
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
        print("Perfect score -- every scenario correctly reasoned.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
