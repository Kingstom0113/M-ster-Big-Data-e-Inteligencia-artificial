import random

# Función para simular el lanzamiento de dos dados
def lanzar_dados():
    dado1 = random.randint(1, 6)  # Lanza el primer dado (valor entre 1 y 6)
    dado2 = random.randint(1, 6)  # Lanza el segundo dado (valor entre 1 y 6)
    
    # Muestra los resultados
    print(f"Resultado del primer dado: {dado1}")
    print(f"Resultado del segundo dado: {dado2}")
    
    # Calcula la suma total
    suma = dado1 + dado2
    print(f"Suma total: {suma}")

# Llamada a la función
lanzar_dados()
