import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset exercise
exercise = sns.load_dataset('exercise')

# Ver las primeras filas del dataset y las columnas
print(exercise.head())  # Ver las primeras filas para inspeccionar el dataset
print(exercise.columns)  # Ver las columnas disponibles

# Convertir las columnas 'time' y 'kind' a arrays de NumPy
exercise['time'] = np.array(exercise['time'])  # Convertir 'time' a un array de NumPy
exercise['kind'] = np.array(exercise['kind'])  # Convertir 'kind' a un array de NumPy

# Ajustar el orden de las categorías (orden alfabético o personalizarlo)
order = ['rest', 'walking', 'running', 'swimming', 'cycling']

# Crear un catplot de tipo stripplot
sns.set(style="whitegrid")  # Estilo de fondo con cuadrícula

# Crear el catplot de tipo stripplot
g = sns.catplot(
    x="kind", y="time", data=exercise, kind="strip", 
    jitter=True, dodge=True, height=6, aspect=1.5, 
    order=order,  # Ajustar el orden de las categorías
    width=0.7,  # Ajustar el ancho de los puntos
    color="blue",  # Color de los puntos
)

# Personalizar el gráfico
g.set_axis_labels("Tipo de Ejercicio", "Duración (minutos)")
g.set_titles("Distribución de la Duración por Tipo de Ejercicio")
plt.xticks(rotation=45)  # Girar las etiquetas del eje x para mejor visibilidad

# Mostrar el gráfico
plt.tight_layout()
plt.show()
