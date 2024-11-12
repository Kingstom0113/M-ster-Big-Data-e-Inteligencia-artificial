from pymongo import MongoClient
import requests

# Conexión a MongoDB Atlas
uri = "mongodb://admin:admin@localhost:27017"
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

# Función para obtener tipos de Pokémon
def get_types():
    url = 'https://pokeapi.co/api/v2/type/'
    response = requests.get(url).json()
    types = response['results']

    type_ids = {}
    for t in types:
        t['name'] = t['name'].capitalize()
        result = types_collection.insert_one(t)  # Almacenar el tipo en la colección
        type_ids[t['name']] = result.inserted_id  # Asociar nombre con ID
    print("Tipos de Pokémon agregados.")
    return type_ids

# Llamada a la función
type_ids = get_types()