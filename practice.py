from fastapi import FastAPI

app = FastAPI()


users = [{
        1:{
        "name": "John",
        "age": 20,
    },
     2:{
        "name": "John",
        "age": 20,
    }
   }]


@app.get("/users/me")
async def read_user_me():
    return {'user_id': 'current user'}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
        return {"user_id": user_id}

        