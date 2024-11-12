from pymongo import MongoClient
from regions import insert_regions

# Conexión a la base de datos MongoDB
uri = "mongodb://admin:admin@localhost:27017"
client = MongoClient(uri)
db = client['PokeApi']

try:
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB Atlas")
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

# Función para insertar profesores
def insert_professors(region_ids):
    try:
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
    except Exception as e:
        print("Error al insertar profesores:", e)

    print("Profesores agregados.")

# Llamada a la función
region_ids = insert_regions()
insert_professors(region_ids)
   