import sqlite3
from pathlib import Path


class AuditRepository:
    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path

    def create_event(
        self,
        question: str,
        allowed: bool,
        reason: str | None,
        answer_preview: str | None,
    ) -> None:
        with sqlite3.connect(self.database_path) as connection:
            connection.execute(
                """
                INSERT INTO audit_events (question, allowed, reason, answer_preview)
                VALUES (?, ?, ?, ?)
                """,
                (question, int(allowed), reason, answer_preview),
            )
            connection.commit()

    def count_events(self) -> int:
        with sqlite3.connect(self.database_path) as connection:
            row = connection.execute("SELECT COUNT(*) FROM audit_events").fetchone()
        return 0 if row is None else int(row[0])
