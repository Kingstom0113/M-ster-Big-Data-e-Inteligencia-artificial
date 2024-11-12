from pymongo import MongoClient

# Conexión a MongoDB Atlas
uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client['PokeApi']

# Verificación de conexión (opcional)
try:
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB")
except Exception as e:
    print("Error de conexión:", e)

# Colecciones de MongoDB
types_collection = db['types']
pokemons_collection = db['pokemons']
attacks_collection = db['attacks']
trainers_collection = db['trainers']
professors_collection = db['professors']
regions_collection = db['regions']
gyms_collection = db['gyms']
teamrockets_collection = db['teamrockets']

def insert_regions():
    # Verificar si ya existen regiones en la colección
    if regions_collection.count_documents({}) > 0:
        print("Las regiones ya existen en la base de datos.")
    else:
        regions = [
            {'name': 'Kanto'},
            {'name': 'Johto'},
            {'name': 'Hoenn'},
            {'name': 'Sinnoh'},
            {'name': 'Unova'},
            {'name': 'Kalos'},
            {'name': 'Alola'},
            {'name': 'Galar'},
            {'name': 'Paldea'},
            {'name': 'Isshu'}
        ]
        regions_collection.insert_many(regions)
        print("Regiones agregadas.")
    
    # Retornar los IDs de las regiones
    regions = regions_collection.find({}, {"name": 1})
    return {region['name']: region['_id'] for region in regions}

# Llamada a la función
region_ids = insert_regions()