import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client["myDB"]
    collection = db["data"]
    
    rec = {"name": "John"}
    ups = collection.delete_many(rec)
    print(ups.deleted_count)