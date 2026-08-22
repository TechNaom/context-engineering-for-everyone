"""
Chapter 1 Practice Bank: The Context Budget

Eight short, independent scenarios, each its own fictional system --
none of them Brackwater Home Internet/SignalDesk or Cobalt Home
Security/GuardLine again. Each scenario is a few sentences and one
judgment question. The point isn't depth on one system (that's what the
exercises did) -- it's speed and accuracy across many different systems,
the way a real context-engineering review actually feels.

Fill in every TODO, then run:

    python3 starter.py

to see your score.
"""

LEDGER_LINES = {
    "L1": "System Instructions",
    "L2": "Grounding Context",
    "L3": "Conversation History",
    "L4": "Recalled Long-Term Memory",
    "L5": "Working Space",
}

# ---------------------------------------------------------------------------
# Scenario 1 -- Windermere Legal Services: a client-intake assistant's system
# prompt has accumulated eleven paragraphs of disclaimers and jurisdiction-
# specific edge cases over a year of ad hoc edits, none ever removed, eating
# a fixed, growing share of every single request's budget. Which ledger
# line explains this gap?
# ---------------------------------------------------------------------------
scenario_1_answer = ""  # TODO: "L1".."L5"

# ---------------------------------------------------------------------------
# Scenario 2 -- Pinecrest Veterinary Group: a symptom-triage assistant keeps
# every article its retriever has ever surfaced in a session, including
# three articles about a condition the vet tech ruled out ten minutes ago,
# still competing for space in every later request. Which line explains
# this?
# ---------------------------------------------------------------------------
scenario_2_answer = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 3 -- Solmark Payments: a fraud-dispute assistant sends the full,
# unsummarized transcript of a dispute conversation on every turn; after 40
# turns the request exceeds the model's window and the earliest turns --
# where the customer first described the disputed charge -- are silently
# dropped. Which line explains this?
# ---------------------------------------------------------------------------
scenario_3_answer = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 4 -- Thistledown Air Cargo: a shipment-tracking assistant has no
# persistent memory layer at all; a customer's stated hazardous-materials
# handling requirement, given once in an earlier session, is never re-
# fetched in a later session and has to be re-explained from scratch every
# time. Which line explains this?
# ---------------------------------------------------------------------------
scenario_4_answer = ""  # TODO

# ---------------------------------------------------------------------------
# Scenario 5 (Judgment) -- Ravenhollow University Registrar: a team's fix
# for an unbounded-history problem is to keep sending the full transcript,
# but only during low-traffic overnight hours "when requests are smaller
# anyway." Does this actually solve the underlying budget problem, or does
# a real gap remain? Answer "yes" if it's an adequate fix, "no" if a real
# gap remains.
# ---------------------------------------------------------------------------
scenario_5_answer = ""  # TODO: "yes" or "no"

# ---------------------------------------------------------------------------
# Scenario 6 (Judgment) -- Copperfield Home Appliances: two real, unequal
# gaps, only one fixable before next week's launch: (a) no eviction policy
# on grounding context, so stale KB hits accumulate and crowd the budget
# over a long session, or (b) the system prompt uses British spelling in
# two places while the rest of the product uses American spelling. Which is
# the higher-priority fix for this chapter's ledger? Answer "a" or "b".
# ---------------------------------------------------------------------------
scenario_6_answer = ""  # TODO: "a" or "b"

# ---------------------------------------------------------------------------
# Scenario 7 (Production-gear) -- Marrowgate Public Library: a research-
# assistant team has budget for one investment. Which of four candidates --
# a bigger model, a re-ranking step that drops stale retrieved articles from
# the request, a faster database, or a prettier chat UI -- most directly
# builds the Grounding Context line's discipline? Answer with the option's
# letter: "a" (bigger model), "b" (re-ranking/eviction step), "c" (faster
# database), or "d" (UI redesign).
# ---------------------------------------------------------------------------
scenario_7_answer = ""  # TODO: "a", "b", "c", or "d"

# ---------------------------------------------------------------------------
# Scenario 8 (Production-gear) -- Fenwick Outdoor Adventures: a trip-
# planning assistant's team ships changes straight from a quick local test
# to production, sends the full transcript every turn with no summarization,
# and never re-fetches a customer's stated gear list from account records on
# later turns -- "the model just carries it in memory." Name BOTH ledger
# lines most directly missing (as a list of two IDs, e.g. ["L1", "L2"]).
# ---------------------------------------------------------------------------
scenario_8_answers = []  # TODO: list of two line IDs


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Windermere Legal Services)", scenario_1_answer == "L1", 1))
    results.append(("Scenario 2 (Pinecrest Veterinary Group)", scenario_2_answer == "L2", 1))
    results.append(("Scenario 3 (Solmark Payments)", scenario_3_answer == "L3", 1))
    results.append(("Scenario 4 (Thistledown Air Cargo)", scenario_4_answer == "L4", 1))
    results.append(("Scenario 5 (Ravenhollow University Registrar, judgment)", scenario_5_answer.strip().lower() == "no", 1))
    results.append(("Scenario 6 (Copperfield Home Appliances, judgment)", scenario_6_answer.strip().lower() == "a", 1))
    results.append(("Scenario 7 (Marrowgate Public Library)", scenario_7_answer.strip().lower() == "b", 1))

    s8_key = {"L3", "L4"}
    s8_given = set(scenario_8_answers)
    results.append(("Scenario 8 (Fenwick Outdoor Adventures)", s8_given == s8_key, 1))

    return results


def main():
    print("Chapter 1 Practice Bank -- Score Report")
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
        print("Perfect score -- every scenario correctly diagnosed.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
