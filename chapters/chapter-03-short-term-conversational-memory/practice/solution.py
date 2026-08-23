"""
Chapter 3 Practice Bank: Short-Term Conversational Memory -- REFERENCE SOLUTION

See README.md for the eight scenarios. This file fills in every TODO
with a correct reference answer and scores a perfect total when run:

    python3 solution.py
"""

# Scenario 1 (judgment) -- Larkmoth Outdoor Retail: raising Line 3's
# token budget alone doesn't fix "the assistant forgot my return window
# request." A bigger budget delays when raw truncation kicks in, but
# without a real eviction/compression policy an early load-bearing fact
# in a long enough conversation still eventually falls out -- the same
# mistake at a later turn count, not a different mistake.
scenario_1_answer = "no"

# Scenario 2 (production-gear) -- Feldspar Municipal Water Utility:
# verbatim budget = 5,000 - 400 - 1,200 = 3,400; at 450 tokens/turn,
# 3,400 // 450 = 7 verbatim turns.
FELDSPAR_LINE3_BUDGET = 5_000
FELDSPAR_PINNED_RESERVE = 400
FELDSPAR_SUMMARY_RESERVE = 1_200
FELDSPAR_AVG_TOKENS_PER_TURN = 450
scenario_2_answer = (
    FELDSPAR_LINE3_BUDGET - FELDSPAR_PINNED_RESERVE - FELDSPAR_SUMMARY_RESERVE
) // FELDSPAR_AVG_TOKENS_PER_TURN

# Scenario 3 (judgment) -- Pemberglen Veterinary Partners: a pinned-fact
# list should NOT be unlimited. An unbounded pin list just recreates the
# original budget problem under a different name -- if every fact can be
# pinned, nothing is actually prioritized, and the pinned-facts reserve
# itself needs its own budget with the least-critical pins evicted or
# folded into the summary first.
scenario_3_answer = "no"

# Scenario 4 (production-gear) -- Sootmarsh Freight Cooperative: first
# turn whose cumulative total reaches or exceeds the 6,000-token trigger.
SOOTMARSH_TRIGGER_THRESHOLD = 6_000
SOOTMARSH_CUMULATIVE = [500, 1_200, 2_000, 3_100, 4_400, 5_800, 7_000, 8_200]
scenario_4_answer = next(
    i + 1 for i, total in enumerate(SOOTMARSH_CUMULATIVE) if total >= SOOTMARSH_TRIGGER_THRESHOLD
)

# Scenario 5 (judgment) -- Glennoak Wealth Advisors: summarizing every
# turn immediately, starting from turn 1, is NOT a good idea. It burns
# compute and latency compressing turns that are still inside the
# verbatim window and haven't aged out yet, and repeated early
# summarization of very recent, still-relevant turns risks losing detail
# the model still needs this turn -- compression should trigger once a
# real threshold is reached, not run continuously from the first turn.
scenario_5_answer = "no"

# Scenario 6 (production-gear) -- Tarnwick Community College: a student
# reporting being unhoused, relevant to a priority financial-aid review,
# is safety/eligibility-critical and should be pinned.
scenario_6_answer = True

# Scenario 7 (production-gear) -- Hushfield Telehealth Network: total =
# 350 + 1,100 + 3,000 = 4,450, which fits inside the 5,000-token budget.
HUSHFIELD_PINNED_TOKENS = 350
HUSHFIELD_SUMMARY_TOKENS = 1_100
HUSHFIELD_VERBATIM_TOKENS = 3_000
HUSHFIELD_LINE3_BUDGET = 5_000
_hushfield_total = HUSHFIELD_PINNED_TOKENS + HUSHFIELD_SUMMARY_TOKENS + HUSHFIELD_VERBATIM_TOKENS
scenario_7_answer = "fits" if _hushfield_total <= HUSHFIELD_LINE3_BUDGET else "deficit"

# Scenario 8 (judgment) -- Vallowmere Grocery Cooperative: adding a
# compression policy does NOT remove the need to still validate against
# the worst realistic case. Compression changes HOW content is kept
# inside budget; it does not guarantee the resulting package (pinned
# facts + summary + verbatim turns) actually fits the worst-case
# conversation without a real validation pass, the same discipline
# Chapter 2 already established for allocation itself.
scenario_8_answer = "no"


# ===========================================================================
# Scoring harness -- identical to starter.py.
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

    expected_7 = "fits" if _hushfield_total <= HUSHFIELD_LINE3_BUDGET else "deficit"
    results.append(("Scenario 7 (Hushfield Telehealth Network)", scenario_7_answer.strip().lower() == expected_7, 1))

    results.append(("Scenario 8 (Vallowmere Grocery Cooperative, judgment)", scenario_8_answer.strip().lower() == "no", 1))

    return results


def main():
    print("Chapter 3 Practice Bank -- Score Report (reference solution)")
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
