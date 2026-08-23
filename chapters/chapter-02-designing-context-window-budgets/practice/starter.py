"""
Chapter 2 Practice Bank: Designing Context Window Budgets

Eight short, independent scenarios, each its own fictional system --
none of them Vantry Health Network/TriageLine or Corravine Freight/
DispatchLine again. Each scenario is a few sentences and one judgment
or arithmetic question about ALLOCATING a budget, not diagnosing one
already broken. The point isn't depth on one system -- it's speed and
accuracy across many different systems, the way a real pre-launch
budget review actually feels.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
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

# ---------------------------------------------------------------------------
# Scenario 1 -- Marrenkirk Insurance Group: a claims-review assistant adds a
# new "Document-Heavy Claim Review" request type, where one large uploaded
# claim file dominates almost every request, with little conversation
# history or persisted memory involved. Which archetype profile (a key in
# REQUEST_TYPE_PROFILES) fits this request type?
# ---------------------------------------------------------------------------
scenario_1_answer = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 2 -- Duvane Utilities Cooperative: an outage-report assistant's
# team allocates Lines 1 through 4 carefully, then lets the model's response
# use "however much is left over, however much that turns out to be,"
# reserving nothing up front. Which recipe step (a value from RECIPE_STEPS)
# did they skip?
# ---------------------------------------------------------------------------
scenario_2_answer = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 3 -- Graytide Hospitality Group: a booking-concierge assistant's
# team computes the Line 2/3/4 split first, using the FULL context window as
# the base, and only afterward subtracts Line 1's system-instructions tokens
# from whatever's left. Is this ordering still correct? (yes/no)
# ---------------------------------------------------------------------------
scenario_3_answer = ""  # TODO: "yes" or "no"

# ---------------------------------------------------------------------------
# Scenario 4 -- Oakspire Home Care Network: a caregiver-scheduling
# assistant's team tests their new budget allocation only against typical,
# average-length scheduling conversations from last month's logs, and never
# checks it against the longest real conversations in their own data. Which
# recipe step (a value from RECIPE_STEPS) did they skip?
# ---------------------------------------------------------------------------
scenario_4_answer = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 5 (judgment) -- Corundale Media Group: a content-review
# assistant's team upgrades from a 16,000-token model to a 128,000-token
# model and declares "our budget allocation problem is solved -- there's
# plenty of room for everything now, no more per-request-type work needed."
# Is this reasoning sound? (yes/no)
# ---------------------------------------------------------------------------
scenario_5_answer = ""  # TODO: "yes" or "no"

# ---------------------------------------------------------------------------
# Scenario 6 (judgment) -- Pallisade Manufacturing: a quality-inspection
# assistant has two request types that happen to share the same archetype
# profile (both are short lookups). A teammate argues this means it's safe
# to copy one request type's EXACT numeric token budget onto the other
# without re-deriving anything, since "the profile already matches." Is this
# safe? (yes/no)
# ---------------------------------------------------------------------------
scenario_6_answer = ""  # TODO: "yes" or "no"

# ---------------------------------------------------------------------------
# Scenario 7 (production-gear) -- Redcliff Credit Union: a fraud-review
# tool-dispatch assistant runs on a 24,000-token context window, reserving
# 2,000 tokens for output and 800 for system instructions. Using the
# "tool_heavy" profile, what is the Grounding Context (L2) allocation, in
# tokens (rounded to the nearest integer)?
# ---------------------------------------------------------------------------
scenario_7_answer = None  # TODO: integer

# ---------------------------------------------------------------------------
# Scenario 8 (production-gear) -- Thackery Regional Exchange: a shipped
# budget allocated L2=9,000, L3=6,000, L4=3,000 tokens. A worst-case audit
# finds the actual need is L2=7,000, L3=8,200, L4=2,500 tokens. Which single
# ledger line ("L2", "L3", or "L4") is under-provisioned (a real deficit)?
# ---------------------------------------------------------------------------
scenario_8_answer = ""  # TODO: "L2", "L3", or "L4"


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
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
    print("Chapter 2 Practice Bank -- Score Report")
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
