import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos
file_path = 'datosClientes.csv'
df = pd.read_csv(file_path)

# Limpiar nombres de columnas para eliminar espacios adicionales
df.columns = df.columns.str.strip()

# 2. Funciones para detectar errores

# 2.1 Exactitud
def check_accuracy(df):
    errores = df[(df['Nombre'].isnull()) | (df['Nombre'].str.strip() == '') |
                 (df['Dirección'].isnull()) | (df['Dirección'].str.strip() == '')]
    return len(errores)


# 2.2 Completitud
def check_completeness(df):
    errores = (
        df['Nombre'].isnull() & df['Dirección'].isnull() & df['Correo Electrónico'].isnull()
    )
    return errores.sum() 

# 2.3 Consistencia
def check_consistency(df):
    telefono_regex = r"^\+34 \d{9}$"
    errores = df[~df['Teléfono'].str.match(telefono_regex, na=False)]
    return len(errores)

# 2.4 Validez
def check_validity(df):
    correo_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    errores = df[~df['Correo Electrónico'].str.match(correo_regex, na=False)]
    return len(errores)

# 2.5 Integridad
def check_integrity(df):
    integridad_errors = df[df['Pedido Válido'] != 'Válido']
    return integridad_errors

# 2.6 Actualización
def check_update(df):
    actualizacion_errors = df[df['Última Actualización (días)'] > 15]
    return actualizacion_errors

# 2.7 Accesibilidad
def check_accessibility(df):
    accesibilidad_errors = df[df['Tiempo Acceso (seg)'] > 0.3]
    return accesibilidad_errors

# 3. Detectar errores y calcular el impacto económico
exactitud_errores = check_accuracy(df)
completitud_errores = check_completeness(df)
consistencia_errores = check_consistency(df)
validez_errores = check_validity(df)
integridad_errores = check_integrity(df)
actualizacion_errores = check_update(df)
accesibilidad_errores = check_accessibility(df)

# 4. Costes asociados a cada métrica
costes = {
    'Exactitud': 1000,
    'Completitud': 500,
    'Consistencia': 2000,
    'Validez': 300,
    'Integridad': 1500,
    'Actualización': 1200,
    'Accesibilidad': 1000
}

# Calcular el impacto económico
impacto = {
    'Exactitud': exactitud_errores * costes['Exactitud'],
    'Completitud': completitud_errores * costes['Completitud'],
    'Consistencia': consistencia_errores * costes['Consistencia'],
    'Validez': validez_errores * costes['Validez'],
    'Integridad': len(integridad_errores) * costes['Integridad'],
    'Actualización': len(actualizacion_errores) * costes['Actualización'],
    'Accesibilidad': len(accesibilidad_errores) * costes['Accesibilidad'],
}

# Impacto económico total
impacto_total = sum(impacto.values())
print(f"Impacto Económico Total: {impacto_total} €")

# 5. Mostrar los resultados de impacto por métrica
for metric, value in impacto.items():
    print(f"Impacto de {metric}: {value} €")

# Lista de colores personalizada
colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# 6. Visualización con gráfico de barras
plt.figure(figsize=(10, 6))
bars = plt.bar(impacto.keys(), impacto.values(), color=colores)

# Agregar etiquetas encima de cada barra
for bar in bars:
    altura = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        altura + 5000,
        f"{altura:,.0f}€",                 
        ha='center', va='bottom', fontsize=10, color='black'
    )

# Personalización del gráfico
plt.title('Impacto Económico por Métrica de Calidad de Datos')
plt.xlabel('Métricas')
plt.ylabel('Coste (€)')

# Ajustar los valores del eje Y para intervalos de 100,000€
max_val = max(impacto.values())
y_ticks = range(0, max_val + 100000, 100000)
plt.yticks(y_ticks, [f"{y:,}€" for y in y_ticks])

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
