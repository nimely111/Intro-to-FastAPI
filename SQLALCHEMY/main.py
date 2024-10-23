from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# db url string
DATABASE_URL = "sqlite:///orm.db"
# established db conection
engine = create_engine(DATABASE_URL, echo=False)
# established db  interaction
Session = sessionmaker(bind=engine)
session = Session()
# establishment of the data models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key = True)
    name = Column(String(50))
    email = Column(String(50))

    # applying one to many relationship
    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # applying one to many relationship
    user = relationship('User', back_populates='posts')


# create all tables in the database if it does not exist
Base.metadata.create_all(engine)

# add users to table
user1 = User(name='Alice', email='alice@example.com')
user2 = User(name='Bob', email='bob@example.com')
post1 = Post(title='Alice\'s first post ', content='This is the content of Alice\'s first post', user=user1)
post2 = Post(title='Alice\'s second post ', content='This is the content of Alice\'s second post', user=user1)
post3 = Post(title='Bob first post', content='This is the content of Bob\'s first post', user=user2)

# add user table, and post table to db
session.add_all([user1, user2, post1, post2, post3])
# save user table, and post table to db
session.commit()

# get all user's posts
# posts_with_users = session.query(User, Post).join(User).all()
# for user, post in posts_with_users:
#     print(f"{post.title}: {user.name}")

# get all alice's posts
alice = session.query(User).filter_by(name = 'Alice').first()
for post in alice.posts:
    print(f"{post.title}")

# advance query to get all alice's posts
filtered_post = session.query(Post).join(User).filter(User.name == 'Alice').all()
for post in filtered_post:
    print(f"Title: {post.title} Author: {post.user.name}")

# query and fetch a specific user
# user = session.query(User).filter_by(name = 'James').first()
# print(user.name)


# delete user
# user = session.query(User).filter_by(name = 'James').first()
# session.delete(user)
# session.commit()
# print("user ",user.name, f"has been deleted")
    
