import json
from datetime import datetime

# Función para cargar los eventos desde un archivo JSON
def cargar_eventos():
    try:
        with open("agenda_eventos.json", "r") as file:
            data = json.load(file)
            return data['eventos']
    except FileNotFoundError:
        # Si el archivo no existe, devolver una lista vacía
        return []

# Función para guardar los eventos en el archivo JSON
def guardar_eventos(eventos):
    with open("agenda_eventos.json", "w") as file:
        json.dump({"eventos": eventos}, file, indent=4)

# Función para agregar un nuevo evento
def agregar_evento(eventos, titulo, fecha, ubicacion, organizador):
    nuevo_evento = {
        "titulo": titulo,
        "fecha": fecha,
        "ubicacion": ubicacion,
        "organizador": organizador
    }
    eventos.append(nuevo_evento)
    guardar_eventos(eventos)

# Función para filtrar eventos por fecha
def filtrar_por_fecha(eventos, fecha):
    return [evento for evento in eventos if evento['fecha'] == fecha]

# Función para filtrar eventos por ubicación
def filtrar_por_ubicacion(eventos, ubicacion):
    return [evento for evento in eventos if evento['ubicacion'].lower() == ubicacion.lower()]

# Función para eliminar eventos pasados
def eliminar_eventos_pasados(eventos):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    eventos_futuros = [evento for evento in eventos if evento['fecha'] >= fecha_actual]
    guardar_eventos(eventos_futuros)
    return eventos_futuros

# Función para mostrar todos los eventos
def mostrar_eventos(eventos):
    if not eventos:
        print("No hay eventos disponibles.")
    for evento in eventos:
        print(f"Título: {evento['titulo']}, Fecha: {evento['fecha']}, Ubicación: {evento['ubicacion']}, Organizador: {evento['organizador']}")

# Inicialización de datos
eventos = cargar_eventos()

# Insertar al menos 10 eventos si no existen
if not eventos:
    eventos = [
        {"titulo": "Conferencia Python", "fecha": "2024-11-15", "ubicacion": "Madrid", "organizador": "PyCon España"},
        {"titulo": "Taller de IA", "fecha": "2024-12-01", "ubicacion": "Barcelona", "organizador": "TechFest"},
        {"titulo": "Hackathon de Ciberseguridad", "fecha": "2024-12-10", "ubicacion": "Sevilla", "organizador": "CyberSec Spain"},
        {"titulo": "Feria de Emprendedores", "fecha": "2024-11-20", "ubicacion": "Valencia", "organizador": "Emprende 2024"},
        {"titulo": "Cumbre de Marketing Digital", "fecha": "2024-12-05", "ubicacion": "Madrid", "organizador": "Digital Marketing Expo"},
        {"titulo": "Expo Innovación Tecnológica", "fecha": "2024-11-25", "ubicacion": "Barcelona", "organizador": "Tech Expo"},
        {"titulo": "Seminario de Blockchain", "fecha": "2024-11-30", "ubicacion": "Bilbao", "organizador": "Blockchain Spain"},
        {"titulo": "Congreso de Medicina", "fecha": "2024-12-15", "ubicacion": "Madrid", "organizador": "Medica 2024"},
        {"titulo": "Festival de Música Electrónica", "fecha": "2024-11-18", "ubicacion": "Madrid", "organizador": "Electro Fest"},
        {"titulo": "Reunión de Startups", "fecha": "2024-12-02", "ubicacion": "Madrid", "organizador": "StartUp Week"}
    ]
    guardar_eventos(eventos)

# Ejemplo de uso

# Mostrar todos los eventos
print("Eventos disponibles en la agenda:")
mostrar_eventos(eventos)

# Filtrar eventos por fecha (ejemplo: 2024-11-15)
print("\nFiltrar eventos por fecha '2024-11-15':")
eventos_fecha = filtrar_por_fecha(eventos, "2024-11-15")
for evento in eventos_fecha:
    print(f"Título: {evento['titulo']}, Fecha: {evento['fecha']}, Ubicación: {evento['ubicacion']}, Organizador: {evento['organizador']}")

# Filtrar eventos por ubicación (ejemplo: Madrid)
print("\nFiltrar eventos por ubicación 'Madrid':")
eventos_ubicacion = filtrar_por_ubicacion(eventos, "Madrid")
for evento in eventos_ubicacion:
    print(f"Título: {evento['titulo']}, Fecha: {evento['fecha']}, Ubicación: {evento['ubicacion']}, Organizador: {evento['organizador']}")

# Eliminar eventos pasados
print("\nEliminar eventos pasados:")
eventos_actualizados = eliminar_eventos_pasados(eventos)
mostrar_eventos(eventos_actualizados)

# Agregar un nuevo evento
print("\nAgregar un nuevo evento:")
agregar_evento(eventos, "Seminario de Big Data", "2024-12-20", "Madrid", "Big Data Expo")
print("Evento agregado con éxito.")
mostrar_eventos(eventos)
