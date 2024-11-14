import random

def generar_apuesta_primitiva():
    # Generar 6 números aleatorios entre 1 y 49 para la apuesta
    apuesta = random.sample(range(1, 50), 6)
    
    # Ordenar los números de la apuesta de menor a mayor
    apuesta.sort()
    
    # Generar un número complementario aleatorio entre 1 y 49
    complementario = random.choice([n for n in range(1, 50) if n not in apuesta])
    
    # Generar un número de reintegro aleatorio entre 0 y 9
    reintegro = random.randint(0, 9)
    
    # Mostrar la apuesta generada
    print("Apuesta de La Primitiva:")
    print(f"Números: {apuesta}")
    print(f"Número Complementario: {complementario}")
    print(f"Número Reintegro: {reintegro}")

# Ejecutar la función para generar una apuesta
generar_apuesta_primitiva()
