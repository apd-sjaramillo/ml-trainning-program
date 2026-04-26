from collections.abc import Generator
from pathlib import Path
import sqlite3

import pytest
from fastapi.testclient import TestClient

from llm_guardrail_service.config import DATABASE_PATH
from llm_guardrail_service.main import app


@pytest.fixture(autouse=True)
def reset_database() -> Generator[None, None, None]:
    database_path = Path(DATABASE_PATH)
    database_path.parent.mkdir(parents=True, exist_ok=True)
    if database_path.exists():
        database_path.unlink()
    schema_path = database_path.parent / "schema.sql"
    connection = sqlite3.connect(database_path)
    try:
        connection.executescript(schema_path.read_text())
        connection.commit()
    finally:
        connection.close()
    yield


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as test_client:
        yield test_client
