from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends
import os

load_dotenv()

CONNECTION_STRING = f"postgresql://{os.getenv("USER")}:{os.getenv("PASSWORD")}@{os.getenv("HOST")}:{os.getenv("PORT")}/{os.getenv("DATABASE")}"

engine = create_engine(CONNECTION_STRING, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DbSession = Annotated[Session, Depends(get_db)]
