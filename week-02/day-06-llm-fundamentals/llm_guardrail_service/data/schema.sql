DROP TABLE IF EXISTS audit_events;

CREATE TABLE audit_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    allowed INTEGER NOT NULL,
    reason TEXT,
    answer_preview TEXT
);
