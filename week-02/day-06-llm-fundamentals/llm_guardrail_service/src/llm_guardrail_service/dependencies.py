from llm_guardrail_service.config import DATABASE_PATH, OLLAMA_BASE_URL, OLLAMA_MODEL
from llm_guardrail_service.repositories.audit_repository import AuditRepository
from llm_guardrail_service.services.answer_service import MockAnswerService
from llm_guardrail_service.services.guardrail_service import GuardrailService
from llm_guardrail_service.services.ollama_client import OllamaClient
from llm_guardrail_service.services.orchestrator_service import OrchestratorService


def get_audit_repository() -> AuditRepository:
    return AuditRepository(DATABASE_PATH)


def get_guardrail_service() -> GuardrailService:
    return GuardrailService(OllamaClient(OLLAMA_BASE_URL, OLLAMA_MODEL))


def get_answer_service() -> MockAnswerService:
    return MockAnswerService()


def get_orchestrator_service() -> OrchestratorService:
    return OrchestratorService(
        guardrail_service=get_guardrail_service(),
        answer_service=get_answer_service(),
        audit_repository=get_audit_repository(),
    )
