import random

# Función para crear la baraja de cartas
def crear_baraja():
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    baraja = [f"{valor} de {palo}" for palo in palos for valor in valores]
    return baraja

# Función para repartir 5 cartas al azar
def repartir_cartas():
    baraja = crear_baraja()
    random.shuffle(baraja)  # Mezcla la baraja
    cartas_repartidas = baraja[:5]  # Reparte las primeras 5 cartas
    return cartas_repartidas

# Llamada a la función para repartir las cartas
cartas = repartir_cartas()

# Mostrar las cartas repartidas
print("Las 5 cartas repartidas son:")
for carta in cartas:
    print(carta)
