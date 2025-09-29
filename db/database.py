from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from core.config import settings
from sqlalchemy import text

user = settings.DB_USER
password = quote_plus(settings.DB_PASSWORD)  # Encode special chars
port_part = f",{settings.DB_PORT}" if settings.DB_PORT else ""
SQL_SERVER_CONNECTION_STRING = (
    f"mssql+pyodbc://{user}:{password}@{settings.DB_SERVER}{port_part}/{settings.DB_NAME}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

SQL_SERVER_CONNECTION_STRING_TEST = (
    f"mssql+pyodbc://{user}:{password}@{settings.DB_SERVER}{port_part}/BACKUP"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(SQL_SERVER_CONNECTION_STRING)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine1 = create_engine(SQL_SERVER_CONNECTION_STRING_TEST)
SessionLocal1 = sessionmaker(autocommit=False, autoflush=False, bind=engine1)


def test_connection():
    db = SessionLocal1()
    try:
        yield db
    finally:
        db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()