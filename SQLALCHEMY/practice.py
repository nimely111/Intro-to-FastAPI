from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
# database url string
DATABASE_URL = 'sqlite:///stu-record.db'
# create connection with the dataabase
engine = create_engine(DATABASE_URL, echo=False)
# set interaction with the database for user each session
SessionLocal = sessionmaker(bind=engine)
# create an instance from the SessionLocal object call db
session = SessionLocal()
# establishment of models
Base = declarative_base()
  

# create a student table
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, Sequence("student_id_seq"), primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    # extablishing relationship
    posts = relationship('Post', back_populates='student')


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
    # establishing one to many relationship for the posts tables
    student = relationship('Student', back_populates='posts')

# add student table to the database
Base.metadata.create_all(engine)

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



session.add(student2)
session.add_all([student3, student4, post1, post2, post3, post4])
session.commit()

# get all posts
student_with_post = session.query(Student, Post).join(Student).all()
for student, post in student_with_post:
    print(f"{post.title}: {student.firstname}")

# get all Samuel's posts
samuel = session.query(Student).filter_by(firstname = 'Samuel').first()
for post in samuel.posts:
    print(f"Title: {post.title}")

# read pydantic model documentation and validation
# advance query to get all Samuel's posts
filtered_posts = session.query(Post).join(Student).filter(Student.firstname == 'Samuel').all()
for post in filtered_posts:
    print(f"Title: {post.title}, Author: {post.student.firstname}")




# fetch a student
# student = session.query(Student).filter_by(firstname = 'Esther').first()
# print(f"Student's Info: {student.firstname, student.lastname}")

# delete a student
# student = session.query(Student).filter_by(firstname='James').first()
# session.delete(student)
# session.commit()
# print(student.firstname)


