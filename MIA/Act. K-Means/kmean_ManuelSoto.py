import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# Cargar el dataset IRIS
dataset = datasets.load_iris()
data = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# Aplicar K-Means con k=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(data)
labels = kmeans.labels_

# Reducir la dimensionalidad para visualizar los clusters
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data)

# Graficar los clusters
plt.figure(figsize=(8, 6))
plt.scatter(data_pca[:, 0], data_pca[:, 1], c=labels, cmap='viridis', alpha=0.6, edgecolors='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centroides')
plt.title('Clusters obtenidos con K-Means')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend()
plt.show()

# Evaluar la calidad del clustering usando Silhouette Score
silhouette_avg = silhouette_score(data, labels)
print(f"Silhouette Score: {silhouette_avg:.2f}")

# ¿Cómo se distribuyen los grupos en la gráfica?
# En la gráfica, los datos se agrupan en tres clusters bien diferenciados.
# Se observa que los centroides están ubicados en el centro de cada grupo.
# Algunos puntos pueden estar cercanos a los límites entre clusters, lo que indica cierta superposición entre ellos.
