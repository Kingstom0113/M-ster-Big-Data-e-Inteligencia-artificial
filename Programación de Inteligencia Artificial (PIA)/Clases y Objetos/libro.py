class Libro:
    def __init__(self, titulo, autor, num_paginas, editorial, año_publicacion):
        # Atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.editorial = editorial
        self.año_publicacion = año_publicacion
    
    def mostrar_informacion(self):
        # Método para mostrar la información del libro
        return (f"Título: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Número de páginas: {self.num_paginas}\n"
                f"Editorial: {self.editorial}\n"
                f"Año de publicación: {self.año_publicacion}")
    
    def es_largo(self):
        # Método para indicar si el libro es largo o corto
        if self.num_paginas > 300:
            return "Este libro es largo."
        else:
            return "Este libro es corto."

# Ejemplo de uso
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417, "Editorial Sudamericana", 1967)
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 96, "Editorial Reynal & Hitchcock", 1943)

# Mostrar información de los libros
print(libro1.mostrar_informacion())
print(libro1.es_largo())
print("\n")
print(libro2.mostrar_informacion())
print(libro2.es_largo())
