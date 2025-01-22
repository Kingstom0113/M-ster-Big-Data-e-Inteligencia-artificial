import pandas as pd
import matplotlib.pyplot as plt

def analizar_datos_titanic(fichero):
    """
    Genera diagramas a partir del archivo 'titanic.csv':
    1. Diagrama de Sectores con los fallecidos y supervivientes.
    2. Histograma con las edades.
    3. Diagrama de Barras con el número de personas en cada clase.
    4. Diagrama de Barras con el número de personas fallecidas y supervivientes en cada clase.
    5. Diagrama de Barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.

    :param fichero: Ruta al archivo CSV con los datos del Titanic.
    """
    # Cargar el archivo CSV
    try:
        titanic = pd.read_csv(fichero)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el fichero: {fichero}")

    # 1. Diagrama de Sectores con los fallecidos y supervivientes
    plt.figure(figsize=(6, 6))
    titanic['Survived'].value_counts().plot.pie(
        autopct='%1.1f%%',
        labels=['Fallecidos', 'Supervivientes'],
        startangle=90,
        colors=['red', 'green']
    )
    plt.title("Fallecidos y Supervivientes")
    plt.ylabel("")  # Eliminar etiqueta del eje Y
    plt.show()

    # 2. Histograma con las edades
    plt.figure(figsize=(8, 6))
    titanic['Age'].dropna().plot.hist(
        bins=20,
        color='blue',
        edgecolor='black',
        alpha=0.7
    )
    plt.title("Distribución de Edades")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.grid(axis='y')
    plt.show()

    # 3. Diagrama de Barras con el número de personas en cada clase
    plt.figure(figsize=(8, 6))
    titanic['Pclass'].value_counts().sort_index().plot.bar(
        color='orange',
        edgecolor='black'
    )
    plt.title("Número de Personas en Cada Clase")
    plt.xlabel("Clase")
    plt.ylabel("Cantidad")
    plt.grid(axis='y')
    plt.show()

    # 4. Diagrama de Barras con el número de personas fallecidas y supervivientes en cada clase
    plt.figure(figsize=(8, 6))
    pd.crosstab(titanic['Pclass'], titanic['Survived']).plot.bar(
        stacked=False,
        color=['red', 'green'],
        edgecolor='black'
    )
    plt.title("Fallecidos y Supervivientes en Cada Clase")
    plt.xlabel("Clase")
    plt.ylabel("Cantidad")
    plt.legend(['Fallecidos', 'Supervivientes'])
    plt.grid(axis='y')
    plt.show()

    # 5. Diagrama de Barras con el número de personas fallecidas y supervivientes acumuladas en cada clase
    plt.figure(figsize=(8, 6))
    pd.crosstab(titanic['Pclass'], titanic['Survived']).plot.bar(
        stacked=True,
        color=['red', 'green'],
        edgecolor='black'
    )
    plt.title("Fallecidos y Supervivientes Acumulados en Cada Clase")
    plt.xlabel("Clase")
    plt.ylabel("Cantidad")
    plt.legend(['Fallecidos', 'Supervivientes'])
    plt.grid(axis='y')
    plt.show()

# Ejemplo de uso (asegúrate de que el archivo titanic.csv esté en el mismo directorio o proporciona la ruta completa)
archivo_titanic = "titanic.csv"
analizar_datos_titanic(archivo_titanic)
