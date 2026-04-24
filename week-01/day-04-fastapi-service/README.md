# Day 4

Your first real service.

## Goal

Refactor a working but poorly structured FastAPI app into a real service with layers, dependency injection, a real SQLite database, and endpoint tests.

## Time Box

1.5 to 2 hours

## What We Expect Students To Learn

- build FastAPI endpoints with validation, status codes, and clean error handling
- use Pydantic models as request and response contracts
- structure code with endpoint -> service -> repository boundaries
- pass dependencies with FastAPI `Depends` instead of creating them inline
- connect the app to a real SQLite database
- test endpoints before adding any AI or retrieval logic

## Exercise

Inside `fastapi_report_service/` there is a standalone FastAPI project for this day.

Students must take a messy but working `report requests` API and turn it into a maintainable service.

### What Is Already Given

- a `pyproject.toml`
- a working FastAPI app in `src/report_service/main.py`
- one working `/health` endpoint
- one working but badly structured `GET /report-requests/{request_id}` endpoint
- one empty `POST /report-requests` endpoint
- a real SQLite app database: `data/app.db`
- a separate SQLite test database: `data/test_app.db`
- SQL files to recreate both databases
- SQLAlchemy models and Pydantic schemas
- starter test fixtures for endpoint tests
- one passing smoke test so students can see the test setup

### What Students Must Build

1. refactor the existing `GET /report-requests/{request_id}` endpoint so it is no longer doing everything inline
2. create the repository and service needed for that endpoint
3. implement `POST /report-requests` from scratch using endpoint -> service -> repository
4. add FastAPI dependency wiring for `db -> repository -> service`
5. keep or improve the existing request and response models
6. add endpoint tests for both the refactored endpoint and the new endpoint

## Suggested Business Rules

- `window_days` must be between 7 and 90
- new requests should always start with status `queued`
- asking for a missing request should return `404`

## Acceptance Criteria

- app runs locally
- endpoints use request and response models
- endpoint code becomes thin
- service owns business rules
- repository owns database access
- app uses `data/app.db`
- tests use `data/test_app.db`
- tests cover at least one happy path and one error path
- behavior stays the same after the refactor
- the new endpoint is implemented with the layered architecture from the start

## How To Run

From the repository root:

```bash
cd ml-trainning-program/week-01/day-04-fastapi-service/fastapi_report_service
uv sync
uv run python scripts/reset_databases.py
uv run uvicorn --app-dir src report_service.main:app --reload
```

Run tests:

```bash
uv run pytest
```

If you are already inside `ml-trainning-program/`, then run:

```bash
cd week-01/day-04-fastapi-service/fastapi_report_service
uv sync
uv run python scripts/reset_databases.py
uv run uvicorn --app-dir src report_service.main:app --reload
```

## Deliverables

- one branch
- one PR named `day-4-<student-name>`
- one service with layered structure
- passing endpoint tests
- a short PR note explaining:
  - what was wrong with the original endpoint
  - what lives in the endpoint
  - what lives in the service
  - what lives in the repository
  - how the test database is separated from the app database
