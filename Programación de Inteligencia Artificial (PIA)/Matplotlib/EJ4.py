import pandas as pd
import matplotlib.pyplot as plt

def diagrama_cajas_notas(notas):
    """
    Genera un diagrama de cajas con las notas de los alumnos.

    :param notas: Serie de Pandas con las notas de los alumnos.
    """
    # Crear el diagrama de cajas
    plt.boxplot(notas, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))

    # Configurar título y etiquetas
    plt.title('Distribución de Notas')
    plt.xlabel('Notas')

    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
notas_ejemplo = pd.Series([8.5, 7.0, 9.0, 6.5, 8.0, 5.5, 7.5, 9.5, 6.0, 8.8, 7.3, 8.2])

diagrama_cajas_notas(notas_ejemplo)
