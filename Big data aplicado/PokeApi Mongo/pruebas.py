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
        {'name': 'Galar'},
        {'name': 'Paldea'},
        {'name': 'Isshu'}
    ]
    # Insertar regiones y almacenar sus IDs
    result = regions_collection.insert_many(regions)
    print("Regiones agregadas.")
    return {region['name']: {'id': region_id, 'name': region['name']} for region_id, region in zip(result.inserted_ids, regions)}

# Función para insertar entrenadores
def insert_trainers(region_ids):
    trainers_collection.insert_many([
    {'name': 'Gary Oak', 'region': region_ids['Kanto'], 'pokemons': ['Blastoise', 'Electivire']},
    {'name': 'May', 'region': region_ids['Hoenn'], 'pokemons': ['Torchic', 'Beautifly']},
    {'name': 'Dawn', 'region': region_ids['Sinnoh'], 'pokemons': ['Piplup', 'Buneary']},
    {'name': 'Serena', 'region': region_ids['Kalos'], 'pokemons': ['Fennekin', 'Sylveon']},
    {'name': 'Clemont', 'region': region_ids['Kalos'], 'pokemons': ['Luxray', 'Magneton']},
    {'name': 'Cynthia', 'region': region_ids['Sinnoh'], 'pokemons': ['Garchomp', 'Togekiss']},
    {'name': 'Lysandre', 'region': region_ids['Kalos'], 'pokemons': ['Mega Gyarados', 'Mienfoo']},
    {'name': 'Leon', 'region': region_ids['Galar'], 'pokemons': ['Charizard', 'Aegislash']},
    {'name': 'Marnie', 'region': region_ids['Galar'], 'pokemons': ['Morgrem', 'Toxicroak']},
    {'name': 'Rosa', 'region': region_ids['Unova'], 'pokemons': ['Snivy', 'Musharna']},
    {'name': 'N', 'region': region_ids['Unova'], 'pokemons': ['Zekrom', 'Reshiram']},
    {'name': 'Flannery', 'region': region_ids['Hoenn'], 'pokemons': ['Torkoal', 'Slugma']},
    {'name': 'Wallace', 'region': region_ids['Hoenn'], 'pokemons': ['Swampert', 'Gyarados']},
    {'name': 'Blue', 'region': region_ids['Kanto'], 'pokemons': ['Rhydon', 'Arcanine']},
    {'name': 'Koga', 'region': region_ids['Kanto'], 'pokemons': ['Weezing', 'Muk']},
    {'name': 'Sabrina', 'region': region_ids['Kanto'], 'pokemons': ['Alakazam', 'Mr. Mime']},
    {'name': 'Giovanni', 'region': region_ids['Kanto'], 'pokemons': ['Rhydon', 'Nidoking']},
    {'name': 'Whitney', 'region': region_ids['Johto'], 'pokemons': ['Miltank', 'Clefairy']},
    {'name': 'Clair', 'region': region_ids['Johto'], 'pokemons': ['Kingdra', 'Dragonair']},
    {'name': 'Chuck', 'region': region_ids['Johto'], 'pokemons': ['Poliwrath', 'Primeape']},
    {'name': 'Misty', 'region': region_ids['Kanto'], 'pokemons': ['Starmie', 'Psyduck']},
    {'name': 'Giovanni', 'region': region_ids['Kanto'], 'pokemons': ['Rhydon', 'Nidoking']},
    {'name': 'Blaine', 'region': region_ids['Kanto'], 'pokemons': ['Arcanine', 'Rapidash']},
    {'name': 'Erika', 'region': region_ids['Kanto'], 'pokemons': ['Vileplume', 'Tangela']},
    {'name': 'Koga', 'region': region_ids['Kanto'], 'pokemons': ['Muk', 'Weezing']},
    {'name': 'Sabrina', 'region': region_ids['Kanto'], 'pokemons': ['Mr. Mime', 'Alakazam']},
    {'name': 'Roxanne', 'region': region_ids['Hoenn'], 'pokemons': ['Geodude', 'Nosepass']},
    {'name': 'Liza', 'region': region_ids['Hoenn'], 'pokemons': ['Lunatone', 'Solrock']},
    {'name': 'Tate', 'region': region_ids['Hoenn'], 'pokemons': ['Solrock', 'Lunatone']},
    {'name': 'Juan', 'region': region_ids['Hoenn'], 'pokemons': ['Swampert', 'Gyarados']},
    {'name': 'Gardenia', 'region': region_ids['Sinnoh'], 'pokemons': ['Torterra', 'Roserade']},
    {'name': 'Fantina', 'region': region_ids['Sinnoh'], 'pokemons': ['Mismagius', 'Gengar']},
    {'name': 'Byron', 'region': region_ids['Sinnoh'], 'pokemons': ['Steelix', 'Bastiodon']},
    {'name': 'Candice', 'region': region_ids['Sinnoh'], 'pokemons': ['Abomasnow', 'Piloswine']},
    {'name': 'Roark', 'region': region_ids['Sinnoh'], 'pokemons': ['Onix', 'Cranidos']},
    {'name': 'Volkner', 'region': region_ids['Sinnoh'], 'pokemons': ['Luxray', 'Electivire']},
    {'name': 'Alain', 'region': region_ids['Kalos'], 'pokemons': ['Charizard', 'Magnezone']},
    {'name': 'Ash', 'region': region_ids['Kanto'], 'pokemons': ['Pikachu', 'Charizard']},
    {'name': 'Leon', 'region': region_ids['Galar'], 'pokemons': ['Charizard', 'Aegislash']},
    {'name': 'Diantha', 'region': region_ids['Kalos'], 'pokemons': ['Gardevoir', 'Talonflame']},
    {'name': 'Zinnia', 'region': region_ids['Hoenn'], 'pokemons': ['Salamence', 'Altaria']},
    {'name': 'Wally', 'region': region_ids['Hoenn'], 'pokemons': ['Ralts', 'Gardevoir']},
    {'name': 'Hugh', 'region': region_ids['Unova'], 'pokemons': ['Oshawott', 'Pignite']},
    {'name': 'Yancy', 'region': region_ids['Unova'], 'pokemons': ['Emolga', 'Vanilluxe']},
    {'name': 'Tierno', 'region': region_ids['Kalos'], 'pokemons': ['Squirtle', 'Seaking']},
    {'name': 'Shauna', 'region': region_ids['Kalos'], 'pokemons': ['Chespin', 'Sylveon']},
    {'name': 'Alola Champion', 'region': region_ids['Alola'], 'pokemons': ['Decidueye', 'Toxapex']},
    {'name': 'Lillie', 'region': region_ids['Alola'], 'pokemons': ['Nebby', 'Vikavolt']},
    {'name': 'Olivia', 'region': region_ids['Alola'], 'pokemons': ['Lycanroc', 'Tyranitar']},
    {'name': 'Mallow', 'region': region_ids['Alola'], 'pokemons': ['Tsareena', 'Lurantis']},
    {'name': 'Kiawe', 'region': region_ids['Alola'], 'pokemons': ['Torkoal', 'Charizard']},
    {'name': 'Sina', 'region': region_ids['Kalos'], 'pokemons': ['Garchomp', 'Mamoswine']},
    {'name': 'Misty', 'region': region_ids['Kanto'], 'pokemons': ['Starmie', 'Psyduck']},
    {'name': 'Blaine', 'region': region_ids['Kanto'], 'pokemons': ['Rapidash', 'Arcanine']}
])

    print("Entrenadores agregados.")

# Función para insertar profesores
def insert_professors(region_ids):
    professors_collection.insert_many([
    {'name': 'Professor Rowan', 'region': region_ids['Sinnoh'], 'specialty': 'Pokemon Evolution'},
    {'name': 'Professor Kukui', 'region': region_ids['Alola'], 'specialty': 'Pokemon Moves and Battle Strategies'},
    {'name': 'Professor Sycamore', 'region': region_ids['Kalos'], 'specialty': 'Mega Evolution'},
    {'name': 'Professor Magnolia', 'region': region_ids['Galar'], 'specialty': 'Dynamax and Gigantamax Phenomena'},
    {'name': 'Professor Willow', 'region': region_ids['Unova'], 'specialty': 'Pokemon Biology'},
    {'name': 'Professor Juniper', 'region': region_ids['Unova'], 'specialty': 'Genetics and Evolution'},
    {'name': 'Professor Oakley', 'region': region_ids['Kanto'], 'specialty': 'Shadow Pokemon Research'},
    {'name': 'Professor Aspen', 'region': region_ids['Sinnoh'], 'specialty': 'Regional Pokemon Species'},
    {'name': 'Professor Oakridge', 'region': region_ids['Paldea'], 'specialty': 'Artificial Pokemon Intelligence'},
    {'name': 'Professor Pine', 'region': region_ids['Johto'], 'specialty': 'Pokemon Ecology'},
    {'name': 'Professor Larch', 'region': region_ids['Sinnoh'], 'specialty': 'Ancient Pokemon Fossils'},
    {'name': 'Professor Burnet', 'region': region_ids['Alola'], 'specialty': 'Ultra Beasts and Alternate Dimensions'},
    {'name': 'Professor Cedric Juniper', 'region': region_ids['Unova'], 'specialty': 'Research on the Unova Region’s Legendary Pokemon'},
    {'name': 'Professor Bambo', 'region': region_ids['Kanto'], 'specialty': 'Pokemon Species of Torren Region'},
    {'name': 'Professor Kettler', 'region': region_ids['Kanto'], 'specialty': 'Behavioral Studies in Pokemon'},
    {'name': 'Professor Radley', 'region': region_ids['Galar'], 'specialty': 'Gigantamaxing Research'},
    {'name': 'Professor Hala', 'region': region_ids['Alola'], 'specialty': 'Island Trials and Traditional Pokemon Training'},
    {'name': 'Professor Burbank', 'region': region_ids['Isshu'], 'specialty': 'Pokemon Genetics and Species Mapping'},
    {'name': 'Professor Tsu', 'region': region_ids['Kalos'], 'specialty': 'Pokemon Breeding and Crossbreeding'},
    {'name': 'Professor Ainsley', 'region': region_ids['Hoenn'], 'specialty': 'Water-type Pokemon Behavior'},
    {'name': 'Professor Usher', 'region': region_ids['Unova'], 'specialty': 'Pokemon Adaptation to Urban Environments'},
    {'name': 'Professor Xenon', 'region': region_ids['Alola'], 'specialty': 'Alola’s Regional Variants and Evolution'},
    {'name': 'Professor Delphine', 'region': region_ids['Galar'], 'specialty': 'Research on Legendary and Mythical Pokemon'},
    {'name': 'Professor Marley', 'region': region_ids['Sinnoh'], 'specialty': 'Pokemon Intelligence and Learning'},
    {'name': 'Professor Ivy', 'region': region_ids['Johto'], 'specialty': 'Pokémon Reproduction and Hybridization'},
    {'name': 'Professor Frida', 'region': region_ids['Sinnoh'], 'specialty': 'Species Ecology and Conservation'},
    {'name': 'Professor Viera', 'region': region_ids['Alola'], 'specialty': 'Environmental Impact of Pokemon in Alola'},
    {'name': 'Professor Thorne', 'region': region_ids['Hoenn'], 'specialty': 'Pokemon Communication'},
    {'name': 'Professor Akira', 'region': region_ids['Kalos'], 'specialty': 'Understanding Mega Evolutions'},
    {'name': 'Professor Alden', 'region': region_ids['Sinnoh'], 'specialty': 'The Study of Legendary Pokemon'},
    {'name': 'Professor Constantine', 'region': region_ids['Galar'], 'specialty': 'Dynamax Phenomena and Strategy'},
    {'name': 'Professor Maris', 'region': region_ids['Kanto'], 'specialty': 'Researching the Behavior of Psychic-Type Pokemon'},
    {'name': 'Professor Nia', 'region': region_ids['Unova'], 'specialty': 'Pokemon Behaviour and Interaction with Humans'},
    {'name': 'Professor Opal', 'region': region_ids['Galar'], 'specialty': 'Fairy-Type Pokemon Research'},
    {'name': 'Professor Rose', 'region': region_ids['Galar'], 'specialty': 'Energy Sources and their Impact on Pokemon'},
    {'name': 'Professor Mapache', 'region': region_ids['Alola'], 'specialty': 'Pokemon Evolution in Unique Environments'},
    {'name': 'Professor Peridot', 'region': region_ids['Johto'], 'specialty': 'Geographic Distribution of Pokemon'},
    {'name': 'Professor Ramona', 'region': region_ids['Hoenn'], 'specialty': 'Regional Ecology of the Hoenn Region'},
    {'name': 'Professor Bellamy', 'region': region_ids['Kalos'], 'specialty': 'Mechanisms of Pokemon Bonding'},
    {'name': 'Professor Merle', 'region': region_ids['Sinnoh'], 'specialty': 'The Study of Steel-Type Pokemon'},
    {'name': 'Professor Corrine', 'region': region_ids['Unova'], 'specialty': 'The Relationship Between Pokemon and Trainers'},
    {'name': 'Professor Daley', 'region': region_ids['Galar'], 'specialty': 'Researching the Effects of Dynamaxing on Pokemon and Trainers'},
    {'name': 'Professor Noctis', 'region': region_ids['Johto'], 'specialty': 'Nighttime Behavior and Research of Pokemon'},
    {'name': 'Professor Remy', 'region': region_ids['Kalos'], 'specialty': 'Advanced Technology in Pokemon Research'},
    {'name': 'Professor Sybil', 'region': region_ids['Hoenn'], 'specialty': 'The Connection Between Psychic-Type and Dragon-Type Pokemon'},
    {'name': 'Professor Tilly', 'region': region_ids['Alola'], 'specialty': 'Study of Mythical and Legendary Pokemon'},
    {'name': 'Professor Atlas', 'region': region_ids['Sinnoh'], 'specialty': 'Research of Ice-Type and Mountain Pokemon'},
    {'name': 'Professor Lux', 'region': region_ids['Kalos'], 'specialty': 'Electric-Type Pokemon Research'},
    {'name': 'Professor Iris', 'region': region_ids['Unova'], 'specialty': 'Dragon-Type Pokemon Research'},
    {'name': 'Professor Vega', 'region': region_ids['Galar'], 'specialty': 'Specialization in Star and Meteorite Pokemon'},
    {'name': 'Professor Alistair', 'region': region_ids['Kanto'], 'specialty': 'Psychic-Type and its Influence on Evolution'},
    {'name': 'Professor Remington', 'region': region_ids['Hoenn'], 'specialty': 'Mapping Pokemon Species in the Hoenn Region'},
    {'name': 'Professor Lucille', 'region': region_ids['Sinnoh'], 'specialty': 'Pokemon Breeding and Crossbreeding'},
    {'name': 'Professor Dexter', 'region': region_ids['Alola'], 'specialty': 'The Impact of Alola’s Regional Changes on Pokemon'},
    {'name': 'Professor Wilfred', 'region': region_ids['Johto'], 'specialty': 'The Evolution of Electric-Type Pokemon'},
    {'name': 'Professor Hunter', 'region': region_ids['Galar'], 'specialty': 'The Study of Rare and Unusual Pokemon'},
    {'name': 'Professor Oren', 'region': region_ids['Kalos'], 'specialty': 'Research of Fossil Pokemon'},
    {'name': 'Professor Ashford', 'region': region_ids['Sinnoh'], 'specialty': 'The Impact of Climate on Pokemon Evolution'},
    {'name': 'Professor Noelle', 'region': region_ids['Hoenn'], 'specialty': 'Ecosystem Interactions Between Pokemon'},
    {'name': 'Professor Ramiro', 'region': region_ids['Alola'], 'specialty': 'Pokemon Habitat and Geography'},
    {'name': 'Professor Harlan', 'region': region_ids['Galar'], 'specialty': 'Research on Wild Pokemon Behavior'},
    {'name': 'Professor Celia', 'region': region_ids['Johto'], 'specialty': 'The Study of Grass-Type Pokemon'},
    {'name': 'Professor Lilith', 'region': region_ids['Kalos'], 'specialty': 'Research on Water-Type Pokemon'},
    {'name': 'Professor Tannis', 'region': region_ids['Sinnoh'], 'specialty': 'Pokemon Metabolism and Growth Patterns'},
    {'name': 'Professor Ogle', 'region': region_ids['Unova'], 'specialty': 'Research on Pokemon Consciousness'},
    {'name': 'Professor Esperanza', 'region': region_ids['Hoenn'], 'specialty': 'Study of Electric-Type Pokemon Behavior'},
    {'name': 'Professor Alda', 'region': region_ids['Galar'], 'specialty': 'Interaction of Steel-Type and Fighting-Type Pokemon'},
    {'name': 'Professor Wilda', 'region': region_ids['Kalos'], 'specialty': 'Research on Fairy-Type Pokemon'},
    {'name': 'Professor Tessa', 'region': region_ids['Alola'], 'specialty': 'Research on the Alola Region’s Legendary Pokemon'}
])

    print("Profesores agregados.")

# Ejemplo de cómo usar estas funciones
region_ids = insert_regions()  # Llamar primero a insert_regions para obtener los IDs
insert_trainers(region_ids)     # Luego insertar entrenadores
insert_professors(region_ids)   # Finalmente insertar profesores




def insert_gyms(region_ids):
    # Lista de datos de los gimnasios por región
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
        # Añadir datos para las demás regiones (Hoenn, Sinnoh, Unova, etc.)
    ]

    # Insertar los gimnasios en la colección
    for gym_data in gyms_data:
        # Insertar los gimnasios de cada región
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

def get_pokedex():
    url = 'https://pokeapi.co/api/v2/pokemon'
    pokedex = []
    while url:
        response = requests.get(url)
        data = response.json()

        # Añadir cada Pokémon y su número de la Pokédex a la lista
        for pokemon in data["results"]:
            # Obtener el ID del Pokémon desde la URL de la respuesta
            pokemon_id = pokemon["url"].split("/")[-2]
            pokedex.append({"name": pokemon["name"], "number": int(pokemon_id)})

        # Obtener la siguiente página de resultados
        url = data["next"]

    return pokedex

# Obtener la lista de Pokémon con su número en la Pokédex
pokedex = get_pokedex()

# Recorremos todos los Pokémon en la Pokédex y actualizamos sus números en la base de datos
for pokemon_info in pokedex:
    pokemon_name = pokemon_info["name"]
    pokemon_number = pokemon_info["number"]

    # Actualizar el Pokémon en la base de datos
    pokemons_collection.update_one(
        {"name": pokemon_name},  # Filtrar por el nombre del Pokémon
        {"$set": {"pokedex_number": pokemon_number}}  # Actualizar el campo "pokedex_number"
    )

print("Pokédex actualizada con los números.")


# Ejecución de funciones
types_dict = get_types()
get_pokemons(types_dict)
get_moves()
insert_trainers(region_ids)
insert_professors(region_ids)
region_ids = insert_regions()
insert_gyms(region_ids)
insert_team_rockets() 
insert_gyms(region_ids)