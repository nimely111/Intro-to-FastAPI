from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    id: int
    item: str
    completed: bool

    
class UpdateTodo(BaseModel):
     id: int
     item: str
    #  completed: Optional[bool] = None
     completed: bool | None = None