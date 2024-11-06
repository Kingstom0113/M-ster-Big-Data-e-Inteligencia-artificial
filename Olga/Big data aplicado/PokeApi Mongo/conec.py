from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)  # Timeout de 5 segundos
    client.admin.command('ping')  # Intentar hacer un ping al servidor
    print("Conexión exitosa a MongoDB!")
except Exception as e:
    print("Error de conexión:", e)
