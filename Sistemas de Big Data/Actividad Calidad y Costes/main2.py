import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Cargar los datos
df = pd.read_csv("datosClientes.csv")

# Funciones de validación
def validar_telefono(telefono):
    return telefono.startswith("+34") and telefono.isdigit()

def validar_email(email):
    # Utilizar una expresión regular más robusta
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def calcular_dias_desde_ultima_actualizacion(fecha_actualizacion):
    fecha_actualizacion = pd.to_datetime(fecha_actualizacion)
    hoy = datetime.date.today()
    return (hoy - fecha_actualizacion.date()).days

# Análisis de métricas y cálculo de costos
def analizar_metricas(df):
    # Exactitud
    errores_exactitud = df[(df['Nombre'].isnull()) | (df['Dirección'].isnull())].shape[0]
    coste_exactitud = errores_exactitud * 1000

    # Completitud (para todos los campos críticos)
    errores_completitud = df.isnull().sum().sum()
    coste_completitud = errores_completitud * 500

    # Consistencia
    errores_consistencia = df[~df['Teléfono'].apply(validar_telefono)].shape[0]
    coste_consistencia = errores_consistencia * 2000

    # Validez
    errores_validez = df[~df['Correo Electrónico'].apply(validar_email)].shape[0]
    coste_validez = errores_validez * 300

    # Integridad
    errores_integridad = df[df['Pedido Válido'] == 'Inválido'].shape[0]
    coste_integridad = errores_integridad * 1500

    # Actualización
    df['Dias desde última actualización'] = df['Última Actualización'].apply(calcular_dias_desde_ultima_actualizacion)
    errores_actualizacion = df[df['Dias desde última actualización'] > 15].shape[0]
    coste_actualizacion = errores_actualizacion * 1200

    # Accesibilidad
    errores_accesibilidad = df[df['Tiempo Acceso'] > 0.3].shape[0]
    coste_accesibilidad = errores_accesibilidad * 1000

    # Crear un DataFrame para los resultados
    resultados = pd.DataFrame({'Métrica': ['Exactitud', 'Completitud', 'Consistencia', 'Validez', 'Integridad', 'Actualización', 'Accesibilidad'],
                               'Errores': [errores_exactitud, errores_completitud, errores_consistencia, errores_validez, errores_integridad, errores_actualizacion, errores_accesibilidad],
                               'Coste': [coste_exactitud, coste_completitud, coste_consistencia, coste_validez, coste_integridad, coste_actualizacion, coste_accesibilidad]})
    return resultados

# Visualización
def visualizar_resultados(resultados):
    plt.bar(resultados['Métrica'], resultados['Coste'])
    plt.xlabel('Métrica')
    plt.ylabel('Coste (€)')
    plt.title('Impacto Económico por Métrica de Calidad')
    plt.xticks(rotation=45)
    plt.show()

# Ejecutar el análisis
resultados = analizar_metricas(df)
visualizar_resultados(resultados)