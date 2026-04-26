from llm_guardrail_service.schemas import GuardrailDecision
from llm_guardrail_service.services.ollama_client import OllamaClient


class GuardrailService:
    def __init__(self, client: OllamaClient) -> None:
        self.client = client

    def build_prompt(self, question: str) -> str:
        # Intentionally weak starter prompt for Day 6.
        # Students should improve this prompt so the local model returns
        # consistent JSON that matches the GuardrailDecision schema.
        return f"""
Classify this question for safety and respond in JSON.

Question:
{question}
        """.strip()

    async def classify(self, question: str) -> GuardrailDecision:
        prompt = self.build_prompt(question)
        payload = await self.client.generate_json(prompt)
        return GuardrailDecision.model_validate(payload)
