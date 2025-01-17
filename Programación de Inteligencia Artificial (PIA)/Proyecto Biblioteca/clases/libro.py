class Libro:
    def __init__(self, id_libro, titulo, autor, anyo, n_pags, genero, editorial, estado, disponible):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo
        self.n_pags = n_pags
        self.genero = genero
        self.editorial = editorial
        self.estado = estado
        self.disponible = disponible

    def to_dict(self):
        return {
            "id_libro": self.id_libro,
            "titulo": self.titulo,
            "autor": self.autor,
            "anyo": self.anyo,
            "n_pags": self.n_pags,
            "genero": self.genero,
            "editorial": self.editorial,
            "estado": self.estado,
            "disponible": self.disponible
        }
