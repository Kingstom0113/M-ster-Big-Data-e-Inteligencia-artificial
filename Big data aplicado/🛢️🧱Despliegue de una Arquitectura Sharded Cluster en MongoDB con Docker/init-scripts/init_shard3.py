from pymongo import MongoClient
import time

time.sleep(10)
client = MongoClient("mongodb://shard1a:27018")
config = {
    "_id": "shard1RS",
    "members": [
        {"_id": 0, "host": "shard1a:27018"},
        {"_id": 1, "host": "shard1b:27018"},
        {"_id": 2, "host": "shard1c:27018"},
    ]
}
client.admin.command("replSetInitiate", config)
print("✅ Shard1 ReplicaSet iniciado")
