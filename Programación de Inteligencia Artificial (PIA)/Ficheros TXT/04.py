with open("el_quijote.txt", "r", encoding="utf-8") as file:
    contenido = file.read()

# Convertir el texto a minúsculas
contenido = contenido.lower()

# Contar las palabras
dulcinea_count = contenido.count("dulcinea")
quijote_count = contenido.count("quijote")
sancho_count = contenido.count("sancho")

print(f"Dulcinea aparece {dulcinea_count} veces.")
print(f"Quijote aparece {quijote_count} veces.")
print(f"Sancho aparece {sancho_count} veces.")
