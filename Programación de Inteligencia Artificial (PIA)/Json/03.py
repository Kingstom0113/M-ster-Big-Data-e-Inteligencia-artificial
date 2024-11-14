import json
from datetime import datetime

# Función para cargar las tareas desde el archivo JSON
def cargar_tareas():
    try:
        with open("agenda_tareas.json", "r") as file:
            data = json.load(file)
            return data['tareas']
    except FileNotFoundError:
        # Si el archivo no existe, devolver una lista vacía
        return []

# Función para guardar las tareas en el archivo JSON
def guardar_tareas(tareas):
    with open("agenda_tareas.json", "w") as file:
        json.dump({"tareas": tareas}, file, indent=4)

# Función para agregar una nueva tarea
def agregar_tarea(tareas, descripcion, vencimiento, estado="pendiente"):
    nueva_tarea = {
        "descripcion": descripcion,
        "vencimiento": vencimiento,
        "estado": estado
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)

# Función para actualizar el estado de una tarea
def actualizar_estado(tareas, descripcion, nuevo_estado):
    for tarea in tareas:
        if tarea['descripcion'].lower() == descripcion.lower():
            tarea['estado'] = nuevo_estado
            guardar_tareas(tareas)
            print(f"La tarea '{descripcion}' ha sido actualizada a '{nuevo_estado}'.")
            return
    print(f"No se encontró una tarea con la descripción '{descripcion}'.")

# Función para filtrar las tareas completadas
def filtrar_tareas_completadas(tareas):
    return [tarea for tarea in tareas if tarea['estado'].lower() == 'completada']

# Función para mostrar todas las tareas
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas en la agenda.")
    for tarea in tareas:
        print(f"Descripción: {tarea['descripcion']}, Vencimiento: {tarea['vencimiento']}, Estado: {tarea['estado']}")

# Función para filtrar tareas por fecha de vencimiento
def filtrar_por_fecha(tareas, fecha):
    return [tarea for tarea in tareas if tarea['vencimiento'] == fecha]

# Inicialización de datos
tareas = cargar_tareas()

# Insertar al menos 10 tareas si no existen tareas
if not tareas:
    tareas = [
        {"descripcion": "Estudiar Python", "vencimiento": "2024-11-01", "estado": "pendiente"},
        {"descripcion": "Revisar proyecto", "vencimiento": "2024-10-29", "estado": "completada"},
        {"descripcion": "Comprar comestibles", "vencimiento": "2024-11-02", "estado": "pendiente"},
        {"descripcion": "Enviar reporte", "vencimiento": "2024-11-03", "estado": "pendiente"},
        {"descripcion": "Llamar al cliente", "vencimiento": "2024-10-30", "estado": "completada"},
        {"descripcion": "Leer libro", "vencimiento": "2024-11-04", "estado": "pendiente"},
        {"descripcion": "Ir al gimnasio", "vencimiento": "2024-11-05", "estado": "pendiente"},
        {"descripcion": "Revisar correo", "vencimiento": "2024-10-28", "estado": "completada"},
        {"descripcion": "Hacer compras online", "vencimiento": "2024-11-06", "estado": "pendiente"},
        {"descripcion": "Reunión con equipo", "vencimiento": "2024-11-07", "estado": "completada"}
    ]
    guardar_tareas(tareas)

# Ejemplo de uso

# Mostrar todas las tareas
print("Tareas actuales en la agenda:")
mostrar_tareas(tareas)

# Agregar una nueva tarea
agregar_tarea(tareas, "Pasear al perro", "2024-11-08", "pendiente")

# Actualizar estado de una tarea
print("\nActualizar estado de 'Estudiar Python' a 'completada':")
actualizar_estado(tareas, "Estudiar Python", "completada")

# Filtrar tareas completadas
print("\nTareas completadas:")
tareas_completadas = filtrar_tareas_completadas(tareas)
for tarea in tareas_completadas:
    print(f"Descripción: {tarea['descripcion']}, Vencimiento: {tarea['vencimiento']}, Estado: {tarea['estado']}")

# Filtrar tareas por fecha de vencimiento
print("\nTareas con vencimiento en '2024-11-01':")
tareas_fecha = filtrar_por_fecha(tareas, "2024-11-01")
for tarea in tareas_fecha:
    print(f"Descripción: {tarea['descripcion']}, Vencimiento: {tarea['vencimiento']}, Estado: {tarea['estado']}")
