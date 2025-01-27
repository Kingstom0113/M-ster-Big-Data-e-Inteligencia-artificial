import pandas as pd
import matplotlib.pyplot as plt

def graficar_cotizaciones_cierre(fichero):
    """
    Genera un diagrama de líneas con las series temporales de las cotizaciones de cierre
    de cada banco.

    :param fichero: Ruta al fichero CSV que contiene las cotizaciones de los bancos.
    """
    # Cargar el archivo CSV
    try:
        data = pd.read_csv(fichero)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el fichero: {fichero}")

    # Verificar que contenga las columnas necesarias
    columnas_necesarias = {'Empresa', 'Cierre'}
    if not columnas_necesarias.issubset(data.columns):
        raise ValueError(f"El fichero debe contener las columnas: {', '.join(columnas_necesarias)}")

    # Crear un gráfico de líneas para las cotizaciones de cierre de cada banco
    plt.figure(figsize=(10, 6))
    for empresa in data['Empresa'].unique():
        # Filtrar los datos por empresa
        datos_empresa = data[data['Empresa'] == empresa]
        
        # Asegurarse de que los datos están ordenados (opcional si hay una columna de fechas)
        if 'Fecha' in data.columns:
            datos_empresa = datos_empresa.sort_values('Fecha')
        
        # Graficar la serie temporal de cierre
        plt.plot(
            datos_empresa.index,  # Usar el índice si no hay una columna de fechas explícita
            datos_empresa['Cierre'],
            marker='o',
            label=empresa
        )

    # Configurar etiquetas y título
    plt.title("Cotizaciones de Cierre de los Bancos")
    plt.xlabel("Índice o Fecha")
    plt.ylabel("Precio de Cierre")
    plt.legend(title="Banco")
    plt.grid(True)

    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso (asegúrate de que el archivo bancos.csv esté en el mismo directorio o proporciona la ruta completa)
archivo_ejemplo = "bancos.csv"
graficar_cotizaciones_cierre(archivo_ejemplo)
