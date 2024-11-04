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

# Función para obtener todos los Pokémon y sus detalles
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
            pokemons_collection.insert_one({
                'name': poke_details['name'],
                'height': poke_details['height'],
                'weight': poke_details['weight'],
                'types': pokemon_types,  # Almacenar la lista de tipos como objetos
                'stats': {stat['stat']['name']: stat['base_stat'] for stat in poke_details['stats']},
                'abilities': [ability['ability']['name'] for ability in poke_details['abilities']]
            })
        
        offset += limit  # Aumentar el offset para la próxima página

    print("Pokémon agregados.")


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

# Función para obtener entrenadores (estáticos porque no hay API)
def insert_trainers():
    trainers_collection.insert_many([
        {'name': 'Ash Ketchum', 'region': 'Kanto', 'pokemons': ['Pikachu', 'Charizard']},
        {'name': 'Misty', 'region': 'Kanto', 'pokemons': ['Starmie', 'Psyduck']},
        {'name': 'Brock', 'region': 'Kanto', 'pokemons': ['Onix', 'Geodude']}
    ])
    print("Entrenadores agregados.")

# Función para obtener profesores (estáticos porque no hay API)
def insert_professors():
    professors_collection.insert_many([
        {'name': 'Professor Oak', 'region': 'Kanto', 'specialty': 'Pokemon Research'},
        {'name': 'Professor Elm', 'region': 'Johto', 'specialty': 'Evolution Research'},
        {'name': 'Professor Birch', 'region': 'Hoenn', 'specialty': 'Pokemon Habitats'}
    ])
    print("Profesores agregados.")

# Función para obtener regiones (estáticos porque no hay API)
def insert_regions():
    regions_collection.insert_many([
        {'name': 'Kanto', 'gyms': ['Pewter City Gym', 'Cerulean City Gym', 'Vermilion City Gym', 'Celadon City Gym', 'Fuchsia City Gym', 'Viridian City Gym', 'Saffron City Gym', 'Cinnabar Island Gym']},
        {'name': 'Johto', 'gyms': ['Violet City Gym', 'Ecruteak City Gym', 'Goldenrod City Gym', 'Azalea Town Gym', 'Mahogany Town Gym', 'Oliveine City Gym', 'Cianwood City Gym', 'Blackthorn City Gym']},
        {'name': 'Hoenn', 'gyms': ['Rustboro City Gym', 'Dewford Town Gym', 'Slateport City Gym', 'Mauville City Gym', 'Verdanturf Town Gym', 'Lavaridge Town Gym', 'Fortree City Gym', 'Sootopolis City Gym', 'Ever Grande City Gym']},
        {'name': 'Sinnoh', 'gyms': ['Oreburgh City Gym', 'Eterna City Gym', 'Veilstone City Gym', 'Pastoria City Gym', 'Hearthome City Gym', 'Canalave City Gym', 'Snowpoint City Gym', 'Sunyshore City Gym']},
        {'name': 'Unova', 'gyms': ['Striaton City Gym', 'Nacrene City Gym', 'Castelia City Gym', 'Nimbasa City Gym', 'Driftveil City Gym', 'Mistralton City Gym', 'Icirrus City Gym', 'Opelucid City Gym', 'Lentimas Town Gym', 'Humilau City Gym']},
        {'name': 'Kalos', 'gyms': ['Santalune City Gym', 'Lumiose City Gym', 'Cyllage City Gym', 'Shalour City Gym', 'Coumarine City Gym', 'Laverre City Gym', 'Snowbelle City Gym']},
        {'name': 'Alola', 'gyms': [], 'trials': ['Melemele Island Trials', 'Akala Island Trials', 'Ulaula Island Trials', 'Poni Island Trials']},
        {'name': 'Galar', 'gyms': ['Motostoke Gym', 'Turffield Gym', 'Hulbury Gym', 'Stow-on-Side Gym', 'Ballonlea Gym', 'Circhester Gym', 'Spikemuth Gym', 'Wyndon Gym']}

    ])
    print("Regiones agregadas.")

# Función para obtener gimnasios (estáticos porque no hay API)
def insert_gyms():
    gyms_collection.insert_many([
{'name': 'Kanto', 'gyms': [
    {'name': 'Pewter City Gym', 'leader': 'Brock', 'type': 'Rock'},
    {'name': 'Cerulean City Gym', 'leader': 'Misty', 'type': 'Water'},
    {'name': 'Vermilion City Gym', 'leader': 'Lieutenant Surge', 'type': 'Electric'},
    {'name': 'Celadon City Gym', 'leader': 'Erika', 'type': 'Grass'},
    {'name': 'Fuchsia City Gym', 'leader': 'Koga', 'type': 'Poison'},
    {'name': 'Viridian City Gym', 'leader': 'Giovanni', 'type': 'Ground'},
    {'name': 'Saffron City Gym', 'leader': 'Sabrina', 'type': 'Psychic'},
    {'name': 'Cinnabar Island Gym', 'leader': 'Blane', 'type': 'Fire'}
]},
{'name': 'Johto', 'gyms': [
    {'name': 'Violet City Gym', 'leader': 'Falkner', 'type': 'Flying'},
    {'name': 'Azalea Town Gym', 'leader': 'Bugsy', 'type': 'Bug'},
    {'name': 'Goldenrod City Gym', 'leader': 'Whitney', 'type': 'Normal'},
    {'name': 'Ecruteak City Gym', 'leader': 'Morty', 'type': 'Ghost'},
    {'name': 'Oliveine City Gym', 'leader': 'Ampharos', 'type': 'Electric'},
    {'name': 'Cianwood City Gym', 'leader': 'Chuck', 'type': 'Fighting'},
    {'name': 'Mahogany Town Gym', 'leader': 'Pryce', 'type': 'Ice'},
    {'name': 'Blackthorn City Gym', 'leader': 'Claire', 'type': 'Dragon'}
]},
{'name': 'Hoenn', 'gyms': [
    {'name': 'Rustboro City Gym', 'leader': 'Roark', 'type': 'Rock'},
    {'name': 'Dewford Town Gym', 'leader': 'Brawly', 'type': 'Fighting'},
    {'name': 'Slateport City Gym', 'leader': 'Wattson', 'type': 'Electric'},
    {'name': 'Mauville City Gym', 'leader': 'Flannery', 'type': 'Fire'},
    {'name': 'Verdanturf Town Gym', 'leader': 'Norman', 'type': 'Normal'},
    {'name': 'Lavaridge Town Gym', 'leader': 'Tate & Liza', 'type': 'Psychic'},
    {'name': 'Fortree City Gym', 'leader': 'Winona', 'type': 'Flying'},
    {'name': 'Sootopolis City Gym', 'leader': 'Wallace', 'type': 'Water'},
    {'name': 'Ever Grande City Gym', 'leader': 'Steven', 'type': 'Steel'}
]},
{'name': 'Sinnoh', 'gyms': [
    {'name': 'Oreburgh City Gym', 'leader': 'Roark', 'type': 'Rock'},
    {'name': 'Eterna City Gym', 'leader': 'Gardenia', 'type': 'Grass'},
    {'name': 'Veilstone City Gym', 'leader': 'Maylene', 'type': 'Fighting'},
    {'name': 'Pastoria City Gym', 'leader': 'Crasher Wake', 'type': 'Water'},
    {'name': 'Hearthome City Gym', 'leader': 'Fantina', 'type': 'Ghost'},
    {'name': 'Canalave City Gym', 'leader': 'Cyrus', 'type': 'Steel'},
    {'name': 'Snowpoint City Gym', 'leader': 'Candice', 'type': 'Ice'},
    {'name': 'Sunyshore City Gym', 'leader': 'Volkner', 'type': 'Electric'}
]},
{'name': 'Unova', 'gyms': [
    {'name': 'Striaton City Gym', 'leader': 'Cilan', 'type': 'Grass'},
    {'name': 'Nacrene City Gym', 'leader': 'Lenora', 'type': 'Normal'},
    {'name': 'Castelia City Gym', 'leader': 'Burgundy', 'type': 'Bug'},
    {'name': 'Nimbasa City Gym', 'leader': 'Elesa', 'type': 'Electric'},
    {'name': 'Driftveil City Gym', 'leader': 'Clay', 'type': 'Ground'},
    {'name': 'Mistralton City Gym', 'leader': 'Skyla', 'type': 'Flying'},
    {'name': 'Icirrus City Gym', 'leader': 'Brycen', 'type': 'Ice'},
    {'name': 'Opelucid City Gym', 'leader': 'Drayden', 'type': 'Dragon'},
    {'name': 'Lentimas Town Gym', 'leader': 'Marley', 'type': 'Ghost'},
    {'name': 'Humilau City Gym', 'leader': 'Marina', 'type': 'Water'}
]},
{'name': 'Kalos', 'gyms': [
    {'name': 'Santalune City Gym', 'leader': 'Viola', 'type': 'Bug'},
    {'name': 'Lumiose City Gym', 'leader': 'Clement', 'type': 'Electric'},
    {'name': 'Cyllage City Gym', 'leader': 'Grant', 'type': 'Rock'},
    {'name': 'Shalour City Gym', 'leader': 'Korrina', 'type': 'Fighting'},
    {'name': 'Coumarine City Gym', 'leader': 'Gina', 'type': 'Grass'},
    {'name': 'Laverre City Gym', 'leader': 'Valerie', 'type': 'Fairy'},
    {'name': 'Snowbelle City Gym', 'leader': 'Wulfric', 'type': 'Ice'}
]},
{'name': 'Alola', 'gyms': [], 'trials': [
    {'name': 'Melemele Island Trials', 'leader': 'Ilima', 'type': 'Normal'},
    {'name': 'Akala Island Trials', 'leader': 'Kiawe', 'type': 'Fire'},
    {'name': 'Ulaula Island Trials', 'leader': 'Nanu', 'type': 'Dark'},
    {'name': 'Poni Island Trials', 'leader': 'Mallow', 'type': 'Grass'}
]},
{'name': 'Galar', 'gyms': [
    {'name': 'Motostoke Gym', 'leader': 'Kabu', 'type': 'Fire'},
    {'name': 'Turffield Gym', 'leader': 'Milo', 'type': 'Grass'},
    {'name': 'Hulbury Gym', 'leader': 'Nessa', 'type': 'Water'},
    {'name': 'Stow-on-Side Gym', 'leader': 'Bee', 'type': 'Fighting'},
    {'name': 'Ballonlea Gym', 'leader': 'Opal', 'type': 'Fairy'},
    {'name': 'Circhester Gym', 'leader': 'Gordie', 'type': 'Rock'},
    {'name': 'Spikemuth Gym', 'leader': 'Piers', 'type': 'Dark'},
    {'name': 'Wyndon Gym', 'leader': 'Leon', 'type': 'Dragon'}
]}

    ])
    print("Gimnasios agregados.")

# Insertar manualmente datos de Equipo Rocket (estáticos porque no hay API)
def insert_team_rocket():
    teamrockets_collection.insert_one({
        'name': 'Team Rocket',
        'members': ['Jessie', 'James', 'Meowth'],
        'objective': 'Stealing rare Pokémon'
    })
    print("Equipo Rocket agregado.")

# Ejecutar las funciones para poblar la base de datos
get_types()
get_pokemons()
get_moves()
insert_trainers()
insert_professors()
insert_regions()
insert_gyms()
insert_team_rocket()

print("Base de datos poblada con éxito.")
