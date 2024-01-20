from fastapi import FastAPI as fastapi
from pymongo.mongo_client import MongoClient
from routes.route import router

app = fastapi()

app.include_router(router)