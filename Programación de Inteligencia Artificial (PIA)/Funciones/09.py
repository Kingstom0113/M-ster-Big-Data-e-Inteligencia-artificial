def ordenar_lista(lista):
    # Implementamos el algoritmo de ordenación por burbuja
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar los elementos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print(ordenar_lista(numeros))  # Salida: [11, 12, 22, 25, 34, 64, 90]