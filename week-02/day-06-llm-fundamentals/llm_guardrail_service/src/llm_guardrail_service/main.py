from fastapi import Depends, FastAPI, HTTPException, status

from llm_guardrail_service.dependencies import get_orchestrator_service
from llm_guardrail_service.schemas import AskRequest, AskResponse
from llm_guardrail_service.services.orchestrator_service import OrchestratorService


app = FastAPI(title="LLM Guardrail Service")


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse, status_code=status.HTTP_200_OK)
async def ask_question(
    payload: AskRequest,
    orchestrator: OrchestratorService = Depends(get_orchestrator_service),
) -> AskResponse:
    try:
        return await orchestrator.handle_question(payload.question)
    except NotImplementedError as exc:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail=str(exc),
        ) from exc
