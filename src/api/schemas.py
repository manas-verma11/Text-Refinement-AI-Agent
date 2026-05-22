from pydantic import BaseModel, Field
from typing import List


class SpellError(BaseModel):
    offset: int
    wrong: str
    suggestion: str
    confidence: float = Field(ge=0.0, le=1.0)


class GrammarError(BaseModel):
    offset: int
    span: str
    issue: str
    correction: str
    confidence: float = Field(ge=0.0, le=1.0)


class RefinementResult(BaseModel):
    spelling_errors: List[SpellError]
    grammar_errors: List[GrammarError]
    refined_text: str


class RefineRequest(BaseModel):
    text: str


class RefineResponse(RefinementResult):
    diff_report: str