"""
Chapter 13 Exercises: Capstone: Designing a Context Engineering System
-- REFERENCE SOLUTION.

Scenario: a second Castellan Fleet Logistics case, deliberately
different from the lesson's own I-80 closure incident -- Unit 2290
(driver M. Alvarado), running a cold-chain load (CFL-90410) from
Boise to Reno, reports a reefer-unit (refrigeration) mechanical
warning mid-route. This is not a road-closure incident; it is a
cargo-integrity incident, and it exercises the same eleven-recipe
composition against a genuinely different set of facts. Applying the
recipe stack to a fresh scenario, from scratch, is the point --
recalling the lesson's own I-80 answers by heart won't get you through
this.

Run:
    python3 solution.py
"""

# ===========================================================================
# Exercise 1 -- match each situation to the recipe that resolves it.
# ===========================================================================
RECIPES = {
    "budget_allocation", "short_term_memory", "long_term_memory",
    "compression_fidelity", "context_ordering", "source_assembly",
    "retrieval_integration", "tool_context", "pipeline_multi_agent",
    "context_isolation", "context_evaluation",
}

EXERCISE_1_SITUATIONS = {
    "reefer_alert_buried_third_in_arrival_order": "context_ordering",
    "manifest_says_load_ok_telematics_says_temp_excursion": "source_assembly",
    "raw_reefer_sensor_dump_has_40_unused_fields": "tool_context",
    "prior_reefer_incident_from_6_months_ago_recalled_might_be_outdated": "long_term_memory",
    "cargo_agent_reasoning_must_not_leak_into_customer_message": "context_isolation",
    "finished_bundle_looks_fine_but_was_never_actually_scored": "context_evaluation",
}

# TODO: assign a recipe name from RECIPES to each situation.
exercise_1_answers = {
    "reefer_alert_buried_third_in_arrival_order": "context_ordering",
    "manifest_says_load_ok_telematics_says_temp_excursion": "source_assembly",
    "raw_reefer_sensor_dump_has_40_unused_fields": "tool_context",
    "prior_reefer_incident_from_6_months_ago_recalled_might_be_outdated": "long_term_memory",
    "cargo_agent_reasoning_must_not_leak_into_customer_message": "context_isolation",
    "finished_bundle_looks_fine_but_was_never_actually_scored": "context_evaluation",
}


# ===========================================================================
# Exercise 2 -- Context Budget Ledger arithmetic (Ch. 1-2)
# ===========================================================================
HARD_LIMIT = 5500

# TODO: given this cargo-integrity request type's own five lines, compute
# the total and whether it validates against the hard limit.
LEDGER = {
    "line1_system": 340,
    "line2_grounding": 2100,
    "line3_history": 700,
    "line4_memory": 960,
    "line5_working_space": 1300,
}

exercise_2_total = sum(LEDGER.values())  # TODO
exercise_2_fits_limit = exercise_2_total <= HARD_LIMIT  # TODO
exercise_2_spare = HARD_LIMIT - exercise_2_total  # TODO


# ===========================================================================
# Exercise 3 -- short-term memory: verbatim window vs. pin vs. compress (Ch. 3)
# ===========================================================================
TURNS = [
    {"id": "a1", "tokens": 80},   # driver clocks in
    {"id": "a2", "tokens": 120},  # normal pre-trip cold-chain seal check
    {"id": "a3", "tokens": 260},  # PINNED: dispatcher logs a one-time temp
                                   # tolerance exception approved by the customer
    {"id": "a4", "tokens": 90},   # routine border crossing
    {"id": "a5", "tokens": 300},  # reefer mechanical warning (newest, decisive)
]
VERBATIM_BUDGET = 320
PINNED_IDS = {"a3"}

# TODO: classify each turn as "verbatim", "pinned", or "compress".
exercise_3_answers = {
    "a1": "compress",
    "a2": "compress",
    "a3": "pinned",
    "a4": "compress",
    "a5": "verbatim",
}


# ===========================================================================
# Exercise 4 -- context isolation: what crosses the boundary? (Ch. 11)
# ===========================================================================
# The Cargo-Integrity Agent reasons over the reefer sensor data and the
# customer's own cold-chain tolerance contract to decide whether the load
# is still sellable. Only a resolved fact should cross to the
# Customer-Comms Agent -- never the agent's own raw sensor-by-sensor
# reasoning or the contract's exact tolerance thresholds (commercially
# sensitive, not the customer's own business to see restated back at them).
ISOLATION_CANDIDATES = {
    "sellable_status_true_or_false": True,          # crosses
    "raw_sensor_readings_by_minute": False,          # stays
    "exact_contract_tolerance_thresholds": False,    # stays
    "recommended_customer_message_tone": True,       # crosses (a curated fact, not raw reasoning)
    "cargo_agents_own_step_by_step_reasoning_trace": False,  # stays
}

# TODO: for each candidate, decide True (crosses the isolation boundary)
# or False (stays inside the Cargo-Integrity Agent's own scope).
exercise_4_answers = {
    "sellable_status_true_or_false": True,
    "raw_sensor_readings_by_minute": False,
    "exact_contract_tolerance_thresholds": False,
    "recommended_customer_message_tone": True,
    "cargo_agents_own_step_by_step_reasoning_trace": False,
}


# ===========================================================================
# Exercise 5 -- Context Evaluation Recipe gate arithmetic (Ch. 12)
# ===========================================================================
REQUIRED_FACTS = {"reefer_status", "sellable_decision", "customer_notify_decision", "new_eta"}
PRESENT_FACTS = {"reefer_status", "sellable_decision", "customer_notify_decision"}  # new_eta missing
NOISE_TOKENS = 30
TOTAL_TOKENS = 400
COMPLETENESS_THRESHOLD = 0.9
NOISE_CEILING = 0.15

# TODO: compute completeness, noise ratio, and whether the gate passes.
exercise_5_completeness = len(REQUIRED_FACTS & PRESENT_FACTS) / len(REQUIRED_FACTS)
exercise_5_noise_ratio = NOISE_TOKENS / TOTAL_TOKENS
exercise_5_gate_passes = (
    exercise_5_completeness >= COMPLETENESS_THRESHOLD
    and exercise_5_noise_ratio <= NOISE_CEILING
)


# ===========================================================================
# Scoring
# ===========================================================================

def score_exercise_1():
    correct = sum(1 for k, v in EXERCISE_1_SITUATIONS.items() if exercise_1_answers.get(k) == v)
    return correct, len(EXERCISE_1_SITUATIONS)


def score_exercise_2():
    expected_total = sum(LEDGER.values())
    expected_fits = expected_total <= HARD_LIMIT
    expected_spare = HARD_LIMIT - expected_total
    correct = 0
    correct += int(exercise_2_total == expected_total)
    correct += int(exercise_2_fits_limit == expected_fits)
    correct += int(exercise_2_spare == expected_spare)
    return correct, 3


def score_exercise_3():
    expected = {"a1": "compress", "a2": "compress", "a3": "pinned", "a4": "compress", "a5": "verbatim"}
    correct = sum(1 for k, v in expected.items() if exercise_3_answers.get(k) == v)
    return correct, len(expected)


def score_exercise_4():
    correct = sum(1 for k, v in ISOLATION_CANDIDATES.items() if exercise_4_answers.get(k) == v)
    return correct, len(ISOLATION_CANDIDATES)


def score_exercise_5():
    expected_completeness = len(REQUIRED_FACTS & PRESENT_FACTS) / len(REQUIRED_FACTS)
    expected_noise = NOISE_TOKENS / TOTAL_TOKENS
    expected_pass = expected_completeness >= COMPLETENESS_THRESHOLD and expected_noise <= NOISE_CEILING
    correct = 0
    correct += int(abs(exercise_5_completeness - expected_completeness) < 1e-9)
    correct += int(abs(exercise_5_noise_ratio - expected_noise) < 1e-9)
    correct += int(exercise_5_gate_passes == expected_pass)
    return correct, 3


def main():
    exercises = [
        ("Exercise 1 -- match situations to recipes", score_exercise_1),
        ("Exercise 2 -- Context Budget Ledger arithmetic", score_exercise_2),
        ("Exercise 3 -- short-term memory classification", score_exercise_3),
        ("Exercise 4 -- isolation boundary judgment", score_exercise_4),
        ("Exercise 5 -- evaluation gate arithmetic", score_exercise_5),
    ]
    total_correct = 0
    total_possible = 0
    print("Chapter 13 Exercises -- Score Report (REFERENCE SOLUTION)")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_correct == total_possible:
        print("\nGate would PASS: this bundle is missing new_eta, though --")
        print("Exercise 5's own gate correctly reports incomplete (75% < 90%),")
        print("even though noise stays well under ceiling. Completeness alone")
        print("blocks this bundle, the same lesson Chapter 12's own worked math")
        print("teaches: fitting budget and being complete are independent axes.")


if __name__ == "__main__":
    main()
