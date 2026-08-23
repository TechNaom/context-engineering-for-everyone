"""
Chapter 9 Practice Bank: Tool-Use Context -- REFERENCE SOLUTION

See README.md for the eight scenarios. This file fills in every TODO
with a correct reference answer and scores a perfect total when run:

    python3 solution.py
"""

# Scenario 1 (judgment) -- Winslow County Emergency Medical Services: a
# dispatch assistant registers all fourteen of its tools' schemas on
# every call, regardless of request type. Does that guarantee the model
# selects the correct tool for a given request?
scenario_1_answer = "no"

# Scenario 2 (production-gear) -- Gullwick Harbor Pilotage Authority:
# five registered tools, with the schema token costs below. The
# "Vessel Arrival Clearance" request type only ever calls
# vessel_position and tide_table. Compute the unconditional total, the
# scoped total, and tokens saved.
GULLWICK_TOOL_SCHEMA_TOKENS = {
    "vessel_position": 180,
    "tide_table": 150,
    "weather_marine": 220,
    "berth_schedule": 190,
    "customs_manifest": 260,
}
GULLWICK_SCOPED_TOOLS = {"vessel_position", "tide_table"}

scenario_2_unconditional_total = sum(GULLWICK_TOOL_SCHEMA_TOKENS.values())
scenario_2_scoped_total = sum(v for k, v in GULLWICK_TOOL_SCHEMA_TOKENS.items() if k in GULLWICK_SCOPED_TOOLS)
scenario_2_tokens_saved = scenario_2_unconditional_total - scenario_2_scoped_total

# Scenario 3 (judgment) -- Sparrowmere Independent News Network: a
# fact-checking assistant curates a source-lookup tool's raw result down
# from twenty fields to the four fields the request type actually needs.
# Does that curation step, by itself, guarantee the curated four-field
# result fits inside the request type's token budget?
scenario_3_answer = "no"

# Scenario 4 (production-gear) -- Hazelcombe Regional Blood Bank
# Network: fit the curated fields below to a 25-token budget, in the
# given priority order, keeping a field only if it fits whole.
HAZELCOMBE_FIELDS_WITH_TOKENS = {
    "expiry_alert": 9,
    "unit_id": 7,
    "blood_type_inventory": 12,
    "temperature_log": 15,
}
HAZELCOMBE_PRIORITY_ORDER = ["expiry_alert", "unit_id", "blood_type_inventory", "temperature_log"]
HAZELCOMBE_BUDGET_TOKENS = 25


def _boundary_safe_field_fit(fields_with_tokens, priority_order, budget):
    kept = []
    total = 0
    for key in priority_order:
        tokens = fields_with_tokens[key]
        if total + tokens <= budget:
            kept.append(key)
            total += tokens
    return kept, total


scenario_4_kept_fields, scenario_4_total_tokens = _boundary_safe_field_fit(
    HAZELCOMBE_FIELDS_WITH_TOKENS, HAZELCOMBE_PRIORITY_ORDER, HAZELCOMBE_BUDGET_TOKENS
)

# Scenario 5 (judgment) -- Renfrew Municipal Snow Removal Cooperative: a
# plow-routing assistant correctly curates and boundary-fits this turn's
# road-condition tool result. Does that, by itself, guarantee an earlier
# turn's road-condition result for the same route is no longer treated
# as current?
scenario_5_answer = "no"

# Scenario 6 (production-gear) -- Dunbar Ridge Avalanche Forecast
# Center: for each pair, should call A be marked superseded (same tool,
# same region, and call B happened at a later turn)?
DUNBAR_RIDGE_PAIRS = {
    "pair_x": {"tool_a": "avalanche_risk_lookup", "region_a": "North Cirque", "turn_a": 4,
               "tool_b": "avalanche_risk_lookup", "region_b": "North Cirque", "turn_b": 11},
    "pair_y": {"tool_a": "avalanche_risk_lookup", "region_a": "North Cirque", "turn_a": 4,
               "tool_b": "avalanche_risk_lookup", "region_b": "South Bowl", "turn_b": 11},
}


def _is_superseded_pair(pair):
    return pair["tool_a"] == pair["tool_b"] and pair["region_a"] == pair["region_b"] and pair["turn_b"] > pair["turn_a"]


scenario_6_answers = {key: _is_superseded_pair(pair) for key, pair in DUNBAR_RIDGE_PAIRS.items()}

# Scenario 7 (production-gear) -- Corvale Regional Air Ambulance
# Consortium: a load-bearing "landing zone hazard" field is at risk of
# truncation under a naive character-count cutoff over a 40-token
# budget. The recipe's own boundary-safe fit keeps every field needed,
# resolving to 36 tokens total. Does naive concatenation drop the
# load-bearing field? Does the recipe preserve it? Does the resolved
# total still fit budget?
CORVALE_BUDGET_TOKENS = 40
CORVALE_NAIVE_TOTAL_TOKENS = 52  # all fields concatenated, no boundary awareness -- overshoots budget
CORVALE_RECIPE_RESOLVED_TOTAL_TOKENS = 36  # curated + boundary-fit, landing-zone-hazard field kept

scenario_7_naive_drops_load_bearing_field = True
scenario_7_recipe_preserves_load_bearing_field = True
scenario_7_resolved_total = CORVALE_RECIPE_RESOLVED_TOTAL_TOKENS
scenario_7_within_budget = scenario_7_resolved_total <= CORVALE_BUDGET_TOKENS

# Scenario 8 (judgment) -- Whitmore County Livestock Health Cooperative:
# a herd-health-status tool call times out this turn. Is it safe to
# silently reuse a stale cached result from three calls ago as if it
# were current, or should the pipeline surface that the tool result is
# currently unavailable?
scenario_8_answer = "surface_tool_unavailable"


# ===========================================================================
# Scoring harness -- identical to starter.py.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Winslow County Emergency Medical Services, judgment)", scenario_1_answer.strip().lower() == "no", 1))

    expected_2_unconditional = sum(GULLWICK_TOOL_SCHEMA_TOKENS.values())
    expected_2_scoped = sum(v for k, v in GULLWICK_TOOL_SCHEMA_TOKENS.items() if k in GULLWICK_SCOPED_TOOLS)
    expected_2_saved = expected_2_unconditional - expected_2_scoped
    results.append((
        "Scenario 2 (Gullwick Harbor Pilotage Authority)",
        scenario_2_unconditional_total == expected_2_unconditional
        and scenario_2_scoped_total == expected_2_scoped
        and scenario_2_tokens_saved == expected_2_saved,
        1,
    ))

    results.append(("Scenario 3 (Sparrowmere Independent News Network, judgment)", scenario_3_answer.strip().lower() == "no", 1))

    expected_4_kept, expected_4_total = _boundary_safe_field_fit(
        HAZELCOMBE_FIELDS_WITH_TOKENS, HAZELCOMBE_PRIORITY_ORDER, HAZELCOMBE_BUDGET_TOKENS
    )
    results.append((
        "Scenario 4 (Hazelcombe Regional Blood Bank Network)",
        scenario_4_kept_fields == expected_4_kept and scenario_4_total_tokens == expected_4_total,
        1,
    ))

    results.append(("Scenario 5 (Renfrew Municipal Snow Removal Cooperative, judgment)", scenario_5_answer.strip().lower() == "no", 1))

    correct_6 = sum(1 for k, pair in DUNBAR_RIDGE_PAIRS.items() if scenario_6_answers.get(k) == _is_superseded_pair(pair))
    results.append(("Scenario 6 (Dunbar Ridge Avalanche Forecast Center)", correct_6 == len(DUNBAR_RIDGE_PAIRS), 1))

    results.append((
        "Scenario 7 (Corvale Regional Air Ambulance Consortium)",
        scenario_7_naive_drops_load_bearing_field is True
        and scenario_7_recipe_preserves_load_bearing_field is True
        and scenario_7_resolved_total == CORVALE_RECIPE_RESOLVED_TOTAL_TOKENS
        and scenario_7_within_budget is True,
        1,
    ))

    results.append(("Scenario 8 (Whitmore County Livestock Health Cooperative, judgment)", scenario_8_answer.strip().lower() == "surface_tool_unavailable", 1))

    return results


def main():
    print("Chapter 9 Practice Bank -- Score Report (reference solution)")
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
