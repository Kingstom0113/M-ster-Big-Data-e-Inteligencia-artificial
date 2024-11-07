cadena = input("Introduce una cadena de texto: ").lower()

vocales = "aeiou"
consonantes = "bcdfghjklmnpqrstvwxyz"

contador_vocales = 0
contador_consonantes = 0

for caracter in cadena:
    if caracter in vocales:
        contador_vocales += 1
    elif caracter in consonantes:
        contador_consonantes += 1

print(f"Vocales: {contador_vocales}")
print(f"Consonantes: {contador_consonantes}")
