import matplotlib.pyplot as plt

# Solicitar al usuario el rango de años
inicio = int(input("Ingrese el año inicial: "))
fin = int(input("Ingrese el año final: "))

# Validar que el rango de años sea válido
if inicio > fin:
    print("El año inicial no puede ser mayor que el año final.")
else:
    # Crear una lista para los años
    años = list(range(inicio, fin + 1))

    # Solicitar las ventas para cada año
    ventas = []
    for año in años:
        venta = float(input(f"Ingrese las ventas para el año {año}: "))
        ventas.append(venta)

    # Generar el gráfico de líneas
    plt.plot(años, ventas, marker='o', linestyle='-', color='blue', label='Ventas')

    # Configurar etiquetas y título
    plt.xlabel('Años')
    plt.ylabel('Ventas')
    plt.title('Evolución de las Ventas')

    # Agregar una cuadrícula y leyenda
    plt.grid(True)
    plt.legend()

    # Mostrar el gráfico
    plt.show()
