from pymongo import MongoClient
import requests

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
# Función para obtener Team Rocket (estáticos porque no hay API)
def insert_team_rockets():
    teamrockets_collection.insert_many([
        {'name': 'Elise', 'role': 'Grunt', 'age': 26},
    {'name': 'Sasha', 'role': 'Agent', 'age': 27},
    {'name': 'Victor', 'role': 'Grunt', 'age': 30},
    {'name': 'Cory', 'role': 'Grunt', 'age': 24},
    {'name': 'Diana', 'role': 'Agent', 'age': 33},
    {'name': 'Ruben', 'role': 'Grunt', 'age': 22},
    {'name': 'Nikki', 'role': 'Grunt', 'age': 28},
    {'name': 'Jason', 'role': 'Agent', 'age': 35},
    {'name': 'Max', 'role': 'Grunt', 'age': 31},
    {'name': 'Alma', 'role': 'Agent', 'age': 30},
    {'name': 'Brody', 'role': 'Grunt', 'age': 32},
    {'name': 'Penny', 'role': 'Grunt', 'age': 29},
    {'name': 'Luca', 'role': 'Grunt', 'age': 26},
    {'name': 'Tessa', 'role': 'Agent', 'age': 31},
    {'name': 'Harley', 'role': 'Grunt', 'age': 30},
    {'name': 'Gavin', 'role': 'Agent', 'age': 38},
    {'name': 'Maya', 'role': 'Grunt', 'age': 25},
    {'name': 'Caleb', 'role': 'Grunt', 'age': 27},
    {'name': 'Isabella', 'role': 'Agent', 'age': 36},
    {'name': 'Henry', 'role': 'Grunt', 'age': 33},
    {'name': 'Lance', 'role': 'Agent', 'age': 31},
    {'name': 'Linda', 'role': 'Grunt', 'age': 29},
    {'name': 'Nate', 'role': 'Grunt', 'age': 28},
    {'name': 'Eliza', 'role': 'Agent', 'age': 34},
    {'name': 'Travis', 'role': 'Grunt', 'age': 26},
    {'name': 'Sophia', 'role': 'Agent', 'age': 37},
    {'name': 'Tommy', 'role': 'Grunt', 'age': 27},
    {'name': 'Eva', 'role': 'Grunt', 'age': 25},
    {'name': 'Blake', 'role': 'Agent', 'age': 34},
    {'name': 'Carla', 'role': 'Grunt', 'age': 32},
    {'name': 'Jessica', 'role': 'Grunt', 'age': 28},
    {'name': 'Ashford', 'role': 'Grunt', 'age': 29},
    {'name': 'Xander', 'role': 'Agent', 'age': 30},
    {'name': 'Tanya', 'role': 'Grunt', 'age': 26},
    {'name': 'Martin', 'role': 'Agent', 'age': 33},
    {'name': 'Kayla', 'role': 'Grunt', 'age': 27},
    {'name': 'Brett', 'role': 'Grunt', 'age': 30},
    {'name': 'Lilliana', 'role': 'Agent', 'age': 35},
    {'name': 'Zane', 'role': 'Grunt', 'age': 32},
    {'name': 'Jenna', 'role': 'Grunt', 'age': 29},
    {'name': 'Isaac', 'role': 'Agent', 'age': 38},
    {'name': 'Kendall', 'role': 'Grunt', 'age': 28},
    {'name': 'Carmen', 'role': 'Grunt', 'age': 33},
    {'name': 'Lucia', 'role': 'Grunt', 'age': 31},
    {'name': 'Dominic', 'role': 'Agent', 'age': 39},
    {'name': 'Aidan', 'role': 'Grunt', 'age': 28},
    {'name': 'Clarissa', 'role': 'Agent', 'age': 34},
    {'name': 'Alex', 'role': 'Grunt', 'age': 29},
    {'name': 'Elliot', 'role': 'Grunt', 'age': 28},
    {'name': 'Barbara', 'role': 'Agent', 'age': 32},
    {'name': 'Riley', 'role': 'Grunt', 'age': 25},
    {'name': 'Tessa', 'role': 'Grunt', 'age': 33},
    {'name': 'Mason', 'role': 'Agent', 'age': 37},
    {'name': 'Kate', 'role': 'Grunt', 'age': 32},
    {'name': 'Mark', 'role': 'Grunt', 'age': 29},
    {'name': 'Amy', 'role': 'Agent', 'age': 31},
    {'name': 'Oscar', 'role': 'Grunt', 'age': 30},
    {'name': 'Jill', 'role': 'Agent', 'age': 36},
    {'name': 'Jordan', 'role': 'Grunt', 'age': 26},
    {'name': 'Nico', 'role': 'Agent', 'age': 38},
    {'name': 'Brianna', 'role': 'Grunt', 'age': 29},
    {'name': 'Derek', 'role': 'Agent', 'age': 33},
    {'name': 'Amber', 'role': 'Grunt', 'age': 30},
    {'name': 'Xenia', 'role': 'Agent', 'age': 35},
    {'name': 'Kara', 'role': 'Grunt', 'age': 32},
    {'name': 'Dexter', 'role': 'Agent', 'age': 39},
    {'name': 'Wesley', 'role': 'Grunt', 'age': 28},
    {'name': 'Olivia', 'role': 'Agent', 'age': 34},
    {'name': 'Lucas', 'role': 'Grunt', 'age': 29},
    {'name': 'Veronica', 'role': 'Grunt', 'age': 30},
    {'name': 'Roberto', 'role': 'Agent', 'age': 37},
    {'name': 'Carla', 'role': 'Grunt', 'age': 32},
    {'name': 'Simon', 'role': 'Agent', 'age': 36},
    {'name': 'Miranda', 'role': 'Grunt', 'age': 29},
    {'name': 'Hannah', 'role': 'Grunt', 'age': 31},
    {'name': 'Raymond', 'role': 'Agent', 'age': 38},
    {'name': 'Shannon', 'role': 'Grunt', 'age': 26},
    {'name': 'Paige', 'role': 'Agent', 'age': 33},
    {'name': 'Jeff', 'role': 'Grunt', 'age': 30},
    {'name': 'Theo', 'role': 'Grunt', 'age': 29},
    {'name': 'Cory', 'role': 'Agent', 'age': 35},
    {'name': 'Nina', 'role': 'Grunt', 'age': 28},
    {'name': 'Adrian', 'role': 'Agent', 'age': 38},
    {'name': 'Phoebe', 'role': 'Grunt', 'age': 25},
    {'name': 'Helen', 'role': 'Grunt', 'age': 32},
    {'name': 'Oscar', 'role': 'Agent', 'age': 33},
    {'name': 'Cassandra', 'role': 'Grunt', 'age': 29},
    {'name': 'Emilia', 'role': 'Agent', 'age': 34},
    {'name': 'Connor', 'role': 'Grunt', 'age': 30},
    {'name': 'Ava', 'role': 'Agent', 'age': 28}
    ])
    print("Team Rocket agregado.")

# Llamada a la función
insert_team_rockets()