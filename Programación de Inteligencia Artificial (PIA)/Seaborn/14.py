import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset Titanic
titanic = sns.load_dataset('titanic')

# Verificar las columnas relevantes
print(titanic[['age', 'pclass']].head())

# Convertir las columnas de 'age' y 'pclass' a arrays de NumPy
age_array = np.array(titanic['age'].dropna())  # Eliminar valores NaN
class_array = np.array(titanic['pclass'].dropna())  # Eliminar valores NaN

# Crear el gráfico combinado: violinplot y stripplot
plt.figure(figsize=(10, 6))

# Graficar el violinplot
sns.violinplot(x='pclass', y='age', data=titanic, inner=None, color='skyblue')

# Superponer el stripplot
sns.stripplot(x='pclass', y='age', data=titanic, jitter=True, color='black', alpha=0.5)

# Personalizar el gráfico
plt.title('Distribución de Edades por Clase en el Titanic')
plt.xlabel('Clase')
plt.ylabel('Edad')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
