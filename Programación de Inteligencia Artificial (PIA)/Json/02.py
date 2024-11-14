import json

# Función para cargar los contactos desde el archivo JSON
def cargar_contactos():
    try:
        with open("directorio_telefonico.json", "r") as file:
            data = json.load(file)
            return data['contactos']
    except FileNotFoundError:
        # Si el archivo no existe, devolver una lista vacía
        return []

# Función para guardar los contactos en el archivo JSON
def guardar_contactos(contactos):
    with open("directorio_telefonico.json", "w") as file:
        json.dump({"contactos": contactos}, file, indent=4)

# Función para agregar un nuevo contacto
def agregar_contacto(contactos, nombre, apellidos, telefono, correo):
    nuevo_contacto = {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo
    }
    contactos.append(nuevo_contacto)
    guardar_contactos(contactos)

# Función para buscar un contacto por nombre
def buscar_contacto(contactos, nombre_buscar):
    resultados = [contacto for contacto in contactos if nombre_buscar.lower() in contacto['nombre'].lower()]
    return resultados

# Función para actualizar el número de teléfono de un contacto
def actualizar_telefono(contactos, nombre, nuevo_telefono):
    for contacto in contactos:
        if contacto['nombre'].lower() == nombre.lower():
            contacto['telefono'] = nuevo_telefono
            guardar_contactos(contactos)
            print(f"El número de teléfono de {nombre} ha sido actualizado.")
            return
    print(f"No se encontró un contacto con el nombre {nombre}.")

# Función para eliminar un contacto
def eliminar_contacto(contactos, nombre):
    for contacto in contactos:
        if contacto['nombre'].lower() == nombre.lower():
            contactos.remove(contacto)
            guardar_contactos(contactos)
            print(f"El contacto de {nombre} ha sido eliminado.")
            return
    print(f"No se encontró un contacto con el nombre {nombre}.")

# Función para mostrar todos los contactos
def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos disponibles.")
    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']} {contacto['apellidos']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")

# Inicialización de datos
contactos = cargar_contactos()

# Insertar al menos 10 registros telefónicos
if not contactos:
    contactos = [
        {"nombre": "Juan", "apellidos": "Pérez", "telefono": "612345678", "correo": "juan@example.com"},
        {"nombre": "Laura", "apellidos": "Gómez", "telefono": "623456789", "correo": "laura@example.com"},
        {"nombre": "Carlos", "apellidos": "Martínez", "telefono": "634567890", "correo": "carlos@example.com"},
        {"nombre": "Ana", "apellidos": "Rodríguez", "telefono": "645678901", "correo": "ana@example.com"},
        {"nombre": "Luis", "apellidos": "Sánchez", "telefono": "656789012", "correo": "luis@example.com"},
        {"nombre": "Marta", "apellidos": "Hernández", "telefono": "667890123", "correo": "marta@example.com"},
        {"nombre": "José", "apellidos": "López", "telefono": "678901234", "correo": "jose@example.com"},
        {"nombre": "Pedro", "apellidos": "González", "telefono": "689012345", "correo": "pedro@example.com"},
        {"nombre": "Elena", "apellidos": "Ruiz", "telefono": "690123456", "correo": "elena@example.com"},
        {"nombre": "Sofia", "apellidos": "Vázquez", "telefono": "701234567", "correo": "sofia@example.com"}
    ]
    guardar_contactos(contactos)

# Ejemplo de uso

# Mostrar los contactos
print("Contactos actuales:")
mostrar_contactos(contactos)

# Agregar un nuevo contacto
agregar_contacto(contactos, "Miguel", "Álvarez", "712345678", "miguel@example.com")

# Buscar un contacto por nombre
print("\nBuscar contacto por nombre 'Carlos':")
resultados = buscar_contacto(contactos, "Carlos")
for resultado in resultados:
    print(f"Encontrado: {resultado['nombre']} {resultado['apellidos']}, Teléfono: {resultado['telefono']}, Correo: {resultado['correo']}")

# Actualizar teléfono de un contacto
print("\nActualizar teléfono de 'Laura':")
actualizar_telefono(contactos, "Laura", "800000000")

# Eliminar un contacto
print("\nEliminar contacto 'Pedro':")
eliminar_contacto(contactos, "Pedro")

# Mostrar los contactos después de los cambios
print("\nContactos después de agregar, actualizar y eliminar:")
mostrar_contactos(contactos)
