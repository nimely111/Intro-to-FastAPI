from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from db.db_setup import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    firstname = Column(String(50))
    email = Column(String(50))


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    Content = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
