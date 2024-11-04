from pymongo import MongoClient

uri = "mongodb+srv://manuelsr0113:Firmamento.34@cluster0.aztgaop.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    # Intenta acceder a la base de datos
    db = client['PokeApi']
    print("Conexión exitosa a la base de datos!")
except Exception as e:
    print(f"Error de conexión: {e}")