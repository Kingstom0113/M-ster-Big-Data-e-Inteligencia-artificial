from empresa import Empresa


def main():
    # Crear la empresa
    empresa = Empresa("MiEmpresa", 10)

    # Cargar empleados iniciales desde el archivo
    empresa.cargar_empleados()

    # Añadir dos empleados nuevos
    empresa.nuevo_empleado("Juan Pérez", 50000)
    empresa.nuevo_empleado("Ana López", 60000)

    # Dar de baja a un empleado
    empleado_a_despedir = empresa.get_empleado(0)
    if empleado_a_despedir:
        empleado_a_despedir.despedir(empresa)

    # Mostrar todos los empleados actuales
    print("\nEmpleados actuales:")
    for emp in empresa._empleados:
        if emp is not None:
            print(emp)


if __name__ == "__main__":
    main()
