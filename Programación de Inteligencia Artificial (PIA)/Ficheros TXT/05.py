from collections import Counter
import re

with open("el_quijote.txt", "r", encoding="utf-8") as file:
    contenido = file.read()

# Normalizar el texto (minúsculas y sin puntuación)
contenido = contenido.lower()
contenido = re.sub(r"[^\w\s]", "", contenido)  # Eliminar signos de puntuación

# Dividir el texto en palabras
palabras = contenido.split()

# Contar la frecuencia de las palabras
frecuencias = Counter(palabras)

# Obtener las 10 palabras más comunes
top_10 = frecuencias.most_common(10)

# Mostrar los resultados
print("Las 10 palabras más frecuentes son:")
for palabra, frecuencia in top_10:
    print(f"{palabra}: {frecuencia}")
