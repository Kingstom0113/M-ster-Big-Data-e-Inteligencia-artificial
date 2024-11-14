import json

# Función para cargar la información de los alumnos desde el archivo JSON
def cargar_alumnos():
    try:
        with open("informacion_alumnos.json", "r") as file:
            data = json.load(file)
            return data['alumnos']
    except FileNotFoundError:
        # Si el archivo no existe, devolver una lista vacía
        return []

# Función para guardar la información de los alumnos en el archivo JSON
def guardar_alumnos(alumnos):
    with open("informacion_alumnos.json", "w") as file:
        json.dump({"alumnos": alumnos}, file, indent=4)

# Función para agregar un nuevo alumno
def agregar_alumno(alumnos, nombre, edad, calificacion, ciudad):
    nuevo_alumno = {
        "nombre": nombre,
        "edad": edad,
        "calificacion": calificacion,
        "ciudad": ciudad
    }
    alumnos.append(nuevo_alumno)
    guardar_alumnos(alumnos)

# Función para eliminar un alumno por nombre
def eliminar_alumno(alumnos, nombre):
    alumnos = [alumno for alumno in alumnos if alumno['nombre'].lower() != nombre.lower()]
    guardar_alumnos(alumnos)
    return alumnos

# Función para filtrar alumnos aprobados (calificación >= 60)
def filtrar_aprobados(alumnos):
    return [alumno for alumno in alumnos if alumno['calificacion'] >= 60]

# Función para calcular la edad promedio de los alumnos
def calcular_edad_promedio(alumnos):
    if not alumnos:
        return 0
    total_edad = sum(alumno['edad'] for alumno in alumnos)
    return total_edad / len(alumnos)

# Función para mostrar todos los alumnos
def mostrar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.")
    for alumno in alumnos:
        print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Calificación: {alumno['calificacion']}, Ciudad: {alumno['ciudad']}")

# Inicialización de datos
alumnos = cargar_alumnos()

# Insertar al menos 10 alumnos si no existen
if not alumnos:
    alumnos = [
        {"nombre": "Carlos", "edad": 20, "calificacion": 85, "ciudad": "Madrid"},
        {"nombre": "Lucía", "edad": 22, "calificacion": 90, "ciudad": "Barcelona"},
        {"nombre": "Pedro", "edad": 19, "calificacion": 55, "ciudad": "Sevilla"},
        {"nombre": "Ana", "edad": 21, "calificacion": 65, "ciudad": "Valencia"},
        {"nombre": "Miguel", "edad": 23, "calificacion": 72, "ciudad": "Madrid"},
        {"nombre": "Sofía", "edad": 20, "calificacion": 92, "ciudad": "Barcelona"},
        {"nombre": "Luis", "edad": 24, "calificacion": 60, "ciudad": "Madrid"},
        {"nombre": "María", "edad": 22, "calificacion": 85, "ciudad": "Sevilla"},
        {"nombre": "Julia", "edad": 19, "calificacion": 40, "ciudad": "Valencia"},
        {"nombre": "José", "edad": 21, "calificacion": 95, "ciudad": "Madrid"}
    ]
    guardar_alumnos(alumnos)

# Ejemplo de uso

# Mostrar todos los alumnos
print("Alumnos registrados:")
mostrar_alumnos(alumnos)

# Calcular la edad promedio
edad_promedio = calcular_edad_promedio(alumnos)
print(f"\nEdad promedio de los alumnos: {edad_promedio:.2f} años")

# Filtrar alumnos aprobados
print("\nAlumnos aprobados:")
aprobados = filtrar_aprobados(alumnos)
for alumno in aprobados:
    print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Calificación: {alumno['calificacion']}, Ciudad: {alumno['ciudad']}")

# Agregar un nuevo alumno
print("\nAgregar un nuevo alumno:")
agregar_alumno(alumnos, "Felipe", 25, 88, "Madrid")
print("Alumno agregado.")

# Eliminar un alumno
print("\nEliminar alumno 'José':")
alumnos = eliminar_alumno(alumnos, "José")
print("Alumno eliminado.")

# Mostrar todos los alumnos después de agregar y eliminar
print("\nAlumnos registrados después de agregar y eliminar:")
mostrar_alumnos(alumnos)
