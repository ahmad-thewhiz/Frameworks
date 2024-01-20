from fastapi import APIRouter
from model.todos import Todo
from config.database import collection
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# GET
@router.get("/")
async def get_todos():
    todos = list_serial(collection.find())
    return todos

# POST
@router.post("/")
async def post_todos(todo: Todo):
    collection.insert_one(dict(todo))
    
# PUT
@router.put("/{id}")
async def put_todos(id: str, todo: Todo):
    collection.update_one({"_id": ObjectId(id)}, {"$set": dict(todo)})
    
# DELETE   
@router.delete("/{id}") 
async def delete_todo(id: str):
    collection.delete_one({"_id": ObjectId(id)})