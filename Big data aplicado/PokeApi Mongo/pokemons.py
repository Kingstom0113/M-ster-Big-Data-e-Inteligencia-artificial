import requests
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
pokemons_collection = db['pokemons']
types_collection = db['types']  # Si necesitas almacenar los tipos de Pokémon

# Función para obtener los datos de todos los Pokémon
def fetch_and_insert_pokemons():
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon_list = []
    next_url = base_url  # URL inicial para obtener la lista de Pokémon

    while next_url:
        response = requests.get(next_url)
        data = response.json()

        # Recorremos los resultados de Pokémon de esta página
        for pokemon in data['results']:
            pokemon_data = fetch_pokemon_data(pokemon['url'])
            if pokemon_data:
                pokemon_list.append(pokemon_data)

        # Si hay una página siguiente, la obtenemos
        next_url = data['next']

    # Insertamos los Pokémon en la base de datos
    if pokemon_list:
        pokemons_collection.insert_many(pokemon_list)
        print(f"Se agregaron {len(pokemon_list)} Pokémon a la base de datos.")
    else:
        print("No se encontraron Pokémon para agregar.")

# Función auxiliar para obtener datos detallados de cada Pokémon
def fetch_pokemon_data(pokemon_url):
    response = requests.get(pokemon_url)
    if response.status_code == 200:
        data = response.json()

        # Estructura que queremos para almacenar el Pokémon
        pokemon_data = {
            'name': data['name'],
            'id': data['id'],
            'types': [type_info['type']['name'] for type_info in data['types']],  # Extraemos los tipos
            'height': data['height'],
            'weight': data['weight'],
            'abilities': [ability['ability']['name'] for ability in data['abilities']],  # Habilidades
            'moves': [move['move']['name'] for move in data['moves']],  # Movimientos
            'sprites': data['sprites']['front_default']  # Imagen del sprite
        }

        return pokemon_data
    else:
        print(f"Error al obtener los datos del Pokémon con URL: {pokemon_url}")
        return None

# Llamada a la función
if __name__ == "__main__":
    fetch_and_insert_pokemons()


