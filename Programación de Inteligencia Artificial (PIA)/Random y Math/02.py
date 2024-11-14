import random

# Función para simular el giro de la ruleta
def giro_ruleta():
    # Los números posibles de la ruleta (1-36 y 0)
    numeros = list(range(1, 37)) + [0]  # Crea una lista con los números del 1 al 36 y el 0
    resultado = random.choice(numeros)  # Elige aleatoriamente un número de la lista

    # Muestra el número resultante
    if resultado == 0:
        print("¡Gana la banca! El número es 0.")
    else:
        print(f"El número de la ruleta es: {resultado}")

# Llamada a la función
giro_ruleta()
