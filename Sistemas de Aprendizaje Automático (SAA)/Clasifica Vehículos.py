import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Cargar datos
df = pd.read_csv('Dataset_Vehiculos.csv')

# Mostrar las primeras filas
print(df.head())

# Información general del DataFrame
df.info()

# Estadísticas descriptivas
print(df.describe())

# Manejo de valores nulos (eliminación de filas con valores nulos)
df.dropna(inplace=True)

# Normalización de datos numéricos
scaler = StandardScaler()
df[['Year', 'Mileage', 'EngineSize', 'Horsepower']] = scaler.fit_transform(df[['Year', 'Mileage', 'EngineSize', 'Horsepower']])

# Separación de variables predictoras y variable objetivo
X = df.drop(columns=['ID', 'Price'])
y = df['Price']

# División en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Aplicar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones con los datos de prueba
y_pred = model.predict(X_test)

# Evaluación del modelo
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Imprimir resultados de la evaluación
print("Resultados de Regresión Lineal:")
print(f"MSE: {mse}")
print(f"MAE: {mae}")
print(f"R²: {r2}")

# Graficar los resultados
plt.figure(figsize=(10, 6))

# Gráfico de dispersión de los datos reales vs. predicciones
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
plt.xlabel('Valor Real')
plt.ylabel('Valor Predicho')
plt.grid(True)
plt.show()
