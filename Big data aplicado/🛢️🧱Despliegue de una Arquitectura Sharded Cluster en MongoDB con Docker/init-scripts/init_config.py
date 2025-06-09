from pymongo import MongoClient
import time

time.sleep(10)
client = MongoClient("mongodb://configsvr1:27019")
config = {
    "_id": "cfgRS",
    "configsvr": True,
    "members": [
        {"_id": 0, "host": "configsvr1:27019"},
        {"_id": 1, "host": "configsvr2:27019"},
        {"_id": 2, "host": "configsvr3:27019"},
    ]
}
client.admin.command("replSetInitiate", config)
print("✅ Config ReplicaSet iniciado")
