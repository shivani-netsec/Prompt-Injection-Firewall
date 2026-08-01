def calculate_score(matches):

    score = 0

    for rule in matches:
        score += rule["score"]

    return score