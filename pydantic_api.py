from fastapi import FastAPI, status
from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional, Literal
from uuid import UUID, uuid4

app = FastAPI()
# TODOS:
# 1. add field validation
# 2. Dynamic UUID
# Populate JSON to python objects
# Custom Validation


# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str = Field(min_length=5, max_length=12)
#     age: int = Field(gt=13, lt=100)

    
#     class Config:
#         json_schema_extra = {
#             'example':{
#                 'email': 'test@example.com',
#                 'password': 'test123!',
#                 'age': 25,
#             }
#         }
    
#     @field_validator('password')
#     def password_validator(cls, value):
#         if value == 'test123!':
#             raise ValueError(f"Please do not use default password {value}")
#         return value
    


# class User(UserCreate):
#     id: UUID = Field(default_factory=uuid4)



# @app.post('/users/', response_model=User, status_code=status.HTTP_201_CREATED)
# def create_user(user: UserCreate):
#     created_user = User(**user.model_dump())
#     return created_user


# learning about repsonse model parameter
class Item(BaseModel):
    name: str 
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = [] 

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_items(item_id: Literal["foo", "bar", "baz"]):
    return Item[item_id]

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


# response include
@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: Literal['foo', 'bar', 'baz']):
    return items[item_id]


# response exclude

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: Literal['foo', 'bar', 'baz']):
    return items[item_id]

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn):
    return user.model_dump()
    