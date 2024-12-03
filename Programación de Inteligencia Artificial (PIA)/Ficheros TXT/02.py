with open("el_quijote.txt", "r", encoding="utf-8") as file:
    contenido = file.read()

apariciones = contenido.lower().count("CAPÍTULO".lower())

print(f"La palabra 'Capítulo' aparece {apariciones} veces en el documento.")
