numeros = [1, 3, 5, 7, 9, 11, 13, 15]

numero_a_buscar = int(input("Ingrese un número a buscar: "))

encontrado = False

for numero in numeros:
    if numero == numero_a_buscar:
        encontrado = True
        print(f"El número {numero_a_buscar} se encuentra en la lista.")

# Este bloque else se ejecuta si el bucle for termina sin encontrar el número
if not encontrado:
    print(f"El número {numero_a_buscar} no se encuentra en la lista.")