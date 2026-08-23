"""
Chapter 6 Practice Bank: Avoiding Lost-in-the-Middle -- REFERENCE SOLUTION

See README.md for the eight scenarios. This file fills in every TODO
with a correct reference answer and scores a perfect total when run:

    python3 solution.py
"""

# Scenario 1 (judgment) -- Nunroth Independent Bookstore Cooperative: a
# team moves every load-bearing fact to the very front of the context
# window. Does that alone guarantee the model reliably uses every fact,
# or does the query/instruction still need its own reserved anchor near
# generation?
scenario_1_answer = "no"

# Scenario 2 (production-gear) -- Vesparro Marine Salvage: a 4,000-token
# assembled window; a load-bearing fact starts at token 1,800 and runs
# 80 tokens. What integer percentile of the window does its midpoint
# fall at (midpoint * 100 // total, integer division)?
VESPARRO_TOTAL_TOKENS = 4_000
VESPARRO_FACT_START = 1_800
VESPARRO_FACT_LENGTH = 80
scenario_2_answer = (
    (VESPARRO_FACT_START + VESPARRO_FACT_LENGTH // 2) * 100 // VESPARRO_TOTAL_TOKENS
)

# Scenario 3 (judgment) -- Holstead Grain Exchange: a compressed fact
# passed Chapter 5's own fidelity check (present, unmodified, within
# budget). Is a passed fidelity check alone sufficient proof the model
# will reliably use that fact from wherever it happens to sit in the
# final window?
scenario_3_answer = "no"

# Scenario 4 (production-gear) -- Quenby Historical Archive Society: two
# facts require an anchor position; the actual produced window's anchor
# placements are given below. Which required facts are missing from the
# anchors, and does the placement pass its own probe?
QUENBY_ANCHOR_REQUIRED = {"founding_charter_date", "donor_restriction_clause"}
QUENBY_ACTUAL_ANCHOR_PLACEMENTS = {"founding_charter_date"}
scenario_4_missing = QUENBY_ANCHOR_REQUIRED - QUENBY_ACTUAL_ANCHOR_PLACEMENTS
scenario_4_passes = len(scenario_4_missing) == 0

# Scenario 5 (judgment) -- Farrowline Dairy Cooperative: does the exact
# shape and magnitude of the lost-in-the-middle effect stay identical
# across every model family and every context length, or does it need
# re-testing per model per this chapter's own re-verified research?
scenario_5_answer = "varies_by_model_and_length"

# Scenario 6 (production-gear) -- Delacroix Regional Airport Authority:
# a 500-turn historical maintenance log is part of the assembled window.
# Does this content belong at the end anchor nearest generation (True),
# or is it reference/history material that belongs elsewhere (False)?
scenario_6_answer = False

# Scenario 7 (production-gear) -- Pennwhistle Community Radio Network: a
# specific frequency-change detail sits in the middle of a long
# maintenance conversation. Does leaving the window in plain arrival
# order reliably surface that detail when asked about it directly?
scenario_7_answer = False

# Scenario 8 (judgment) -- Ostergaard Marine Insurance: a positional
# probe fails once, flagging a load-bearing clause still buried in the
# middle band. Is it safe to just re-run the exact same arrival-order
# pipeline again, unchanged, and hope for a better result?
scenario_8_answer = "no"


# ===========================================================================
# Scoring harness -- identical to starter.py.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Nunroth Independent Bookstore Cooperative, judgment)", scenario_1_answer.strip().lower() == "no", 1))

    expected_2 = (VESPARRO_FACT_START + VESPARRO_FACT_LENGTH // 2) * 100 // VESPARRO_TOTAL_TOKENS
    results.append(("Scenario 2 (Vesparro Marine Salvage)", scenario_2_answer == expected_2, 1))

    results.append(("Scenario 3 (Holstead Grain Exchange, judgment)", scenario_3_answer.strip().lower() == "no", 1))

    expected_4_missing = QUENBY_ANCHOR_REQUIRED - QUENBY_ACTUAL_ANCHOR_PLACEMENTS
    expected_4_passes = len(expected_4_missing) == 0
    results.append(("Scenario 4 (Quenby Historical Archive Society)", scenario_4_missing == expected_4_missing and scenario_4_passes == expected_4_passes, 1))

    results.append(("Scenario 5 (Farrowline Dairy Cooperative, judgment)", scenario_5_answer.strip().lower() == "varies_by_model_and_length", 1))

    results.append(("Scenario 6 (Delacroix Regional Airport Authority)", scenario_6_answer is False, 1))

    results.append(("Scenario 7 (Pennwhistle Community Radio Network)", scenario_7_answer is False, 1))

    results.append(("Scenario 8 (Ostergaard Marine Insurance, judgment)", scenario_8_answer.strip().lower() == "no", 1))

    return results


def main():
    print("Chapter 6 Practice Bank -- Score Report (reference solution)")
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
