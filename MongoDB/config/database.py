from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.3xg80hx.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db
collection = db.todo_collection