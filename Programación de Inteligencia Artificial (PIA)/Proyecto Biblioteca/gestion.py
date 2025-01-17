import csv
from datetime import datetime
from clases.libro import Libro
from clases.usuario import Usuario
from clases.prestamo import Prestamo


# Función para leer datos desde un archivo CSV
def read_csv(file_path):
    """Lee y devuelve los registros de un archivo CSV como una lista de diccionarios."""
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


# Función para escribir datos en un archivo CSV
def write_csv(file_path, data, fieldnames):
    """Escribe una lista de diccionarios en un archivo CSV."""
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# Validación de fechas en formato español (DD-MM-AAAA)
def validar_fecha(fecha):
    """Valida que una fecha ingresada tenga el formato DD-MM-AAAA."""
    try:
        return datetime.strptime(fecha, "%d-%m-%Y")
    except ValueError:
        print("Formato de fecha inválido. Por favor, use el formato DD-MM-AAAA.")
        return None


### Gestión de Libros ###

def alta_libro(file_path):
    """Permite registrar un nuevo libro en la biblioteca."""
    libros = read_csv(file_path)
    id_libro = input("ID del Libro: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    anyo = input("Año: ")
    n_pags = input("Número de Páginas: ")
    genero = input("Género: ")
    editorial = input("Editorial: ")
    estado = input("Estado: ")
    disponible = "Sí"

    nuevo_libro = Libro(id_libro, titulo, autor, anyo, n_pags, genero, editorial, estado, disponible)
    libros.append(nuevo_libro.to_dict())
    write_csv(file_path, libros, nuevo_libro.to_dict().keys())
    print("Libro añadido correctamente.")


def listar_libros(file_path):
    """Muestra un listado de los libros registrados en la biblioteca."""
    libros = read_csv(file_path)
    if not libros:
        print("No hay libros registrados.")
        return

    for libro in libros:
        print(f"ID: {libro['id_libro']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Disponible: {libro['disponible']}")


def baja_libro(file_path):
    """Permite eliminar un libro del sistema por su ID."""
    libros = read_csv(file_path)
    id_libro = input("ID del Libro a eliminar: ")
    libro = next((l for l in libros if l['id_libro'] == id_libro), None)

    if not libro:
        print("El libro no existe.")
        return

    libros = [l for l in libros if l['id_libro'] != id_libro]
    write_csv(file_path, libros, libros[0].keys())
    print("Libro eliminado correctamente.")


def modificar_libro(file_path):
    """Permite modificar los datos de un libro existente."""
    libros = read_csv(file_path)
    id_libro = input("ID del Libro a modificar: ")
    libro = next((l for l in libros if l['id_libro'] == id_libro), None)

    if not libro:
        print("El libro no existe.")
        return

    # Modificar los datos
    libro['titulo'] = input(f"Título ({libro['titulo']}): ") or libro['titulo']
    libro['autor'] = input(f"Autor ({libro['autor']}): ") or libro['autor']
    libro['anyo'] = input(f"Año ({libro['anyo']}): ") or libro['anyo']
    libro['n_pags'] = input(f"Número de Páginas ({libro['n_pags']}): ") or libro['n_pags']
    libro['genero'] = input(f"Género ({libro['genero']}): ") or libro['genero']
    libro['editorial'] = input(f"Editorial ({libro['editorial']}): ") or libro['editorial']
    libro['estado'] = input(f"Estado ({libro['estado']}): ") or libro['estado']

    # Actualizar y guardar los cambios
    write_csv(file_path, libros, libros[0].keys())
    print("Libro modificado correctamente.")


### Gestión de Usuarios ###

def alta_usuario(file_path):
    """Permite registrar un nuevo usuario en el sistema."""
    usuarios = read_csv(file_path)
    id_usuario = input("ID del Usuario: ")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    dni = input("DNI: ")
    correo_e = input("Correo Electrónico: ")
    tlfno = input("Teléfono: ")
    direccion = input("Dirección: ")
    edad = input("Edad: ")

    nuevo_usuario = Usuario(id_usuario, nombre, apellidos, dni, correo_e, tlfno, direccion, edad)
    usuarios.append(nuevo_usuario.to_dict())
    write_csv(file_path, usuarios, nuevo_usuario.to_dict().keys())
    print("Usuario añadido correctamente.")


def listar_usuarios(file_path):
    """Muestra un listado de los usuarios registrados en el sistema."""
    usuarios = read_csv(file_path)
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for usuario in usuarios:
        print(f"ID: {usuario['id_usuario']}, Nombre: {usuario['nombre']}, Correo: {usuario['correo_e']}")


def baja_usuario(file_path):
    """Permite eliminar un usuario del sistema por su ID."""
    usuarios = read_csv(file_path)
    id_usuario = input("ID del Usuario a eliminar: ")
    usuario = next((u for u in usuarios if u['id_usuario'] == id_usuario), None)

    if not usuario:
        print("El usuario no existe.")
        return

    usuarios = [u for u in usuarios if u['id_usuario'] != id_usuario]
    write_csv(file_path, usuarios, usuarios[0].keys())
    print("Usuario eliminado correctamente.")


def modificar_usuario(file_path):
    """Permite modificar los datos de un usuario existente."""
    usuarios = read_csv(file_path)
    id_usuario = input("ID del Usuario a modificar: ")
    usuario = next((u for u in usuarios if u['id_usuario'] == id_usuario), None)

    if not usuario:
        print("El usuario no existe.")
        return

    # Modificar los datos
    usuario['nombre'] = input(f"Nombre ({usuario['nombre']}): ") or usuario['nombre']
    usuario['apellidos'] = input(f"Apellidos ({usuario['apellidos']}): ") or usuario['apellidos']
    usuario['dni'] = input(f"DNI ({usuario['dni']}): ") or usuario['dni']
    usuario['correo_e'] = input(f"Correo Electrónico ({usuario['correo_e']}): ") or usuario['correo_e']
    usuario['tlfno'] = input(f"Teléfono ({usuario['tlfno']}): ") or usuario['tlfno']
    usuario['direccion'] = input(f"Dirección ({usuario['direccion']}): ") or usuario['direccion']
    usuario['edad'] = input(f"Edad ({usuario['edad']}): ") or usuario['edad']

    # Actualizar y guardar los cambios
    write_csv(file_path, usuarios, usuarios[0].keys())
    print("Usuario modificado correctamente.")

    ### Gestión de Préstamos ###

def registrar_prestamo(usuarios_file, libros_file, prestamos_file):
    """Registra un préstamo de un libro a un usuario."""
    usuarios = read_csv(usuarios_file)
    libros = read_csv(libros_file)
    prestamos = read_csv(prestamos_file)

    id_usuario = input("ID del Usuario: ")
    usuario = next((u for u in usuarios if u['id_usuario'] == id_usuario), None)
    if not usuario:
        print("Usuario no encontrado. Debe registrarlo primero.")
        return

    id_libro = input("ID del Libro: ")
    libro = next((l for l in libros if l['id_libro'] == id_libro), None)
    if not libro:
        print("Libro no encontrado.")
        return

    if libro['disponible'].lower() != "sí":
        print("El libro no está disponible para préstamo.")
        return

    fecha_inicio = input("Fecha de inicio (DD-MM-AAAA): ")
    fecha_validada_inicio = validar_fecha(fecha_inicio)
    if not fecha_validada_inicio:
        return

    fecha_fin = input("Fecha de fin (DD-MM-AAAA): ")
    fecha_validada_fin = validar_fecha(fecha_fin)
    if not fecha_validada_fin:
        return

    id_prestamo = f"P-{len(prestamos) + 1}"
    nuevo_prestamo = Prestamo(id_prestamo, id_usuario, id_libro, fecha_inicio, fecha_fin, "")

    prestamos.append(nuevo_prestamo.to_dict())
    write_csv(prestamos_file, prestamos, nuevo_prestamo.to_dict().keys())

    # Marcar el libro como no disponible
    for l in libros:
        if l['id_libro'] == id_libro:
            l['disponible'] = "No"
            break
    write_csv(libros_file, libros, libros[0].keys())

    print("Préstamo registrado correctamente.")


def registrar_devolucion(libros_file, prestamos_file):
    """Registra la devolución de un libro prestado."""
    libros = read_csv(libros_file)
    prestamos = read_csv(prestamos_file)

    id_prestamo = input("ID del Préstamo: ")
    prestamo = next((p for p in prestamos if p['id_prestamo'] == id_prestamo), None)
    if not prestamo:
        print("Préstamo no encontrado.")
        return

    if prestamo['fecha_devolucion']:
        print("El préstamo ya fue devuelto.")
        return

    fecha_devolucion = input("Fecha de devolución (DD-MM-AAAA): ")
    fecha_validada = validar_fecha(fecha_devolucion)
    if not fecha_validada:
        return

    prestamo['fecha_devolucion'] = fecha_devolucion

    # Marcar el libro como disponible
    for l in libros:
        if l['id_libro'] == prestamo['idlibro']:
            l['disponible'] = "Sí"
            break

    write_csv(prestamos_file, prestamos, prestamos[0].keys())
    write_csv(libros_file, libros, libros[0].keys())
    print("Devolución registrada correctamente.")


def listar_prestamos_pendientes(prestamos_file):
    """Lista los préstamos que aún no han sido devueltos."""
    prestamos = read_csv(prestamos_file)
    pendientes = [p for p in prestamos if not p['fecha_devolucion']]

    if not pendientes:
        print("No hay préstamos pendientes.")
        return

    print("\n--- Préstamos Pendientes ---")
    for prestamo in pendientes:
        print(f"ID Préstamo: {prestamo['id_prestamo']}, ID Usuario: {prestamo['id_usuario']}, "
              f"ID Libro: {prestamo['id_libro']}, Fecha Inicio: {prestamo['fecha_inicio']}, Fecha Fin: {prestamo['fecha_fin']}")

