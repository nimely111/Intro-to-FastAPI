from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class Item(BaseException):
    name: str 
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = [] 

@app.post("/items")
async def create_items(item: Item):
    return item
