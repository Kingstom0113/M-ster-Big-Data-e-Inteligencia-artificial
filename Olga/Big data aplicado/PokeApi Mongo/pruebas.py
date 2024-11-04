from pymongo import MongoClient
import requests

# Conexión a MongoDB Atlas
uri = "mongodb+srv://manuelsr0113:Firmamento.34@cluster0.aztgaop.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['PokeApi']  # Base de datos llamada 'PokeApi'

# Verificación de conexión (opcional)
try:
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB Atlas")
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

# Función para insertar regiones y almacenar sus IDs
def insert_regions():
    regions = [
        {'name': 'Kanto'},
        {'name': 'Johto'},
        {'name': 'Hoenn'},
        {'name': 'Sinnoh'},
        {'name': 'Unova'},
        {'name': 'Kalos'},
        {'name': 'Alola'},
        {'name': 'Galar'}
    ]
    # Insertar regiones y almacenar sus IDs
    result = regions_collection.insert_many(regions)
    print("Regiones agregadas.")
    return {region['name']: {'id': region_id, 'name': region['name']} for region_id, region in zip(result.inserted_ids, regions)}

# Función para insertar entrenadores
def insert_trainers(region_ids):
    trainers_collection.insert_many([
        {'name': 'Ash Ketchum', 'region': region_ids['Kanto'], 'pokemons': ['Pikachu', 'Charizard']},
        {'name': 'Misty', 'region': region_ids['Kanto'], 'pokemons': ['Starmie', 'Psyduck']},
        {'name': 'Brock', 'region': region_ids['Kanto'], 'pokemons': ['Onix', 'Geodude']}
    ])
    print("Entrenadores agregados.")

# Función para insertar profesores
def insert_professors(region_ids):
    professors_collection.insert_many([
        {'name': 'Professor Oak', 'region': region_ids['Kanto'], 'specialty': 'Pokemon Research'},
        {'name': 'Professor Elm', 'region': region_ids['Johto'], 'specialty': 'Evolution Research'},
        {'name': 'Professor Birch', 'region': region_ids['Hoenn'], 'specialty': 'Pokemon Habitats'}
    ])
    print("Profesores agregados.")

# Ejemplo de cómo usar estas funciones
region_ids = insert_regions()  # Llamar primero a insert_regions para obtener los IDs
insert_trainers(region_ids)     # Luego insertar entrenadores
insert_professors(region_ids)   # Finalmente insertar profesores


# Función para insertar gimnasios
def insert_gyms(region_ids):
    gyms_data = [
        {
            'region': region_ids['Kanto'],  # Referenciando la región por ID y nombre
            'gyms': [
                {'name': 'Pewter City Gym', 'leader': 'Brock', 'type': 'Rock'},
                {'name': 'Cerulean City Gym', 'leader': 'Misty', 'type': 'Water'},
                {'name': 'Vermilion City Gym', 'leader': 'Lieutenant Surge', 'type': 'Electric'},
                {'name': 'Celadon City Gym', 'leader': 'Erika', 'type': 'Grass'},
                {'name': 'Fuchsia City Gym', 'leader': 'Koga', 'type': 'Poison'},
                {'name': 'Viridian City Gym', 'leader': 'Giovanni', 'type': 'Ground'},
                {'name': 'Saffron City Gym', 'leader': 'Sabrina', 'type': 'Psychic'},
                {'name': 'Cinnabar Island Gym', 'leader': 'Blane', 'type': 'Fire'}
            ]
        },
        {
            'region': region_ids['Johto'],  # Referenciando la región por ID y nombre
            'gyms': [
                {'name': 'Violet City Gym', 'leader': 'Falkner', 'type': 'Flying'},
                {'name': 'Azalea Town Gym', 'leader': 'Bugsy', 'type': 'Bug'},
                {'name': 'Goldenrod City Gym', 'leader': 'Whitney', 'type': 'Normal'},
                {'name': 'Ecruteak City Gym', 'leader': 'Morty', 'type': 'Ghost'},
                {'name': 'Mahogany Town Gym', 'leader': 'Pryce', 'type': 'Ice'},
                {'name': 'Olivine City Gym', 'leader': 'Ampharos', 'type': 'Electric'},
                {'name': 'Cianwood City Gym', 'leader': 'Chuck', 'type': 'Fighting'},
                {'name': 'Blackthorn City Gym', 'leader': 'Clair', 'type': 'Dragon'}
            ]
        },
        {
            'region': region_ids['Hoenn'],  # Referenciando la región por ID y nombre
            'gyms': [
                {'name': 'Rustboro City Gym', 'leader': 'Roark', 'type': 'Rock'},
                {'name': 'Dewford Town Gym', 'leader': 'Brawly', 'type': 'Fighting'},
                {'name': 'Slateport City Gym', 'leader': 'Flannery', 'type': 'Fire'},
                {'name': 'Mauville City Gym', 'leader': 'Wattson', 'type': 'Electric'},
                {'name': 'Verdanturf Town Gym', 'leader': 'Wattson', 'type': 'Normal'},
                {'name': 'Lavaridge Town Gym', 'leader': 'Flannery', 'type': 'Fire'},
                {'name': 'Fortree City Gym', 'leader': 'Winona', 'type': 'Flying'},
                {'name': 'Sootopolis City Gym', 'leader': 'Wallace', 'type': 'Water'},
                {'name': 'Ever Grande City Gym', 'leader': 'Steven', 'type': 'Steel'}
            ]
        }
    ]

    print("Gimnasios agregados.")

# Función para obtener Team Rocket (estáticos porque no hay API)
def insert_team_rockets():
    teamrockets_collection.insert_many([
        {'name': 'Jessie', 'role': 'Member', 'age': 29},
        {'name': 'James', 'role': 'Member', 'age': 31},
        {'name': 'Meowth', 'role': 'Mascot', 'age': 5}
    ])
    print("Team Rocket agregado.")


# Función para obtener todos los Pokémon y sus detalles, incluyendo ataques
def get_pokemons(type_ids):
    url = 'https://pokeapi.co/api/v2/pokemon'
    offset = 0
    limit = 100  

    while True:
        response = requests.get(f"{url}?limit={limit}&offset={offset}").json()
        if not response['results']:
            break

        for pokemon in response['results']:
            poke_details = requests.get(pokemon['url']).json()
            pokemon_types = [
                {
                    'id': type_ids[t['type']['name'].capitalize()],  # Almacenar el ID del tipo
                    'name': t['type']['name'].capitalize()  # Almacenar el nombre del tipo
                } for t in poke_details['types']
            ]

            # Obtener los movimientos del Pokémon
            pokemon_moves = []
            for move in poke_details['moves']:
                move_details = requests.get(move['move']['url']).json()
                pokemon_moves.append({
                    'id': move_details['id'],  # ID del movimiento
                    'name': move_details['name']  # Nombre del movimiento
                })

            # Insertar Pokémon en la colección
            pokemons_collection.insert_one({
                'name': poke_details['name'],
                'height': poke_details['height'],
                'weight': poke_details['weight'],
                'types': pokemon_types,  # Almacenar la lista de tipos como objetos
                'stats': {stat['stat']['name']: stat['base_stat'] for stat in poke_details['stats']},
                'abilities': [ability['ability']['name'] for ability in poke_details['abilities']],
                'moves': pokemon_moves  # Almacenar los movimientos como una lista de objetos
            })
        
        offset += limit  # Aumentar el offset para la próxima página

    print("Pokémon agregados.")

# Ejecución de funciones
types_dict = get_types()  # Obtener tipos y guardarlos en el diccionario
get_pokemons(types_dict)  # Obtener Pokémon usando el diccionario de tipos
get_moves()  # Obtener movimientos
insert_trainers(region_ids)  # Inserta entrenadores
insert_professors(region_ids)  # Inserta profesores
region_ids = insert_regions()  # Inserta regiones
insert_gyms(region_ids)  # Inserta gimnasios
insert_team_rockets()  # Inserta Team Rocket

