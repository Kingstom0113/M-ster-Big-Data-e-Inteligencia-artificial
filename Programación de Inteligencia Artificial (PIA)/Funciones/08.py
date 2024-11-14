def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'  # Definimos las vocales en minúscula y mayúscula
    contador = 0  # Inicializamos un contador en 0
    for char in cadena:
        if char in vocales:
            contador += 1  # Incrementamos el contador si el carácter es una vocal
    return contador

print(contar_vocales("Hola Mundo"))  # Salida: 4, porque hay 4 vocales (o, a, u, o)
print(contar_vocales("Python"))     # Salida: 1, porque solo hay una vocal (o)
