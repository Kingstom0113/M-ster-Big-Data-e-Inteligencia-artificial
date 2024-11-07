numero = int(input("Introduce un número entre 1 y 100: "))

intentos = 0

while intentos < 5:
    intento = int(input("Adivina el número: "))
    intentos += 1
    
    if intento == numero:
        print("¡Felicidades! Adivinaste el número.")
        break
    elif intento < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    
else:
    print("Lo siento, no adivinaste el número en 5 intentos.")
