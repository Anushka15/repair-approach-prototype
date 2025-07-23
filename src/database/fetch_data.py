from sqlalchemy import text
from src.database.db_connection import create_engine_for_db

def fetch_data_results(query: str, params: dict = None):
    engine = create_engine_for_db()
    conn = None
    try:
        conn = engine.connect()
        result = conn.execute(text(query), params or {})
        rows = result.fetchall()
        return rows
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        if conn:
            conn.close()
