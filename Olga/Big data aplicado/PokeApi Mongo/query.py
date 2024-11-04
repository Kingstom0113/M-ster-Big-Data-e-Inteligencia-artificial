from pymongo import MongoClient

# Configuración de la conexión a MongoDB Atlas
def connect_to_mongo(uri):
    try:
        client = MongoClient(uri)
        print("Conexión exitosa a MongoDB Atlas")
        return client
    except Exception as e:
        print("Error de conexión:", e)
        return None

# Obtener datos de Bulbasaur
def get_bulbasaur_data(collection):
    try:
        bulbasaur = collection.find_one({'name': 'bulbasaur'})  # Busca por el nombre 'bulbasaur'
        return bulbasaur  # Retorna los datos de Bulbasaur
    except Exception as e:
        print("Error al obtener los datos de Bulbasaur:", e)
        return None

# Mostrar los datos en un formato legible
def display_data(data):
    if data:
        print("Datos de Bulbasaur:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("Bulbasaur no encontrado en la base de datos.")

# Función principal
def main():
    # URI de conexión (reemplaza con tu propia URI)
    uri = "mongodb+srv://manuelsr0113:Firmamento.34@cluster0.aztgaop.mongodb.net/?retryWrites=true&w=majority"
    
    # Conexión a la base de datos
    client = connect_to_mongo(uri)
    if client:
        db = client['PokeApi']  # Base de datos llamada 'PokeApi'
        pokemons_collection = db['pokemons']  # Colección de Pokémon
        
        # Obtener datos de Bulbasaur
        bulbasaur_data = get_bulbasaur_data(pokemons_collection)
        
        # Mostrar los datos
        display_data(bulbasaur_data)

# Ejecutar la función principal
if __name__ == "__main__":
    main()
