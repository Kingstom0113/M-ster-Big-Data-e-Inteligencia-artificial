import pandas as pd
import matplotlib.pyplot as plt

def graficar_ingresos_gastos(dataframe):
    """
    Genera un diagrama de líneas con los ingresos y gastos de una empresa por meses.

    :param dataframe: DataFrame de Pandas con dos columnas: 'Ingresos' y 'Gastos', 
                      y los meses como índice.
    """
    # Verificar que el DataFrame contenga las columnas necesarias
    if not {'Ingresos', 'Gastos'}.issubset(dataframe.columns):
        raise ValueError("El DataFrame debe contener las columnas 'Ingresos' y 'Gastos'.")

    # Crear el diagrama de líneas
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe.index, dataframe['Ingresos'], marker='o', linestyle='-', color='green', label='Ingresos')
    plt.plot(dataframe.index, dataframe['Gastos'], marker='o', linestyle='-', color='red', label='Gastos')

    # Configurar etiquetas y título
    plt.title("Evolución de Ingresos y Gastos")
    plt.xlabel("Meses")
    plt.ylabel("Cantidad (en unidades monetarias)")
    plt.ylim(0)  # El eje Y comienza en 0

    # Agregar una leyenda y cuadrícula
    plt.legend()
    plt.grid(True)

    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
datos_ejemplo = pd.DataFrame({
    'Ingresos': [5000, 7000, 8000, 7500, 9500, 10000, 8500, 11000, 12000, 10500, 11500, 13000],
    'Gastos': [4000, 5000, 6000, 5500, 7000, 8000, 6500, 9000, 8500, 9000, 9500, 10000]
}, index=[
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 
    'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
])

graficar_ingresos_gastos(datos_ejemplo)
