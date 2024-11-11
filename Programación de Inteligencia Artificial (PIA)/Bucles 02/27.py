import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Bienvenido al juego de adivinanza!")
print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")

while True:
    # Solicitar al usuario que ingrese un número
    intento = int(input("Introduce tu suposición: "))
    intentos += 1
    
    if intento < numero_secreto:
        print("El número es mayor. ¡Intenta de nuevo!")
    elif intento > numero_secreto:
        print("El número es menor. ¡Intenta de nuevo!")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        break
