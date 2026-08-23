"""
Chapter 4 Project (L2 Assisted): Design Brightmoor Elder Law Group's
CaseLine Short-Term AND Long-Term Memory -- REFERENCE SOLUTION

See README.md for the full spec and task instructions. This is ONE
valid, complete design -- not the only correct one, since the
administrative pin/retrieval calls and both write-ups are intentionally
open design choices. Use it to check your reasoning's completeness and
rigor, not to match numbers exactly.
"""

# Line 3 (this session's Conversation History) and Line 4 (Recalled
# Long-Term Memory) were already allocated via Chapter 2's recipe for
# this request type -- given here, not re-derived. This project's own
# job is the memory POLICY layered on top of both, at the exact
# boundary Chapter 3 (short-term, within one session) and Chapter 4
# (long-term, across sessions) each own.
LINE3_BUDGET = 3_800
LINE4_BUDGET = 250

# A fixed, real running-summary size for this session's own short-term
# policy (Chapter 3's mechanic, reused as a given here, not re-derived).
SUMMARY_TOKENS = 900

# THIS SESSION -- the case is currently open; these are the current,
# still-in-progress session's own turns, oldest first.
CURRENT_SESSION_TURN_TOKENS = [300, 320, 280, 350, 310, 330, 290, 340, 360, 300]

# Candidate facts disclosed THIS session -- Chapter 3's own short-term
# pin/no-pin call, scoped to Line 3 only.
CURRENT_SESSION_FACTS = {
    "fact_1_new_poa_document_signed": {"turn": 2, "category": "legal_critical", "tokens": 70},
    "fact_2_prefers_video_calls": {"turn": 3, "category": "administrative", "tokens": 25},
    "fact_3_capacity_concern_raised_by_family": {"turn": 5, "category": "legal_critical", "tokens": 90},
    "fact_4_asked_about_parking_at_office": {"turn": 6, "category": "small_talk", "tokens": 15},
    "fact_5_court_hearing_date_confirmed": {"turn": 8, "category": "legal_critical", "tokens": 60},
}
SHORT_TERM_REQUIRED_PIN_CATEGORIES = {"legal_critical"}
SHORT_TERM_FORBIDDEN_PIN_CATEGORIES = {"small_talk"}

# THE PERSISTENT STORE -- facts already written from PRIOR, now-closed
# sessions on this same case, months apart. This chapter's own job: not
# whether these were captured (they already are), but which of them are
# still eligible to be retrieved back into THIS turn's Line 4.
PERSISTENT_STORE = {
    "lt_fact_1_original_poa_signed_2023": {"category": "legal_critical", "status": "superseded", "tokens": 70},
    "lt_fact_2_prior_capacity_eval_clean_2023": {"category": "legal_critical", "status": "superseded", "tokens": 85},
    "lt_fact_3_standing_family_contact_preference": {"category": "administrative", "status": "active", "tokens": 40},
    "lt_fact_4_prior_hearing_date_rescheduled": {"category": "legal_critical", "status": "expired", "tokens": 55},
    "lt_fact_5_client_language_preference_spanish": {"category": "legal_critical", "status": "active", "tokens": 45},
    "lt_fact_6_old_small_talk_note_favorite_tea": {"category": "small_talk", "status": "active", "tokens": 20},
}
LONG_TERM_REQUIRED_RETRIEVAL_CATEGORIES = {"legal_critical"}  # required WHEN status == active
LONG_TERM_FORBIDDEN_RETRIEVAL_CATEGORIES = {"small_talk"}  # forbidden regardless of status

# ---------------------------------------------------------------------------
# YOUR DESIGN
# ---------------------------------------------------------------------------

# Short-term (Line 3): pin every legal_critical fact from THIS session;
# skip the one administrative fact (recoverable from the case file, not
# worth the reserve); never pin the small_talk fact.
PINNED_FACT_IDS = [
    "fact_1_new_poa_document_signed",
    "fact_3_capacity_concern_raised_by_family",
    "fact_5_court_hearing_date_confirmed",
]

# Verbatim window: the maximum number of the 10 current-session turns
# (most recent first) that still fits Line 3's budget alongside the
# pins and the fixed summary.
VERBATIM_WINDOW_TURNS = 7

SHORT_TERM_JUSTIFICATION = (
    "All three legal_critical facts from this session (the new POA, the "
    "capacity concern, the confirmed hearing date) are pinned -- each "
    "would change how CaseLine should respond even many turns later, and "
    "none can be safely left to recency. The one administrative fact "
    "(video-call preference) is left unpinned: it is recoverable from the "
    "case record and not worth spending pinned-reserve tokens on. The "
    "small_talk fact (parking question) is never pinned. The verbatim "
    "window is set to the maximum size (7 of 10 turns) that still fits "
    "inside the 3,800-token Line 3 budget alongside the pins and the "
    "fixed 900-token summary."
)

# Long-term (Line 4): retrieve every ACTIVE legal_critical fact
# (required); retrieve the one active administrative fact too, since it
# materially affects how this session should be handled (judgment call);
# never retrieve superseded/expired records or the small_talk record,
# regardless of its status.
RETRIEVED_LONG_TERM_FACT_IDS = [
    "lt_fact_5_client_language_preference_spanish",
    "lt_fact_3_standing_family_contact_preference",
]

LONG_TERM_RETRIEVAL_JUSTIFICATION = (
    "lt_fact_5 (active, legal_critical -- the client's language "
    "preference) is required: it changes how every session with this "
    "client should be conducted, not just the session it was disclosed "
    "in. lt_fact_3 (active, administrative -- standing family contact "
    "preference) is also retrieved by judgment, since it materially "
    "affects who CaseLine should loop in this session. The two "
    "superseded facts (the original 2023 POA and the original clean "
    "capacity evaluation) are excluded on purpose -- both were "
    "overwritten by this session's own new facts, and retrieving them "
    "would contradict what the client just said. The expired hearing-"
    "date record is excluded because it no longer describes anything "
    "current. The small_talk record about favorite tea is excluded "
    "regardless of its active status, because small_talk was never an "
    "eligible write category in the first place -- its presence in the "
    "store is a pre-existing data quality issue, not a reason to "
    "retrieve it now."
)


# ===========================================================================
# Structural + internal-consistency self-check -- identical to starter.py.
# ===========================================================================

def short_term_pinned_tokens():
    return sum(CURRENT_SESSION_FACTS[f]["tokens"] for f in PINNED_FACT_IDS if f in CURRENT_SESSION_FACTS)


def short_term_verbatim_tokens():
    if not isinstance(VERBATIM_WINDOW_TURNS, int) or not (1 <= VERBATIM_WINDOW_TURNS <= len(CURRENT_SESSION_TURN_TOKENS)):
        return None
    return sum(CURRENT_SESSION_TURN_TOKENS[-VERBATIM_WINDOW_TURNS:])


def short_term_total_tokens():
    v = short_term_verbatim_tokens()
    if v is None:
        return None
    return short_term_pinned_tokens() + SUMMARY_TOKENS + v


def check_short_term_pins():
    errors = []
    if not isinstance(PINNED_FACT_IDS, list) or not PINNED_FACT_IDS:
        errors.append("PINNED_FACT_IDS must be a non-empty list of fact keys from CURRENT_SESSION_FACTS.")
        return errors

    unknown = [f for f in PINNED_FACT_IDS if f not in CURRENT_SESSION_FACTS]
    if unknown:
        errors.append(f"PINNED_FACT_IDS contains unknown fact keys: {unknown}")

    required = {f for f, v in CURRENT_SESSION_FACTS.items() if v["category"] in SHORT_TERM_REQUIRED_PIN_CATEGORIES}
    missing_required = required - set(PINNED_FACT_IDS)
    if missing_required:
        errors.append(f"These legal_critical facts MUST be pinned this session: {sorted(missing_required)}")

    forbidden = {f for f, v in CURRENT_SESSION_FACTS.items() if v["category"] in SHORT_TERM_FORBIDDEN_PIN_CATEGORIES}
    wrongly_pinned = forbidden & set(PINNED_FACT_IDS)
    if wrongly_pinned:
        errors.append(f"These small_talk facts must NOT be pinned: {sorted(wrongly_pinned)}")

    return errors


def check_short_term_budget():
    errors = []
    if not isinstance(VERBATIM_WINDOW_TURNS, int) or not (1 <= VERBATIM_WINDOW_TURNS <= len(CURRENT_SESSION_TURN_TOKENS)):
        errors.append(f"VERBATIM_WINDOW_TURNS must be an integer between 1 and {len(CURRENT_SESSION_TURN_TOKENS)}.")
        return errors

    total = short_term_total_tokens()
    if total is None:
        errors.append("Could not compute short-term package tokens -- fix VERBATIM_WINDOW_TURNS first.")
        return errors

    if total > LINE3_BUDGET:
        errors.append(
            f"Short-term package total ({total} tokens) exceeds the {LINE3_BUDGET}-token Line 3 budget "
            f"by {total - LINE3_BUDGET} tokens -- shrink VERBATIM_WINDOW_TURNS or reconsider your pins."
        )

    return errors


def long_term_retrieved_tokens():
    return sum(PERSISTENT_STORE[f]["tokens"] for f in RETRIEVED_LONG_TERM_FACT_IDS if f in PERSISTENT_STORE)


def check_long_term_retrieval():
    errors = []
    if not isinstance(RETRIEVED_LONG_TERM_FACT_IDS, list):
        errors.append("RETRIEVED_LONG_TERM_FACT_IDS must be a list of fact keys from PERSISTENT_STORE.")
        return errors

    unknown = [f for f in RETRIEVED_LONG_TERM_FACT_IDS if f not in PERSISTENT_STORE]
    if unknown:
        errors.append(f"RETRIEVED_LONG_TERM_FACT_IDS contains unknown fact keys: {unknown}")

    # Required: every ACTIVE legal_critical record must be retrieved.
    required = {
        f for f, v in PERSISTENT_STORE.items()
        if v["status"] == "active" and v["category"] in LONG_TERM_REQUIRED_RETRIEVAL_CATEGORIES
    }
    missing_required = required - set(RETRIEVED_LONG_TERM_FACT_IDS)
    if missing_required:
        errors.append(f"These active legal_critical records MUST be retrieved: {sorted(missing_required)}")

    # Forbidden regardless of status: any small_talk record.
    forbidden_category = {
        f for f, v in PERSISTENT_STORE.items() if v["category"] in LONG_TERM_FORBIDDEN_RETRIEVAL_CATEGORIES
    }
    wrongly_retrieved_category = forbidden_category & set(RETRIEVED_LONG_TERM_FACT_IDS)
    if wrongly_retrieved_category:
        errors.append(f"These small_talk records must NEVER be retrieved: {sorted(wrongly_retrieved_category)}")

    # Forbidden regardless of category: any non-active (superseded/expired) record.
    non_active = {f for f, v in PERSISTENT_STORE.items() if v["status"] != "active"}
    wrongly_retrieved_stale = non_active & set(RETRIEVED_LONG_TERM_FACT_IDS)
    if wrongly_retrieved_stale:
        errors.append(f"These superseded/expired records must NEVER be retrieved: {sorted(wrongly_retrieved_stale)}")

    return errors


def check_long_term_budget():
    errors = []
    total = long_term_retrieved_tokens()
    if total > LINE4_BUDGET:
        errors.append(
            f"Retrieved long-term package total ({total} tokens) exceeds the {LINE4_BUDGET}-token "
            f"Line 4 budget by {total - LINE4_BUDGET} tokens -- reconsider your retrieval choices."
        )
    return errors


def check_writeups():
    errors = []
    if len(SHORT_TERM_JUSTIFICATION.strip()) < 40:
        errors.append("SHORT_TERM_JUSTIFICATION should be a real 2-4 sentence explanation (40+ characters)")
    if len(LONG_TERM_RETRIEVAL_JUSTIFICATION.strip()) < 40:
        errors.append("LONG_TERM_RETRIEVAL_JUSTIFICATION should be a real 2-4 sentence explanation (40+ characters)")
    return errors


def main():
    print("Chapter 4 Project -- Self-Check (reference solution)")
    print("=" * 60)
    pin_errors = check_short_term_pins()
    st_budget_errors = check_short_term_budget()
    retrieval_errors = check_long_term_retrieval()
    lt_budget_errors = check_long_term_budget()
    writeup_errors = check_writeups()
    all_errors = pin_errors + st_budget_errors + retrieval_errors + lt_budget_errors + writeup_errors

    st_total = short_term_total_tokens()
    lt_total = long_term_retrieved_tokens()
    print("-- Short-term (this session, Line 3) --")
    print(f"Pinned facts: {PINNED_FACT_IDS} ({short_term_pinned_tokens()} tokens)")
    print(f"Verbatim window: {VERBATIM_WINDOW_TURNS} turns ({short_term_verbatim_tokens()} tokens)")
    print(f"Summary: {SUMMARY_TOKENS} tokens (fixed)")
    print(f"Line 3 package total: {st_total} / {LINE3_BUDGET} tokens")
    print("-- Long-term (recalled into this turn, Line 4) --")
    print(f"Retrieved facts: {RETRIEVED_LONG_TERM_FACT_IDS} ({lt_total} tokens)")
    print(f"Line 4 package total: {lt_total} / {LINE4_BUDGET} tokens")

    if not all_errors:
        print("\nPASS -- short-term pins and budget are correct, long-term retrieval obeys")
        print("required/forbidden categories and staleness rules, and both packages fit")
        print("their respective budgets.")
    else:
        print(f"\n{len(all_errors)} issue(s) found:")
        for e in all_errors:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
