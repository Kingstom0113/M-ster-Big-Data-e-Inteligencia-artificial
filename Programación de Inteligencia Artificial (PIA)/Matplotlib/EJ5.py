import pandas as pd
import matplotlib.pyplot as plt

def guardar_diagrama_sectores(ventas, titulo):
    """
    Crea un diagrama de sectores con las ventas y lo guarda como un archivo PNG.

    :param ventas: Serie de Pandas con el número de ventas por mes.
    :param titulo: Título del diagrama y nombre del archivo PNG.
    """
    # Crear el diagrama de sectores
    plt.figure(figsize=(6, 6))  # Establecer el tamaño de la figura
    plt.pie(
        ventas, 
        labels=ventas.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=plt.cm.Paired.colors
    )
    plt.title(titulo)

    # Guardar el gráfico como archivo PNG
    nombre_archivo = f"{titulo}.png"
    plt.savefig(nombre_archivo, format='png', dpi=300)

    # Cerrar la figura para liberar memoria
    plt.close()
    print(f"Diagrama guardado como '{nombre_archivo}'")

# Ejemplo de uso
ventas_ejemplo = pd.Series(
    [150, 200, 250],
    index=["Enero", "Febrero", "Marzo"]
)
titulo_ejemplo = "Ventas del Primer Trimestre"

guardar_diagrama_sectores(ventas_ejemplo, titulo_ejemplo)
