import re


SUSPICIOUS_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions?",
    r"forget\s+(everything|previous\s+instructions?)",
    r"reveal\s+(the\s+)?system\s+(prompt|information)",
    r"developer\s+mode",
    r"jailbreak",
    r"override\s+instructions?",
    r"act\s+as",
    r"do\s+anything\s+now",
    r"bypass"
]

def detect_patterns(prompt):
    prompt =prompt.lower()

    matches = []

    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, prompt):
            matches.append(pattern)
    return matches
    