import numpy as np
import math

def matriz_transformacion_homogenea(angulo, longitud):
    """
    Crea una matriz de transformación homogénea para un eslabón de un brazo robótico.

    Args:
        angulo: Ángulo de la articulación en grados.
        longitud: Longitud del eslabón.

    Returns:
        Matriz de transformación homogénea de 4x4.
    """
    angulo_rad = math.radians(angulo)
    matriz = np.array([
        [math.cos(angulo_rad), -math.sin(angulo_rad), 0, longitud * math.cos(angulo_rad)],
        [math.sin(angulo_rad), math.cos(angulo_rad), 0, longitud * math.sin(angulo_rad)],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return matriz

def cinematica_directa_2dof(angulos, longitudes):
    """
    Calcula la cinemática directa de un brazo robótico de 2 DOF.

    Args:
        angulos: Lista de ángulos de las articulaciones en grados.
        longitudes: Lista de longitudes de los eslabones.

    Returns:
        Coordenadas (x, y) del efector final.
    """
    T01 = matriz_transformacion_homogenea(angulos[0], longitudes[0])
    T12 = matriz_transformacion_homogenea(angulos[1], longitudes[1])
    T02 = np.dot(T01, T12)
    x = T02[0, 3]
    y = T02[1, 3]
    return x, y

# Ejemplo de uso
angulos = [(30, 45), (60, 90), (0, 180), (-45, 120)]
longitudes = [10, 8]  # Longitudes de los eslabones

for angulo in angulos:
    x, y = cinematica_directa_2dof(angulo, longitudes)
    print(f"Ángulos: {angulo}, Posición del efector final: ({x:.2f}, {y:.2f})")