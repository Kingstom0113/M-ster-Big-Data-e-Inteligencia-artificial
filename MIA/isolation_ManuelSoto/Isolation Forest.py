import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Generar datos simulados de transacciones bancarias
np.random.seed(42)
n_samples = 1000
n_anomalies = 50

# Datos normales
amounts = np.random.normal(loc=100, scale=20, size=n_samples)
transactions = pd.DataFrame({'amount': amounts})

# Introducir anomalías
anomaly_indices = np.random.choice(n_samples, n_anomalies, replace=False)
transactions.loc[anomaly_indices, 'amount'] *= np.random.uniform(2, 6, size=n_anomalies)

# Escalar los datos
scaler = StandardScaler()
transactions_scaled = scaler.fit_transform(transactions)

# Aplicar Isolation Forest
model = IsolationForest(contamination=0.05, random_state=42)
transactions['anomaly_score'] = model.fit_predict(transactions_scaled)
transactions['is_anomaly'] = transactions['anomaly_score'] == -1

# Visualizar resultados
plt.figure(figsize=(10, 6))
plt.hist(transactions['amount'], bins=50, alpha=0.75, label='Normal Transactions')
plt.hist(transactions.loc[transactions['is_anomaly'], 'amount'], bins=50, color='red', alpha=0.75, label='Anomalies')
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.title('Distribution of Transaction Amounts with Anomalies')
plt.legend()
plt.show()

# Guardar dataset generado
transactions.to_csv("transactions.csv", index=False)

# Respuesta en comentario de código:
# El umbral de detección varía con el hiperparámetro 'contamination', que define la proporción de anomalías esperadas.
# Si 'contamination' es alto, se detectan más anomalías (pero con mayor probabilidad de falsos positivos).
# Si es bajo, se detectan menos anomalías, pero con menor probabilidad de falsos positivos.
# Otros hiperparámetros como 'n_estimators' (número de árboles) afectan la precisión del modelo, pero en menor medida al umbral de detección.
