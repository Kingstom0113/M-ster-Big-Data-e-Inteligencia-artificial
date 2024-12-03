import pickle
from empleado import Empleado


class Empresa:
    def __init__(self, nombre, tamaño):
        self._nombre = nombre
        self._tamaño = tamaño
        self._empleados = [None] * tamaño  # Lista fija para el tamaño máximo

    def get_nombre(self):
        return self._nombre

    def get_tamaño(self):
        return self._tamaño

    def get_empleado(self, indice):
        if 0 <= indice < self._tamaño:
            return self._empleados[indice]
        raise IndexError("Índice fuera de rango")

    def despide_empleado(self, num_empleado):
        for i, empleado in enumerate(self._empleados):
            if empleado and empleado.get_num_empleado() == num_empleado:
                self._empleados[i] = None
                self._actualizar_archivo()
                print(f"Empleado #{num_empleado} ha sido despedido.")
                return
        print(f"No se encontró al empleado con número {num_empleado}.")

    def nuevo_empleado_directo(self, empleado):
        for i in range(self._tamaño):
            if self._empleados[i] is None:
                self._empleados[i] = empleado
                self._actualizar_archivo()
                return
        print("La empresa ha alcanzado su capacidad máxima de empleados.")

    def nuevo_empleado(self, nombre, sueldo):
        nuevo = Empleado(self, nombre, sueldo)

    def _actualizar_archivo(self):
        # Guardar empleados en el archivo binario
        empleados_a_guardar = [e for e in self._empleados if e is not None]
        with open("MisEmpleados.dat", "wb") as archivo:
            pickle.dump(empleados_a_guardar, archivo)

    def cargar_empleados(self):
        try:
            with open("MisEmpleados.dat", "rb") as archivo:
                empleados_cargados = pickle.load(archivo)
                for empleado in empleados_cargados:
                    self.nuevo_empleado_directo(empleado)
        except FileNotFoundError:
            print("Archivo 'MisEmpleados.dat' no encontrado. Iniciando con una lista vacía.")
