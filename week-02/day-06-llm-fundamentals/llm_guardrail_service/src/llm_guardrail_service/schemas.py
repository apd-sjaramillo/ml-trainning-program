from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class GuardrailDecision(BaseModel):
    harassment: bool
    prompt_injection: bool
    allowed: bool
    reason: str | None


class AskResponse(BaseModel):
    allowed: bool
    reason: str | None
    answer: str | None
