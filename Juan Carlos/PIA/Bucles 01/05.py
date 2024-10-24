palabra = input("Ingrese una palabra: ")

inicio = 0
fin = len(palabra) - 1

es_palindromo = True
while inicio < fin:
    if palabra[inicio] != palabra[fin]:
        es_palindromo = False
        break
    inicio += 1
    fin -= 1

if es_palindromo:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")