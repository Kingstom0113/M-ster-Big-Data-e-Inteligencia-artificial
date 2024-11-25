import pandas as pd
import re
import matplotlib.pyplot as plt

# 1. Cargar los datos
file_path = 'datosClientes.csv'  # Asegúrate de que el archivo esté en la ruta correcta
df = pd.read_csv(file_path)

# Limpiar nombres de columnas para eliminar espacios adicionales
df.columns = df.columns.str.strip()

# Mostrar los nombres de las columnas para verificar
print(df.columns)

# 2. Funciones para detectar errores

# 2.1 Exactitud
def check_accuracy(df):
    exactitud_errors = df[(df['Nombre'].str.strip() == '') | (df['Dirección'].str.strip() == '')]
    return exactitud_errors

# 2.2 Completitud
def check_completeness(df):
    completitud_errors = df[df[['Nombre', 'Dirección', 'Correo Electrónico']].isnull().any(axis=1)]
    return completitud_errors

# 2.3 Consistencia
def check_consistency(df):
    regex_phone = r'^\+34 \d{9}$'
    consistencia_errors = df[~df['Teléfono'].str.match(regex_phone, na=False)]
    return consistencia_errors

# 2.4 Validez
def check_validity(df):
    regex_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    validez_errors = df[~df['Correo Electrónico'].str.match(regex_email, na=False)]
    return validez_errors

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
    'Exactitud': len(exactitud_errores) * costes['Exactitud'],
    'Completitud': len(completitud_errores) * costes['Completitud'],
    'Consistencia': len(consistencia_errores) * costes['Consistencia'],
    'Validez': len(validez_errores) * costes['Validez'],
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

# 6. Visualización con gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(impacto.keys(), impacto.values(), color='skyblue')
plt.title('Impacto Económico por Métrica de Calidad de Datos')
plt.xlabel('Métricas')
plt.ylabel('Coste (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

