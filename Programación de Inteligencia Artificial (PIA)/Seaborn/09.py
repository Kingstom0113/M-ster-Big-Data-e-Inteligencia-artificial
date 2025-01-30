import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Crear un DataFrame simulado con datos de ventas diarias
np.random.seed(0)  # Semilla para reproducibilidad

# Generar fechas (un año de datos diarios)
dates = pd.date_range('2023-01-01', periods=365, freq='D')

# Simular datos de ventas con una tendencia estacional
seasonality = np.sin(np.linspace(0, 4 * np.pi, 365))  # Sine wave para simular estacionalidad
trend = np.linspace(0, 20, 365)  # Tendencia lineal
noise = np.random.normal(0, 3, 365)  # Ruido aleatorio

# Las ventas son la suma de la tendencia, la estacionalidad y el ruido
sales = trend + seasonality * 10 + noise

# Crear el DataFrame
df = pd.DataFrame({
    'date': dates,
    'sales': sales
})

# Convertir los datos a arrays
df['date'] = np.array(df['date'])
df['sales'] = np.array(df['sales'])

# Crear el gráfico de líneas con Seaborn
sns.set(style="whitegrid")  # Estilo de fondo con cuadrícula

# Gráfico de líneas con la serie de tiempo de ventas
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='sales', data=df, label='Ventas Diarias', color='blue')

# Aplicar un suavizado a la serie de tiempo usando un 'Lowess' (suavizado local)
sns.lineplot(x='date', y='sales', data=df, label='Suavizado', color='red', 
             estimator='mean', ci=None)

# Personalizar las líneas con estilos diferenciados
plt.title('Ventas Diarias con Suavizado Estacional', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Ventas', fontsize=12)
plt.xticks(rotation=45)
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
