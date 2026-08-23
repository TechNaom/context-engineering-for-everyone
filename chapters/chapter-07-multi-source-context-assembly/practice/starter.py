"""
Chapter 7 Practice Bank: Multi-Source Context Assembly

See README.md for the eight scenarios. Fill in each `# TODO`, then run:

    python3 starter.py

to see a score report. Compare against solution.py, which scores a
perfect total.
"""

AUTHORITY_RANK = {
    "system_instructions": 4,
    "live_tool_output": 3,
    "conversation_history": 2,
    "retrieved_document": 1,
}

# Scenario 1 (judgment) -- Juniper Ridge Veterinary Partners: a
# retrieved vaccination-history document and a live clinic-system tool
# call, both individually correct, are joined in whatever order they
# arrived, with no authority ranking and no contradiction check. Does
# that guarantee the combined result is coherent?
# TODO: "yes" or "no"
scenario_1_answer = None

# Scenario 2 (production-gear) -- Quarrydale Auto Diagnostics
# Cooperative: a retrieved service-history document and a live
# recall-status tool call disagree about the same claim
# ("current_recall_status"). Which source wins per AUTHORITY_RANK?
QUARRYDALE_SOURCE_X = "retrieved_document"
QUARRYDALE_SOURCE_Y = "live_tool_output"
# TODO: QUARRYDALE_SOURCE_X or QUARRYDALE_SOURCE_Y, whichever has the
# higher AUTHORITY_RANK value
scenario_2_answer = None

# Scenario 3 (judgment) -- Tamworth Regional Housing Trust: a team
# strips exact duplicate sentences across a lease-policy document and
# the system instructions, but never ranks authority and never checks
# whether two sources disagree using different wording. Is that a
# sufficient assembly step on its own?
# TODO: "yes" or "no"
scenario_3_answer = None

# Scenario 4 (production-gear) -- Wexford Maritime Charter Group: a
# three-week-old retrieved document states a charter fee of "$450/day";
# a live booking-system tool call states "$525/day" for the same
# charter type -- a genuine contradiction. Separately, the retrieved
# document says "check in at the marina office" and the conversation
# history says "meet at the marina office" -- the same fact, restated.
# True = genuine contradiction; False = restatement or unrelated fact.
WEXFORD_CLAIM_PAIRS = {
    "charter_fee_conflict": True,
    "checkin_location_restatement": False,
}
# TODO: fill in your own True/False call for each key (should match
# WEXFORD_CLAIM_PAIRS once reasoned through)
scenario_4_answers = {
    "charter_fee_conflict": None,  # TODO
    "checkin_location_restatement": None,  # TODO
}

# Scenario 5 (judgment) -- Dovetail Woodcraft Guild: deduplicating
# restated content across two sources frees a large number of tokens,
# comfortably inside budget. Does that alone guarantee no contradiction
# remains in the assembled set?
# TODO: "yes" or "no"
scenario_5_answer = None

# Scenario 6 (production-gear) -- Cinderfield Volunteer Fire Network: a
# claim ("station_coverage_area") is asserted by a retrieved document
# (90 tokens) and by the system instructions (30 tokens). Which source
# should be kept, and how many tokens does dropping the other save?
CINDERFIELD_INSTANCES = [
    ("retrieved_document", 90),
    ("system_instructions", 30),
]


def _highest_authority_instance(instances):
    return max(instances, key=lambda pair: AUTHORITY_RANK[pair[0]])


# TODO: the source name (str) with the higher AUTHORITY_RANK
scenario_6_kept_source = None
# TODO: sum of all instance token costs minus the kept instance's own cost (int)
scenario_6_tokens_saved = None

# Scenario 7 (production-gear) -- Barleycroft Grain & Feed Cooperative:
# a retrieved grain-quality document says the moisture threshold for
# acceptance is "14%"; a live grain-sensor tool call says "18%" for the
# same delivery -- a genuine, load-bearing contradiction (accepting or
# rejecting a delivery depends on it). Naive concatenation includes both
# claims unresolved (500 raw tokens). The Source Assembly Recipe
# resolves the contradiction via authority ranking (live sensor wins)
# and deduplicates 40 tokens of restated content elsewhere. Does naive
# concatenation leave the contradiction unresolved? Does the recipe
# resolve it? Does the resolved total still fit the 480-token budget?
BARLEYCROFT_BUDGET_TOKENS = 480
BARLEYCROFT_NAIVE_TOTAL_TOKENS = 500
BARLEYCROFT_TOKENS_FREED = 40

# TODO: bool -- does naive concatenation leave the contradiction unresolved?
scenario_7_naive_contains_contradiction = None
# TODO: bool -- does the recipe resolve the contradiction?
scenario_7_recipe_resolves_contradiction = None
# TODO: int -- BARLEYCROFT_NAIVE_TOTAL_TOKENS minus BARLEYCROFT_TOKENS_FREED
scenario_7_resolved_total = None
# TODO: bool -- does scenario_7_resolved_total fit BARLEYCROFT_BUDGET_TOKENS?
scenario_7_within_budget = None

# Scenario 8 (judgment) -- Yewmarsh Wildlife Sanctuary: a review finds
# one contradiction where both sources share the exact same authority
# rank, giving no clear winner. Is it safe to ship the assembled context
# as-is, or must the pipeline resolve or escalate the tie?
# TODO: "ship_as_is" or "resolve_or_escalate"
scenario_8_answer = None


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Juniper Ridge Veterinary Partners, judgment)", (scenario_1_answer or "").strip().lower() == "no", 1))

    expected_2 = (
        QUARRYDALE_SOURCE_X
        if AUTHORITY_RANK[QUARRYDALE_SOURCE_X] > AUTHORITY_RANK[QUARRYDALE_SOURCE_Y]
        else QUARRYDALE_SOURCE_Y
    )
    results.append(("Scenario 2 (Quarrydale Auto Diagnostics Cooperative)", scenario_2_answer == expected_2, 1))

    results.append(("Scenario 3 (Tamworth Regional Housing Trust, judgment)", (scenario_3_answer or "").strip().lower() == "no", 1))

    correct_4 = sum(1 for k, v in WEXFORD_CLAIM_PAIRS.items() if scenario_4_answers.get(k) == v)
    results.append(("Scenario 4 (Wexford Maritime Charter Group)", correct_4 == len(WEXFORD_CLAIM_PAIRS), 1))

    results.append(("Scenario 5 (Dovetail Woodcraft Guild, judgment)", (scenario_5_answer or "").strip().lower() == "no", 1))

    expected_6_kept = _highest_authority_instance(CINDERFIELD_INSTANCES)[0]
    expected_6_saved = sum(t for _, t in CINDERFIELD_INSTANCES) - _highest_authority_instance(CINDERFIELD_INSTANCES)[1]
    results.append(("Scenario 6 (Cinderfield Volunteer Fire Network)", scenario_6_kept_source == expected_6_kept and scenario_6_tokens_saved == expected_6_saved, 1))

    expected_7_resolved = BARLEYCROFT_NAIVE_TOTAL_TOKENS - BARLEYCROFT_TOKENS_FREED
    expected_7_within = expected_7_resolved <= BARLEYCROFT_BUDGET_TOKENS
    results.append((
        "Scenario 7 (Barleycroft Grain & Feed Cooperative)",
        scenario_7_naive_contains_contradiction is True
        and scenario_7_recipe_resolves_contradiction is True
        and scenario_7_resolved_total == expected_7_resolved
        and scenario_7_within_budget == expected_7_within,
        1,
    ))

    results.append(("Scenario 8 (Yewmarsh Wildlife Sanctuary, judgment)", (scenario_8_answer or "").strip().lower() == "resolve_or_escalate", 1))

    return results


def main():
    print("Chapter 7 Practice Bank -- Score Report")
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
