inicio = int(input("Introduce el valor inicial del rango: "))
fin = int(input("Introduce el valor final del rango: "))

suma = 0

for numero in range(inicio, fin + 1):
    suma += numero

print(f"La suma de los números en el rango de {inicio} a {fin} es: {suma}")
