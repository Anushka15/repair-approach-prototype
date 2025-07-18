# database/connection.py

from sqlalchemy import create_engine
from config.config import DATABASE

def create_connection():
    try:
        db_url = f"{DATABASE['driver']}://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['dbname']}"
        engine = create_engine(db_url)
        return engine.connect()
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None