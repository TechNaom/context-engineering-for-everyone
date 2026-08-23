"""
Chapter 3 Project (L1 Guided): Design Wrayland Behavioral Health Group's
Recurring Counseling Check-In Short-Term Memory Policy

Wrayland Behavioral Health Group is a fictional outpatient counseling
provider. Its patient-messaging assistant, SupportLine, already has a
correctly allocated Line 3 (Conversation History) budget for its
"Recurring Counseling Check-In" request type -- Chapter 2's recipe
already ran; that number is a given below, not something to re-derive.
Your job is this chapter's own skill: design the real eviction/
compression POLICY that keeps a long-running counseling conversation's
history inside that budget without silently dropping a safety-relevant
fact, the exact gap this chapter's own hook (Emberlynn Transit
Cooperative's RouteLine) fell into.

THE SYSTEM
----------
SupportLine holds multi-week, recurring check-in conversations with
patients in outpatient counseling. Conversations run long -- 16+ turns
per multi-week check-in period -- and, like any real conversation, some
turns matter far more than others regardless of when they happened.

THE SPEC
--------
  Line 3 (Conversation History) budget:  7,500 tokens (fixed, given)
  Running summary size (fixed, given):   1,200 tokens

  16 real turns from a Recurring Counseling Check-In conversation,
  token count per turn, in order (oldest first) -- see TURN_TOKENS
  below.

  6 candidate facts disclosed across the conversation -- see FACTS
  below. Each has a category:
    - safety_critical / clinical_change -> MUST be pinned
    - small_talk                        -> must NOT be pinned
    - administrative                    -> your judgment call either way

YOUR TASK
---------
1. Fill in PINNED_FACT_IDS: the list of fact keys from FACTS you choose
   to pin. Every safety_critical and clinical_change fact MUST be in
   this list; no small_talk fact may be in this list; the two
   administrative facts are your own judgment call.
2. Fill in VERBATIM_WINDOW_TURNS: how many of the most recent turns
   (out of 16) stay raw, uncompressed. Choose a value such that
   (pinned-fact tokens) + (the fixed 1,200-token summary) + (the token
   sum of your last VERBATIM_WINDOW_TURNS turns) fits inside the
   7,500-token Line 3 budget.
3. Fill in POLICY_JUSTIFICATION: 2-4 real sentences defending your
   pin choices and verbatim window size together.
4. Fill in FOLLOW_UP_PLAN: 2-4 real sentences on what happens to any
   turn that falls outside your verbatim window and isn't independently
   pinned -- name what covers it and why that's an acceptable tradeoff
   for this request type.

Fill in every TODO, then run:

    python3 starter.py

to see a self-check. Like Chapter 2's project, most of this one IS
mechanically checkable against your own numbers (required/forbidden
pins, and whether your total package fits the given budget) -- only the
QUALITY of your justification and follow-up reasoning is open-ended.
Compare your full reasoning against solution.py, then self-grade
against RUBRIC.md.
"""

LINE3_BUDGET = 7_500
SUMMARY_TOKENS = 1_200

TURN_TOKENS = [380, 410, 450, 300, 520, 490, 460, 500, 470, 430, 510, 480, 460, 500, 490, 470]

FACTS = {
    "fact_1_safety_plan_disclosure": {"turn": 2, "category": "safety_critical", "tokens": 90},
    "fact_2_prefers_afternoon_sessions": {"turn": 3, "category": "administrative", "tokens": 30},
    "fact_3_medication_dosage_change": {"turn": 5, "category": "clinical_change", "tokens": 70},
    "fact_4_liked_therapists_book_recommendation": {"turn": 6, "category": "small_talk", "tokens": 25},
    "fact_5_disclosed_relapse_risk_trigger": {"turn": 9, "category": "safety_critical", "tokens": 85},
    "fact_6_insurance_plan_changed": {"turn": 11, "category": "administrative", "tokens": 40},
}

REQUIRED_PIN_CATEGORIES = {"safety_critical", "clinical_change"}
FORBIDDEN_PIN_CATEGORIES = {"small_talk"}

# TODO: list of fact keys from FACTS you choose to pin.
PINNED_FACT_IDS = [
    # TODO
]

# TODO: how many of the most recent 16 turns stay verbatim.
VERBATIM_WINDOW_TURNS = None  # TODO: int, 1-16

# TODO: 2-4 sentences defending your pin choices and window size.
POLICY_JUSTIFICATION = ""

# TODO: 2-4 sentences on what covers turns outside your verbatim window
# that aren't independently pinned, and why that's acceptable here.
FOLLOW_UP_PLAN = ""


# ===========================================================================
# Structural + internal-consistency self-check -- do not need to edit
# anything below this line. It verifies your PINNED_FACT_IDS choices are
# valid against the required/forbidden categories, and that your full
# package (pins + fixed summary + your verbatim window) actually fits
# the given 7,500-token budget -- it does not grade whether your
# administrative-fact judgment calls or your write-ups are wise, only
# that they're present and substantive. Compare against solution.py for
# that.
# ===========================================================================

def pinned_tokens():
    return sum(FACTS[f]["tokens"] for f in PINNED_FACT_IDS if f in FACTS)


def verbatim_tokens():
    if not isinstance(VERBATIM_WINDOW_TURNS, int) or not (1 <= VERBATIM_WINDOW_TURNS <= len(TURN_TOKENS)):
        return None
    return sum(TURN_TOKENS[-VERBATIM_WINDOW_TURNS:])


def total_tokens():
    v = verbatim_tokens()
    if v is None:
        return None
    return pinned_tokens() + SUMMARY_TOKENS + v


def check_pins():
    errors = []
    if not isinstance(PINNED_FACT_IDS, list) or not PINNED_FACT_IDS:
        errors.append("PINNED_FACT_IDS must be a non-empty list of fact keys from FACTS.")
        return errors

    unknown = [f for f in PINNED_FACT_IDS if f not in FACTS]
    if unknown:
        errors.append(f"PINNED_FACT_IDS contains unknown fact keys: {unknown}")

    required = {f for f, v in FACTS.items() if v["category"] in REQUIRED_PIN_CATEGORIES}
    missing_required = required - set(PINNED_FACT_IDS)
    if missing_required:
        errors.append(f"These safety-critical / clinical-change facts MUST be pinned: {sorted(missing_required)}")

    forbidden = {f for f, v in FACTS.items() if v["category"] in FORBIDDEN_PIN_CATEGORIES}
    wrongly_pinned = forbidden & set(PINNED_FACT_IDS)
    if wrongly_pinned:
        errors.append(f"These small_talk facts must NOT be pinned: {sorted(wrongly_pinned)}")

    return errors


def check_budget():
    errors = []
    if not isinstance(VERBATIM_WINDOW_TURNS, int) or not (1 <= VERBATIM_WINDOW_TURNS <= len(TURN_TOKENS)):
        errors.append(f"VERBATIM_WINDOW_TURNS must be an integer between 1 and {len(TURN_TOKENS)}.")
        return errors

    total = total_tokens()
    if total is None:
        errors.append("Could not compute total package tokens -- fix VERBATIM_WINDOW_TURNS first.")
        return errors

    if total > LINE3_BUDGET:
        errors.append(
            f"Package total ({total} tokens: {pinned_tokens()} pinned + {SUMMARY_TOKENS} summary + "
            f"{verbatim_tokens()} verbatim) exceeds the {LINE3_BUDGET}-token Line 3 budget by "
            f"{total - LINE3_BUDGET} tokens -- shrink VERBATIM_WINDOW_TURNS or reconsider your pins."
        )

    return errors


def check_writeups():
    errors = []
    if len(POLICY_JUSTIFICATION.strip()) < 40:
        errors.append("POLICY_JUSTIFICATION should be a real 2-4 sentence explanation (40+ characters)")
    if len(FOLLOW_UP_PLAN.strip()) < 40:
        errors.append("FOLLOW_UP_PLAN should be a real 2-4 sentence explanation (40+ characters)")
    return errors


def main():
    print("Chapter 3 Project -- Self-Check")
    print("=" * 60)
    pin_errors = check_pins()
    budget_errors = check_budget()
    writeup_errors = check_writeups()
    all_errors = pin_errors + budget_errors + writeup_errors

    total = total_tokens()
    print(f"Pinned facts: {PINNED_FACT_IDS} ({pinned_tokens()} tokens)")
    print(f"Verbatim window: {VERBATIM_WINDOW_TURNS} turns ({verbatim_tokens()} tokens)")
    print(f"Summary: {SUMMARY_TOKENS} tokens (fixed)")
    print(f"Package total: {total} / {LINE3_BUDGET} tokens")

    if not all_errors:
        print("PASS -- required facts are pinned, no forbidden facts are pinned, and the")
        print("full package fits inside the Line 3 budget.")
        print("Now compare your reasoning (not just structure) against solution.py,")
        print("and check your work against RUBRIC.md before considering this project done.")
    else:
        print(f"{len(all_errors)} issue(s) found:")
        for e in all_errors:
            print(f"  - {e}")
        print("\nFix the issues above and re-run this file.")


if __name__ == "__main__":
    main()
