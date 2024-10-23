from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from db.db_setup import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    firstname = Column(String(50))
    firstname = Column(String(50))
    email = Column(String(50))
    # establishing one to many relationship
    posts = relationship('Post', back_populates = 'student')


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    Content = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
    # establishing one to many relationship
    student = relationship('Student', back_populates = 'posts')