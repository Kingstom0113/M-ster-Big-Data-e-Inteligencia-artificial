import pandas as pd
import csv

def cargar_cotizaciones(archivo):
    """
    Carga un archivo CSV de cotizaciones y devuelve un diccionario con los datos por columna.

    Args:
        archivo (str): Nombre del archivo CSV.

    Returns:
        dict: Diccionario con los datos por columna.
    """

    df = pd.read_csv(archivo)
    return df.to_dict('list')

def crear_estadisticas(datos, archivo_salida):
    """
    Crea un archivo CSV con las estadísticas (mínimo, máximo y media) de cada columna.

    Args:
        datos (dict): Diccionario con los datos por columna.
        archivo_salida (str): Nombre del archivo CSV de salida.
    """

    estadisticas = {}
    for columna, valores in datos.items():
        estadisticas[columna] = {
            'minimo': min(valores),
            'maximo': max(valores),
            'media': sum(valores) / len(valores)
        }

    with open(archivo_salida, 'w', newline='') as csvfile:
        fieldnames = ['columna', 'minimo', 'maximo', 'media']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for columna, stats in estadisticas.items():
            writer.writerow({'columna': columna, **stats})

# Ejemplo de uso:
archivo_entrada = 'cotizacion.csv'
archivo_salida = 'estadisticas.csv'

datos = cargar_cotizaciones(archivo_entrada)
crear_estadisticas(datos, archivo_salida)