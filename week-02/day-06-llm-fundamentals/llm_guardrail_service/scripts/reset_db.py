from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def build_database() -> None:
    database_path = DATA_DIR / "audit.db"
    if database_path.exists():
        database_path.unlink()

    connection = sqlite3.connect(database_path)
    try:
        schema_sql = (DATA_DIR / "schema.sql").read_text()
        connection.executescript(schema_sql)
        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    build_database()
