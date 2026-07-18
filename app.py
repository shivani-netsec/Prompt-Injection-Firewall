from fastapi import FastAPI
from proxy import send_to_llm
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return{"message":"Prompt Injection Api Working"}

@app.post("/chat")
def chat(request: PromptRequest):

    response = send_to_llm(request.prompt)

    return {
        "response": response
    }


