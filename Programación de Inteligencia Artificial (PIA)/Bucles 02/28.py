suma = 0
contador = 0

while True:
    numero = float(input("Introduce un número (ingresa 0 para terminar): "))
    
    if numero == 0:
        break
    
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    print("No se ingresaron números válidos para calcular el promedio.")
