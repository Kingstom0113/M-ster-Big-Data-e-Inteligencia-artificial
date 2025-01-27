import pandas as pd
import matplotlib.pyplot as plt

def graficar_evolucion_ventas(ventas, tipo_grafico):
    """
    Genera un gráfico del tipo especificado con la evolución de las ventas por años.

    :param ventas: Serie de Pandas con el número de ventas por años.
    :param tipo_grafico: Tipo de gráfico a generar ('líneas', 'barras', 'sectores', 'áreas').
    """
    plt.figure(figsize=(8, 6))  # Configurar el tamaño de la figura
    titulo = "Evolución del Número de Ventas"

    if tipo_grafico == "líneas":
        plt.plot(ventas.index, ventas.values, marker='o', linestyle='-', color='blue', label='Ventas')
        plt.title(titulo)
        plt.xlabel("Años")
        plt.ylabel("Número de Ventas")
        plt.legend()
        plt.grid(True)

    elif tipo_grafico == "barras":
        plt.bar(ventas.index, ventas.values, color='orange', label='Ventas')
        plt.title(titulo)
        plt.xlabel("Años")
        plt.ylabel("Número de Ventas")
        plt.legend()
        plt.grid(axis='y')

    elif tipo_grafico == "sectores":
        plt.pie(ventas.values, labels=ventas.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        plt.title(titulo)

    elif tipo_grafico == "áreas":
        plt.fill_between(ventas.index, ventas.values, color='green', alpha=0.4, label='Ventas')
        plt.plot(ventas.index, ventas.values, marker='o', color='green')
        plt.title(titulo)
        plt.xlabel("Años")
        plt.ylabel("Número de Ventas")
        plt.legend()
        plt.grid(True)

    else:
        raise ValueError("El tipo de gráfico debe ser 'líneas', 'barras', 'sectores' o 'áreas'.")

    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
ventas_ejemplo = pd.Series(
    [500, 600, 550, 700, 750],
    index=[2018, 2019, 2020, 2021, 2022]
)

# Generar gráficos de ejemplo
graficar_evolucion_ventas(ventas_ejemplo, "líneas")
graficar_evolucion_ventas(ventas_ejemplo, "barras")
graficar_evolucion_ventas(ventas_ejemplo, "sectores")
graficar_evolucion_ventas(ventas_ejemplo, "áreas")
