import os

# Crear la subcarpeta si no existe
subcarpeta = "Capitulos"
os.makedirs(subcarpeta, exist_ok=True)

with open("el_quijote.txt", "r", encoding="utf-8") as file:
    contenido = file.read()

# Dividir el contenido por capítulos
capitulos = contenido.split("Capítulo ")

# Iterar sobre los capítulos, omitiendo el primero si es un encabezado antes del primer capítulo
for i, capitulo in enumerate(capitulos[1:], start=1):
    numero = capitulo.split(" ", 1)[0]  # Obtener el número del capítulo (XX, I, etc.)
    contenido_capitulo = "Capítulo " + capitulo  # Añadir "Capítulo" al inicio del texto
    nombre_archivo = os.path.join(subcarpeta, f"Capitulo_{numero}.txt")  # Crear la ruta del archivo
    with open(nombre_archivo, "w", encoding="utf-8") as nuevo_fichero:
        nuevo_fichero.write(contenido_capitulo)

print(f"Los capítulos se han guardado en la subcarpeta '{subcarpeta}'.")
