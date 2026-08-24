"""
Chapter 12 Practice Bank: Evaluating Context Quality -- REFERENCE SOLUTION

See README.md for the eight scenarios. This file fills in every TODO
with a correct reference answer and scores a perfect total when run:

    python3 solution.py
"""

# Scenario 1 (judgment) -- Ossbrook Regional Grain Futures Clearinghouse.
scenario_1_answer = "no"

# Scenario 2 (production-gear) -- Colton Regional Home Inspection Licensing
# Board.
COLTON_REQUIRED_FACTS = {
    "current_inspection_status": {"found": True},
    "prior_variance_granted": {"found": True},
    "code_version_applied": {"found": False},
    "applicant_license_number": {"found": True},
    "appeal_deadline_date": {"found": True},
}

scenario_2_completeness = sum(1 for f in COLTON_REQUIRED_FACTS.values() if f["found"]) / len(COLTON_REQUIRED_FACTS)

# Scenario 3 (judgment) -- Bramfield Regional Wildfire Evacuation
# Coordination Center.
scenario_3_answer = "no"

# Scenario 4 (production-gear) -- Grendale Regional Court Interpreter
# Certification Board.
GRENDALE_NOISE_TOKENS = 180
GRENDALE_TOTAL_TOKENS = 1200
GRENDALE_THRESHOLD = 0.10

scenario_4_noise_ratio = GRENDALE_NOISE_TOKENS / GRENDALE_TOTAL_TOKENS
scenario_4_exceeds_threshold = scenario_4_noise_ratio > GRENDALE_THRESHOLD

# Scenario 5 (judgment) -- Delmoore Regional Pension Fund Audit Office.
scenario_5_answer = "no"

# Scenario 6 (production-gear) -- Sennwick Regional Livestock Export Health
# Certification Bureau.
SENNWICK_FRONT_END = 270
SENNWICK_BACK_START = 1530
SENNWICK_POSITIONS = {
    "current_health_certificate": 900,     # middle
    "export_destination_country": 100,     # front
    "quarantine_status_flag": 1650,        # back
}


def _bucket(position, front_end=SENNWICK_FRONT_END, back_start=SENNWICK_BACK_START):
    if position < front_end:
        return "front"
    if position > back_start:
        return "back"
    return "middle"


scenario_6_answers = {k: _bucket(v) for k, v in SENNWICK_POSITIONS.items()}

# Scenario 7 (production-gear) -- Bexmoor Regional Building Code Variance
# Board.
BEXMOOR_CANDIDATES = {
    "bundle_alpha": {"completeness": 1.0, "noise_ratio": 0.08, "critical_fact_bucket": "back"},
    "bundle_beta": {"completeness": 1.0, "noise_ratio": 0.15, "critical_fact_bucket": "front"},
    "bundle_gamma": {"completeness": 0.6, "noise_ratio": 0.02, "critical_fact_bucket": "front"},
}


def _gate_passes(candidate, threshold=0.10):
    return (
        candidate["completeness"] == 1.0
        and candidate["noise_ratio"] <= threshold
        and candidate["critical_fact_bucket"] != "middle"
    )


scenario_7_answers = {k: _gate_passes(v) for k, v in BEXMOOR_CANDIDATES.items()}

# Scenario 8 (judgment) -- Warrenfield Regional Small Business Disaster Loan
# Review Panel.
scenario_8_answer = "no"


# ===========================================================================
# Scoring harness -- identical to starter.py.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Ossbrook Regional Grain Futures Clearinghouse, judgment)",
                     scenario_1_answer.strip().lower() == "no", 1))

    expected_2 = sum(1 for f in COLTON_REQUIRED_FACTS.values() if f["found"]) / len(COLTON_REQUIRED_FACTS)
    results.append(("Scenario 2 (Colton Regional Home Inspection Licensing Board)",
                     abs(scenario_2_completeness - expected_2) < 1e-9, 1))

    results.append(("Scenario 3 (Bramfield Regional Wildfire Evacuation Coordination Center, judgment)",
                     scenario_3_answer.strip().lower() == "no", 1))

    expected_4_ratio = GRENDALE_NOISE_TOKENS / GRENDALE_TOTAL_TOKENS
    results.append((
        "Scenario 4 (Grendale Regional Court Interpreter Certification Board)",
        abs(scenario_4_noise_ratio - expected_4_ratio) < 1e-9
        and scenario_4_exceeds_threshold == (expected_4_ratio > GRENDALE_THRESHOLD),
        1,
    ))

    results.append(("Scenario 5 (Delmoore Regional Pension Fund Audit Office, judgment)",
                     scenario_5_answer.strip().lower() == "no", 1))

    expected_6 = {k: _bucket(v) for k, v in SENNWICK_POSITIONS.items()}
    correct_6 = sum(1 for k, v in expected_6.items() if scenario_6_answers.get(k) == v)
    results.append(("Scenario 6 (Sennwick Regional Livestock Export Health Certification Bureau)",
                     correct_6 == len(expected_6), 1))

    correct_7 = sum(1 for k, v in BEXMOOR_CANDIDATES.items() if scenario_7_answers.get(k) == _gate_passes(v))
    results.append(("Scenario 7 (Bexmoor Regional Building Code Variance Board)",
                     correct_7 == len(BEXMOOR_CANDIDATES), 1))

    results.append(("Scenario 8 (Warrenfield Regional Small Business Disaster Loan Review Panel, judgment)",
                     scenario_8_answer.strip().lower() == "no", 1))

    return results


def main():
    print("Chapter 12 Practice Bank -- Score Report (reference solution)")
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
