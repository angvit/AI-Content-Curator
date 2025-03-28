from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = ""
engine = create_engine(DATABASE_URL)

# managing transactions and DB state
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# yield a fresh session per request (FASTAPI)
def get_db():
    # session instance
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

