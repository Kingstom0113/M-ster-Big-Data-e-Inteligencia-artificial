from collections import Counter
import re

with open("el_quijote.txt", "r", encoding="utf-8") as file:
    lineas = file.readlines()

# Normalizar el texto
contenido = [re.sub(r"[^\w\s]", "", linea.lower()) for linea in lineas]

# Dividir el texto en palabras por línea y guardar el índice de línea
palabra_linea = {}
for i, linea in enumerate(contenido, start=1):
    for palabra in linea.split():
        if palabra not in palabra_linea:
            palabra_linea[palabra] = i

# Contar la frecuencia de palabras en todo el texto
contenido_completo = " ".join(contenido)
frecuencias = Counter(contenido_completo.split())

# Obtener las palabras más comunes con la primera línea donde aparecen
top_frecuentes = frecuencias.most_common(10)
resultado = [(palabra, frecuencia, palabra_linea[palabra]) for palabra, frecuencia in top_frecuentes]

# Mostrar los resultados
print("Las palabras más frecuentes y la primera línea donde aparecen:")
for palabra, frecuencia, linea in resultado:
    print(f"{palabra}: {frecuencia} veces, primera aparición en la línea {linea}")
