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


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=5, max_length=12)
    age: int = Field(gt=13, lt=100)

    
    class Config:
        json_schema_extra = {
            'example':{
                'email': 'test@example.com',
                'password': 'test123!',
                'age': 25,
            }
        }
    
    @field_validator('password')
    def password_validator(cls, value):
        if value == 'test123!':
            raise ValueError(f"Please do not use default password {value}")
        return value
    


class User(UserCreate):
    id: UUID = Field(default_factory=uuid4)



@app.post('/users/', response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    created_user = User(**user.model_dump())
    return created_user

