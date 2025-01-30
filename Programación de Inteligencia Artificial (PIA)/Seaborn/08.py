import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset iris
iris = sns.load_dataset('iris')

# Convertir las columnas numéricas a arrays
iris['sepal_length'] = np.array(iris['sepal_length'])
iris['sepal_width'] = np.array(iris['sepal_width'])
iris['petal_length'] = np.array(iris['petal_length'])
iris['petal_width'] = np.array(iris['petal_width'])

# Crear un pairplot con diferentes tipos de gráficos en la diagonal y fuera de la diagonal
sns.set(style="whitegrid")  # Estilo de fondo blanco con cuadrícula

# Pairplot con diferentes tipos de gráficos en la diagonal y fuera de la diagonal
pairplot = sns.pairplot(
    iris,
    hue="species",                # Colorear según la especie
    diag_kind="hist",             # Histograma en la diagonal
    kind='scatter',               # Tipo de gráfico fuera de la diagonal
    height=2.5,                   # Tamaño de las subparcelas
    aspect=1.2                     # Relación de aspecto de las subparcelas
)

# Agregar una regresión lineal en las relaciones fuera de la diagonal
# Usamos `map_lower` para aplicar `sns.regplot` en la parte inferior de la diagonal
pairplot.map_lower(sns.regplot, scatter_kws={'s': 20}, line_kws={'color': 'red', 'lw': 1})

# Mostrar el gráfico
plt.show()

