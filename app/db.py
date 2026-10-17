from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

Database_URL = "sqlite:///./taskvault.db"

engine = create_engine(Database_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind= engine , autoflush=False)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()