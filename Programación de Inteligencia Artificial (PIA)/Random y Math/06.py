import random

# Función para simular una quiniela de 15 partidos
def simulacion_quiniela():
    # Los posibles resultados para cada partido
    resultados_posibles = ['1', 'X', '2']
    
    # Crear una lista para almacenar los resultados de los 15 partidos
    resultados = []
    
    print("Simulación de Quiniela con 15 partidos:")
    
    # Simular los 15 partidos
    for i in range(1, 16):
        resultado = random.choice(resultados_posibles)  # Elegir un resultado aleatorio
        resultados.append(f"Partido {i}: {resultado}")
    
    # Mostrar los resultados de todos los partidos
    for resultado in resultados:
        print(resultado)

# Ejecutar la simulación de la quiniela
simulacion_quiniela()
