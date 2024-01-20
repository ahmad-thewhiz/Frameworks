import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # db = client["myDB"]
    # collection = db["data"]
    
    # print(client, db, collection)
    
    allDBs = client.list_database_names()
    print(allDBs)
    
    coll = client[allDBs[3]]
    print(coll.list_collection_names())
    
    