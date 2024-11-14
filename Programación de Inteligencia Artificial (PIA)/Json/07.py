import json
from datetime import datetime

# Función para cargar los libros desde un archivo JSON
def cargar_libros():
    try:
        with open("catalogo_libros.json", "r") as file:
            data = json.load(file)
            return data['libros']
    except FileNotFoundError:
        # Si el archivo no existe, devolver una lista vacía
        return []

# Función para guardar los libros en el archivo JSON
def guardar_libros(libros):
    with open("catalogo_libros.json", "w") as file:
        json.dump({"libros": libros}, file, indent=4)

# Función para agregar un libro al catálogo
def agregar_libro(libros, titulo, autor, genero, año):
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "año": año
    }
    libros.append(nuevo_libro)
    guardar_libros(libros)

# Función para filtrar libros por género
def filtrar_por_genero(libros, genero):
    return [libro for libro in libros if libro['genero'].lower() == genero.lower()]

# Función para filtrar libros por autor
def filtrar_por_autor(libros, autor):
    return [libro for libro in libros if libro['autor'].lower() == autor.lower()]

# Función para listar libros recientes (últimos 5 años)
def listar_libros_recientes(libros):
    año_actual = datetime.now().year
    libros_recientes = [libro for libro in libros if libro['año'] >= año_actual - 5]
    return libros_recientes

# Función para mostrar todos los libros
def mostrar_libros(libros):
    if not libros:
        print("No hay libros disponibles en el catálogo.")
    for libro in libros:
        print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, Año: {libro['año']}")

# Inicialización de datos
libros = cargar_libros()

# Insertar al menos 10 libros si no existen
if not libros:
    libros = [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "genero": "Ficción", "año": 1967},
        {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "genero": "Clásico", "año": 1605},
        {"titulo": "1984", "autor": "George Orwell", "genero": "Distopía", "año": 1949},
        {"titulo": "Matar a un Ruiseñor", "autor": "Harper Lee", "genero": "Ficción", "año": 1960},
        {"titulo": "Orgullo y Prejuicio", "autor": "Jane Austen", "genero": "Romántico", "año": 1813},
        {"titulo": "Donde Viven los Monstruos", "autor": "Maurice Sendak", "genero": "Infantil", "año": 1963},
        {"titulo": "Cumbres Borrascosas", "autor": "Emily Brontë", "genero": "Gótico", "año": 1847},
        {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "genero": "Ciencia Ficción", "año": 1953},
        {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón", "genero": "Misterio", "año": 2001},
        {"titulo": "Harry Potter y la Piedra Filosofal", "autor": "J.K. Rowling", "genero": "Fantasía", "año": 1997}
    ]
    guardar_libros(libros)

# Ejemplo de uso

# Mostrar todos los libros
print("Libros disponibles en el catálogo:")
mostrar_libros(libros)

# Filtrar libros por género (ejemplo: Ficción)
print("\nFiltrar libros por género 'Ficción':")
libros_ficcion = filtrar_por_genero(libros, "Ficción")
for libro in libros_ficcion:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, Año: {libro['año']}")

# Filtrar libros por autor (ejemplo: Gabriel García Márquez)
print("\nFiltrar libros por autor 'Gabriel García Márquez':")
libros_gabriel = filtrar_por_autor(libros, "Gabriel García Márquez")
for libro in libros_gabriel:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, Año: {libro['año']}")

# Listar libros recientes (últimos 5 años)
print("\nLibros recientes (últimos 5 años):")
libros_recientes = listar_libros_recientes(libros)
for libro in libros_recientes:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, Año: {libro['año']}")

# Agregar un nuevo libro
print("\nAgregar un nuevo libro:")
agregar_libro(libros, "El Gran Gatsby", "F. Scott Fitzgerald", "Clásico", 1925)
print("Libro agregado con éxito.")
mostrar_libros(libros)
