"""
Chapter 5 Practice Bank: Context Compression and Summarization -- REFERENCE SOLUTION

See README.md for the eight scenarios. This file fills in every TODO
with a correct reference answer and scores a perfect total when run:

    python3 solution.py
"""

# Scenario 1 (judgment) -- Lynhaven Community Health Partners: a team's
# conversation history gets compressed every time it exceeds budget.
# Does compression automatically lose load-bearing facts, or only when
# nothing extracts candidates and checks the result first?
scenario_1_answer = "only_with_no_fidelity_check"

# Scenario 2 (production-gear) -- Sablewood Legal Trust: a raw segment
# is 3,000 tokens; the fixed compression target is 600 tokens. How many
# tokens must be cut?
SABLEWOOD_RAW_TOKENS = 3_000
SABLEWOOD_TARGET_TOKENS = 600
scenario_2_answer = SABLEWOOD_RAW_TOKENS - SABLEWOOD_TARGET_TOKENS

# Scenario 3 (judgment) -- Coalridge Municipal Transit Authority: a team
# calls one prompt ("summarize this") and trusts whatever comes back,
# with no pre-extraction and no post-hoc check. Is that a sufficient
# compression policy for content a real decision depends on?
scenario_3_answer = "no"

# Scenario 4 (production-gear) -- Pikestone Logistics Group: three
# candidates were flagged before compressing. The produced summary's
# actual content is given below. Which candidates are missing, and does
# the fidelity check pass?
PIKESTONE_CANDIDATES = {"shipment_id_88213", "delay_reason_customs_hold", "warehouse_bay_7"}
PIKESTONE_SUMMARY_CONTENT = {"shipment_id_88213", "warehouse_bay_7"}
scenario_4_missing = PIKESTONE_CANDIDATES - PIKESTONE_SUMMARY_CONTENT
scenario_4_passes = len(scenario_4_missing) == 0

# Scenario 5 (judgment) -- Rowancraig Insurance Underwriters: a claims
# file has both narrative complaint text and a structured table of
# exact policy numbers and dates. Does an extractive strategy matter
# more for the structured table or the narrative text?
scenario_5_answer = "structured_table"

# Scenario 6 (production-gear) -- Draymoor Agricultural Cooperative: a
# content segment is a list of exact soil-sample lab results with
# specific numeric readings. Should this be compressed with an
# extractive strategy (True) or is abstractive paraphrase fine (False)?
scenario_6_answer = True

# Scenario 7 (production-gear) -- Osprey Ridge Wealth Management: a raw
# advisory conversation states a client's exact portfolio rebalance
# target of "22% bonds." Naive "summarize as concisely as possible"
# compression drops the exact percentage in favor of "adjusted their
# bond allocation." Does naive compression preserve the exact figure a
# downstream trade instruction depends on?
scenario_7_answer = False

# Scenario 8 (judgment) -- Talmarsh Veterinary Alliance: a fidelity
# check fails because a flagged candidate (a specific medication dosage)
# is missing from the compressed output. Is it safe to just retry the
# exact same naive prompt again, unchanged, and hope for a better
# result?
scenario_8_answer = "no"


# ===========================================================================
# Scoring harness -- identical to starter.py.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Lynhaven Community Health Partners, judgment)", scenario_1_answer.strip().lower() == "only_with_no_fidelity_check", 1))

    expected_2 = SABLEWOOD_RAW_TOKENS - SABLEWOOD_TARGET_TOKENS
    results.append(("Scenario 2 (Sablewood Legal Trust)", scenario_2_answer == expected_2, 1))

    results.append(("Scenario 3 (Coalridge Municipal Transit Authority, judgment)", scenario_3_answer.strip().lower() == "no", 1))

    expected_4_missing = PIKESTONE_CANDIDATES - PIKESTONE_SUMMARY_CONTENT
    expected_4_passes = len(expected_4_missing) == 0
    results.append(("Scenario 4 (Pikestone Logistics Group)", scenario_4_missing == expected_4_missing and scenario_4_passes == expected_4_passes, 1))

    results.append(("Scenario 5 (Rowancraig Insurance Underwriters, judgment)", scenario_5_answer.strip().lower() == "structured_table", 1))

    results.append(("Scenario 6 (Draymoor Agricultural Cooperative)", scenario_6_answer is True, 1))

    results.append(("Scenario 7 (Osprey Ridge Wealth Management)", scenario_7_answer is False, 1))

    results.append(("Scenario 8 (Talmarsh Veterinary Alliance, judgment)", scenario_8_answer.strip().lower() == "no", 1))

    return results


def main():
    print("Chapter 5 Practice Bank -- Score Report (reference solution)")
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
