class Prestamo:
    def __init__(self, id_prestamo, id_usuario, id_libro, fecha_inicio, fecha_fin, fecha_devolucion=None):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_devolucion = fecha_devolucion

    def to_dict(self):
        return {
        'id_prestamo': self.id_prestamo,
        'id_usuario': self.id_usuario,
        'id_libro': self.id_libro,
        'fecha_inicio': self.fecha_inicio,
        'fecha_fin': self.fecha_fin,
        'fecha_devolucion': self.fecha_devolucion
    }

