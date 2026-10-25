import os
DATABASES = {
    "primary": {
        "driver": "postgresql",
        "host": "localhost",
        "port": 5433,
        "user": "anushka",
        "password": os.environ.get("PRA_DB_PASSWORD", ""),
        "dbname": "anushka_local",
        "driver": "postgresql+psycopg2",
    },
    "secondary": {
        "driver": "postgresql",
        "host": "localhost",
        "port": 5432,
        "user": "holocleanuser",
        "password": os.environ.get("HOC_DB_PASSWORD", ""),
        "dbname": "holo",
    },
}
