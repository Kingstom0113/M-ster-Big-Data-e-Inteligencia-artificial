def es_perfecto(n):
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

# Buscar números perfectos entre 1 y 1000
for num in range(1, 1001):
    if es_perfecto(num):
        print(f"{num} es un número perfecto.")
