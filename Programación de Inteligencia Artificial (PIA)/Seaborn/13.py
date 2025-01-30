import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Crear un DataFrame con distribuciones normales simuladas
np.random.seed(42)  # Para obtener los mismos resultados cada vez

# Generar datos para tres grupos diferentes con distintas medias y desviaciones estándar
group_1 = np.random.normal(loc=0, scale=1, size=1000)  # Media 0, desviación 1
group_2 = np.random.normal(loc=2, scale=1.5, size=1000)  # Media 2, desviación 1.5
group_3 = np.random.normal(loc=-2, scale=0.5, size=1000)  # Media -2, desviación 0.5

# Crear un DataFrame con los datos
data = {
    'Group 1': group_1,
    'Group 2': group_2,
    'Group 3': group_3
}

# Convertir los datos a un formato adecuado para Seaborn (en un solo DataFrame)
import pandas as pd
df = pd.DataFrame(data)

# Graficar los histogramas superpuestos
sns.set(style="whitegrid")

# Crear el gráfico de histogramas superpuestos
plt.figure(figsize=(10, 6))

# Graficar el primer grupo
sns.histplot(df['Group 1'], bins=30, kde=False, color="blue", label="Group 1", alpha=0.5)

# Graficar el segundo grupo
sns.histplot(df['Group 2'], bins=30, kde=False, color="green", label="Group 2", alpha=0.5)

# Graficar el tercer grupo
sns.histplot(df['Group 3'], bins=30, kde=False, color="red", label="Group 3", alpha=0.5)

# Agregar leyenda, etiquetas y título
plt.legend(title="Groups")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogramas Superpuestos de Diferentes Grupos")

# Mostrar el gráfico
plt.tight_layout()
plt.show()
