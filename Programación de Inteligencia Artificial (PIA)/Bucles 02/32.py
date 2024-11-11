numeros = [int(x) for x in input("Introduce una lista de números separados por espacio: ").split()]

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print(f"El número más grande en la lista es: {mayor}")
