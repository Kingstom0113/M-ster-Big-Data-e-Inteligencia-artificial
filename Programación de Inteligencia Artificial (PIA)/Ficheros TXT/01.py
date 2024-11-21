with open("el_quijote.txt", "r", encoding="utf-8") as file:
    contenido = file.read()


palabras = contenido.split()
numero_de_palabras = len(palabras)

print(f"El número total de palabras en el fichero es: {numero_de_palabras}")
