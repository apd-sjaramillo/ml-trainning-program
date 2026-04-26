from llm_guardrail_service.schemas import AskResponse


class OrchestratorService:
    def __init__(self, guardrail_service, answer_service, audit_repository) -> None:
        self.guardrail_service = guardrail_service
        self.answer_service = answer_service
        self.audit_repository = audit_repository

    async def handle_question(self, question: str) -> AskResponse:
        raise NotImplementedError("Implement handle_question during the Day 6 exercise")
