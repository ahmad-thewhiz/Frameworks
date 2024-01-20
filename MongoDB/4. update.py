import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client["myDB"]
    collection = db["data"]
    
    # prev = {"name": "Hannah"}
    # nextt = {"$set": {"address": "1234 Main St"}}
    # collection.update_one(prev, nextt)
    
    prev = {"name": "John"}
    nextt = {"$set": {"address": "23 St Petersberg Street"}}
    ups = collection.update_many(prev, nextt)
    print(ups.modified_count)