import random

# Función para crear una baraja de cartas
def crear_baraja():
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    # La baraja es una lista de tuplas con el valor de la carta y su palo
    baraja = [(valor, palo) for palo in palos for valor in valores]
    return baraja

# Función para obtener el valor numérico de una carta
def obtener_valor_carta(carta):
    valor, _ = carta
    if valor in ['J', 'Q', 'K']:
        return 10  # J, Q y K valen 10 puntos
    elif valor == 'A':
        return 11  # As puede valer 11, pero se ajustará si es necesario
    else:
        return int(valor)  # El valor numérico de las cartas 2-10

# Función para repartir una carta
def repartir_carta(baraja):
    carta = random.choice(baraja)
    baraja.remove(carta)  # Elimina la carta de la baraja para no repetirla
    return carta

# Función principal del juego de Blackjack
def juego_blackjack():
    print("¡Bienvenido al Blackjack!")
    
    # Crear la baraja
    baraja = crear_baraja()
    
    # Repartir las cartas iniciales
    mano_jugador = [repartir_carta(baraja), repartir_carta(baraja)]
    mano_dealer = [repartir_carta(baraja), repartir_carta(baraja)]
    
    # Mostrar las cartas iniciales
    print("\nTus cartas:", [f"{valor} de {palo}" for valor, palo in mano_jugador])
    print("Carta del dealer: [", f"{mano_dealer[0][0]} de {mano_dealer[0][1]}", "]")

    # Función para calcular la puntuación total
    def calcular_puntaje(mano):
        puntaje = 0
        ases = 0
        for carta in mano:
            valor, _ = carta
            puntaje += obtener_valor_carta(carta)
            if valor == 'A':
                ases += 1
        # Ajustar los ases si es necesario
        while puntaje > 21 and ases:
            puntaje -= 10
            ases -= 1
        return puntaje

    # El jugador juega
    while True:
        puntaje_jugador = calcular_puntaje(mano_jugador)
        if puntaje_jugador > 21:
            print("\nTus cartas:", [f"{valor} de {palo}" for valor, palo in mano_jugador])
            print(f"Tu puntaje es: {puntaje_jugador}. ¡Te has pasado de 21! Has perdido.")
            return
        
        print(f"\nTu puntaje es: {puntaje_jugador}")
        accion = input("¿Quieres pedir otra carta (s/n)? ").lower()
        
        if accion == 's':
            mano_jugador.append(repartir_carta(baraja))
        elif accion == 'n':
            break
        else:
            print("Opción no válida. Responde 's' para pedir otra carta o 'n' para plantarte.")
    
    # El dealer juega
    print("\nTurno del dealer:")
    while calcular_puntaje(mano_dealer) < 17:
        mano_dealer.append(repartir_carta(baraja))
    
    puntaje_dealer = calcular_puntaje(mano_dealer)
    print(f"Las cartas del dealer son: {[f'{valor} de {palo}' for valor, palo in mano_dealer]}")
    print(f"El puntaje del dealer es: {puntaje_dealer}")
    
    # Determinar el resultado final
    if puntaje_dealer > 21:
        print("\nEl dealer se pasó de 21. ¡Has ganado!")
    elif puntaje_jugador > puntaje_dealer:
        print("\n¡Has ganado!")
    elif puntaje_jugador < puntaje_dealer:
        print("\nEl dealer gana.")
    else:
        print("\nEmpate.")

# Iniciar el juego
juego_blackjack()
