from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from enum import Enum

class ExplanationStyle(str, Enum):
    VISUAL = "visual"
    ANALOGY = "analogy"
    TECHNICAL = "technical"
    PRACTICAL = "practical"
    SIMPLIFIED = "simplified"

class InteractionType(str, Enum):
    CONTINUE = "continue"
    MORE_DETAILS = "more_details"
    ANALOGY = "analogy"
    EXAMPLE = "example"
    CLARIFY = "clarify"
    BACK = "back"

class ExplanationRequest(BaseModel):
    topic: str
    user_id: Optional[str] = None
    preferred_style: Optional[ExplanationStyle] = None
    context: Optional[str] = None

class InteractionButton(BaseModel):
    type: InteractionType
    label: str
    icon: str
    description: Optional[str] = None

class ExplanationStep(BaseModel):
    step_number: int
    content: str
    visual_type: str  # diagram, animation, code, text
    visual_data: Optional[Dict[str, Any]] = None
    interaction_buttons: List[InteractionButton]
    checkpoint: bool = False

class ExplanationResponse(BaseModel):
    id: str
    topic: str
    current_step: int
    total_steps: int
    steps: List[ExplanationStep]
    style: ExplanationStyle
    metadata: Optional[Dict[str, Any]] = None

class InteractionRequest(BaseModel):
    explanation_id: str
    user_id: Optional[str] = None
    interaction_type: InteractionType
    current_step: int
    user_input: Optional[str] = None

class InteractionResponse(BaseModel):
    success: bool
    next_step: Optional[ExplanationStep] = None
    branched: bool = False
    message: Optional[str] = None

class UserProgress(BaseModel):
    user_id: str
    explanation_id: str
    current_step: int
    completed_steps: List[int]
    interactions: List[Dict[str, Any]]
    understanding_score: float
    created_at: str
    updated_at: str