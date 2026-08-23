"""
Chapter 9 Exercises: Tool-Use Context -- REFERENCE SOLUTION

Scenario: Kestrel Regional Grid Operations Cooperative, a fictional
multi-substation electric grid operator. Its dispatcher-support
assistant, RelayLine, has nine registered tools but only ever calls two
of them for a "Substation Overload Risk Check" request. Chapters 1-8's
own recipes have already run for this request type: a correct budget,
correct memory handling, nothing over budget needing compression, no
positional risk, and (once this chapter's own bundle is ready) no
multi-source contradiction left unresolved. The protocol carrying a
tool call is correct and out of scope; your job is this chapter's own
new skill: scoping tool definitions, curating and boundary-safely
fitting a tool's raw result, and managing tool-call history across a
multi-step loop.

This file fills in every TODO with a correct reference answer and
scores a perfect total when run:

    python3 solution.py
"""

# ===========================================================================
# Exercise 1 -- match each scenario to the right tool-context approach.
# ===========================================================================
APPROACHES = {"unconditional_full_registry", "scoped_tools_raw_passthrough", "tool_context_recipe"}

EXERCISE_1_SCENARIOS = {
    "all_nine_tool_schemas_sent_every_call_raw_result_char_cutoff": (
        "Every one of the nine registered tools' schemas is sent on "
        "every call regardless of request type, and a called tool's "
        "raw result is appended verbatim, then cut off wherever the "
        "budget runs out by raw character count."
    ),
    "only_two_tools_scoped_in_but_raw_result_still_dumped_and_cutoff": (
        "Only the two tools this request type can actually call are "
        "included, but a called tool's full raw result is still "
        "appended verbatim with no field curation or boundary-safe fit."
    ),
    "scope_budget_curate_fit_evict_handoff": (
        "Tool definitions are scoped to the request type, each "
        "included schema is budgeted explicitly, a called tool's raw "
        "result is curated to only the fields needed, the curated "
        "result is fit to budget at a field boundary, superseded "
        "tool-call history is evicted, and the resolved bundle is "
        "handed to Chapter 7's own Source Assembly Recipe."
    ),
}

exercise_1_answers = {
    "all_nine_tool_schemas_sent_every_call_raw_result_char_cutoff": "unconditional_full_registry",
    "only_two_tools_scoped_in_but_raw_result_still_dumped_and_cutoff": "scoped_tools_raw_passthrough",
    "scope_budget_curate_fit_evict_handoff": "tool_context_recipe",
}

# ===========================================================================
# Exercise 2 -- order the Tool Context Recipe's six steps.
# ===========================================================================
RECIPE_STEPS = {
    "step_scope_tools": "Scope tool definitions to the request type -- don't include every registered tool's schema unconditionally.",
    "step_budget_schema": "Budget each included tool's schema as its own explicit line item, paid whether or not the tool is actually called this turn.",
    "step_curate_result": "Curate a tool's raw result to only the fields this request type actually needs before it enters context.",
    "step_boundary_safe_fit": "Fit the curated result to budget at a field boundary, never truncating mid-key or mid-value.",
    "step_evict_history": "Budget and evict superseded tool-call history across a multi-step loop.",
    "step_handoff_source_assembly": "Hand the resolved, typed tool_result to Chapter 7's own Source Assembly Recipe.",
}

exercise_2_order = [
    "step_scope_tools",
    "step_budget_schema",
    "step_curate_result",
    "step_boundary_safe_fit",
    "step_evict_history",
    "step_handoff_source_assembly",
]

# ===========================================================================
# Exercise 3 (production-gear) -- request-type tool scoping and schema
# budget.
# ===========================================================================
TOOL_SCHEMA_TOKENS = {
    "substation_status": 210,
    "load_forecast": 240,
    "crew_roster": 220,
    "outage_map": 260,
    "weather_alert": 230,
    "breaker_history": 250,
    "maintenance_ticket_create": 200,
    "fuel_reserve": 190,
    "vendor_contact": 180,
}

OVERLOAD_RISK_CHECK_TOOLS = {"substation_status", "load_forecast"}

exercise_3_unconditional_total_tokens = sum(TOOL_SCHEMA_TOKENS.values())
exercise_3_scoped_total_tokens = sum(
    v for k, v in TOOL_SCHEMA_TOKENS.items() if k in OVERLOAD_RISK_CHECK_TOOLS
)
exercise_3_tokens_saved = exercise_3_unconditional_total_tokens - exercise_3_scoped_total_tokens

# ===========================================================================
# Exercise 4 (production-gear) -- result curation.
# ===========================================================================
SUBSTATION_RAW_FIELDS = {
    "station_id": ("KGRD-14", 8),
    "region": ("Kestrel North Division", 10),
    "voltage_class_kv": (69, 5),
    "current_load_pct": (94, 6),
    "capacity_mva": (150, 5),
    "last_inspection_date": ("2026-03-14", 8),
    "breaker_status": ("closed", 6),
    "active_alert": ("Overload warning -- load exceeds 90% capacity", 14),
    "maintenance_crew_assigned": ("Crew 7", 6),
    "gps_coordinates": ("41.02,-104.88", 10),
    "asset_age_years": (18, 5),
}

exercise_4_curated_fields = {"station_id", "current_load_pct", "breaker_status", "active_alert"}

# ===========================================================================
# Exercise 5 (production-gear) -- field-boundary-safe budget fit.
# ===========================================================================
FIELD_PRIORITY_ORDER = ["active_alert", "station_id", "breaker_status", "current_load_pct"]
TOOL_RESULT_BUDGET_TOKENS = 30


def _boundary_safe_field_fit(fields, priority_order, budget):
    kept = []
    running_total = 0
    for key in priority_order:
        _, tokens = fields[key]
        if running_total + tokens <= budget:
            kept.append(key)
            running_total += tokens
    return kept, running_total


exercise_5_kept_fields, exercise_5_total_tokens = _boundary_safe_field_fit(
    SUBSTATION_RAW_FIELDS, FIELD_PRIORITY_ORDER, TOOL_RESULT_BUDGET_TOKENS
)

# ===========================================================================
# Exercise 6 (production-gear) -- tool-call history eviction.
# ===========================================================================
TOOL_CALL_HISTORY = {
    "call_1": {"tool": "substation_status", "station": "KGRD-14", "turn": 2},
    "call_2": {"tool": "load_forecast", "station": "KGRD-14", "turn": 3},
    "call_3": {"tool": "substation_status", "station": "KGRD-14", "turn": 9},
    "call_4": {"tool": "substation_status", "station": "KGRD-9", "turn": 10},
}


def _is_superseded(call_id, history):
    call = history[call_id]
    for other_id, other in history.items():
        if other_id == call_id:
            continue
        if other["tool"] == call["tool"] and other["station"] == call["station"] and other["turn"] > call["turn"]:
            return True
    return False


exercise_6_answers = {call_id: _is_superseded(call_id, TOOL_CALL_HISTORY) for call_id in TOOL_CALL_HISTORY}

# ===========================================================================
# Exercise 7 (production-gear) -- naive-vs-recipe regression gate.
# ===========================================================================
NAIVE_FIELD_ORDER = [
    "station_id", "region", "voltage_class_kv", "current_load_pct",
    "capacity_mva", "last_inspection_date", "breaker_status",
    "active_alert", "maintenance_crew_assigned", "gps_coordinates",
    "asset_age_years",
]
NAIVE_CUTOFF_BUDGET_TOKENS = 30


def _naive_char_cutoff_kept_fields(fields, field_order, budget):
    kept = []
    running_total = 0
    for key in field_order:
        _, tokens = fields[key]
        if running_total + tokens <= budget:
            kept.append(key)
            running_total += tokens
        else:
            break
    return kept


_naive_kept = _naive_char_cutoff_kept_fields(SUBSTATION_RAW_FIELDS, NAIVE_FIELD_ORDER, NAIVE_CUTOFF_BUDGET_TOKENS)

exercise_7_naive_drops_active_alert = "active_alert" not in _naive_kept
exercise_7_recipe_preserves_active_alert = "active_alert" in exercise_5_kept_fields
exercise_7_recipe_within_budget = exercise_5_total_tokens <= TOOL_RESULT_BUDGET_TOKENS

# ===========================================================================
# Exercise 8 (production-gear) -- source-assembly handoff typing.
# ===========================================================================
EXERCISE_8_CANDIDATES = {
    "item_a": {"type": "tool_result", "curated": True, "stale": False},
    "item_b": {"type": "tool_result", "curated": False, "stale": False},
    "item_c": {"type": None, "curated": True, "stale": False},
    "item_d": {"type": "tool_result", "curated": True, "stale": True},
}


def _is_ready_for_handoff(item):
    return item["type"] == "tool_result" and item["curated"] is True and item["stale"] is False


exercise_8_answers = {key: _is_ready_for_handoff(item) for key, item in EXERCISE_8_CANDIDATES.items()}


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_exercise_1():
    key = {
        "all_nine_tool_schemas_sent_every_call_raw_result_char_cutoff": "unconditional_full_registry",
        "only_two_tools_scoped_in_but_raw_result_still_dumped_and_cutoff": "scoped_tools_raw_passthrough",
        "scope_budget_curate_fit_evict_handoff": "tool_context_recipe",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_scope_tools",
        "step_budget_schema",
        "step_curate_result",
        "step_boundary_safe_fit",
        "step_evict_history",
        "step_handoff_source_assembly",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    expected_unconditional = sum(TOOL_SCHEMA_TOKENS.values())
    expected_scoped = sum(v for k, v in TOOL_SCHEMA_TOKENS.items() if k in OVERLOAD_RISK_CHECK_TOOLS)
    expected_saved = expected_unconditional - expected_scoped
    correct = 0
    correct += int(exercise_3_unconditional_total_tokens == expected_unconditional)
    correct += int(exercise_3_scoped_total_tokens == expected_scoped)
    correct += int(exercise_3_tokens_saved == expected_saved)
    return correct, 3


def score_exercise_4():
    expected = {"station_id", "current_load_pct", "breaker_status", "active_alert"}
    correct = int(exercise_4_curated_fields == expected)
    return correct, 1


def score_exercise_5():
    expected_kept, expected_total = _boundary_safe_field_fit(
        SUBSTATION_RAW_FIELDS, FIELD_PRIORITY_ORDER, TOOL_RESULT_BUDGET_TOKENS
    )
    correct = 0
    correct += int(exercise_5_kept_fields == expected_kept)
    correct += int(exercise_5_total_tokens == expected_total)
    return correct, 2


def score_exercise_6():
    correct = sum(
        1 for call_id in TOOL_CALL_HISTORY
        if exercise_6_answers.get(call_id) == _is_superseded(call_id, TOOL_CALL_HISTORY)
    )
    return correct, len(TOOL_CALL_HISTORY)


def score_exercise_7():
    naive_kept = _naive_char_cutoff_kept_fields(SUBSTATION_RAW_FIELDS, NAIVE_FIELD_ORDER, NAIVE_CUTOFF_BUDGET_TOKENS)
    expected_naive_drops = "active_alert" not in naive_kept
    recipe_kept, recipe_total = _boundary_safe_field_fit(
        SUBSTATION_RAW_FIELDS, FIELD_PRIORITY_ORDER, TOOL_RESULT_BUDGET_TOKENS
    )
    correct = 0
    correct += int(exercise_7_naive_drops_active_alert == expected_naive_drops)
    correct += int(exercise_7_recipe_preserves_active_alert == ("active_alert" in recipe_kept))
    correct += int(exercise_7_recipe_within_budget == (recipe_total <= TOOL_RESULT_BUDGET_TOKENS))
    return correct, 3


def score_exercise_8():
    correct = sum(
        1 for k, item in EXERCISE_8_CANDIDATES.items()
        if exercise_8_answers.get(k) == _is_ready_for_handoff(item)
    )
    return correct, len(EXERCISE_8_CANDIDATES)


def main():
    exercises = [
        ("Exercise 1 -- match scenarios to tool-context approaches", score_exercise_1),
        ("Exercise 2 -- order the Tool Context Recipe", score_exercise_2),
        ("Exercise 3 -- request-type tool scoping and schema budget", score_exercise_3),
        ("Exercise 4 -- result curation", score_exercise_4),
        ("Exercise 5 -- field-boundary-safe budget fit", score_exercise_5),
        ("Exercise 6 -- tool-call history eviction", score_exercise_6),
        ("Exercise 7 -- naive-vs-recipe regression gate", score_exercise_7),
        ("Exercise 8 -- source-assembly handoff typing", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 9 Exercises -- Score Report (REFERENCE SOLUTION)")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    print(
        f"Field-boundary-safe fit kept: {exercise_5_kept_fields} "
        f"| total tokens: {exercise_5_total_tokens}/{TOOL_RESULT_BUDGET_TOKENS}"
    )


if __name__ == "__main__":
    main()
