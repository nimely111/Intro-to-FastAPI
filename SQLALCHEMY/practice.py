from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Sequence
from db.db_setup import engine, session, Base  

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


