import random

numero_secreto = random.randint(1, 100)

adivinanza = int(input("Adivina el número secreto (entre 1 y 100): "))

while adivinanza != numero_secreto:
    if adivinanza < numero_secreto:
        print("Demasiado bajo. Intenta nuevamente.")
    else:
        print("Demasiado alto. Intenta nuevamente.")
    adivinanza = int(input("Adivina el número secreto (entre 1 y 100): "))

print(f"Adivinaste el número secreto: {numero_secreto}")