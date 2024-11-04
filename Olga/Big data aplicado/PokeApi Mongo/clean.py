from pymongo import MongoClient

# Conéctate a la base de datos
uri = "mongodb+srv://manuelsr0113:Firmamento.34@cluster0.aztgaop.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

# Selecciona la base de datos
db = client['PokeApi']  # Cambia 'PokeApi' por el nombre de tu base de datos

# Itera sobre cada colección en la base de datos
for collection_name in db.list_collection_names():
    collection = db[collection_name]
    # Borra todos los documentos de la colección
    result = collection.delete_many({})
    print(f"Borrados {result.deleted_count} documentos de la colección '{collection_name}'.")

# Cierra la conexión
client.close()
