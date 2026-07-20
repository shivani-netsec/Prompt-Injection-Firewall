from fastapi import FastAPI
from proxy import send_to_llm
from pydantic import BaseModel
from detector.patterns import detect_patterns
from scoring.engine import calculate_score

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return{"message":"Prompt Injection Api Working"}

@app.post("/chat")
def chat(request: PromptRequest):

    matches = detect_patterns(request.prompt)

    score = calculate_score(matches)

    if score >= 50:

        return {
            "status": "Blocked",
            "reason": "Prompt Injection Detected",
            "matched_patterns": matches
        }

    response = send_to_llm(request.prompt)

    return {
        "status": "Allowed",
        "response": response
    }

