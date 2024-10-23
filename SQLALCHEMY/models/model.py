from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
from db.db_setup import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    firstname = Column(String(50))
    email = Column(String(50))

