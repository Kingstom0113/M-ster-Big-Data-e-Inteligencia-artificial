numeros = input("Introduce una lista de números separados por espacios: ").split()
numeros = [int(numero) for numero in numeros]

mayor = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
