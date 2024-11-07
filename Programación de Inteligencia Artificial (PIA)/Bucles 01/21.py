suma = 0

while True:
    numero = int(input("Introduce un número (ingresa un número negativo para terminar): "))
    if numero < 0:
        break
    suma += numero

print(f"La suma de los números ingresados es: {suma}")
