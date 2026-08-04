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

def get_recent_incidents(limit=10):

    incidents = []

    if not os.path.exists(LOG_FILE):
        return incidents

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    logs = content.split("=" * 60)

    for log in reversed(logs):

        log = log.strip()

        if not log:
            continue

        incident = {
            "event_id": "",
            "severity": "",
            "decision": "",
            "processing_time": ""
        }

        for line in log.splitlines():

            if line.startswith("Event ID:"):
                incident["event_id"] = line.replace("Event ID:", "").strip()

            elif line.startswith("Severity:"):
                incident["severity"] = line.replace("Severity:", "").strip()

            elif line.startswith("Decision:"):
                incident["decision"] = line.replace("Decision:", "").strip()

            elif line.startswith("Processing Time:"):
                incident["processing_time"] = line.replace("Processing Time:", "").strip()

        incidents.append(incident)

        if len(incidents) >= limit:
            break

    return incidents