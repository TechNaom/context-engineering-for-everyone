"""
Module 6 Assessment, Part 1: Context-Evaluation Exercise

Ternfield Regional Disability Benefits Review Office's ClaimLens system
(Chapter 12's own lesson scenario, a fresh case) is reviewing Case
TF-9102. The assembled 3,000-token bundle has three independent
problems at once: an incomplete required-fact set, a noise ratio over
threshold, and a critical fact buried in the middle bucket.

Fill in each `# TODO`, then run:

    python3 starter.py

to see a structural self-check report. Compare your full response
against solution.py, and self-grade against RUBRIC.md.
"""

BUNDLE_TOTAL_TOKENS = 3000
FRONT_BUCKET_END = 450     # first 15% of 3000
BACK_BUCKET_START = 2550   # last 15% of 3000
NOISE_THRESHOLD = 0.10

# Case TF-9102's own four required facts, with their own found status and
# (if found) position in the assembled 3,000-token bundle.
REQUIRED_FACTS = {
    "current_lifting_restriction": {"priority": "critical", "found": True, "position": 1600},
    "diagnosis_code": {"priority": "standard", "found": True, "position": 200},
    "referring_physician_name": {"priority": "standard", "found": True, "position": 2800},
    "updated_medication_list": {"priority": "standard", "found": False, "position": None},
}

# prior_case_notes source contains 330 tokens carried over from an
# unrelated applicant's own file by a stale join.
NOISE_TOKENS = 330


def completeness_score(required_facts):
    # TODO: return found / total as a float.
    return 0.0  # TODO


def noise_ratio(noise_tokens, total_tokens):
    # TODO: return noise_tokens / total_tokens as a float.
    return 0.0  # TODO


def position_bucket(position, front_end=FRONT_BUCKET_END, back_start=BACK_BUCKET_START):
    # TODO: return "front", "middle", "back", or "missing" (if position is None).
    return ""  # TODO


def context_quality_gate(completeness, noise_ratio_value, position_audit, required_facts, threshold=NOISE_THRESHOLD):
    # TODO: return True only if completeness == 1.0, noise_ratio_value <= threshold,
    # and no CRITICAL fact is bucketed "middle".
    return False  # TODO


# TODO: compute these four values using the functions above.
part1_completeness = 0.0  # TODO
part2_noise_ratio = 0.0  # TODO
part3_position_audit = {}  # TODO: dict of fact_name -> bucket string, for every required fact
part4_gate_decision = None  # TODO: True or False

# TODO (Part 5, open-ended): write a short justification naming ALL THREE
# problems this bundle has, citing the actual computed numbers -- not a
# generic "this bundle needs work."
part5_justification = ""  # TODO


# ===========================================================================
# Structural self-check -- do not need to edit anything below this line.
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
    print("Module 6 Assessment, Part 1 -- Structural Self-Check")
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
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
