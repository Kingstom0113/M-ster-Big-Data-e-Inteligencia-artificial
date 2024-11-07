contador_positivos = 0
contador_negativos = 0
contador_ceros = 0

while True:
    numero = float(input("Introduce un número (o escribe 'salir' para terminar): "))
    
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1
    else:
        contador_ceros += 1
        
    continuar = input("¿Quieres introducir otro número? (si/no): ").lower()
    if continuar != 'si':
        break

print(f"Positivos: {contador_positivos}")
print(f"Negativos: {contador_negativos}")
print(f"Ceros: {contador_ceros}")
