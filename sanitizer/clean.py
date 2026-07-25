import re

DANGEROUS_PATTERNS = [

    r"ignore( all)? previous instructions",
    r"forget( all)? previous instructions",
    r"forget everything",
    r"reveal system prompt",
    r"system prompt",
    r"developer mode",
    r"jailbreak",
    r"override instructions",
    r"do anything now",
    r"dan mode"

]


def sanitize_prompt(prompt):

    cleaned = prompt

    removed = []

    for pattern in DANGEROUS_PATTERNS:

        if re.search(pattern, cleaned, re.IGNORECASE):

            removed.append(pattern)

            cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)

    cleaned = re.sub(r"\band\b", "", cleaned, flags=re.IGNORECASE)

    cleaned = re.sub(r"\s+", " ", cleaned)

    cleaned = cleaned.strip(" ,.")

    return cleaned, removed