import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline

# 1. Carga y Exploración de Datos
# Descargamos el dataset de viviendas de California
dataset = fetch_california_housing()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['PRICE'] = dataset.target

print("\n📊 Primeras filas del dataset:")
print(df.head())

# 2. Preprocesamiento de Datos
# Seleccionamos características relevantes
X = df[['MedInc', 'AveRooms', 'HouseAge', 'AveOccup']]
y = df['PRICE']

# Normalización de los datos para mejorar el rendimiento del modelo
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividimos los datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 3. Construcción del Modelo con características polinómicas
print("\n🔍 Entrenando modelo de regresión polinómica...")
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Creamos y entrenamos el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train_poly, y_train)
y_pred = model.predict(X_test_poly)

# 4. Evaluación del Modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📈 Resultados de la regresión polinómica:")
print(f'➡️ Error Cuadrático Medio (MSE): {mse:.2f}')
print(f'➡️ Coeficiente de Determinación (R²): {r2:.2f}')

# Visualización de resultados
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Regresión Lineal Polinómica: Predicciones vs Valores Reales")
plt.show()

# 5. Análisis y Mejoras
print("\n⚖️ Comparando con otros modelos...")

# Comparación con Regresión Ridge
ridge = Ridge(alpha=1.0)
ridge.fit(X_train_poly, y_train)
y_pred_ridge = ridge.predict(X_test_poly)

# Comparación con Regresión Lasso
lasso = Lasso(alpha=0.1)
lasso.fit(X_train_poly, y_train)
y_pred_lasso = lasso.predict(X_test_poly)

# Métricas de Ridge y Lasso
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
r2_ridge = r2_score(y_test, y_pred_ridge)

mse_lasso = mean_squared_error(y_test, y_pred_lasso)
r2_lasso = r2_score(y_test, y_pred_lasso)

print("\n📊 Comparación de Modelos:")
print(f'🔹 Ridge - MSE: {mse_ridge:.2f}, R²: {r2_ridge:.2f}')
print(f'🔹 Lasso - MSE: {mse_lasso:.2f}, R²: {r2_lasso:.2f}')

print("\n✅ Análisis final: Ridge parece ser una mejor opción que Lasso en este caso.")
