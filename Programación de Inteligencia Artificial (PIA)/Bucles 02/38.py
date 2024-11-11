numeros = [int(x) for x in input("Introduce una lista de números separados por espacio: ").split()]

# Inicializamos el mayor y el segundo mayor
mayor = segundo_mayor = float('-inf')

for num in numeros:
    if num > mayor:
        segundo_mayor = mayor
        mayor = num
    elif num > segundo_mayor and num != mayor:
        segundo_mayor = num

if segundo_mayor == float('-inf'):
    print("No hay un segundo número más grande en la lista.")
else:
    print(f"El segundo número más grande en la lista es: {segundo_mayor}")
