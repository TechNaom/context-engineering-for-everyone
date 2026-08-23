"""
Chapter 4 Project (L2 Assisted): Design Brightmoor Elder Law Group's
CaseLine Short-Term AND Long-Term Memory

Brightmoor Elder Law Group is a fictional elder-law firm. Its
client-facing case assistant, CaseLine, supports guardianship and
estate cases that run for a year or more, across many separate
sessions with attorneys and family members -- weeks or months apart.
This is Module 2's closing lab, per the curriculum map's own project
ladder: "Design short-term and long-term memory for a provided
long-running assistant, partial scaffold." It sits exactly at the
boundary Chapters 3 and 4 each own: Chapter 3's short-term policy
governs THIS session's own conversation history (Line 3); Chapter 4's
long-term policy governs what was already persisted from PRIOR,
closed sessions, and what of that gets recalled back into Line 4 for
THIS turn.

THE SYSTEM
----------
CaseLine holds a currently open session with a client on an active
guardianship case. Line 3 (this session's Conversation History) and
Line 4 (Recalled Long-Term Memory) were both already allocated via
Chapter 2's recipe for this request type -- both numbers are given
below, not something to re-derive.

PART 1 -- THIS SESSION (short-term, Line 3, Chapter 3's own skill)
--------------------------------------------------------------------
  Line 3 budget (fixed, given):           3,800 tokens
  Running summary size (fixed, given):      900 tokens
  10 real turns from the currently open session, token count per turn,
  oldest first -- see CURRENT_SESSION_TURN_TOKENS below.
  5 candidate facts disclosed THIS session -- see CURRENT_SESSION_FACTS
  below. Category legal_critical -> MUST be pinned; small_talk -> must
  NOT be pinned; administrative -> your own judgment call.

PART 2 -- THE PERSISTENT STORE (long-term, Line 4, Chapter 4's own
skill, this project's new material)
--------------------------------------------------------------------
  Line 4 budget (fixed, given): 250 tokens
  6 fact records already written to the persistent store from PRIOR,
  now-closed sessions on this same case -- see PERSISTENT_STORE below.
  Each record has a category and a status (active / superseded /
  expired). A record with status != "active" must NEVER be retrieved,
  regardless of category -- it has already been overwritten or has
  gone stale. A record with category "small_talk" must NEVER be
  retrieved, regardless of status -- it should not have been written
  in the first place, and its presence here is a pre-existing data
  quality issue you must not compound by retrieving it anyway. Every
  ACTIVE legal_critical record MUST be retrieved.

YOUR TASK
---------
1. Fill in PINNED_FACT_IDS and VERBATIM_WINDOW_TURNS for THIS session
   (Chapter 3's skill, scoped only to CURRENT_SESSION_FACTS and
   CURRENT_SESSION_TURN_TOKENS) so the short-term package (pins +
   fixed summary + verbatim window) fits inside the 3,800-token Line 3
   budget.
2. Fill in RETRIEVED_LONG_TERM_FACT_IDS: which records from
   PERSISTENT_STORE should be recalled into Line 4 for this turn.
   Obey the required/forbidden rules above; the one active
   "administrative" record is your own judgment call. The total
   retrieved must fit inside the 250-token Line 4 budget.
3. Fill in SHORT_TERM_JUSTIFICATION and LONG_TERM_RETRIEVAL_JUSTIFICATION:
   2-4 real sentences each, defending your Part 1 and Part 2 choices
   separately -- in particular, explain why the superseded/expired
   records are correctly excluded from Line 4, not just that they are.

Fill in every TODO, then run:

    python3 starter.py

to see a self-check. Like Chapters 2 and 3's own projects, most of this
one IS mechanically checkable against your own numbers (required/
forbidden pins and retrieval, staleness exclusion, and whether both
packages fit their given budgets) -- only the QUALITY of your two
write-ups and the two judgment calls (the administrative pin, the
administrative retrieval) are open-ended. Compare your full reasoning
against solution.py, then self-grade against RUBRIC.md.
"""

LINE3_BUDGET = 3_800
LINE4_BUDGET = 250
SUMMARY_TOKENS = 900

CURRENT_SESSION_TURN_TOKENS = [300, 320, 280, 350, 310, 330, 290, 340, 360, 300]

CURRENT_SESSION_FACTS = {
    "fact_1_new_poa_document_signed": {"turn": 2, "category": "legal_critical", "tokens": 70},
    "fact_2_prefers_video_calls": {"turn": 3, "category": "administrative", "tokens": 25},
    "fact_3_capacity_concern_raised_by_family": {"turn": 5, "category": "legal_critical", "tokens": 90},
    "fact_4_asked_about_parking_at_office": {"turn": 6, "category": "small_talk", "tokens": 15},
    "fact_5_court_hearing_date_confirmed": {"turn": 8, "category": "legal_critical", "tokens": 60},
}
SHORT_TERM_REQUIRED_PIN_CATEGORIES = {"legal_critical"}
SHORT_TERM_FORBIDDEN_PIN_CATEGORIES = {"small_talk"}

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

# TODO (Part 1 -- short-term, this session): list of fact keys from
# CURRENT_SESSION_FACTS you choose to pin.
PINNED_FACT_IDS = [
    # TODO
]

# TODO (Part 1): how many of the most recent 10 current-session turns
# stay verbatim.
VERBATIM_WINDOW_TURNS = None  # TODO: int, 1-10

# TODO: 2-4 sentences defending your Part 1 pin choices and window size.
SHORT_TERM_JUSTIFICATION = ""

# TODO (Part 2 -- long-term, the persistent store): list of fact keys
# from PERSISTENT_STORE you choose to retrieve into THIS turn's Line 4.
RETRIEVED_LONG_TERM_FACT_IDS = [
    # TODO
]

# TODO: 2-4 sentences defending your Part 2 retrieval choices, including
# why the superseded/expired/small_talk records are correctly excluded.
LONG_TERM_RETRIEVAL_JUSTIFICATION = ""


# ===========================================================================
# Structural + internal-consistency self-check -- do not need to edit
# anything below this line. It verifies your PINNED_FACT_IDS and
# RETRIEVED_LONG_TERM_FACT_IDS choices are valid against the
# required/forbidden categories and staleness rules, and that both
# packages fit their given budgets -- it does not grade whether your
# two judgment calls or your write-ups are wise, only that they're
# present and substantive. Compare against solution.py for that.
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

    required = {
        f for f, v in PERSISTENT_STORE.items()
        if v["status"] == "active" and v["category"] in LONG_TERM_REQUIRED_RETRIEVAL_CATEGORIES
    }
    missing_required = required - set(RETRIEVED_LONG_TERM_FACT_IDS)
    if missing_required:
        errors.append(f"These active legal_critical records MUST be retrieved: {sorted(missing_required)}")

    forbidden_category = {
        f for f, v in PERSISTENT_STORE.items() if v["category"] in LONG_TERM_FORBIDDEN_RETRIEVAL_CATEGORIES
    }
    wrongly_retrieved_category = forbidden_category & set(RETRIEVED_LONG_TERM_FACT_IDS)
    if wrongly_retrieved_category:
        errors.append(f"These small_talk records must NEVER be retrieved: {sorted(wrongly_retrieved_category)}")

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
    print("Chapter 4 Project -- Self-Check")
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
        print("Now compare your reasoning (not just structure) against solution.py,")
        print("and check your work against RUBRIC.md before considering this project done.")
    else:
        print(f"\n{len(all_errors)} issue(s) found:")
        for e in all_errors:
            print(f"  - {e}")
        print("\nFix the issues above and re-run this file.")


if __name__ == "__main__":
    main()
