# LLM Guardrail Service

Standalone Day 6 exercise project.

## Run

```bash
cd ml-trainning-program/week-02/day-06-llm-fundamentals/llm_guardrail_service
uv sync
uv run python scripts/reset_db.py
uv run uvicorn --app-dir src llm_guardrail_service.main:app --reload
```

## Local Model

Expected local setup:

```bash
ollama pull llama3.2:3b
ollama serve
```

Default model name:

- `llama3.2:3b`

Override with:

- `OLLAMA_MODEL`

## Notes

- the local model is only for guardrail classification
- the stronger answer model is represented by a mock service in this starter
- if students have Snowflake or Databricks access, they can replace the mock answer service
- the hardest part of this lab is not the HTTP call to Ollama
- the hardest part is prompt design + routing logic + tests
