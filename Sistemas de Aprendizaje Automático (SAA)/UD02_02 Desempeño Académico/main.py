import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Cargar el dataset
df = pd.read_csv("Dataset_Academico.csv")

# Verificar valores nulos
df.isnull().sum()

# Codificar variables categóricas
label_encoder = LabelEncoder()
df['rendimiento_academico'] = label_encoder.fit_transform(df['rendimiento_academico'])

# Separar variables predictoras y variable objetivo
X = df.drop(columns=['rendimiento_academico'])
y = df['rendimiento_academico']

# Escalar características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Definir y entrenar modelos
models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM": SVC(kernel='linear', probability=True)
}

# Evaluar modelos
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Modelo: {name}")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(f"Precisión: {acc}\n")
    results[name] = acc

# Comparar resultados
df_results = pd.DataFrame(list(results.items()), columns=['Modelo', 'Precisión'])
print(df_results)
