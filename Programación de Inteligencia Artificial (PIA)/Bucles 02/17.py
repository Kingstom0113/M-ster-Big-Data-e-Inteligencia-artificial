caracter = input("Introduce un carácter: ").lower()

if caracter in 'aeiou':
    print(f"El carácter '{caracter}' es una vocal.")
else:
    print(f"El carácter '{caracter}' no es una vocal.")
