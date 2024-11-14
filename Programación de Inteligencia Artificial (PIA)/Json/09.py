import json

# Función para cargar las películas desde un archivo JSON
def cargar_peliculas():
    try:
        with open("catalogo_peliculas.json", "r") as file:
            data = json.load(file)
            return data['peliculas']
    except FileNotFoundError:
        # Si el archivo no existe, devolver una lista vacía
        return []

# Función para guardar las películas en el archivo JSON
def guardar_peliculas(peliculas):
    with open("catalogo_peliculas.json", "w") as file:
        json.dump({"peliculas": peliculas}, file, indent=4)

# Función para agregar una nueva película
def agregar_pelicula(peliculas, titulo, director, año, genero):
    nueva_pelicula = {
        "titulo": titulo,
        "director": director,
        "año": año,
        "genero": genero
    }
    peliculas.append(nueva_pelicula)
    guardar_peliculas(peliculas)

# Función para filtrar las películas por género
def filtrar_por_genero(peliculas, genero):
    return [pelicula for pelicula in peliculas if pelicula['genero'].lower() == genero.lower()]

# Función para listar directores únicos
def listar_directores_unicos(peliculas):
    directores = {pelicula['director'] for pelicula in peliculas}
    return directores

# Función para mostrar todas las películas
def mostrar_peliculas(peliculas):
    if not peliculas:
        print("No hay películas disponibles.")
    for pelicula in peliculas:
        print(f"Título: {pelicula['titulo']}, Director: {pelicula['director']}, Año: {pelicula['año']}, Género: {pelicula['genero']}")

# Inicialización de datos
peliculas = cargar_peliculas()

# Insertar al menos 10 películas si no existen
if not peliculas:
    peliculas = [
        {"titulo": "El Laberinto del Fauno", "director": "Guillermo del Toro", "año": 2006, "genero": "Fantasía"},
        {"titulo": "Mar Adentro", "director": "Alejandro Amenábar", "año": 2004, "genero": "Drama"},
        {"titulo": "Inception", "director": "Christopher Nolan", "año": 2010, "genero": "Ciencia Ficción"},
        {"titulo": "La Vida es Bella", "director": "Roberto Benigni", "año": 1997, "genero": "Comedia"},
        {"titulo": "El Secreto de Sus Ojos", "director": "Juan José Campanella", "año": 2009, "genero": "Suspenso"},
        {"titulo": "Forrest Gump", "director": "Robert Zemeckis", "año": 1994, "genero": "Drama"},
        {"titulo": "Titanic", "director": "James Cameron", "año": 1997, "genero": "Romántica"},
        {"titulo": "El Padrino", "director": "Francis Ford Coppola", "año": 1972, "genero": "Crimen"},
        {"titulo": "The Dark Knight", "director": "Christopher Nolan", "año": 2008, "genero": "Acción"},
        {"titulo": "Gladiator", "director": "Ridley Scott", "año": 2000, "genero": "Aventura"}
    ]
    guardar_peliculas(peliculas)

# Ejemplo de uso

# Mostrar todas las películas
print("Películas disponibles en el catálogo:")
mostrar_peliculas(peliculas)

# Filtrar películas por género (ejemplo: Drama)
print("\nFiltrar películas por género 'Drama':")
peliculas_genero = filtrar_por_genero(peliculas, "Drama")
for pelicula in peliculas_genero:
    print(f"Título: {pelicula['titulo']}, Director: {pelicula['director']}, Año: {pelicula['año']}, Género: {pelicula['genero']}")

# Listar directores únicos
print("\nDirectores únicos:")
directores = listar_directores_unicos(peliculas)
for director in directores:
    print(director)

# Agregar una nueva película
print("\nAgregar una nueva película:")
agregar_pelicula(peliculas, "El Origen", "Christopher Nolan", 2010, "Ciencia Ficción")
print("Película agregada con éxito.")
mostrar_peliculas(peliculas)
