import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# ----------------------------
# 1. Carga y Exploración de Datos
# ----------------------------

# Descargamos el dataset MNIST
print("Descargando el dataset MNIST...")
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist.data, mnist.target.astype(int)  # Convertimos las etiquetas a enteros
print("Dataset cargado con éxito.\n")

# Dividimos los datos en 80% entrenamiento y 20% prueba
print("Dividiendo el dataset en entrenamiento (80%) y prueba (20%)...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("División completada.\n")

# Normalizamos los datos para mejorar el rendimiento del modelo
print("Normalizando los datos...")
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print("Normalización completada.\n")

# ----------------------------
# 2. Entrenamiento del Modelo con k=3
# ----------------------------

print("Entrenando el modelo KNN con k=3...")
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
print("Modelo entrenado.\n")

# Realizamos predicciones en el conjunto de prueba
print("Realizando predicciones...")
y_pred = knn.predict(X_test)
print("Predicciones completadas.\n")

# ----------------------------
# 3. Evaluación del Modelo
# ----------------------------

print("========== REPORTE DE CLASIFICACIÓN ==========")
print(classification_report(y_test, y_pred))
print("=============================================\n")

print("========== MATRIZ DE CONFUSIÓN ==========")
print(confusion_matrix(y_test, y_pred))
print("=========================================\n")

# ----------------------------
# 4. Experimentación con Diferentes Valores de K
# ----------------------------

k_values = [1, 3, 5, 7, 9]
accuracies = []

print("Probando diferentes valores de k...")
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    acc = knn.score(X_test, y_test)
    accuracies.append(acc)
    print(f'Precisión con k={k}: {acc:.4f}')

# Graficamos la relación entre k y la precisión
plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracies, marker='o', linestyle='-', color='b')
plt.xlabel('Número de Vecinos (k)')
plt.ylabel('Precisión')
plt.title('Precisión del Modelo KNN en función de k')
plt.grid()
plt.show()

print("Proceso completado. ¡Análisis finalizado!")
