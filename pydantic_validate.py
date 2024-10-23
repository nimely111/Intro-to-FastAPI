from pydantic import BaseModel, EmailStr

# pydantic BENEFITS
# IDE TYPEHINTS
# DATA VALIDATION
# JOSN SERIALIZATION

class User(BaseModel):
    name: str 
    email: EmailStr
    account_id: int

# user = User(name='Sam', email='sam@example.com', account_id=1234)
# print(user.name)
user = User(name='Sam', email='sam@example.com', account_id=1234)

print(user.name)