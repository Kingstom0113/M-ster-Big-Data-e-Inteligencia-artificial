palabra = input("Ingrese una palabra: ")

contador_vocales = 0

vocales = "aeiouAEIOU"

for caracter in palabra:
    if caracter in vocales:
        contador_vocales += 1

print(f"El número total de vocales en la palabra es: {contador_vocales}")