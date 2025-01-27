import random
import math
import matplotlib.pyplot as plt

# Generar 20 números enteros aleatorios entre 0 y 100
x_values = random.sample(range(0, 101), 20)

# Calcular la raíz cuadrada de cada número
y_values = [math.sqrt(x) for x in x_values]

# Crear el gráfico de dispersión
plt.scatter(x_values, y_values, color='blue', label='Raíz cuadrada')

# Configurar etiquetas y título
plt.xlabel('Valores (X)')
plt.ylabel('Raíz cuadrada (Y)')
plt.title('Gráfico de dispersión: Valores vs. Raíz cuadrada')

# Agregar una cuadrícula y leyenda
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()
