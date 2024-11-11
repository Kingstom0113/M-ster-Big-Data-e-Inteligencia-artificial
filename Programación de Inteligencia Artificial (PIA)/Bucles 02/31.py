palabra = input("Introduce una palabra: ").lower()

es_palindromo = True
longitud = len(palabra)

for i in range(longitud // 2):
    if palabra[i] != palabra[longitud - 1 - i]:
        es_palindromo = False
        break

if es_palindromo:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
