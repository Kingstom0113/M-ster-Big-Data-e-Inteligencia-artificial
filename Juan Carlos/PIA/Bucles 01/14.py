numeros = [3, 41, 12, 9, 74, 15]

numero_mas_grande = numeros[0]

for numero in numeros:
    if numero > numero_mas_grande:
        numero_mas_grande = numero

print(f"El número más grande en la lista es: {numero_mas_grande}")