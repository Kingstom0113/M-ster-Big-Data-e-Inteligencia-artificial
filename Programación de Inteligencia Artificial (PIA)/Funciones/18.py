# Definir la lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usar filter() con lambda para filtrar los números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Imprimir los números pares
print(pares)
