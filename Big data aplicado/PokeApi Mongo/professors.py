from pymongo import MongoClient
import random

# Conexión a la base de datos MongoDB
uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client['PokeApi']

try:
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB Atlas")
except Exception as e:
    print("Error de conexión:", e)

# Colecciones de MongoDB
professors_collection = db['professors']

# Obtener todas las regiones desde la colección 'regions'
regions = list(db.regions.find({}, {"_id": 1, "name": 1}))

# Función para insertar profesores
professors_data= [
        {'name': 'Professor Rowan', 'specialty': 'Pokemon Evolution'},
        {'name': 'Professor Kukui', 'specialty': 'Pokemon Moves and Battle Strategies'},
        {'name': 'Professor Sycamore', 'specialty': 'Mega Evolution'},
        {'name': 'Professor Magnolia', 'specialty': 'Dynamax and Gigantamax Phenomena'},
        {'name': 'Professor Willow', 'specialty': 'Pokemon Biology'},
        {'name': 'Professor Juniper', 'specialty': 'Genetics and Evolution'},
        {'name': 'Professor Oakley', 'specialty': 'Shadow Pokemon Research'},
        {'name': 'Professor Aspen', 'specialty': 'Regional Pokemon Species'},
        {'name': 'Professor Oakridge', 'specialty': 'Artificial Pokemon Intelligence'},
        {'name': 'Professor Pine', 'specialty': 'Pokemon Ecology'},
        {'name': 'Professor Larch', 'specialty': 'Ancient Pokemon Fossils'},
        {'name': 'Professor Burnet', 'specialty': 'Ultra Beasts and Alternate Dimensions'},
        {'name': 'Professor Cedric Juniper', 'specialty': 'Research on the Unova Region’s Legendary Pokemon'},
        {'name': 'Professor Bambo', 'specialty': 'Pokemon Species of Torren Region'},
        {'name': 'Professor Kettler', 'specialty': 'Behavioral Studies in Pokemon'},
        {'name': 'Professor Radley', 'specialty': 'Gigantamaxing Research'},
        {'name': 'Professor Hala', 'specialty': 'Island Trials and Traditional Pokemon Training'},
        {'name': 'Professor Burbank', 'specialty': 'Pokemon Genetics and Species Mapping'},
        {'name': 'Professor Tsu', 'specialty': 'Pokemon Breeding and Crossbreeding'},
        {'name': 'Professor Ainsley', 'specialty': 'Water-type Pokemon Behavior'},
        {'name': 'Professor Usher', 'specialty': 'Pokemon Adaptation to Urban Environments'},
        {'name': 'Professor Xenon', 'specialty': 'Alola’s Regional Variants and Evolution'},
        {'name': 'Professor Delphine', 'specialty': 'Research on Legendary and Mythical Pokemon'},
        {'name': 'Professor Marley', 'specialty': 'Pokemon Intelligence and Learning'},
        {'name': 'Professor Ivy', 'specialty': 'Pokémon Reproduction and Hybridization'},
        {'name': 'Professor Frida', 'specialty': 'Species Ecology and Conservation'},
        {'name': 'Professor Viera', 'specialty': 'Environmental Impact of Pokemon in Alola'},
        {'name': 'Professor Thorne', 'specialty': 'Pokemon Communication'},
        {'name': 'Professor Akira', 'specialty': 'Understanding Mega Evolutions'},
        {'name': 'Professor Alden', 'specialty': 'The Study of Legendary Pokemon'},
        {'name': 'Professor Constantine', 'specialty': 'Dynamax Phenomena and Strategy'},
        {'name': 'Professor Maris', 'specialty': 'Researching the Behavior of Psychic-Type Pokemon'},
        {'name': 'Professor Nia', 'specialty': 'Pokemon Behaviour and Interaction with Humans'},
        {'name': 'Professor Opal', 'specialty': 'Fairy-Type Pokemon Research'},
        {'name': 'Professor Rose', 'specialty': 'Energy Sources and their Impact on Pokemon'},
        {'name': 'Professor Mapache', 'specialty': 'Pokemon Evolution in Unique Environments'},
        {'name': 'Professor Peridot', 'specialty': 'Geographic Distribution of Pokemon'},
        {'name': 'Professor Ramona', 'specialty': 'Regional Ecology of the Hoenn Region'},
        {'name': 'Professor Bellamy', 'specialty': 'Mechanisms of Pokemon Bonding'},
        {'name': 'Professor Merle', 'specialty': 'The Study of Steel-Type Pokemon'},
        {'name': 'Professor Corrine', 'specialty': 'The Relationship Between Pokemon and Trainers'},
        {'name': 'Professor Daley', 'specialty': 'Researching the Effects of Dynamaxing on Pokemon and Trainers'},
        {'name': 'Professor Noctis', 'specialty': 'Nighttime Behavior and Research of Pokemon'},
        {'name': 'Professor Remy', 'specialty': 'Advanced Technology in Pokemon Research'},
        {'name': 'Professor Sybil', 'specialty': 'The Connection Between Psychic-Type and Dragon-Type Pokemon'},
        {'name': 'Professor Tilly', 'specialty': 'Study of Mythical and Legendary Pokemon'},
        {'name': 'Professor Atlas', 'specialty': 'Research of Ice-Type and Mountain Pokemon'},
        {'name': 'Professor Lux', 'specialty': 'Electric-Type Pokemon Research'},
        {'name': 'Professor Iris', 'specialty': 'Dragon-Type Pokemon Research'},
        {'name': 'Professor Vega', 'specialty': 'Specialization in Star and Meteorite Pokemon'},
        {'name': 'Professor Alistair', 'specialty': 'Psychic-Type and its Influence on Evolution'},
        {'name': 'Professor Remington', 'specialty': 'Mapping Pokemon Species in the Hoenn Region'},
        {'name': 'Professor Lucille', 'specialty': 'Pokemon Breeding and Crossbreeding'},
        {'name': 'Professor Dexter', 'specialty': 'The Impact of Alola’s Regional Changes on Pokemon'},
        {'name': 'Professor Wilfred', 'specialty': 'The Evolution of Electric-Type Pokemon'},
        {'name': 'Professor Hunter', 'specialty': 'The Study of Rare and Unusual Pokemon'},
        {'name': 'Professor Oren', 'specialty': 'Research of Fossil Pokemon'},
        {'name': 'Professor Ashford', 'specialty': 'The Impact of Climate on Pokemon Evolution'},
        {'name': 'Professor Noelle', 'specialty': 'Ecosystem Interactions Between Pokemon'},
        {'name': 'Professor Ramiro', 'specialty': 'Pokemon Habitat and Geography'},
        {'name': 'Professor Harlan', 'specialty': 'Research on Wild Pokemon Behavior'},
        {'name': 'Professor Celia', 'specialty': 'The Study of Grass-Type Pokemon'},
        {'name': 'Professor Lilith', 'specialty': 'Research on Water-Type Pokemon'},
        {'name': 'Professor Tannis', 'specialty': 'Pokemon Metabolism and Growth Patterns'},
        {'name': 'Professor Ogle', 'specialty': 'Research on Pokemon Consciousness'},
        {'name': 'Professor Esperanza', 'specialty': 'Study of Electric-Type Pokemon Behavior'},
        {'name': 'Professor Alda', 'specialty': 'Interaction of Steel-Type and Fighting-Type Pokemon'},
        {'name': 'Professor Wilda', 'specialty': 'Research on Fairy-Type Pokemon'},
        {'name': 'Professor Tessa', 'specialty': 'Research on the Alola Region’s Legendary Pokemon'}
]
   
professors = []

# Recorrer todos los profesores y asignarles una región
for professor in professors_data:
    # Seleccionar una región aleatoria para cada profesor
    region = random.choice(regions)  # Escoger una región aleatoria de la lista de regiones

    # Crear el documento del profesor con su región
    professor_document = {
        "name": professor['name'],
        "specialty": professor['specialty'],
        "regions": [{
            "id": region["_id"],  # ID de la región
            "name": region["name"]  # Nombre de la región
        }]
    }

    professors.append(professor_document)

# Insertar los documentos en la colección 'professors'
if professors:
    db.professors.insert_many(professors)
    print("Profesores agregados a la base de datos.")
else:
    print("No se encontraron profesores para agregar.")