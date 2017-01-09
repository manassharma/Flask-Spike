__author__ = "Manas Sharma"

from pymongo import MongoClient
import os

def init():
    try:
        client = MongoClient(os.environ['MONGOLAB_URI'])
        db = client['microblogging']
        #collection = db['userlogin']
        #collection.insert({"name": "test123", "password": "test"})
    except Exception:
        print("Unable to connect to mongodb instance")

if __name__ == "__main__":
    init()
