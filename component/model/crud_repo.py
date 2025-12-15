import json
from bson import json_util
from component.core.db_config import get_dbconnection

client = get_dbconnection()
#print(client)

def insert(data, cl_name):
    dbname = get_dbconnection()
    collection_name = dbname[cl_name]
    response = collection_name.insert_one(data)
    id = str(response.inserted_id)
    print(id)
    return id

def get_all(cl_name, chat_id):
    dbname = get_dbconnection()
    collection = dbname[cl_name]
    cursor = collection.find({"chat_id": chat_id})
    data = json.loads(json_util.dumps(cursor))
    return data
