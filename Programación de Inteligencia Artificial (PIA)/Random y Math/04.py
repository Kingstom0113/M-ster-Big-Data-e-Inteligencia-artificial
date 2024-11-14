import random

# Función para simular el giro de la ruleta
def giro_ruleta():
    # Los números posibles de la ruleta (1-36 y 0)
    numeros = list(range(1, 37)) + [0]  # Crea una lista con los números del 1 al 36 y el 0
    return random.choice(numeros)  # Elige aleatoriamente un número de la lista

# Función principal del juego
def juego_ruleta():
    print("¡Bienvenido al juego de la ruleta!")
    try:
        # Solicita al jugador que adivine el número
        adivinanza = int(input("Adivina el número de la ruleta (entre 0 y 36): "))
        
        # Verifica que la entrada sea válida
        if adivinanza < 0 or adivinanza > 36:
            print("Por favor, ingresa un número entre 0 y 36.")
            return
        
        # Realiza el giro de la ruleta
        resultado = giro_ruleta()
        
        # Muestra el resultado del giro
        print(f"El número de la ruleta es: {resultado}")
        
        # Verifica si el jugador acertó
        if adivinanza == resultado:
            print("¡Felicidades! Has acertado el número.")
        else:
            print("Lo siento, no has acertado. ¡Intenta de nuevo!")
    
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Llamada a la función para comenzar el juego
juego_ruleta()
