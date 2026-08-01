import time
from fastapi import FastAPI
from proxy import send_to_llm
from pydantic import BaseModel
from detector.patterns import detect_patterns
from scoring.engine import calculate_score
from heuristic.analyzer import heuristic_score
from sanitizer.clean import sanitize_prompt
from logger.audit import log_request
from fastapi import Request
from fastapi.responses import HTMLResponse
from dashboard.dashboard import templates
from utils.risk import classify_risk



app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return{"message":"Prompt Injection Api Working"}

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request
        }
    )

@app.post("/chat")
def chat(request: PromptRequest):
    start_time = time.perf_counter()
    matches = detect_patterns(request.prompt)
    pattern_score = calculate_score(matches)
    behavior_score, reasons = heuristic_score(request.prompt)
    score = pattern_score + behavior_score
    severity, decision = classify_risk(score)



    if score >= 70:
        explanation = "Prompt blocked because it contains high-risk prompt injection indicators."
    elif score >= 40:
        explanation = "Potential prompt injection attempt detected. Unsafe instructions were removed before forwarding the request."
    else:
        explanation = "No prompt injection indicators detected."

    clean_prompt, removed = sanitize_prompt(request.prompt)

    if clean_prompt == "":

        processing_time = round(time.perf_counter() - start_time, 4)

        log_request(
            request.prompt,
            clean_prompt,
            score,
            severity,
            "Blocked",
            matches,
            reasons,
            removed,
            processing_time
    )
  
        return {
            "status": "Blocked",
            "severity": severity,
            "reason": "Prompt became empty after sanitization.",
            "risk_score": score,
            "explanation": explanation,
            "processing_time": processing_time,
            "removed_phrases": removed,
            "heuristic_reasons": reasons
    }


    if score >= 70:

        processing_time = round(time.perf_counter() - start_time, 4)

        log_request(
            request.prompt,
            clean_prompt,
            score,
            severity,
            "Blocked",
            matches,
            reasons,
            removed,
            processing_time
    )
        
        return {
            "status": "Blocked",
            "severity": severity,
            "risk_score": score,
            "explanation": explanation,
            "matched_patterns": matches,
            "heuristic_reasons": reasons,
            "removed_phrases": removed,
            "processing_time": processing_time
    }
         
    elif score >= 40:

        response = send_to_llm(clean_prompt)
        processing_time = round(time.perf_counter() - start_time, 4)

        log_request(
            request.prompt,
            clean_prompt,
            score,
            severity,
            "Sanitized",
            matches,
            reasons,
            removed,
            processing_time
        )

        return {
            "status": "Sanitized",
            "severity": severity,
            "risk_score": score,
            "explanation": explanation,
            "matched_patterns": matches,
            "heuristic_reasons": reasons,
            "removed_phrases": removed,
            "sanitized_prompt": clean_prompt,
            "response": response,
            "processing_time": processing_time
    }
    

    else:

        response = send_to_llm(request.prompt)
        processing_time = round(time.perf_counter() - start_time, 4)


        log_request(
        request.prompt,
        clean_prompt,
        score,
        severity,
        "Sanitized",
        matches,
        reasons,
        removed,
        processing_time
    )
    

    return {
        "status": "Allowed",
        "risk_score": score,
        "severity": severity,
        "explanation": explanation,
        "matched_patterns": matches,
        "heuristic_reasons": reasons,
        "removed_phrases": removed,
        "sanitized_prompt": clean_prompt,
        "response": response,
        "processing_time": processing_time
}
