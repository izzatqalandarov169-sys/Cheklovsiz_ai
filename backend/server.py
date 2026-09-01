"""Cheklovsiz AI local backend skeleton.
Run: pip install fastapi uvicorn && uvicorn server:app --reload
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Cheklovsiz AI", version="0.1.0")

class ChatRequest(BaseModel):
    message: str

class VideoRequest(BaseModel):
    prompt: str
    duration: int = 5

@app.get("/health")
def health():
    return {"status": "ok", "service": "Cheklovsiz AI"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"reply": "Local chat model hali ulanmagan.", "message": req.message}

@app.post("/generate-video")
def generate_video(req: VideoRequest):
    return {"status": "queued", "prompt": req.prompt, "duration": req.duration}
