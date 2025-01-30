import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Cargar el dataset diamonds
diamonds = sns.load_dataset("diamonds")

# Convertir columnas a arrays de NumPy
carat = np.array(diamonds['carat'])
price = np.array(diamonds['price'])
depth = np.array(diamonds['depth'])

# Aplicar un estilo personalizado
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Crear el gráfico de caja
sns.boxplot(x=pd.cut(diamonds['carat'], bins=[0, 1, 2, 3, 4, 5]), y=diamonds['price'], hue=diamonds['cut'], palette="pastel")

# Agregar etiquetas y título
plt.xlabel("Rango de Quilates")
plt.ylabel("Precio")
plt.title("Distribución de Precios por Rango de Quilates y Tipo de Corte")

# Mostrar el gráfico
plt.legend(title="Tipo de Corte")
plt.show()
