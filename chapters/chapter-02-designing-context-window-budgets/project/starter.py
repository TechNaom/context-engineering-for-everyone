"""
Chapter 2 Project (L1 Guided): Design Halveston Regional Health System's
Post-Discharge Follow-Up Budget

This project completes Module 1's second lab: instead of diagnosing an
existing system's gaps (Chapter 1's project), you DESIGN a real token
budget allocation for a brand-new request type before it ships. See
README.md and RUBRIC.md for full context and grading criteria.

THE SYSTEM
----------
Halveston Regional Health System is a fictional hospital network. Its
patient-messaging assistant, IntakeLine, already handles a short intake
request type. The team is now shipping a new request type:
"Post-Discharge Follow-Up" -- a recurring, multi-session conversation
that reviews a discharged patient's medications, comorbidities, and
recovery progress over several weeks, spanning 12-25 turns per session
across the follow-up period, with a moderate amount of retrieved
grounding content (discharge instructions, medication-interaction
lookups) and a genuinely heavy recalled-memory need (the patient's full
medication list, comorbidities, and notes from prior follow-up
sessions).

THE SPEC
--------
  Context window (this model):        48,000 tokens
  Reserved output (Line 5):            2,500 tokens (fixed, given)
  System instructions (Line 1):        1,200 tokens (fixed, given)

  A worst-case content audit of real Post-Discharge Follow-Up sessions
  found these actual token needs per line:
      Grounding Context (L2) worst case:        9,000 tokens
      Conversation History (L3) worst case:    16,000 tokens
      Recalled Long-Term Memory (L4) worst case: 12,000 tokens

YOUR TASK
---------
1. Fill in ALLOCATION with your own token allocation for L2, L3, and L4
   (integers). The three values MUST sum to exactly the remaining budget
   after Line 5 and Line 1 are subtracted from the window (compute this
   yourself -- it is not given directly). Choose a split you can defend
   for this request type's real shape; you are not required to reuse
   one of the lesson's four archetype profiles exactly, but
   PROFILE_JUSTIFICATION must explain your reasoning either way.
2. Fill in PROFILE_JUSTIFICATION: 2-4 real sentences defending your
   split against this request type's actual shape (a recurring,
   memory-heavy, moderately long conversation).
3. Fill in VALIDATION: for each of L2, L3, and L4, compare YOUR OWN
   allocation against the worst-case numbers above and mark each line
   "surplus" (your allocation covers the worst case) or "deficit" (it
   doesn't).
4. Fill in FOLLOW_UP_PLAN: 2-4 real sentences on what happens next for
   any line you marked "deficit" -- name a real technique (not "just
   allocate more," since the budget is fixed) and which later chapter
   in this course owns it.

Fill in every TODO, then run:

    python3 starter.py

to see a self-check. Unlike Chapter 1's project, most of this one IS
mechanically checkable against your own numbers (the sum constraint,
and whether your surplus/deficit calls are internally consistent) --
only the QUALITY of your profile split and follow-up reasoning is
open-ended. Compare your full reasoning against solution.py, then
self-grade against RUBRIC.md.
"""

CONTEXT_WINDOW_TOKENS = 48_000
RESERVED_OUTPUT_TOKENS = 2_500
SYSTEM_INSTRUCTIONS_TOKENS = 1_200

WORST_CASE_ACTUAL = {
    "L2": 9_000,
    "L3": 16_000,
    "L4": 12_000,
}

# TODO: your token allocation for L2, L3, L4. Must sum to exactly the
# remaining budget (context window minus reserved output minus system
# instructions).
ALLOCATION = {
    "L2": None,  # TODO: integer
    "L3": None,  # TODO: integer
    "L4": None,  # TODO: integer
}

# TODO: 2-4 sentences defending your split above.
PROFILE_JUSTIFICATION = ""

# TODO: for each line, "surplus" or "deficit", based on comparing YOUR
# ALLOCATION above against WORST_CASE_ACTUAL.
VALIDATION = {
    "L2": "",  # TODO
    "L3": "",  # TODO
    "L4": "",  # TODO
}

# TODO: 2-4 sentences on what happens next for any line marked "deficit"
# above (name a real technique and which later chapter owns it). If you
# have no deficits, explain briefly why your split still has real
# headroom, not just luck.
FOLLOW_UP_PLAN = ""


# ===========================================================================
# Structural + internal-consistency self-check -- do not need to edit
# anything below this line. Most of this check verifies your numbers are
# INTERNALLY CONSISTENT with each other (the sum constraint, and whether
# your own surplus/deficit calls match your own allocation) -- it does not
# grade whether your PROFILE_JUSTIFICATION or FOLLOW_UP_PLAN reasoning is
# wise, only that they exist and are substantive. Compare your full
# reasoning against solution.py for that.
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
    print("Chapter 2 Project -- Self-Check")
    print("=" * 60)
    print(f"Remaining budget (window - output - system): {remaining_budget()} tokens")

    alloc_errors = check_allocation()
    val_errors = check_validation()
    all_errors = alloc_errors + val_errors

    if not all_errors:
        print("PASS -- allocation is complete, sums correctly, and your surplus/deficit")
        print("calls are internally consistent with your own numbers.")
        print("Now compare your reasoning (not just structure) against solution.py,")
        print("and check your work against RUBRIC.md before considering this project done.")
    else:
        print(f"{len(all_errors)} issue(s) found:")
        for e in all_errors:
            print(f"  - {e}")
        print("\nFix the issues above and re-run this file.")


if __name__ == "__main__":
    main()
