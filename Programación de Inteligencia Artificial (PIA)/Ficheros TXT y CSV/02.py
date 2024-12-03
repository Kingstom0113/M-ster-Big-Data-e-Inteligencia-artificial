import os

# Ruta del fichero del listín telefónico
LISTIN_FILE = "listin.txt"

def crear_listin():
    """Crea el fichero listin.txt si no existe."""
    if not os.path.exists(LISTIN_FILE):
        with open(LISTIN_FILE, "w") as file:
            pass  # Crear el archivo vacío
        print("Fichero 'listin.txt' creado.")
    else:
        print("El fichero 'listin.txt' ya existe.")

def consultar_telefono():
    """Consulta el teléfono de un cliente por su nombre."""
    nombre = input("Introduce el nombre del cliente: ").strip()
    try:
        with open(LISTIN_FILE, "r") as file:
            for linea in file:
                cliente, telefono = linea.strip().split(",")
                if cliente.lower() == nombre.lower():
                    print(f"Teléfono de {cliente}: {telefono}")
                    return
        print(f"No se encontró el cliente '{nombre}' en el listín.")
    except FileNotFoundError:
        print("El fichero 'listin.txt' no existe. Debes crearlo primero.")

def anadir_cliente():
    """Añade un nuevo cliente con su teléfono al listín."""
    nombre = input("Introduce el nombre del cliente: ").strip()
    telefono = input("Introduce el teléfono del cliente: ").strip()
    try:
        with open(LISTIN_FILE, "a") as file:
            file.write(f"{nombre},{telefono}\n")
        print(f"Cliente '{nombre}' añadido con éxito.")
    except FileNotFoundError:
        print("El fichero 'listin.txt' no existe. Debes crearlo primero.")

def eliminar_cliente():
    """Elimina el teléfono de un cliente del listín."""
    nombre = input("Introduce el nombre del cliente a eliminar: ").strip()
    try:
        with open(LISTIN_FILE, "r") as file:
            lineas = file.readlines()
        with open(LISTIN_FILE, "w") as file:
            encontrado = False
            for linea in lineas:
                cliente, telefono = linea.strip().split(",")
                if cliente.lower() != nombre.lower():
                    file.write(linea)
                else:
                    encontrado = True
            if encontrado:
                print(f"Cliente '{nombre}' eliminado con éxito.")
            else:
                print(f"No se encontró el cliente '{nombre}' en el listín.")
    except FileNotFoundError:
        print("El fichero 'listin.txt' no existe. Debes crearlo primero.")

# Menú principal
def menu():
    """Muestra el menú principal y ejecuta las opciones del programa."""
    while True:
        print("\n--- GESTIÓN DEL LISTÍN TELEFÓNICO ---")
        print("1. Crear el fichero del listín (si no existe)")
        print("2. Consultar el teléfono de un cliente")
        print("3. Añadir un nuevo cliente")
        print("4. Eliminar un cliente")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            crear_listin()
        elif opcion == "2":
            consultar_telefono()
        elif opcion == "3":
            anadir_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
