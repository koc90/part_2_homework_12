from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.URI import URI


engine = create_engine(URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
