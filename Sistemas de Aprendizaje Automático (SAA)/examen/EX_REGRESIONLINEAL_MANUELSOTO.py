import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import make_regression

# Genero los datos sintéticos
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)

# Convierto a DataFrame para mayor claridad
df = pd.DataFrame({'Superficie': X.flatten(), 'Precio': y})

# Divido en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creo y entreno el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Hago predicciones
y_pred = modelo.predict(X_test)

# Evaluo el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Error Cuadrático Medio (MSE): {mse:.2f}')
print(f'Coeficiente de Determinación (R²): {r2:.2f}')

# Visualización de los datos y la regresión
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regresión Lineal')
plt.xlabel('Superficie')
plt.ylabel('Precio')
plt.title('Regresión Lineal: Precio vs Superficie')
plt.legend()
plt.show()

# Posibles mejoras:
# - Agregar más datos para mejorar la representatividad.
# - Incluir más variables predictoras (número de habitaciones, ubicación, etc.).
# - Aplicar transformación a los datos si hay relaciones no lineales.
# - Probar modelos más complejos como regresión polinómica o redes neuronales.
