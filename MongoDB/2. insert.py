import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDB"]
    collection = db["data"]
    
    # collection.insert_one({"name": "John", "address": "Highway 37"})
    
    newData = [
        {
            "name": "Amy", "address": "Apple st 652"
        },
        {
            "name": "Hannah", "address": "Mountain 21"
        },
        {
            "name": "Michael", "address": "Valley 345"
        }
    ]
    
    # collection.insert_many(newData)
    
    updatedNewData = [
        {
            "_id": 1,"name": "Saj", "address": "Google st 652"
        },
        {
            "_id": 2,"name": "Maxwell", "address": "Valley 21"
        },
        {
            "_id": 3,"name": "Fedrick", "address": "Peak 345"
        }
    ]
    
    # collection.insert_many(updatedNewData)