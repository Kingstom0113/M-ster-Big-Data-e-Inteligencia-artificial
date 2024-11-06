from pymongo import MongoClient

# Conexión a la base de datos MongoDB
uri = "mongodb+srv://manuelsr0113:Firmamento.34@cluster0.aztgaop.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["PokeApi"]  # Base de datos llamada 'PokeApi'
coleccion = db["gyms"]  # Colección llamada 'gyms'

try:
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB Atlas")
except Exception as e:
    print("Error de conexión:", e)

# Documento JSON modificado sin variables y con comillas dobles
documento = [
    {
        "region": "672a2dcf6f86a8ba93a4a727",  # Reemplaza "ID_de_Kanto" por el ID real de la región Kanto
        "gyms": [
            {"name": "Pewter City Gym", "leader": "Brock", "type": "Rock"},
            {"name": "Cerulean City Gym", "leader": "Misty", "type": "Water"},
            {"name": "Vermilion City Gym", "leader": "Lieutenant Surge", "type": "Electric"},
            {"name": "Celadon City Gym", "leader": "Erika", "type": "Grass"},
            {"name": "Fuchsia City Gym", "leader": "Koga", "type": "Poison"},
            {"name": "Viridian City Gym", "leader": "Giovanni", "type": "Ground"},
            {"name": "Saffron City Gym", "leader": "Sabrina", "type": "Psychic"},
            {"name": "Cinnabar Island Gym", "leader": "Blane", "type": "Fire"}
        ]
    },
    {
        "region": "672a2dcf6f86a8ba93a4a728",  # Reemplaza "ID_de_Johto" por el ID real de la región Johto
        "gyms": [
            {"name": "Violet City Gym", "leader": "Falkner", "type": "Flying"},
            {"name": "Azalea Town Gym", "leader": "Bugsy", "type": "Bug"},
            {"name": "Goldenrod City Gym", "leader": "Whitney", "type": "Normal"},
            {"name": "Ecruteak City Gym", "leader": "Morty", "type": "Ghost"},
            {"name": "Mahogany Town Gym", "leader": "Pryce", "type": "Ice"},
            {"name": "Olivine City Gym", "leader": "Jasmine", "type": "Steel"},
            {"name": "Cianwood City Gym", "leader": "Chuck", "type": "Fighting"},
            {"name": "Blackthorn City Gym", "leader": "Clair", "type": "Dragon"}
        ]
    },
    {
        "region": "672a2dcf6f86a8ba93a4a729",  # Reemplaza "ID_de_Hoenn" por el ID real de la región Hoenn
        "gyms": [
            {"name": "Rustboro City Gym", "leader": "Roxanne", "type": "Rock"},
            {"name": "Dewford Town Gym", "leader": "Brawly", "type": "Fighting"},
            {"name": "Mauville City Gym", "leader": "Wattson", "type": "Electric"},
            {"name": "Lavaridge Town Gym", "leader": "Flannery", "type": "Fire"},
            {"name": "Petalburg City Gym", "leader": "Norman", "type": "Normal"},
            {"name": "Fortree City Gym", "leader": "Winona", "type": "Flying"},
            {"name": "Mossdeep City Gym", "leader": "Tate & Liza", "type": "Psychic"},
            {"name": "Sootopolis City Gym", "leader": "Wallace", "type": "Water"}
        ]
    }
]

# Inserción del documento en la colección
coleccion.insert_many(documento)
print("Documento insertado correctamente en MongoDB.")
