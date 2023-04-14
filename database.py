from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

#
SQLALCHEMY_DATABASE_URL = "sqlite:///./news.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://210030010@iitdh.ac.in:Iitdharwad@123.in@postgresserver/news.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
