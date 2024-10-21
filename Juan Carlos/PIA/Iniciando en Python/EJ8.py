# 1. Crear el set 'frutas' con los valores dados
frutas = {"manzana", "banana", "naranja", "uva"}

# 2. Agregar una nueva fruta "pera" al set
frutas.add("pera")

# 3. Intentar agregar la fruta "banana" nuevamente al set
frutas.add("banana")  # No pasará nada, ya que "banana" ya está en el set

# 4. Eliminar la fruta "naranja" del set
frutas.remove("naranja")

# 5. Imprimir todos los elementos del set
print("Elementos del set:", frutas)
