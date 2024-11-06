from pymongo import MongoClient
import requests

# Conexión a MongoDB Atlas
uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client['PokeApi']

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

    types_to_insert = []
    type_ids = {}
    for t in types:
        t['name'] = t['name'].capitalize()
        types_to_insert.append(t)  # Acumular los tipos
        result = types_collection.insert_one(t)  # Almacenar el tipo en la colección
        type_ids[t['name']] = result.inserted_id  # Asociar nombre con ID

    types_collection.insert_many(types_to_insert)  # Insertar todos de una vez
    print("Tipos de Pokémon agregados.")
    return type_ids

# Función para obtener todos los movimientos (ataques)
def get_moves():
    url = 'https://pokeapi.co/api/v2/move'
    offset = 0
    limit = 100  # Puedes ajustar esto si es necesario

    while True:
        try:
            response = requests.get(f"{url}?limit={limit}&offset={offset}").json()
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la solicitud de movimientos: {e}")
            break
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

# Función para insertar gimnasios
def insert_gyms(region_ids):
    gyms_data = [
    {
        "region": region_ids["Kanto"],
        "gyms": [
            {"name": "Pewter City Gym", "leader": "Brock", "type": "Rock"},
            {"name": "Cerulean City Gym", "leader": "Misty", "type": "Water"},
            {"name": "Vermilion City Gym", "leader": "Lieutenant Surge", "type": "Electric"},
            {"name": "Celadon City Gym", "leader": "Erika", "type": "Grass"},
            {"name": "Fuchsia City Gym", "leader": "Koga", "type": "Poison"},
            {"name": "Saffron City Gym", "leader": "Sabrina", "type": "Psychic"},
            {"name": "Cinnabar Island Gym", "leader": "Blaine", "type": "Fire"},
            {"name": "Viridian City Gym", "leader": "Giovanni", "type": "Ground"}
        ]
    },
    {
        "region": region_ids["Johto"],
        "gyms": [
            {"name": "Violet City Gym", "leader": "Falkner", "type": "Flying"},
            {"name": "Azalea Town Gym", "leader": "Bugsy", "type": "Bug"},
            {"name": "Goldenrod City Gym", "leader": "Whitney", "type": "Normal"},
            {"name": "Ecruteak City Gym", "leader": "Morty", "type": "Ghost"},
            {"name": "Cianwood City Gym", "leader": "Chuck", "type": "Fighting"},
            {"name": "Olivine City Gym", "leader": "Jasmine", "type": "Steel"},
            {"name": "Mahogany Town Gym", "leader": "Pryce", "type": "Ice"},
            {"name": "Blackthorn City Gym", "leader": "Clair", "type": "Dragon"}
        ]
    },
    {
        "region": region_ids["Hoenn"],
        "gyms": [
            {"name": "Rustboro City Gym", "leader": "Roxanne", "type": "Rock"},
            {"name": "Dewford Town Gym", "leader": "Brawly", "type": "Fighting"},
            {"name": "Slateport City Gym", "leader": "Tate & Liza", "type": "Psychic"},
            {"name": "Mauville City Gym", "leader": "Wattson", "type": "Electric"},
            {"name": "Verdanturf Town Gym", "leader": "Flannery", "type": "Fire"},
            {"name": "Fortree City Gym", "leader": "Winona", "type": "Flying"},
            {"name": "Lilycove City Gym", "leader": "Tate & Liza", "type": "Psychic"},
            {"name": "Mossdeep City Gym", "leader": "Steven Stone", "type": "Steel"}
        ]
    },
    {
        "region": region_ids["Sinnoh"],
        "gyms": [
            {"name": "Oreburgh City Gym", "leader": "Roark", "type": "Rock"},
            {"name": "Eterna City Gym", "leader": "Gardenia", "type": "Grass"},
            {"name": "Hearthome City Gym", "leader": "Fantina", "type": "Ghost"},
            {"name": "Veilstone City Gym", "leader": "Maylene", "type": "Fighting"},
            {"name": "Pastoria City Gym", "leader": "Crasher Wake", "type": "Water"},
            {"name": "Snowpoint City Gym", "leader": "Candice", "type": "Ice"},
            {"name": "Sunyshore City Gym", "leader": "Volkner", "type": "Electric"},
            {"name": "Canalave City Gym", "leader": "Byron", "type": "Steel"}
        ]
    },
    {
        "region": region_ids["Unova"],
        "gyms": [
            {"name": "Striaton City Gym", "leader": "Cilan", "type": "Grass"},
            {"name": "Nacrene City Gym", "leader": "Lenora", "type": "Normal"},
            {"name": "Castelia City Gym", "leader": "Burgh", "type": "Bug"},
            {"name": "Nimbasa City Gym", "leader": "Elesa", "type": "Electric"},
            {"name": "Driftveil City Gym", "leader": "Clay", "type": "Ground"},
            {"name": "Mistralton City Gym", "leader": "Skyla", "type": "Flying"},
            {"name": "Icirrus City Gym", "leader": "Brycen", "type": "Ice"},
            {"name": "Opelucid City Gym", "leader": "Drayden", "type": "Dragon"}
        ]
    },
    {
        "region": region_ids["Kalos"],
        "gyms": [
            {"name": "Santalune City Gym", "leader": "Viola", "type": "Bug"},
            {"name": "Cyllage City Gym", "leader": "Grant", "type": "Rock"},
            {"name": "Shalour City Gym", "leader": "Korrina", "type": "Fighting"},
            {"name": "Ambrette Town Gym", "leader": "Ramone", "type": "Water"},
            {"name": "Geosenge Town Gym", "leader": "Clemont", "type": "Electric"},
            {"name": "Coumarine City Gym", "leader": "Ramos", "type": "Grass"},
            {"name": "Lumiose City Gym", "leader": "Leona", "type": "Normal"},
            {"name": "Anistar City Gym", "leader": "Olympia", "type": "Psychic"}
        ]
    },
    {
        "region": region_ids["Alola"],
        "gyms": [
            {"name": "Kukui's Gym", "leader": "Professor Kukui", "type": "Fighting"},
            {"name": "Melemele Island Gym", "leader": "Hala", "type": "Fighting"},
            {"name": "Akala Island Gym", "leader": "Olivia", "type": "Rock"},
            {"name": "Ulaula Island Gym", "leader": "Nanu", "type": "Dark"},
            {"name": "Poni Island Gym", "leader": "Hapu", "type": "Ground"}
        ]
    },
    {
        "region": region_ids["Galar"],
        "gyms": [
            {"name": "Motostoke Gym", "leader": "Kabu", "type": "Fire"},
            {"name": "Turffield Gym", "leader": "Milton", "type": "Grass"},
            {"name": "Hulbury Gym", "leader": "Nessa", "type": "Water"},
            {"name": "Stow-on-Side Gym", "leader": "Bea", "type": "Fighting"},
            {"name": "Circhester Gym", "leader": "Gordie", "type": "Rock"},
            {"name": "Spikemuth Gym", "leader": "Marnie", "type": "Dark"},
            {"name": "Ballett Town Gym", "leader": "Raihan", "type": "Dragon"},
            {"name": "Hammerlocke Gym", "leader": "Leon", "type": "Dragon"}
        ]
    }
]


    for gym_data in gyms_data:
        region = gym_data["region"]
        gyms = gym_data["gyms"]

        for gym in gyms:
            gym["region"] = region  # Asociar el gimnasio con la región
            gyms_collection.insert_one(gym)

    print("Gimnasios agregados.")

# Función para obtener Team Rocket (estáticos porque no hay API)
def insert_team_rockets():
    teamrockets_collection.insert_many([
    {'name': 'Elise', 'role': 'Grunt', 'age': 26},
    {'name': 'Sasha', 'role': 'Agent', 'age': 27},
    {'name': 'Victor', 'role': 'Grunt', 'age': 30},
    {'name': 'Cory', 'role': 'Grunt', 'age': 24},
    {'name': 'Diana', 'role': 'Agent', 'age': 33},
    {'name': 'Ruben', 'role': 'Grunt', 'age': 22},
    {'name': 'Nikki', 'role': 'Grunt', 'age': 28},
    {'name': 'Jason', 'role': 'Agent', 'age': 35},
    {'name': 'Max', 'role': 'Grunt', 'age': 31},
    {'name': 'Alma', 'role': 'Agent', 'age': 30},
    {'name': 'Brody', 'role': 'Grunt', 'age': 32},
    {'name': 'Penny', 'role': 'Grunt', 'age': 29},
    {'name': 'Luca', 'role': 'Grunt', 'age': 26},
    {'name': 'Tessa', 'role': 'Agent', 'age': 31},
    {'name': 'Harley', 'role': 'Grunt', 'age': 30},
    {'name': 'Gavin', 'role': 'Agent', 'age': 38},
    {'name': 'Maya', 'role': 'Grunt', 'age': 25},
    {'name': 'Caleb', 'role': 'Grunt', 'age': 27},
    {'name': 'Isabella', 'role': 'Agent', 'age': 36},
    {'name': 'Henry', 'role': 'Grunt', 'age': 33},
    {'name': 'Lance', 'role': 'Agent', 'age': 31},
    {'name': 'Linda', 'role': 'Grunt', 'age': 29},
    {'name': 'Nate', 'role': 'Grunt', 'age': 28},
    {'name': 'Eliza', 'role': 'Agent', 'age': 34},
    {'name': 'Travis', 'role': 'Grunt', 'age': 26},
    {'name': 'Sophia', 'role': 'Agent', 'age': 37},
    {'name': 'Tommy', 'role': 'Grunt', 'age': 27},
    {'name': 'Eva', 'role': 'Grunt', 'age': 25},
    {'name': 'Blake', 'role': 'Agent', 'age': 34},
    {'name': 'Carla', 'role': 'Grunt', 'age': 32},
    {'name': 'Jessica', 'role': 'Grunt', 'age': 28},
    {'name': 'Ashford', 'role': 'Grunt', 'age': 29},
    {'name': 'Xander', 'role': 'Agent', 'age': 30},
    {'name': 'Tanya', 'role': 'Grunt', 'age': 26},
    {'name': 'Martin', 'role': 'Agent', 'age': 33},
    {'name': 'Kayla', 'role': 'Grunt', 'age': 27},
    {'name': 'Brett', 'role': 'Grunt', 'age': 30},
    {'name': 'Lilliana', 'role': 'Agent', 'age': 35},
    {'name': 'Zane', 'role': 'Grunt', 'age': 32},
    {'name': 'Jenna', 'role': 'Grunt', 'age': 29},
    {'name': 'Isaac', 'role': 'Agent', 'age': 38},
    {'name': 'Kendall', 'role': 'Grunt', 'age': 28},
    {'name': 'Carmen', 'role': 'Grunt', 'age': 33},
    {'name': 'Lucia', 'role': 'Grunt', 'age': 31},
    {'name': 'Dominic', 'role': 'Agent', 'age': 39},
    {'name': 'Aidan', 'role': 'Grunt', 'age': 28},
    {'name': 'Clarissa', 'role': 'Agent', 'age': 34},
    {'name': 'Alex', 'role': 'Grunt', 'age': 29},
    {'name': 'Elliot', 'role': 'Grunt', 'age': 28},
    {'name': 'Barbara', 'role': 'Agent', 'age': 32},
    {'name': 'Riley', 'role': 'Grunt', 'age': 25},
    {'name': 'Tessa', 'role': 'Grunt', 'age': 33},
    {'name': 'Mason', 'role': 'Agent', 'age': 37},
    {'name': 'Kate', 'role': 'Grunt', 'age': 32},
    {'name': 'Mark', 'role': 'Grunt', 'age': 29},
    {'name': 'Amy', 'role': 'Agent', 'age': 31},
    {'name': 'Oscar', 'role': 'Grunt', 'age': 30},
    {'name': 'Jill', 'role': 'Agent', 'age': 36},
    {'name': 'Jordan', 'role': 'Grunt', 'age': 26},
    {'name': 'Nico', 'role': 'Agent', 'age': 38},
    {'name': 'Brianna', 'role': 'Grunt', 'age': 29},
    {'name': 'Derek', 'role': 'Agent', 'age': 33},
    {'name': 'Amber', 'role': 'Grunt', 'age': 30},
    {'name': 'Xenia', 'role': 'Agent', 'age': 35},
    {'name': 'Kara', 'role': 'Grunt', 'age': 32},
    {'name': 'Dexter', 'role': 'Agent', 'age': 39},
    {'name': 'Wesley', 'role': 'Grunt', 'age': 28},
    {'name': 'Olivia', 'role': 'Agent', 'age': 34},
    {'name': 'Lucas', 'role': 'Grunt', 'age': 29},
    {'name': 'Veronica', 'role': 'Grunt', 'age': 30},
    {'name': 'Roberto', 'role': 'Agent', 'age': 37},
    {'name': 'Carla', 'role': 'Grunt', 'age': 32},
    {'name': 'Simon', 'role': 'Agent', 'age': 36},
    {'name': 'Miranda', 'role': 'Grunt', 'age': 29},
    {'name': 'Hannah', 'role': 'Grunt', 'age': 31},
    {'name': 'Raymond', 'role': 'Agent', 'age': 38},
    {'name': 'Shannon', 'role': 'Grunt', 'age': 26},
    {'name': 'Paige', 'role': 'Agent', 'age': 33},
    {'name': 'Jeff', 'role': 'Grunt', 'age': 30},
    {'name': 'Theo', 'role': 'Grunt', 'age': 29},
    {'name': 'Cory', 'role': 'Agent', 'age': 35},
    {'name': 'Nina', 'role': 'Grunt', 'age': 28},
    {'name': 'Adrian', 'role': 'Agent', 'age': 38},
    {'name': 'Phoebe', 'role': 'Grunt', 'age': 25},
    {'name': 'Helen', 'role': 'Grunt', 'age': 32},
    {'name': 'Oscar', 'role': 'Agent', 'age': 33},
    {'name': 'Cassandra', 'role': 'Grunt', 'age': 29},
    {'name': 'Emilia', 'role': 'Agent', 'age': 34},
    {'name': 'Connor', 'role': 'Grunt', 'age': 30},
    {'name': 'Ava', 'role': 'Agent', 'age': 28}
])

    print("Team Rocket agregado.")

# Función para obtener todos los Pokémon y sus detalles, incluyendo ataques
def get_pokemons(type_ids):
    url = 'https://pokeapi.co/api/v2/pokemon'
    offset = 0
    limit = 100  

    while True:
        try:
            response = requests.get(f"{url}?limit={limit}&offset={offset}").json()
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la solicitud de Pokémon: {e}")
            break

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

# Función para obtener la Pokédex
def get_pokedex():
    url = 'https://pokeapi.co/api/v2/pokedex/national/'
    response = requests.get(url).json()
    # Aquí podrías guardar la Pokédex completa si es necesario
    print("Pokédex obtenida.")

# Ejecución de funciones
types_dict = get_types()
get_pokemons(types_dict)
get_moves()
region_ids = insert_regions()
insert_trainers(region_ids)
insert_professors(region_ids)
insert_gyms(region_ids)
insert_team_rockets()
get_pokedex()