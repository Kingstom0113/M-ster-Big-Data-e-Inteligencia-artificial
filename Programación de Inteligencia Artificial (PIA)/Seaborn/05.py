import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset iris
iris = sns.load_dataset("iris")

# Convertir columnas a arrays de NumPy
sepal_length = np.array(iris['sepal_length'])
species = np.array(iris['species'])

# Aplicar un estilo personalizado
sns.set_style("whitegrid")
plt.figure(figsize=(8, 6))

# Crear el gráfico de violín
sns.violinplot(x=iris['species'], y=iris['sepal_length'], inner="point", palette="muted", split=False)

# Agregar etiquetas y título
plt.xlabel("Especie")
plt.ylabel("Longitud del Sépalo")
plt.title("Distribución de la Longitud del Sépalo por Especie")

# Mostrar el gráfico
plt.show()