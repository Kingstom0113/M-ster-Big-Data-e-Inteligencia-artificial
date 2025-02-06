import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset fmri
fmri = sns.load_dataset('fmri')

# Convertir las columnas 'timepoint' y 'signal' a arrays de NumPy
fmri['time'] = np.array(fmri['timepoint'])
fmri['response'] = np.array(fmri['signal'])

# Crear la cuadrícula de FacetGrid
g = sns.FacetGrid(fmri, col="subject", col_wrap=4, height=3)

# Crear los gráficos de KDE para cada sujeto
g.map(sns.kdeplot, "time", "response")

# Personalizar el diseño de la cuadrícula
g.set_axis_labels("Tiempo", "Respuesta")
g.set_titles("Sujeto {col_name}")

# Mostrar los gráficos
plt.show()

