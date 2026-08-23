"""
Chapter 3 Project (L1 Guided): Design Wrayland Behavioral Health Group's
Recurring Counseling Check-In Short-Term Memory Policy -- REFERENCE SOLUTION

See README.md for the full spec and task instructions. This is ONE
valid, complete policy -- not the only correct one, since the verbatim
window size and which "administrative" facts get pinned are
intentionally open design choices. Use it to check your reasoning's
completeness and rigor, not to match numbers exactly.
"""

# Line 3 (Conversation History) was already allocated via Chapter 2's
# recipe for this request type -- given here, not re-derived.
LINE3_BUDGET = 7_500

# A running summary of turns outside the verbatim window. Its real,
# measured token size for this conversation shape is a fixed given.
SUMMARY_TOKENS = 1_200

# Sixteen real turns from a Recurring Counseling Check-In conversation,
# token count per turn, in order (oldest first).
TURN_TOKENS = [380, 410, 450, 300, 520, 490, 460, 500, 470, 430, 510, 480, 460, 500, 490, 470]

# Candidate facts disclosed across the conversation. Category determines
# whether pinning is REQUIRED, FORBIDDEN, or a judgment call:
#   safety_critical / clinical_change -> must be pinned
#   small_talk                        -> must NOT be pinned
#   administrative                    -> your judgment call either way
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

# Chosen policy: pin only the required facts (skip both administrative
# facts) and use the maximum verbatim window that still fits budget.
PINNED_FACT_IDS = [
    "fact_1_safety_plan_disclosure",
    "fact_3_medication_dosage_change",
    "fact_5_disclosed_relapse_risk_trigger",
]

# Verbatim window: keep the 12 most recent turns raw (turns 5-16);
# turns 1-4 are covered only by the running summary, except for
# fact_1 (turn 2), which survives via pinning despite falling outside
# the verbatim window.
VERBATIM_WINDOW_TURNS = 12

POLICY_JUSTIFICATION = (
    "Only the two safety_critical facts and the one clinical_change fact "
    "are pinned -- both administrative facts (session-time preference, "
    "insurance plan) are recoverable from the case record elsewhere and "
    "aren't worth spending pinned-reserve tokens on. Pinning them anyway "
    "would just shrink the verbatim window for no real safety benefit. "
    "The verbatim window is set to the maximum size (12 of 16 turns) "
    "that still fits the 7,500-token budget alongside the fixed "
    "1,200-token summary and the 245 tokens of required pins, keeping "
    "recent context as rich as the budget honestly allows."
)

FOLLOW_UP_PLAN = (
    "Turns 1-4 (the oldest four) fall outside the 12-turn verbatim "
    "window and are represented only by the running summary, except for "
    "fact_1's safety plan disclosure at turn 2, which survives because "
    "it's explicitly pinned. This is an accepted tradeoff, not a gap: "
    "the summary's job (rendering older turns compactly rather than "
    "dropping them) is Chapter 5's subject in depth, and this policy "
    "already keeps the one safety-relevant fact from that period alive "
    "on its own, independent of the summary's fidelity."
)


# ===========================================================================
# Structural + internal-consistency self-check -- identical to starter.py.
# ===========================================================================

def pinned_tokens():
    return sum(FACTS[f]["tokens"] for f in PINNED_FACT_IDS)


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
    print("Chapter 3 Project -- Self-Check (reference solution)")
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
    else:
        print(f"{len(all_errors)} issue(s) found:")
        for e in all_errors:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
