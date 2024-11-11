numeros = input("Introduce una lista de números separados por espacios: ").split()
numeros = [float(numero) for numero in numeros]

suma = 0
for numero in numeros:
    suma += numero

promedio = suma / len(numeros)
print(f"El promedio de la lista es: {promedio}")
