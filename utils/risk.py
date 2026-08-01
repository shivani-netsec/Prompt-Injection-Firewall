def classify_risk(score):
    if score >= 70:
        return "Critical", "Blocked"
    elif score >= 40:
        return "Medium", "Sanitized"
    else:
        return "Low", "Allowed"