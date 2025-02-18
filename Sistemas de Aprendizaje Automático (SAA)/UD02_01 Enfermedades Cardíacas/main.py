import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Cargar el dataset
df = pd.read_csv("Dataset_Enfermedades.csv")

# Exploración de datos
print(df.info())
print(df.describe())
print(df.isnull().sum())  # Verificar valores nulos

# Visualización de datos
sns.pairplot(df, hue='enfermedad_cardiaca')
plt.show()

# Separar variables predictoras y variable objetivo
X = df.drop(columns=['enfermedad_cardiaca'])
y = df['enfermedad_cardiaca']

# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Estandarización de los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Modelos de clasificación
models = {
    "Regresión Logística": LogisticRegression(),
    "Árbol de Decisión": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "SVM": SVC(probability=True)
}

# Entrenamiento y evaluación
def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
    
    print(f"\nModelo: {model.__class__.__name__}")
    print(classification_report(y_test, y_pred))
    print("Matriz de confusión:\n", confusion_matrix(y_test, y_pred))
    if y_prob is not None:
        print("AUC-ROC Score:", roc_auc_score(y_test, y_prob))

for name, model in models.items():
    evaluate_model(model, X_train, X_test, y_train, y_test)
