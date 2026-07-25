from fastapi import FastAPI
from proxy import send_to_llm
from pydantic import BaseModel
from detector.patterns import detect_patterns
from scoring.engine import calculate_score
from heuristic.analyzer import heuristic_score
from sanitizer.clean import sanitize_prompt

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return{"message":"Prompt Injection Api Working"}

@app.post("/chat")
def chat(request: PromptRequest):

    matches = detect_patterns(request.prompt)

    pattern_score = calculate_score(matches)
    behavior_score, reasons = heuristic_score(request.prompt)
    score = pattern_score + behavior_score
    clean_prompt, removed = sanitize_prompt(request.prompt)

    # if score >= 50:

    #     return {
    #         "status": "Blocked",
    #         "risk_score": score,
    #         "matched_patterns": matches,
    #         "heuristic_reasons": reasons
    #     }

    if clean_prompt == "":
        return {
        "status": "Blocked",
        "reason": "Prompt became empty after sanitization.",
        "risk_score": score,
        "removed_phrases": removed,
        "heuristic_reasons": reasons
    }


    if score >= 70:
        return {
            "status": "Blocked",
            "risk_score": score,
            "matched_patterns": matches,
            "heuristic_reasons": reasons,
            "removed_phrases": removed
        }
         
    elif score >= 40:

        response = send_to_llm(clean_prompt)


        return {
            "status": "Sanitized",
            "risk_score": score,
            "matched_patterns": matches,
            "heuristic_reasons": reasons,
            "removed_phrases": removed,
            "sanitized_prompt": clean_prompt,
            "response": response
        }

    else:

        response = send_to_llm(request.prompt)

        return {
            "status": "Allowed",
            "risk_score": score,
            "matched_patterns": matches,
            "heuristic_reasons": reasons,
            "removed_phrases": removed,
            "response": response
        }
    

