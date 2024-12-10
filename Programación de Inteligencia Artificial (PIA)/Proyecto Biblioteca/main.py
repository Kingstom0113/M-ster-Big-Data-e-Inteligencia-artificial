from gestion import (
    alta_libro, listar_libros, baja_libro, modificar_libro,  # Importar las funciones relacionadas con libros
    alta_usuario, listar_usuarios, baja_usuario, modificar_usuario,  # Importar las funciones relacionadas con usuarios
    registrar_prestamo, registrar_devolucion,
    listar_prestamos_pendientes
)

# Rutas de los archivos
LIBROS_FILE = 'datos/biblioLibros.csv'
USUARIOS_FILE = 'datos/biblioUsuarios.csv'
PRESTAMOS_FILE = 'datos/biblioPrestamos.csv'

def menu_principal():
    while True:
        print("\n--- Biblioteca Comarcal ---")
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Registrar Préstamo")
        print("4. Registrar Devolución")
        print("5. Listados de Préstamos Pendientes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestion_libros()
        elif opcion == "2":
            gestion_usuarios()
        elif opcion == "3":
            registrar_prestamo(USUARIOS_FILE, LIBROS_FILE, PRESTAMOS_FILE)
        elif opcion == "4":
            registrar_devolucion(LIBROS_FILE, PRESTAMOS_FILE)
        elif opcion == "5":
            listar_prestamos_pendientes(PRESTAMOS_FILE)
        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def gestion_libros():
    while True:
        print("\n--- Gestión de Libros ---")
        print("1. Alta de Libro")
        print("2. Baja de Libro")
        print("3. Modificar Libro")
        print("4. Listar Libros")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_libro(LIBROS_FILE)
        elif opcion == "2":
            baja_libro(LIBROS_FILE)  # Ya está definida e importada
        elif opcion == "3":
            modificar_libro(LIBROS_FILE)  # Ya está definida e importada
        elif opcion == "4":
            listar_libros(LIBROS_FILE)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def gestion_usuarios():
    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Alta de Usuario")
        print("2. Baja de Usuario")
        print("3. Modificar Usuario")
        print("4. Listar Usuarios")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_usuario(USUARIOS_FILE)
        elif opcion == "2":
            baja_usuario(USUARIOS_FILE)
        elif opcion == "3":
            modificar_usuario(USUARIOS_FILE)
        elif opcion == "4":
            listar_usuarios(USUARIOS_FILE)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()


def gestion_usuarios():
    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Alta de Usuario")
        print("2. Baja de Usuario")
        print("3. Modificar Usuario")
        print("4. Listar Usuarios")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_usuario(USUARIOS_FILE)
        elif opcion == "2":
            baja_usuario(USUARIOS_FILE)
        elif opcion == "3":
            modificar_usuario(USUARIOS_FILE)
        elif opcion == "4":
            listar_usuarios(USUARIOS_FILE)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
