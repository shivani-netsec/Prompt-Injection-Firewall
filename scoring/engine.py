PATTERN_SCORES = {
    "ignore previous instructions": 40,
    "ignore all previous instructions": 40,
    "forget previous instructions": 35,
    "forget everything": 30,
    "system prompt": 25,
    "reveal system prompt": 40,
    "developer mode": 25,
    "jailbreak": 50,
    "bypass": 20,
    "act as": 15,
    "do anything now": 45,
    "dan mode": 50,
    "override instructions": 40
}


def calculate_score(matches):

    score = 0

    for match in matches:
        score += PATTERN_SCORES.get(match, 0)

    return score