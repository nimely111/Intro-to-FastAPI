from fastapi import FastAPI
from uuid import uuid4
from typing import List
from models import User, Role, Gender


# app instance
app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name = "Victria",
        last_name = "Johnson",
        gender = Gender.female,
        roles = [Role.student]        
    ),
     User(
        id=uuid4(),
        first_name = "Samuel",
        last_name = "Nimely",
        gender = Gender.male,
        roles = [Role.admin, Role.user]        
    )
]

@app.get("/")
async def root():
    return {"Hello": "Samuel"}

@app.get("/users")
async def fetch_users():
    return db;