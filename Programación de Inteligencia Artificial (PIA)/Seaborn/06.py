import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Cargar el dataset titanic
titanic = sns.load_dataset("titanic").dropna()

# Convertir columnas a arrays de NumPy
class_array = np.array(titanic['class'])
fare_array = np.array(titanic['fare'])

# Aplicar un estilo personalizado
sns.set_style("whitegrid")
plt.figure(figsize=(8, 6))

# Crear el gráfico de barras con agregación
sns.barplot(x="class", y="fare", hue="sex", data=titanic, palette="coolwarm", ci="sd")

# Agregar etiquetas y título
plt.xlabel("Clase")
plt.ylabel("Tarifa Promedio")
plt.title("Promedio de Tarifas Pagadas por Clase con Desviación Estándar")

# Mostrar el gráfico
plt.legend(title="Género")
plt.show()