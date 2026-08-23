"""
Chapter 2 Project (L1 Guided): Design Halveston Regional Health System's
Post-Discharge Follow-Up Budget -- REFERENCE SOLUTION

See starter.py for the full spec and task instructions. This is ONE
valid, complete allocation -- not the only correct split, since the
profile choice is intentionally open-ended. Use it to check your
reasoning's completeness and rigor, not to match numbers exactly.
"""

CONTEXT_WINDOW_TOKENS = 48_000
RESERVED_OUTPUT_TOKENS = 2_500
SYSTEM_INSTRUCTIONS_TOKENS = 1_200

WORST_CASE_ACTUAL = {
    "L2": 9_000,
    "L3": 16_000,
    "L4": 12_000,
}

# Remaining budget: 48,000 - 2,500 - 1,200 = 44,300
# Chosen split: 25% grounding / 35% history / 40% recalled memory --
# heavier on memory than the lesson's own "long_recurring" archetype
# (35/40/25) because this request type's recalled-memory need (full
# medication list, comorbidities, prior follow-up notes) is unusually
# large even for a recurring conversation type, and grounding here is
# comparatively light (discharge instructions + interaction lookups,
# not a large document).
ALLOCATION = {
    "L2": round(44_300 * 0.25),  # 11,075
    "L3": round(44_300 * 0.35),  # 15,505
    "L4": round(44_300 * 0.40),  # 17,720
}

PROFILE_JUSTIFICATION = (
    "Post-Discharge Follow-Up is memory-dominant, not history-dominant or "
    "grounding-dominant: the recalled record (full medication list, "
    "comorbidities, notes from prior follow-up sessions) is what actually "
    "keeps a multi-week follow-up safe, so Line 4 gets the largest single "
    "share at 40%, well above the lesson's long_recurring archetype's 25%. "
    "Line 3 still gets a real 35% because individual sessions run 12-25 "
    "turns, and Line 2 gets the smallest share at 25% because grounding "
    "here is a moderate lookup, not a dominant document."
)

# For each line: allocated vs. worst-case actual.
#   L2: 11,075 > 9,000  -> surplus
#   L3: 15,505 < 16,000 -> deficit (505 tokens short)
#   L4: 17,720 > 12,000 -> surplus
VALIDATION = {
    "L2": "surplus",
    "L3": "deficit",
    "L4": "surplus",
}

FOLLOW_UP_PLAN = (
    "Line 3 (Conversation History) is 505 tokens short of the worst-case "
    "need even after a deliberate, memory-heavy allocation -- this is a "
    "real, honest deficit, not a sign the allocation math was done wrong. "
    "The fix is Chapter 3's own subject: a real short-term-memory "
    "compression policy (summarize turns from earlier follow-up sessions "
    "into a compact running note) so the longest 25-turn sessions fit "
    "inside 15,505 tokens without a blind end-of-window truncation."
)


# ===========================================================================
# Structural + internal-consistency self-check -- identical to starter.py.
# ===========================================================================

def remaining_budget():
    return CONTEXT_WINDOW_TOKENS - RESERVED_OUTPUT_TOKENS - SYSTEM_INSTRUCTIONS_TOKENS


def check_allocation():
    errors = []
    expected_keys = {"L2", "L3", "L4"}
    if set(ALLOCATION.keys()) != expected_keys:
        errors.append(f"ALLOCATION must have exactly these keys: {sorted(expected_keys)}")
        return errors

    for line, tokens in ALLOCATION.items():
        if not isinstance(tokens, int) or tokens <= 0:
            errors.append(f"ALLOCATION[{line!r}] must be a positive integer, got {tokens!r}")

    if all(isinstance(v, int) for v in ALLOCATION.values()):
        total = sum(ALLOCATION.values())
        expected_total = remaining_budget()
        if total != expected_total:
            errors.append(
                f"ALLOCATION values must sum to exactly {expected_total} "
                f"(the real remaining budget after Line 5 and Line 1), got {total}"
            )
        for line, tokens in ALLOCATION.items():
            share = tokens / expected_total if expected_total else 0
            if not (0.05 <= share <= 0.80):
                errors.append(
                    f"ALLOCATION[{line!r}] is {share:.0%} of the remaining budget -- "
                    f"outside a plausible 5%-80% range for any single line; double-check it."
                )

    if len(PROFILE_JUSTIFICATION.strip()) < 40:
        errors.append("PROFILE_JUSTIFICATION should be a real 2-4 sentence explanation (40+ characters)")

    return errors


def check_validation():
    errors = []
    if not all(isinstance(v, int) for v in ALLOCATION.values()):
        errors.append("Cannot check VALIDATION until ALLOCATION is fully filled in with integers.")
        return errors

    for line in ("L2", "L3", "L4"):
        allocated = ALLOCATION[line]
        actual = WORST_CASE_ACTUAL[line]
        expected = "surplus" if allocated > actual else "deficit"
        given = VALIDATION.get(line, "").strip().lower()
        if given != expected:
            errors.append(
                f"VALIDATION[{line!r}] should be {expected!r} given your own ALLOCATION[{line!r}]="
                f"{allocated} vs. worst-case need {actual}, got {given!r}"
            )

    if len(FOLLOW_UP_PLAN.strip()) < 40:
        errors.append("FOLLOW_UP_PLAN should be a real 2-4 sentence explanation (40+ characters)")

    return errors


def main():
    print("Chapter 2 Project -- Self-Check (reference solution)")
    print("=" * 60)
    print(f"Remaining budget (window - output - system): {remaining_budget()} tokens")
    print(f"ALLOCATION: {ALLOCATION} (sum={sum(ALLOCATION.values())})")

    alloc_errors = check_allocation()
    val_errors = check_validation()
    all_errors = alloc_errors + val_errors

    if not all_errors:
        print("PASS -- allocation is complete, sums correctly, and surplus/deficit calls")
        print("are internally consistent.")
    else:
        print(f"{len(all_errors)} issue(s) found:")
        for e in all_errors:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
