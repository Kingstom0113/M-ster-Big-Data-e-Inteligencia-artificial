inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el fin del rango: "))

suma_pares = 0

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        suma_pares += numero

print(f"La suma de los números pares en el rango de {inicio} a {fin} es {suma_pares}.")
