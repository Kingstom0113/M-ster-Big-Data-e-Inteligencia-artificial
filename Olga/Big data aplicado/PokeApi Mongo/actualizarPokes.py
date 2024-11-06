from pymongo import MongoClient

# Conexión a MongoDB
uri = "mongodb+srv://manuelsr0113:Firmamento.34@cluster0.aztgaop.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["PokeApi"]
pokemon_collection = db["pokemons"]
regions_collection = db["regions"]

# Mapeo de regiones basado en el rango de números de Pokémon
region_map = {
    "Kanto": {"id": "672a2dcf6f86a8ba93a4a727", "name": "Kanto", "pokemon_range": (1, 151)},
    "Johto": {"id": "672a2dcf6f86a8ba93a4a728", "name": "Johto", "pokemon_range": (152, 251)},
    "Hoenn": {"id": "672a2dcf6f86a8ba93a4a729", "name": "Hoenn", "pokemon_range": (252, 386)},
    "Sinnoh": {"id": "672a2dcf6f86a8ba93a4a730", "name": "Sinnoh", "pokemon_range": (387, 493)},
    "Unova": {"id": "672a2dcf6f86a8ba93a4a731", "name": "Unova", "pokemon_range": (494, 649)},
    "Kalos": {"id": "672a2dcf6f86a8ba93a4a732", "name": "Kalos", "pokemon_range": (650, 721)},
    "Alola": {"id": "672a2dcf6f86a8ba93a4a733", "name": "Alola", "pokemon_range": (722, 809)},
    "Galar": {"id": "672a2dcf6f86a8ba93a4a734", "name": "Galar", "pokemon_range": (810, 898)},
    "Paldea": {"id": "672a2dcf6f86a8ba93a4a735", "name": "Paldea", "pokemon_range": (899, 1010)}
}

# Recorremos todos los Pokémon para actualizarlos
for pokemon in pokemon_collection.find():
    pokemon_number = pokemon.get("number")  # Asegúrate de usar el campo correcto

    if pokemon_number is None:
        print(f"Error: Pokémon {pokemon['name']} no tiene campo 'number'. Saltando...")
        continue

    # Determinar la región del Pokémon
    for region_data in region_map.values():
        if region_data["pokemon_range"][0] <= pokemon_number <= region_data["pokemon_range"][1]:
            # Actualizar el Pokémon con la región correspondiente
            pokemon_collection.update_one(
                {"_id": pokemon["_id"]},
                {"$set": {
                    "region": {
                        "id": region_data["id"],
                        "name": region_data["name"]
                    }
                }}
            )
            print(f"Pokémon {pokemon['name']} actualizado con la región {region_data['name']}")
            break

print("Actualización completa de todas las regiones de los Pokémon.")
