import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset mpg
mpg = sns.load_dataset('mpg')

# Ver las primeras filas del dataset y las columnas
print(mpg.head())  # Ver las primeras filas para inspeccionar el dataset
print(mpg.columns)  # Ver las columnas disponibles

# Convertir las columnas 'horsepower' y 'weight' a arrays de NumPy
mpg['horsepower'] = np.array(mpg['horsepower'])
mpg['weight'] = np.array(mpg['weight'])

# Eliminar filas con valores nulos (en caso de que existan)
mpg.dropna(subset=['horsepower', 'weight'], inplace=True)

# Crear un gráfico de regresión lineal múltiple
sns.set(style="whitegrid")

# Crear el gráfico de regresión lineal múltiple
sns.lmplot(
    x="weight", y="horsepower", data=mpg, 
    aspect=2, height=6, 
    ci=95,  # Nivel de confianza del 95% para la banda de confianza
    scatter_kws={'s': 50, 'alpha': 0.5},  # Estilo de los puntos de dispersión
    line_kws={'color': 'red', 'linewidth': 2}  # Estilo de la línea de regresión
)

# Personalizar el gráfico
plt.title("Regresión Lineal entre Peso y Potencia de los Vehículos", fontsize=16)
plt.xlabel("Peso (Weight)")
plt.ylabel("Potencia (Horsepower)")

# Mostrar el gráfico
plt.tight_layout()
plt.show()
