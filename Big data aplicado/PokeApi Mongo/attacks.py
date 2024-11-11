from pymongo import MongoClient
import requests

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

# Función para obtener todos los movimientos (ataques)
def get_moves():
    url = 'https://pokeapi.co/api/v2/move'
    offset = 0
    limit = 100  # Puedes ajustar esto si es necesario

    while True:
        response = requests.get(f"{url}?limit={limit}&offset={offset}").json()
        if not response['results']:
            break  # Salir si no hay más resultados

        for move in response['results']:
            move_details = requests.get(move['url']).json()
            attacks_collection.insert_one({
                'name': move_details['name'],
                'accuracy': move_details['accuracy'],
                'power': move_details['power'],
                'type': move_details['type']['name'] if move_details['type'] else None
            })

        offset += limit  # Aumentar el offset para la próxima página

    print("Movimientos (ataques) agregados.")

# Llamada a la función
get_moves()