from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

# Cargo el conjunto de datos Iris
datos = load_iris()
X, y = datos.data, datos.target

# Divido los datos en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizo las características
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Implemento el modelo KNN con k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Realizo predicciones
y_pred = knn.predict(X_test)

# Evaluo la precisión
precision = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {precision:.2f}')

# Muestro matriz de confusión
matriz_confusion = confusion_matrix(y_test, y_pred)
print('Matriz de Confusión:')
print(matriz_confusion)

# Explicación sobre el valor de k
def explicar_k(ks):
    """Evalúa el modelo para diferentes valores de k y muestra la precisión."""
    for k in ks:
        modelo = KNeighborsClassifier(n_neighbors=k)
        modelo.fit(X_train, y_train)
        y_pred_k = modelo.predict(X_test)
        precision_k = accuracy_score(y_test, y_pred_k)
        print(f'Para k={k}, la precisión es: {precision_k:.2f}')

# Pruebo diferentes valores de k
explicar_k([1, 3, 5, 7, 9])
