class Restaurante:
    def __init__(self, nombre, tipo_cocina, menu=None):
        # Atributos del restaurante
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.menu = menu if menu is not None else []  # Si no se pasa un menú, se crea uno vacío
    
    def añadir_plato(self, plato):
        # Método para añadir un plato al menú
        self.menu.append(plato)
        return f"El plato '{plato}' ha sido añadido al menú."
    
    def mostrar_menu(self):
        # Método para mostrar el menú completo
        if self.menu:
            menu_str = "\n".join(self.menu)
            return f"Menú del restaurante {self.nombre}:\n{menu_str}"
        else:
            return f"El menú del restaurante {self.nombre} está vacío."
    
    def tomar_pedido(self, plato):
        # Método para tomar un pedido y mostrar el plato elegido
        if plato in self.menu:
            return f"El cliente ha pedido el plato: {plato}."
        else:
            return f"El plato '{plato}' no está disponible en el menú."

# Ejemplo de uso
restaurante1 = Restaurante("La Bella Italia", "Italiana", ["Pizza", "Pasta", "Lasagna"])
restaurante2 = Restaurante("El Mexicano", "Mexicana")

# Añadir platos al menú
print(restaurante1.añadir_plato("Tiramisu"))  # Añadir un plato a restaurante1
print(restaurante2.añadir_plato("Tacos"))  # Añadir un plato a restaurante2
print(restaurante2.añadir_plato("Burritos"))  # Añadir otro plato a restaurante2

# Mostrar el menú completo
print(restaurante1.mostrar_menu())  # Mostrar menú de restaurante1
print(restaurante2.mostrar_menu())  # Mostrar menú de restaurante2

# Tomar un pedido
print(restaurante1.tomar_pedido("Pasta"))  # Tomar pedido de plato disponible
print(restaurante2.tomar_pedido("Quesadillas"))  # Intentar tomar un pedido de un plato no disponible
