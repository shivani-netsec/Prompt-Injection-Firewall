import re

RULES = [

    {
        "id": "PIF-001",
        "name": "Instruction Override",
        "pattern": r"ignore\s+(all\s+)?previous\s+instructions?",
        "severity": "Critical",
        "score": 40
    },

    {
        "id": "PIF-002",
        "name": "System Prompt Disclosure",
        "pattern": r"reveal\s+(the\s+)?system\s+(prompt|information)",
        "severity": "Critical",
        "score": 40
    },

    {
        "id": "PIF-003",
        "name": "Forget Previous Instructions",
        "pattern": r"forget\s+(everything|previous\s+instructions?)",
        "severity": "High",
        "score": 35
    },

    {
        "id": "PIF-004",
        "name": "Developer Mode",
        "pattern": r"developer\s+mode",
        "severity": "Medium",
        "score": 25
    },

    {
        "id": "PIF-005",
        "name": "Jailbreak Attempt",
        "pattern": r"jailbreak",
        "severity": "Critical",
        "score": 50
    },

    {
        "id": "PIF-006",
        "name": "Instruction Bypass",
        "pattern": r"override\s+instructions?",
        "severity": "High",
        "score": 40
    },

    {
        "id": "PIF-007",
        "name": "Role Manipulation",
        "pattern": r"act\s+as",
        "severity": "Medium",
        "score": 15
    },

    {
        "id": "PIF-008",
        "name": "DAN Attack",
        "pattern": r"do\s+anything\s+now",
        "severity": "Critical",
        "score": 45
    },

    {
        "id": "PIF-009",
        "name": "Security Bypass",
        "pattern": r"bypass",
        "severity": "Medium",
        "score": 20
    }

]


def detect_patterns(prompt):

    prompt = prompt.lower()

    matches = []

    for rule in RULES:

        if re.search(rule["pattern"], prompt):
            matches.append(rule)

    return matches