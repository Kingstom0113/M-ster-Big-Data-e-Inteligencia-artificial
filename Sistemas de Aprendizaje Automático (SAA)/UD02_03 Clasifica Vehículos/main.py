# Importar las librerías necesarias
import pandas as pd
import numpy as np  # Importamos numpy para usar log
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Cargar el dataset
df = pd.read_csv('Dataset_Vehiculos.csv')

# Mostrar las primeras filas del dataframe
print(df.head())

# Exploración de datos
# Estadísticas descriptivas
print(df.describe())

# Visualización de la distribución de las variables
sns.pairplot(df)
plt.show()

# Correlación entre las variables
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.show()

# Preparación de los datos
# Codificación One-Hot para las variables categóricas 'FuelType' y 'Transmission'
df = pd.get_dummies(df, columns=['FuelType', 'Transmission'], drop_first=True)

# División en características (X) y variable objetivo (y)
X = df.drop(columns=['ID', 'Price'])
y = df['Price']

# Aplicar una transformación logarítmica a la variable 'Price' (solo si tiene una distribución sesgada)
y = y.apply(lambda x: x if x <= 0 else np.log(x))

# División en conjuntos de entrenamiento y prueba (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalización de las variables numéricas
numerical_columns = ['Year', 'Mileage', 'EngineSize', 'Horsepower']
scaler = StandardScaler()
X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])

# Implementación de los algoritmos de regresión
# 1. Regresión Lineal
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)

# 2. Regresión Polinómica
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X_train)
poly_model = LinearRegression()
poly_model.fit(X_poly, y_train)
X_test_poly = poly.transform(X_test)
poly_predictions = poly_model.predict(X_test_poly)

# 3. Regresión Ridge
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)
ridge_predictions = ridge_model.predict(X_test)

# 4. Regresión Lasso
lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X_train, y_train)
lasso_predictions = lasso_model.predict(X_test)

# Métricas de evaluación
def evaluate_model(predictions, y_test):
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return mse, mae, r2

# Evaluar los modelos
lr_mse, lr_mae, lr_r2 = evaluate_model(lr_predictions, y_test)
poly_mse, poly_mae, poly_r2 = evaluate_model(poly_predictions, y_test)
ridge_mse, ridge_mae, ridge_r2 = evaluate_model(ridge_predictions, y_test)
lasso_mse, lasso_mae, lasso_r2 = evaluate_model(lasso_predictions, y_test)

# Mostrar los resultados
print(f"\nRegresión Lineal: MSE={lr_mse}, MAE={lr_mae}, R²={lr_r2}")
print(f"Regresión Polinómica: MSE={poly_mse}, MAE={poly_mae}, R²={poly_r2}")
print(f"Regresión Ridge: MSE={ridge_mse}, MAE={ridge_mae}, R²={ridge_r2}")
print(f"Regresión Lasso: MSE={lasso_mse}, MAE={lasso_mae}, R²={lasso_r2}")

# Comparación de los resultados de cada modelo
best_model = None
best_r2 = max(lr_r2, poly_r2, ridge_r2, lasso_r2)

if best_r2 == lr_r2:
    best_model = 'Regresión Lineal'
elif best_r2 == poly_r2:
    best_model = 'Regresión Polinómica'
elif best_r2 == ridge_r2:
    best_model = 'Regresión Ridge'
else:
    best_model = 'Regresión Lasso'

print(f"\nEl mejor modelo es: {best_model} con un R² de {best_r2}")


