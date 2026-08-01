from datetime import datetime
import uuid 

LOG_FILE = "logs/firewall.log"


def log_request(
    original_prompt,
    sanitized_prompt,
    risk_score,
    severity,
    decision,
    matched_patterns,
    heuristic_reasons,
    removed_phrases,
    processing_time
):
    event_id = f"PIF-{str(uuid.uuid4())[:8].upper()}"
    
    print("Logging request...")

    
    with open(LOG_FILE, "a", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")

        file.write(f"Event ID: {event_id}\n")

        file.write(f"Timestamp: {datetime.now()}\n")

        file.write(f"Processing Time: {processing_time} seconds\n")

        file.write(f"Original Prompt:\n{original_prompt}\n\n")

        file.write(f"Sanitized Prompt:\n{sanitized_prompt}\n\n")

        file.write(f"Risk Score: {risk_score}\n")

        file.write(f"Severity: {severity}\n")

        file.write(f"Decision: {decision}\n\n")

        file.write(f"Matched Patterns:\n")

        if matched_patterns:
            for rule in matched_patterns:
                file.write(f"- {rule['id']} | {rule['name']}\n")
        else:
            file.write("None\n")

        file.write("\nHeuristic Reasons:\n")

        if heuristic_reasons:
            for reason in heuristic_reasons:
                file.write(f"- {reason}\n")
        else:
            file.write("None\n")

        file.write("\nRemoved Phrases:\n")

        if removed_phrases:
            for phrase in removed_phrases:
                file.write(f"- {phrase}\n")
        else:
            file.write("None\n")

        file.write("\n")

        file.write("=" * 60)

        file.write("\n\n")