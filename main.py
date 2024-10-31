# from fastapi import FastAPI, Path, Query, HTTPException, status
# from typing import Optional
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     price: float
#     brand: Optional[str] = None


# class UpdateItem(BaseModel):
#     name: Optional[str] = None
#     price: Optional[float] = None
#     brand: Optional[str] = None


# app = FastAPI()

# # @app.get("/")
# # async def home():
# #     return {"data": "Hello Samuel"}

# # @app.get("/about")
# # async def about():
# #     return {"data": "About Samuel"}

# # path/query endpoint parameters

# # inventory= {
# #     1:{
# #         "ID": 1,
# #         "name": "Milk",
# #         "price": 3.99,
# #         "brand": "Nido"
# #     },
# #     2:{
# #         "ID": 2,
# #         "name": "T-Shirt",
# #         "price": 30.89,
# #         "brand": "Adidas"
# #     },
# #     3:{
# #         "ID": 3,
# #         "name": "Sneaker",
# #         "price": 13.59,
# #         "brand": "Nike"
# #     }
# # }

# inventory= {}


# # using the single and multiple path parameter as well as type hint
# @app.get("/get-item/{item_id}/{name}")
# async def get_item(item_id: int, name: str = None):
#     return inventory[item_id]

# # http://127.0.0.1:8000/get-item/1/name=Milk
# # single parameter http://127.0.0.1:8000/get-item/1
  
# # adding more details to an item using the path function or path parameter 
# # and adding constraints to the description
# @app.get("/get-item-details/{item_id}")
# def get_item_details(item_id: int = Path(info="The ID of the item you'd like to view.", gt=0, lt=3)):
#     return inventory[item_id]

# # # query parameters is something that comes 
# # after the question mark in a url ex: "facebook.com/home?redirect=/sam&msg=fail"
# @app.get("/get-by-brand")
# def get_item_by_brand(name: str, brand: str):
#     for item_id in inventory:
#         if inventory[item_id]["brand"] == brand:
#             return inventory[item_id]
#     raise HTTPException(status_code=404, detail="Item brand not found. please verify item brand.")

# # with in the query parameter we have a require field. if we want to be optional, we can set the variable type to None or we can import the Optional package from the typing module. this method is advisable from the fastapi docs as well as giving a better auto completion http://127.0.0.1:8000/get-by-brand?brand=Nido&name=Milk


# # it's recomemded from the fastapi doc that you import the optional package whenever you have an optional parameter. 
# # calling the require parameter http://127.0.0.1:8000/get-by-name?test=2&name=Milk
# # @app.get("/get-by-name/{item_id}")
# # def get_item(*, item_id: int, name: Optional[str] = None, test: int):
# #     for item_id in inventory:
# #         if inventory[item_id]["name"] == name:
# #             return inventory[item_id]
# #     return {"Data": "Not found"}
# # http://127.0.0.1:8000/get-by-name?test=1&name=T-Shirt
# # allow the above route to accept path parameter, optional query parameter and the mandatory test parameter
# @app.get("/get-by-name")
# def get_item_by_name(*, name: str =  Query(None, title = "Name", description="Name of item."),):
#     for item_id in inventory:
#         if inventory[item_id].name == name:
#             return inventory[item_id]
#     raise HTTPException(status_code=404, detail="Item name not found")

# # request body and the post method
# # When sending information to a database, you are not going to be sending the information as a path or query parameter, but you are going to be sending a bunch of information known as a request body.

# @app.post("/create-item/{item_id}")
# def create_item(item_id: int, item: Item):
#     if item_id in inventory:
#            raise HTTPException(status_code=400, detail="Item ID already exist")

    
#     inventory[item_id] = item
#     return inventory[item_id]


# # using the put method to update items
# @app.put("/update-item/{item_id}") 
# def update_item(item_id: int, item: UpdateItem):
#      if item_id not in inventory:
#             raise HTTPException(status_code=404, detail="Item ID does not exist")

     
#      if item.name != None:
#         inventory[item_id].name = item.name

#      if item.price != None:
#         inventory[item_id].price = item.price

#      if item.brand != None:
#         inventory[item_id].brand = item.brand

#      return inventory[item_id]


# # using the delete method to remove items
# @app.delete("/delete-item")
# def delete_item(item_id: int = Query(..., description="The ID of the item to delete", gt=0)):
#    if item_id not in inventory:
#         raise HTTPException(status_code=404, detail="Item ID does not exist")
#    del inventory[item_id]
#    raise HTTPException(status_code=200, detail="Item deleted successfully")



# # return status codes and error responses from these endpoints



# @app.get("/items/{item_id}/{name}")
# def fetch_items(item_id: int, name: str):
#     return inventory[item_id]