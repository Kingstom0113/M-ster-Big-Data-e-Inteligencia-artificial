cadena = input("Introduce una cadena de texto: ")
cifrada = ""

for caracter in cadena:
    if caracter.isalpha():
        if caracter.islower():
            cifrada += chr(((ord(caracter) - ord('a') + 1) % 26) + ord('a'))
        else:
            cifrada += chr(((ord(caracter) - ord('A') + 1) % 26) + ord('A'))
    else:
        cifrada += caracter

print(f"Cadena cifrada: {cifrada}")
