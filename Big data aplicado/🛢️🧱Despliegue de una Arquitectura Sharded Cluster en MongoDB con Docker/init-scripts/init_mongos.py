from pymongo import MongoClient
import time

time.sleep(15)
client = MongoClient("mongodb://mongos1:27017")

# Agregar shards
client.admin.command("addShard", "shard1RS/shard1a:27018,shard1b:27018,shard1c:27018")
client.admin.command("addShard", "shard2RS/shard2a:27018,shard2b:27018,shard2c:27018")
client.admin.command("addShard", "shard3RS/shard3a:27018,shard3b:27018,shard3c:27018")

# Habilitar particionado
client.admin.command("enableSharding", "testdb")
client.admin.command("shardCollection", "testdb.testcoll", key={"_id": "hashed"})

print("✅ Shards añadidos y particionado habilitado")
