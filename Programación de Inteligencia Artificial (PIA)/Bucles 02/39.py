numeros = [int(x) for x in input("Introduce una lista de números separados por espacio: ").split()]

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números impares:", impares)
