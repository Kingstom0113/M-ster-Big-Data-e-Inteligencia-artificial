import json
import re
from datetime import datetime

# Función para cargar datos desde un archivo JSON
def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

# Validación de email
def patron_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))

# Validación de teléfono (9 dígitos, comienza con 6, 7 o 9)
def patron_telefono(telefono):
    patron = r'^[679]\d{8}$'
    return bool(re.match(patron, telefono))

# Validación de código postal (5 dígitos)
def patron_codigo_postal(codigo_postal):
    patron = r'^\d{5}$'
    return bool(re.match(patron, codigo_postal))

# Validación de matrícula (4 dígitos seguidos de 3 letras)
def patron_matricula(matricula):
    patron = r'^\d{4}[A-Z]{3}$'
    return bool(re.match(patron, matricula))

# Validación de año (entre 1900 y el año actual)
def patron_ano(ano):
    anio_actual = datetime.now().year
    return 1900 <= int(ano) <= anio_actual

# Validación de email del propietario de vehículo
def patron_email_propietario(email):
    return patron_email(email)  # Reutilizando la misma función para el email

# Función para validar los datos de los alumnos
def validar_alumnos(alumnos):
    validos = []
    for alumno in alumnos:
        if (patron_email(alumno['email']) and
            patron_telefono(alumno['telefono']) and
            patron_codigo_postal(alumno['codigo_postal'])):
            validos.append(alumno)
    return validos

# Función para validar los datos de los vehículos
def validar_vehiculos(vehiculos):
    validos = []
    for vehiculo in vehiculos:
        if (patron_matricula(vehiculo['matricula']) and
            patron_ano(vehiculo['año']) and
            patron_email_propietario(vehiculo['propietario_email'])):
            validos.append(vehiculo)
    return validos

# Ejemplo de estructura de los archivos JSON

# Contenido de alumnos.json
alumnos_data = {
    "alumnos": [
        {"nombre": "Carlos Pérez", "email": "carlos@example.com", "telefono": "612345678", "codigo_postal": "28001", "curso": "DAW2"},
        {"nombre": "Lucía Gómez", "email": "lucia@example.com", "telefono": "623456789", "codigo_postal": "08002", "curso": "DAW1"},
        {"nombre": "Juan Rodríguez", "email": "juan@invalid", "telefono": "612345678", "codigo_postal": "28003", "curso": "DAM2"},
        {"nombre": "Ana Sánchez", "email": "ana.sanchez@example.com", "telefono": "935123456", "codigo_postal": "29004", "curso": "DAW2"}
    ]
}

# Contenido de vehiculos.json
vehiculos_data = {
    "vehiculos": [
        {"matricula": "1234ABC", "marca": "Toyota", "modelo": "Corolla", "año": "2020", "propietario_email": "propietario1@example.com"},
        {"matricula": "5678DEF", "marca": "Honda", "modelo": "Civic", "año": "2018", "propietario_email": "propietario2@example.com"},
        {"matricula": "9101XYZ", "marca": "Ford", "modelo": "Focus", "año": "2015", "propietario_email": "propietario3@example"},
        {"matricula": "1122GHI", "marca": "BMW", "modelo": "X5", "año": "2023", "propietario_email": "propietario4@example.com"}
    ]
}

# Guardar los datos de ejemplo en los archivos JSON
with open("alumnos.json", "w") as file:
    json.dump(alumnos_data, file, indent=4)

with open("vehiculos.json", "w") as file:
    json.dump(vehiculos_data, file, indent=4)

# Cargar y validar los datos de alumnos
alumnos = cargar_datos("alumnos.json")["alumnos"]
alumnos_validos = validar_alumnos(alumnos)

# Mostrar los alumnos válidos
print("Alumnos válidos:")
for alumno in alumnos_validos:
    print(alumno)

# Cargar y validar los datos de vehículos
vehiculos = cargar_datos("vehiculos.json")["vehiculos"]
vehiculos_validos = validar_vehiculos(vehiculos)

# Mostrar los vehículos válidos
print("\nVehículos válidos:")
for vehiculo in vehiculos_validos:
    print(vehiculo)
