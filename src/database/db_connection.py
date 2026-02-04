# database/connection.py

from sqlalchemy import create_engine,text
from config.config import DATABASES
from sqlalchemy.engine import URL

def create_engine_for_db(which: str = "primary"):
    cfg = DATABASES[which]
    url = URL.create(drivername=cfg["driver"],
        username=cfg["user"],
        password=cfg["password"],
        host=cfg["host"],
        port=cfg["port"],
        database=cfg["dbname"],
    )
    return create_engine(url)