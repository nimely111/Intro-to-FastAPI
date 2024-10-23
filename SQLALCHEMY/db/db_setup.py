from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# database url string
DATABASE_URL = 'sqlite:///stu-record.db'
# database connection
engine = create_engine(DATABASE_URL, echo=False)
# database interaction
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
# skeleton of models
Base = declarative_base()
