numeros = [10, -5, 8, 0, -3, 15, 7] 
suma_positivos = 0

for numero in numeros:
    if numero > 0:
        suma_positivos += numero

print(f"La suma de los números positivos es: {suma_positivos}")
