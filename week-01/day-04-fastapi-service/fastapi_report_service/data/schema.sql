DROP TABLE IF EXISTS report_requests;

CREATE TABLE report_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT NOT NULL,
    report_type TEXT NOT NULL,
    window_days INTEGER NOT NULL,
    requested_by TEXT NOT NULL,
    status TEXT NOT NULL
);
