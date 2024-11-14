from pymongo import MongoClient
import random

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
trainers_collection = db['trainers']

# Obtener todas las regiones desde la colección 'regions'
regions = list(db.regions.find({}, {"_id": 1, "name": 1}))

trainers_data= [
    {'name': 'Gary Oak', 'pokemons': ['Blastoise', 'Electivire']},
    {'name': 'May', 'pokemons': ['Torchic', 'Beautifly']},
    {'name': 'Dawn', 'pokemons': ['Piplup', 'Buneary']},
    {'name': 'Serena', 'pokemons': ['Fennekin', 'Sylveon']},
    {'name': 'Clemont', 'pokemons': ['Luxray', 'Magneton']},
    {'name': 'Cynthia', 'pokemons': ['Garchomp', 'Togekiss']},
    {'name': 'Lysandre', 'pokemons': ['Mega Gyarados', 'Mienfoo']},
    {'name': 'Leon', 'pokemons': ['Charizard', 'Aegislash']},
    {'name': 'Marnie', 'pokemons': ['Morgrem', 'Toxicroak']},
    {'name': 'Rosa', 'pokemons': ['Snivy', 'Musharna']},
    {'name': 'N', 'pokemons': ['Zekrom', 'Reshiram']},
    {'name': 'Flannery', 'pokemons': ['Torkoal', 'Slugma']},
    {'name': 'Wallace', 'pokemons': ['Swampert', 'Gyarados']},
    {'name': 'Blue', 'pokemons': ['Rhydon', 'Arcanine']},
    {'name': 'Koga', 'pokemons': ['Weezing', 'Muk']},
    {'name': 'Sabrina', 'pokemons': ['Alakazam', 'Mr. Mime']},
    {'name': 'Giovanni', 'pokemons': ['Rhydon', 'Nidoking']},
    {'name': 'Whitney', 'pokemons': ['Miltank', 'Clefairy']},
    {'name': 'Clair', 'pokemons': ['Kingdra', 'Dragonair']},
    {'name': 'Chuck', 'pokemons': ['Poliwrath', 'Primeape']},
    {'name': 'Misty', 'pokemons': ['Starmie', 'Psyduck']},
    {'name': 'Giovanni', 'pokemons': ['Rhydon', 'Nidoking']},
    {'name': 'Blaine', 'pokemons': ['Arcanine', 'Rapidash']},
    {'name': 'Erika', 'pokemons': ['Vileplume', 'Tangela']},
    {'name': 'Koga', 'pokemons': ['Muk', 'Weezing']},
    {'name': 'Sabrina', 'pokemons': ['Mr. Mime', 'Alakazam']},
    {'name': 'Roxanne', 'pokemons': ['Geodude', 'Nosepass']},
    {'name': 'Liza', 'pokemons': ['Lunatone', 'Solrock']},
    {'name': 'Tate', 'pokemons': ['Solrock', 'Lunatone']},
    {'name': 'Juan', 'pokemons': ['Swampert', 'Gyarados']},
    {'name': 'Gardenia', 'pokemons': ['Torterra', 'Roserade']},
    {'name': 'Fantina', 'pokemons': ['Mismagius', 'Gengar']},
    {'name': 'Byron', 'pokemons': ['Steelix', 'Bastiodon']},
    {'name': 'Candice', 'pokemons': ['Abomasnow', 'Piloswine']},
    {'name': 'Roark', 'pokemons': ['Onix', 'Cranidos']},
    {'name': 'Volkner', 'pokemons': ['Luxray', 'Electivire']},
    {'name': 'Alain', 'pokemons': ['Charizard', 'Magnezone']},
    {'name': 'Ash', 'pokemons': ['Pikachu', 'Charizard']},
    {'name': 'Leon', 'pokemons': ['Charizard', 'Aegislash']},
    {'name': 'Diantha', 'pokemons': ['Gardevoir', 'Talonflame']},
    {'name': 'Zinnia', 'pokemons': ['Salamence', 'Altaria']},
    {'name': 'Wally', 'pokemons': ['Ralts', 'Gardevoir']},
    {'name': 'Hugh', 'pokemons': ['Oshawott', 'Pignite']},
    {'name': 'Yancy', 'pokemons': ['Emolga', 'Vanilluxe']},
    {'name': 'Tierno', 'pokemons': ['Squirtle', 'Seaking']},
    {'name': 'Shauna', 'pokemons': ['Chespin', 'Sylveon']},
    {'name': 'Alola Champion', 'pokemons': ['Decidueye', 'Toxapex']},
    {'name': 'Lillie', 'pokemons': ['Nebby', 'Vikavolt']},
    {'name': 'Olivia', 'pokemons': ['Lycanroc', 'Tyranitar']},
    {'name': 'Mallow', 'pokemons': ['Tsareena', 'Lurantis']},
    {'name': 'Kiawe', 'pokemons': ['Torkoal', 'Charizard']},
    {'name': 'Sina', 'pokemons': ['Garchomp', 'Mamoswine']},
    {'name': 'Misty', 'pokemons': ['Starmie', 'Psyduck']},
    {'name': 'Blaine', 'pokemons': ['Rapidash', 'Arcanine']}
]

trainers = []

for region in regions:
    region_name = region['name']
    region_id = region['_id']

    for trainer in trainers_data:
        existing_trainer = trainers_collection.find_one({'name': trainer['name']})

        if not existing_trainer:
            selected_region = random.choice(regions)
            new_trainer = {
            'name': trainer['name'],
            'region': selected_region['_id'],
            'region_name': selected_region['name'],
            'pokemons': trainer['pokemons']
        }
            trainers.append(new_trainer)

# Insertar entrenadores en la colección 'trainers'
trainers_collection.insert_many(trainers)
print("Entrenadores agregados a la base de datos.")
