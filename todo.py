from fastapi import FastAPI, HTTPException
from models import Todo, UpdateTodo


# initialize the fast api instance
app = FastAPI()



@app.get("/")
async def home():
    return {"message": "Hello World"}



todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todos found"}
    


# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "todo has been added"}

# Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, updateTodo: UpdateTodo):
        for todo in todos:
            if todo.id == todo_id:
                todo.id = todo_id
                todo.item = updateTodo.item
                todo.completed = updateTodo.completed
                return {"message": "todo updated successfully"}
        raise HTTPException(status_code=404, detail="No todo found")


 
# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "todo item has been DELETED!"}
    raise HTTPException(status_code=404, detail="No todos found")