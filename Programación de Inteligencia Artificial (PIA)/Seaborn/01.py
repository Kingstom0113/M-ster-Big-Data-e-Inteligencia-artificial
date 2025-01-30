import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset de automóviles
mpg = sns.load_dataset("mpg").dropna()  # Eliminar valores nulos

# Convertir columnas a arrays de NumPy
horsepower = np.array(mpg['horsepower'])
weight = np.array(mpg['weight'])
mpg_values = np.array(mpg['mpg'])

# Aplicar un estilo personalizado
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Crear el gráfico de dispersión
scatter = plt.scatter(horsepower, mpg_values, s=weight/10, c=mpg_values, cmap='coolwarm', alpha=0.7, edgecolors='k')

# Agregar etiquetas y título
plt.xlabel("Caballos de fuerza")
plt.ylabel("Millas por galón (mpg)")
plt.title("Relación entre Caballos de Fuerza y Eficiencia de Combustible")
plt.colorbar(label="Eficiencia de combustible (mpg)")

# Mostrar el gráfico
plt.show()
