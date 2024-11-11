from pymongo import MongoClient


# Conexión a la base de datos MongoDB
uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client['PokeApi']
coleccion = db["gyms"]  # Colección llamada 'gyms'

try:
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB Atlas")
except Exception as e:
    print("Error de conexión:", e)

# Documento JSON modificado sin variables y con comillas dobles
documento = [
    {
        "region": {
            "id": "672a2dcf6f86a8ba93a4a727",  
            "name": "Kanto"
        },
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
        "region": {
            "id": "672a2dcf6f86a8ba93a4a728",  
            "name": "Johto"
        },
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
        "region": {
            "id": "672a2dcf6f86a8ba93a4a729",  
            "name": "Hoenn"
        },
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
    },
    {
        "region": {
            "id": "672a2dcf6f86a8ba93a4a730",  
            "name": "Sinnoh"
        },
        "gyms": [
            {"name": "Oreburgh City Gym", "leader": "Roark", "type": "Rock"},
            {"name": "Eterna City Gym", "leader": "Gardenia", "type": "Grass"},
            {"name": "Veilstone City Gym", "leader": "Maylene", "type": "Fighting"},
            {"name": "Pastoria City Gym", "leader": "Crasher Wake", "type": "Water"},
            {"name": "Hearthome City Gym", "leader": "Fantina", "type": "Ghost"},
            {"name": "Canalave City Gym", "leader": "Byron", "type": "Steel"},
            {"name": "Snowpoint City Gym", "leader": "Candice", "type": "Ice"},
            {"name": "Sunyshore City Gym", "leader": "Volkner", "type": "Electric"}
        ]
    },
    {
        "region": {
            "id": "672a2dcf6f86a8ba93a4a731",  
            "name": "Unova"
        },
        "gyms": [
            {"name": "Striaton City Gym", "leader": "Cilan, Chili & Cress", "type": "Grass/Fire/Water"},
            {"name": "Nacrene City Gym", "leader": "Lenora", "type": "Normal"},
            {"name": "Castelia City Gym", "leader": "Burgh", "type": "Bug"},
            {"name": "Nimbasa City Gym", "leader": "Elesa", "type": "Electric"},
            {"name": "Driftveil City Gym", "leader": "Clay", "type": "Ground"},
            {"name": "Mistralton City Gym", "leader": "Skyla", "type": "Flying"},
            {"name": "Icirrus City Gym", "leader": "Brycen", "type": "Ice"},
            {"name": "Opelucid City Gym", "leader": "Drayden/Iris", "type": "Dragon"}
        ]
    },
    {
        "region": {
            "id": "672a2dcf6f86a8ba93a4a732",  
            "name": "Kalos"
        },
        "gyms": [
            {"name": "Santalune City Gym", "leader": "Viola", "type": "Bug"},
            {"name": "Cyllage City Gym", "leader": "Grant", "type": "Rock"},
            {"name": "Shalour City Gym", "leader": "Korrina", "type": "Fighting"},
            {"name": "Coumarine City Gym", "leader": "Ramos", "type": "Grass"},
            {"name": "Lumiose City Gym", "leader": "Clemont", "type": "Electric"},
            {"name": "Laverre City Gym", "leader": "Valerie", "type": "Fairy"},
            {"name": "Anistar City Gym", "leader": "Olympia", "type": "Psychic"},
            {"name": "Snowbelle City Gym", "leader": "Wulfric", "type": "Ice"}
        ]
    },
    {
    "region": {
        "id": "672a2dcf6f86a8ba93a4a733",  
        "name": "Alola"
    },
    "gyms": [
        {
            "name": "Verdant Cavern Trial",
            "leader": "Captain Ilima",
            "type": "Normal",
            "location": "Melemele Island"
        },
        {
            "name": "Brooklet Hill Trial",
            "leader": "Captain Lana",
            "type": "Water",
            "location": "Akala Island"
        },
        {
            "name": "Wela Volcano Park Trial",
            "leader": "Captain Kiawe",
            "type": "Fire",
            "location": "Akala Island"
        },
        {
            "name": "Lush Jungle Trial",
            "leader": "Captain Mallow",
            "type": "Grass",
            "location": "Akala Island"
        },
        {
            "name": "Shady House Trial",
            "leader": "Captain Nanu",
            "type": "Dark",
            "location": "Ula'ula Island"
        },
        {
            "name": "Hokulani Observatory Trial",
            "leader": "Captain Sophocles",
            "type": "Electric",
            "location": "Ula'ula Island"
        },
        {
            "name": "Vast Poni Canyon Trial",
            "leader": "Captain Mina",
            "type": "Fairy",
            "location": "Poni Island"
        }
    ],
    "kahunas": [
        {
            "name": "Hala",
            "type": "Fighting",
            "location": "Melemele Island"
        },
        {
            "name": "Olivia",
            "type": "Rock",
            "location": "Akala Island"
        },
        {
            "name": "Nanu",
            "type": "Dark",
            "location": "Ula'ula Island"
        },
        {
            "name": "Hapu",
            "type": "Ground",
            "location": "Poni Island"
        }
    ]
},
    {
        "region": {
            "id": "672a2dcf6f86a8ba93a4a734",  
            "name": "Galar"
        },
        "gyms": [
            {"name": "Turffield Gym", "leader": "Milo", "type": "Grass"},
            {"name": "Hulbury Gym", "leader": "Nessa", "type": "Water"},
            {"name": "Motostoke Gym", "leader": "Kabu", "type": "Fire"},
            {"name": "Stow-on-Side Gym", "leader": "Bea/Allister", "type": "Fighting/Ghost"},
            {"name": "Ballonlea Gym", "leader": "Opal", "type": "Fairy"},
            {"name": "Circhester Gym", "leader": "Gordie/Melony", "type": "Rock/Ice"},
            {"name": "Spikemuth Gym", "leader": "Piers", "type": "Dark"},
            {"name": "Hammerlocke Gym", "leader": "Raihan", "type": "Dragon"}
        ]
    },
    {
        "region": {
            "id": "672a2dcf6f86a8ba93a4a735",  
            "name": "Paldea"
        },
        "gyms": [
            {"name": "Cortondo Gym", "leader": "Katy", "type": "Bug"},
            {"name": "Artazon Gym", "leader": "Brassius", "type": "Grass"},
            {"name": "Levincia Gym", "leader": "Iono", "type": "Electric"},
            {"name": "Cascarrafa Gym", "leader": "Kofu", "type": "Water"},
            {"name": "Medali Gym", "leader": "Larry", "type": "Normal"},
            {"name": "Montenevera Gym", "leader": "Ryme", "type": "Ghost"},
            {"name": "Alfornada Gym", "leader": "Tulip", "type": "Psychic"},
            {"name": "Glaseado Gym", "leader": "Grusha", "type": "Ice"}
        ]
    }
]
coleccion.insert_many(documento)
print("Gimnasios insertado correctamente en MongoDB.")
