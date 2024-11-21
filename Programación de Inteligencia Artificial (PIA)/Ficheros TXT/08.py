import re

with open("el_quijote.txt", "r", encoding="utf-8") as file:
    contenido = file.read()

contenido = contenido.replace("\n", " ")  
contenido = re.sub(r"[^\w\s.]", "", contenido) 

frases = contenido.split(". ")

longitudes_frases = [(frase, len(frase)) for frase in frases]

frases_ordenadas = sorted(longitudes_frases, key=lambda x: x[1], reverse=True)

print("Las 5 frases más largas son:")
for i, (frase, longitud) in enumerate(frases_ordenadas[:5], 1):
    print(f"\nFrase {i} (Longitud: {longitud} caracteres):\n{frase.strip()}.\n")
