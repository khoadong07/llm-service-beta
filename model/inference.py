from pydantic import BaseModel
from typing import List

class Context(BaseModel):
    sentiment: str
    value: str

class EntityRecognition(BaseModel):
    type: str
    value: str

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
