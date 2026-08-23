"""
Chapter 2 Practice Bank: Designing Context Window Budgets -- REFERENCE SOLUTION

See starter.py for the eight scenarios. This file fills in every TODO
with a correct reference answer and scores a perfect total when run:

    python3 solution.py
"""

REQUEST_TYPE_PROFILES = {
    "short_lookup": {"L2": 0.45, "L3": 0.35, "L4": 0.20},
    "long_recurring": {"L2": 0.35, "L3": 0.40, "L4": 0.25},
    "tool_heavy": {"L2": 0.55, "L3": 0.25, "L4": 0.20},
    "long_document": {"L2": 0.65, "L3": 0.20, "L4": 0.15},
}

RECIPE_STEPS = {
    "step_fix_limit",
    "step_reserve_output",
    "step_fix_system",
    "step_split_profile",
    "step_validate_worst_case",
}

# Scenario 1 -- Marrenkirk Insurance Group: one dominant uploaded document,
# little history or memory -- the long_document archetype.
scenario_1_answer = "long_document"

# Scenario 2 -- Duvane Utilities Cooperative: no reserved output allowance
# at all -- step_reserve_output was skipped.
scenario_2_answer = "step_reserve_output"

# Scenario 3 -- Graytide Hospitality Group: NOT correct. Splitting L2/3/4
# against the full window before subtracting Line 1 overstates what's
# actually available, silently over-allocating every one of those three
# lines by however many tokens Line 1 actually costs.
scenario_3_answer = "no"

# Scenario 4 -- Oakspire Home Care Network: validated only against the
# median case, never the longest real conversations -- step_validate_worst_case
# was skipped.
scenario_4_answer = "step_validate_worst_case"

# Scenario 5 (judgment) -- Corundale Media Group: NOT sound. A bigger window
# raises Step 1's ceiling but doesn't remove the need to reserve output, fix
# system instructions, and split the remainder by this request type's real
# profile -- the recipe still has to run, just against a larger number.
scenario_5_answer = "no"

# Scenario 6 (judgment) -- Pallisade Manufacturing: NOT safe by itself. A
# matching profile shape only says the PERCENTAGE split should be similar --
# it says nothing about whether the two request types share the same window
# size, reserved-output size, or system-instructions size, all of which
# change the actual token numbers even when the percentages match.
scenario_6_answer = "no"

# Scenario 7 (production-gear) -- Redcliff Credit Union: 24,000 - 2,000 -
# 800 = 21,200 remaining; tool_heavy L2 = 21,200 * 0.55 = 11,660.
scenario_7_answer = round((24_000 - 2_000 - 800) * REQUEST_TYPE_PROFILES["tool_heavy"]["L2"])

# Scenario 8 (production-gear) -- Thackery Regional Exchange: L2 (9,000 vs
# 7,000) and L4 (3,000 vs 2,500) both have surplus; L3 (6,000 vs 8,200) is
# the real deficit.
scenario_8_answer = "L3"


# ===========================================================================
# Scoring harness -- identical to starter.py.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Marrenkirk Insurance Group)", scenario_1_answer.strip().lower() == "long_document", 1))
    results.append(("Scenario 2 (Duvane Utilities Cooperative)", scenario_2_answer.strip().lower() == "step_reserve_output", 1))
    results.append(("Scenario 3 (Graytide Hospitality Group)", scenario_3_answer.strip().lower() == "no", 1))
    results.append(("Scenario 4 (Oakspire Home Care Network)", scenario_4_answer.strip().lower() == "step_validate_worst_case", 1))
    results.append(("Scenario 5 (Corundale Media Group, judgment)", scenario_5_answer.strip().lower() == "no", 1))
    results.append(("Scenario 6 (Pallisade Manufacturing, judgment)", scenario_6_answer.strip().lower() == "no", 1))

    remaining_7 = 24_000 - 2_000 - 800
    expected_7 = round(remaining_7 * REQUEST_TYPE_PROFILES["tool_heavy"]["L2"])
    results.append(("Scenario 7 (Redcliff Credit Union)", scenario_7_answer == expected_7, 1))

    results.append(("Scenario 8 (Thackery Regional Exchange)", scenario_8_answer.strip().upper() == "L3", 1))

    return results


def main():
    print("Chapter 2 Practice Bank -- Score Report (reference solution)")
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
        print("Perfect score -- every scenario correctly allocated.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
