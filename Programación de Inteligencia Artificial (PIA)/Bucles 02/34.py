def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Solicitar al usuario ingresar una lista de números
numeros = [int(x) for x in input("Introduce una lista de números separados por espacio: ").split()]

if esta_ordenada(numeros):
    print("La lista está ordenada de manera ascendente.")
else:
    print("La lista no está ordenada de manera ascendente.")
