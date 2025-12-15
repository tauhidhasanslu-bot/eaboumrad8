import os
import certifi
from dotenv import load_dotenv
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

load_dotenv()

def get_dbconnection():
    uri = os.environ.get('MONGO_URI')
    client = MongoClient(
        uri,
        tls=True,
        tlsAllowInvalidCertificates=False,
        tlsCAFile=certifi.where(),
        server_api=ServerApi('1')
    )
    try:
        client.admin.command('ping')
        #print("successfully connected")
    except Exception as e:
        print(e)
    return client['naturopath_db']

if __name__ == '__main__':
    dbname = get_dbconnection()



 