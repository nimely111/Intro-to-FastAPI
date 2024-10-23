from pydantic import BaseModel, EmailStr, field_validator

# pydantic BENEFITS
# IDE TYPEHINTS
# DATA VALIDATION
# JOSN SERIALIZATION

class User(BaseModel):
    name: str 
    email: EmailStr
    account_id: int

# adding custom validation
    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <=0:
            raise ValueError(f"account_id must be positive: {value}")
        return value
            

# user = User(name='Sam', email='sam@example.com', account_id=1234)
# print(user.name)
user = User(name='Sam', email='sam@example.com', account_id=-1234)

print(user)