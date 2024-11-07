palabras = ["manzana", "banana", "cereza", "mango", "melón", "arándano", "mandarina"]

letra_especifica = input("Ingrese una letra específica: ").lower()

contador_palabras = 0

for palabra in palabras:
    if palabra.lower().startswith(letra_especifica):
        contador_palabras += 1

print(f"El número total de palabras que empiezan con '{letra_especifica}' es: {contador_palabras}")