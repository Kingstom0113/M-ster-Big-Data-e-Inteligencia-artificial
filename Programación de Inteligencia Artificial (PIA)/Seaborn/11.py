import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset penguins
penguins = sns.load_dataset('penguins')

# Ver las primeras filas del dataset y las columnas
print(penguins.head())  # Ver las primeras filas para inspeccionar el dataset
print(penguins.columns)  # Ver las columnas disponibles

# Convertir las columnas 'flipper_length_mm' y 'body_mass_g' a arrays de NumPy
penguins['flipper_length_mm'] = np.array(penguins['flipper_length_mm'])
penguins['body_mass_g'] = np.array(penguins['body_mass_g'])

# Crear un swarmplot
sns.set(style="whitegrid")  # Estilo de fondo con cuadrícula

# Crear el gráfico swarmplot
g = sns.swarmplot(
    x="species", y="body_mass_g", data=penguins, dodge=True, 
    size=8, color="blue", alpha=0.7
)

# Personalizar el gráfico
g.set_xlabel("Especie")  # Establecer la etiqueta del eje X
g.set_ylabel("Peso Corporal (g)")  # Establecer la etiqueta del eje Y
g.set_title("Relación entre el Tamaño de las Aletas y el Peso Corporal de los Pingüinos")  # Título del gráfico

# Mostrar el gráfico
plt.tight_layout()
plt.show()

