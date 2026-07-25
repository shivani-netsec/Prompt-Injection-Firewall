SUSPICIOUS_PATTERNS =[
    "ignore previous instructions",
    "ignore all previous instructions",
    "forget previous instructions",
    "forget everything",
    "system prompt",
    "reveal system prompt",
    "developer mode",
    "jailbreak",
    "bypass",
    "act as",
    "do anything now",
    "dan mode",
    "override instructions"
]

def detect_patterns(prompt):
    prompt =prompt.lower()

    matches = []

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in prompt:
            matches.append(pattern)
    return matches
    