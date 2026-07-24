from fastapi import FastAPI
from proxy import send_to_llm
from pydantic import BaseModel
from detector.patterns import detect_patterns
from scoring.engine import calculate_score
from heuristic.analyzer import heuristic_score

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

    if score >= 50:

        return {
            "status": "Blocked",
            "risk_score": score,
            "matched_patterns": matches,
            "heuristic_reasons": reasons
        }

    response = send_to_llm(request.prompt)

    return {
        "status": "Allowed",
        "risk_score": score,
        "heuristic_reasons": reasons,
        "response": response
    }

