cadena = input("Introduce una cadena de texto: ")

letras = 0
digitos = 0

for caracter in cadena:
    if caracter.isalpha():
        letras += 1
    elif caracter.isdigit():
        digitos += 1

print(f"Número de letras: {letras}")
print(f"Número de dígitos: {digitos}")
