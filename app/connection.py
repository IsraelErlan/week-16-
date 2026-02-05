import json
from pymongo import MongoClient
from os import getenv


mongo_uri = getenv("MONGO_URI", "mongodb://localhost:27017")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")
file_path = './employee_data_advanced.json'




def connect_db(): 
    try: 
        myclient = MongoClient(mongo_uri)
        db = myclient[mongo_db]
        return db
    except Exception as e:
        raise e
    

def get_collection():
    db = connect_db()
    Collection = db[mongo_collection]
    return Collection


def init_db():
    collection = get_collection()
    with open(file_path) as file:
        file_data = json.load(file)
    ins_result = collection.insert_many(file_data)