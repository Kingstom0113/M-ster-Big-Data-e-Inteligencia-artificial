lista1 = input("Introduce los elementos de la primera lista separados por espacios: ").split()
lista2 = input("Introduce los elementos de la segunda lista separados por espacios: ").split()

coincidencias = 0

for elemento in lista1:
    if elemento in lista2:
        coincidencias += 1

print(f"El número de elementos que coinciden es: {coincidencias}")
