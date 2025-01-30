import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

# Simulación de un DataFrame con resultados de clasificación
# En este caso, 1 representa una clase positiva y 0 representa una clase negativa.
y_true = np.array([0, 1, 0, 1, 1, 0, 1, 1, 0, 0])  # Etiquetas reales
y_pred = np.array([0, 0, 0, 1, 1, 0, 1, 0, 0, 1])  # Etiquetas predichas

# Generar la matriz de confusión
cm = confusion_matrix(y_true, y_pred)

# Convertir la matriz de confusión a un DataFrame de Pandas para mayor facilidad de manejo
cm_df = pd.DataFrame(cm, index=["Clase 0", "Clase 1"], columns=["Predicción 0", "Predicción 1"])

# Crear el mapa de calor
plt.figure(figsize=(8, 6))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues', cbar=True, annot_kws={"size": 16}, linewidths=0.5)

# Personalizar el gráfico
plt.title("Matriz de Confusión con Mapa de Calor", fontsize=16)
plt.xlabel("Predicción", fontsize=14)
plt.ylabel("Real", fontsize=14)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
