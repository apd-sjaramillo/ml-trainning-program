# FastAPI Report Service

Standalone Day 4 exercise project.

The starting point is intentionally uneven:

- one endpoint works, but is too heavy inside `src/report_service/main.py`
- one endpoint is blank and must be built properly

The challenge is to refactor it into:

- endpoint layer
- service layer
- repository layer
- dependency wiring with FastAPI

## Databases

- `data/app.db`: used by the running app
- `data/test_app.db`: used by tests through dependency overrides

To recreate both:

```bash
uv run python scripts/reset_databases.py
```

To run the app:

```bash
uv sync
uv run uvicorn --app-dir src report_service.main:app --reload
```

Important:

- run these commands from `week-01/day-04-fastapi-service/fastapi_report_service`
- if you are one directory above, `uv` will not find this project's `pyproject.toml`
- `--app-dir src` is needed so `uvicorn` can import `report_service`
