import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset de penguins
penguins = sns.load_dataset("penguins").dropna()

# Seleccionar solo las columnas numéricas
numeric_penguins = penguins.select_dtypes(include=[np.number])

# Convertir a arrays de NumPy
penguins_arrays = numeric_penguins.to_numpy()

# Calcular la matriz de correlación
correlation_matrix = numeric_penguins.corr()

# Aplicar un estilo personalizado
sns.set_style("whitegrid")
plt.figure(figsize=(8, 6))

# Crear el mapa de calor
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

# Agregar título
plt.title("Mapa de Calor de Correlación - Penguins")

# Mostrar el gráfico
plt.show()
