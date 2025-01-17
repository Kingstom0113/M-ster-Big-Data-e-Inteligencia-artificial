class Usuario:
    def __init__(self, id_usuario, nombre, apellidos, dni, correo_e, tlfno, direccion, edad):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.correo_e = correo_e
        self.tlfno = tlfno
        self.direccion = direccion
        self.edad = edad

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "dni": self.dni,
            "correo_e": self.correo_e,
            "tlfno": self.tlfno,
            "direccion": self.direccion,
            "edad": self.edad
        }
