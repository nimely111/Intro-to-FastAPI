from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from db.db_setup import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    # establishing one to many relationship
    posts = relationship('Post', back_populates = 'student')


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
    # establishing one to many relationship
    student = relationship('Student', back_populates = 'posts')

student1 = Student(
        firstname='Samuel', 
        lastname='Nimely', 
        email='samuel@example.com'
    )

student2 = Student(
        firstname='Victoria', 
        lastname='Johnson', 
        email='victoria@example.com'
    )
student3 = Student(
        firstname='James', 
        lastname='Dolo', 
        email='james@example.com'
    )

student4 = Student(
        firstname='Esther', 
        lastname='Jones', 
        email='esther@example.com'
    )
post1 = Post(
        title='Samuel\'s first post', 
        content='This is Samuel\'s first post', 
        student=student1
        )

post2 = Post(
        title='Samuel\'s second post', 
        content='This is Samuel\'s second post', 
        student=student1
        )

post3 = Post(
        title='Victoria\'s first post', 
        content='This is Victoria\'s first post', 
        student=student2
        )

post4 = Post(
        title='James first post', 
        content='This is James first post', 
        student=student3
        )