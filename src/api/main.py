from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict
import time

from src.agent.graph import graph
from src.agent.prompts import ALLOWED_TONES, ALLOWED_PURPOSES, ALLOWED_USE_CASES
from src.utils.diff_utils import get_text_changes
from src.utils.privacy_utils import detect_sensitive_data, mask_sensitive_data
from src.utils.feedback_utils import save_feedback
from src.utils.analytics_utils import save_usage_log, get_analytics_summary


api = FastAPI(title="Text Refinement AI Agent")


class RefineRequest(BaseModel):
    text: str = Field(..., min_length=1)
    tone: str = "Professional"
    purpose: str = "General Text"
    use_case: str = "General Refinement"
    mask_sensitive_data: bool = True


class RefineResponse(BaseModel):
    original_text: str
    processed_text: str
    refined_text: str
    tone: str
    purpose: str
    use_case: str
    detected_sensitive_data: List[str]
    changes: List[Dict[str, str]]
    processing_time_seconds: float
    error_message: str = ""


class FeedbackRequest(BaseModel):
    original_text: str
    processed_text: str = ""
    refined_text: str
    tone: str
    purpose: str
    use_case: str
    rating: str
    comment: str = ""
    sensitive_data_detected: List[str] = []


class FeedbackResponse(BaseModel):
    message: str
    feedback_id: str


@api.get("/")
def home():
    return {
        "message": "Text Refinement AI Agent API is running",
        "allowed_tones": ALLOWED_TONES,
        "allowed_purposes": ALLOWED_PURPOSES,
        "allowed_use_cases": ALLOWED_USE_CASES
    }


@api.post("/refine", response_model=RefineResponse)
def refine_text(request: RefineRequest):
    start_time = time.perf_counter()

    detected_items = detect_sensitive_data(request.text)

    processed_text = request.text

    if request.mask_sensitive_data:
        processed_text = mask_sensitive_data(request.text)

    state = {
        "input_text": processed_text,
        "tone": request.tone,
        "purpose": request.purpose,
        "use_case": request.use_case
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

    processing_time = round(time.perf_counter() - start_time, 2)

    save_usage_log(
        {
            "tone": result["tone"],
            "purpose": result["purpose"],
            "use_case": result["use_case"],
            "input_length": len(request.text),
            "output_length": len(result["final_output"]),
            "change_count": len(changes),
            "sensitive_data_count": len(detected_items),
            "sensitive_data_types": detected_items,
            "masked_sensitive_data": request.mask_sensitive_data,
            "processing_time_seconds": processing_time
        }
    )

    return RefineResponse(
        original_text=request.text,
        processed_text=result["input_text"],
        refined_text=result["final_output"],
        tone=result["tone"],
        purpose=result["purpose"],
        use_case=result["use_case"],
        detected_sensitive_data=detected_items,
        changes=changes,
        processing_time_seconds=processing_time,
        error_message=result.get("error_message", "")
    )


@api.post("/feedback", response_model=FeedbackResponse)
def submit_feedback(request: FeedbackRequest):
    allowed_ratings = ["Good", "Needs Improvement"]

    if request.rating not in allowed_ratings:
        raise HTTPException(
            status_code=400,
            detail="Invalid rating. Allowed ratings are: Good, Needs Improvement"
        )

    saved_feedback = save_feedback(
        {
            "original_text": request.original_text,
            "processed_text": request.processed_text,
            "refined_text": request.refined_text,
            "tone": request.tone,
            "purpose": request.purpose,
            "use_case": request.use_case,
            "rating": request.rating,
            "comment": request.comment,
            "sensitive_data_detected": request.sensitive_data_detected
        }
    )

    return FeedbackResponse(
        message="Feedback submitted successfully",
        feedback_id=saved_feedback["feedback_id"]
    )


@api.get("/analytics")
def analytics_dashboard():
    return get_analytics_summary()