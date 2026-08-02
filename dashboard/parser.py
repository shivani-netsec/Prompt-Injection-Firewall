import os

LOG_FILE = "logs/firewall.log"


def get_dashboard_stats():

    stats = {
        "total": 0,
        "allowed": 0,
        "sanitized": 0,
        "blocked": 0
    }

    if not os.path.exists(LOG_FILE):
        return stats

    with open(LOG_FILE, "r", encoding="utf-8") as file:

        content = file.read()

    stats["allowed"] = content.count("Decision: Allowed")
    stats["sanitized"] = content.count("Decision: Sanitized")
    stats["blocked"] = content.count("Decision: Blocked")

    stats["total"] = (
        stats["allowed"]
        + stats["sanitized"]
        + stats["blocked"]
    )

    return stats