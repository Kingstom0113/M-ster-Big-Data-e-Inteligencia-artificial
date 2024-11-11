import requests
from pymongo import MongoClient

# Conexión a MongoDB
uri = "mongodb+srv://manuelsr0113:Firmamento.34@cluster0.aztgaop.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["PokeApi"]
pokemon_collection = db["pokemons"]

# Función para obtener la lista de Pokémon y sus números de la Pokédex desde la PokéAPI
def get_pokedex():
    pokedex = []
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"  # Puedes limitar a 1000 Pokémon, hay 898 en total en la Pokédex

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

    # Buscar el Pokémon en la colección
    pokemon = pokemon_collection.find_one({"name": pokemon_name})

    if pokemon:
        # Actualizamos el documento del Pokémon con el número de la Pokédex
        pokemon_collection.update_one(
            {"_id": pokemon["_id"]},
            {"$set": {"number": pokemon_number}}  # Añadimos el número de la Pokédex
        )
        print(f"Pokémon {pokemon_name} actualizado con el número {pokemon_number}.")
    else:
        print(f"Pokémon {pokemon_name} no encontrado en la base de datos.")

print("Actualización completa de los números de la Pokédex para todos los Pokémon.")
