KEYWORDS = [
    "ignore",
    "forget",
    "reveal",
    "override",
    "bypass",
    "developer",
    "system",
    "secret",
    "hidden"
]


def heuristic_score(prompt):

    score = 0
    reasons = []

    prompt_lower = prompt.lower()

    # Keyword heuristic
    for word in KEYWORDS:
        if word in prompt_lower:
            score += 10
            reasons.append(f"Keyword detected: {word}")

    # Long prompt
    if len(prompt) > 500:
        score += 15
        reasons.append("Very long prompt")

    # Excessive uppercase
    uppercase = sum(1 for c in prompt if c.isupper())

    if uppercase > 30:
        score += 10
        reasons.append("Excessive uppercase characters")

    # Excessive special characters
    special = sum(
        1 for c in prompt
        if not c.isalnum() and not c.isspace()
    )

    if special > 20:
        score += 10
        reasons.append("Too many special characters")

    return score, reasons