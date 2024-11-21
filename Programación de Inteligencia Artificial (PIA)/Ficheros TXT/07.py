import re

with open("el_quijote.txt", "r", encoding="utf-8") as file:
    contenido = file.read()

# Normalizar el texto (convertir todo a minúsculas y eliminar puntuación)
contenido = contenido.lower()
contenido = re.sub(r"[^\w\s]", "", contenido)  # Eliminar signos de puntuación

# Dividir el texto en palabras
palabras = contenido.split()

# Calcular la longitud media de las palabras
longitudes = [len(palabra) for palabra in palabras]
longitud_media = sum(longitudes) / len(longitudes) if longitudes else 0

print(f"La longitud media de las palabras en el documento es: {longitud_media:.2f} caracteres.")
