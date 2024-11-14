import requests
from pymongo import MongoClient

# Conexión a la base de datos MongoDB
uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client['PokeApi']

# Colecciones de MongoDB
pokemons_collection = db['pokemons']
regions_collection = db['regions']
attacks_collection = db['attacks']  # Referencia a la colección 'attacks'

# Obtener todas las regiones de la colección 'regions' en MongoDB
def get_regions_from_db():
    regions = list(regions_collection.find({}, {"_id": 1, "name": 1}))
    print("Regiones obtenidas de MongoDB:", regions)  # Depuración
    return {region['_id']: region['name'] for region in regions}

# Función para obtener todos los pokemons desde la PokéAPI
def get_all_pokemons():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1302"  # URL base con un límite de 1000 Pokémon
    pokemons = []
    next_url = url
    
    while next_url:
        response = requests.get(next_url)
        data = response.json()
        
        print(f"Obteniendo datos de la página: {next_url}")  # Depuración
        
        for pokemon in data['results']:
            pokemon_data = get_pokemon_details(pokemon['url'])
            if pokemon_data:
                pokemons.append(pokemon_data)
        
        next_url = data.get('next')

    print(f"Total de Pokémon obtenidos: {len(pokemons)}")  # Depuración
    return pokemons

# Función para obtener detalles de un Pokémon específico
def get_pokemon_details(pokemon_url):
    response = requests.get(pokemon_url)
    data = response.json()
    
    # Crear el documento del Pokémon
    pokemon_document = {
        "name": data['name'],
        "id": data['id'],
        "height": data['height'],
        "weight": data['weight'],
        "types": [t['type']['name'] for t in data['types']],  # Lista de tipos
        "abilities": [a['ability']['name'] for a in data['abilities']],  # Lista de habilidades
        "stats": {stat['stat']['name']: stat['base_stat'] for stat in data['stats']},  # Estadísticas
        "moves": get_move_references(data['moves'])  # Lista de referencias a ataques
    }
    
    # Asociar la región a este Pokémon
    region_id, region_name = get_region_by_pokemon_id(data['id'])
    
    # Agregar la región al documento
    pokemon_document["region"] = {
        "id": region_id,
        "name": region_name
    }

    return pokemon_document

# Función para obtener las referencias de los movimientos desde la colección 'attacks'
def get_move_references(moves):
    move_references = []
    
    for move in moves:
        move_name = move['move']['name']
        # Buscar el movimiento en la colección 'attacks'
        attack = attacks_collection.find_one({"name": move_name})
        
        if attack:
            move_references.append({
                "id": attack['_id'],  # Agregar el _id del ataque
                "name": attack['name']  # Agregar el nombre del ataque
            })
        
    return move_references

# Función para determinar la región basada en el ID del Pokémon
def get_region_by_pokemon_id(pokemon_id):
    if 1 <= pokemon_id <= 151:
        return get_region_info("Kanto")
    elif 152 <= pokemon_id <= 251:
        return get_region_info("Johto")
    elif 252 <= pokemon_id <= 386:
        return get_region_info("Hoenn")
    elif 387 <= pokemon_id <= 493:
        return get_region_info("Sinnoh")
    elif 494 <= pokemon_id <= 649:
        return get_region_info("Unova")
    elif 650 <= pokemon_id <= 721:
        return get_region_info("Kalos")
    elif 722 <= pokemon_id <= 809:
        return get_region_info("Alola")
    elif 810 <= pokemon_id <= 898:
        return get_region_info("Galar")
    elif 899 <= pokemon_id <= 1000:
        return get_region_info("Paldea")
    elif 1001 <= pokemon_id <= 1086:
        return get_region_info("Isshu")
    else:
        return get_region_info("Unknown Region")

def get_region_info(region_name):
    region = regions_collection.find_one({"name": region_name})
    if region:
        return region['_id'], region['name']
    else:
        return None, "Unknown Region"

# Insertar los Pokémon en la base de datos
def insert_pokemons_into_db():
    pokemons = get_all_pokemons()
    
    if pokemons:
        print(f"Inserción de {len(pokemons)} Pokémon en la base de datos...")
        pokemons_collection.insert_many(pokemons)
        print(f"{len(pokemons)} Pokémon han sido agregados a la base de datos.")
    else:
        print("No se encontraron Pokémon para agregar.")

insert_pokemons_into_db()

