PATTERN_SCORES = {
    r"ignore\s+(all\s+)?previous\s+instructions?": 40,
    r"forget\s+(everything|previous\s+instructions?)": 35,
    r"reveal\s+(the\s+)?system\s+(prompt|information)": 40,
    r"developer\s+mode": 25,
    r"jailbreak": 50,
    r"override\s+instructions?": 40,
    r"act\s+as": 15,
    r"do\s+anything\s+now": 45,
    r"bypass": 20
}



def calculate_score(matches):

    score = 0

    for match in matches:
        score += PATTERN_SCORES.get(match, 0)

    return score