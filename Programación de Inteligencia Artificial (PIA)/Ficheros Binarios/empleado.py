class Empleado:
    _contador_empleado = 1  # Contador estático para números únicos de empleado

    def __init__(self, empresa, nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo
        self._num_empleado = Empleado._contador_empleado
        Empleado._contador_empleado += 1

        # Añadir el empleado a la empresa automáticamente
        empresa.nuevo_empleado_directo(self)

    def get_nombre(self):
        return self._nombre

    def get_sueldo(self):
        return self._sueldo

    def get_num_empleado(self):
        return self._num_empleado

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_sueldo(self, nuevo_sueldo):
        self._sueldo = nuevo_sueldo

    def __str__(self):
        return f"Empleado #{self._num_empleado}: {self._nombre}, Sueldo: {self._sueldo}"

    def aumentar_sueldo(self, porcentaje):
        self._sueldo += self._sueldo * (porcentaje / 100)

    def despedir(self, empresa):
        empresa.despide_empleado(self._num_empleado)
