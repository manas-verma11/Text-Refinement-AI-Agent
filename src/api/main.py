from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.agent.graph import graph
from src.agent.prompts import ALLOWED_TONES, ALLOWED_PURPOSES


api = FastAPI(title="Text Refinement AI Agent")


class RefineRequest(BaseModel):
    text: str = Field(..., min_length=1)
    tone: str = "Professional"
    purpose: str = "General Text"


class RefineResponse(BaseModel):
    original_text: str
    refined_text: str
    tone: str
    purpose: str
    error_message: str = ""


@api.get("/")
def home():
    return {
        "message": "Text Refinement AI Agent API is running",
        "allowed_tones": ALLOWED_TONES,
        "allowed_purposes": ALLOWED_PURPOSES
    }


@api.post("/refine", response_model=RefineResponse)
def refine_text(request: RefineRequest):
    state = {
        "input_text": request.text,
        "tone": request.tone,
        "purpose": request.purpose
    }

    result = graph.invoke(state)

    if result.get("error_message"):
        raise HTTPException(
            status_code=400,
            detail=result["error_message"]
        )

    return RefineResponse(
        original_text=result["input_text"],
        refined_text=result["final_output"],
        tone=result["tone"],
        purpose=result["purpose"],
        error_message=result.get("error_message", "")
    )