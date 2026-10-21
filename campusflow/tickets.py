"""Ticket creation and priority calculation."""


def calculate_priority(urgency, affected_users):
    """
    Return the priority label for a ticket based on the 4-rule system.

    Rules (checked IN ORDER — first match wins):
      1. high urgency AND affected_users >= 10 → "critical"
      2. high urgency OR  affected_users >= 10 → "high"
      3. medium urgency OR affected_users >= 3 → "medium"
      4. otherwise                              → "low"
    """
    # Rule 1: critical — high urgency AND >= 10 users
    if urgency == "high" and affected_users >= 10:
        return "critical"

    # Rule 2: high — high urgency OR >= 10 users
    if urgency == "high" or affected_users >= 10:
        return "high"

    # Rule 3: medium — medium urgency OR >= 3 users
    # TODO: fill in the condition below. It should be an `if` returning "medium"
    #       when (urgency is "medium") OR (affected_users >= 3).
    if urgency == "medium" or affected_users >= 3:
        return "medium"

    # Rule 4: fallback — everything else
    return "low"