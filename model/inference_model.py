from pydantic import BaseModel
from typing import List, Any


class Context(BaseModel):
    sentiment: str
    value: str


class EntityRecognition(BaseModel):
    type: str
    value: str


class InferenceRequest(BaseModel):
    content_input: str
    main_brand: str


class InferenceResponse(BaseModel):
    result: Any


class InferenceResult(BaseModel):
    sentiment: str
    severity: str
    emotion: str
    polarity: float
    intensity: str
    topic: str
    subtopic: str
    category: str
    industry: str
    subject: str
    product_type: str
    angle: str
    entity_recognition: List[EntityRecognition]
    intent: str
    purpose: str
    tone: str
    audience: str
    mention_mainbrand: bool
    context: List[Context]
    explanation: str
    spam: str
    advertisement: str


class CommentRequest(BaseModel):
    id: str
    content: str


class CommentResponse(BaseModel):
    id: str
    sentiment: str


class InferenceContextRequest(BaseModel):
    content: str
    id: str
    comment: List[CommentRequest]


class InferenceContextResponse(BaseModel):
    topic: str
    subtopic: str
    sentiment: str
    id: str
    comment: List[CommentResponse]
