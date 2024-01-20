import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDB"]
    collection = db["data"]
    
    # one = collection.find_one({'name': 'John'})
    # print(one)
    
    # <pymongo.cursor.Cursor object at 0x000001F680E2ABD0> // this is a cursor object
    
    # alldocs = collection.find({'name': 'John'})
    # for item in alldocs:
    #     print(item)
    
    # 1 - display
    # 0 - hide
    # if anyone item is 1, then by default all other items are 0 except id which is by default 1 but we can hide it by 0
    
    # alldocs = collection.find({'name': 'John'}, {'_id': 0, 'name': 1})
    # print(alldocs.count_documents())
    # for item in alldocs:
    #     print(item)
        
    alldocs = collection.find({'name': 'John'}, {'_id': 0, 'name': 1}).limit(1)
    # print(alldocs.count_documents())
    for item in alldocs:
        print(item)
    
    # all occurrences of the people with Hannah and marks less than or equal to 80
    # alldocs = collection.find({'name': 'Hannah', "marks": {"$lte": 80}}) 
    # # print(alldocs.count_documents())
    # for item in alldocs:
    #     print(item)