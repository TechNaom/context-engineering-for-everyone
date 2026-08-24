"""
Chapter 10 Practice Bank: Context Engineering for Multi-Agent Systems

Eight short, independent scenarios, each its own fictional multi-step or
multi-agent pipeline -- none of them Heronbrook Regional Grantmaking
Alliance/GrantPilot or Prescott County Emergency Housing Placement
Network/PlacementLine again. Each scenario is a few sentences and one
judgment or arithmetic question about this chapter's own new skill:
scoping a step's own context contract, budgeting each step as its own
ledger line, isolating context per unit of work, and deciding what a
sub-agent's own delegated payload should and shouldn't include -- not
tool-result curation within a single step (that's Chapter 9's job), and
not deciding when withholding context is the right design choice on
purpose (that's Chapter 11's job).

Fill in each `# TODO`, then run:

    python3 starter.py

to see a score report. Compare against solution.py, which scores a
perfect total.
"""

# Scenario 1 (judgment) -- Bramwell County Court Interpreter Scheduling
# Service: a three-step scheduling pipeline hands every step the full
# accumulated shift history of every case scheduled so far today,
# unscoped. Does every individual step reasoning correctly about
# whatever it's shown guarantee the pipeline produces the right
# schedule for the current case?
scenario_1_answer = None  # TODO: "yes" or "no"

# Scenario 2 (production-gear) -- Solmere Regional Disaster Shelter
# Intake Network: a shelter-assignment pipeline has processed 6 prior
# households this shift, each leaving 120 raw tokens in the
# orchestrator's own accumulated history. The current household's own
# curated inputs total 80 tokens. The Assignment Agent's own budget is
# 200 tokens. Compute the naive (unscoped) total and whether it
# overflows, and the scoped total and whether it fits.
SOLMERE_PRIOR_HOUSEHOLDS = 6
SOLMERE_RAW_TOKENS_PER_PRIOR = 120
SOLMERE_CURRENT_CURATED_TOKENS = 80
SOLMERE_ASSIGNMENT_BUDGET = 200

scenario_2_naive_tokens = 0  # TODO
scenario_2_naive_overflows = None  # TODO
scenario_2_scoped_tokens = 0  # TODO
scenario_2_scoped_fits = None  # TODO

# Scenario 3 (judgment) -- Anchorfield Regional Small Business Loan
# Consortium: an underwriting pipeline correctly scopes each step to the
# current applicant's own data, with no other applicant's data included.
# Does that scoping alone guarantee the working context resets between
# one applicant's review and the next?
scenario_3_answer = None  # TODO: "yes" or "no"

# Scenario 4 (production-gear) -- Hawkridge Regional Reforestation
# Grants Program: curate a Site Assessment Agent's own 5-field raw
# output down to the fields the Approval Agent's own contract actually
# needs: the site id and the soil viability score -- not the full survey
# notes, surveyor name, or visit date.
HAWKRIDGE_RAW_OUTPUT = {
    "site_id": "HR-114",
    "soil_viability_score": 82,
    "survey_notes": "Extensive notes on drainage and canopy density...",
    "surveyor_name": "J. Alvarez",
    "visit_date": "2026-05-02",
}

scenario_4_curated_fields = set()  # TODO

# Scenario 5 (judgment) -- Havermill County Meals-on-Wheels Route
# Optimization Service: a route-planning pipeline's Route Agent
# correctly receives only the current route's own delivery list. Does
# that, by itself, guarantee a completed route's own driver-assignment
# from earlier in the shift won't be reused for the current route?
scenario_5_answer = None  # TODO: "yes" or "no"

# Scenario 6 (production-gear) -- Ledgemont Regional Water Utility Leak
# Response Pipeline: for each candidate payload handed to the
# Dispatch Agent, is it correctly scoped (has a defined task AND
# includes no other work order's own data)?
LEDGEMONT_PAYLOADS = {
    "payload_x": {"task": "dispatch_repair_crew", "other_work_orders_included": False},
    "payload_y": {"task": "dispatch_repair_crew", "other_work_orders_included": True},
    "payload_z": {"task": None, "other_work_orders_included": False},
}

scenario_6_answers = {
    "payload_x": None,  # TODO
    "payload_y": None,  # TODO
    "payload_z": None,  # TODO
}

# Scenario 7 (production-gear) -- Tessington Regional Scholarship Review
# Board: a four-step pipeline, each step with its own ledger line.
# Confirm each step's own scoped tokens fit its own budget, and compute
# the pipeline-wide total scoped tokens and total budget.
TESSINGTON_STEP_BUDGETS = {"screening_agent": 150, "essay_review_agent": 300, "reference_check_agent": 200, "award_agent": 250}
TESSINGTON_STEP_SCOPED_TOKENS = {"screening_agent": 50, "essay_review_agent": 210, "reference_check_agent": 90, "award_agent": 140}

scenario_7_fits_per_step = {
    "screening_agent": None,  # TODO
    "essay_review_agent": None,  # TODO
    "reference_check_agent": None,  # TODO
    "award_agent": None,  # TODO
}
scenario_7_pipeline_total_scoped = 0  # TODO
scenario_7_pipeline_total_budget = 0  # TODO

# Scenario 8 (judgment) -- Cresswell Regional Building Permit Review
# Pipeline: a permit-review pipeline's final Approval Agent produces a
# resolved decision that mixes fields from two different permit
# applications reviewed back to back in the same session. Is this
# record ready to hand downstream to the applicant-facing notification
# system?
scenario_8_answer = None  # TODO: "yes" or "no"


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def _is_correctly_scoped(payload):
    return payload["task"] is not None and payload["other_work_orders_included"] is False


def score():
    results = []

    results.append(("Scenario 1 (Bramwell County Court Interpreter Scheduling Service, judgment)", (scenario_1_answer or "").strip().lower() == "no", 1))

    expected_2_naive = SOLMERE_PRIOR_HOUSEHOLDS * SOLMERE_RAW_TOKENS_PER_PRIOR + SOLMERE_CURRENT_CURATED_TOKENS
    results.append((
        "Scenario 2 (Solmere Regional Disaster Shelter Intake Network)",
        scenario_2_naive_tokens == expected_2_naive
        and scenario_2_naive_overflows == (expected_2_naive > SOLMERE_ASSIGNMENT_BUDGET)
        and scenario_2_scoped_tokens == SOLMERE_CURRENT_CURATED_TOKENS
        and scenario_2_scoped_fits == (SOLMERE_CURRENT_CURATED_TOKENS <= SOLMERE_ASSIGNMENT_BUDGET),
        1,
    ))

    results.append(("Scenario 3 (Anchorfield Regional Small Business Loan Consortium, judgment)", (scenario_3_answer or "").strip().lower() == "no", 1))

    expected_4 = {"site_id", "soil_viability_score"}
    results.append(("Scenario 4 (Hawkridge Regional Reforestation Grants Program)", scenario_4_curated_fields == expected_4, 1))

    results.append(("Scenario 5 (Havermill County Meals-on-Wheels Route Optimization Service, judgment)", (scenario_5_answer or "").strip().lower() == "no", 1))

    correct_6 = sum(1 for k, v in LEDGEMONT_PAYLOADS.items() if scenario_6_answers.get(k) == _is_correctly_scoped(v))
    results.append(("Scenario 6 (Ledgemont Regional Water Utility Leak Response Pipeline)", correct_6 == len(LEDGEMONT_PAYLOADS), 1))

    expected_fits_7 = {s: TESSINGTON_STEP_SCOPED_TOKENS[s] <= TESSINGTON_STEP_BUDGETS[s] for s in TESSINGTON_STEP_BUDGETS}
    results.append((
        "Scenario 7 (Tessington Regional Scholarship Review Board)",
        scenario_7_fits_per_step == expected_fits_7
        and scenario_7_pipeline_total_scoped == sum(TESSINGTON_STEP_SCOPED_TOKENS.values())
        and scenario_7_pipeline_total_budget == sum(TESSINGTON_STEP_BUDGETS.values()),
        1,
    ))

    results.append(("Scenario 8 (Cresswell Regional Building Permit Review Pipeline, judgment)", (scenario_8_answer or "").strip().lower() == "no", 1))

    return results


def main():
    print("Chapter 10 Practice Bank -- Score Report")
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
