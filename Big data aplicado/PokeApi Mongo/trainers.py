from pymongo import MongoClient
from regions import insert_regions

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

# Llamada a la función
region_ids = insert_regions()
insert_trainers(region_ids)
