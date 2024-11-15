from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, EmailStr
from typing import Optional, Literal, Annotated
from config import settings
from enum import Enum


app = FastAPI(
    title=settings.PROJECT_NAME, 
    version=settings.PROJECT_VERSION
    )

# PART 2 path parameter
@app.get('/users')
async def list_users():
    return {"message": "list users route"}


@app.get("/users/me")
async def get_current_user():
    return {"message":"this is the current user"}


@app.get("/users/{user_id}")
async def get_users(user_id: str):
    return {"user_id": user_id}


class CanditateModel(str, Enum):
    james = "James"
    peter = "Peter"
    david = "David"


@app.get("/vote/{canditate_name}")
async def get_canditate_name(canditate_name: CanditateModel):
    if canditate_name is CanditateModel.james:
        return {    
            "canditate_name": canditate_name, 
            "message": f"You voted for {canditate_name.value}"
        }
    if canditate_name.value == "Peter":
        return {    
            "canditate_name": canditate_name, 
            "message": f"You voted for {canditate_name.value}"
        }
    return {
        "canditate_name": canditate_name,
        "message": f"You voted for {canditate_name.value}"
        }


# PART 3 query parameter

fake_item_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_item_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_item(
    item_id: str, 
    sample_query_param: str, 
    q: str | None = None, 
    short: bool = False
    ):
    item = {
        "item_id": item_id, 
        "sample_query_param": sample_query_param
    }
    if q:
        item.update({"q": q})
    if not short:
       item.update(
           {
               "description": "This is an amazing item that has a long description"
           }
       )
    return item

# using path and query parameters

# @app.get("/users/{user_id}/items/{fni_id}")
# async def get_user_item(user_id: int, fni_id: str, q: str | None = None, short: bool = False):
#     item = {"fni_id": fni_id, "owner_id": user_id}
#     if q:
#         item.update(
#             {"q": q}
#         )
#     if not short:
#         item.update(
#             {'description': 'lorem ipsum is the best dummy text'}
#         )
#     return item



@app.get("/students/{student_id}/scholars/{scholar_id}")
async def read_scholar_student(
        student_id: int, 
        scholar_id: str, 
        scholar_description: str,
        scholar_type: str | None = None, 
        is_scholar_option: bool = False,
    ):
    scholar_data = {
        "scholar_id": scholar_id, 
        "student_id": student_id,
        "scholar_description":scholar_description
    }

    if scholar_type:
        scholar_data.update({"scholar": f"This student is a {scholar_type}"})

    if not is_scholar_option:
        scholar_data.update({"eligibility": "You are NOT eligibility to stay in the dorm"})
    else:
         scholar_data.update({"eligibility": "You are eligibility to stay in the dorm"})

    
    if  scholar_description:
        scholar_data.update({"description": scholar_description})

    return scholar_data



# PART 4 Request Body
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Request Body + path
@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_wit_tax = item.price + item.tax
        item_dict.update(
            {"price_with_tax": price_wit_tax}
        )
    return item_dict



# Request Body + path + query
@app.put("/items/{item_id}")
async def update_item(
        item_id: int, 
        item: Item, 
        q: str | None = None
    ):
    results = {"item_id": item_id, **item.dict()}
    if q:
        results.update(
            {"q": q}
        )
    return results

# PART 5 query parameter and string validation
@app.get("/items/")
async def read_items(
        q: Annotated[
            list[str], 
        Query(
            min_length=3, 
            max_length=10,
            title="sample query string", 
             description="Query string for the items to search in the database that have a good match",
            alias="item-query",
            deprecated=True
            )] = ["table", "chair"] 
            ):
    results = {"items": [{"item_id": "chair"}, {"item_id": "table"}]}
    if q:
        results.update({"q": q})
    return results


# @app.get("/items/")
# async def read_default_items(q: Annotated[list[str], Query()] = ["Table", "Chair"]):
#     results = {"items": [{"fni_id": "chair"}, {"fni_id": "table"}]}
#     if q:
#         results.update({"q": q})
#     return results


@app.get("/items_hidden")
async def hidden_query_route(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not found"}



# PART 6 PATH PARAMETERS AND NUMERIC VALIDATIONS
@app.get("/inventories/{id}")
async def read_inventory(
    id: Annotated[int, 
    Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None
    ):
    results = {"item_id": id}
    if q:
        results.update({"q": q})
    return results



@app.get("/furnituries/{fni_id}")
async def read_furniture(
    *,
    fni_id: int = Path(..., title="The ID of the item to get", gt=10, le=100),
    q: str = Query(alias="query-item"),
    size: float = Query(..., lt=0, le=7.75)
    ):
    results = {"fni_id": fni_id, "size": size}
    if q:
        results.update({"q": q})
    return results



# ============================================================
@router.get('/get-coach-rocks/{coach_id}', status_code=status.HTTP_200_OK)
async def get_coach_rocks(
    coach_id: int,
    db: Session = Depends(get_db), 
    token_data: TokenData = Depends(verify_coach_or_coachmanager_access_token)
    ):
    """
    Get the 'rocks' or tasks assigned to a particular coach by coach ID
    """
    
    # Validate if the user is a coach
    coach = db.query(User).filter(
        User.id == coach_id, 
        User.role.in_([UserRole.Coach, UserRole.HeadCoach, UserRole.AssistantCoach])
    ).first()

    if not coach:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coach not found")

    # Fetch the coach's rocks (tasks/assignments)
    rocks = db.query(COOTodoList).filter(
        COOTodoList.user_id == coach_id,
        COOTodoList.status == "Pending"  # Assuming you are checking for 'Pending' tasks
    ).all()

    if not rocks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No rocks (tasks) found for this coach")

    return {"coach_id": coach_id, "coach_name": f"{coach.firstname} {coach.lastname}", "rocks": rocks}




# learning about repsonse model parameter PART 13
# class Item(BaseModel):
#     name: str 
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = [] 

# users = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }


# @app.get("/users/{user_id}", response_model=Item)
# async def read_users(user_id: Literal["foo", "bar", "baz"]):
#     return Item[user_id]

# @app.post("/users/", response_model=Item)
# async def create_item(item: Item):
#     return item


# # response include
# @app.get(
#     "/users/{user_id}/name",
#     response_model=Item,
#     response_model_include={"name", "description"},
# )
# async def read_item_name(user_id: Literal['foo', 'bar', 'baz']):
#     return users[user_id]


# # response exclude

# @app.get("/users/{user_id}/public", response_model=Item, response_model_exclude={"tax"})
# async def read_item_public_data(user_id: Literal['foo', 'bar', 'baz']):
#     return users[user_id]

# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None


# class UserIn(UserBase):
#     password: str

# class UserOut(UserBase):
#     pass

# @app.post("/users/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user.model_dump()
    
    
    
    
    