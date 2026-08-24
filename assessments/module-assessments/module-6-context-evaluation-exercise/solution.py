"""
Module 6 Assessment, Part 1: Context-Evaluation Exercise -- REFERENCE SOLUTION

See README.md for the scenario. This file fills in every TODO with a
correct reference answer and passes the structural self-check when run:

    python3 solution.py
"""

BUNDLE_TOTAL_TOKENS = 3000
FRONT_BUCKET_END = 450     # first 15% of 3000
BACK_BUCKET_START = 2550   # last 15% of 3000
NOISE_THRESHOLD = 0.10

REQUIRED_FACTS = {
    "current_lifting_restriction": {"priority": "critical", "found": True, "position": 1600},
    "diagnosis_code": {"priority": "standard", "found": True, "position": 200},
    "referring_physician_name": {"priority": "standard", "found": True, "position": 2800},
    "updated_medication_list": {"priority": "standard", "found": False, "position": None},
}

NOISE_TOKENS = 330


def completeness_score(required_facts):
    found = sum(1 for f in required_facts.values() if f["found"])
    return found / len(required_facts)


def noise_ratio(noise_tokens, total_tokens):
    return noise_tokens / total_tokens


def position_bucket(position, front_end=FRONT_BUCKET_END, back_start=BACK_BUCKET_START):
    if position is None:
        return "missing"
    if position < front_end:
        return "front"
    if position > back_start:
        return "back"
    return "middle"


def context_quality_gate(completeness, noise_ratio_value, position_audit, required_facts, threshold=NOISE_THRESHOLD):
    critical_in_middle = any(
        position_audit[name] == "middle" and f["priority"] == "critical"
        for name, f in required_facts.items()
    )
    return completeness == 1.0 and noise_ratio_value <= threshold and not critical_in_middle


part1_completeness = completeness_score(REQUIRED_FACTS)
part2_noise_ratio = noise_ratio(NOISE_TOKENS, BUNDLE_TOTAL_TOKENS)
part3_position_audit = {name: position_bucket(f["position"]) for name, f in REQUIRED_FACTS.items()}
part4_gate_decision = context_quality_gate(part1_completeness, part2_noise_ratio, part3_position_audit, REQUIRED_FACTS)

part5_justification = (
    "This bundle fails the context quality gate on all three independent axes at "
    "once, not just one: completeness is 0.75 (3/4), missing "
    "updated_medication_list entirely; the noise ratio is 0.11 (330/3000 tokens), "
    "over the 0.10 threshold, from an unrelated applicant's own notes pulled in by "
    "a stale join; and current_lifting_restriction, the one CRITICAL required fact, "
    "sits at position 1600 -- inside the middle bucket (between the 450-token front "
    "cutoff and the 2550-token back cutoff) -- meaning it is both technically present "
    "and at real risk of being under-weighted the way Chapter 6's own Lost-in-the-"
    "Middle findings describe. Fixing only one of the three (for example, adding "
    "the missing medication list) would still leave this bundle failing the gate on "
    "the other two."
)


# ===========================================================================
# Structural self-check -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def _expected():
    completeness = sum(1 for f in REQUIRED_FACTS.values() if f["found"]) / len(REQUIRED_FACTS)
    noise = NOISE_TOKENS / BUNDLE_TOTAL_TOKENS
    audit = {}
    for name, f in REQUIRED_FACTS.items():
        pos = f["position"]
        if pos is None:
            audit[name] = "missing"
        elif pos < FRONT_BUCKET_END:
            audit[name] = "front"
        elif pos > BACK_BUCKET_START:
            audit[name] = "back"
        else:
            audit[name] = "middle"
    critical_in_middle = any(
        audit[name] == "middle" and f["priority"] == "critical"
        for name, f in REQUIRED_FACTS.items()
    )
    gate = completeness == 1.0 and noise <= NOISE_THRESHOLD and not critical_in_middle
    return completeness, noise, audit, gate


def self_check():
    exp_completeness, exp_noise, exp_audit, exp_gate = _expected()
    results = []
    results.append(("Part 1 -- completeness score", abs(part1_completeness - exp_completeness) < 1e-9))
    results.append(("Part 2 -- noise ratio", abs(part2_noise_ratio - exp_noise) < 1e-9))
    results.append(("Part 3 -- positional audit", part3_position_audit == exp_audit))
    results.append(("Part 4 -- combined gate decision", part4_gate_decision == exp_gate))
    justification_ok = (
        isinstance(part5_justification, str)
        and len(part5_justification.strip()) >= 40
        and part5_justification.strip().lower() not in ("", "todo", "n/a")
    )
    results.append(("Part 5 -- justification present and descriptive", justification_ok))
    return results


def main():
    print("Module 6 Assessment, Part 1 -- Structural Self-Check (REFERENCE SOLUTION)")
    print("=" * 60)
    results = self_check()
    passed = 0
    for label, ok in results:
        print(f"{label}: {'PASS' if ok else 'FAIL'}")
        passed += int(ok)
    print("=" * 60)
    print(f"TOTAL: {passed}/{len(results)}")
    if passed == len(results):
        print("Structural self-check passed. Now self-grade against RUBRIC.md.")


if __name__ == "__main__":
    main()
