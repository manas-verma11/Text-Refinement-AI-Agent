from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict

from src.agent.graph import graph
from src.agent.prompts import ALLOWED_TONES, ALLOWED_PURPOSES
from src.utils.diff_utils import get_text_changes
from src.utils.privacy_utils import detect_sensitive_data, mask_sensitive_data


api = FastAPI(title="Text Refinement AI Agent")


class RefineRequest(BaseModel):
    text: str = Field(..., min_length=1)
    tone: str = "Professional"
    purpose: str = "General Text"
    mask_sensitive_data: bool = True


class RefineResponse(BaseModel):
    original_text: str
    processed_text: str
    refined_text: str
    tone: str
    purpose: str
    detected_sensitive_data: List[str]
    changes: List[Dict[str, str]]
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
    detected_items = detect_sensitive_data(request.text)

    processed_text = request.text

    if request.mask_sensitive_data:
        processed_text = mask_sensitive_data(request.text)

    state = {
        "input_text": processed_text,
        "tone": request.tone,
        "purpose": request.purpose
    }

    result = graph.invoke(state)

    if result.get("error_message"):
        raise HTTPException(
            status_code=400,
            detail=result["error_message"]
        )

    changes = get_text_changes(
        result["input_text"],
        result["final_output"]
    )

    return RefineResponse(
        original_text=request.text,
        processed_text=result["input_text"],
        refined_text=result["final_output"],
        tone=result["tone"],
        purpose=result["purpose"],
        detected_sensitive_data=detected_items,
        changes=changes,
        error_message=result.get("error_message", "")
    )