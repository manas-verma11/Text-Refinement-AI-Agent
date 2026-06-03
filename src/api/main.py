from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from src.agent.graph import graph
from src.agent.prompts import ALLOWED_TONES


api = FastAPI(title="Text Refinement AI Agent")


class RefineRequest(BaseModel):
    text: str = Field(..., min_length=1)
    tone: str = "Professional"


class RefineResponse(BaseModel):
    original_text: str
    refined_text: str
    tone: str
    error_message: str = ""


@api.get("/")
def home():
    return {
        "message": "Text Refinement AI Agent API is running",
        "allowed_tones": ALLOWED_TONES
    }


@api.post("/refine", response_model=RefineResponse)
def refine_text(request: RefineRequest):
    state = {
        "input_text": request.text,
        "tone": request.tone
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
        error_message=result.get("error_message", "")
    )