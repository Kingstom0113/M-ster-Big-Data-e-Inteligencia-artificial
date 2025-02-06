import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset tips
tips = sns.load_dataset("tips")

# Convertir columnas a arrays de NumPy
total_bill = np.array(tips['total_bill'])
tip = np.array(tips['tip'])

# Aplicar un estilo personalizado
sns.set_style("ticks")
plt.figure(figsize=(8, 6))

# Crear el gráfico KDE con rug plot
sns.kdeplot(total_bill, fill=True, bw_adjust=0.8, color="green", linewidth=2)
sns.rugplot(total_bill, color="red", height=0.1)

# Agregar etiquetas y título
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.title("Distribución de Total Bill con KDE y Rug Plot")

# Mostrar el gráfico
plt.show()