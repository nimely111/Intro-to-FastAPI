from pydantic import BaseModel, EmailStr, field_validator

# pydantic BENEFITS
# IDE TYPE HINTS
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
user = User(name='Sam', email='sam@example.com', account_id=1234)
print(user)
print('====================')

# JSON SERIALIZATION
# convert from model to dictionary object
# user_dict_obj = user.dict()
user_dict_obj = user.model_dump()
print(user_dict_obj)
print('====================')

# to convert a pydantic model to json you can call the json method on the model instance
# user_json_str = user.json()
# print(user_json_str)

user_json_str = user.model_dump_json()
print(user_json_str)
print('====================')


# convert json string back to pydantic model
# user = User.parse_raw(json_str)
user = User.model_validate_json(user_json_str)
print(user)
# pydantic vs dataclass
'''
                    pydantic vs dataclass
    TYPE HINTS        ✅         ✅
    Data Validation   ✅         ❌ 
    Serialization     ✅         ⚠ 
    Built in          ❌         ✅

'''