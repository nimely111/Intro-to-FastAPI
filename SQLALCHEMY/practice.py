from db.db_setup import engine, session, Base  
from models.models import Student, Post
# add student table to the database
Base.metadata.create_all(engine)

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


