import matplotlib.pyplot as plt

def graficar_notas(notas, color):
    """
    Genera un diagrama de barras con las notas de las asignaturas en el color dado.

    :param notas: Diccionario con las asignaturas como claves y las notas como valores.
    :param color: Cadena que representa el color de las barras.
    """
    # Extraer las asignaturas y las notas
    asignaturas = list(notas.keys())
    valores = list(notas.values())

    # Crear el gráfico de barras
    plt.bar(asignaturas, valores, color=color)

    # Configurar etiquetas y título
    plt.xlabel('Asignaturas')
    plt.ylabel('Notas')
    plt.title('Diagrama de barras de las notas')

    # Ajustar rango de notas (opcional)
    plt.ylim(0, 10)  # Asumiendo que las notas son del 0 al 10

    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
notas_ejemplo = {
    'Matemáticas': 8.5,
    'Física': 7.0,
    'Química': 9.0,
    'Historia': 6.5,
    'Literatura': 8.0
}
color_ejemplo = 'skyblue'

graficar_notas(notas_ejemplo, color_ejemplo)
