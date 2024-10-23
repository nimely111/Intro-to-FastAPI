from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database url string
DATABASE_URL = 'sqlite:///articles_record.db'

# database connection
engine = create_engine(DATABASE_URL, echo=False)

# database interaction
SessionLocal = sessionmaker(bind=engine)

# skeleton of models
Base = declarative_base()