from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def build_database(database_name: str, seed_name: str) -> None:
    database_path = DATA_DIR / database_name
    if database_path.exists():
        database_path.unlink()

    connection = sqlite3.connect(database_path)
    try:
        schema_sql = (DATA_DIR / "schema.sql").read_text()
        seed_sql = (DATA_DIR / seed_name).read_text()
        connection.executescript(schema_sql)
        connection.executescript(seed_sql)
        connection.commit()
    finally:
        connection.close()


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    build_database("app.db", "seed_app.sql")
    build_database("test_app.db", "seed_test.sql")


if __name__ == "__main__":
    main()
