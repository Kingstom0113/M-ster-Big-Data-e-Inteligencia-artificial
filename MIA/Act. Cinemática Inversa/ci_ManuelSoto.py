import numpy as np
import math
import random

def cinematica_inversa_2dof(x, y, l1, l2):
    """
    Calcula a cinemática inversa de um braço robótico de 2 DOF.

    Args:
        x: Coordenada x do efetor final.
        y: Coordenada y do efetor final.
        l1: Comprimento do primeiro elo.
        l2: Comprimento do segundo elo.

    Returns:
        Tupla de ângulos (theta1, theta2) em graus, ou None se não houver solução.
    """
    try:
        c2 = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
        s2 = math.sqrt(1 - c2**2)

        # Solução para theta2
        theta2_1 = math.atan2(s2, c2)
        theta2_2 = math.atan2(-s2, c2)

        # Solução para theta1
        k1 = l1 + l2 * c2
        k2 = l2 * s2

        theta1_1 = math.atan2(y, x) - math.atan2(k2, k1)
        theta1_2 = math.atan2(y, x) - math.atan2(-k2, k1)

        return (math.degrees(theta1_1), math.degrees(theta2_1)), (math.degrees(theta1_2), math.degrees(theta2_2))
    except ValueError:
        return None # Retorna None caso o valor dentro da raiz quadrada seja negativo.

# Exemplo de uso
longitudes = [10, 8]  # Comprimentos dos elos
posicoes = []
for _ in range(10):
    x = random.uniform(-18, 18)  # Gera x aleatório dentro do alcance
    y = random.uniform(-18, 18)  # Gera y aleatório dentro do alcance
    posicoes.append((x, y))

# Tabela de resultados
print("Posição (x, y) | Ângulos (theta1, theta2) - Solução 1 | Ângulos (theta1, theta2) - Solução 2")
print("-----------------|--------------------------------------|--------------------------------------")

for posicao in posicoes:
    x, y = posicao
    solucoes = cinematica_inversa_2dof(x, y, longitudes[0], longitudes[1])
    if solucoes:
        solucao1, solucao2 = solucoes
        print(f"({x:.2f}, {y:.2f})       | ({solucao1[0]:.2f}, {solucao1[1]:.2f})                       | ({solucao2[0]:.2f}, {solucao2[1]:.2f})")
    else:
        print(f"({x:.2f}, {y:.2f})       | Fora de alcance                                | Fora de alcance")